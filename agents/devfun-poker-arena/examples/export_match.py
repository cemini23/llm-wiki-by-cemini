"""Resolve which competition an export/crawl job should target.

Playground enter sets CEMINI_EXPORT_MATCH + ARENA_LOBBY_COMPETITION_ID.
Legacy S1_TOURNAMENT_COMP must not win when those are set — that bug left
T10/S11 crawls stuck on an old S1 id.
"""
from __future__ import annotations

import os


def resolve_export_competition_id(cli_match: str | None = None) -> str:
    """Prefer explicit export match, then live lobby, then legacy S1."""
    for raw in (
        cli_match,
        os.environ.get("CEMINI_EXPORT_MATCH"),
        os.environ.get("ARENA_LOBBY_COMPETITION_ID"),
        os.environ.get("CEMINI_HL_PRIMARY_COMP"),
        os.environ.get("S1_TOURNAMENT_COMP"),
    ):
        value = (raw or "").strip()
        if value:
            return value
    return "cmpy2qy65002ud9ej6b7jjq0l"
