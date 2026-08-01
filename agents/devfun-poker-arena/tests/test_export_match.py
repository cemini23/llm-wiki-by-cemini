"""Export competition match resolution (S11 / stale S1 guard)."""
from __future__ import annotations

import os
import sys
from pathlib import Path

_EXAMPLES = Path(__file__).resolve().parent.parent / "examples"
if str(_EXAMPLES) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES))

from export_match import resolve_export_competition_id  # noqa: E402


def test_cli_match_wins() -> None:
    os.environ["CEMINI_EXPORT_MATCH"] = "env-export"
    os.environ["ARENA_LOBBY_COMPETITION_ID"] = "env-lobby"
    os.environ["S1_TOURNAMENT_COMP"] = "env-s1"
    assert resolve_export_competition_id("cli-match") == "cli-match"


def test_export_match_beats_stale_s1() -> None:
    os.environ["CEMINI_EXPORT_MATCH"] = "s11-live"
    os.environ["ARENA_LOBBY_COMPETITION_ID"] = "s11-lobby"
    os.environ["S1_TOURNAMENT_COMP"] = "stale-s1"
    assert resolve_export_competition_id(None) == "s11-live"


def test_lobby_beats_stale_s1_when_export_unset() -> None:
    os.environ.pop("CEMINI_EXPORT_MATCH", None)
    os.environ["ARENA_LOBBY_COMPETITION_ID"] = "s11-lobby"
    os.environ["S1_TOURNAMENT_COMP"] = "stale-s1"
    assert resolve_export_competition_id("") == "s11-lobby"
