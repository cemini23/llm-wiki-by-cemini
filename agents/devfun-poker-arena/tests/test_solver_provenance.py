"""Tests for K136 P0 solver_provenance module."""
from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "examples"))

# Resilient import (pattern from test_sandbox_rubric_epoch.py)
def _require_attr(mod, name: str):
    if not hasattr(mod, name):
        raise AttributeError(f"solver_provenance missing required attribute: {name}")

spec = importlib.util.spec_from_file_location("solver_provenance", ROOT / "examples" / "solver_provenance.py")
_solver_provenance = importlib.util.module_from_spec(spec)
spec.loader.exec_module(_solver_provenance)

_require_attr(_solver_provenance, "SOLVER_FAMILIES")
_require_attr(_solver_provenance, "EQUILIBRIUM_SELECTION")
_require_attr(_solver_provenance, "PROVENANCE_SCHEMA")
_require_attr(_solver_provenance, "SolverProvenanceError")
_require_attr(_solver_provenance, "normalize_family")
_require_attr(_solver_provenance, "solver_provenance")
_require_attr(_solver_provenance, "stamp_chart_provenance")
_require_attr(_solver_provenance, "read_chart_provenance")
_require_attr(_solver_provenance, "read_chart_file_provenance")
_require_attr(_solver_provenance, "family_of")
_require_attr(_solver_provenance, "same_family")
_require_attr(_solver_provenance, "provenance_fingerprint")
_require_attr(_solver_provenance, "assert_diffable")
_require_attr(_solver_provenance, "diff_charts")


# Aliases for convenience
normalize_family = _solver_provenance.normalize_family
solver_provenance = _solver_provenance.solver_provenance
stamp_chart_provenance = _solver_provenance.stamp_chart_provenance
read_chart_provenance = _solver_provenance.read_chart_provenance
read_chart_file_provenance = _solver_provenance.read_chart_file_provenance
family_of = _solver_provenance.family_of
same_family = _solver_provenance.same_family
provenance_fingerprint = _solver_provenance.provenance_fingerprint
assert_diffable = _solver_provenance.assert_diffable
diff_charts = _solver_provenance.diff_charts
SolverProvenanceError = _solver_provenance.SolverProvenanceError


def test_normalize_family_aliases():
    """Test that common aliases map to canonical names."""
    assert normalize_family("cfr+") == "cfr_plus"
    assert normalize_family("CFR+") == "cfr_plus"
    assert normalize_family("FP") == "fictitious_play"
    assert normalize_family("fp") == "fictitious_play"
    assert normalize_family("r-nad") == "rnad"
    assert normalize_family("R-NAD") == "rnad"
    assert normalize_family("rnad") == "rnad"
    assert normalize_family("") == "unknown"
    assert normalize_family(None) == "unknown"
    assert normalize_family("junk_not_in_vocab") == "unknown"


def test_solver_provenance_block_shape():
    """Test provenance block has correct schema and fields."""
    prov = solver_provenance(
        "cfr+",
        version="2.1",
        equilibrium_selection="time_average",
        nash_set_singleton=True,
        notes="Test provenance",
    )
    assert prov["schema"] == "solver-provenance-v1"
    assert prov["solver_family"] == "cfr_plus"
    assert prov["solver_version"] == "2.1"
    assert prov["equilibrium_selection"] == "time_average"
    assert prov["nash_set_singleton"] is True
    assert prov["notes"] == "Test provenance"
    assert "stamped_at" in prov
    # stamped_at should be ISO format UTC
    assert prov["stamped_at"].endswith("Z")


def test_solver_provenance_invalid_equilibrium_selection():
    """Test that invalid equilibrium_selection raises ValueError."""
    try:
        solver_provenance("cfr", equilibrium_selection="invalid_selection")
        assert False, "Should have raised ValueError"
    except ValueError as e:
        assert "invalid_selection" in str(e)


def test_stamp_does_not_mutate_input():
    """Test that stamp_chart_provenance does not mutate input payload."""
    payload = {"ranges": {"BTN": {"AA": "raise"}}, "schema": "test-v1"}
    original_payload = payload.copy()
    prov = solver_provenance("cfr")
    stamped = stamp_chart_provenance(payload, prov)
    # Original unchanged
    assert payload == original_payload
    assert "solver_provenance" not in payload
    # Stamped has the key
    assert "solver_provenance" in stamped
    assert stamped["solver_provenance"]["solver_family"] == "cfr"


def test_read_chart_provenance_absent_returns_none():
    """Test read_chart_provenance returns None for missing key."""
    payload = {"ranges": {}}
    assert read_chart_provenance(payload) is None
    # Should not raise on empty dict
    assert read_chart_provenance({}) is None
    assert read_chart_provenance(None) is None


def test_same_family_true_false_unknown():
    """Test same_family behavior: same -> True, different -> False, unknown -> False."""
    prov_cfr = solver_provenance("cfr")
    prov_cfr2 = solver_provenance("cfr")
    prov_cfr_plus = solver_provenance("cfr_plus")
    prov_unknown = solver_provenance("unknown")

    # Same family
    assert same_family(prov_cfr, prov_cfr2) is True
    # Different families
    assert same_family(prov_cfr, prov_cfr_plus) is False
    # Unknown on either side
    assert same_family(prov_cfr, prov_unknown) is False
    assert same_family(prov_unknown, prov_cfr) is False
    # Both unknown
    assert same_family(prov_unknown, {"solver_family": "unknown"}) is False


