"""K139 DeepSearch scaffold + staged reflection (delta on K161)."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "examples"))

from researcher_trajectory_summary import (  # noqa: E402
    filter_deepsearch_units,
    load_deepsearch_trajectory_filter_config,
    scaffold_block_for_brief,
    staged_reflection_hint,
)

CFG = ROOT / "config" / "hu_deepsearch_trajectory_filter.json"

_OK_TAGS = {
    "progress_verification": True,
    "grounded_reflection": True,
    "failure_recovery": True,
    "teacher_imitation_only": False,
}


def _unit(hand_id: str, *, spot: str, experience: str = "", **extra):
    u = {
        "hand_id": hand_id,
        "spot_class": spot,
        "tags": dict(_OK_TAGS),
        "street": "river",
        "hole_key": "AsKd",
        "board": ["2c", "2d", "7h", "9s", "Jc"],
        "reasoning": "hero AsKd missed value on Jc",
        "verified": True,
        "post_loss_action_changed": True,
    }
    if experience:
        u["experience"] = experience
        u["scaffold"] = {"experience": experience}
    u.update(extra)
    return u


def test_config_has_scaffold_fields():
    cfg = load_deepsearch_trajectory_filter_config(CFG)
    assert cfg["advisory_only"] is True
    assert "scaffold_fields" in cfg
    for k in ("completed_list", "todo_list", "experience", "information"):
        assert k in cfg["scaffold_fields"]
    assert "missing_experience_after_repeat_fails" in cfg["drop_if"]
    assert cfg["scaffold_require_experience_after_fails"] == 2
    # K161 tags remain source of truth
    assert "progress_verification" in cfg["required_tags"]


def test_first_fail_eligible_without_experience():
    units = [_unit("a1", spot="river|tpk|miss")]
    out = filter_deepsearch_units(units, config=CFG)
    assert out["n_eligible"] == 1
    assert out["n_rejected"] == 0


def test_repeat_fail_without_experience_dropped():
    units = [
        _unit("a1", spot="river|tpk|miss"),
        _unit("a2", spot="river|tpk|miss"),  # 2nd fail, no experience
    ]
    out = filter_deepsearch_units(units, config=CFG)
    assert out["n_eligible"] == 1
    assert out["n_rejected"] == 1
    assert out["rejected"][0]["reason"] == "missing_experience_after_repeat_fails"
    assert out["rejected"][0]["hand_id"] == "a2"


def test_repeat_fail_with_experience_eligible():
    units = [
        _unit("a1", spot="river|tpk|miss"),
        _unit(
            "a2",
            spot="river|tpk|miss",
            experience="do not overfold trip boards vs passive HUD",
        ),
    ]
    out = filter_deepsearch_units(units, config=CFG)
    assert out["n_eligible"] == 2
    assert out["n_rejected"] == 0


def test_staged_reflection_soft_then_strong():
    soft = staged_reflection_hint(1, config=CFG)
    strong = staged_reflection_hint(2, config=CFG)
    assert "hud" in soft.lower() or "sizing" in soft.lower()
    assert soft != strong
    assert "grounded" in strong.lower() or "board" in strong.lower() or "leak" in strong.lower()


def test_scaffold_block_for_brief():
    block = scaffold_block_for_brief(
        report_text="street=River board=2c2d7h action=fold",
        leak_hint="overfold river",
        fail_count=2,
        config=CFG,
    )
    assert isinstance(block["completed_list"], list)
    assert isinstance(block["todo_list"], list)
    assert block["experience"]
    assert block["information"]
    assert "reflection_hint" in block
