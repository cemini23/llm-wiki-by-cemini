"""Halloran-class TAG widen — VPIP/PFR lift without gin.

v2: BB/SB defend before broadway auto-folds / raise→fold downgrade.
v3: SB-facing-raise is the VPIP bottleneck (nearly all SB spots) — widen
steal-sized SB defend set and raise size cap; keep trash folds.
"""
from __future__ import annotations

import os
from typing import Any


def tag_widen_enabled() -> bool:
    raw = os.environ.get("CEMINI_TAG_WIDEN", "0")
    return raw.strip().lower() in ("1", "true", "yes", "on")


def tag_sb_unopened_steal(hand_class: str, position: str = "SB") -> bool:
    """Playground unopened SB steal — chart extras + QJo-class.

    Chart already marks TAG_SB_OPEN_EXTRA as raise; decide used to fold them
    as SB trash before the open landed (P13 SB raise 15.6%). Include extras
    here so the first-in path fires. Off when TAG_WIDEN=0 (tournament freeze).
    """
    if position != "SB" or not hand_class:
        return False
    if not tag_widen_enabled():
        return False
    return hand_class in TAG_SB_STEAL_OPEN or hand_class in TAG_SB_OPEN_EXTRA


def cheap_priced_continue(
    *,
    equity: float,
    pot_odds: float,
    call_chips: int,
    pot: int,
    stack_chips: int = 0,
) -> bool:
    """Playground-only: skip texture folds when vs-random equity still covers.

    `estimate_equity` is MC vs 1 random opponent (overstates vs a betting
    range). Require high vs-random equity + a cheap price so a ~15pp haircut
    still calls. Off when TAG_WIDEN=0 (tournament freeze). Does not cover
    committed pots (stack-off / overbet).
    """
    if not tag_widen_enabled():
        return False
    if call_chips <= 0 or pot < 0:
        return False
    try:
        eq = float(equity)
        po = float(pot_odds)
    except (TypeError, ValueError):
        return False
    if eq < 0.55 or eq < po + 0.12:
        return False
    if call_chips > max(int(pot * 0.45), 1):
        return False
    if stack_chips > 0 and call_chips > max(int(stack_chips * 0.08), 1):
        return False
    return True


def tag_blind_defend_enabled() -> bool:
    """Tournament-only BB/SB defend lane — independent of full CEMINI_TAG_WIDEN."""
    raw = os.environ.get("CEMINI_TAG_BLIND_DEFEND", "0")
    return raw.strip().lower() in ("1", "true", "yes", "on")


def tag_widen_margins() -> dict[str, float]:
    """Stronger than v1, still below gin-era −0.04 spew."""
    return {
        "preflop_fold_margin_delta": -0.04,
        "fold_slack_delta": -0.025,
        "call_margin_delta": -0.035,
        "open_steal_equity": 0.40,
    }


def tag_widen_allowed(
    *,
    short_stack: bool = False,
    qual_protect: bool = False,
    lead_protect: bool = False,
    first_protect: bool = False,
) -> bool:
    """Never widen under protect / short-stack (T10 lesson)."""
    if not tag_widen_enabled():
        return False
    if short_stack or qual_protect or lead_protect or first_protect:
        return False
    return True


def apply_tag_widen_margins(
    margins: dict[str, Any],
    *,
    short_stack: bool = False,
    qual_protect: bool = False,
    lead_protect: bool = False,
    first_protect: bool = False,
) -> dict[str, Any]:
    if not tag_widen_allowed(
        short_stack=short_stack,
        qual_protect=qual_protect,
        lead_protect=lead_protect,
        first_protect=first_protect,
    ):
        return margins
    out = dict(margins)
    for key, delta in tag_widen_margins().items():
        if key in ("open_steal_equity", "chase_open_equity"):
            try:
                cur = float(out.get(key, 0.99))
            except (TypeError, ValueError):
                cur = 0.99
            out[key] = min(cur, float(delta))
        else:
            try:
                out[key] = float(out.get(key, 0.0)) + float(delta)
            except (TypeError, ValueError):
                out[key] = float(delta)
    return out


# 6-max BB defend — includes broadways that _BB_BROADWAY_FOLD would otherwise kill.
TAG_BB_CALL = frozenset({
    "AA", "KK", "QQ", "JJ", "TT", "99", "88", "77", "66", "55", "44", "33", "22",
    "AKs", "AKo", "AQs", "AQo", "AJs", "AJo", "ATs", "ATo", "A9s", "A8s", "A7s",
    "A5s", "A4s", "A3s", "A2s",
    "KQs", "KQo", "KJs", "KJo", "KTs", "KTo", "K9s",
    "QJs", "QJo", "QTs", "QTo", "Q9s", "JTs", "JTo", "J9s", "T9s", "T8s",
    "98s", "97s", "87s", "76s", "65s", "54s",
})

