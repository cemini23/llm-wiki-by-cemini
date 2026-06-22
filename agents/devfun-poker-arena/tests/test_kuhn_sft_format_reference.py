"""Tests for K126 Kuhn poker SFT format reference helpers."""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "examples"))

from kuhn_sft_format_reference import (  # noqa: E402
    KUHN_SFT_DATASETS,
    analyze_trace,
    arena_decide_schema,
    assert_reference_only,
    build_reference_report,
    format_comparison_matrix,
    load_fixture_samples,
    parse_kuhn_messages,
)


def test_load_fixture_samples_embeds_two_rows():
    samples = load_fixture_samples()
    assert len(samples) == 2
    assert samples[0]["dataset"] == KUHN_SFT_DATASETS[0].id
    assert samples[1]["dataset"] == KUHN_SFT_DATASETS[1].id


def test_parse_kuhn_messages_q_sample_has_boxed_bet():
    samples = load_fixture_samples()
    parsed = parse_kuhn_messages(samples[1]["row"]["messages"])
    assert parsed.round_id == "spiral-q-004"
    assert parsed.player_card == "Q"
    assert parsed.available_actions == ("check", "bet")
    assert parsed.boxed_action == "bet"
    assert parsed.has_boxed_answer is True


def test_format_comparison_matrix_has_steal_column():
    matrix = format_comparison_matrix()
    assert len(matrix) >= 8
    assert all("steal" in row for row in matrix)
    assert any(row["steal"] == "yes" for row in matrix)
    assert any(row["steal"] == "no" for row in matrix)


def test_reasoning_gap_is_documented_against_arena_cap():
    samples = load_fixture_samples()
    summary = analyze_trace(samples[1]["row"]["messages"])
    reasoning_cap = arena_decide_schema()["properties"]["reasoning"]["max_chars"]
    assert reasoning_cap == 150
    assert summary["thinking_chars"] > reasoning_cap
    assert summary["thinking_exceeds_arena_reasoning"] is True


def test_dataset_licenses_are_no_license():
    assert [dataset.license for dataset in KUHN_SFT_DATASETS] == [
        "NO LICENSE",
        "NO LICENSE",
    ]


def test_build_reference_report_summarizes_samples():
    samples = load_fixture_samples()
    report = build_reference_report(samples)
    assert report["reference_only"] is True
    assert report["dataset_count"] == 2
    assert report["sample_count"] == 2
    assert "reasoning_length_discipline" in report["steal_candidates"]
    assert report["samples"][1]["boxed_action"] == "bet"


def test_assert_reference_only_blocks_training_mode(monkeypatch):
    monkeypatch.setenv("TRAINING_MODE", "1")
    with pytest.raises(RuntimeError, match="reference-only"):
        assert_reference_only()
