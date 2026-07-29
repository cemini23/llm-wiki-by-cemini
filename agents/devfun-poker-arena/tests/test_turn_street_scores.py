"""K191/K193 turn-street scores tests."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "examples"))

from turn_street_scores import (  # noqa: E402
    STREETS,
    aggregate_turn_scores,
    classify_action,
    classify_facing,
    normalize_street,
    score_decision_street,
    turn_street_scores_brief_section,
)


def test_normalize_street():
    assert normalize_street("turn") == "Turn"
    assert normalize_street("Preflop") == "Preflop"
    assert normalize_street("RIVER") == "River"


def test_classify_action_and_facing():
    assert classify_action("fold") == "fold"
    assert classify_action("call") == "passive"
    assert classify_action("raise") == "aggressive"
    assert classify_action("all-in") == "aggressive"
    assert classify_facing({"call_chips": 0}) == "check"
    assert classify_facing({"call_chips": 12}) == "bet"
    assert classify_facing({"to_call": 8, "facing_raise": True}) == "raise"


def test_score_decision_street_fields():
    sc = score_decision_street(
        {
            "street": "Turn",
            "action": "call",
            "call_chips": 10,
            "success": True,
            "hand_id": "h1",
            "position": "BB",
        }
    )
    assert sc["street"] == "Turn"
    assert sc["facing"] == "bet"
    assert sc["action_class"] == "passive"
    assert sc["success"] is True
    assert sc["hand_id"] == "h1"
    assert sc["schema"] == "devfun.turn_street_score.v1"


def test_aggregate_turn_scores_per_street():
    rows = [
        {
            "record_type": "decision",
            "street": "Preflop",
            "action": "raise",
            "call_chips": 0,
            "success": True,
        },
        {
            "record_type": "decision",
            "street": "Turn",
            "action": "fold",
            "call_chips": 20,
            "success": False,
        },
        {
            "record_type": "decision",
            "street": "Turn",
            "action": "call",
            "to_call": 10,
            "success": True,
        },
        {
            "record_type": "hand_result",
            "chip_delta": 40,
        },
    ]
    agg = aggregate_turn_scores(rows)
    assert agg["schema"] == "devfun.turn_street_scores.v1"
    assert agg["advisory_only"] is True
    assert agg["decision_count"] == 3
    assert agg["by_street"]["Preflop"]["n"] == 1
    assert agg["by_street"]["Turn"]["n"] == 2
    assert agg["by_street"]["Flop"]["n"] == 0
    assert agg["by_street"]["Turn"]["action_class_counts"]["fold"] == 1
    assert agg["by_street"]["Turn"]["action_class_counts"]["passive"] == 1
    # 1 success of 2 known on Turn
    assert abs(agg["by_street"]["Turn"]["success_rate"] - 0.5) < 1e-9
    for s in STREETS:
        assert s in agg["by_street"]


def test_brief_section_lists_streets():
    agg = aggregate_turn_scores(
        [{"street": "River", "action": "bet", "call_chips": 0, "success": True}]
    )
    md = turn_street_scores_brief_section(agg)
    assert "Turn-street scores" in md
    assert "River" in md
    assert "advisory_only" in md


def test_summarize_selfplay_wires_turn_street_scores():
    """Optional advisory key on trajectory summary."""
    from researcher_trajectory_summary import summarize_selfplay_trajectory

    rows = [
        {
            "record_type": "decision",
            "street": "Flop",
            "action": "check",
            "call_chips": 0,
            "position": "BTN",
            "n_players": 2,
            "reasoning_len": 20,
        },
        {
            "record_type": "hand_result",
            "chip_delta": 5,
        },
    ]
    out = summarize_selfplay_trajectory(rows)
    assert "turn_street_scores" in out
    tss = out["turn_street_scores"]
    assert tss["by_street"]["Flop"]["n"] == 1
    assert tss["advisory_only"] is True
