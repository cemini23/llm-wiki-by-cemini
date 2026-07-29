"""K160 three-axis eval stub."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "examples"))

from eval_three_axes import score_axes  # noqa: E402


def test_score_axes_beats_baseline():
    out = score_axes(
        {"calibration": 0.8, "decision_bb100": 5.0, "self_knowledge": True},
        baseline_bb100=0.0,
    )
    assert out["calibration"] == 0.8
    assert out["decision_quality"]["beats_baseline"] is True
    assert out["decision_quality"]["missing_baseline"] is False
    assert out["self_knowledge"] == 1.0
    assert out["advisory_only"] is True


def test_score_axes_flags_missing_baseline():
    out = score_axes({"decision_bb100": 1.0})
    assert out["decision_quality"]["missing_baseline"] is True
    assert out["decision_quality"]["beats_baseline"] is None
