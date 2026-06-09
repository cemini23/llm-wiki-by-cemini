#!/usr/bin/env python3
"""Texas Hold'em lobby loop for dev.fun (Playground / Tournament seasons).

Uses POST /texas/join (not benchmark/start). Pair with cemini_decide.
"""
from __future__ import annotations

import argparse
import json
import os
import random
import sys
import time
from pathlib import Path
from typing import Any, Optional

from dotenv import load_dotenv

_EXAMPLES = Path(__file__).resolve().parent
if str(_EXAMPLES) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES))

import cemini_decide  # noqa: E402
from agent import _normalize_action_name, _safe_research_context  # noqa: E402
from session_memory import (  # noqa: E402
    exploit_from_memory,
    update_session_memory,
    villain_memory_for_table,
)
from qualification_guard import fetch_qualification_status  # noqa: E402
from blind_pressure import avg_blind_tax_per_hand, hands_to_erosion  # noqa: E402
from pace_control import join_retry_seconds  # noqa: E402
from hl_runtime_config import is_kill_switch_active, kill_switch_status, load_style_overrides  # noqa: E402
from nemesis_seed import seed_nemesis_state  # noqa: E402
from arena_client import (  # noqa: E402
    ArenaClient,
    ArenaError,
    DEFAULT_BASE,
    load_or_register,
    load_state,
    save_state,
)
from output_sanitize import maybe_sanitize_action  # noqa: E402
from playground_timeseries import append_playground_snapshot  # noqa: E402

POLL_INTERVAL = 2.0
POLL_JITTER = 0.5
LOBBY_LOG_INTERVAL_S = 120.0
QUAL_STATUS_INTERVAL_S = 600.0
PAYMENT_CONFIRM_WAIT_S = 5.0
PAYMENT_CONFIRM_ATTEMPTS = 24


def _env_flag(name: str, default: str = "1") -> bool:
    raw = os.environ.get(name, default)
    return raw.strip().lower() not in ("0", "false", "no", "off")


def _ko_survival_max_hands() -> int:
    raw = os.environ.get("CEMINI_KO_SURVIVAL_HANDS", "200")
    try:
        return max(0, int(raw))
    except ValueError:
        return 200


def _ko_survival_min_stack() -> int:
    raw = os.environ.get("CEMINI_KO_SURVIVAL_MIN_STACK", "2000")
    try:
        return max(0, int(raw))
    except ValueError:
        return 2000


def _lobby_role_label(competition_id: str) -> tuple[str, str]:
    """Resolve human label + registry role for logs and timeseries."""
    s1 = os.environ.get("S1_TOURNAMENT_COMP", "").strip()
    s2 = os.environ.get("S2_PLAYGROUND_COMP", "").strip()
    if competition_id and competition_id == s1:
        return "Tournament S1", "s1_tournament"
    if competition_id and competition_id == s2:
        return "Playground S2", "s2_playground"
    label = os.environ.get("CEMINI_LOBBY_LABEL", "").strip().replace("_", " ")
    role = os.environ.get("CEMINI_LOBBY_ROLE", "").strip()
    return label or competition_id, role or "lobby"


def _lobby_log_scope(competition_id: str) -> str:
    label, role = _lobby_role_label(competition_id)
    return f"comp={competition_id} role={role} label={label}"


