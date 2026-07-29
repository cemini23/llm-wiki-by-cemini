"""Blueprint v3 offline agreement gate tests."""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "examples"))

from blueprint_v3_agreement_gate import (  # noqa: E402
    total_variation_distance,
    run_gate,
)
from solver_policy_v3 import FREE_ACTIONS  # noqa: E402


def test_total_variation_distance_identical():
    freqs = {"check": 0.5, "bet_033": 0.3, "bet_075": 0.2, "allin": 0.0}
    assert total_variation_distance(freqs, freqs, FREE_ACTIONS) == 0.0


def test_total_variation_distance_disjoint():
    a = {"check": 1.0, "bet_033": 0.0, "bet_075": 0.0, "allin": 0.0}
    b = {"check": 0.0, "bet_033": 0.0, "bet_075": 0.0, "allin": 1.0}
    assert total_variation_distance(a, b, FREE_ACTIONS) == 1.0


def test_total_variation_distance_partial():
    a = {"check": 0.6, "bet_033": 0.4, "bet_075": 0.0, "allin": 0.0}
    b = {"check": 0.4, "bet_033": 0.6, "bet_075": 0.0, "allin": 0.0}
    assert total_variation_distance(a, b, FREE_ACTIONS) == pytest.approx(0.2)


@pytest.mark.xfail(reason="needs ≥1 held-out dump; may fail if dump dir sparse")
def test_gate_smoke_if_dumps_exist(tmp_path):
    dump_dir = Path("/tmp/cemini-texassolver-dumps-v3")
    baked = ROOT / "research" / "postflop_hu_buckets_v3.json"
    grid = ROOT / "research" / "texassolver_spot_grid_v3.json"
    if not dump_dir.is_dir() or not any(dump_dir.glob("*.json")):
        pytest.skip("no solver dumps in /tmp/cemini-texassolver-dumps-v3")
    if not baked.is_file():
        pytest.skip("baked v3 JSON missing")

    report_path = tmp_path / "agreement.json"
    report = run_gate(
        baked_path=baked,
        grid_path=grid,
        dump_dir=dump_dir,
        report_path=report_path,
    )
    assert report_path.is_file()
    assert "mean_tv" in report
    assert report["keys_compared"] >= 1