def test_assert_diffable_same_family_ok():
    """Test assert_diffable passes for same family with singleton None."""
    prov_a = solver_provenance("cfr", nash_set_singleton=None)
    prov_b = solver_provenance("cfr", nash_set_singleton=None)
    record = assert_diffable(prov_a, prov_b, disclose=False)
    assert record["diffable"] is True
    assert record["same_family"] is True
    assert record["disclosed"] is False
    assert record["family_a"] == "cfr"
    assert record["family_b"] == "cfr"


def test_assert_diffable_cross_family_raises():
    """Test cross-family raises SolverProvenanceError without disclose."""
    prov_a = solver_provenance("cfr_plus")
    prov_b = solver_provenance("rnad")
    try:
        assert_diffable(prov_a, prov_b, disclose=False)
        assert False, "Should have raised SolverProvenanceError"
    except SolverProvenanceError as e:
        assert "cfr_plus" in str(e) or "cross-family" in str(e)


def test_assert_diffable_cross_family_with_disclose():
    """Test cross-family allowed with disclose=True."""
    prov_a = solver_provenance("cfr_plus")
    prov_b = solver_provenance("rnad")
    record = assert_diffable(prov_a, prov_b, disclose=True)
    assert record["diffable"] is True
    assert record["same_family"] is False
    assert record["disclosed"] is True


def test_assert_diffable_known_nonsingleton_raises():
    """Test same family but known non-singleton raises without disclose."""
    prov_a = solver_provenance("cfr", nash_set_singleton=False)
    prov_b = solver_provenance("cfr", nash_set_singleton=None)
    try:
        assert_diffable(prov_a, prov_b, disclose=False)
        assert False, "Should have raised SolverProvenanceError"
    except SolverProvenanceError as e:
        assert "non-singleton" in str(e).lower() or "singleton" in str(e).lower()


def test_assert_diffable_known_nonsingleton_with_disclose():
    """Test non-singleton allowed with disclose=True."""
    prov_a = solver_provenance("cfr", nash_set_singleton=False)
    prov_b = solver_provenance("cfr", nash_set_singleton=True)
    record = assert_diffable(prov_a, prov_b, disclose=True)
    assert record["diffable"] is True
    assert record["disclosed"] is True


def test_diff_charts_guarded_and_payload():
    """Test diff_charts guarded by provenance and returns correct diffs."""
    # Same family - should diff cleanly
    payload_a = {
        "schema": "test-v1",
        "ranges": {
            "BTN": {"AA": "raise", "KK": "raise", "QQ": "call"},
            "BB": {"AA": "raise"},
        },
        "solver_provenance": solver_provenance("cfr"),
    }
    payload_b = {
        "schema": "test-v1",
        "ranges": {
            "BTN": {"AA": "raise", "KK": "call", "JJ": "raise"},  # KK changed, JJ added
            "BB": {"AA": "raise", "KK": "call"},  # KK added
        },
        "solver_provenance": solver_provenance("cfr"),
    }
    result = diff_charts(payload_a, payload_b, disclose=False)
    assert result["disclosure"]["same_family"] is True
    assert result["disclosure"]["diffable"] is True
    # QQ removed from BTN
    removed = [(r["position"], r["hand"]) for r in result["removed"]]
    assert ("BTN", "QQ") in removed
    # JJ added to BTN
    added = [(a["position"], a["hand"]) for a in result["added"]]
    assert ("BTN", "JJ") in added
    # KK changed from raise to call in BTN
    changed = [(c["position"], c["hand"], c["from"], c["to"]) for c in result["changed"]]
    assert ("BTN", "KK", "raise", "call") in changed
    assert result["n_changed"] >= 1


def test_diff_charts_cross_family_raises():
    """Test diff_charts raises on cross-family without disclose."""
    payload_a = {
        "ranges": {"BTN": {}},
        "solver_provenance": solver_provenance("cfr"),
    }
    payload_b = {
        "ranges": {"BTN": {}},
        "solver_provenance": solver_provenance("rnad"),
    }
    try:
        diff_charts(payload_a, payload_b, disclose=False)
        assert False, "Should have raised SolverProvenanceError"
    except SolverProvenanceError:
        pass  # Expected


def test_provenance_fingerprint_deterministic():
    """Test fingerprint is deterministic for same provenance."""
    prov1 = solver_provenance("cfr", version="1", equilibrium_selection="time_average")
    prov2 = solver_provenance("cfr", version="1", equilibrium_selection="time_average")
    fp1 = provenance_fingerprint(prov1)
    fp2 = provenance_fingerprint(prov2)
    assert fp1 == fp2
    assert len(fp1) == 64  # SHA256 hex length


def test_read_chart_file_provenance_roundtrip(tmp_path: Path):
    """Test write/read roundtrip of provenance via file."""
    payload = {
        "schema": "test-v1",
        "ranges": {"BTN": {"AA": "raise"}},
    }
    prov = solver_provenance("mafp", notes="Test roundtrip")
    stamped = stamp_chart_provenance(payload, prov)

    out_path = tmp_path / "test_chart.json"
    out_path.write_text(json.dumps(stamped, indent=2))

    loaded = read_chart_file_provenance(out_path)
    assert loaded is not None
    assert loaded["solver_family"] == "mafp"
    assert loaded["notes"] == "Test roundtrip"


def test_family_of_payload_vs_direct():
    """Test family_of works with both payload and provenance dict directly."""
    prov = solver_provenance("cfr_plus")
    payload = {"solver_provenance": prov}

    assert family_of(prov) == "cfr_plus"
    assert family_of(payload) == "cfr_plus"
    assert family_of({}) == "unknown"
    assert family_of(None) == "unknown"
