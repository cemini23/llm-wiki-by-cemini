"""Anti-collusion guards for jackpot probe fleet.

Probes must not share tables with the qualification bot or each other while
Playground anti-cheat is active. Default: no lobby join until operator enables.
"""
from __future__ import annotations

import os
from typing import Iterable


def join_enabled() -> bool:
    return os.environ.get("JACKPOT_27_JOIN_ENABLED", "0").strip().lower() in (
        "1",
        "true",
        "yes",
    )


def _blocked_agent_ids() -> frozenset[str]:
    raw = os.environ.get(
        "JACKPOT_27_BLOCKED_AGENT_IDS",
        os.environ.get("CEMINI_QUAL_AGENT_ID", "cmpy4lcyi001y11vnekn1zlo3"),
    )
    return frozenset(x.strip() for x in raw.split(",") if x.strip())


def _fleet_handle_prefixes() -> tuple[str, ...]:
    raw = os.environ.get("JACKPOT_27_FLEET_HANDLE_PREFIX", "arena_probe,cemini_wiki")
    return tuple(p.strip().lower() for p in raw.split(",") if p.strip())


def table_has_blocked_agent(table: dict, *, self_agent_id: str = "") -> bool:
    """True when another seat is our qual bot, a sibling probe, or blocked id."""
    blocked = _blocked_agent_ids()
    prefixes = _fleet_handle_prefixes()
    hero = table.get("selfSeatNumber")
    for seat in table.get("seats") or []:
        if seat.get("seatNumber") == hero:
            continue
        aid = str(seat.get("agentId") or "")
        if self_agent_id and aid == self_agent_id:
            continue
        if aid and aid in blocked:
            return True
        handle = (
            seat.get("agentHandle")
            or seat.get("agentName")
            or seat.get("agentId")
            or ""
        ).lower()
        if any(handle.startswith(p) for p in prefixes):
            return True
    return False


def sibling_seat_labels(table: dict, *, self_agent_id: str = "") -> list[str]:
    """Human-readable labels for blocked seats (logging)."""
    blocked = _blocked_agent_ids()
    prefixes = _fleet_handle_prefixes()
    hero = table.get("selfSeatNumber")
    out: list[str] = []
    for seat in table.get("seats") or []:
        if seat.get("seatNumber") == hero:
            continue
        aid = str(seat.get("agentId") or "")
        if self_agent_id and aid == self_agent_id:
            continue
        handle = seat.get("agentHandle") or seat.get("agentName") or aid
        handle_l = str(handle).lower()
        if (aid and aid in blocked) or any(handle_l.startswith(p) for p in prefixes):
            out.append(str(handle or aid))
    return out
