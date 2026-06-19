"""Lightweight per-session villain memory for lobby play.

Tracks recent aggression per opponent agent id within a competition session.
Fed into cemini_decide via research_context — mirrors Agent Memory Test themes:
extract stable patterns, update on new evidence, abstain when sample is thin.

K118 F6: per-villain deque of last 5 showdown outcomes (won/lost + preflop aggression).
"""
from __future__ import annotations

import os
from typing import Any

_MIN_SAMPLES = 3
_AGGR_THRESHOLD = 0.55  # fold-to-bet rate below this → "aggro"
_SHOWDOWN_QUEUE_MAX = 5
_PROCESSED_TABLES_MAX = 400
_SHOWDOWN_MIN_FOR_EXPLOIT = 2
_SHOWDOWN_DOMINANCE = 3  # of last ≤5


def _session_memory_enabled() -> bool:
    raw = str(os.environ.get("CEMINI_SESSION_MEMORY", "1")).strip().lower()
    return raw not in {"", "0", "false", "off", "no"}


def _seat_agent_map(table: dict) -> dict[int, str]:
    out: dict[int, str] = {}
    for s in table.get("seats") or []:
        sn = s.get("seatNumber")
        aid = s.get("agentId") or s.get("playerId")
        if sn is not None and aid:
            out[int(sn)] = str(aid)
    return out


def _hero_seat(table: dict) -> int | None:
    sn = table.get("selfSeatNumber")
    return int(sn) if sn is not None else None


def _street_bets(table: dict) -> list[tuple[str, int, int]]:
    """(agent_id, chips, seat) for current-street aggressive actions if present."""
    events = table.get("actionHistory") or table.get("actions") or []
    street = (table.get("street") or "").lower()
    rows: list[tuple[str, int, int]] = []
    agents = _seat_agent_map(table)
    for ev in events:
        if not isinstance(ev, dict):
            continue
        if street and (ev.get("street") or "").lower() not in ("", street):
            continue
        act = (ev.get("action") or ev.get("type") or "").lower()
        if act not in ("bet", "raise", "all-in", "allin"):
            continue
        seat = ev.get("seatNumber")
        if seat is None:
            continue
        aid = agents.get(int(seat)) or ev.get("agentId")
        if not aid:
            continue
        amt = int(ev.get("amount") or ev.get("chips") or 0)
        rows.append((str(aid), amt, int(seat)))
    return rows


def _winner_agent_ids(table_row: dict) -> set[str]:
    out: set[str] = set()
    for w in table_row.get("winners") or []:
        if not isinstance(w, dict):
            continue
        aid = w.get("agentId") or w.get("playerId")
        if aid:
            out.add(str(aid))
    return out


def _villain_preflop_aggressive(table_row: dict, villain_aid: str) -> bool:
    agents = _seat_agent_map(table_row)
    for ev in table_row.get("actionHistory") or table_row.get("actions") or []:
        if not isinstance(ev, dict):
            continue
        est = (ev.get("street") or "preflop").lower()
        if est not in ("preflop", ""):
            continue
        act = (ev.get("action") or ev.get("type") or "").lower()
        if act not in ("bet", "raise", "all-in", "allin"):
            continue
        seat = ev.get("seatNumber")
        aid = None
        if seat is not None:
            aid = agents.get(int(seat)) or ev.get("agentId")
        else:
            aid = ev.get("agentId")
        if aid and str(aid) == villain_aid:
            return True
    return False


def _villain_showed_at_showdown(seat: dict, villain_aid: str, winners: set[str]) -> bool:
    if str(villain_aid) in winners:
        return True
    if int(seat.get("payoutChips") or 0) > 0:
        return True
    hole = seat.get("holeCards") or []
    return bool(hole)


def _trim_processed_tables(state: dict) -> list[str]:
    seen = list(state.get("showdown_tables_seen") or [])
    if len(seen) > _PROCESSED_TABLES_MAX:
        seen = seen[-_PROCESSED_TABLES_MAX:]
        state["showdown_tables_seen"] = seen
    return seen


