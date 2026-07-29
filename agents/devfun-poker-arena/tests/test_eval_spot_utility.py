"""K197 spot utility ranking."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "examples"))

from eval_spot_utility import rank_spots_by_utility  # noqa: E402


def test_rank_prefers_lift_over_fail_rate_alone():
    spots = [
        {"id": "high_fail", "fail_rate": 0.9, "lift": 0.1, "cost": 1.0},
        {"id": "high_lift", "fail_rate": 0.2, "lift": 2.0, "cost": 1.0},
    ]
    ranked = rank_spots_by_utility(spots)
    assert ranked[0]["id"] == "high_lift"
    assert ranked[0]["utility"] > ranked[1]["utility"]