def _apply_competition_posture(competition_id: str) -> None:
    """Per-comp env — shared .env loses to systemd on some hosts; comp id is source of truth."""
    s1 = os.environ.get("S1_TOURNAMENT_COMP", "").strip()
    s2 = os.environ.get("S2_PLAYGROUND_COMP", "cmq57o53r0bhw18g23qkydb08").strip()
    if competition_id == s2:
        # S2-only volume push — faster joins than default volume (20/45/30).
        os.environ.update({
            "CEMINI_TOURNAMENT_MODE": "0",
            "JACKPOT_ROYAL_ENABLED": "1",
            "JACKPOT_ROYAL_SHOWDOWN": "1",
            "JACKPOT_27_HUNT_ENABLED": "0",
            "CEMINI_PACE_PHASE": "volume",
            "CEMINI_JOIN_RETRY_S": "12",
            "CEMINI_IN_QUEUE_RETRY_S": "25",
            "CEMINI_LOW_STACK_JOIN_RETRY_S": "15",
            "CEMINI_S1B_MIN_STACK_BB": "60",
            "CEMINI_QUAL_CUTOFF_RANK": "20",
            "CEMINI_EVAL_PANEL_GATE": "0",
        })
    elif competition_id == s1 or os.environ.get("CEMINI_TOURNAMENT_MODE", "").strip().lower() in (
        "1", "true", "yes", "on",
    ):
        os.environ.update({
            "CEMINI_TOURNAMENT_MODE": "1",
            "JACKPOT_ROYAL_ENABLED": "0",
            "JACKPOT_ROYAL_SHOWDOWN": "0",
            "JACKPOT_27_HUNT_ENABLED": "0",
            "CEMINI_JOIN_RETRY_S": "12",
            "CEMINI_IN_QUEUE_RETRY_S": "25",
            "CEMINI_LOW_STACK_JOIN_RETRY_S": "15",
        })


def _sync_competition_scope(state: dict, competition_id: str) -> None:
    """Reset per-season counters when the lobby competition changes (board reset)."""
    prev = state.get("lobby_competition_id")
    if prev == competition_id:
        return
    state["lobby_competition_id"] = competition_id
    state["hands_played"] = 0
    state.pop("session_villain_memory", None)
    seed_nemesis_state(state)


def _ko_survival_lane(state: dict, qual_status: dict) -> bool:
    """Hour-one / reset survival — no exploit widening until buffer built."""
    if not _env_flag("CEMINI_KO_SURVIVAL", "1"):
        return False
    hands = int(state.get("hands_played") or 0)
    if hands < _ko_survival_max_hands():
        return True
    chips = qual_status.get("chips")
    if chips is not None and int(chips) < _ko_survival_min_stack():
        return True
    return False


def _arena_error_text(body: Any) -> str:
    """Normalize Arena error bodies (dict JSON or Cloudflare HTML) to text."""
    if isinstance(body, dict):
        for key in ("error", "message", "detail"):
            val = body.get(key)
            if val:
                return str(val)
        return str(body)
    return str(body or "")


def _join(client: ArenaClient, competition_id: str, tx_hash: Optional[str] = None) -> dict:
    body: dict = {"competitionId": competition_id}
    if tx_hash:
        body["txHash"] = tx_hash
    return client.post("/texas/join", body)


def _pay_entry_fee(client: ArenaClient, payment: dict) -> str:
    """Pay competition entry from agent wallet; return txHash."""
    dest = payment.get("to")
    amt = payment.get("amount")
    if not dest or not amt:
        raise ValueError(f"invalid payment requirements: {payment}")
    resp = client.post("/agent/wallet/transfer/native", {
        "chain": payment.get("chain") or "monad",
        "to": dest,
        "amount": str(amt),
    })
    tx_hash = resp.get("txHash")
    if not tx_hash:
        raise ValueError(f"transfer returned no txHash: {resp}")
    return tx_hash


def _join_with_entry_fee(
    client: ArenaClient,
    competition_id: str,
    payment: dict,
    state: Optional[dict] = None,
    save_state_fn=None,
) -> dict:
    """Transfer entry fee, then join with txHash (poll until mined)."""
    tx_hash = _pay_entry_fee(client, payment)
    print(f"[cemini-lobby] entry fee tx={tx_hash}")
    if state is not None:
        state["entry_fee_tx_hash"] = tx_hash
        if save_state_fn:
            save_state_fn(state)
    last_err: Optional[ArenaError] = None
    for attempt in range(1, PAYMENT_CONFIRM_ATTEMPTS + 1):
        time.sleep(PAYMENT_CONFIRM_WAIT_S)
        try:
            return _join(client, competition_id, tx_hash=tx_hash)
        except ArenaError as e:
            last_err = e
            msg = _arena_error_text(e.body)
            if e.status == 400 and "not yet mined" in msg.lower():
                print(f"[cemini-lobby] waiting for tx confirm ({attempt}/{PAYMENT_CONFIRM_ATTEMPTS})")
                continue
            raise
    if last_err:
        raise last_err
    raise RuntimeError("join with payment failed")


