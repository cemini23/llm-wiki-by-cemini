"""Offline trajectory-bound report tests."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "examples"))

from trajectory_bound_report import build_summary, main  # noqa: E402


def test_trajectory_bound_detects_breached_hand(tmp_path: Path):
    rows = [
        {
            "record_type": "decision",
            "hand_id": 1,
            "step": 1,
            "street": "Preflop",
            "action": "raise",
            "reasoning": '{vr: "open btn", ke: "AK strong"}',
            "hole_key": "AsKd",
            "pot_chips": 3,
        },
        {"record_type": "hand_result", "hand_id": 1, "chip_delta": 6},
        {
            "record_type": "decision",
            "hand_id": 2,
            "step": 1,
            "street": "Flop",
            "action": "call",
            "reasoning": 'bad trace says board has Qh and Jc',
            "hole_key": "AsKd",
            "pot_chips": 20,
        },
        {"record_type": "hand_result", "hand_id": 2, "chip_delta": -10},
    ]

    summary = build_summary(rows, {"tau": 0.05, "mode": "independent"})

    assert summary["totals"]["breach_count"] == 1
    assert summary["totals"]["tau"] == 0.05
    assert summary["totals"]["mode"] == "independent"
    assert summary["per_hand"][0]["hand_id"] == 1
    assert summary["per_hand"][0]["breached"] is False
    assert summary["per_hand"][1]["hand_id"] == 2
    assert summary["per_hand"][1]["breached"] is True


def test_trajectory_bound_cli_writes_schema_keys(tmp_path: Path):
    selfplay = tmp_path / "selfplay.jsonl"
    out_dir = tmp_path / "out"
    rows = [
        {
            "record_type": "decision",
            "hand_id": 10,
            "step": 1,
            "street": "Preflop",
            "action": "fold",
            "reasoning": '{vr: "trash fold"}',
            "hole_key": "7c2d",
            "pot_chips": 3,
        },
        {"record_type": "hand_result", "hand_id": 10, "chip_delta": -1},
    ]
    selfplay.write_text(
        "".join(json.dumps(row, sort_keys=True) + "\n" for row in rows),
        encoding="utf-8",
    )

    assert main(["--selfplay", str(selfplay), "--out-dir", str(out_dir)]) == 0

    summary = json.loads((out_dir / "trajectory_bound_summary.json").read_text())
    assert set(summary) == {"per_hand", "totals"}
    assert {"hand_id", "r_star", "breached", "decision_count"} <= set(summary["per_hand"][0])
    assert {"breach_count", "tau", "mode"} <= set(summary["totals"])
