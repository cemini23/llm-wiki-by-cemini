"""K141 partial-spec trajectory eval — SWE-INTERACT style phased rubric reveal.

Single-turn tri-verifier pass does not guarantee multi-turn / progressive-spec
recovery. This module scores trajectories where evaluation criteria are only
partially known until a reveal turn (default: action index 2).

Pairs with sandbox_tri_verifier (K132), mechanical invariants (K140), collapse (K136).
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Optional

from sandbox_tri_verifier import is_generic_reasoning, score_trajectory

_SCENARIOS_PATH = Path(__file__).resolve().parent / "partial_spec_scenarios.json"
_DEFAULT_SCENARIO_ID = "researcher_rubric_reveal_v1"


def _load_scenarios() -> dict[str, Any]:
    if not _SCENARIOS_PATH.is_file():
        return {}
    return json.loads(_SCENARIOS_PATH.read_text(encoding="utf-8"))


def load_scenario(scenario_id: str = _DEFAULT_SCENARIO_ID) -> dict[str, Any]:
    scenarios = _load_scenarios()
    if scenario_id not in scenarios:
        raise KeyError(f"unknown partial-spec scenario: {scenario_id}")
    return dict(scenarios[scenario_id])


def active_dimensions(action_index: int, scenario: dict[str, Any]) -> list[str]:
    """1-based action index — phase 1 before reveal_at_action, phase 2 after."""
    reveal = int(scenario.get("reveal_at_action", 2))
    if action_index < reveal:
        return list(scenario.get("phase1_dimensions") or [])
    return list(scenario.get("phase2_dimensions") or [])


def _dim_pass(dim_data: dict[str, Any]) -> bool:
    return bool(dim_data.get("pass", False))


def phased_action_pass(
    scored_action: dict[str, Any],
    action_index: int,
    scenario: dict[str, Any],
) -> bool:
    dims = scored_action.get("dimensions") or {}
    active = active_dimensions(action_index, scenario)
    if not active:
        return bool(scored_action.get("pass", False))
    return all(_dim_pass(dims.get(name) or {}) for name in active)


def verify_vague_start(
    scored_actions: list[dict[str, Any]],
    scenario: dict[str, Any],
) -> dict[str, Any]:
    """Phase 1 only — agent must stay legal under minimal rubric."""
    reveal = int(scenario.get("reveal_at_action", 2))
    phase1 = scored_actions[: max(0, reveal - 1)]
    if not phase1:
        return {"pass": True, "checked": 0, "failed": 0}

    failed = 0
    for idx, row in enumerate(phase1, start=1):
        if not phased_action_pass(row, idx, scenario):
            failed += 1
    return {
        "pass": failed == 0,
        "checked": len(phase1),
        "failed": failed,
        "hazard": None if failed == 0 else "partial_spec:vague_start_fail",
    }


def verify_progressive_reveal(
    scored_actions: list[dict[str, Any]],
    scenario: dict[str, Any],
) -> dict[str, Any]:
    """Post-reveal actions must satisfy full rubric dimensions."""
    reveal = int(scenario.get("reveal_at_action", 2))
    phase2 = scored_actions[reveal - 1 :]
    if not phase2:
        return {"pass": True, "checked": 0, "failed": 0}

    failed = 0
    for offset, row in enumerate(phase2):
        idx = reveal + offset
        if not phased_action_pass(row, idx, scenario):
            failed += 1
    return {
        "pass": failed == 0,
        "checked": len(phase2),
        "failed": failed,
        "hazard": None if failed == 0 else "partial_spec:progressive_reveal_fail",
    }


def _reasoning_text(payload: dict[str, Any]) -> str:
    for key in ("reasoning_text", "reasoning", "message"):
        val = payload.get(key)
        if isinstance(val, str) and val.strip():
            return val.strip()
    return ""


def verify_requirement_memory(
    events: list[dict[str, Any]],
    scored_actions: list[dict[str, Any]],
    scenario: dict[str, Any],
) -> dict[str, Any]:
    """After reveal, generic reasoning is forbidden; earlier turns exempt."""
    memory = scenario.get("memory") or {}
    if not memory.get("forbid_generic_reasoning_after_reveal", True):
        return {"pass": True, "checked": 0, "violations": 0}

    reveal = int(scenario.get("reveal_at_action", 2))
    violations = 0
    checked = 0
    for i in range(reveal - 1, min(len(events), len(scored_actions))):
        checked += 1
        payload = events[i].get("payload") or {}
        if is_generic_reasoning(_reasoning_text(payload)):
            violations += 1
    return {
        "pass": violations == 0,
        "checked": checked,
        "violations": violations,
        "hazard": None if violations == 0 else "partial_spec:requirement_memory_fail",
    }


def verify_rework_detection(
    events: list[dict[str, Any]],
    scenario: dict[str, Any],
) -> dict[str, Any]:
    """Detect excessive action flip-flops within the same street."""
    rework = scenario.get("rework") or {}
    max_flips = int(rework.get("max_action_flips_per_street", 2))

    by_street: dict[str, list[str]] = {}
    for evt in events:
        table = evt.get("table") or {}
        street = str(table.get("street") or "unknown").lower()
        action = str(evt.get("action") or "").lower()
        by_street.setdefault(street, []).append(action)

    flip_violations = 0
    for street, actions in by_street.items():
        if len(actions) < 3:
            continue
        flips = sum(1 for a, b in zip(actions, actions[1:]) if a != b)
        if flips > max_flips:
            flip_violations += 1

    return {
        "pass": flip_violations == 0,
        "streets_checked": len(by_street),
        "flip_violations": flip_violations,
        "hazard": None if flip_violations == 0 else "partial_spec:rework_flip_flop",
    }


def verify_partial_spec_trajectory(
    events: list[dict[str, Any]],
    *,
    scenario_id: str = _DEFAULT_SCENARIO_ID,
    base_score: Optional[dict[str, Any]] = None,
) -> dict[str, Any]:
    """Run K141 partial-spec checks on a trajectory event list."""
    scenario = load_scenario(scenario_id)
    base = base_score if base_score is not None else score_trajectory(events)
    scored = base.get("actions") or []

    vague = verify_vague_start(scored, scenario)
    reveal = verify_progressive_reveal(scored, scenario)
    memory = verify_requirement_memory(events, scored, scenario)
    rework = verify_rework_detection(events, scenario)

    checks = {
        "vague_start": vague,
        "progressive_reveal": reveal,
        "requirement_memory": memory,
        "rework_detection": rework,
    }
    all_pass = all(c.get("pass", False) for c in checks.values())

    return {
        "scenario_id": scenario_id,
        "partial_spec_pass": all_pass,
        "checks": checks,
        "base_trajectory": {
            "trajectory_pass": base.get("trajectory_pass"),
            "summary": base.get("summary"),
        },
    }


def format_partial_spec_report(result: dict[str, Any]) -> str:
    lines = [
        "=" * 50,
        "K141 PARTIAL-SPEC TRAJECTORY REPORT",
        "=" * 50,
        f"Scenario: {result.get('scenario_id')}",
        f"Overall: {'PASS' if result.get('partial_spec_pass') else 'FAIL'}",
    ]
    for name, check in (result.get("checks") or {}).items():
        status = "PASS" if check.get("pass") else f"FAIL ({check.get('hazard')})"
        lines.append(f"  {name}: {status}")
    base = result.get("base_trajectory") or {}
    summary = base.get("summary") or {}
    if summary:
        lines.append(
            f"Base tri-verifier: {summary.get('passed_actions', 0)}/"
            f"{summary.get('total_actions', 0)} actions"
        )
    return "\n".join(lines)
