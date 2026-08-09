"""P2-2 flat-dominate — prefer call over fold/3bet vs leader/nemesis opens IP/BB.

Gated by CEMINI_FLAT_DOMINATE=1 (s12 posture). Medium-strength continue-range
(AT+, KQ, 55–JJ, suited connectors) flattens vs known nemesis/leader opens
instead of over-folding, while value 3bet (P1-2) still takes priority.
"""
from __future__ import annotations

import os
from typing import Optional

_FLAT_DOMINATE_HANDS = frozenset({
    "ATs", "ATo", "AJs", "AJo", "AQs", "AQo", "AKs", "AKo",
    "KQo", "KQs", "KJs", "KTs",
    "55", "66", "77", "88", "99", "TT", "JJ",
    "JTs", "T9s", "98s", "87s", "76s", "65s",
})


def flat_dominate_enabled() -> bool:
    raw = os.environ.get("CEMINI_FLAT_DOMINATE", "0")
    return raw.strip().lower() in ("1", "true", "yes", "on")


def is_leader_nemesis_handle(handle: str) -> bool:
    """True when the opener handle is a seeded nemesis or nemesis-prefixed."""
    h = (handle or "").lower().strip()
    if not h:
        return False
    try:
        from nemesis_seed import nemesis_handles, nemesis_prefixes
        if h in nemesis_handles():
            return True
        return any(h.startswith(p) for p in nemesis_prefixes() if p)
    except Exception:
        return False


def try_flat_dominate_call(
    *,
    hand_class: str,
    position: str,
    in_position: bool,
    call_chips: int,
    big_blind: int,
    hero_stack_chips: int,
    available: list,
    villain_handle: str = "",
) -> tuple[str, None] | None:
    """Call (not fold/3bet) medium-strength hands vs leader/nemesis opens IP/BB."""
    if not flat_dominate_enabled():
        return None
    if call_chips <= 0 or "call" not in available:
        return None
    if hand_class not in _FLAT_DOMINATE_HANDS:
        return None
    if not (in_position or position == "BB"):
        return None
    if not is_leader_nemesis_handle(villain_handle):
        return None
    bb = max(int(big_blind or 2), 1)
    if call_chips > bb * 4:
        return None
    if hero_stack_chips > 0 and call_chips > hero_stack_chips * 0.20:
        return None
    return "call", None
