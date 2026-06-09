"""Tests for deploy_registry tournament tracking."""
from __future__ import annotations

import json
from pathlib import Path

import pytest

from deploy_registry import (
    append_deploy_record,
    append_eval_record,
    append_tournament_candidate,
    env_digest,
    pick_deploy_for_tournament,
    read_deploys,
    score_deploy_candidate,
)


@pytest.fixture
def hl_tmp(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    d = tmp_path / "hl-loop"
    d.mkdir()
    monkeypatch.setenv("CEMINI_HL_REPORTS_DIR", str(d))
    return d


def test_env_digest_stable() -> None:
    a = env_digest({"CEMINI_FOO": "1", "CEMINI_BAR": "2"})
    b = env_digest({"CEMINI_BAR": "2", "CEMINI_FOO": "1"})
    assert a == b
    assert len(a) == 16


def test_append_deploy_and_eval(hl_tmp: Path) -> None:
    row = append_deploy_record(
        source="test",
        commit="abc1234",
        hl_round=3,
        hands=100,
        competition_id="comp1",
        preflight="full",
        env_extra={"CEMINI_EVAL_PANEL_GATE": "1"},
    )
    assert row["schema"] == "devfun.deploy_record.v1"
    assert row["env_digest"]

    eval_row = append_eval_record(
        hands=50,
        adjusted_bb100=-12.5,
        tag="smoke",
        competition_id="seed_poker_eval_s1",
        commit="abc1234",
    )
    assert eval_row["adjustedBbPer100"] == -12.5

    deploys = read_deploys()
    assert len(deploys) == 1
    assert (hl_tmp / "eval_timeseries.jsonl").is_file()


def test_pick_deploy_for_tournament(hl_tmp: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("CEMINI_EVAL_PANEL_BB100_FLOOR", "-17.45")
    append_deploy_record(
        source="hl_loop",
        commit="good1",
        hl_round=1,
        hands=50,
        preflight="full",
        env_extra={},
    )
    append_deploy_record(
        source="hl_loop",
        commit="bad1",
        hl_round=2,
        hands=80,
        preflight="full",
        env_extra={},
    )
    # Inject preflight metrics via file
    metrics = hl_tmp / "preflight_metrics.json"
    metrics.write_text(
        json.dumps({"ts": "2026-06-08T00:00:00Z", "eval_panel_bb100": -14.0}) + "\n"
    )
    append_deploy_record(
        source="hl_loop",
        commit="good1",
        hl_round=1,
        hands=50,
        preflight="full",
    )

    # good1 should win with -14 from preflight on redeploy... actually second good1 overwrites digest
    # Score good1 with eval record
    append_eval_record(
        hands=500,
        adjusted_bb100=-14.0,
        tag="full",
        competition_id="seed_poker_eval_s1",
        commit="good1",
    )
    append_eval_record(
        hands=500,
        adjusted_bb100=-20.0,
        tag="full",
        competition_id="seed_poker_eval_s1",
        commit="bad1",
    )

    picks = pick_deploy_for_tournament(min_eval_bb100=-17.45, require_eval_pass=True, limit=3)
    assert picks
    assert picks[0]["commit"] == "good1"
    assert picks[0]["eval_pass"] is True


def test_tournament_candidate_lock(hl_tmp: Path) -> None:
    append_deploy_record(source="test", commit="lock1", hl_round=5, hands=200)
    append_eval_record(
        hands=50,
        adjusted_bb100=-10.0,
        tag="smoke",
        competition_id="seed_poker_eval_s1",
        commit="lock1",
    )
    row = append_tournament_candidate(
        label="s1b-final",
        commit="lock1",
        competition_id="cmp_test",
        rationale="best eval smoke",
        lock=True,
    )
    assert row["schema"] == "devfun.tournament_candidate.v1"
    assert (hl_tmp / "tournament_candidate.json").is_file()
    assert (hl_tmp / "tournament_candidates.jsonl").is_file()


def test_score_deploy_candidate_playground_link(hl_tmp: Path) -> None:
    pg = hl_tmp / "playground_timeseries.jsonl"
    pg.write_text(
        json.dumps(
            {
                "ts": "2026-06-08T12:00:00Z",
                "commit": "c1",
                "replay_chip_delta_avg": 2.5,
                "rank": 25,
                "chips": 5000,
                "buffer_chips": 1200,
            }
        )
        + "\n"
    )
    deploy = {"commit": "c1", "ts": "2026-06-08T11:00:00Z"}
    pg_rows = [json.loads(line) for line in pg.read_text().splitlines() if line.strip()]
    scored = score_deploy_candidate(
        deploy,
        eval_rows=[],
        playground_rows=pg_rows,
        min_eval_bb100=-17.45,
    )
    assert scored["playground"]["samples"] == 1
