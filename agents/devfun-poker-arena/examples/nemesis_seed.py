"""Known nemesis handles — tight default vs repeat tablemates (S1a export intel)."""
from __future__ import annotations

import os

_DEFAULT = ("hunterguy102", "thaddius")
_DEFAULT_PREFIXES = ("v12_",)


def nemesis_handles() -> frozenset[str]:
    raw = os.environ.get("CEMINI_NEMESIS_HANDLES", "")
    if raw.strip():
        parts = (p.strip().lower() for p in raw.split(","))
        return frozenset(p for p in parts if p)
    return frozenset(h.lower() for h in _DEFAULT)


def nemesis_prefixes() -> tuple[str, ...]:
    raw = os.environ.get("CEMINI_NEMESIS_PREFIXES", "v12_")
    if raw.strip():
        parts = (p.strip().lower() for p in raw.split(","))
        return tuple(p for p in parts if p)
    return _DEFAULT_PREFIXES


def _seat_is_nemesis(seat: dict, handles: frozenset[str], prefixes: tuple[str, ...]) -> bool:
    handle = (seat.get("agentHandle") or seat.get("agentName") or "").lower()
    aid = (seat.get("agentId") or "").lower()
    if handle in handles or aid in handles:
        return True
    return any(handle.startswith(p) for p in prefixes if handle)


def seed_nemesis_state(state: dict) -> None:
    """Persist nemesis list in lobby state for decide() context."""
    state["nemesis_handles"] = sorted(nemesis_handles())
    state["nemesis_prefixes"] = list(nemesis_prefixes())


def table_nemesis_opener(table: dict, handles: frozenset[str] | None = None) -> bool:
    """True when a seated nemesis has the largest preflop bet (likely opener)."""
    if not handles:
        handles = nemesis_handles()
    prefixes = nemesis_prefixes()
    if not handles and not prefixes:
        return False
    hero = table.get("selfSeatNumber")
    best_bet = -1
    best_is_nemesis = False
    for seat in table.get("seats") or []:
        sn = seat.get("seatNumber")
        if sn == hero:
            continue
        handle = (seat.get("agentHandle") or seat.get("agentName") or "").lower()
        aid = (seat.get("agentId") or "").lower()
        is_nem = _seat_is_nemesis(seat, handles, prefixes)
        bet = int(seat.get("currentBetChips") or 0)
        if bet > best_bet:
            best_bet = bet
            best_is_nemesis = is_nem
        elif bet == best_bet and bet > 0 and is_nem:
            best_is_nemesis = True
    return best_is_nemesis and best_bet > int(table.get("bigBlindChips") or 20)
