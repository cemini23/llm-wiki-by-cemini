"""Researcher trajectory summary smoke tests."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "examples"))

from researcher_trajectory_summary import (  # noqa: E402
    build_manifest,
    compute_exploitability_advisory,
    compute_forgetting_factor_regret,
    compute_memory_gap,
    compute_selfplay_axes,
    compute_yardstick_pool_grade,
    evaluate_gates,
    load_yardstick_pool_config,
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


def test_memory_gap_bound_veto_memory_off():
    """Test that bound vetoes when memory is off are correctly counted."""
    decisions = [
        {"trajectory_bound_veto": True, "session_memory_on": False},
        {"trajectory_bound_veto": True, "session_memory_on": False},
        {"trajectory_bound_veto": False, "session_memory_on": False},
    ]
    result = compute_memory_gap(decisions)
    assert result["bound_veto_total"] == 2
    assert result["bound_veto_memory_off"] == 2
    assert result["misdecide_memory_on"] == 0


def test_memory_gap_misdecide_memory_on():
    """Test that mis-decisions (veto when memory is on) are correctly counted."""
    decisions = [
        {"trajectory_bound_veto": True, "session_memory_on": True},  # misdecide
        {"trajectory_bound_veto": True, "session_memory_on": True},  # misdecide
        {"trajectory_bound_veto": True, "session_memory_on": False},
        {"trajectory_bound_veto": False, "session_memory_on": True},
    ]
    result = compute_memory_gap(decisions)
    assert result["bound_veto_total"] == 3
    assert result["bound_veto_memory_off"] == 1
    assert result["misdecide_memory_on"] == 2


def test_memory_gap_empty_decisions():
    """Test that empty decisions return zero counts."""
    result = compute_memory_gap([])
    assert result["bound_veto_total"] == 0
    assert result["bound_veto_memory_off"] == 0
    assert result["misdecide_memory_on"] == 0


def test_memory_gap_missing_telemetry():
    """Test that decisions without telemetry are skipped."""
    decisions = [
        {"trajectory_bound_veto": True},  # missing session_memory_on
        {"trajectory_bound_veto": False, "session_memory_on": True},
    ]
    result = compute_memory_gap(decisions)
    # First decision skipped, second counted
    assert result["bound_veto_total"] == 0
    assert result["bound_veto_memory_off"] == 0
    assert result["misdecide_memory_on"] == 0


def test_exploitability_advisory_none_without_inputs():
    assert compute_exploitability_advisory() is None


def test_exploitability_advisory_disconnect_emagnet_pattern():
    """Skill OK vs soft field but yardstick deeply negative → disconnect."""
    adv = compute_exploitability_advisory(
        skill_bb100=8.0,
        yardstick_bb100=-45.0,
        opponent_bb100={"rock": 12.0, "maniac_shark_lag": -45.0},
    )
    assert adv is not None
    assert adv["advisory_only"] is True
    assert adv["disconnect"] is True
    assert adv["yardstick_handle"] == "maniac_shark_lag"
    assert adv["skill_ok"] is True
    assert adv["yardstick_bad"] is True


def test_exploitability_advisory_no_disconnect_when_yardstick_ok():
    adv = compute_exploitability_advisory(
        opponent_bb100={"ten": 4.3, "maniac_shark_lag": -5.0},
    )
    assert adv is not None
    assert adv["disconnect"] is False
    assert adv["skill_bb100"] == round((4.3 + -5.0) / 2, 4)


def test_exploitability_advisory_in_manifest_not_a_gate():
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
        {"record_type": "hand_result", "hand_id": 1, "chip_delta": 5},
    ]
    summary = summarize_selfplay_trajectory(rows)
    adv = compute_exploitability_advisory(skill_bb100=5.0, yardstick_bb100=-80.0)
    manifest = build_manifest(
        selfplay_summary=summary,
        arena_summary=None,
        bundle_dir=Path("/tmp"),
        exploitability_advisory=adv,
    )
    assert manifest["gate_pass"] is True
    assert evaluate_gates(manifest) == []
    assert manifest["exploitability_advisory"]["disconnect"] is True


def test_yardstick_pool_grade_pct_pass():
    cfg = load_yardstick_pool_config()
    grade = compute_yardstick_pool_grade(
        {"ten": 5.0, "maniac_shark_lag": -2.0, "tight": -3.0},
        pool_config=cfg,
    )
    assert grade["advisory_only"] is True
    assert grade["n_checked"] == 3
    assert grade["n_pass"] == 2
    assert grade["pct_pass"] == round(2 / 3, 4)
    assert grade["per_handle"]["ten"]["pass"] is True
    assert grade["per_handle"]["maniac_shark_lag"]["pass"] is False
    assert grade["per_handle"]["lag"]["missing"] is True
    assert grade["worst_handle"] == "tight"


def test_yardstick_pool_grade_in_manifest_not_a_gate():
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
        {"record_type": "hand_result", "hand_id": 1, "chip_delta": 5},
    ]
    summary = summarize_selfplay_trajectory(rows)
    grade = compute_yardstick_pool_grade({"tight": 8.0})
    manifest = build_manifest(
        selfplay_summary=summary,
        arena_summary=None,
        bundle_dir=Path("/tmp"),
        yardstick_pool_grade=grade,
    )
    assert manifest["gate_pass"] is True
    assert manifest["yardstick_pool_grade"]["pct_pass"] == 1.0


def test_forgetting_factor_regret_stable_session():
    # Recent hands match lifetime — no drift.
    chip_deltas = [4.0] * 20
    out = compute_forgetting_factor_regret(chip_deltas, decay=0.95)
    assert out["n_hands"] == 20
    assert out["lifetime_mean_bb"] == 2.0
    assert out["recency_weighted_mean_bb"] == 2.0
    assert out["drift_flag"] is False
    assert out["advisory_only"] is True


def test_forgetting_factor_regret_drift_flag():
    # Strong early wins, recent losses → recency sags vs lifetime.
    chip_deltas = [10.0] * 15 + [-10.0] * 10
    out = compute_forgetting_factor_regret(
        chip_deltas, decay=0.95, drift_bb_threshold=1.0,
    )
    assert out["n_hands"] == 25
    assert out["lifetime_mean_bb"] > out["recency_weighted_mean_bb"]
    assert out["drift_flag"] is True


def test_forgetting_regret_wired_in_selfplay_summary():
    rows = [
        {
            "record_type": "decision",
            "hand_id": i,
            "street": "Preflop",
            "position": "BTN",
            "action": "raise",
            "reasoning": '{vr: "ln:pre@BTN"}',
            "hole_key": "AsKd",
        }
        for i in range(1, 6)
    ] + [
        {"record_type": "hand_result", "hand_id": i, "chip_delta": 4}
        for i in range(1, 6)
    ]
    summary = summarize_selfplay_trajectory(rows, forgetting_decay=0.9)
    fr = summary.get("forgetting_regret") or {}
    assert fr.get("n_hands") == 5
    assert fr.get("decay") == 0.9
    assert fr.get("lifetime_mean_bb") == 2.0
