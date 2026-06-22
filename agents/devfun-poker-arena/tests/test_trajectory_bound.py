"""Unit tests for cemini_trajectory_bound WS-A math."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "examples"))

from cemini_trajectory_bound import (  # noqa: E402
    BoundConfig,
    DecisionContribution,
    TrajectoryBoundState,
    compose_decision,
    contribution_from_features,
    evaluate_veto,
    per_decision_bounds,
    propagate,
    PredicateBound,
)


def _cfg() -> BoundConfig:
    return BoundConfig(veto_threshold=0.05, composition_mode="independent")


def test_compose_independent_vs_union():
    bounds = [PredicateBound("a", 0.1), PredicateBound("b", 0.2)]
    independent = compose_decision(bounds, "independent")
    union = compose_decision(bounds, "union")
    assert independent < union
    assert 0.0 <= independent <= 1.0


def test_propagate_monotonic():
    cfg = _cfg()
    state = TrajectoryBoundState()
    features = {
        "hand_id": 1,
        "action": "bet",
        "street": "River",
        "reasoning": "value",
        "hole_key": "AsKd",
        "equity": 0.2,
        "sims": 100,
        "matches_regression_forbidden": False,
        "available_actions": {"bet": True, "fold": True},
    }
    c1 = contribution_from_features(features, cfg)
    s1 = propagate(state, c1)
    c2 = contribution_from_features({**features, "action": "raise"}, cfg)
    s2 = propagate(s1, c2)
    assert s2.cumulative_risk >= s1.cumulative_risk


def test_evaluate_veto_triggers():
    cfg = _cfg()
    state = TrajectoryBoundState(hand_id=1, cumulative_risk=0.2)
    result = evaluate_veto(state, {"check": True, "fold": True}, cfg)
    assert result.veto
    assert result.action == "check"


def test_per_decision_bounds_mc_equity():
    cfg = BoundConfig(river_bluff_floor=0.45, composition_mode="independent")
    bounds = per_decision_bounds(
        {
            "action": "bet",
            "equity": 0.15,
            "sims": 50,
            "reasoning": "",
            "hole_key": "7c2d",
            "matches_regression_forbidden": False,
            "available_actions": {"bet": True},
        },
        cfg,
    )
    mc = next(b for b in bounds if b.name == "mc_equity")
    assert mc.u > 0.0