def record_showdown_from_table(
    state: dict,
    table_row: dict,
    hero_agent_id: str,
) -> bool:
    """Ingest one settled recent-table row; return True when newly recorded."""
    tid = str(table_row.get("id") or table_row.get("tableId") or "")
    if not tid or not hero_agent_id:
        return False
    seen = _trim_processed_tables(state)
    if tid in seen:
        return False

    winners = _winner_agent_ids(table_row)
    seats = table_row.get("seats") or []
    hero_seat = next(
        (s for s in seats if str(s.get("agentId") or "") == hero_agent_id),
        None,
    )
    if not hero_seat:
        seen.append(tid)
        state["showdown_tables_seen"] = seen
        return False

    hero_won = hero_agent_id in winners or int(hero_seat.get("payoutChips") or 0) > 0
    mem = state.setdefault("session_villain_memory", {})
    recorded = False
    for seat in seats:
        if not isinstance(seat, dict):
            continue
        aid = seat.get("agentId") or seat.get("playerId")
        if not aid or str(aid) == hero_agent_id:
            continue
        if not _villain_showed_at_showdown(seat, str(aid), winners):
            continue
        rec = mem.setdefault(
            str(aid),
            {"aggressive_acts": 0, "passive_acts": 0, "samples": 0, "showdowns": []},
        )
        queue = list(rec.get("showdowns") or [])
        queue.append({
            "hero_won": bool(hero_won),
            "villain_won": str(aid) in winners,
            "villain_preflop_aggressive": _villain_preflop_aggressive(table_row, str(aid)),
        })
        rec["showdowns"] = queue[-_SHOWDOWN_QUEUE_MAX:]
        recorded = True

    seen.append(tid)
    state["showdown_tables_seen"] = seen
    return recorded


def poll_showdown_memory(
    client: Any,
    state: dict,
    hero_agent_id: str,
    competition_id: str | None,
) -> int:
    """Fetch recent settled tables and append new showdown rows. Returns new count."""
    from analyze import _fetch_recent_tables  # noqa: WPS433

    if not hero_agent_id:
        return 0
    tables = _fetch_recent_tables(client, hero_agent_id, competition_id, limit=40)
    n = 0
    for row in tables:
        if record_showdown_from_table(state, row, hero_agent_id):
            n += 1
    return n


def _showdown_summary(showdowns: list[dict]) -> dict[str, Any]:
    if not showdowns:
        return {}
    n = len(showdowns)
    villain_wins = sum(1 for x in showdowns if x.get("villain_won"))
    hero_wins = sum(1 for x in showdowns if x.get("hero_won"))
    preflop_aggro = sum(1 for x in showdowns if x.get("villain_preflop_aggressive"))
    return {
        "n": n,
        "villain_wins": villain_wins,
        "hero_wins": hero_wins,
        "preflop_aggro": preflop_aggro,
    }


def _showdown_exploit_margins(villains: dict[str, dict]) -> dict[str, float]:
    """Tune margins from last ≤5 showdowns vs villains at this table."""
    margins: dict[str, float] = {}
    for rec in villains.values():
        sd_raw = rec.get("showdowns")
        if isinstance(sd_raw, dict):
            summary = sd_raw
            if int(summary.get("n") or 0) < _SHOWDOWN_MIN_FOR_EXPLOIT:
                continue
        else:
            sd = list(sd_raw or [])
            if len(sd) < _SHOWDOWN_MIN_FOR_EXPLOIT:
                continue
            summary = _showdown_summary(sd)
        if summary.get("villain_wins", 0) >= _SHOWDOWN_DOMINANCE:
            margins["fold_slack_delta"] = margins.get("fold_slack_delta", 0.0) + 0.02
            margins["preflop_fold_margin_delta"] = (
                margins.get("preflop_fold_margin_delta", 0.0) + 0.02
            )
        elif summary.get("hero_wins", 0) >= _SHOWDOWN_DOMINANCE:
            margins["bet_bar_delta"] = margins.get("bet_bar_delta", 0.0) - 0.02
            margins["call_margin_delta"] = margins.get("call_margin_delta", 0.0) - 0.02
        if summary.get("preflop_aggro", 0) >= _SHOWDOWN_DOMINANCE:
            margins["fold_slack_delta"] = margins.get("fold_slack_delta", 0.0) + 0.015
    return margins


