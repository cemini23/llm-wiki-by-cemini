"""K195 rubric → capability-tree diagnosis tests."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "examples"))

from capability_tree import (  # noqa: E402
    diagnose_rubric_failures,
    load_capability_tree_config,
    validate_exclusive_domains,
)

CFG = ROOT / "config" / "hu_capability_tree.json"


def test_config_has_rubric_criteria_map():
    cfg = load_capability_tree_config(CFG)
    rc = cfg.get("rubric_criteria") or {}
    assert isinstance(rc, dict)
    assert "river_value" in rc
    assert rc["river_value"]["domain"] == "policy"
    assert rc["preflop_open"]["child"] == "preflop_chart"
    assert "K195" in (cfg.get("notes") or "")


def test_diagnose_clusters_policy_weakest():
    d = diagnose_rubric_failures(
        ["river_value", "facing_fold", "preflop_open", "self_play_bb100"],
        CFG,
    )
    assert d["schema"] == "devfun.rubric_capability_diagnosis.v1"
    assert d["advisory_only"] is True
    assert d["k"] == "K195"
    assert d["failed_count"] == 4
    assert d["mapped_count"] == 4
    assert d["unmapped"] == []
    assert set(d["by_domain"]["policy"]) == {
        "river_value",
        "facing_fold",
        "preflop_open",
    }
    assert d["by_domain"]["eval"] == ["self_play_bb100"]
    # policy has 3 fails → weakest first
    assert d["fix_order"][0] == "policy"
    assert d["weakest_nodes"][0]["failure_count"] == 3
    assert "postflop_heuristic" in d["weakest_nodes"][0]["foci"]


def test_diagnose_unmapped_criteria():
    d = diagnose_rubric_failures(["totally_unknown_crit_xyz"], CFG)
    assert d["mapped_count"] == 0
    assert d["unmapped"] == ["totally_unknown_crit_xyz"]
    assert d["weakest_nodes"] == []


def test_diagnose_child_id_fallback():
    """Bare tree child ids map via membership when not in rubric_criteria keys."""
    d = diagnose_rubric_failures(["postflop_heuristic", "hud"], CFG)
    assert "policy" in d["by_domain"]
    assert "table" in d["by_domain"]
    assert "postflop_heuristic" in d["by_domain"]["policy"]


def test_diagnose_does_not_break_exclusive_gate():
    gate = validate_exclusive_domains(load_capability_tree_config(CFG))
    assert gate["pass"] is True
