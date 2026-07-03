"""Tri-verifier for static-agent bundle regression — correctness, efficiency, critical-point.

FaraGen1.5 tri-verifier pattern (arXiv 2606.20785) adapted for arena-tool MCP bundle eval.
Scores trajectories on three dimensions: correctness, efficiency, critical-point adherence.

Complements K131 ToolBench-X hazard taxonomy:
- timeout (efficiency fail)
- bad amount / illegal action (correctness fail)
- generic reasoning (critical-point fail)

No external deps beyond stdlib.
"""
from __future__ import annotations

import json
import os
import re
from typing import Any, Optional

from sandbox_mechanical_invariants import verify_mechanical_invariants
from tool_rl_collapse_detector import verify_action_payload_collapse

# Import FALLBACK_REASONING patterns from output_sanitize for is_generic_reasoning
# Duplicated here to avoid import dependency in sandbox bundle context
FALLBACK_REASONING = '{vr: "std", ke: "legal", pp: "pot control"}'
GENERIC_MESSAGE = "act"

# K131 hazard patterns (ToolBench-X taxonomy)
_GENERIC_PATTERNS = [
    re.compile(r'\{vr:\s*"std"\s*,\s*ke:\s*"legal"\s*,\s*pp:\s*"pot control"\s*\}', re.IGNORECASE),
    re.compile(r'vr:\s*"std"', re.IGNORECASE),
    re.compile(r'ke:\s*"legal"', re.IGNORECASE),
    re.compile(r'pp:\s*"pot control"', re.IGNORECASE),
    re.compile(r'^act\s*$', re.IGNORECASE),
    re.compile(r'fallback', re.IGNORECASE),
    re.compile(r'placeholder', re.IGNORECASE),
    re.compile(r'discard cycle', re.IGNORECASE),
    re.compile(r'minimal legal action', re.IGNORECASE),
]

# Efficiency thresholds (seconds)
_EFFICIENCY_HARD_DEADLINE_S = 10.0  # Hard ceiling per decision
_EFFICIENCY_SOFT_RATIO = 0.9  # Soft limit: 90% of deadline
_MAX_IDLE_POLL_LOOPS = 3  # Excessive polling threshold


def verify_correctness(
    action: str,
    allowed_actions: list[str],
    *,
    action_payload: Optional[dict[str, Any]] = None,
    allowed_block: Optional[dict[str, Any]] = None,
) -> dict[str, Any]:
    """Verify action is legal per allowedActions; amount within raise/bet range when present."""
    result: dict[str, Any] = {
        "pass": False,
        "hazard": None,
        "details": {},
    }

    if not allowed_actions:
        result["hazard"] = "correctness:no_allowed_actions_oracle"
        result["details"]["error"] = "allowed_actions list is empty or None"
        return result

    norm_action = action.lower().strip()
    norm_allowed = [a.lower().strip() for a in allowed_actions]

    if norm_action not in norm_allowed:
        result["hazard"] = "correctness:illegal_action"
        result["details"]["action"] = action
        result["details"]["allowed"] = allowed_actions
        return result

    payload = action_payload or {}
    amount = payload.get("amount")
    block = allowed_block or {}

    if amount is not None and norm_action in ("bet", "raise", "all-in"):
        try:
            amt = int(amount)
        except (TypeError, ValueError):
            result["hazard"] = "correctness:bad_amount"
            result["details"]["amount"] = amount
            result["details"]["error"] = "amount is not an integer"
            return result

        range_key = "raiseRange" if norm_action in ("raise", "all-in") else "betRange"
        rng = block.get(range_key) or block.get("raise_range") or block.get("bet_range")
        if isinstance(rng, dict):
            min_amt = rng.get("min")
            max_amt = rng.get("max")
            if min_amt is not None and amt < int(min_amt):
                result["hazard"] = "correctness:bad_amount"
                result["details"]["amount"] = amt
                result["details"]["min"] = min_amt
                result["details"]["max"] = max_amt
                return result
            if max_amt is not None and amt > int(max_amt):
                result["hazard"] = "correctness:bad_amount"
                result["details"]["amount"] = amt
                result["details"]["min"] = min_amt
                result["details"]["max"] = max_amt
                return result

    result["pass"] = True
    result["details"]["action"] = action
    result["details"]["allowed"] = allowed_actions
    return result


