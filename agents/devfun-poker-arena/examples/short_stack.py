"""Short-stack push/fold — overrides chase/gin widen when shallow.

Post-mortem T10 2026-08-01: gin+chase at ~154 chips spewed the stack.
When hero stack < CEMINI_SHORT_STACK_BB (default 12), play push/fold only.

P1-3: two bands under the short-stack threshold —
  ≤ CEMINI_SHORT_STACK_JAM_BB (default 8):  jam-or-fold only (push chart)
  8–12bb: selective raise/jam — premiums + suited broadway; fold trash opens
  ≥ CEMINI_SHORT_STACK_BB: not the short-stack path
"""
from __future__ import annotations

import os
from typing import Optional


def short_stack_bb_threshold() -> float:
    raw = os.environ.get("CEMINI_SHORT_STACK_BB", "20")
    try:
        return max(0.0, float(raw))
    except ValueError:
        return 20.0


def short_stack_jam_bb_threshold() -> float:
    """Boundary for the ≤8bb jam-or-fold band (default 8)."""
    raw = os.environ.get("CEMINI_SHORT_STACK_JAM_BB", "8")
    try:
        return max(0.0, float(raw))
    except ValueError:
        return 8.0


def hero_stack_bb(table: dict, self_seat: dict | None = None) -> float:
    bb = float(table.get("bigBlind") or table.get("bb") or table.get("bigBlindChips") or 20)
    if bb <= 0:
        bb = 20.0
    chips = None
    if self_seat is not None:
        chips = self_seat.get("stackChips") or self_seat.get("chips")
    if chips is None:
        hero = table.get("selfSeatNumber")
        for seat in table.get("seats") or []:
            if seat.get("seatNumber") == hero:
                chips = seat.get("stackChips") or seat.get("chips")
                break
    try:
        return float(chips or 0) / bb
    except (TypeError, ValueError):
        return 99.0


def is_short_stack(table: dict, self_seat: dict | None = None) -> bool:
    thr = short_stack_bb_threshold()
    if thr <= 0:
        return False
    return hero_stack_bb(table, self_seat) < thr


# Any-two jams when ultra-short; tighten as stack deepens within short band.
_PUSH_ANY = frozenset()  # unused sentinel

_PUSH_BTN = frozenset({
    "22", "33", "44", "55", "66", "77", "88", "99", "TT", "JJ", "QQ", "KK", "AA",
    "A2s", "A3s", "A4s", "A5s", "A6s", "A7s", "A8s", "A9s", "ATs", "AJs", "AQs", "AKs",
    "A2o", "A3o", "A4o", "A5o", "A7o", "A8o", "A9o", "ATo", "AJo", "AQo", "AKo",
    "K9s", "KTs", "KJs", "KQs", "KTo", "KJo", "KQo",
    "Q9s", "QTs", "QJs", "QJo", "J9s", "JTs", "T9s", "98s", "87s", "76s", "65s",
})

_PUSH_CO = frozenset({
    "22", "33", "44", "55", "66", "77", "88", "99", "TT", "JJ", "QQ", "KK", "AA",
    "A2s", "A3s", "A4s", "A5s", "A7s", "A8s", "A9s", "ATs", "AJs", "AQs", "AKs",
    "A9o", "ATo", "AJo", "AQo", "AKo",
    "K9s", "KTs", "KJs", "KQs", "KJo", "KQo",
    "QTs", "QJs", "JTs", "T9s", "98s", "87s",
})

_PUSH_MP = frozenset({
    "55", "66", "77", "88", "99", "TT", "JJ", "QQ", "KK", "AA",
    "A9s", "ATs", "AJs", "AQs", "AKs", "AJo", "AQo", "AKo",
    "KTs", "KJs", "KQs", "QJs", "JTs",
})

_PUSH_UTG = frozenset({
    "77", "88", "99", "TT", "JJ", "QQ", "KK", "AA",
    "ATs", "AJs", "AQs", "AKs", "AQo", "AKo",
    "KQs", "KJs",
})

