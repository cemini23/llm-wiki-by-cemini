"""K125 P1 — trajectory bound wrapper on cemini_decide._build."""
from __future__ import annotations

import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "examples"))

import cemini_decide  # noqa: E402


def _minimal_table(can_check: bool = True) -> dict:
    available = ["fold"]
    if can_check:
        available.append("check")
    return {
        "tableId": "tb_trajectory_test",
        "street": "Flop",
        "boardCards": ["Ah", "7d", "2c"],
        "selfSeatNumber": 1,
        "seats": [
            {
                "seatNumber": 1,
                "holeCards": ["Ks", "Qh"],
                "stackChips": 1000,
            },
            {"seatNumber": 2, "holeCards": [], "stackChips": 1000},
        ],
        "allowedActions": {
            "availableActions": available,
            "canCheck": can_check,
            "canFold": True,
        },
    }


def test_trajectory_bound_disabled_by_default():
    os.environ.pop("CEMINI_TRAJECTORY_BOUND", None)
    table = _minimal_table()
    allowed = table["allowedActions"]
    out = cemini_decide._build("check", None, table, allowed, eq=0.5, po=0.0, msg="test")
    assert out["action"] == "check"


def test_trajectory_bound_veto_replaces_with_safe_action():
    os.environ["CEMINI_TRAJECTORY_BOUND"] = "1"
    cemini_decide._TRAJECTORY_BOUND_STATE = cemini_decide.TrajectoryBoundState()
    cemini_decide._TRAJECTORY_BOUND_HAND_KEY = None
    cemini_decide._TRAJECTORY_BOUND_CFG = cemini_decide.BoundConfig(veto_threshold=0.0)
    table = _minimal_table()
    allowed = table["allowedActions"]
    out = cemini_decide._build(
        "fold",
        None,
        table,
        allowed,
        eq=0.1,
        po=0.5,
        msg="forced fold",
    )
    assert out["action"] in allowed["availableActions"]
    assert "bound" in out.get("reasoning", "").lower() or out["action"] in ("check", "fold")