def _pending(client: ArenaClient, competition_id: str) -> dict:
    return client.get(f"/texas/pending-actions?competitionId={competition_id}")


def _lobby_status(client: ArenaClient, competition_id: str) -> dict:
    try:
        return client.get(f"/texas/lobby?competitionId={competition_id}")
    except ArenaError:
        return {}


def _log_lobby_queue(client: ArenaClient, competition_id: str) -> None:
    body = _lobby_status(client, competition_id)
    lob = body.get("lobby") if isinstance(body, dict) else None
    if not isinstance(lob, dict):
        return
    pos = lob.get("position")
    total = lob.get("total")
    if pos is not None:
        print(f"[cemini-lobby] queue position {pos}/{total} — waiting for table")


def _rebuy_with_payment(
    client: ArenaClient,
    competition_id: str,
    payment: dict,
) -> dict:
    tx_hash = _pay_entry_fee(client, payment)
    print(f"[cemini-lobby] rebuy tx={tx_hash}")
    last_err: Optional[ArenaError] = None
    for attempt in range(1, PAYMENT_CONFIRM_ATTEMPTS + 1):
        time.sleep(PAYMENT_CONFIRM_WAIT_S)
        try:
            return client.post("/texas/rebuy", {
                "competitionId": competition_id,
                "txHash": tx_hash,
            })
        except ArenaError as e:
            last_err = e
            msg = _arena_error_text(e.body)
            if e.status == 400 and "not yet mined" in msg.lower():
                print(f"[cemini-lobby] rebuy waiting for tx ({attempt}/{PAYMENT_CONFIRM_ATTEMPTS})")
                continue
            raise
    if last_err:
        raise last_err
    raise RuntimeError("rebuy with payment failed")


def _try_rebuy(client: ArenaClient, competition_id: str) -> bool:
    """Rebuy chips when table buy-in exceeds stack. Returns True if rebuy attempted."""
    try:
        resp = client.post("/texas/rebuy", {"competitionId": competition_id})
        print(f"[cemini-lobby] rebuy: {json.dumps(resp, sort_keys=True)[:300]}")
        return True
    except ArenaError as e:
        if e.status != 402:
            print(f"[cemini-lobby] rebuy failed: {e.status} {e.body}", file=sys.stderr)
            return False
        pay = e.body.get("paymentRequirements") or {} if isinstance(e.body, dict) else {}
        try:
            resp = _rebuy_with_payment(client, competition_id, pay)
            print(f"[cemini-lobby] rebuy after pay: {json.dumps(resp, sort_keys=True)[:300]}")
            return True
        except ArenaError as pay_err:
            print(f"[cemini-lobby] rebuy pay failed: {pay_err.status} {pay_err.body}",
                  file=sys.stderr)
            return False
        except Exception as exc:
            print(f"[cemini-lobby] rebuy pay error: {exc}", file=sys.stderr)
            return False