def update_session_memory(state: dict, table: dict) -> None:
    """Call after each hero action submission with latest table snapshot."""
    mem = state.setdefault("session_villain_memory", {})
    hero = _hero_seat(table)
    if hero is None:
        return
    for aid, _amt, seat in _street_bets(table):
        if seat == hero:
            continue
        rec = mem.setdefault(
            aid,
            {"aggressive_acts": 0, "passive_acts": 0, "samples": 0, "showdowns": []},
        )
        rec["aggressive_acts"] = int(rec.get("aggressive_acts", 0)) + 1
        rec["samples"] = int(rec.get("samples", 0)) + 1
    agents = _seat_agent_map(table)
    events = table.get("actionHistory") or table.get("actions") or []
    street = (table.get("street") or "").lower()
    for ev in events:
        if not isinstance(ev, dict):
            continue
        if street and (ev.get("street") or "").lower() not in ("", street):
            continue
        act = (ev.get("action") or ev.get("type") or "").lower()
        if act not in ("check", "call"):
            continue
        seat = ev.get("seatNumber")
        if seat is None or int(seat) == hero:
            continue
        aid = agents.get(int(seat)) or ev.get("agentId")
        if not aid:
            continue
        rec = mem.setdefault(
            str(aid),
            {"aggressive_acts": 0, "passive_acts": 0, "samples": 0, "showdowns": []},
        )
        rec["passive_acts"] = int(rec.get("passive_acts", 0)) + 1
        rec["samples"] = int(rec.get("samples", 0)) + 1


def villain_memory_for_table(state: dict, table: dict) -> dict[str, Any]:
    """Return memory slice for active villains at this table."""
    if not _session_memory_enabled():
        return {"villains": {}, "note": "abstain — session memory disabled"}
    mem = state.get("session_villain_memory") or {}
    hero = _hero_seat(table)
    agents = _seat_agent_map(table)
    villains: dict[str, dict] = {}
    for seat, aid in agents.items():
        if hero is not None and seat == hero:
            continue
        rec = mem.get(aid)
        if not rec:
            continue
        samples = int(rec.get("samples", 0))
        sd = list(rec.get("showdowns") or [])
        sd_summary = _showdown_summary(sd)
        if samples < _MIN_SAMPLES:
            villains[aid] = {
                "label": "unknown",
                "samples": samples,
                "confidence": "low",
                "showdowns": sd_summary,
            }
            continue
        ag = int(rec.get("aggressive_acts", 0))
        total = max(1, ag + int(rec.get("passive_acts", 0)))
        aggr_rate = ag / total
        label = "aggro" if aggr_rate >= _AGGR_THRESHOLD else "passive"
        villains[aid] = {
            "label": label,
            "aggr_rate": round(aggr_rate, 2),
            "samples": samples,
            "confidence": "high" if samples >= 8 else "medium",
            "showdowns": sd_summary,
        }
    if not villains:
        return {"villains": {}, "note": "abstain — insufficient session samples"}
    return {"villains": villains}


def exploit_from_memory(villain_mem: dict[str, Any]) -> dict[str, float]:
    """Map session memory to margin deltas (neutral if abstaining)."""
    villains = villain_mem.get("villains") or {}
    if not villains:
        return {}
    labels = [v.get("label") for v in villains.values() if v.get("confidence") != "low"]
    margins: dict[str, float] = {}
    if labels:
        if labels.count("aggro") >= labels.count("passive"):
            margins = {"call_margin_delta": -0.02, "fold_slack_delta": 0.03}
        else:
            margins = {"bet_bar_delta": -0.02, "call_margin_delta": 0.02}
    sd_margins = _showdown_exploit_margins(villains)
    for key, delta in sd_margins.items():
        margins[key] = margins.get(key, 0.0) + delta
    return margins
