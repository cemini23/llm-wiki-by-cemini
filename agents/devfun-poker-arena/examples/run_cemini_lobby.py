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
    poll_showdown_memory,
    update_session_memory,
    villain_memory_for_table,
)
from hierarchical_session_state import (  # noqa: E402
    attach_hierarchical_slice,
    empty_state,
    evict_completed,
    reset_mid_term,
    update_scratchpad_facts,
    update_short_term,
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


def _sandbox_pvp_submit_only() -> bool:
    """Sandbox PvP comps use bundle submit — not texas/join lobby."""
    return os.environ.get("CEMINI_SANDBOX_PVP_SUBMIT_ONLY", "").strip().lower() in (
        "1", "true", "yes", "on",
    )


def _researcher_track_primary() -> bool:
    """Researcher Round is the optimization target; Playground is optional intel."""
    role = os.environ.get("CEMINI_LOBBY_ROLE", "").strip().lower()
    track = os.environ.get("CEMINI_PRIMARY_TRACK", "").strip().lower()
    if os.environ.get("CEMINI_RESEARCHER_MODE", "").strip().lower() in ("1", "true", "yes", "on"):
        return True
    return role in ("researcher_primary", "researcher_prep") or track == "researcher"


def _lobby_role_label(competition_id: str) -> tuple[str, str]:
    """Resolve human label + registry role for logs and timeseries."""
    s1 = os.environ.get("S1_TOURNAMENT_COMP", "").strip()
    s2t = os.environ.get("S2_TOURNAMENT_COMP", "").strip()
    s2 = os.environ.get("S2_PLAYGROUND_COMP", "").strip()
    s3 = os.environ.get("S3_PLAYGROUND_COMP", "").strip()
    s9 = os.environ.get("S9_PLAYGROUND_COMP", "cmrt1wzu40jm911suskj9qebe").strip()
    s10 = os.environ.get("S10_PLAYGROUND_COMP", "cms0bwufmf3n8kyykdpxi6d2i").strip()
    s11 = os.environ.get("S11_PLAYGROUND_COMP", "cms7hrnjg20czv7oi85cho570").strip()
    s10t = os.environ.get("S10_TOURNAMENT_COMP", "").strip()
    rcomp = os.environ.get("ARENA_RESEARCHER_COMP_ID", "").strip()
    if competition_id and competition_id == rcomp:
        return "Researcher Round", "researcher_round"
    label = os.environ.get("CEMINI_LOBBY_LABEL", "").strip().replace("_", " ")
    role = os.environ.get("CEMINI_LOBBY_ROLE", "").strip()
    if label and role:
        return label, role
    if competition_id and competition_id == s1:
        return "Tournament S1", "s1_tournament"
    if competition_id and competition_id == s2t:
        return "Tournament S2", "s2_tournament"
    if competition_id and s10t and competition_id == s10t:
        return "Tournament S10", "s10_tournament"
    if competition_id and competition_id == s2:
        return "Playground S2", "s2_playground"
    if competition_id and competition_id == s3:
        return "Playground S3", "s3_playground"
    if competition_id and competition_id == s9:
        return "Playground S9", "s9_playground"
    if competition_id and competition_id == s10:
        return "Playground S10", "s10_playground"
    if competition_id and competition_id == s11:
        return "Playground S11", "s11_playground"
    label = os.environ.get("CEMINI_LOBBY_LABEL", "").strip().replace("_", " ")
    role = os.environ.get("CEMINI_LOBBY_ROLE", "").strip()
    return label or competition_id, role or "lobby"


def _lobby_log_scope(competition_id: str) -> str:
    label, role = _lobby_role_label(competition_id)
    return f"comp={competition_id} role={role} label={label}"


def _apply_competition_posture(competition_id: str) -> None:
    """Per-comp env — comp id is source of truth (not global CEMINI_TOURNAMENT_MODE)."""
    s1 = os.environ.get("S1_TOURNAMENT_COMP", "").strip()
    s2t = os.environ.get("S2_TOURNAMENT_COMP", "").strip()
    s2 = os.environ.get("S2_PLAYGROUND_COMP", "cmq57o53r0bhw18g23qkydb08").strip()
    s3 = os.environ.get("S3_PLAYGROUND_COMP", "").strip()
    s9 = os.environ.get("S9_PLAYGROUND_COMP", "cmrt1wzu40jm911suskj9qebe").strip()
    s10 = os.environ.get("S10_PLAYGROUND_COMP", "cms0bwufmf3n8kyykdpxi6d2i").strip()
    s11 = os.environ.get("S11_PLAYGROUND_COMP", "cms7hrnjg20czv7oi85cho570").strip()
    s10t = os.environ.get("S10_TOURNAMENT_COMP", "").strip()
    rcomp = os.environ.get("ARENA_RESEARCHER_COMP_ID", "").strip()
    _pg_role = os.environ.get("CEMINI_LOBBY_ROLE", "").strip().lower()
    _chip_qual_playground = competition_id in (s9, s10, s11) or _pg_role in (
        "s9_playground",
        "s10_playground",
        "s11_playground",
    )
    _s10_tournament = (
        (s10t and competition_id == s10t)
        or _pg_role == "s10_tournament"
    )
    if rcomp and competition_id == rcomp:
        os.environ.update({
            "CEMINI_RESEARCHER_MODE": "1",
            "CEMINI_TABLE_FORMAT": "hu",
            "CEMINI_TOURNAMENT_MODE": "0",
            "CEMINI_EVAL_PANEL_GATE": "0",
            "CEMINI_PLACEMENT_CHASE": "0",
            "CEMINI_SANITIZE_OUTPUT": "1",
            "CEMINI_PACE_PHASE": "researcher",
            "CEMINI_JOIN_RETRY_S": "60",
            "CEMINI_IN_QUEUE_RETRY_S": "120",
            "CEMINI_LOW_STACK_JOIN_RETRY_S": "300",
            "JACKPOT_ROYAL_ENABLED": "0",
            "JACKPOT_ROYAL_SHOWDOWN": "0",
            "JACKPOT_27_HUNT_ENABLED": "0",
        })
    elif competition_id == s3:
        if _researcher_track_primary():
            # Playground S3 — background intel only while Researcher is primary.
            os.environ.update({
                "CEMINI_TOURNAMENT_MODE": "0",
                "CEMINI_EVAL_PANEL_GATE": "0",
                "CEMINI_PACE_PHASE": "intel",
                "CEMINI_JOIN_RETRY_S": "3600",
                "CEMINI_IN_QUEUE_RETRY_S": "600",
                "CEMINI_LOW_STACK_JOIN_RETRY_S": "3600",
                "CEMINI_QUAL_CUTOFF_RANK": "20",
                "CEMINI_PRIZE_CUTOFF_RANK": "20",
                "CEMINI_PLAYGROUND_TIMESERIES": "0",
                "JACKPOT_ROYAL_ENABLED": "0",
                "JACKPOT_ROYAL_SHOWDOWN": "0",
                "JACKPOT_27_HUNT_ENABLED": "0",
            })
        else:
            os.environ.update({
                "CEMINI_TOURNAMENT_MODE": "0",
                "CEMINI_EVAL_PANEL_GATE": "0",
                "CEMINI_PACE_PHASE": "volume",
                "CEMINI_JOIN_RETRY_S": "12",
                "CEMINI_IN_QUEUE_RETRY_S": "25",
                "CEMINI_LOW_STACK_JOIN_RETRY_S": "15",
                "CEMINI_QUAL_CUTOFF_RANK": "20",
                "CEMINI_PRIZE_CUTOFF_RANK": "20",
                "JACKPOT_ROYAL_ENABLED": "0",
                "JACKPOT_ROYAL_SHOWDOWN": "0",
                "JACKPOT_27_HUNT_ENABLED": "0",
            })
    elif competition_id == s2:
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
    elif _chip_qual_playground:
        # Playground S9/S10 chip qual — 6-max grind (top 20 → paired Tournament).
        # Briefs: S1a nit ~10–16% VPIP; gin/HU ladder/eval crush OFF.
        os.environ.update({
            "CEMINI_TOURNAMENT_MODE": "0",
            "CEMINI_TABLE_FORMAT": "6max",
            "CEMINI_RESEARCHER_MODE": "0",
            "CEMINI_SANDBOX_PVP_SUBMIT_ONLY": "0",
            "CEMINI_EVAL_PANEL_GATE": "0",
            "CEMINI_EVAL_PANEL_MODE": "0",
            "CEMINI_PLACEMENT_CHASE": "0",
            "CEMINI_PACE_PHASE": "volume",
            "CEMINI_JOIN_RETRY_S": "12",
            "CEMINI_IN_QUEUE_RETRY_S": "25",
            "CEMINI_LOW_STACK_JOIN_RETRY_S": "15",
            "CEMINI_S1B_MIN_STACK_BB": "60",
            "CEMINI_QUAL_CUTOFF_RANK": "20",
            "CEMINI_PRIZE_CUTOFF_RANK": "20",
            "CEMINI_COLD_START_NO_STEAL": "0",
            "CEMINI_TAG_WIDEN": "1",
            "CEMINI_KO_SURVIVAL": "1",
            "CEMINI_KO_SURVIVAL_HANDS": "40",
            "CEMINI_KO_SURVIVAL_MIN_STACK": "700",
            "CEMINI_STAGGER_LOCKS": "1",
            "CEMINI_NUTS_DETECT": "1",
            "CEMINI_SANITIZE_OUTPUT": "1",
            "CEMINI_PLAYGROUND_TIMESERIES": "1",
            "CEMINI_GIN_KILL": "1",
            "CEMINI_GIN_STYLE": "0",
            "CEMINI_GIN_STYLE_PREFLOP": "0",
            "CEMINI_GIN_STYLE_POSTFLOP": "0",
            "CEMINI_GIN_STYLE_GATE": "0",
            "CEMINI_GIN_V008": "0",
            "CEMINI_GIN_V2_EXPLOITS": "0",
            "CEMINI_SHORT_STACK_BB": "20",
            "CEMINI_MAX_REBUYS": "2",
            "CEMINI_REBUY_MAX_MON": "5",
            "CEMINI_SURVIVAL_STACK_CHIPS": "500",
            "CEMINI_MAFP_CHART": "0",
            "CEMINI_SOLVER_V3": "0",
            "CEMINI_SOLVER_HARD": "0",
            "CEMINI_TRAJECTORY_BOUND": "0",
            "CEMINI_VERIFIER_BON": "0",
            "CEMINI_EVAL_CRUSH": "0",
            "JACKPOT_ROYAL_ENABLED": "0",
            "JACKPOT_ROYAL_SHOWDOWN": "0",
            "JACKPOT_27_HUNT_ENABLED": "0",
        })
    elif _s10_tournament:
        # Tournament S10 — abandoned after bust (2026-08-01). If lobby lands here,
        # stay gin-killed + short-stack safe; do not re-enable climb widen.
        os.environ.update({
            "CEMINI_TOURNAMENT_MODE": "1",
            "CEMINI_TABLE_FORMAT": "auto",
            "CEMINI_RESEARCHER_MODE": "0",
            "CEMINI_SANDBOX_PVP_SUBMIT_ONLY": "0",
            "CEMINI_PLACEMENT_CHASE": "0",
            "CEMINI_EVAL_PANEL_GATE": "0",
            "CEMINI_EVAL_PANEL_MODE": "0",
            "CEMINI_PRIZE_CUTOFF_RANK": "3",
            "CEMINI_QUAL_CUTOFF_RANK": "25",
            "CEMINI_KO_SURVIVAL": "1",
            "CEMINI_KO_SURVIVAL_HANDS": "60",
            "CEMINI_SURVIVAL_STACK_CHIPS": "400",
            "CEMINI_S1B_MIN_STACK_BB": "60",
            "CEMINI_STAGGER_LOCKS": "0",
            "CEMINI_COLD_START_NO_STEAL": "1",
            "CEMINI_NEMESIS_TIGHT": "1",
            "CEMINI_GIN_KILL": "1",
            "CEMINI_GIN_STYLE": "0",
            "CEMINI_GIN_STYLE_PREFLOP": "0",
            "CEMINI_GIN_STYLE_POSTFLOP": "0",
            "CEMINI_GIN_STYLE_GATE": "0",
            "CEMINI_GIN_V008": "0",
            "CEMINI_GIN_V2_EXPLOITS": "0",
            "CEMINI_SHORT_STACK_BB": "20",
            "CEMINI_MAX_REBUYS": "2",
            "CEMINI_REBUY_MAX_MON": "5",
            "CEMINI_MAFP_CHART": "0",
            "CEMINI_SOLVER_V3": "0",
            "CEMINI_EVAL_CRUSH": "0",
            "CEMINI_JOIN_RETRY_S": "25",
            "CEMINI_IN_QUEUE_RETRY_S": "60",
            "CEMINI_LOW_STACK_JOIN_RETRY_S": "30",
            "JACKPOT_ROYAL_ENABLED": "0",
            "JACKPOT_ROYAL_SHOWDOWN": "0",
            "JACKPOT_27_HUNT_ENABLED": "0",
        })
    elif competition_id in (s1, s2t):
        os.environ.update({
            "CEMINI_TOURNAMENT_MODE": "1",
            "CEMINI_PRIZE_CUTOFF_RANK": "10",
            "CEMINI_QUAL_CUTOFF_RANK": "10",
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
    state["rebuy_count"] = 0
    state.pop("rebuy_fund_blocked_until", None)
    state.pop("rebuy_fund_block_reason", None)
    state.pop("rebuy_fund_block_logged", None)
    state.pop("session_villain_memory", None)
    state.pop("showdown_tables_seen", None)
    # K161: reset mid-term hierarchical memory on competition board change
    if "hierarchical_session" in state:
        reset_mid_term(state["hierarchical_session"])
    else:
        state["hierarchical_session"] = empty_state()
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


def _wallet_native_balance(client: ArenaClient, chain: str = "monad") -> Optional[dict]:
    try:
        body = client.get(f"/agent/wallet?chain={chain}")
        if isinstance(body, dict):
            return body.get("nativeBalance") if isinstance(body.get("nativeBalance"), dict) else None
    except ArenaError:
        return None
    return None


def _payment_amount_insufficient(wallet_bal: Optional[dict], payment: dict) -> bool:
    """Heuristic: compare wei strings when both sides look like integer token amounts."""
    if not wallet_bal or not payment:
        return False
    try:
        have = int(str(wallet_bal.get("value") or "0"))
        need = int(str(payment.get("amount") or "0"))
    except (TypeError, ValueError):
        return False
    # Arena rebuy fees are whole-MON strings (e.g. "250"); wallet value is wei.
    if need > 0 and need < 10_000 and have < need * 10 ** 15:
        return True
    return have < need


def _mark_rebuy_fund_block(state: dict, reason: str, hours: float = 6.0) -> None:
    state["rebuy_fund_blocked_until"] = time.time() + hours * 3600.0
    state["rebuy_fund_block_reason"] = reason[:500]


def _rebuy_fund_blocked(state: dict) -> bool:
    until = state.get("rebuy_fund_blocked_until")
    if until is None:
        return False
    try:
        return time.time() < float(until)
    except (TypeError, ValueError):
        return False


def _pay_entry_fee(client: ArenaClient, payment: dict) -> str:
    """Pay competition entry from agent wallet; return txHash."""
    dest = payment.get("to")
    amt = payment.get("amount")
    if not dest or not amt:
        raise ValueError(f"invalid payment requirements: {payment}")
    chain = payment.get("chain") or "monad"
    bal = _wallet_native_balance(client, chain)
    if _payment_amount_insufficient(bal, payment):
        have_fmt = bal.get("formatted") if bal else "?"
        raise ArenaError(
            402,
            {
                "error": "wallet_underfunded",
                "message": (
                    f"wallet native {have_fmt} {payment.get('currency') or 'MON'} "
                    f"< rebuy/entry fee {amt} — fund agent wallet then retry"
                ),
            },
        )
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


def _max_rebuys() -> int:
    raw = os.environ.get("CEMINI_MAX_REBUYS", "2")
    try:
        return max(0, int(raw))
    except ValueError:
        return 2


def _rebuy_max_mon() -> float:
    """Refuse paid rebuy if Arena fee (MON) exceeds this. 0 = unlimited."""
    raw = os.environ.get("CEMINI_REBUY_MAX_MON", "5")
    try:
        return max(0.0, float(raw))
    except ValueError:
        return 5.0


def _try_rebuy(
    client: ArenaClient,
    competition_id: str,
    state: Optional[dict] = None,
    save_state_fn=None,
) -> bool:
    """Rebuy chips when table buy-in exceeds stack. Returns True if rebuy attempted."""
    if state is not None and _rebuy_fund_blocked(state):
        return False
    if state is not None:
        used = int(state.get("rebuy_count") or 0)
        cap = _max_rebuys()
        if used >= cap:
            print(
                f"[cemini-lobby] rebuy blocked: count {used} >= CEMINI_MAX_REBUYS={cap}",
                file=sys.stderr,
            )
            _mark_rebuy_fund_block(
                state, f"max rebuys {cap} reached (post-mortem T10)", hours=72.0,
            )
            if save_state_fn:
                save_state_fn(state)
            return False
    try:
        resp = client.post("/texas/rebuy", {"competitionId": competition_id})
        print(f"[cemini-lobby] rebuy: {json.dumps(resp, sort_keys=True)[:300]}")
        if state is not None:
            state["rebuy_count"] = int(state.get("rebuy_count") or 0) + 1
            state.pop("rebuy_fund_blocked_until", None)
            state.pop("rebuy_fund_block_reason", None)
            if save_state_fn:
                save_state_fn(state)
        return True
    except ArenaError as e:
        if e.status != 402:
            print(f"[cemini-lobby] rebuy failed: {e.status} {e.body}", file=sys.stderr)
            return False
        pay = e.body.get("paymentRequirements") or {} if isinstance(e.body, dict) else {}
        try:
            fee_cap = _rebuy_max_mon()
            if fee_cap > 0 and pay:
                try:
                    fee = float(pay.get("amount") or 0)
                except (TypeError, ValueError):
                    fee = 0.0
                if fee > fee_cap:
                    msg = (
                        f"rebuy fee {fee} MON > CEMINI_REBUY_MAX_MON={fee_cap} "
                        "(T10 post-mortem: refuse 250 MON yolo)"
                    )
                    print(f"[cemini-lobby] {msg}", file=sys.stderr)
                    if state is not None:
                        _mark_rebuy_fund_block(state, msg, hours=72.0)
                        if save_state_fn:
                            save_state_fn(state)
                    return False
            resp = _rebuy_with_payment(client, competition_id, pay)
            print(f"[cemini-lobby] rebuy after pay: {json.dumps(resp, sort_keys=True)[:300]}")
            if state is not None:
                state["rebuy_count"] = int(state.get("rebuy_count") or 0) + 1
                state.pop("rebuy_fund_blocked_until", None)
                state.pop("rebuy_fund_block_reason", None)
                if save_state_fn:
                    save_state_fn(state)
            return True
        except ArenaError as pay_err:
            print(f"[cemini-lobby] rebuy pay failed: {pay_err.status} {pay_err.body}",
                  file=sys.stderr)
            err_body = pay_err.body if isinstance(pay_err.body, dict) else {}
            if pay_err.status in (402, 503):
                bal = _wallet_native_balance(client, pay.get("chain") or "monad")
                if bal:
                    print(
                        f"[cemini-lobby] wallet native {bal.get('formatted')} "
                        f"{pay.get('currency') or 'MON'} — fee amount {pay.get('amount')}",
                        file=sys.stderr,
                    )
                if state is not None and (
                    err_body.get("error") in (
                        "NATIVE_TRANSFER_PREFLIGHT_FAILED",
                        "wallet_underfunded",
                    )
                    or pay_err.status == 402
                ):
                    _mark_rebuy_fund_block(
                        state,
                        str(err_body.get("message") or err_body.get("error") or pay_err.body),
                    )
                    if save_state_fn:
                        save_state_fn(state)
                    print(
                        "[cemini-lobby] rebuy fund block — pausing rebuy attempts for 6h "
                        "(fund wallet or manual Arena rebuy)",
                        file=sys.stderr,
                    )
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
    s2t_comp = os.environ.get("S2_TOURNAMENT_COMP", "").strip()
    rcomp = os.environ.get("ARENA_RESEARCHER_COMP_ID", "").strip()

    def _tournament_table_priority(cid: str) -> int:
        """Lower = higher priority. Researcher + tournament beat playground on deadline ties."""
        if rcomp and cid == rcomp:
            return -1
        if s1_comp and cid == s1_comp:
            return 0
        if s2t_comp and cid == s2t_comp:
            return 1
        return 2
    if dual_comp and dual_comp == competition_id:
        dual_comp = ""
    _apply_competition_posture(competition_id)
    if dual_comp:
        print(
            f"[cemini-lobby] dual lobby: primary {_lobby_log_scope(competition_id)} "
            f"+ secondary {_lobby_log_scope(dual_comp)} (tournament priority on deadline ties)",
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
    placement_protect = False
    placement_chase = False
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
            if _sandbox_pvp_submit_only():
                if force or (now - last_lobby_log_at) >= LOBBY_LOG_INTERVAL_S:
                    print(
                        "[cemini-lobby] sandbox PvP submit-only — skip texas/join "
                        f"(poll submit_sandbox_pvp.py; intel comp={dual_comp or competition_id})",
                        flush=True,
                    )
                    last_lobby_log_at = now
                return
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
                if _rebuy_fund_blocked(state):
                    if not state.get("rebuy_fund_block_logged"):
                        print(
                            f"[cemini-lobby] stack {hero_stack} < BB {big_blind} — "
                            f"rebuy paused: {state.get('rebuy_fund_block_reason', '?')}",
                            file=sys.stderr,
                        )
                        state["rebuy_fund_block_logged"] = True
                        save_state(state)
                elif _try_rebuy(client, competition_id, state, save_state):
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
                placement_chase=placement_chase,
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
                    if _try_rebuy(client, competition_id, state, save_state):
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
            nonlocal last_qual_check_at, qual_protect, lead_protect, first_protect
            nonlocal placement_protect, placement_chase, qual_status
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
                placement_protect = bool(st.get("placement_protect"))
                placement_chase = bool(st.get("placement_chase"))
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
                elif placement_protect:
                    print(
                        f"[cemini-lobby] MONEY ZONE protect ON "
                        f"(top {st.get('prize_cutoff_rank', 10)}) "
                        f"rank={st.get('rank')} chips={st.get('chips')} "
                        f"buffer=+{st.get('buffer_chips')} vs #{st.get('cutoff_chips')}"
                    )
                elif placement_chase:
                    print(
                        f"[cemini-lobby] CHASE zone "
                        f"(need top {st.get('prize_cutoff_rank', 10)} for prize) "
                        f"rank={st.get('rank')} chips={st.get('chips')} "
                        f"gap to bubble={st.get('buffer_chips')}"
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
                pri = _tournament_table_priority(cid)
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
                    placement_protect = bool(st.get("placement_protect"))
                    placement_chase = bool(st.get("placement_chase"))
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
                if placement_protect:
                    ctx["placement_protect"] = True
                if placement_chase:
                    ctx["placement_chase"] = True
                if is_kill_switch_active():
                    ctx["kill_switch"] = True
                if table_comp == competition_id and _ko_survival_lane(state, qual_status):
                    ctx["ko_survival_lane"] = True
                    # Do NOT set survival_mode here. That flips survival_tight and
                    # permanently overrides placement_chase margins (mild KO branch
                    # becomes dead code). Super-audit T10 2026-07-30 consensus.
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
                # Keep villain memory during KO hour-one when chasing (need reads).
                if villain_mem and not (
                    qual_protect
                    or first_protect
                    or (ctx.get("ko_survival_lane") and not placement_chase)
                ):
                    ctx["session_villain_memory"] = villain_mem
                    mem_margins = exploit_from_memory(villain_mem)
                    if mem_margins:
                        hud = ctx.setdefault("opponent_hud", {})
                        base = hud.get("margins") or {}
                        hud["margins"] = {**base, **{
                            k: base.get(k, 0.0) + v for k, v in mem_margins.items()
                        }}
                # K161: bounded hierarchical slice (never full trajectories)
                state.setdefault("hierarchical_session", empty_state())
                hero_seat = table.get("selfSeatNumber")
                stack_bb = None
                try:
                    for seat in table.get("seats") or []:
                        if seat.get("seatNumber") == hero_seat:
                            chips = seat.get("chips")
                            bb = table.get("bigBlind") or table.get("bb") or 2
                            if chips is not None and bb:
                                stack_bb = round(float(chips) / float(bb), 2)
                            break
                except (TypeError, ValueError):
                    stack_bb = None
                facts = {"table_id": table.get("tableId")}
                if stack_bb is not None:
                    facts["stack_bb"] = stack_bb
                update_scratchpad_facts(state["hierarchical_session"], facts)
                attach_hierarchical_slice(ctx, state)
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
                    update_short_term(
                        state.setdefault("hierarchical_session", empty_state()),
                        {
                            "hand_id": table.get("tableId"),
                            "action": action.get("action"),
                            "position": table.get("selfPosition") or table.get("position"),
                        },
                    )
                    evict_completed(state["hierarchical_session"])
                    hero_aid = str(creds.get("agentId") or "")
                    if hero_aid:
                        poll_showdown_memory(client, state, hero_aid, table_comp)
                    save_state(state)
                    stack_note = ""
                    if stack_bb is not None:
                        stack_note = f" stack_bb={stack_bb}"
                    reason = action.get("message") or action.get("reasoning") or ""
                    if isinstance(reason, str) and len(reason) > 80:
                        reason = reason[:77] + "..."
                    reason_note = f" reason={reason!r}" if reason else ""
                    print(
                        f"[cemini-lobby] {_lobby_log_scope(table_comp)} "
                        f"action={action.get('action')} hands_acted={hands_acted}"
                        f"{stack_note}{reason_note}"
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
                hero_aid = str(creds.get("agentId") or "")
                if hero_aid:
                    poll_showdown_memory(client, state, hero_aid, competition_id)
                    if dual_comp:
                        poll_showdown_memory(client, state, hero_aid, dual_comp)
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
