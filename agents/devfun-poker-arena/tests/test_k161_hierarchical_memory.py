"""K161 hierarchical session memory tests."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "examples"))

from hierarchical_session_state import (  # noqa: E402
    build_memory_slice_for_decide,
    compute_hierarchical_memory_advisory,
    empty_state,
    estimate_slice_chars,
    evict_completed,
    load_hierarchical_memory_config,
    reset_mid_term,
    update_scratchpad_facts,
    update_short_term,
    append_session_summary,
    upsert_active_goal,
    upsert_recent_job,
)

CFG = ROOT / "config" / "hu_hierarchical_memory.json"


def test_config_schema_and_notes():
    cfg = load_hierarchical_memory_config(CFG)
    assert cfg["schema"] == "devfun.hu_hierarchical_memory.v1"
    assert cfg["advisory_only"] is True
    assert "2607.07666" in cfg["notes"]
    assert cfg["short_term"]["max_hands"] == 8


def test_short_term_ring_cap():
    state = empty_state()
    cfg = load_hierarchical_memory_config(CFG)
    for i in range(12):
        update_short_term(state, {"hand_id": f"h{i}", "action": "fold"}, config=cfg)
    assert len(state["short_term"]["hands"]) == 8
    assert state["short_term"]["hands"][0]["hand_id"] == "h4"


def test_mid_term_summary_cap():
    state = empty_state()
    cfg = load_hierarchical_memory_config(CFG)
    for i in range(5):
        append_session_summary(state, f"summary-{i}", config=cfg)
    assert len(state["mid_term"]["session_summaries"]) == 3


def test_evict_completed_goals_and_jobs():
    state = empty_state()
    upsert_active_goal(state, "g1", {"status": "active", "title": "drill"})
    upsert_active_goal(state, "g2", {"status": "completed", "title": "done"})
    upsert_recent_job(state, "j1", {"status": "completed"})
    upsert_recent_job(state, "j2", {"status": "running"})
    removed = evict_completed(state)
    assert "active_goals:g2" in removed
    assert "recent_jobs:j1" in removed
    assert "g1" in state["mid_term"]["active_goals"]
    assert "j2" in state["mid_term"]["recent_jobs"]


def test_slice_under_budget_and_excludes_forbidden():
    state = empty_state()
    cfg = load_hierarchical_memory_config(CFG)
    update_scratchpad_facts(
        state,
        {"stack_bb": 100, "reasoning": "SHOULD_NOT_APPEAR", "hud": "lag"},
        config=cfg,
    )
    for i in range(8):
        update_short_term(
            state,
            {"hand_id": f"h{i}", "action": "call", "chip_delta": -2},
            config=cfg,
        )
    slice_dict = build_memory_slice_for_decide(state, config=cfg)
    assert estimate_slice_chars(slice_dict) <= cfg["slice_max_chars"]
    assert "reasoning" not in slice_dict["short_term"]["scratchpad_facts"]
    blob = json.dumps(slice_dict)
    assert "action_history" not in blob
    assert "trajectory" not in blob


def test_reset_mid_term_preserves_short():
    state = empty_state()
    update_short_term(state, {"hand_id": "h1", "action": "fold"})
    upsert_active_goal(state, "g1", {"status": "active"})
    reset_mid_term(state)
    assert state["short_term"]["hands"]
    assert state["mid_term"]["active_goals"] == {}


def test_hierarchical_advisory_only():
    slice_dict = build_memory_slice_for_decide(empty_state())
    adv = compute_hierarchical_memory_advisory(slice_dict)
    assert adv["advisory_only"] is True
    assert adv["schema"] == "devfun.hierarchical_memory_advisory.v1"
    assert adv["within_budget"] is True
