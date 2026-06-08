"""Jackpot lane — royal showdown + 7-2 bluff rules."""
from __future__ import annotations

import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "examples"))

import cemini_decide  # noqa: E402
from cemini_decide import decide  # noqa: E402
from jackpot_rules import (  # noqa: E402
    BLUFF_27_RULE,
    ROYAL_RULE,
    is_two_seven_offsuit_hand_class,
    royal_showdown_mode,
    summarize_jackpots,
)
from tests.helpers.cemini_tables import _allowed, six_max_table  # noqa: E402


def test_api_rule_strings_documented():
    assert "showdown" in ROYAL_RULE.lower()
    assert "7-2" in BLUFF_27_RULE or "2-7" in BLUFF_27_RULE


def test_two_seven_hand_class():
    assert is_two_seven_offsuit_hand_class("72o")
    assert not is_two_seven_offsuit_hand_class("27o")


def test_summarize_jackpots():
    body = {
        "jackpots": [
            {"handType": "RoyalFlush", "status": "Available", "amount": 100},
            {"handType": "RoyalFlush", "status": "Claimed", "amount": 100},
            {"handType": "TwoSevenOffsuitBluff", "status": "Available", "amount": 50},
        ]
    }
    s = summarize_jackpots(body)
    assert s["total_slots"] == 3
    assert s["by_type"]["RoyalFlush"]["available"] == 1
    assert s["by_type"]["RoyalFlush"]["claimed"] == 1
    assert s["by_type"]["TwoSevenOffsuitBluff"]["available"] == 1


def test_royal_prefers_check_for_showdown_jackpot():
    os.environ["JACKPOT_ROYAL_SHOWDOWN"] = "1"
    assert royal_showdown_mode()
    table = six_max_table(
        name="royal_showdown_check",
        hero_seat=1,
        button_seat=1,
        street="River",
        board=["Ah", "Kh", "Th", "5d", "2c"],
        pot=200,
        hero_hole=["Qh", "Jh"],
        hero_stack=900,
        allowed=_allowed(
            can_check=True,
            can_bet=True,
            bet_range={"min": 20, "max": 900},
        ),
    )
    out = decide(table, deadline_s=10.0)
    assert out["action"] == "check"
    assert "fold" not in out["action"]


def test_royal_calls_facing_bet():
    os.environ["JACKPOT_ROYAL_SHOWDOWN"] = "1"
    table = six_max_table(
        name="royal_showdown_call",
        hero_seat=1,
        button_seat=1,
        street="River",
        board=["Ah", "Kh", "Th", "5d", "2c"],
        pot=400,
        hero_hole=["Qh", "Jh"],
        hero_stack=700,
        allowed=_allowed(
            can_call=True,
            call_chips=100,
        ),
    )
    out = decide(table, deadline_s=10.0)
    assert out["action"] == "call"
