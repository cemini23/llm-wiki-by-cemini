"""WP2 — postflop HU bucket table + solver_frequencies bias."""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "examples"))

from postflop_buckets import (  # noqa: E402
    _reset_bucket_cache,
    bias_thresholds_from_freqs,
    build_solver_frequencies_context,
    classify_board_texture,
    generate_bucket_table,
    load_postflop_buckets,
    lookup_freqs,
    postflop_buckets_enabled,
    resolve_freqs_for_equity,
    strength_bin,
    write_postflop_buckets,
)
from cemini_decide import (  # noqa: E402
    _postflop_free,
    retrieve_solver_context,
)


@pytest.fixture(autouse=True)
def _isolate_env(monkeypatch):
    monkeypatch.delenv("CEMINI_POSTFLOP_BUCKETS", raising=False)
    monkeypatch.delenv("CEMINI_POSTFLOP_BUCKETS_PATH", raising=False)
    monkeypatch.delenv("CEMINI_MAFP_CHART", raising=False)
    _reset_bucket_cache()
    yield
    _reset_bucket_cache()


def test_generate_schema_key_count_and_provenance(tmp_path):
    out = write_postflop_buckets(tmp_path / "postflop_hu_buckets.json")
    data = json.loads(out.read_text(encoding="utf-8"))
    buckets = data["buckets"]
    assert 50 <= len(buckets) <= 100
    assert data.get("schema") == "postflop-hu-buckets-v1"
    assert data.get("meta", {}).get("generator") == "heuristic_bucket_v1"
    notes = str((data.get("solver_provenance") or {}).get("notes", ""))
    assert "heuristic_bucket_v1" in notes or data["meta"]["generator"] == "heuristic_bucket_v1"
    # Sample key shape
    sample = next(iter(buckets))
    parts = sample.split("|")
    assert len(parts) == 4
    raw = buckets[sample]
    for k in ("bet", "check", "call", "fold", "raise", "size_pot_frac"):
        assert k in raw
    s = sum(raw[k] for k in ("bet", "check", "call", "fold", "raise"))
    assert abs(s - 1.0) < 1e-6


def test_classifier_unit_cases():
    assert classify_board_texture(["Ah", "7d", "2c"]) == "dry"
    assert classify_board_texture(["Ah", "Kh", "Qh"]) == "wet"
    assert classify_board_texture(["9h", "8d", "7c"]) == "wet"  # connected
    assert classify_board_texture(["Ah", "Ad", "7c"]) == "paired"
    assert classify_board_texture(["Kh", "Kd", "Ks"]) == "paired"
    assert strength_bin(0.10) == "air"
    assert strength_bin(0.40) == "weak"
    assert strength_bin(0.55) == "medium"
    assert strength_bin(0.75) == "strong"
    assert strength_bin(0.95) == "nuts"


def test_o1_lookup_no_network(tmp_path, monkeypatch):
    path = write_postflop_buckets(tmp_path / "b.json")
    monkeypatch.setenv("CEMINI_POSTFLOP_BUCKETS", "1")
    monkeypatch.setenv("CEMINI_POSTFLOP_BUCKETS_PATH", str(path))
    _reset_bucket_cache()
    f1 = lookup_freqs("flop", "ip", "dry", "medium")
    f2 = lookup_freqs("flop", "ip", "dry", "medium")
    assert f1 is not None and f1 == f2
    assert "bet" in f1 and "size_pot_frac" in f1


def test_flag_off_postflop_free_identical():
    """Flag off / no solver_freqs → byte-identical action for free spots."""
    allowed = {
        "canBet": True,
        "canCheck": True,
        "betRange": {"min": 20, "max": 200},
        "availableActions": ["bet", "check"],
    }
    available = ["bet", "check"]
    a = _postflop_free(0.80, allowed, available, pot=100, solver_freqs=None)
    b = _postflop_free(0.80, allowed, available, pot=100)
    assert a == b
    assert a[0] == "bet"


def test_flag_on_bias_changes_bet_check(tmp_path, monkeypatch):
    """High check-freq air bucket raises bet_bar → check where bare equity would bet."""
    path = write_postflop_buckets(tmp_path / "b.json")
    monkeypatch.setenv("CEMINI_POSTFLOP_BUCKETS", "1")
    monkeypatch.setenv("CEMINI_POSTFLOP_BUCKETS_PATH", str(path))
    _reset_bucket_cache()

    allowed = {
        "canBet": True,
        "canCheck": True,
        "betRange": {"min": 20, "max": 200},
        "availableActions": ["bet", "check"],
    }
    available = ["bet", "check"]
    # equity just above default 0.72 bar
    equity = 0.73
    base = _postflop_free(equity, allowed, available, pot=100, solver_freqs=None)
    assert base[0] == "bet"

    # Force air-like freqs: high check → positive bet_bar_delta → may check
    air_freqs = {
        "bet": 0.05,
        "check": 0.90,
        "call": 0.02,
        "fold": 0.02,
        "raise": 0.01,
        "size_pot_frac": 0.33,
    }
    biased = _postflop_free(equity, allowed, available, pot=100, solver_freqs=air_freqs)
    # At least one of: action changes OR size differs when both bet
    if base[0] == biased[0] == "bet":
        # size should follow size_pot_frac (0.33 vs default 0.66)
        assert biased[1] is not None and base[1] is not None
        assert biased[1] < base[1]
    else:
        assert biased[0] == "check"

    # Strong IP stab freqs lower bar: check→bet on marginal equity
    equity2 = 0.68
    base2 = _postflop_free(equity2, allowed, available, pot=100, solver_freqs=None)
    assert base2[0] == "check"
    stab = {
        "bet": 0.90,
        "check": 0.05,
        "call": 0.02,
        "fold": 0.02,
        "raise": 0.01,
        "size_pot_frac": 0.50,
    }
    biased2 = _postflop_free(equity2, allowed, available, pot=100, solver_freqs=stab)
    assert biased2[0] == "bet"


