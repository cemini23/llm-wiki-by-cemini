"""Track B tests for sandbox tri-verifier scoring."""
from __future__ import annotations

import importlib
import inspect
import sys
from pathlib import Path
from typing import Any

import pytest

ROOT = Path(__file__).resolve().parent.parent
EXAMPLES = ROOT / "examples"
HELPERS = ROOT / "tests" / "helpers"

for path in (EXAMPLES, HELPERS):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

from cemini_tables import hu_sb_unopened  # noqa: E402
from output_sanitize import FALLBACK_REASONING  # noqa: E402

_IMPORT_ERROR: Exception | None = None
_VERIFIER_MOD = None
try:
    _VERIFIER_MOD = importlib.import_module("sandbox_tri_verifier")
except Exception as exc:  # pragma: no cover - exercised only when module is absent/broken
    _IMPORT_ERROR = exc


def _require_module():
    if _VERIFIER_MOD is None:
        pytest.fail(f"could not import examples/sandbox_tri_verifier.py: {_IMPORT_ERROR}")
    return _VERIFIER_MOD


def _require_attr(name: str):
    mod = _require_module()
    if not hasattr(mod, name):
        pytest.fail(f"sandbox_tri_verifier is missing required symbol: {name}")
    return getattr(mod, name)


def _good_reasoning() -> str:
    return '{vr: "hu:btn-open", ke: "AA strong", pp: "IP value", sr: "2.0x open"}'


def _action(action: str, *, amount: int | None = None, reasoning: str | None = None) -> dict[str, Any]:
    payload = {
        "action": action,
        "message": action,
        "reasoning": reasoning or _good_reasoning(),
        "reasoning_text": reasoning or _good_reasoning(),
    }
    if amount is not None:
        payload["amount"] = amount
    return payload


def _table():
    return hu_sb_unopened(["As", "Ah"])


def _allowed_actions(table: dict[str, Any]) -> list[str]:
    return list(table["allowedActions"]["availableActions"])


def _call(fn, **values):
    """Call verifier helpers without hardcoding one exact signature."""
    signature = inspect.signature(fn)
    aliases = {
        "table": {"table", "state", "game_state", "hand_state"},
        "action": {"action", "candidate", "payload", "decision"},
        "allowed_actions": {"allowed_actions", "available_actions"},
        "action_payload": {"action_payload", "payload"},
        "reasoning": {"reasoning", "reasoning_text"},
        "elapsed_s": {"elapsed_s", "elapsed", "latency_s", "duration_s", "decision_s", "runtime_s"},
        "budget_s": {"budget_s", "budget", "time_budget_s", "timeout_s", "max_seconds"},
        "deadline_s": {"deadline_s"},
        "rows": {"rows", "trajectory", "actions", "samples", "decisions"},
        "events": {"events"},
    }
    bound: dict[str, Any] = {}
    for param_name in signature.parameters:
        if param_name in values:
            bound[param_name] = values[param_name]
            continue
        for canonical, names in aliases.items():
            if param_name in names and canonical in values:
                bound[param_name] = values[canonical]
                break
    return fn(**bound)