def run_lobby(args: argparse.Namespace) -> int:
    load_dotenv()
    client = ArenaClient(
        os.environ.get("ARENA_API_BASE", DEFAULT_BASE),
        api_key=os.environ.get("ARENA_API_KEY") or None,
    )
    competition_id = (
        args.competition_id or os.environ.get("ARENA_LOBBY_COMPETITION_ID")
        or "cmpr1vesh2it1x69xmtpiaecp"
    )
    dual_comp = (
        getattr(args, "also_competition_id", None)
        or os.environ.get("CEMINI_DUAL_LOBBY_COMP", "")
    ).strip()
    s1_comp = os.environ.get("S1_TOURNAMENT_COMP", "").strip()
    if dual_comp and dual_comp == competition_id:
        dual_comp = ""
    _apply_competition_posture(competition_id)
    if dual_comp:
        print(
            f"[cemini-lobby] dual lobby: primary {_lobby_log_scope(competition_id)} "
            f"+ secondary {_lobby_log_scope(dual_comp)} (S1 priority on deadline ties)",
            flush=True,
        )
    decide_fn = cemini_decide.decide
    retrieve_fn = cemini_decide.retrieve_solver_context
    state = load_state()
    _sync_competition_scope(state, competition_id)
    seed_nemesis_state(state)
    save_state(state)
    hands_acted = 0
    rng = random.Random()
    last_join_at = 0.0
    last_lobby_log_at = 0.0
    last_qual_check_at = 0.0
    qual_protect = False
    lead_protect = False
    first_protect = False
    qual_status: dict = {}
    in_queue_only = False
    last_pace_log_at = 0.0
    dual_last_join_at = 0.0
    dual_in_queue_only = False

    try:
        creds = load_or_register(client, args.handle, args.name, args.quote)
        print(
            f"[cemini-lobby] agent={creds.get('agentId')} "
            f"{_lobby_log_scope(competition_id)}"
        )

        def ensure_joined(force: bool = False) -> None:
            nonlocal last_join_at, last_lobby_log_at, in_queue_only, last_pace_log_at
            now = time.time()
            if is_kill_switch_active():
                if (now - last_pace_log_at) >= LOBBY_LOG_INTERVAL_S:
                    ks = kill_switch_status()
                    print(
                        f"[cemini-lobby] KILL SWITCH ACTIVE — no new joins: "
                        f"{ks.get('reason', '?')}"
                    )
                    last_pace_log_at = now
                return
            hero_stack = qual_status.get("chips")
            if hero_stack is not None:
                try:
                    hero_stack = int(hero_stack)
                except (TypeError, ValueError):
                    hero_stack = None
            buy_in = int(os.environ.get("ARENA_PLAYGROUND_START_CHIPS") or 1000)
            big_blind = int(os.environ.get("ARENA_PLAYGROUND_BIG_BLIND") or 2)
            # API: rebuy only when total chips < bigBlindChips (not merely < table buy-in).
            if hero_stack is not None and hero_stack < big_blind:
                print(
                    f"[cemini-lobby] stack {hero_stack} < BB {big_blind} — rebuy attempt",
                    file=sys.stderr,
                )
                if _try_rebuy(client, competition_id):
                    refresh_qualification(force=True)
                    try:
                        hero_stack = int(qual_status.get("chips") or hero_stack)
                    except (TypeError, ValueError):
                        pass
            style = load_style_overrides()
            mult = float(style.get("join_retry_multiplier") or 1.0)
            retry_s = join_retry_seconds(
                first_protect=first_protect,
                lead_protect=lead_protect,
                qual_protect=qual_protect,
                in_queue_only=in_queue_only,
                hero_stack_chips=hero_stack,
                retry_multiplier=mult,
            )
            pace_phase = (os.environ.get("CEMINI_PACE_PHASE") or "").strip().lower()
            if (now - last_pace_log_at) >= LOBBY_LOG_INTERVAL_S:
                if first_protect:
                    print(
                        f"[cemini-lobby] pace throttle (first): "
                        f"join retry {retry_s:.0f}s — preserve #1 buffer"
                    )
                    last_pace_log_at = now
                elif pace_phase == "volume":
                    below = (
                        hero_stack is not None and hero_stack < buy_in
                    )
                    print(
                        f"[cemini-lobby] pace volume: join retry {retry_s:.0f}s "
                        f"(queue={'yes' if in_queue_only else 'no'}"
                        f"{', below buy-in' if below else ''})"
                    )
                    last_pace_log_at = now
                elif lead_protect or qual_protect:
                    tier = "lead" if lead_protect else "qualification"
                    print(
                        f"[cemini-lobby] pace throttle ({tier}): "
                        f"join retry {retry_s:.0f}s — fewer tables, preserve buffer"
                    )
                    last_pace_log_at = now
            if not force and (now - last_join_at) < retry_s:
                if in_queue_only and (now - last_lobby_log_at) >= LOBBY_LOG_INTERVAL_S:
                    _log_lobby_queue(client, competition_id)
                    last_lobby_log_at = now
                return
            try:
                join_resp = _join(client, competition_id)
                last_join_at = now
                in_queue_only = False
                state.pop("entry_fee_tx_hash", None)
                save_state(state)
                print(f"[cemini-lobby] join: {json.dumps(join_resp, sort_keys=True)[:500]}")
            except ArenaError as e:
                err_text = _arena_error_text(e.body).lower()
                if e.status >= 500:
                    print(f"[cemini-lobby] join server error {e.status}, retry later",
                          file=sys.stderr)
                    last_join_at = now
                    return
                if e.status == 402:
                    pay = e.body.get("paymentRequirements") or {} if isinstance(e.body, dict) else {}
                    pending_tx = state.get("entry_fee_tx_hash")
                    if pending_tx:
                        print(f"[cemini-lobby] retrying join with pending tx {pending_tx}",
                              file=sys.stderr)
                        try:
                            join_resp = _join(client, competition_id, tx_hash=pending_tx)
                            last_join_at = now
                            state.pop("entry_fee_tx_hash", None)
                            save_state(state)
                            print(f"[cemini-lobby] join after pending tx: "
                                  f"{json.dumps(join_resp, sort_keys=True)[:500]}")
                            return
                        except ArenaError as pend_err:
                            msg = _arena_error_text(pend_err.body)
                            if pend_err.status == 400 and "not yet mined" in msg.lower():
                                print("[cemini-lobby] tx still indexing on Arena…", file=sys.stderr)
                                last_join_at = now
                                return
                            if pend_err.status != 402:
                                print(f"[cemini-lobby] pending tx join failed: "
                                      f"{pend_err.status} {pend_err.body}", file=sys.stderr)
                                last_join_at = now
                                return
                    amt = pay.get("amount", "?")
                    cur = pay.get("currency", "MON")
                    w = client.get("/agent/wallet?chain=monad")
                    bal = (w.get("nativeBalance") or {}).get("formatted", "?")
                    print(
                        f"[cemini-lobby] entry fee {amt} {cur} — agent balance {bal} MON",
                        file=sys.stderr,
                    )
                    try:
                        join_resp = _join_with_entry_fee(
                            client, competition_id, pay, state=state, save_state_fn=save_state)
                        last_join_at = now
                        state.pop("entry_fee_tx_hash", None)
                        save_state(state)
                        print(f"[cemini-lobby] join after pay: "
                              f"{json.dumps(join_resp, sort_keys=True)[:500]}")
                    except ArenaError as pay_err:
                        msg = _arena_error_text(pay_err.body)
                        if pay_err.status == 400 and "not yet mined" in msg.lower():
                            # _join_with_entry_fee raises before storing — handled below
                            pass
                        print(f"[cemini-lobby] entry pay/join failed: {pay_err.status} "
                              f"{pay_err.body}", file=sys.stderr)
                        last_join_at = now
                    except Exception as pay_exc:
                        print(f"[cemini-lobby] entry pay/join error: {pay_exc}",
                              file=sys.stderr)
                        last_join_at = now
                    return
                if e.status == 403:
                    print("[cemini-lobby] X claim required — verify owner on dev.fun",
                          file=sys.stderr)
                    raise SystemExit(3) from e
                if e.status == 409 and (
                    "not enough chips" in err_text or "insufficient_chips" in err_text
                ):
                    if _try_rebuy(client, competition_id):
                        refresh_qualification(force=True)
                        last_join_at = 0.0
                        in_queue_only = False
                    else:
                        last_join_at = now
                    return
                if e.status == 409 and "already in the matchmaking lobby" in err_text:
                    in_queue_only = True
                    last_join_at = now
                    if (now - last_lobby_log_at) >= LOBBY_LOG_INTERVAL_S:
                        _log_lobby_queue(client, competition_id)
                        last_lobby_log_at = now
                    return
                in_queue_only = False
                print(f"[cemini-lobby] join note: {e.status} {e.body}", file=sys.stderr)
                last_join_at = now

        if not args.skip_join:
            ensure_joined(force=True)

        def refresh_qualification(force: bool = False) -> None:
            nonlocal last_qual_check_at, qual_protect, lead_protect, first_protect, qual_status
            now = time.time()
            if not force and (now - last_qual_check_at) < QUAL_STATUS_INTERVAL_S:
                return
            last_qual_check_at = now
            try:
                st = fetch_qualification_status(client, competition_id)
                qual_status = st
                qual_protect = bool(st.get("qualification_protect"))
                lead_protect = bool(st.get("lead_protect"))
                first_protect = bool(st.get("first_protect"))
                lock_note = ""
                if st.get("max_playable_chips") is not None:
                    lock_note = (
                        f" lock tier={st.get('lock_tier')} "
                        f"floor={st.get('qual_floor_chips')} "
                        f"locked={st.get('locked_chips')} playable={st.get('max_playable_chips')}"
                    )
                if first_protect:
                    print(
                        f"[cemini-lobby] FIRST protect ON "
                        f"rank={st.get('rank')} chips={st.get('chips')} "
                        f"buffer=+{st.get('buffer_chips')} vs #{st.get('cutoff_chips')} "
                        f"(pace {join_retry_seconds(first_protect=True, lead_protect=True, qual_protect=True, in_queue_only=False):.0f}s join retry)"
                        f"{lock_note}"
                    )
                elif lead_protect:
                    print(
                        f"[cemini-lobby] LEAD protect ON "
                        f"rank={st.get('rank')} chips={st.get('chips')} "
                        f"buffer=+{st.get('buffer_chips')} vs #{st.get('cutoff_chips')} "
                        f"(blind tax ~{avg_blind_tax_per_hand():.1f}/hand, "
                        f"~{hands_to_erosion(int(st.get('buffer_chips') or 0))} passive hands to erase buffer)"
                        f"{lock_note}"
                    )
                elif qual_protect:
                    print(
                        f"[cemini-lobby] qualification protect ON "
                        f"rank={st.get('rank')} chips={st.get('chips')} "
                        f"buffer=+{st.get('buffer_chips')} vs #{st.get('cutoff_chips')}"
                        f"{lock_note}"
                    )
                elif st.get("rank") is not None:
                    print(
                        f"[cemini-lobby] protect OFF "
                        f"rank={st.get('rank')} buffer=+{st.get('buffer_chips')}"
                    )
            except Exception as exc:
                print(f"[cemini-lobby] qual status skip: {exc}", file=sys.stderr)
            else:
                try:
                    append_playground_snapshot(
                        client,
                        agent_id=str(creds.get("agentId") or ""),
                        competition_id=competition_id,
                        qual_status=qual_status,
                        hands_played=int(state.get("hands_played") or 0),
                    )
                except Exception as ts_exc:
                    print(f"[cemini-lobby] timeseries skip: {ts_exc}", file=sys.stderr)

        refresh_qualification(force=True)

        def ensure_dual_joined(force: bool = False) -> None:
            nonlocal dual_last_join_at, dual_in_queue_only
            if not dual_comp:
                return
            now = time.time()
            retry_s = float(os.environ.get("CEMINI_JOIN_RETRY_S", "12"))
            if not force and (now - dual_last_join_at) < retry_s:
                return
            _apply_competition_posture(dual_comp)
            try:
                join_resp = _join(client, dual_comp)
                dual_last_join_at = now
                dual_in_queue_only = False
                print(
                    f"[cemini-lobby] {_lobby_log_scope(dual_comp)} "
                    f"join: {json.dumps(join_resp, sort_keys=True)[:300]}"
                )
            except ArenaError as e:
                err_text = _arena_error_text(e.body).lower()
                dual_last_join_at = now
                if e.status == 409 and "already in the matchmaking lobby" in err_text:
                    dual_in_queue_only = True
                    return
                if e.status == 409 and "max_concurrent_tables" in err_text:
                    # Discord: limit is per competition — API may still return global.
                    print(
                        f"[cemini-lobby] {_lobby_log_scope(dual_comp)} "
                        f"join blocked (max_concurrent_tables) — keep polling pending",
                        file=sys.stderr,
                    )
                    return
                print(
                    f"[cemini-lobby] {_lobby_log_scope(dual_comp)} "
                    f"join note: {e.status} {e.body}",
                    file=sys.stderr,
                )

        while True:
            try:
                pending = _pending(client, competition_id)
            except ArenaError as e:
                print(f"[cemini-lobby] pending-actions error: {e}", file=sys.stderr)
                ensure_joined(force=True)
                time.sleep(POLL_INTERVAL)
                continue

            tables = pending.get("tables") if isinstance(pending, dict) else []
            if not isinstance(tables, list):
                tables = []
            if dual_comp:
                try:
                    pending2 = _pending(client, dual_comp)
                    extra = pending2.get("tables") if isinstance(pending2, dict) else []
                    if isinstance(extra, list):
                        for row in extra:
                            cid = row.get("competitionId") or dual_comp
                            tables.append({**row, "competitionId": cid})
                except ArenaError as e:
                    print(
                        f"[cemini-lobby] {_lobby_log_scope(dual_comp)} "
                        f"pending-actions error: {e}",
                        file=sys.stderr,
                    )

            def _table_sort_key(row: dict) -> tuple[int, int]:
                cid = row.get("competitionId") or competition_id
                # S1 tournament wins deadline ties (operator priority).
                pri = 0 if s1_comp and cid == s1_comp else 1
                return (pri, int(row.get("actionDeadlineAt") or 0))

            tables = sorted(tables, key=_table_sort_key)

            if tables:
                in_queue_only = False
                dual_in_queue_only = False
                table = tables[0]
                table_comp = table.get("competitionId") or competition_id
                if not table.get("competitionId"):
                    table = {**table, "competitionId": table_comp}
                _apply_competition_posture(table_comp)
                if table_comp != competition_id:
                    st = fetch_qualification_status(client, table_comp)
                    qual_protect = bool(st.get("qualification_protect"))
                    lead_protect = bool(st.get("lead_protect"))
                    first_protect = bool(st.get("first_protect"))
                    qual_status = st
                else:
                    refresh_qualification()
                deadline_ms = table.get("actionDeadlineAt") or 0
                deadline_s = (
                    max(0.0, (deadline_ms / 1000.0) - time.time()) if deadline_ms else 10.0
                )
                ctx = _safe_research_context(table, retrieve_fn)
                if qual_protect or lead_protect:
                    ctx["qualification_protect"] = qual_protect
                    ctx["survival_mode"] = True
                if lead_protect:
                    ctx["lead_protect"] = True
                if first_protect:
                    ctx["first_protect"] = True
                if is_kill_switch_active():
                    ctx["kill_switch"] = True
                if table_comp == competition_id and _ko_survival_lane(state, qual_status):
                    ctx["ko_survival_lane"] = True
                    ctx["survival_mode"] = True
                nemesis = state.get("nemesis_handles")
                if nemesis:
                    ctx["nemesis_handles"] = nemesis
                st = qual_status
                if st.get("max_playable_chips") is not None:
                    ctx["leaderboard_chips"] = st.get("chips")
                    ctx["cutoff_chips"] = st.get("cutoff_chips")
                    ctx["max_playable_chips"] = st.get("max_playable_chips")
                    ctx["lock_tier"] = st.get("lock_tier")
                villain_mem = villain_memory_for_table(state, table)
                if villain_mem and not (
                    qual_protect or first_protect or ctx.get("ko_survival_lane")
                ):
                    ctx["session_villain_memory"] = villain_mem
                    mem_margins = exploit_from_memory(villain_mem)
                    if mem_margins:
                        hud = ctx.setdefault("opponent_hud", {})
                        base = hud.get("margins") or {}
                        hud["margins"] = {**base, **{
                            k: base.get(k, 0.0) + v for k, v in mem_margins.items()
                        }}
                try:
                    action = decide_fn(table, deadline_s=deadline_s, research_context=ctx)
                except TypeError:
                    action = decide_fn(table, deadline_s=deadline_s)
                action = _normalize_action_name(action)
                action = maybe_sanitize_action(action)
                payload = {"tableId": table["tableId"], **action}
                try:
                    client.post("/texas/action", payload)
                    hands_acted += 1
                    state["hands_played"] = state.get("hands_played", 0) + 1
                    update_session_memory(state, table)
                    save_state(state)
                    print(
                        f"[cemini-lobby] {_lobby_log_scope(table_comp)} "
                        f"action={action.get('action')} hands_acted={hands_acted}"
                    )
                except ArenaError as e:
                    if e.status == 409:
                        continue
                    if e.status == 400:
                        try:
                            client.post("/texas/action", {
                                "tableId": table["tableId"],
                                "action": "fold",
                                "message": "fallback after illegal action",
                                "reasoning": '{vr: "std", ke: "legal", pp: "pot control"}',
                            })
                        except ArenaError:
                            pass
                        continue
                    print(f"[cemini-lobby] action error: {e}", file=sys.stderr)
                    continue

            if args.max_actions and hands_acted >= args.max_actions:
                print(f"[cemini-lobby] hit --max-actions={args.max_actions}, stopping")
                return 0

            if not tables:
                now = time.time()
                refresh_qualification()
                if in_queue_only and (now - last_lobby_log_at) >= LOBBY_LOG_INTERVAL_S:
                    _log_lobby_queue(client, competition_id)
                    last_lobby_log_at = now
                ensure_joined(force=False)
                ensure_dual_joined(force=False)
                time.sleep(POLL_INTERVAL + rng.uniform(-POLL_JITTER, POLL_JITTER))
    finally:
        client.close()


def _apply_prod_defense_defaults() -> None:
    """Enable anti-profiling defaults for live lobby unless operator overrides."""
    os.environ.setdefault("CEMINI_SANITIZE_OUTPUT", "1")
    os.environ.setdefault("CEMINI_MIX_POSTFLOP", "1")


def main(argv: Optional[list[str]] = None) -> int:
    _apply_prod_defense_defaults()
    p = argparse.ArgumentParser(description="Cemini dev.fun texas lobby loop")
    p.add_argument("--competition-id", default=None)
    p.add_argument(
        "--also-competition-id",
        default=None,
        help="Second competition in same loop (per-event table limit; S1 priority on ties)",
    )
    p.add_argument("--max-actions", type=int, default=0,
                   help="Stop after N actions submitted (0 = run until interrupt)")
    p.add_argument("--skip-join", action="store_true",
                   help="Skip initial join (still re-joins periodically when idle)")
    p.add_argument("--handle", default="cemini_wiki_poker")
    p.add_argument("--name", default="Cemini Wiki Poker")
    p.add_argument("--quote", default="structured skills over swagger")
    return run_lobby(p.parse_args(argv))


if __name__ == "__main__":
    raise SystemExit(main())
