"""Lobby join pacing — slow table intake when qualification/lead protect is on."""
from __future__ import annotations

import os

DEFAULT_JOIN_RETRY_S = 60.0
DEFAULT_IN_QUEUE_RETRY_S = 180.0
DEFAULT_QUAL_JOIN_RETRY_S = 300.0  # 5 min — still seated, fewer new tables
DEFAULT_LEAD_JOIN_RETRY_S = 900.0  # 15 min — time game > chip game when safely ahead
DEFAULT_FIRST_JOIN_RETRY_S = 1800.0  # 30 min — rank #1: minimize new table intake
DEFAULT_LOW_STACK_JOIN_RETRY_S = 3600.0  # stack < buy-in — avoid 409 join loops
DEFAULT_PLAYGROUND_BUY_IN = 1000


def _env_float(name: str, default: float) -> float:
    raw = os.environ.get(name)
    if raw is None or raw == "":
        return default
    return float(raw)


def join_retry_seconds(
    *,
    first_protect: bool = False,
    lead_protect: bool,
    qual_protect: bool,
    in_queue_only: bool,
    hero_stack_chips: int | None = None,
    buy_in_chips: int | None = None,
    retry_multiplier: float = 1.0,
) -> float:
    """Seconds between join attempts when idle (no pending actions).

    First place uses the longest backoff; lead protect is next; qualification
    protect is moderate; otherwise use the default lobby cadence (or in-queue wait).
    When hero stack is below buy-in, use at least CEMINI_LOW_STACK_JOIN_RETRY_S.
    """
    if in_queue_only:
        base = _env_float("CEMINI_IN_QUEUE_RETRY_S", DEFAULT_IN_QUEUE_RETRY_S)
    elif first_protect:
        base = _env_float("CEMINI_FIRST_JOIN_RETRY_S", DEFAULT_FIRST_JOIN_RETRY_S)
    elif lead_protect:
        base = _env_float("CEMINI_LEAD_JOIN_RETRY_S", DEFAULT_LEAD_JOIN_RETRY_S)
    elif qual_protect:
        base = _env_float("CEMINI_QUAL_JOIN_RETRY_S", DEFAULT_QUAL_JOIN_RETRY_S)
    else:
        base = _env_float("CEMINI_JOIN_RETRY_S", DEFAULT_JOIN_RETRY_S)

    buy_in = buy_in_chips
    if buy_in is None:
        raw = os.environ.get("ARENA_PLAYGROUND_START_CHIPS")
        buy_in = int(raw) if raw else DEFAULT_PLAYGROUND_BUY_IN
    if hero_stack_chips is not None and hero_stack_chips < buy_in:
        low = _env_float("CEMINI_LOW_STACK_JOIN_RETRY_S", DEFAULT_LOW_STACK_JOIN_RETRY_S)
        return max(base, low) * max(retry_multiplier, 1.0)
    return base * max(retry_multiplier, 1.0)
