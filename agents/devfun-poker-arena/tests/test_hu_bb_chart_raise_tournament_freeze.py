"""HU BB chart raise must refuse under tournament mode (stack repair)."""
from __future__ import annotations

import os
import sys
from pathlib import Path

import pytest

_EXAMPLES = Path(__file__).resolve().parent.parent / "examples"
if str(_EXAMPLES) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES))

from cemini_decide import _hu_bb_chart_raise_vs_open  # noqa: E402


@pytest.fixture
def _isolate_env():
    saved = dict(os.environ)
    yield
    os.environ.clear()
    os.environ.update(saved)


def _hu_bb_table() -> dict:
    return {
        "bigBlind": 20,
        "bb": 20,
        "seats": [
            {"seatNumber": 1, "stack": 1000, "inHand": True},
            {"seatNumber": 2, "stack": 1000, "inHand": True},
        ],
        "selfSeatNumber": 2,
    }


def test_hu_bb_raise_refused_in_tournament(_isolate_env):
    os.environ["CEMINI_TOURNAMENT_MODE"] = "1"
    os.environ["CEMINI_TABLE_FORMAT"] = "hu"
    out = _hu_bb_chart_raise_vs_open(
        _hu_bb_table(),
        {"canRaise": True, "raiseRange": {"min": 80, "max": 1000}},
        ["fold", "call", "raise"],
        pot=60,
        call_chips=40,
        suggested="raise",
        position="BB",
    )
    assert out is None


def test_hu_bb_raise_refused_facing_reraise(_isolate_env):
    os.environ.pop("CEMINI_TOURNAMENT_MODE", None)
    os.environ["CEMINI_TABLE_FORMAT"] = "hu"
    # call > 3bb → already facing a re-raise
    out = _hu_bb_chart_raise_vs_open(
        _hu_bb_table(),
        {"canRaise": True, "raiseRange": {"min": 200, "max": 1000}},
        ["fold", "call", "raise"],
        pot=200,
        call_chips=80,
        suggested="raise",
        position="BB",
    )
    assert out is None


def test_hu_bb_raise_allowed_playground_open(_isolate_env):
    os.environ["CEMINI_TOURNAMENT_MODE"] = "0"
    os.environ["CEMINI_TABLE_FORMAT"] = "hu"
    out = _hu_bb_chart_raise_vs_open(
        _hu_bb_table(),
        {"canRaise": True, "raiseRange": {"min": 60, "max": 1000}},
        ["fold", "call", "raise"],
        pot=40,
        call_chips=20,
        suggested="raise",
        position="BB",
    )
    assert out is not None
    assert out[0] == "raise"
