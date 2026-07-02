"""Tests for Tool-RL structural collapse detector (K136 P0)."""
from __future__ import annotations

import importlib
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
EXAMPLES = ROOT / "examples"

if str(EXAMPLES) not in sys.path:
    sys.path.insert(0, str(EXAMPLES))

_IMPORT_ERROR: Exception | None = None
_DETECTOR_MOD = None
try:
    _DETECTOR_MOD = importlib.import_module("tool_rl_collapse_detector")
except Exception as exc:  # pragma: no cover
    _IMPORT_ERROR = exc


def _require_module():
    if _DETECTOR_MOD is None:
        pytest.fail(f"could not import examples/tool_rl_collapse_detector.py: {_IMPORT_ERROR}")
    return _DETECTOR_MOD


def _require_attr(name: str):
    mod = _require_module()
    if not hasattr(mod, name):
        pytest.fail(f"tool_rl_collapse_detector is missing required symbol: {name}")
    return getattr(mod, name)


def _good_reasoning() -> str:
    return '{vr: "hu:btn-open", ke: "AA strong", pp: "IP value", sr: "2.0x open"}'


def test_detect_collapse_ok_on_hand_specific_reasoning():
    detect_collapse = _require_attr("detect_collapse")
    result = detect_collapse(_good_reasoning())
    assert result["mode"] == "ok"
    assert result["hazards"] == []


def test_detect_collapse_polluted_on_control_tokens():
    detect_collapse = _require_attr("detect_collapse")
    text = f"{_good_reasoning()} <|tool|> join_pve"
    result = detect_collapse(text)
    assert result["mode"] == "polluted"
    assert any("control_token" in h for h in result["hazards"])
    assert any("join_pve" in h for h in result["hazards"])


def test_detect_collapse_polluted_on_fenced_json_tool_block():
    detect_collapse = _require_attr("detect_collapse")
    text = 'Thinking...\n```json\n{"tool": "submit_action", "arguments": {"action": "raise"}}\n```'
    result = detect_collapse(text)
    assert result["mode"] == "polluted"
    assert any("fenced_tool_block" in h for h in result["hazards"])


def test_detect_collapse_collapsed_on_whitespace_only():
    detect_collapse = _require_attr("detect_collapse")
    result = detect_collapse("   \n\t  ")
    assert result["mode"] == "collapsed"
    assert any("whitespace_only" in h for h in result["hazards"])


def test_detect_collapse_collapsed_on_broken_json_stub():
    detect_collapse = _require_attr("detect_collapse")
    result = detect_collapse('{"tool": "get_game_state", "arguments": {')
    assert result["mode"] == "collapsed"
    assert any("json" in h for h in result["hazards"])


def test_verify_action_payload_collapse_checks_all_fields():
    verify_action_payload_collapse = _require_attr("verify_action_payload_collapse")
    ok_payload = {
        "message": "raise",
        "reasoning": _good_reasoning(),
        "reasoning_text": _good_reasoning(),
    }
    ok_result = verify_action_payload_collapse(ok_payload)
    assert ok_result["mode"] == "ok"
    assert ok_result["hazards"] == []

    polluted_payload = {
        "message": "call",
        "reasoning": _good_reasoning(),
        "reasoning_text": "poll get_game_state then act",
    }
    polluted_result = verify_action_payload_collapse(polluted_payload)
    assert polluted_result["mode"] == "polluted"
    assert any("reasoning_text:polluted:mcp_tool_name:get_game_state" in h for h in polluted_result["hazards"])

    collapsed_payload = {
        "message": "   ",
        "reasoning": "",
        "reasoning_text": "",
    }
    collapsed_result = verify_action_payload_collapse(collapsed_payload)
    assert collapsed_result["mode"] == "collapsed"
    assert any("whitespace_only" in h for h in collapsed_result["hazards"])


def test_score_action_includes_tool_rl_collapse_dimension():
    import sandbox_tri_verifier as verifier  # noqa: WPS433

    from cemini_tables import hu_sb_unopened  # noqa: E402

    helpers = ROOT / "tests" / "helpers"
    if str(helpers) not in sys.path:
        sys.path.insert(0, str(helpers))

    table = hu_sb_unopened(["As", "Ah"])
    good_payload = {
        "action": "raise",
        "amount": 4,
        "message": "raise",
        "reasoning": _good_reasoning(),
        "reasoning_text": _good_reasoning(),
    }
    good_score = verifier.score_action(
        action="raise",
        allowed_actions=list(table["allowedActions"]["availableActions"]),
        elapsed_s=0.2,
        deadline_s=1.0,
        action_payload=good_payload,
        table=table,
    )
    collapse_dim = good_score["dimensions"]["tool_rl_collapse"]
    assert collapse_dim["pass"] is True
    assert collapse_dim["mode"] == "ok"

    bad_payload = dict(good_payload)
    bad_payload["reasoning_text"] = "<|tool|> submit_action"
    bad_score = verifier.score_action(
        action="raise",
        allowed_actions=list(table["allowedActions"]["availableActions"]),
        elapsed_s=0.2,
        deadline_s=1.0,
        action_payload=bad_payload,
        table=table,
    )
    bad_dim = bad_score["dimensions"]["tool_rl_collapse"]
    assert bad_dim["pass"] is False
    assert bad_dim["mode"] == "polluted"
    assert good_score["pass"] is True
    assert bad_score["pass"] is False
