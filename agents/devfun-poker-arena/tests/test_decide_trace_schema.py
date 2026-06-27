"""Tests for the relaxed DecideTrace schema stub."""
from __future__ import annotations

import importlib
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
EXAMPLES = ROOT / "examples"

if str(EXAMPLES) not in sys.path:
    sys.path.insert(0, str(EXAMPLES))

decide_trace = importlib.import_module("decide_trace")


def test_validate_decide_trace_accepts_permissive_trace():
    trace = decide_trace.validate_decide_trace(
        {
            "street": "Preflop",
            "action_class": "Raise",
            "rationale": "button open versus passive blind",
        }
    )

    assert trace.street == "preflop"
    assert trace.action_class == "raise"
    assert trace.sizing_intent is None
    assert trace.hero_stack is None
    assert trace.villain_stack is None
    assert trace.pot is None
    assert decide_trace.RELAXED_DECIDE_TRACE_SCHEMA["required"] == ["street", "action_class"]


def test_validate_decide_trace_rejects_bad_action_class():
    with pytest.raises(ValueError, match="action_class"):
        decide_trace.validate_decide_trace(
            {
                "street": "turn",
                "action_class": "dance",
            }
        )
