"""K276 withhold-contract tests (Cybersec lane, arXiv 2608.12292 pattern)."""
from __future__ import annotations

import os
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "examples"))
sys.path.insert(0, str(ROOT / "tests"))

from output_sanitize import maybe_sanitize_action  # noqa: E402
from withhold_contract import (  # noqa: E402
    check_outbound_action,
    detect_leak,
    withhold_contract_enabled,
)


def test_ahkd_in_message_revised():
    r = detect_leak("fold AhKd", ["Ah", "Kd"])
    assert r["leaked"] is True
    assert r["matches"]
    assert "Ah" not in r["revised"]
    assert "Kd" not in r["revised"]
    assert "[HOLE]" in r["revised"]


def test_board_only_not_leak():
    r = detect_leak("Ks on flop, I bet small", ["Ah", "Qd"])
    assert r["leaked"] is False
    assert r["matches"] == []
    assert r["revised"] == "Ks on flop, I bet small"


def test_word_and_symbol_forms_detected():
    r = detect_leak("Ace of hearts is mine; also A♥", ["Ah"])
    assert r["leaked"] is True
    assert "hearts" not in r["revised"]
    assert "♥" not in r["revised"]
    assert "[HOLE]" in r["revised"]


def test_lowercase_concatenated_hole_cards_revised():
    r = detect_leak("fold ahkd", ["ah", "kd"])
    assert r["leaked"] is True
    assert r["revised"] == "fold [HOLE]"
    assert r["matches"] == ["ahkd"]


def test_lowercase_card_does_not_match_inside_english_word():
    r = detect_leak("perhaps fold", ["ah"])
    assert r["leaked"] is False
    assert r["revised"] == "perhaps fold"


def test_hand_class_literal_revised():
    r = detect_leak("playing AKo from the button", [], extra_secrets=["AKo"])
    assert r["leaked"] is True
    assert "AKo" not in r["revised"]
    assert "[HAND]" in r["revised"]


def test_empty_text_and_cards_not_leak():
    assert detect_leak("", ["Ah"])["leaked"] is False
    assert detect_leak(None, ["Ah"])["leaked"] is False
    assert detect_leak("fold Ah", [])["leaked"] is False


def test_check_outbound_action_revises_over_block():
    action = {
        "action": "raise",
        "message": "raise with AhKd for value",
        "reasoning": "top pair A♥, strong",
    }
    out = check_outbound_action(
        action, hole_cards=["Ah", "Kd"], hand_class="AKo"
    )
    # Revise over block: a dict comes back, never a raise.
    assert isinstance(out, dict)
    assert out["action"] == "raise"
    assert "Ah" not in str(out["message"]) + str(out["reasoning"])
    assert "[HOLE]" in out["message"]


def test_untrusted_hole_source_rejected():
    # Observation / tool_result must never supply the secret set — the API
    # refuses the untrusted channel instead of trusting the fake hole list.
    with pytest.raises(ValueError):
        check_outbound_action(
            {"action": "fold", "message": "x"},
            hole_cards=["Ah", "Kd"],
            hole_source="observation",
        )
    with pytest.raises(ValueError):
        check_outbound_action(
            {"action": "fold", "message": "x"},
            hole_cards=["Ah", "Kd"],
            hole_source="tool_result",
        )


def test_env_gate_off_passthrough(monkeypatch):
    monkeypatch.setenv("CEMINI_WITHHOLD_CONTRACT", "0")
    assert withhold_contract_enabled() is False
    action = {"action": "call", "message": "call with Ah"}
    out = check_outbound_action(action, hole_cards=["Ah"])
    assert out is action  # no-op passthrough
    # detect still works with the gate off
    assert detect_leak("call with Ah", ["Ah"])["leaked"] is True


def test_sanitize_off_withhold_on_still_redacts(monkeypatch):
    monkeypatch.setenv("CEMINI_SANITIZE_OUTPUT", "0")
    monkeypatch.delenv("CEMINI_WITHHOLD_CONTRACT", raising=False)
    assert withhold_contract_enabled() is True
    out = maybe_sanitize_action(
        {"action": "call", "message": "call with AhQd", "reasoning": "r"},
        hole_cards=["Ah", "Qd"],
    )
    assert "Ah" not in str(out.get("message", "")) + str(out.get("reasoning", ""))
    assert "[HOLE]" in out["message"]


def test_maybe_sanitize_withhold_wire_verify_line():
    """Handoff verify one-liner equivalent."""
    a = maybe_sanitize_action(
        {"action": "fold", "message": "fold AhKd", "reasoning": "x"},
        hole_cards=["Ah", "Kd"],
    )
    assert "Ah" not in str(a.get("message", "")) + str(a.get("reasoning", ""))


def test_no_hole_cards_keeps_existing_sanitize_behavior(monkeypatch):
    monkeypatch.setenv("CEMINI_SANITIZE_OUTPUT", "1")
    out = maybe_sanitize_action(
        {"action": "fold", "message": "open_defend@BTN", "reasoning": '{sk: "x"}'}
    )
    assert out["message"] == "fold"
    assert "sk:" not in out["reasoning"]
