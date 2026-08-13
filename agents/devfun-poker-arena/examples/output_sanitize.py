"""Strip strategy telegraphy from Arena action payloads (prod anti-profiling).

Sandbox static-agent bundles should set CEMINI_SANITIZE_OUTPUT=0 — Arena trajectory
rejects generic reasoning (docs.dev.fun researcher guide).
"""
from __future__ import annotations

import os
from typing import Any

from withhold_contract import check_outbound_action  # K276 withhold wire

GENERIC_MESSAGE = "act"
FALLBACK_REASONING = '{vr: "std", ke: "legal", pp: "pot control"}'

_ACTION_MESSAGES = {
    "fold": "fold",
    "check": "check",
    "call": "call",
    "bet": "bet",
    "raise": "raise",
    "all-in": "all-in",
}


def sanitize_output_enabled() -> bool:
    raw = os.environ.get("CEMINI_SANITIZE_OUTPUT", "")
    return raw.strip().lower() in ("1", "true", "yes", "on")


def maybe_sanitize_action(
    action: dict[str, Any],
    hole_cards: Any = None,
    hand_class: str = "",
) -> dict[str, Any]:
    """Return a copy with generic message/reasoning when sanitization is on.

    Optional K276 withhold pass: when ``hole_cards`` (decide-trusted) are
    provided, run the withhold contract over ``message`` / ``reasoning`` and
    revise leaked hole/hand tokens. Existing callers (no extra kwargs) are
    unchanged.
    """
    out = action
    if sanitize_output_enabled():
        out = dict(action)
        act = str(out.get("action") or "fold")
        out["message"] = _ACTION_MESSAGES.get(act, GENERIC_MESSAGE)[:500]
        out["reasoning"] = FALLBACK_REASONING
    if hole_cards:
        out = check_outbound_action(
            out,
            hole_cards=hole_cards,
            hand_class=hand_class,
        )
    return out
