"""Halloran-class TAG widen — mild VPIP/PFR lift without gin.

Playground nit (~9–12% VPIP) cannot climb chip-qual. This module applies
bounded preflop/postflop margin deltas and optional chart defend overlays.
Gin / V008 / V2 remain hard-killed elsewhere.
"""
from __future__ import annotations

import os
from typing import Any


def tag_widen_enabled() -> bool:
    raw = os.environ.get("CEMINI_TAG_WIDEN", "0")
    return raw.strip().lower() in ("1", "true", "yes", "on")


def tag_widen_margins() -> dict[str, float]:
    """Mild TAG deltas — not gin-era −0.04 spew."""
    return {
        "preflop_fold_margin_delta": -0.025,
        "fold_slack_delta": -0.015,
        "call_margin_delta": -0.02,
        # Absolute: unlock selective CO/BTN steals vs rock / loose-passive HUD
        "open_steal_equity": 0.44,
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
            # Prefer lower steal bar (easier open) but do not raise an already-low bar
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


# 6-max BB defend overlay — base chart has empty BB call set (VPIP killer).
TAG_BB_CALL = frozenset({
    "AA", "KK", "QQ", "JJ", "TT", "99", "88", "77", "66", "55", "44", "33", "22",
    "AKs", "AKo", "AQs", "AQo", "AJs", "AJo", "ATs", "ATo", "A9s", "A8s", "A7s",
    "A5s", "A4s", "A3s", "A2s",
    "KQs", "KQo", "KJs", "KJo", "KTs", "K9s",
    "QJs", "QJo", "QTs", "Q9s", "JTs", "J9s", "T9s", "98s", "87s", "76s", "65s",
})

TAG_BB_3BET = frozenset({
    "AA", "KK", "QQ", "JJ", "TT", "AKs", "AKo", "AQs", "AQo", "AJs", "KQs",
})

TAG_SB_OPEN_EXTRA = frozenset({
    "77", "66", "55", "AJo", "ATs", "A9s", "A5s", "KQo", "KTs", "QTs", "JTs", "T9s", "98s",
})
