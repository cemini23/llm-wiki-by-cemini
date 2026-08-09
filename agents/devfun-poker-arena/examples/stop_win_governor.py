"""P2-4 session stop-win governor — default off, code + tests only.

CEMINI_STOP_WIN_MULT=0 default. When set >0 (e.g. 2.2) and a tournament session
holds chips >= start_stack * mult for CEMINI_STOP_WIN_HANDS=20 consecutive hands,
recommend slowing the join/retry cadence to 600s to bank variance. Default stays
0 on prod — no behavior change unless the operator opts in via env.
"""
from __future__ import annotations

import os

_STOP_WIN_SLOW_JOIN_SECONDS = 600


def stop_win_mult() -> float:
    """Return the configured stop-win multiplier; 0 = disabled."""
    raw = os.environ.get("CEMINI_STOP_WIN_MULT", "0").strip()
    try:
        return max(0.0, float(raw))
    except (TypeError, ValueError):
        return 0.0


def stop_win_hands() -> int:
    """Consecutive-hand threshold before a winning session slows joins."""
    raw = os.environ.get("CEMINI_STOP_WIN_HANDS", "20").strip()
    try:
        return max(1, int(raw))
    except (TypeError, ValueError):
        return 20


def stop_win_slow_join(
    *,
    hand_count: int,
    current_stack: int,
    start_stack: int,
    mult: float | None = None,
    hands: int | None = None,
) -> tuple[bool, int] | None:
    """Pure decision: (slow_join=True, retry_seconds) or None when not triggered.

    Enabled only when the configured multiplier is >0. Requires at least `hands`
    consecutive played hands AND chips held at or above start_stack * mult.
    """
    if mult is None:
        mult = stop_win_mult()
    if hands is None:
        hands = stop_win_hands()
    if mult <= 0:
        return None
    if hand_count < hands:
        return None
    if start_stack > 0 and current_stack < int(start_stack * mult):
        return None
    return True, _STOP_WIN_SLOW_JOIN_SECONDS
