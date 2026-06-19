"""Table format detection for Researcher dual-readiness (HU vs 6-max)."""
from __future__ import annotations

import os
from typing import Literal

TableFormat = Literal["hu", "6max"]


def _env_table_format() -> str:
    return os.environ.get("CEMINI_TABLE_FORMAT", "auto").strip().lower()


def active_player_count(table: dict) -> int:
    seats = table.get("seats") or []
    n = 0
    for s in seats:
        if not isinstance(s, dict):
            continue
        status = (s.get("status") or "Active").lower()
        if status in ("folded", "out", "empty"):
            continue
        n += 1
    if n:
        return n
    max_p = table.get("maxPlayers")
    if max_p is not None:
        try:
            return int(max_p)
        except (TypeError, ValueError):
            pass
    return len(seats) or 6


def resolve_table_format(table: dict | None = None) -> TableFormat:
    """Resolve format from env + live table shape. `auto` → HU when ≤2 active seats."""
    raw = _env_table_format()
    if raw in ("hu", "heads-up", "headsup", "2max", "2-max"):
        return "hu"
    if raw in ("6max", "6-max", "six", "6"):
        return "6max"
    if table is not None:
        n = active_player_count(table)
        if n <= 2:
            return "hu"
    return "6max"


def researcher_mode_enabled() -> bool:
    return os.environ.get("CEMINI_RESEARCHER_MODE", "").strip().lower() in (
        "1", "true", "yes", "on",
    )