def test_retrieve_context_flag_off_no_solver_frequencies(monkeypatch):
    monkeypatch.setenv("CEMINI_POSTFLOP_BUCKETS", "0")
    table = {
        "street": "Flop",
        "selfSeatNumber": 1,
        "buttonSeatNumber": 1,
        "boardCards": ["Ah", "7d", "2c"],
        "seats": [
            {"seatNumber": 1, "holeCards": ["As", "Kd"], "status": "Active"},
            {"seatNumber": 2, "holeCards": ["Qh", "Jc"], "status": "Active"},
        ],
    }
    ctx = retrieve_solver_context(table)
    assert "solver_frequencies" not in ctx or ctx.get("solver_frequencies") is None


def test_retrieve_context_flag_on_has_slice(tmp_path, monkeypatch):
    path = write_postflop_buckets(tmp_path / "b.json")
    monkeypatch.setenv("CEMINI_POSTFLOP_BUCKETS", "1")
    monkeypatch.setenv("CEMINI_POSTFLOP_BUCKETS_PATH", str(path))
    monkeypatch.setenv("CEMINI_TABLE_FORMAT", "hu")
    _reset_bucket_cache()
    table = {
        "street": "Flop",
        "selfSeatNumber": 1,
        "buttonSeatNumber": 1,
        "boardCards": ["Ah", "7d", "2c"],
        "seats": [
            {"seatNumber": 1, "holeCards": ["As", "Kd"], "status": "Active"},
            {"seatNumber": 2, "holeCards": ["Qh", "Jc"], "status": "Active"},
        ],
    }
    ctx = retrieve_solver_context(table)
    sf = ctx.get("solver_frequencies")
    assert sf is not None
    assert sf.get("texture") == "dry"
    assert sf.get("role") == "ip"
    assert "by_strength" in sf
    freqs = resolve_freqs_for_equity(sf, 0.72)
    assert freqs is not None
    assert "bet" in freqs


def test_missing_file_fail_open(monkeypatch, tmp_path):
    monkeypatch.setenv("CEMINI_POSTFLOP_BUCKETS", "1")
    monkeypatch.setenv("CEMINI_POSTFLOP_BUCKETS_PATH", str(tmp_path / "nope.json"))
    _reset_bucket_cache()
    assert load_postflop_buckets() is None
    assert lookup_freqs("flop", "ip", "dry", "medium") is None
    table = {
        "street": "Flop",
        "selfSeatNumber": 1,
        "buttonSeatNumber": 1,
        "boardCards": ["Ah", "7d", "2c"],
        "seats": [
            {"seatNumber": 1, "holeCards": ["As", "Kd"], "status": "Active"},
            {"seatNumber": 2, "status": "Active"},
        ],
    }
    # No exception
    ctx = build_solver_frequencies_context(table, in_position=True)
    assert ctx is None


def test_bias_deltas_clamped():
    extreme = {
        "bet": 1.0, "check": 0.0, "call": 0.0, "fold": 0.0, "raise": 0.0,
        "size_pot_frac": 0.5,
    }
    b = bias_thresholds_from_freqs(extreme, facing_bet=False)
    assert -0.08 <= b["bet_bar_delta"] <= 0.08
    face = {
        "bet": 0.0, "check": 0.0, "call": 0.0, "fold": 1.0, "raise": 0.0,
        "size_pot_frac": 0.5,
    }
    f = bias_thresholds_from_freqs(face, facing_bet=True)
    assert -0.08 <= f["fold_slack_delta"] <= 0.08


def test_loader_idempotent(tmp_path, monkeypatch):
    path = write_postflop_buckets(tmp_path / "b.json")
    monkeypatch.setenv("CEMINI_POSTFLOP_BUCKETS", "1")
    monkeypatch.setenv("CEMINI_POSTFLOP_BUCKETS_PATH", str(path))
    _reset_bucket_cache()
    a = lookup_freqs("river", "oop", "wet", "air")
    b = lookup_freqs("river", "oop", "wet", "air")
    assert a == b
