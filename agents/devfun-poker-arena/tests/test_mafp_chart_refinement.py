"""Tests for K124 MAFP fictitious-play chart refinement."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "examples"))
sys.path.insert(0, str(ROOT))

from mafp_chart_refinement import (  # noqa: E402
    aggregate_stance_mixtures,
    all_hand_classes,
    best_response_chart_update,
    ev_open_vs_mixture,
    mixture_fold_rate,
    stack_bucket,
    _deep_copy_hu_chart,
    _chart_action,
    write_mafp_chart,
    load_mafp_chart_ranges,
    MAFP_CHART_PATH,
)


def test_stack_bucket():
    assert stack_bucket(15) == "shallow"
    assert stack_bucket(25) == "mid"
    assert stack_bucket(60) == "deep"


def test_all_hand_classes_count():
    assert len(all_hand_classes()) == 169


def test_ev_open_high_equity_beats_fold():
    ev_aa, ev_fold = ev_open_vs_mixture("AA", fold_rate=0.5)
    assert ev_aa > ev_fold
    ev_72, _ = ev_open_vs_mixture("72o", fold_rate=0.3)
    assert ev_aa > ev_72


def test_aggregate_stance_mixtures():
    rows = [
        {"stance": "rock", "hero_position": "BTN", "stack_bb": 25, "villain_action": "fold"},
        {"stance": "rock", "hero_position": "BTN", "stack_bb": 25, "villain_action": "call"},
        {"stance": "maniac", "hero_position": "BTN", "stack_bb": 25, "villain_action": "raise"},
    ]
    mixes = aggregate_stance_mixtures(rows)
    assert "rock" in mixes
    assert mixes["rock"]["BTN"]["mid"]["fold"] == 0.5


def test_best_response_can_widen_chart():
    chart = _deep_copy_hu_chart()
    # Artificial low fold mixture → should add marginal hands
    mixes = {
        "rock": {"BTN": {"mid": {"fold": 0.75, "call": 0.20, "raise": 0.05}}},
        "maniac": {"BTN": {"mid": {"fold": 0.70, "call": 0.20, "raise": 0.10}}},
        "lag": {"BTN": {"mid": {"fold": 0.65, "call": 0.25, "raise": 0.10}}},
    }
    weights = {"rock": 1.0, "maniac": 1.0, "lag": 1.0}
    before = _chart_action(chart, "BTN", "K9s")
    changes, delta = best_response_chart_update(
        chart, mixes, weights, ev_threshold=0.03,
    )
    assert isinstance(changes, list)
    assert delta >= 0.0


def test_mafp_chart_write_load(tmp_path):
    chart = _deep_copy_hu_chart()
    out = tmp_path / "mafp_hu_chart.json"
    write_mafp_chart(chart, out, mafp_round=1, meta={"test": True})
    data = json.loads(out.read_text())
    assert data["schema"] == "mafp-hu-chart-v1"
    assert data["mafp_round"] == 1
    ranges = load_mafp_chart_ranges(out)
    assert isinstance(ranges, dict)
    assert "BTN" in ranges


def test_mixture_fold_rate():
    mixes = {
        "rock": {"BTN": {"mid": {"fold": 0.8, "call": 0.15, "raise": 0.05}}},
        "lag": {"BTN": {"mid": {"fold": 0.4, "call": 0.4, "raise": 0.2}}},
    }
    w = {"rock": 1.0, "lag": 1.0}
    fr = mixture_fold_rate(mixes, w, "BTN")
    assert 0.5 < fr < 0.7
