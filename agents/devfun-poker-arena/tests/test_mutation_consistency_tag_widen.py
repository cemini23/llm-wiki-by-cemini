"""K235 mutation-consistency — TAG widen flips chart defend predictably."""
from __future__ import annotations

import os
import sys
from pathlib import Path

_EXAMPLES = Path(__file__).resolve().parent.parent / "examples"
if str(_EXAMPLES) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES))

from research_static_chart import research_static_chart  # noqa: E402


def _six_max_bb_table(hole: list[str]) -> dict:
    seats = [{"seatNumber": i, "holeCards": [], "chips": 1000} for i in range(6)]
    seats[0] = {"seatNumber": 0, "holeCards": hole, "chips": 1000, "position": "BB"}
    return {
        "street": "Preflop",
        "tableFormat": "6max",
        "selfSeatNumber": 0,
        "buttonSeatNumber": 5,
        "seats": seats,
    }


def test_tag_widen_mutation_expands_bb_88(monkeypatch):
    """Metamorphic: CEMINI_TAG_WIDEN 0→1 must change 88 BB fold → call/raise."""
    table = _six_max_bb_table(["8h", "8d"])
    monkeypatch.setenv("CEMINI_TAG_WIDEN", "0")
    off = research_static_chart(table)
    assert off.get("preflop_action") == "fold"
    monkeypatch.setenv("CEMINI_TAG_WIDEN", "1")
    on = research_static_chart(table)
    assert on.get("preflop_action") in ("call", "raise")
    assert "tag" in (on.get("source") or "")