_PUSH_SB = _PUSH_BTN | frozenset({"K8s", "Q8s", "J8s", "T8s", "97s", "86s", "A6o"})

_PUSH_BB_CALL = frozenset({
    "22", "33", "44", "55", "66", "77", "88", "99", "TT", "JJ", "QQ", "KK", "AA",
    "A2s", "A3s", "A4s", "A5s", "A7s", "A8s", "A9s", "ATs", "AJs", "AQs", "AKs",
    "A9o", "ATo", "AJo", "AQo", "AKo",
    "K9s", "KTs", "KJs", "KQs", "QTs", "QJs", "JTs", "T9s", "98s",
})


# P1-3 8–12bb selective band — premiums + suited broadway only (fold trash opens).
_SELECTIVE_JAM = frozenset({
    "AA", "KK", "QQ", "JJ", "TT", "99", "88", "77",
    "AKs", "AKo", "AQs", "AQo", "AJs", "ATs", "A9s", "A5s", "A4s",
    "KQs", "KJs", "KTs", "QJs", "QTs", "JTs", "T9s",
})


def _selective_band_hand(hand_class: str) -> bool:
    return (hand_class or "").strip() in _SELECTIVE_JAM


def push_hand_ok(hand_class: str, position: str) -> bool:
    hc = (hand_class or "").strip()
    pos = (position or "").upper()
    if pos == "BTN":
        return hc in _PUSH_BTN
    if pos == "CO":
        return hc in _PUSH_CO
    if pos == "MP":
        return hc in _PUSH_MP
    if pos == "UTG":
        return hc in _PUSH_UTG
    if pos == "SB":
        return hc in _PUSH_SB
    if pos == "BB":
        return hc in _PUSH_BB_CALL
    return hc in _PUSH_MP


def short_stack_preflop_action(
    *,
    hand_class: str,
    position: str,
    available: list[str],
    allowed: dict,
    call_chips: int,
    stack_chips: int,
    stack_bb: Optional[float] = None,
) -> Optional[tuple[str, Optional[int]]]:
    """Return (action, amount) for short-stack preflop, or None to defer.

    ``stack_bb`` selects the band: ≤8bb (or None) uses the push chart;
    8–12bb uses the tighter selective jam set.
    """
    jam_ok = push_hand_ok(hand_class, position)
    # P15: 77 UTG open-jam after the lock blinded us down. EP 77 is a fold
    # unopened; still jam/call if already facing a raise in the ≤8bb band.
    if (
        (position or "").upper() == "UTG"
        and (hand_class or "").strip() == "77"
        and int(call_chips or 0) <= 0
    ):
        jam_ok = False
    if stack_bb is not None:
        try:
            stack_bb_f = float(stack_bb)
        except (TypeError, ValueError):
            stack_bb_f = 0.0
        if stack_bb_f > short_stack_jam_bb_threshold():
            jam_ok = _selective_band_hand(hand_class)
    can_raise = bool(allowed.get("canRaise")) and "raise" in available
    can_allin = "all-in" in available or bool(allowed.get("canAllIn"))
    can_call = bool(allowed.get("canCall")) and "call" in available
    can_check = bool(allowed.get("canCheck")) and "check" in available
    can_fold = "fold" in available

    # Facing a bet/raise: jam or fold (call only if all-in priced as call).
    if call_chips > 0:
        if jam_ok and (can_raise or can_allin):
            if can_allin and "all-in" in available:
                return "all-in", None
            if can_raise:
                return "raise", int(stack_chips)
        if jam_ok and can_call and call_chips >= max(1, int(stack_chips * 0.7)):
            return "call", None
        if can_fold:
            return "fold", None
        if can_check:
            return "check", None
        return "fold", None

    # Unopened / checked to us: jam opens only.
    if jam_ok and (can_raise or can_allin):
        if can_allin and "all-in" in available:
            return "all-in", None
        if can_raise:
            return "raise", int(stack_chips)
    if can_check:
        return "check", None
    if can_fold:
        return "fold", None
    return None
