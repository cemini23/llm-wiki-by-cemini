"""K164 capability tree routing tests."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "examples"))

from capability_tree import (  # noqa: E402
    CapabilityFrameStack,
    capability_tree_markdown,
    domain_ids,
    load_capability_tree_config,
    simulate_hu_researcher_nested_session,
    validate_exclusive_domains,
    visible_children,
)

CFG = ROOT / "config" / "hu_capability_tree.json"


def test_config_schema_and_notes():
    cfg = load_capability_tree_config(CFG)
    assert cfg["schema"] == "devfun.hu_capability_tree.v1"
    assert cfg["advisory_only"] is True
    assert "2607.11138" in cfg["notes"]
    assert cfg["require_mutually_exclusive_roots"] is True
    assert cfg["nested_work"] == "push_pop"


def test_domains_exclusive_and_nonempty():
    gate = validate_exclusive_domains(load_capability_tree_config(CFG))
    assert gate["pass"] is True
    assert gate["errors"] == []
    ids = domain_ids(load_capability_tree_config(CFG))
    assert set(ids) == {"table", "policy", "memory", "eval", "submit"}


def test_visible_children_capped():
    kids = visible_children("policy", config=CFG)
    assert kids == ["preflop_chart", "postflop_heuristic", "skill_binding"]
    assert len(kids) <= 6


def test_unknown_domain_raises():
    try:
        visible_children("vendors", config=CFG)
        assert False, "expected KeyError"
    except KeyError as exc:
        assert "vendors" in str(exc)


def test_markdown_table_lists_submit_leaf():
    md = capability_tree_markdown(load_capability_tree_config(CFG))
    assert "`submit`" in md
    assert "sandbox_submit" in md


def test_overlap_fails_gate():
    cfg = load_capability_tree_config(CFG)
    cfg["top_domains"][0]["children"] = ["shared_child"]
    cfg["top_domains"][1]["children"] = ["shared_child"]
    gate = validate_exclusive_domains(cfg)
    assert gate["pass"] is False
    assert any("shared_child" in e for e in gate["errors"])


def test_frame_push_pop_returns_parent():
    stack = CapabilityFrameStack(config=load_capability_tree_config(CFG))
    stack.push("eval", label="root")
    stack.push("policy", focus="postflop_heuristic", label="mafp")
    assert stack.depth == 2
    assert stack.visible_slice()["active_domain"] == "policy"
    assert stack.visible_slice()["visible_children"] == ["postflop_heuristic"]
    popped = stack.pop()
    assert popped.label == "mafp"
    assert stack.peek().label == "root"
    assert stack.visible_slice()["active_domain"] == "eval"


def test_submit_requires_prebind():
    stack = CapabilityFrameStack(config=load_capability_tree_config(CFG))
    try:
        stack.push("submit", prebind_ok=False)
        assert False, "expected PermissionError"
    except PermissionError as exc:
        assert "prebind" in str(exc).lower()
    stack.push("submit", focus="prebind_pin", prebind_ok=True)
    assert stack.peek().domain_id == "submit"


def test_hu_researcher_nested_session_smoke():
    result = simulate_hu_researcher_nested_session(config=CFG, prebind_ok=True)
    assert result["ok"] is True
    assert result["final_depth"] == 0
    events = [row["event"] for row in result["transcript"]]
    assert "push_mafp" in events
    assert "push_exploit_nested" in events
    assert any(e.startswith("pop_return:") for e in events)
    assert "push_submit" in events
    depths = [row["slice"]["depth"] for row in result["transcript"]]
    assert max(depths) >= 3
    assert depths[-1] == 0