def _boolish(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    if isinstance(value, (int, float)):
        return value > 0
    if isinstance(value, tuple):
        for item in value:
            if isinstance(item, bool):
                return item
        for item in value:
            if isinstance(item, dict):
                return _boolish(item)
    if isinstance(value, dict):
        for key in (
            "pass",
            "passed",
            "ok",
            "valid",
            "is_valid",
            "is_legal",
            "legal",
            "within_budget",
            "hand_specific",
            "critical_point",
        ):
            if key in value:
                return _boolish(value[key])
        for key in ("score", "total_score", "passed_count"):
            if key in value:
                return _boolish(value[key])
    raise AssertionError(f"could not coerce verifier result to bool: {value!r}")


def _scoreish(value: Any) -> float:
    if isinstance(value, bool):
        return 1.0 if value else 0.0
    if isinstance(value, (int, float)):
        return float(value)
    if isinstance(value, tuple):
        nums = [item for item in value if isinstance(item, (int, float, bool))]
        if nums:
            return float(sum(float(item) for item in nums))
        for item in value:
            if isinstance(item, dict):
                return _scoreish(item)
    if isinstance(value, dict):
        for key in ("score", "total_score", "aggregate_score", "passed_count", "pass_count"):
            if key in value:
                return float(value[key])
        if "summary" in value and isinstance(value["summary"], dict):
            summary = value["summary"]
            if "passed_actions" in summary:
                return float(summary["passed_actions"])
        if "dimensions" in value and isinstance(value["dimensions"], dict):
            dims = value["dimensions"]
            if {"correctness", "efficiency", "critical_point"} & set(dims):
                return float(sum(1.0 for item in dims.values() if isinstance(item, dict) and item.get("pass")))
        if "pass" in value:
            return 1.0 if value["pass"] else 0.0
        if "verifiers" in value and isinstance(value["verifiers"], (list, tuple)):
            return float(sum(_scoreish(item) for item in value["verifiers"]))
    raise AssertionError(f"could not coerce verifier result to score: {value!r}")


def _text_blob(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return value.lower()
    if isinstance(value, tuple):
        return " ".join(_text_blob(item) for item in value).strip()
    if isinstance(value, dict):
        return " ".join(_text_blob(item) for item in value.values()).strip()
    return str(value).lower()


def _make_row(table: dict[str, Any], action: dict[str, Any], *, elapsed_s: float) -> dict[str, Any]:
    return {
        "action": action["action"],
        "allowed_actions": _allowed_actions(table),
        "deadline_s": 1.0,
        "payload": action,
        "table": table,
        "elapsed_s": elapsed_s,
    }


def test_correctness_legal_vs_illegal_action():
    verify_correctness = _require_attr("verify_correctness")
    table = _table()
    legal = _action("raise", amount=4)
    illegal = _action("dance")

    legal_result = _call(
        verify_correctness,
        action=legal["action"],
        allowed_actions=_allowed_actions(table),
    )
    illegal_result = _call(
        verify_correctness,
        action=illegal["action"],
        allowed_actions=_allowed_actions(table),
    )

    assert _boolish(legal_result) is True
    assert _boolish(illegal_result) is False


def test_efficiency_within_deadline_vs_timeout():
    verify_efficiency = _require_attr("verify_efficiency")

    within_budget = _call(verify_efficiency, elapsed_s=0.20, deadline_s=1.00)
    timed_out = _call(verify_efficiency, elapsed_s=1.25, deadline_s=1.00)

    assert _boolish(within_budget) is True
    assert _boolish(timed_out) is False
    assert any(token in _text_blob(timed_out) for token in ("timeout", "deadline", "budget"))


def test_critical_point_hand_specific_vs_generic_fallback():
    verify_critical_point = _require_attr("verify_critical_point")
    is_generic_reasoning = _require_attr("is_generic_reasoning")
    table = _table()
    specific = _action("raise", amount=4, reasoning=_good_reasoning())
    generic = _action("raise", amount=4, reasoning=FALLBACK_REASONING)

    specific_result = _call(verify_critical_point, action_payload=specific, table=table)
    generic_result = _call(verify_critical_point, action_payload=generic, table=table)

    assert _boolish(specific_result) is True
    assert _boolish(generic_result) is False
    assert is_generic_reasoning(FALLBACK_REASONING) is True
    assert is_generic_reasoning(_good_reasoning()) is False


def test_k131_hazards_bad_amount_generic_reasoning_and_timeout_budget():
    verify_critical_point = _require_attr("verify_critical_point")
    score_action = _require_attr("score_action")
    table = _table()

    bad_amount = _action("raise", amount=2)
    generic = _action("raise", amount=4, reasoning=FALLBACK_REASONING)

    bad_amount_result = _call(
        score_action,
        action=bad_amount["action"],
        allowed_actions=_allowed_actions(table),
        elapsed_s=0.20,
        deadline_s=1.00,
        action_payload=bad_amount,
        table=table,
    )
    timeout_result = _call(
        score_action,
        action=bad_amount["action"],
        allowed_actions=_allowed_actions(table),
        elapsed_s=1.40,
        deadline_s=1.00,
        action_payload=bad_amount,
        table=table,
    )
    generic_result = _call(verify_critical_point, action_payload=generic, table=table)

    assert _boolish(bad_amount_result) is False
    assert "amount" in _text_blob(bad_amount_result)
    assert _boolish(generic_result) is False
    assert "generic" in _text_blob(generic_result) or "fallback" in _text_blob(generic_result)
    assert _boolish(timeout_result) is False
    assert any(token in _text_blob(timeout_result) for token in ("timeout", "deadline", "budget"))


def test_score_action_combines_tri_verifiers():
    score_action = _require_attr("score_action")
    table = _table()
    good = _action("raise", amount=4, reasoning=_good_reasoning())
    bad = _action("raise", amount=2, reasoning=FALLBACK_REASONING)

    good_result = _call(
        score_action,
        action=good["action"],
        allowed_actions=_allowed_actions(table),
        elapsed_s=0.20,
        deadline_s=1.00,
        action_payload=good,
        table=table,
    )
    bad_result = _call(
        score_action,
        action=bad["action"],
        allowed_actions=_allowed_actions(table),
        elapsed_s=1.40,
        deadline_s=1.00,
        action_payload=bad,
        table=table,
    )

    assert _scoreish(good_result) > _scoreish(bad_result)


def test_score_trajectory_aggregates_pass_fail():
    score_trajectory = _require_attr("score_trajectory")
    table = _table()
    good_row = _make_row(table, _action("raise", amount=4), elapsed_s=0.20)
    bad_row = _make_row(table, _action("raise", amount=2, reasoning=FALLBACK_REASONING), elapsed_s=1.40)

    mixed = _call(score_trajectory, events=[good_row, bad_row])
    all_good = _call(score_trajectory, events=[good_row, good_row])

    assert _scoreish(all_good) > _scoreish(mixed)
    assert mixed["summary"]["total_actions"] == 2
    assert mixed["summary"]["passed_actions"] == 1
    assert mixed["summary"]["failed_actions"] == 1
    assert all_good["summary"]["passed_actions"] == 2
    assert all_good["summary"]["failed_actions"] == 0