def verify_efficiency(
    elapsed_s: float,
    deadline_s: float,
    poll_loops: int = 0,
    *,
    hard_deadline_s: float = _EFFICIENCY_HARD_DEADLINE_S,
    soft_ratio: float = _EFFICIENCY_SOFT_RATIO,
    max_poll_loops: int = _MAX_IDLE_POLL_LOOPS,
) -> dict[str, Any]:
    """Verify action within per-decision budget; no idle poll loops burning match clock.

    Args:
        elapsed_s: Actual time elapsed for decision computation
        deadline_s: Deadline/budget for this decision (from table or config)
        poll_loops: Number of idle poll loops consumed (0 = no polling)
        hard_deadline_s: Hard deadline threshold (default: _EFFICIENCY_HARD_DEADLINE_S)
        soft_ratio: Soft deadline ratio (default: _EFFICIENCY_SOFT_RATIO)
        max_poll_loops: Max allowed poll loops (default: _MAX_IDLE_POLL_LOOPS)

    Returns:
        Dict with pass (bool), hazard (str or None), and efficiency metrics
    """
    result: dict[str, Any] = {
        "pass": False,
        "hazard": None,
        "details": {},
    }

    result["details"]["elapsed_s"] = elapsed_s
    result["details"]["deadline_s"] = deadline_s
    result["details"]["poll_loops"] = poll_loops
    result["details"]["ratio"] = elapsed_s / deadline_s if deadline_s > 0 else None

    # K131 hazard: timeout (exceeded hard deadline)
    if elapsed_s > hard_deadline_s:
        result["hazard"] = "efficiency:timeout_hard_deadline"
        return result

    # K131 hazard: exceeded soft deadline (inefficient)
    if deadline_s > 0 and elapsed_s > (deadline_s * soft_ratio):
        result["hazard"] = "efficiency:deadline_exceeded_soft"
        return result

    # K131 hazard: excessive idle polling (burning match clock)
    if poll_loops > max_poll_loops:
        result["hazard"] = "efficiency:excessive_polling"
        return result

    result["pass"] = True
    return result


def verify_critical_point(
    action_payload: dict[str, Any],
    table: Optional[dict] = None,
) -> dict[str, Any]:
    """Verify reasoning_text is hand-specific (not generic); critical point timing.

    For static-agent bundles: reasoning must be hand-specific, not generic placeholders.
    Arena rejects generic reasoning on trajectory.

    Args:
        action_payload: The action payload dict (contains reasoning, reasoning_text, message)
        table: Optional table state for critical-point context (e.g., join_pve timing)

    Returns:
        Dict with pass (bool), hazard (str or None), and critical-point details
    """
    result: dict[str, Any] = {
        "pass": False,
        "hazard": None,
        "details": {},
    }

    # Extract reasoning fields
    reasoning = action_payload.get("reasoning") or ""
    reasoning_text = action_payload.get("reasoning_text") or ""
    message = action_payload.get("message") or ""

    result["details"]["reasoning_present"] = bool(reasoning)
    result["details"]["reasoning_text_present"] = bool(reasoning_text)
    result["details"]["message_present"] = bool(message)

    # Check for generic reasoning (K131 hazard pattern)
    combined_text = f"{reasoning} {reasoning_text} {message}"

    if is_generic_reasoning(combined_text):
        result["hazard"] = "critical_point:generic_reasoning"
        result["details"]["generic_detected"] = True
        result["details"]["sample"] = (reasoning_text or reasoning or message)[:100]
        return result

    # Check hand-specificity: reasoning should reference concrete hand elements
    # e.g., hole cards, board texture, position, stack depth, pot odds
    hand_specific_markers = [
        r'[akqjt2-9][cdhs]',  # Card notation (e.g., As, Kh)
        r'board',
        r'flop',
        r'turn',
        r'river',
        r'pot',
        r'stack',
        r'position',
        r'bb',  # big blind
        r'sb',  # small blind
        r'btn',  # button
        r'equity',
        r'odds',
        r'\d+\.?\d*',  # Numeric values (bets, odds, percentages)
    ]

    has_hand_specific = False
    for marker in hand_specific_markers:
        if re.search(marker, combined_text, re.IGNORECASE):
            has_hand_specific = True
            break

    # Note: Not requiring hand-specific markers to avoid false negatives on
    # legitimate abstract reasoning. The key rejection is generic patterns.
    result["details"]["hand_specific_markers_found"] = has_hand_specific

    # Critical point timing check (optional table context)
    if table is not None:
        # Verify agent didn't read harness/assets before proper initialization
        # This is a conceptual check - actual enforcement is harness-side
        table_phase = table.get("phase") or table.get("bettingRound")
        result["details"]["table_phase"] = table_phase

        # Session completion without forfeit check proxy
        session_status = table.get("sessionStatus") or table.get("status")
        if session_status and session_status.lower() in ("forfeit", "timeout", "error"):
            result["hazard"] = "critical_point:session_forfeit"
            return result

    result["pass"] = True
    return result


