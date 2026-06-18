"""Heads-up regression — Poker Agent Challenge researcher track."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "examples"))
sys.path.insert(0, str(ROOT))

from tests.fixtures.hu_regression_spots import hu_regression_spots  # noqa: E402
from tests.test_cemini_regression import _run  # noqa: E402


def test_hu_regression_spots():
    for spot in hu_regression_spots():
        action = _run(spot.table, spot.context)["action"]
        if spot.forbidden:
            assert action not in spot.forbidden, (
                f"{spot.id}: got {action!r}, forbidden={sorted(spot.forbidden)} "
                f"— {spot.notes}"
            )
        if spot.required:
            assert action in spot.required, (
                f"{spot.id}: expected one of {sorted(spot.required)}, got {action!r}"
            )


def test_hu_regression_count():
    assert len(hu_regression_spots()) >= 5