TAG_BB_3BET = frozenset({
    "AA", "KK", "QQ", "JJ", "TT", "AKs", "AKo", "AQs", "AQo", "AJs", "KQs",
})

# SB vs open (v3) — still tighter than BB; covers halloran-class blind defense.
# Excludes pure trash (72o/T5o) that correctly fold in live logs.
TAG_SB_DEFEND = frozenset({
    "AA", "KK", "QQ", "JJ", "TT", "99", "88", "77", "66", "55", "44", "33", "22",
    "AKs", "AKo", "AQs", "AQo", "AJs", "AJo", "ATs", "ATo", "A9s", "A8s", "A5s", "A4s",
    "KQs", "KQo", "KJs", "KJo", "KTs", "K9s",
    "QJs", "QJo", "QTs", "Q9s", "JTs", "JTo", "J9s", "T9s", "T8s",
    "98s", "97s", "87s", "86s", "76s", "65s", "54s",
})

TAG_SB_OPEN_EXTRA = frozenset({
    "77", "66", "55", "44", "33",
    "AJo", "ATs", "A9s", "A5s", "A4s",
    "KQo", "KJs", "KTs", "QTs", "QJs", "JTs", "T9s", "98s", "87s", "76s",
})

# Mild unopened SB steal (P13 P1) — QJo-class only. Not gin. Off when TAG_WIDEN=0.
# Combined with TAG_SB_OPEN_EXTRA in tag_sb_unopened_steal (S14 climb).
TAG_SB_STEAL_OPEN = frozenset({
    "QJo", "KJo", "ATo", "KTo",
})

# P13 P2 stalled-climb: value 3bet from blinds vs steal-sized opens. Not polar.
TAG_VALUE_3BET = frozenset({
    "AA", "KK", "QQ", "AKs", "AKo",
})

TAG_MP_OPEN_EXTRA = frozenset({
    "66", "55", "ATs", "A9s", "KQo", "KTs", "QTs", "JTs", "T9s",
})

TAG_CO_OPEN_EXTRA = frozenset({
    "44", "33", "22", "A4s", "A3s", "A2s", "K9s", "Q9s", "J9s", "T8s", "87s", "76s",
})

# Steal-size cap in BBs (v2 was 3.5 — missed many 3–4x opens).
_TAG_DEFEND_MAX_BB = 4.5
_TAG_DEFEND_MAX_STACK_FRAC = 0.32

# Tournament blind-defend lane: tighter than playground TAG widen.
_BLIND_DEFEND_MAX_BB = 3.0
_BLIND_DEFEND_MAX_STACK_FRAC = 0.10

# P1-5: blind-defend initiative — 3bet (not flat) with these vs ≤3bb opens.
_BLIND_DEFEND_3BET = frozenset({
    "JJ", "QQ", "KK", "AA", "AKs", "AKo", "AQs",
})

# Sensible BB/SB defend vs ≤3bb open — broadway, pairs, suited connectors.
# SB excludes QJo (open-only under placement_chase; no cold-call spew).
TAG_BLIND_DEFEND_BB = frozenset({
    "AA", "KK", "QQ", "JJ", "TT", "99", "88", "77", "66", "55", "44", "33", "22",
    "AKs", "AKo", "AQs", "AQo", "AJs", "AJo", "ATs", "ATo", "A9s", "A8s", "A5s", "A4s",
    "KQs", "KQo", "KJs", "KJo", "KTs", "KTo", "K9s",
    "QJs", "QJo", "QTs", "QTo", "Q9s", "JTs", "JTo", "J9s", "T9s", "T8s",
    "98s", "97s", "87s", "76s", "65s", "54s",
})

TAG_BLIND_DEFEND_SB = frozenset({
    "AA", "KK", "QQ", "JJ", "TT", "99", "88", "77", "66", "55", "44", "33", "22",
    "AKs", "AKo", "AQs", "AQo", "AJs", "AJo", "ATs", "ATo", "A9s", "A8s", "A5s", "A4s",
    "KQs", "KQo", "KJs", "KJo", "KTs", "K9s",
    "QJs", "QTs", "Q9s", "JTs", "J9s", "T9s", "T8s",
    "98s", "97s", "87s", "76s", "65s", "54s",
})


def tag_bb_defend_hand(hand_class: str) -> bool:
    if not hand_class:
        return False
    if hand_class in TAG_BB_CALL:
        return True
    if tag_blind_defend_enabled() and hand_class in TAG_BLIND_DEFEND_BB:
        return True
    return False


def tag_sb_defend_hand(hand_class: str) -> bool:
    if not hand_class:
        return False
    if hand_class in TAG_SB_DEFEND:
        return True
    if tag_blind_defend_enabled() and hand_class in TAG_BLIND_DEFEND_SB:
        return True
    return False


