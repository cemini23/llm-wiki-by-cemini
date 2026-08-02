"""Halloran-class TAG widen — VPIP/PFR lift without gin.

v2: BB/SB defend must beat hard-coded broadway auto-folds and the
facing-raise chart raise→fold downgrade (those kept VPIP ~8% after v1).
"""
from __future__ import annotations

import os
from typing import Any


def tag_widen_enabled() -> bool:
    raw = os.environ.get("CEMINI_TAG_WIDEN", "0")
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

# SB vs open — tighter than BB (OOP); still wider than nemesis-premium-only.
TAG_SB_DEFEND = frozenset({
    "AA", "KK", "QQ", "JJ", "TT", "99", "88", "77",
    "AKs", "AKo", "AQs", "AQo", "AJs", "AJo", "ATs",
    "KQs", "KQo", "KJs", "QJs",
})

TAG_SB_OPEN_EXTRA = frozenset({
    "77", "66", "55", "44",
    "AJo", "ATs", "A9s", "A5s", "A4s",
    "KQo", "KJs", "KTs", "QTs", "QJs", "JTs", "T9s", "98s", "87s",
})

TAG_MP_OPEN_EXTRA = frozenset({
    "66", "55", "ATs", "A9s", "KQo", "KTs", "QTs", "JTs", "T9s",
})

TAG_CO_OPEN_EXTRA = frozenset({
    "44", "33", "22", "A4s", "A3s", "A2s", "K9s", "Q9s", "J9s", "T8s", "87s", "76s",
})


def tag_bb_defend_hand(hand_class: str) -> bool:
    return bool(hand_class) and hand_class in TAG_BB_CALL


def tag_sb_defend_hand(hand_class: str) -> bool:
    return bool(hand_class) and hand_class in TAG_SB_DEFEND


def tag_skip_broadway_auto_fold(hand_class: str, position: str) -> bool:
    """Bypass _BB_BROADWAY_FOLD auto-folds for TAG defend hands."""
    if not tag_widen_enabled() or not hand_class:
        return False
    if position == "BB":
        return hand_class in TAG_BB_CALL
    if position == "SB":
        return hand_class in TAG_SB_DEFEND
    return False


def tag_facing_raise_to_call(hand_class: str, position: str) -> bool:
    """Chart said raise but not 3bet-ok — defend as call instead of fold."""
    if not tag_widen_enabled() or not hand_class:
        return False
    if position == "BB":
        return hand_class in TAG_BB_CALL
    if position == "SB":
        return hand_class in TAG_SB_DEFEND
    return False


def try_tag_bb_sb_defend(
    *,
    hand_class: str,
    position: str,
    call_chips: int,
    big_blind: int,
    available: list,
    hero_stack_chips: int,
) -> tuple[str, None] | None:
    """Steal-sized BB/SB defend — no equity gate (chart set already filtered)."""
    if not tag_widen_enabled():
        return None
    if call_chips <= 0 or "call" not in available:
        return None
    bb = max(int(big_blind or 2), 1)
    # Steal / small open only — not facing 5x+ bombs
    if call_chips > bb * 3.5:
        return None
    if call_chips > hero_stack_chips * 0.28:
        return None
    if position == "BB" and hand_class in TAG_BB_CALL:
        return "call", None
    if position == "SB" and hand_class in TAG_SB_DEFEND:
        return "call", None
    return None
