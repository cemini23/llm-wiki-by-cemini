"""Tournament S12 3bet tier — value 3bet (P1-2) + thin IP polar bluff slice (P2-1).

Both gated by env knobs set in the s12 tournament posture. No gin involved.
"""
from __future__ import annotations

import os
from typing import Optional

# P1-2 value set — prefer 3bet over call vs ≤3.5bb raises IP/BB with >12bb stack.
_TOURNAMENT_3BET_VALUE = frozenset({
    "AA", "KK", "QQ", "JJ", "TT", "AKs", "AKo", "AQs", "AJs", "KQs",
})

# P2-1 thin IP bluff 3bet slice — only vs CO/BTN opens, small size, fold to 4bet.
_POLAR_IP_3BET = frozenset({
    "A2s", "A3s", "A4s", "A5s", "K9s", "KTs",
})


def tournament_3bet_enabled() -> bool:
    raw = os.environ.get("CEMINI_TOURNAMENT_3BET", "0")
    return raw.strip().lower() in ("1", "true", "yes", "on")


def tournament_3bet_polar_enabled() -> bool:
    raw = os.environ.get("CEMINI_TOURNAMENT_3BET_POLAR", "0")
    return raw.strip().lower() in ("1", "true", "yes", "on")


def _raise_to(allowed: dict, available: list, *, pot: int, mult: float) -> tuple[str, int] | None:
    if allowed.get("canRaise") and "raise" in available:
        rr = allowed.get("raiseRange") or {}
        min_r = int(rr.get("min") or max(int(pot * 0.5), 1))
        max_r = int(rr.get("max") or min_r)
        target = max(min_r, min(int(pot * mult), max_r))
        return "raise", target
    if allowed.get("canBet") and "bet" in available:
        br = allowed.get("betRange") or {}
        min_b = int(br.get("min") or max(int(pot * 0.5), 1))
        max_b = int(br.get("max") or min_b)
        target = max(min_b, min(int(pot * mult), max_b))
        return "bet", target
    return None


def preflop_opener_position(table: dict) -> str:
    """Position label of the non-hero seat with the largest preflop bet ('' if none)."""
    if not table:
        return ""
    hero = table.get("selfSeatNumber")
    best_bet = -1
    best_pos = ""
    for seat in table.get("seats") or []:
        sn = seat.get("seatNumber")
        if sn == hero:
            continue
        try:
            bet = int(seat.get("currentBetChips") or 0)
        except (TypeError, ValueError):
            bet = 0
        if bet > best_bet:
            best_bet = bet
            best_pos = seat.get("position") or ""
    return best_pos


def try_tournament_value_3bet(
    *,
    hand_class: str,
    position: str,
    in_position: bool,
    call_chips: int,
    pot: int,
    allowed: dict,
    available: list,
    hero_stack_chips: int,
    big_blind: int,
) -> tuple[str, int | None] | None:
    """P1-2: value 3bet vs ≤3.5bb raise IP/BB with >12bb stack.

    Set {QQ+, AK, AQs, AJs, KQs, JJ, TT}; prefer 3bet over call; cap total
    3bet at 35% of stack; no polar bluffs here (those are P2-1).
    """
    if not tournament_3bet_enabled():
        return None
    if call_chips <= 0:
        return None
    if hand_class not in _TOURNAMENT_3BET_VALUE:
        return None
    if not (in_position or position == "BB"):
        return None
    bb = max(int(big_blind or 2), 1)
    if call_chips > bb * 3.5:
        return None
    if hero_stack_chips <= bb * 12:
        return None
    max_raise = int(hero_stack_chips * 0.35)
    if call_chips > max_raise:
        return None
    if "bet" not in available and "raise" not in available:
        return None
    mult = 2.6 if call_chips <= bb * 3 else 2.3
    out = _raise_to(allowed, available, pot=pot, mult=mult)
    if out and out[1] is not None and out[1] <= max_raise:
        return out
    return None


def try_tournament_polar_3bet(
    *,
    hand_class: str,
    position: str,
    in_position: bool,
    call_chips: int,
    pot: int,
    allowed: dict,
    available: list,
    hero_stack_chips: int,
    big_blind: int,
    opener_position: str = "",
) -> tuple[str, int | None] | None:
    """P2-1: thin IP polar 3bet bluff slice vs CO/BTN opens only.

    Small size, capped at 25% stack; fold-to-4bet is handled by the caller's
    existing weak-hand fold logic on the next facing-bet. Default off in prod.
    """
    if not tournament_3bet_polar_enabled():
        return None
    if call_chips <= 0:
        return None
    if hand_class not in _POLAR_IP_3BET:
        return None
    if not in_position or position not in ("BTN", "CO"):
        return None
    if opener_position and opener_position not in ("CO", "BTN"):
        return None
    bb = max(int(big_blind or 2), 1)
    if call_chips > bb * 3.5:
        return None
    if hero_stack_chips <= bb * 12:
        return None
    max_raise = int(hero_stack_chips * 0.25)
    if call_chips > max_raise:
        return None
    if "bet" not in available and "raise" not in available:
        return None
    mult = 2.4 if call_chips <= bb * 2.5 else 2.2
    out = _raise_to(allowed, available, pot=pot, mult=mult)
    if out and out[1] is not None and out[1] <= max_raise:
        return out
    return None
