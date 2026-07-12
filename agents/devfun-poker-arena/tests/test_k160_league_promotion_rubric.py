"""K160 league promotion rubric — yardstick vs style gaps."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "examples"))

from researcher_trajectory_summary import compute_league_promotion_rubric_advisory  # noqa: E402


def test_rubric_advisory_only():
    out = compute_league_promotion_rubric_advisory()
    assert out["advisory_only"] is True
    assert out["schema"] == "devfun.league_promotion_rubric.v1"
    assert out["footsiesgym_env"] == "footsiesgym_separate"


def test_rubric_yardstick_gap():
    grade = {"pct_pass": 0.5, "n_pass": 2, "n_checked": 4}
    out = compute_league_promotion_rubric_advisory(yardstick_grade=grade)
    assert out["yardstick_gap"] is True
    assert "yardstick_pool_incomplete" in out["gaps"]


def test_rubric_style_gap():
    drift = {"style_ok": False, "d_policy_tv": 0.9}
    out = compute_league_promotion_rubric_advisory(style_drift=drift)
    assert out["style_gap"] is True
    assert "style_drift_exceeds_tv" in out["gaps"]


def test_rubric_footsiesgym_separate_note():
    adv = {"disconnect": True, "skill_bb100": 5.0, "yardstick_bb100": -50.0}
    out = compute_league_promotion_rubric_advisory(exploitability_advisory=adv)
    assert out["footsiesgym_note"] is not None
    assert "FootsiesGym" in out["footsiesgym_note"]
    assert out["yardstick_gap"] is False


def test_gate_failures_exclude_style_metrics():
    """Style/yardstick must not appear in hard gate_failures."""
    from researcher_trajectory_summary import build_manifest, evaluate_gates

    manifest = build_manifest(
        selfplay_summary={"decision_count": 10, "axes": {"M8_hallucination_rate": 0.0}},
        arena_summary={"hero_submissions": 1},
        bundle_dir=Path("/tmp/test-bundle"),
        yardstick_pool_grade={"pct_pass": 0.0},
        style_drift={"style_ok": False, "d_policy_tv": 0.9},
        league_promotion_rubric={"gaps": ["style_drift_exceeds_tv"]},
    )
    failures = evaluate_gates(manifest)
    joined = " ".join(failures).lower()
    assert "style" not in joined
    assert "yardstick" not in joined
