"""Verification-chain tests (Cybersec K278 ATOBench, arXiv 2608.12996 pattern).

No ATOBench clone — offline trace scoring only. Paper metrics ≠ poker EV.
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "examples"))

from verification_chain import (  # noqa: E402
    attach_evidence,
    evidence_intact,
    pair_traces,
    score_trace,
)


def _grounded(action: str, locator: str = "h1") -> dict:
    return attach_evidence({"action": action}, {"locator": locator})


def _ungrounded(action: str) -> dict:
    return {"action": action}


# --- attach_evidence ---


def test_attach_without_locator_not_intact():
    step = attach_evidence({"action": "fold"}, {})
    assert step["_evidence_ok"] is False
    assert evidence_intact(step) is False


def test_attach_with_locator_intact():
    step = attach_evidence({"action": "fold"}, {"locator": "h1"})
    assert step["_evidence_ok"] is True
    assert evidence_intact(step) is True


def test_attach_does_not_mutate_action():
    action = {"action": "fold"}
    attach_evidence(action, {"locator": "h1"})
    assert action == {"action": "fold"}


def test_attach_garbage_input_fail_open():
    step = attach_evidence("fold", {"locator": "h1"})
    assert isinstance(step, dict)
    assert step["_evidence_ok"] is True
    assert evidence_intact(step) is True
    step2 = attach_evidence({"action": "fold"}, "not-a-dict")
    assert step2["_evidence_ok"] is False
    assert evidence_intact(step2) is False


# --- score_trace ---


def test_three_grounded_folds_intact():
    steps = [_grounded("fold"), _grounded("fold"), _grounded("fold")]
    s = score_trace(steps)
    assert s["evidence_intact"] is True
    assert s["busy_after_break"] is False
    assert s["activity_ne_verification"] is False
    assert s["activity"] == 3
    assert s["grounded_count"] == 3
    assert s["ungrounded_count"] == 0


def test_two_grounded_then_three_ungrounded_repeats():
    steps = [
        _grounded("fold"),
        _grounded("check"),
        _ungrounded("probe"),
        _ungrounded("probe"),
        _ungrounded("probe"),
    ]
    s = score_trace(steps)
    assert s["first_break_index"] == 2
    assert s["busy_after_break"] is True
    assert s["activity_ne_verification"] is True
    assert s["repetitions"] >= 2
    assert s["grounded_count"] == 2
    assert s["ungrounded_count"] == 3


def test_empty_trace_not_intact():
    s = score_trace([])
    assert s["evidence_intact"] is False
    assert s["activity"] == 0
    assert s["first_break_index"] is None


# --- evidence_intact observed-state consistency ---


def test_observed_state_mismatch_not_intact():
    step = attach_evidence(
        {"action": "fold"},
        {"locator": "h1", "observed": {"street": "flop"}},
    )
    assert evidence_intact(step, {"street": "turn"}) is False


def test_observed_state_match_intact():
    step = attach_evidence(
        {"action": "fold"},
        {"locator": "h1", "observed": {"street": "flop"}},
    )
    assert evidence_intact(step, {"street": "flop", "board": "AhKd"}) is True


def test_no_observed_state_is_intact_when_locator_present():
    step = attach_evidence({"action": "fold"}, {"locator": "h1"})
    assert evidence_intact(step, {"street": "flop"}) is True


# --- pair_traces ---


def test_pair_same_outcome_different_evidence_path():
    native = [
        _grounded("fold"),
        attach_evidence({"action": "call", "outcome": "win"}, {"locator": "h1"}),
    ]
    treatment = [
        _grounded("fold"),
        _ungrounded("probe"),
        _ungrounded("probe"),
        {"action": "probe", "outcome": "win"},
    ]
    p = pair_traces(native, treatment)
    assert p["outcome_same"] is True
    assert p["evidence_path_same"] is False


def test_pair_identical_traces():
    trace = [_grounded("fold"), _grounded("call")]
    p = pair_traces(trace, list(trace))
    assert p["first_divergence"] is None
    assert p["evidence_path_same"] is True


def test_pair_sqli_style_activity_not_verification():
    # Native stays grounded (short); treatment keeps probing after the
    # evidence path breaks — activity up, repetitions up.
    native = [
        _grounded("fold"),
        attach_evidence({"action": "call", "outcome": "win"}, {"locator": "h1"}),
    ]
    treatment = [
        _grounded("fold"),
        _ungrounded("probe"),
        _ungrounded("probe"),
        _ungrounded("probe"),
        _ungrounded("probe"),
        {"action": "probe", "outcome": "win"},
    ]
    p = pair_traces(native, treatment)
    assert p["treatment_score"]["activity_ne_verification"] is True
    assert p["treatment_score"]["activity"] > p["native_score"]["activity"]
    assert p["treatment_score"]["repetitions"] > p["native_score"]["repetitions"]
    assert p["native_score"]["activity_ne_verification"] is False


def test_pair_no_terminal_outcome_gives_none():
    native = [_grounded("fold")]
    treatment = [_grounded("fold")]
    p = pair_traces(native, treatment)
    assert p["outcome_same"] is None


def test_pair_length_mismatch_divergence():
    native = [_grounded("fold")]
    treatment = [_grounded("fold"), _grounded("call")]
    p = pair_traces(native, treatment)
    assert p["first_divergence"] == 1
