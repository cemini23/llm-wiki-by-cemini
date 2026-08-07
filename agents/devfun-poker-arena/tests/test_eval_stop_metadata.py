"""K226/K257 — anytime-valid eval stop metadata."""
from __future__ import annotations

import sys
from pathlib import Path

_EXAMPLES = Path(__file__).resolve().parent.parent / "examples"
if str(_EXAMPLES) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES))

from eval_stop_metadata import (  # noqa: E402
    STOP_METADATA_KEYS,
    assert_no_current_hand_peek,
    record_stop_decision,
)


def _sample_stop_decision() -> dict:
    return record_stop_decision(
        n_hands=1200,
        estimator="AsympCS",
        bound_halfwidth_bb=1.0,
        stopped=True,
        reason="anytime-valid bound reached",
        paired_log_path="logs/arena-ab-0001.jsonl",
        value_model_excludes_current_hand=True,
    )


def test_record_stop_decision_has_all_schema_keys():
    meta = _sample_stop_decision()
    for key in STOP_METADATA_KEYS:
        assert key in meta
    assert meta["n_hands"] == 1200
    assert meta["estimator"] == "AsympCS"
    assert meta["bound_halfwidth_bb"] == 1.0
    assert meta["stopped"] is True
    assert meta["value_model_excludes_current_hand"] is True


def test_record_stop_decision_fail_open_on_missing():
    meta = record_stop_decision(
        n_hands=None,
        estimator=None,
        bound_halfwidth_bb=None,
        stopped=None,
        reason=None,
        paired_log_path=None,
        value_model_excludes_current_hand=None,
    )
    assert meta["n_hands"] == 0
    assert meta["stopped"] is False
    assert meta["value_model_excludes_current_hand"] is False
    assert meta["paired_log_path"] == ""


def test_peek_guard_true_when_hand_absent():
    assert assert_no_current_hand_peek({"h1", "h2", "h3"}, "h99") is True


def test_peek_guard_false_when_hand_present():
    assert assert_no_current_hand_peek({"h1", "h2", "h3"}, "h2") is False


def test_peek_guard_fail_open_empty_is_safe():
    assert assert_no_current_hand_peek(set(), "h1") is True
    assert assert_no_current_hand_peek(None, "h1") is True


def test_docs_mention_arxiv_id():
    docs = (
        Path(__file__).resolve().parent.parent
        / "references"
        / "anytime-valid-agent-eval-stopping.md"
    )
    assert "2608.06362" in docs.read_text(encoding="utf-8")
