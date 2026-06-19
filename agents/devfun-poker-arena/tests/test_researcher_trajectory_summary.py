"""Researcher trajectory summary smoke tests."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "examples"))

from researcher_trajectory_summary import (  # noqa: E402
    build_manifest,
    compute_selfplay_axes,
    evaluate_gates,
    summarize_selfplay_trajectory,
)


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
            "reasoning": '{vr: "ln:pre@BTN", ke: "55% eq"}',
            "hole_key": "AsKd",
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
            "reasoning": '{vr: "ln:flo@BTN"}',
            "hole_key": "AsKd",
            "n_players": 2,
        },
        {"record_type": "hand_result", "hand_id": 1, "chip_delta": 10},
    ]
    summary = summarize_selfplay_trajectory(rows)
    assert summary["decision_count"] == 2
    assert summary["vpip_proxy"] == 1.0
    assert summary["pfr_proxy"] == 1.0
    assert summary["bet_size_buckets"]["large"] == 1
    assert "axes" in summary
    assert "M8_hallucination_rate" in summary["axes"]


def test_m8_hallucination_gate():
    rows = [
        {
            "record_type": "decision",
            "hand_id": 1,
            "street": "Flop",
            "position": "BTN",
            "action": "check",
            "reasoning": "seeing Qh on board",  # hallucinated card
            "hole_key": "AsKd",
        },
    ]
    axes = compute_selfplay_axes(rows, [])
    assert axes["M8_hallucination_rate"] == 1.0


def test_gate_pass_selfplay():
    rows = [
        {
            "record_type": "decision",
            "hand_id": 1,
            "street": "Preflop",
            "position": "BTN",
            "action": "raise",
            "reasoning": '{vr: "ln:pre@BTN"}',
            "hole_key": "AsKd",
        },
        {
            "record_type": "decision",
            "hand_id": 2,
            "street": "Preflop",
            "position": "UTG",
            "action": "fold",
            "reasoning": '{vr: "ln:pre@UTG"}',
            "hole_key": "7c2d",
        },
        {"record_type": "hand_result", "hand_id": 1, "chip_delta": 5},
        {"record_type": "hand_result", "hand_id": 2, "chip_delta": -2},
    ]
    summary = summarize_selfplay_trajectory(rows)
    manifest = build_manifest(
        selfplay_summary=summary,
        arena_summary=None,
        bundle_dir=Path("/tmp"),
    )
    assert manifest["gate_pass"] is True
    assert evaluate_gates(manifest) == []
