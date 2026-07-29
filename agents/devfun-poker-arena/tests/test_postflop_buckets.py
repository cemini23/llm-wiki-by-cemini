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
    bias_scale_params,
    bias_thresholds_from_freqs,
    build_solver_frequencies_context,
    classify_board_texture,
    generate_bucket_table,
    load_postflop_buckets,
    lookup_freqs,
    postflop_buckets_enabled,
    resolve_bias_generator,
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
    monkeypatch.delenv("CEMINI_SOLVER_HARD", raising=False)
    monkeypatch.delenv("CEMINI_DEEPCFR", raising=False)
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
    b = bias_thresholds_from_freqs(extreme, facing_bet=False, generator="heuristic_bucket_v1")
    assert -0.08 <= b["bet_bar_delta"] <= 0.08
    face = {
        "bet": 0.0, "check": 0.0, "call": 0.0, "fold": 1.0, "raise": 0.0,
        "size_pot_frac": 0.5,
    }
    f = bias_thresholds_from_freqs(face, facing_bet=True, generator="heuristic_bucket_v1")
    assert -0.08 <= f["fold_slack_delta"] <= 0.08


def test_bias_solver_scale_wider_clamp():
    """texas_solver_v1 / deepcfr_lite_v1 use Phase-1 solver scale (±0.14)."""
    p_h = bias_scale_params("heuristic_bucket_v1")
    p_s = bias_scale_params("texas_solver_v1")
    p_d = bias_scale_params("deepcfr_lite_v1")
    assert p_h["clamp"] == pytest.approx(0.08)
    assert p_s["clamp"] == pytest.approx(0.14)
    assert p_s["free_mult"] == pytest.approx(0.15)
    assert p_s["fold_mult"] == pytest.approx(0.18)
    assert p_s["call_mult"] == pytest.approx(0.15)
    assert p_s["raise_mult"] == pytest.approx(0.225)
    assert p_d["clamp"] == pytest.approx(0.14)

    extreme = {
        "bet": 0.0, "check": 1.0, "call": 0.0, "fold": 0.0, "raise": 0.0,
        "size_pot_frac": 0.5,
    }
    # (check-bet)*0.15 = 0.15 → clamped to ±0.14
    b = bias_thresholds_from_freqs(extreme, facing_bet=False, generator="texas_solver_v1")
    assert abs(b["bet_bar_delta"]) == pytest.approx(0.14)
    assert b["bet_bar_delta"] > 0.08  # stronger than heuristic clamp ceiling

    face = {
        "bet": 0.0, "check": 0.0, "call": 0.0, "fold": 1.0, "raise": 0.0,
        "size_pot_frac": 0.5,
    }
    f = bias_thresholds_from_freqs(face, facing_bet=True, generator="texas_solver_v1")
    assert -0.14 <= f["fold_slack_delta"] <= 0.14
    assert abs(f["fold_slack_delta"]) > 0.08


def test_bias_scale_from_loaded_meta(tmp_path, monkeypatch):
    """Loaded texas_solver_v1 meta engages stronger scale when flag on."""
    path = tmp_path / "solver_buckets.json"
    # Minimal valid table
    path.write_text(
        json.dumps({
            "schema": "postflop-hu-buckets-v1",
            "meta": {"generator": "texas_solver_v1", "key_count": 1},
            "buckets": {
                "flop|ip|dry|medium": {
                    "bet": 0.3, "check": 0.3, "call": 0.15,
                    "fold": 0.15, "raise": 0.1, "size_pot_frac": 0.5,
                }
            },
        }),
        encoding="utf-8",
    )
    monkeypatch.setenv("CEMINI_POSTFLOP_BUCKETS", "1")
    monkeypatch.setenv("CEMINI_POSTFLOP_BUCKETS_PATH", str(path))
    monkeypatch.delenv("CEMINI_POSTFLOP_BIAS_SCALE", raising=False)
    _reset_bucket_cache()
    assert resolve_bias_generator() == "texas_solver_v1"
    extreme = {
        "bet": 0.0, "check": 1.0, "call": 0.0, "fold": 0.0, "raise": 0.0,
        "size_pot_frac": 0.5,
    }
    b = bias_thresholds_from_freqs(extreme, facing_bet=False)
    assert b["bet_bar_delta"] > 0.08


def test_heuristic_refuses_overwrite_texas_solver(tmp_path):
    path = tmp_path / "postflop_hu_buckets.json"
    path.write_text(
        json.dumps({
            "meta": {"generator": "texas_solver_v1"},
            "buckets": {"flop|ip|dry|air": {"bet": 0.2, "check": 0.2, "call": 0.2, "fold": 0.2, "raise": 0.2, "size_pot_frac": 0.5}},
        }),
        encoding="utf-8",
    )
    with pytest.raises(SystemExit):
        write_postflop_buckets(path, force_heuristic=False)
    # force overwrites
    out = write_postflop_buckets(path, force_heuristic=True)
    data = json.loads(out.read_text(encoding="utf-8"))
    assert data["meta"]["generator"] == "heuristic_bucket_v1"


def test_loader_idempotent(tmp_path, monkeypatch):
    path = write_postflop_buckets(tmp_path / "b.json")
    monkeypatch.setenv("CEMINI_POSTFLOP_BUCKETS", "1")
    monkeypatch.setenv("CEMINI_POSTFLOP_BUCKETS_PATH", str(path))
    _reset_bucket_cache()
    a = lookup_freqs("river", "oop", "wet", "air")
    b = lookup_freqs("river", "oop", "wet", "air")
    assert a == b


def test_bake_strength_bin_category_helpers():
    """Bake uses hand-category equity → strength_bin (no solver EV)."""
    from bake_texassolver_buckets import (
        estimate_equity_category,
        strength_bin_for_combo,
        classify_action,
        player_to_role,
    )

    # Set on paired board → nuts-ish
    assert estimate_equity_category(["Kh", "Kd"], ["Ks", "7c", "2d"]) >= 0.85
    assert strength_bin_for_combo("KhKd", ["Ks", "7c", "2d"]) in ("strong", "nuts")
    # Air
    assert strength_bin_for_combo("3c2d", ["Ah", "Kd", "Qc"]) in ("air", "weak")
    assert classify_action("BET 10.000000")[0] == "bet"
    assert classify_action("CHECK")[0] == "check"
    assert classify_action("RAISE 34.000000")[0] == "raise"
    assert player_to_role(1) == "oop"
    assert player_to_role(0) == "ip"
