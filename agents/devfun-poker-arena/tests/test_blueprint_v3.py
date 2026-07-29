"""Blueprint v3 — per-hand-bucket free/facing policy tests."""
from __future__ import annotations

import random
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "examples"))

from solver_policy_v3 import (  # noqa: E402
    FACING_ACTIONS,
    FREE_ACTIONS,
    HAND_BUCKETS,
    blueprint_v3_enabled,
    build_key,
    coverage_ok,
    facing_node,
    hand_bucket,
    load_blueprint_v3,
    lookup_policy,
    sample_action_v3,
    spr_bin,
)


def test_spr_bins_v3():
    assert spr_bin(80, 50) == "le2"
    assert spr_bin(80, 20) == "2to5"
    assert spr_bin(120, 20) == "gt5"


def test_facing_node_buckets():
    assert facing_node(10, 40) == "vs_small"
    assert facing_node(20, 40) == "vs_mid"
    assert facing_node(30, 40) == "vs_big"
    assert facing_node(40, 40) == "vs_over"
    assert facing_node(10, 40, vs_raise=True) == "vs_raise"


def test_hand_bucket_deterministic():
    b = ["Kd", "7c", "2s"]
    h1 = hand_bucket(["Ah", "Kd"], b)
    h2 = hand_bucket(["Ah", "Kd"], b)
    assert h1 == h2
    assert h1 in HAND_BUCKETS


def test_free_facing_disjoint_action_sets():
    free_key = build_key("flop", "srp", "ip", "dry", "2to5", "free", "tp_good")
    face_key = build_key("flop", "srp", "ip", "dry", "2to5", "vs_mid", "tp_good")
    free_entry = {
        "freqs": {k: (1.0 if k == "check" else 0.0) for k in FREE_ACTIONS},
        "node": "free",
        "combos": 25,
        "weight": 1.0,
    }
    face_entry = {
        "freqs": {k: (1.0 if k == "fold" else 0.0) for k in FACING_ACTIONS},
        "node": "vs_mid",
        "combos": 25,
        "weight": 1.0,
    }
    assert "fold" not in free_entry["freqs"] or free_entry["freqs"].get("fold", 0) == 0
    assert "check" not in face_entry["freqs"] or face_entry["freqs"].get("check", 0) == 0
    assert "bet_033" in free_entry["freqs"]
    assert "fold" in face_entry["freqs"]
    assert free_key != face_key


def test_sample_drops_illegal():
    entry = {
        "freqs": {"check": 0.0, "bet_033": 1.0, "bet_075": 0.0, "allin": 0.0},
        "node": "free",
    }
    rng = random.Random(0)
    out = sample_action_v3(
        entry,
        ["check"],
        facing=False,
        pot=20,
        call_chips=0,
        rng=rng,
        allowed={"betRange": {"min": 6, "max": 80}},
    )
    assert out is not None
    assert out[0] == "check"


def test_coverage_gate_fail_open():
    assert coverage_ok(None) is False
    assert coverage_ok({"freqs": {"check": 1.0}, "node": "free", "combos": 2, "weight": 1.0}) is False
    assert coverage_ok(
        {"freqs": {"check": 1.0, "bet_033": 0.0, "bet_075": 0.0, "allin": 0.0},
         "node": "free", "combos": 25, "weight": 0.01},
    ) is True
    assert coverage_ok(
        {"freqs": {"check": 1.0}, "node": "free", "combos": 5, "weight": 1.0},
        smoke=True,
    ) is True
    assert coverage_ok({"freqs": {"check": 1.0}, "node": "free", "combos": 3, "weight": 0.001}) is False


def test_blueprint_v3_flag(monkeypatch):
    monkeypatch.delenv("CEMINI_SOLVER_V3", raising=False)
    assert blueprint_v3_enabled() is False
    monkeypatch.setenv("CEMINI_SOLVER_V3", "1")
    assert blueprint_v3_enabled() is (ROOT / "research" / "postflop_hu_buckets_v3.json").is_file()


def test_load_smoke_file_if_present():
    path = ROOT / "research" / "postflop_hu_buckets_v3.json"
    if not path.is_file():
        pytest.skip("smoke bake output not present")
    payload = load_blueprint_v3(force=True)
    assert payload is not None
    meta = payload.get("meta") or {}
    assert meta.get("generator") == "texas_solver_blueprint_v3"
    buckets = payload.get("buckets") or {}
    assert len(buckets) >= 1
    sample_key = next(iter(buckets))
    entry = lookup_policy(sample_key, payload)
    assert entry is not None
    node = str(entry.get("node") or sample_key.split("|")[5])
    if node == "free":
        assert set((entry.get("freqs") or entry).keys()) <= set(FREE_ACTIONS)
    else:
        assert set((entry.get("freqs") or entry).keys()) <= set(FACING_ACTIONS)
