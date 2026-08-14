"""Eval integrity tests (CCC K277 + light K280 + light K281, arXiv methodology).

No Vero / MARC-v1 / AutoDesign / InterSAGE clone — offline, pure helpers only.
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "examples"))

from eval_integrity import (  # noqa: E402
    ENDPOINT_FIELDS,
    TREATMENT_KEYS,
    assert_external_pass_criteria,
    bind_endpoint,
    grade_treatment_blind,
    joint_score,
    strip_treatment,
)

FULL_RECORD = {
    "treatment_bytes": "0101",
    "executed_behavior": "bet",
    "authorization": "allowed",
    "outcome_rule": "win_if_higher",
    "analysis_unit": "hand",
}


# --- strip_treatment ---


def test_strip_removes_treatment_keys_and_leaves_original():
    record = {"executed_behavior": "bet", "arm": "A", "is_treatment": True}
    original = dict(record)
    stripped = strip_treatment(record)
    assert "arm" not in stripped
    assert "is_treatment" not in stripped
    assert stripped["executed_behavior"] == "bet"
    # original unchanged
    assert record == original
    assert record["arm"] == "A"
    assert record["is_treatment"] is True


def test_strip_nested_grader_input():
    record = {
        "executed_behavior": "bet",
        "grader_input": {"arm": "A", "note": "hi"},
    }
    stripped = strip_treatment(record)
    assert "arm" not in stripped["grader_input"]
    assert stripped["grader_input"]["note"] == "hi"


def test_strip_fail_open_on_garbage():
    assert strip_treatment(None) == {}
    assert strip_treatment("nope") == {}


# --- bind_endpoint ---


def test_bind_fails_when_only_label():
    r = bind_endpoint({"label": "win"})
    assert r["ok"] is False
    assert set(ENDPOINT_FIELDS) <= set(r["missing"])


def test_bind_succeeds_with_all_five_fields():
    r = bind_endpoint(FULL_RECORD)
    assert r["ok"] is True
    assert r["missing"] == []


def test_bind_collection_values_for_byte_behavior():
    record = dict(FULL_RECORD)
    record["treatment_bytes"] = ["b1", "b2"]
    record["executed_behavior"] = ("bet",)
    r = bind_endpoint(record)
    assert r["ok"] is True


def test_bind_blank_string_is_missing():
    record = dict(FULL_RECORD, authorization="   ")
    r = bind_endpoint(record)
    assert r["ok"] is False
    assert "authorization" in r["missing"]


# --- grade_treatment_blind ---


def test_grade_relabel_arm_does_not_change_grader_view():
    a = grade_treatment_blind(
        {"executed_behavior": "bet", "arm": "A"}, "win"
    )
    b = grade_treatment_blind(
        {"executed_behavior": "bet", "arm": "B"}, "win"
    )
    assert a["ok"] is True
    assert b["ok"] is True
    assert a["grader_view"] == b["grader_view"]
    assert a["outcome_class"] == "win"
    assert b["outcome_class"] == "win"


def test_grade_leftover_treatment_key_is_leak():
    r = grade_treatment_blind(
        {"executed_behavior": "bet", "grader_input": {"arm": "A", "nested": {"arm": "B"}}},
        "win",
    )
    assert r["ok"] is False
    assert r["reason"] == "treatment_leak"


def test_grade_fail_open_on_garbage():
    r = grade_treatment_blind(None, "win")
    assert r["ok"] is True
    assert r["grader_view"] == {}


# --- joint_score ---


def test_joint_outcome_plus_reexec_bool_ok():
    r = joint_score(True, True)
    assert r["ok"] is True
    assert r["outcome_ok"] is True
    assert r["verification_ok"] is True


def test_joint_self_report_string_fails():
    r = joint_score(True, "yes")
    assert r["ok"] is False
    assert r["verification_ok"] is False
    assert any("self-report" in note for note in r["notes"])


def test_joint_outcome_only_fails():
    r = joint_score(True, None)
    assert r["ok"] is False
    assert r["outcome_ok"] is True
    assert r["verification_ok"] is False


def test_joint_verification_only_fails():
    r = joint_score(False, True)
    assert r["ok"] is False
    assert r["outcome_ok"] is False
    assert r["verification_ok"] is True


def test_joint_identity_self_report_fails():
    report = {"verdict": "looks right"}
    r = joint_score(True, report, self_report=report)
    assert r["ok"] is False
    assert r["verification_ok"] is False


# --- assert_external_pass_criteria ---


def test_owner_hitl_ok():
    r = assert_external_pass_criteria({"owner": "hitl"})
    assert r["ok"] is True


def test_owner_external_ok():
    r = assert_external_pass_criteria({"owner": "external"})
    assert r["ok"] is True


def test_owner_optimizer_fail():
    r = assert_external_pass_criteria({"owner": "optimizer"})
    assert r["ok"] is False
    assert r["reason"] == "closed_loop"


def test_owner_missing_fail():
    assert assert_external_pass_criteria({})["reason"] == "missing_owner"
    assert assert_external_pass_criteria(None)["reason"] == "missing_owner"


def test_self_rewrite_fail():
    r = assert_external_pass_criteria(
        {"owner": "external", "mutated_by": "scorer-1", "scorer_id": "scorer-1"}
    )
    assert r["ok"] is False
    assert r["reason"] == "self_rewrite"


def test_unknown_owner_fail_closed():
    r = assert_external_pass_criteria({"owner": "the-auditor-who-is-me"})
    assert r["ok"] is False
