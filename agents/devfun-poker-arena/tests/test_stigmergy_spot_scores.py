"""K141 stigmergic spot-class scores tests."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "examples"))

from stigmergy_spot_scores import (  # noqa: E402
    StigmergySpotScores,
    apply_stigmergy_to_deepsearch_filter,
    load_stigmergy_config,
    rank_eligible_spot_classes,
    stigmergy_brief_section,
)

CFG = ROOT / "config" / "hu_stigmergy_spot_scores.json"


def test_config_loads():
    cfg = load_stigmergy_config(CFG)
    assert cfg["schema"] == "devfun.hu_stigmergy_spot_scores.v1"
    assert 0 < float(cfg["rho"]) <= 1.0
    assert float(cfg["cap"]) > 0
    assert "pressure" in cfg["channels"]
    assert cfg.get("advisory_only") is True


def test_update_and_rank_prefers_pressure_block():
    s = StigmergySpotScores(CFG)
    s.update_score("spot_a", "pressure", 3.0)
    s.update_score("spot_a", "block", 2.0)
    s.update_score("spot_b", "completion", 5.0)  # success → lower shortlist priority
    s.update_score("spot_c", "pressure", 0.5)
    ranked = s.rank_classes(["spot_b", "spot_c", "spot_a"])
    assert ranked[0] == "spot_a"
    assert ranked.index("spot_c") < ranked.index("spot_b")


def test_decay_all_scales_by_rho():
    s = StigmergySpotScores(
        {
            "schema": "devfun.hu_stigmergy_spot_scores.v1",
            "rho": 0.5,
            "cap": 10.0,
            "channels": ["pressure", "completion", "block"],
            "scores": {"x": {"pressure": 4.0, "completion": 0.0, "block": 0.0}},
            "advisory_only": True,
        }
    )
    s.decay_all()
    assert abs(s.channel_scores("x")["pressure"] - 2.0) < 1e-9


def test_cap_clamps_updates():
    s = StigmergySpotScores(
        {
            "rho": 0.9,
            "cap": 5.0,
            "scores": {},
            "advisory_only": True,
        }
    )
    s.update_score("hot", "pressure", 100.0)
    assert s.channel_scores("hot")["pressure"] == 5.0


def test_rank_units_preserves_advisory_flag():
    s = StigmergySpotScores(CFG)
    s.update_score("river_overbet", "pressure", 4.0)
    units = [
        {"hand_id": "1", "spot_class": "preflop_open"},
        {"hand_id": "2", "spot_class": "river_overbet"},
    ]
    ranked = s.rank_units(units)
    assert ranked[0]["spot_class"] == "river_overbet"
    assert ranked[0]["_stigmergy_advisory_only"] is True


def test_apply_after_deepsearch_filter_does_not_drop_eligible():
    filter_out = {
        "eligible": [
            {"hand_id": "a", "spot_class": "low"},
            {"hand_id": "b", "spot_class": "high"},
        ],
        "rejected": [],
        "n_eligible": 2,
        "advisory_only": True,
    }
    s = StigmergySpotScores(CFG)
    s.update_score("high", "block", 3.0)
    out = apply_stigmergy_to_deepsearch_filter(filter_out, scores=s)
    assert out["n_eligible"] == 2
    assert len(out["eligible"]) == 2
    assert out["eligible"][0]["spot_class"] == "high"
    assert out["eligible_ranked_by_stigmergy"] is True
    assert out["stigmergy_advisory_only"] is True


def test_module_helper_rank_eligible():
    s = StigmergySpotScores(CFG)
    s.update_score("z", "pressure", 1.0)
    ordered = rank_eligible_spot_classes(["y", "z"], scores=s)
    assert ordered == ["z", "y"]


def test_brief_section_mentions_advisory():
    s = StigmergySpotScores(CFG)
    s.update_score("btn_vs_bb_river", "pressure", 2.0)
    md = stigmergy_brief_section(["btn_vs_bb_river", "other"], scores=s)
    assert "advisory" in md.lower()
    assert "btn_vs_bb_river" in md
    assert "K141" in md


def test_hierarchical_memory_lists_stigmergy_ref():
    mem = json_load_memory()
    refs = mem.get("long_term_refs") or []
    assert any("stigmergy" in str(r) for r in refs), refs


def json_load_memory() -> dict:
    import json

    path = ROOT / "config" / "hu_hierarchical_memory.json"
    return json.loads(path.read_text(encoding="utf-8"))
