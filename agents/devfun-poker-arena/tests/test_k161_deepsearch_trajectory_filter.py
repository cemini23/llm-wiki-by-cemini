"""K161 DeepSearch trajectory filter tests."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "examples"))

from researcher_trajectory_summary import (  # noqa: E402
    build_failure_mining_units,
    build_manifest,
    compute_deepsearch_trajectory_filter_advisory,
    evaluate_gates,
    filter_deepsearch_units,
    infer_mining_tags,
    load_deepsearch_trajectory_filter_config,
)

CFG = ROOT / "config" / "hu_deepsearch_trajectory_filter.json"


def test_config_loads():
    cfg = load_deepsearch_trajectory_filter_config(CFG)
    assert cfg["schema"] == "devfun.hu_deepsearch_trajectory_filter.v1"
    assert "progress_verification" in cfg["required_tags"]
    assert cfg["advisory_only"] is True


def test_all_three_tags_eligible():
    unit = {
        "hand_id": "ok1",
        "tags": {
            "progress_verification": True,
            "grounded_reflection": True,
            "failure_recovery": True,
            "teacher_imitation_only": False,
        },
    }
    out = filter_deepsearch_units([unit], config=CFG)
    assert out["n_eligible"] == 1
    assert out["n_rejected"] == 0


def test_missing_tag_rejected():
    unit = {
        "hand_id": "bad1",
        "tags": {
            "progress_verification": True,
            "grounded_reflection": True,
            "failure_recovery": False,
        },
    }
    out = filter_deepsearch_units([unit], config=CFG)
    assert out["n_rejected"] == 1
    assert out["rejected"][0]["reason"] == "missing_required_tags"


def test_teacher_imitation_rejected():
    unit = {
        "hand_id": "teach1",
        "tags": {
            "progress_verification": True,
            "grounded_reflection": True,
            "failure_recovery": True,
            "teacher_imitation_only": True,
        },
    }
    out = filter_deepsearch_units([unit], config=CFG)
    assert out["rejected"][0]["reason"] == "teacher_imitation_only"


def test_infer_grounded_from_hole_in_reasoning():
    unit = {
        "hole_key": "AsKd",
        "board": [],
        "reasoning": "hero AsKd missed value",
        "verified": True,
        "post_loss_action_changed": True,
    }
    tags = infer_mining_tags(unit)
    assert tags["grounded_reflection"] is True
    assert tags["progress_verification"] is True
    assert tags["failure_recovery"] is True


def test_build_failure_mining_units_from_losses():
    rows = [
        {"type": "hand_result", "hand_id": "a", "chip_delta": -10, "action": "call"},
        {"type": "hand_result", "hand_id": "b", "chip_delta": 4, "action": "raise"},
        {"type": "hand_result", "hand_id": "c", "chip_delta": -2, "action": "fold"},
    ]
    units = build_failure_mining_units(rows)
    assert len(units) == 2
    assert units[0]["hand_id"] == "a"
    assert units[0]["next_hand_chip_delta"] == 4.0


def test_advisory_not_in_gate_failures():
    rows = [
        {
            "type": "hand_result",
            "hand_id": "x",
            "chip_delta": -5,
            "teacher_imitation_only": True,
            "tags": {
                "progress_verification": True,
                "grounded_reflection": True,
                "failure_recovery": True,
                "teacher_imitation_only": True,
            },
        }
    ]
    adv = compute_deepsearch_trajectory_filter_advisory(rows, config=CFG)
    assert adv["advisory_only"] is True
    manifest = build_manifest(
        selfplay_summary={"decision_count": 3, "axes": {"M8_hallucination_rate": 0.0}},
        arena_summary={"hero_submissions": 1},
        bundle_dir=Path("/tmp/k161-test"),
        deepsearch_trajectory_filter=adv,
    )
    joined = " ".join(evaluate_gates(manifest)).lower()
    assert "deepsearch" not in joined
    assert "teacher" not in joined
    assert manifest["deepsearch_trajectory_filter"]["n_rejected"] >= 1
