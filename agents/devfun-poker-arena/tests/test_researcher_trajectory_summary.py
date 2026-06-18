"""Researcher trajectory summary smoke tests."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "examples"))

from researcher_trajectory_summary import summarize_selfplay_trajectory  # noqa: E402


def test_summarize_selfplay_trajectory():
    rows = [
        {
            "record_type": "decision",
            "hand_id": 1,
            "street": "Preflop",
            "position": "BTN",
            "action": "raise",
            "amount": 6,
            "pot_chips": 3,
            "bet_size_bucket": "large",
            "reasoning_len": 12,
            "n_players": 2,
        },
        {
            "record_type": "decision",
            "hand_id": 1,
            "street": "Flop",
            "position": "BTN",
            "action": "check",
            "pot_chips": 15,
            "bet_size_bucket": "none",
            "reasoning_len": 8,
            "n_players": 2,
        },
        {"record_type": "hand_result", "hand_id": 1, "chip_delta": 10},
    ]
    summary = summarize_selfplay_trajectory(rows)
    assert summary["decision_count"] == 2
    assert summary["vpip_proxy"] == 1.0
    assert summary["pfr_proxy"] == 1.0
    assert summary["bet_size_buckets"]["large"] == 1