def is_generic_reasoning(text: str) -> bool:
    """Reject FALLBACK_REASONING patterns from output_sanitize.

    Returns True if the text matches generic/placeholder reasoning patterns
    that Arena rejects on trajectory.

    Args:
        text: The reasoning text to check

    Returns:
        True if text is generic/placeholder reasoning
    """
    if not text or not text.strip():
        return True  # Empty reasoning is generic

    text_normalized = text.strip()

    for pattern in _GENERIC_PATTERNS:
        if pattern.search(text_normalized):
            return True

    # Check for exact match with FALLBACK_REASONING
    if FALLBACK_REASONING in text_normalized:
        return True

    # Check for GENERIC_MESSAGE
    if text_normalized.lower() == GENERIC_MESSAGE.lower():
        return True

    return False


def score_action(
    action: str,
    allowed_actions: list[str],
    elapsed_s: float,
    deadline_s: float,
    action_payload: dict[str, Any],
    table: Optional[dict] = None,
    poll_loops: int = 0,
    *,
    thresholds: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Score a single action across all three verifier dimensions.

    Args:
        action: The action taken
        allowed_actions: List of legal actions from table state
        elapsed_s: Decision elapsed time
        deadline_s: Decision deadline
        action_payload: Full action payload (for reasoning check)
        table: Optional table state
        poll_loops: Number of poll loops used
        thresholds: Optional dict with deadline_hard_s, soft_ratio, max_poll_loops

    Returns:
        Dict with pass per dimension and overall pass
    """
    # Unpack thresholds for efficiency check
    eff_kwargs = {}
    if thresholds:
        eff_kwargs["hard_deadline_s"] = thresholds.get("deadline_hard_s", _EFFICIENCY_HARD_DEADLINE_S)
        eff_kwargs["soft_ratio"] = thresholds.get("soft_ratio", _EFFICIENCY_SOFT_RATIO)
        eff_kwargs["max_poll_loops"] = thresholds.get("max_poll_loops", _MAX_IDLE_POLL_LOOPS)

    mechanical_invariants = verify_mechanical_invariants(
        table,
        action,
        allowed_actions,
        action_payload=action_payload,
    )

    correctness = verify_correctness(
        action,
        allowed_actions,
        action_payload=action_payload,
        allowed_block=(table or {}).get("allowedActions") if table else None,
    )
    efficiency = verify_efficiency(elapsed_s, deadline_s, poll_loops, **eff_kwargs)
    critical_point = verify_critical_point(action_payload, table)
    collapse_result = verify_action_payload_collapse(action_payload)
    tool_rl_collapse = {
        "pass": collapse_result["mode"] == "ok",
        "hazard": collapse_result["hazards"][0] if collapse_result["hazards"] else None,
        "mode": collapse_result["mode"],
        "hazards": collapse_result["hazards"],
        "details": collapse_result["details"],
    }

    all_pass = (
        mechanical_invariants.get("pass", False)
        and correctness.get("pass", False)
        and efficiency.get("pass", False)
        and critical_point.get("pass", False)
        and tool_rl_collapse.get("pass", False)
    )

    return {
        "action": action,
        "pass": all_pass,
        "mechanical_invariants": {
            "pass": mechanical_invariants.get("pass", False),
            "hazards": mechanical_invariants.get("hazards", []),
            "details": mechanical_invariants.get("details", {}),
        },
        "dimensions": {
            "mechanical_invariants": mechanical_invariants,
            "correctness": correctness,
            "efficiency": efficiency,
            "critical_point": critical_point,
            "tool_rl_collapse": tool_rl_collapse,
        },
    }


def score_trajectory(events: list[dict[str, Any]]) -> dict[str, Any]:
    """Score a trajectory (list of action events) across all three dimensions.

    Each event dict should contain:
        - action: str
        - allowed_actions: list[str]
        - elapsed_s: float
        - deadline_s: float
        - payload: dict (action payload with reasoning)
        - table: dict (optional)
        - poll_loops: int (optional, default 0)

    Args:
        events: List of action event dicts from a session/trajectory

    Returns:
        Dict with summary stats and per-action scores
    """
    scored_actions: list[dict[str, Any]] = []

    for evt in events:
        score = score_action(
            action=evt.get("action", ""),
            allowed_actions=evt.get("allowed_actions", []),
            elapsed_s=evt.get("elapsed_s", 0.0),
            deadline_s=evt.get("deadline_s", 10.0),
            action_payload=evt.get("payload", {}),
            table=evt.get("table"),
            poll_loops=evt.get("poll_loops", 0),
        )
        scored_actions.append(score)

    # Aggregate metrics
    total = len(scored_actions)
    passed = sum(1 for s in scored_actions if s.get("pass", False))

    dim_counts: dict[str, dict[str, int]] = {
        "mechanical_invariants": {"pass": 0, "fail": 0, "hazards": {}},
        "correctness": {"pass": 0, "fail": 0, "hazards": {}},
        "efficiency": {"pass": 0, "fail": 0, "hazards": {}},
        "critical_point": {"pass": 0, "fail": 0, "hazards": {}},
        "tool_rl_collapse": {"pass": 0, "fail": 0, "hazards": {}},
    }

    for s in scored_actions:
        dims = s.get("dimensions", {})
        for dim_name, dim_data in dims.items():
            if dim_name not in dim_counts:
                continue
            if dim_data.get("pass", False):
                dim_counts[dim_name]["pass"] += 1
            else:
                dim_counts[dim_name]["fail"] += 1
                hazard_list = dim_data.get("hazards")
                if isinstance(hazard_list, list) and hazard_list:
                    for hazard in hazard_list:
                        dim_counts[dim_name]["hazards"][hazard] = (
                            dim_counts[dim_name]["hazards"].get(hazard, 0) + 1
                        )
                else:
                    hazard = dim_data.get("hazard")
                    if hazard:
                        dim_counts[dim_name]["hazards"][hazard] = (
                            dim_counts[dim_name]["hazards"].get(hazard, 0) + 1
                        )

    result = {
        "trajectory_pass": passed == total and total > 0,
        "summary": {
            "total_actions": total,
            "passed_actions": passed,
            "failed_actions": total - passed,
            "pass_rate": passed / total if total > 0 else 0.0,
        },
        "dimensions": dim_counts,
        "actions": scored_actions,
    }
    return _attach_partial_spec(result, events)


def _attach_partial_spec(result: dict[str, Any], events: list[dict[str, Any]]) -> dict[str, Any]:
    """K141 phased rubric eval — supplemental; does not change trajectory_pass by default."""
    try:
        from sandbox_partial_spec_eval import verify_partial_spec_trajectory

        pspec = verify_partial_spec_trajectory(events, base_score=result)
        result["partial_spec"] = pspec
        if os.environ.get("CEMINI_PARTIAL_SPEC_GATE", "").strip().lower() in ("1", "true", "yes"):
            result["trajectory_pass"] = bool(
                result.get("trajectory_pass") and pspec.get("partial_spec_pass")
            )
    except Exception as exc:  # pragma: no cover - scenario file missing in broken deploy
        result["partial_spec"] = {
            "partial_spec_pass": False,
            "error": str(exc),
        }
    return result


def format_score_report(score_result: dict[str, Any]) -> str:
    """Format a score result as a readable string report.

    Args:
        score_result: The result from score_action or score_trajectory

    Returns:
        Formatted string report
    """
    lines: list[str] = []

    if "trajectory_pass" in score_result:
        # Trajectory report
        lines.append("=" * 50)
        lines.append("TRI-VERIFIER TRAJECTORY REPORT")
        lines.append("=" * 50)
        lines.append(f"Overall: {'PASS' if score_result['trajectory_pass'] else 'FAIL'}")

        summary = score_result.get("summary", {})
        lines.append(f"Actions: {summary.get('passed_actions', 0)}/{summary.get('total_actions', 0)} passed")
        lines.append(f"Pass rate: {summary.get('pass_rate', 0.0):.1%}")

        lines.append("\nDimension breakdown:")
        dims = score_result.get("dimensions", {})
        for dim_name, dim_data in dims.items():
            total = dim_data["pass"] + dim_data["fail"]
            rate = dim_data["pass"] / total if total > 0 else 0.0
            lines.append(f"  {dim_name}: {dim_data['pass']}/{total} ({rate:.1%})")
            if dim_data["hazards"]:
                lines.append(f"    Hazards: {dim_data['hazards']}")
    else:
        # Single action report
        lines.append("=" * 50)
        lines.append("TRI-VERIFIER ACTION REPORT")
        lines.append("=" * 50)
        lines.append(f"Action: {score_result.get('action', 'unknown')}")
        lines.append(f"Overall: {'PASS' if score_result.get('pass') else 'FAIL'}")

        dims = score_result.get("dimensions", {})
        for dim_name, dim_data in dims.items():
            status = "PASS" if dim_data.get("pass") else f"FAIL ({dim_data.get('hazard', 'unknown')})"
            lines.append(f"  {dim_name}: {status}")

    return "\n".join(lines)


if __name__ == "__main__":
    # Example/demo usage
    example_events = [
        {
            "action": "raise",
            "allowed_actions": ["fold", "check", "call", "raise"],
            "elapsed_s": 2.5,
            "deadline_s": 10.0,
            "payload": {
                "action": "raise",
                "amount": 100,
                "reasoning_text": "3bet from BTN with AKs, board is dry",
                "message": "value bet",
            },
            "table": {"phase": "preflop"},
            "poll_loops": 0,
        },
        {
            "action": "call",
            "allowed_actions": ["fold", "call", "raise"],
            "elapsed_s": 1.0,
            "deadline_s": 10.0,
            "payload": {
                "action": "call",
                "reasoning_text": FALLBACK_REASONING,  # Generic - should fail
            },
            "poll_loops": 0,
        },
        {
            "action": "all-in",
            "allowed_actions": ["fold", "call"],  # all-in not allowed - should fail
            "elapsed_s": 3.0,
            "deadline_s": 10.0,
            "payload": {
                "action": "all-in",
                "reasoning_text": "bluff shove on wet board",
            },
            "poll_loops": 5,  # Excessive polling - should fail efficiency
        },
    ]

    result = score_trajectory(example_events)
    print(format_score_report(result))
    print("\n" + "=" * 50)
    print("JSON OUTPUT:")
    print(json.dumps(result, indent=2))
