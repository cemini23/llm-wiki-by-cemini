"""VAKRA eval-axis checklist tests (CCC K275, arXiv 2608.12282 methodology).

No IBM/vakra clone, no HF download — local checklist scoring only.
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "examples"))

from vakra_eval_axes import score_eval  # noqa: E402

COMPLETE = {
    "api_paradigm": "compositional",
    "reasoning_hops": 3,
    "multi_source": True,
    "nl_policy_constraint": True,
    "reexec_verified": True,
    "policy_constrained_queries": ["what is villain's hole card?"],
}


def test_incomplete_record_missing_reexec():
    record = {k: v for k, v in COMPLETE.items() if k != "reexec_verified"}
    r = score_eval(record)
    assert r["complete"] is False
    assert "reexec_verified" in r["missing"]


def test_complete_record():
    r = score_eval(COMPLETE)
    assert r["complete"] is True
    assert r["missing"] == []


def test_hops_out_of_range_flagged():
    for hops in (1, 7):
        record = dict(COMPLETE, reasoning_hops=hops)
        r = score_eval(record)
        assert r["complete"] is False
        assert "reasoning_hops" in r["missing"]
        assert any("range" in note for note in r["notes"])


def test_invalid_api_paradigm_missing():
    record = dict(COMPLETE, api_paradigm="rest")
    r = score_eval(record)
    assert "api_paradigm" in r["missing"]


def test_reexec_self_report_string_invalid():
    record = dict(COMPLETE, reexec_verified="yes")
    r = score_eval(record)
    assert r["complete"] is False
    assert "reexec_verified" in r["missing"]
    assert any("self-report" in note for note in r["notes"])


def test_policy_constrained_queries_required():
    record = {k: v for k, v in COMPLETE.items() if k != "policy_constrained_queries"}
    r = score_eval(record)
    assert r["complete"] is False
    assert "policy_constrained_queries" in r["missing"]


def test_empty_record_never_complete():
    r = score_eval({})
    assert r["complete"] is False
    assert len(r["missing"]) >= 5


def test_non_string_query_list_not_coverage():
    record = dict(COMPLETE, policy_constrained_queries=[0, "", "  "])
    r = score_eval(record)
    assert r["complete"] is False
    assert "policy_constrained_queries" in r["missing"]