def tag_skip_broadway_auto_fold(hand_class: str, position: str) -> bool:
    """Bypass _BB_BROADWAY_FOLD auto-folds for TAG / blind-defend hands."""
    if not hand_class:
        return False
    if not (tag_widen_enabled() or tag_blind_defend_enabled()):
        return False
    if position == "BB":
        if tag_widen_enabled() and hand_class in TAG_BB_CALL:
            return True
        if tag_blind_defend_enabled() and hand_class in TAG_BLIND_DEFEND_BB:
            return True
        return False
    if position == "SB":
        if tag_widen_enabled() and hand_class in TAG_SB_DEFEND:
            return True
        if tag_blind_defend_enabled() and hand_class in TAG_BLIND_DEFEND_SB:
            return True
        return False
    return False


def tag_facing_raise_to_call(hand_class: str, position: str) -> bool:
    """Chart said raise but not 3bet-ok — defend as call instead of fold."""
    if not hand_class:
        return False
    if not (tag_widen_enabled() or tag_blind_defend_enabled()):
        return False
    if position == "BB":
        if tag_widen_enabled() and hand_class in TAG_BB_CALL:
            return True
        if tag_blind_defend_enabled() and hand_class in TAG_BLIND_DEFEND_BB:
            return True
        return False
    if position == "SB":
        if tag_widen_enabled() and hand_class in TAG_SB_DEFEND:
            return True
        if tag_blind_defend_enabled() and hand_class in TAG_BLIND_DEFEND_SB:
            return True
        return False
    return False


def try_tag_bb_sb_defend(
    *,
    hand_class: str,
    position: str,
    call_chips: int,
    big_blind: int,
    available: list,
    hero_stack_chips: int,
    allowed: dict | None = None,
) -> tuple[str, int | None] | None:
    """Steal-sized BB/SB defend — no equity gate (chart set already filtered).

    P13 P2: QQ+/AK 3bet vs steal-sized opens when a raise is legal (playground
    TAG only). Still flats the rest of TAG_BB_CALL / TAG_SB_DEFEND.
    """
    if not tag_widen_enabled():
        return None
    if call_chips <= 0 or "call" not in available:
        return None
    bb = max(int(big_blind or 2), 1)
    if call_chips > bb * _TAG_DEFEND_MAX_BB:
        return None
    if call_chips > hero_stack_chips * _TAG_DEFEND_MAX_STACK_FRAC:
        return None
    if (
        hand_class in TAG_VALUE_3BET
        and position in ("BB", "SB")
        and "raise" in available
        and hero_stack_chips >= bb * 15
    ):
        rr = (allowed or {}).get("raiseRange") or {}
        min_r = int(rr.get("min") or call_chips * 2)
        max_r = int(rr.get("max") or min_r)
        target = max(min_r, min(int(call_chips * 2 + bb), max_r))
        if target <= int(hero_stack_chips * 0.35):
            return "raise", target
    if position == "BB" and hand_class in TAG_BB_CALL:
        return "call", None
    if position == "SB" and hand_class in TAG_SB_DEFEND:
        return "call", None
    return None


def try_tag_blind_defend(
    *,
    hand_class: str,
    position: str,
    call_chips: int,
    big_blind: int,
    available: list,
    hero_stack_chips: int,
    allowed: dict | None = None,
) -> tuple[str, int | None] | None:
    """Tournament BB/SB defend vs ≤3bb open / ≤10% stack — no full TAG_WIDEN needed.

    P1-5: with JJ+/AK/AQs and ≥15bb stack, 3bet (raise) instead of flat-call
    when a raise is available and the sizing stays ≤35% of stack.
    """
    if not tag_blind_defend_enabled():
        return None
    if call_chips <= 0 or "call" not in available:
        return None
    if position not in ("BB", "SB"):
        return None
    bb = max(int(big_blind or 2), 1)
    if call_chips > bb * _BLIND_DEFEND_MAX_BB:
        return None
    if hero_stack_chips > 0 and call_chips > hero_stack_chips * _BLIND_DEFEND_MAX_STACK_FRAC:
        return None
    if hand_class in _BLIND_DEFEND_3BET and hero_stack_chips >= bb * 15:
        if "raise" in available:
            rr = (allowed or {}).get("raiseRange") or {}
            min_r = int(rr.get("min") or call_chips * 2)
            max_r = int(rr.get("max") or min_r)
            target = max(min_r, min(int(call_chips * 2 + bb), max_r))
            if target <= int(hero_stack_chips * 0.35):
                return "raise", target
    if position == "BB" and hand_class in TAG_BLIND_DEFEND_BB:
        return "call", None
    if position == "SB" and hand_class in TAG_BLIND_DEFEND_SB:
        return "call", None
    return None
