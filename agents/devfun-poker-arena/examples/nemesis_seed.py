"""Known nemesis handles — tight default vs repeat tablemates (S1a/S2 export intel)."""
from __future__ import annotations

import os

from villain_archetype import (  # noqa: E402
    archetype_toggles_enabled,
    dominant_villain_from_table,
    jeff_nemesis_handle,
    linear_aggro_exploit_on,
    phoenix_cluster_exploit_on,
    phoenix_cluster_handle,
    premium_nit_exploit_on,
    wide_passive_exploit_on,
)

_DEFAULT = (
    "hunterguy102",
    "thaddius",
    "v_16",
    "0xjeff_ai",
    "jagoan_neon",
)
_DEFAULT_PREFIXES = ("v12_", "phoenix-rises-nrkdhd", "phoenix-nrkdhd", "phoenix-")
# Linear-aggro nemesis — defend/3-bet IP; do not blanket-fold suited broadway (S1 export).
_LINEAR_AGGRO_NEMESIS = frozenset({
    "thaddius",
    "maxcaution",
    "bingbong",
    "vector_ai",
    "ed_209_charlie",
})


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


def linear_aggro_nemesis_handles() -> frozenset[str]:
    raw = os.environ.get("CEMINI_LINEAR_AGGRO_NEMESIS", "")
    if raw.strip():
        parts = (p.strip().lower() for p in raw.split(","))
        return frozenset(p for p in parts if p)
    return _LINEAR_AGGRO_NEMESIS


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


def table_nemesis_opener_handle(
    table: dict,
    handles: frozenset[str] | None = None,
) -> str:
    """Lowercase handle of the nemesis seat with the largest preflop bet, else ''."""
    if not handles:
        handles = nemesis_handles()
    prefixes = nemesis_prefixes()
    hero = table.get("selfSeatNumber")
    best_bet = -1
    best_handle = ""
    for seat in table.get("seats") or []:
        sn = seat.get("seatNumber")
        if sn == hero:
            continue
        if not _seat_is_nemesis(seat, handles, prefixes):
            continue
        bet = int(seat.get("currentBetChips") or 0)
        handle = (seat.get("agentHandle") or seat.get("agentName") or "").lower()
        if bet > best_bet:
            best_bet = bet
            best_handle = handle
    bb = int(table.get("bigBlindChips") or 20)
    if best_bet <= bb:
        return ""
    return best_handle


def table_archetype_nemesis(table: dict) -> bool:
    """True when dominant villain archetype has nemesis exploit enabled."""
    if not archetype_toggles_enabled():
        return False
    handle, stats, arch = dominant_villain_from_table(table)
    if not arch or arch == "unknown":
        return False
    if arch == "premium_nit" and premium_nit_exploit_on():
        return True
    if arch in ("wide_passive", "phoenix_passive") and wide_passive_exploit_on():
        return True
    if arch == "linear_aggro" and linear_aggro_exploit_on():
        return True
    if phoenix_cluster_handle(handle) and phoenix_cluster_exploit_on():
        return True
    if jeff_nemesis_handle(handle) and linear_aggro_exploit_on():
        return True
    return False


def table_nemesis_pressure(table: dict, handles: frozenset[str] | None = None) -> bool:
    """Named nemesis opener OR archetype nemesis (S2 audit consensus)."""
    if table_nemesis_opener(table, handles):
        return True
    return table_archetype_nemesis(table)
