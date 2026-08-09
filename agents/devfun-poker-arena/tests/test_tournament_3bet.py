"""P1-2 tournament value 3bet tier + P2-1 thin IP polar bluff 3bet."""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

_EXAMPLES = Path(__file__).resolve().parent.parent / "examples"
if str(_EXAMPLES) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES))

from tournament_3bet import (  # noqa: E402
    preflop_opener_position,
    tournament_3bet_enabled,
    tournament_3bet_polar_enabled,
    try_tournament_polar_3bet,
    try_tournament_value_3bet,
)


@pytest.fixture(autouse=True)
def _clear_env(monkeypatch):
    monkeypatch.delenv("CEMINI_TOURNAMENT_3BET", raising=False)
    monkeypatch.delenv("CEMINI_TOURNAMENT_3BET_POLAR", raising=False)


def _allowed() -> dict:
    return {
        "canRaise": True,
        "raiseRange": {"min": 120, "max": 2000},
        "availableActions": ["fold", "call", "raise"],
    }


def test_tournament_3bet_off_by_default():
    assert tournament_3bet_enabled() is False
    assert tournament_3bet_polar_enabled() is False


def test_value_3bet_qq_ip(monkeypatch):
    monkeypatch.setenv("CEMINI_TOURNAMENT_3BET", "1")
    out = try_tournament_value_3bet(
        hand_class="QQ", position="BTN", in_position=True,
        call_chips=60, pot=90, allowed=_allowed(),
        available=["fold", "call", "raise"],
        hero_stack_chips=3000, big_blind=20,
    )
    assert out is not None and out[0] == "raise"
    assert out[1] is not None and out[1] <= 3000 * 0.35


def test_value_3bet_ak_bb(monkeypatch):
    monkeypatch.setenv("CEMINI_TOURNAMENT_3BET", "1")
    out = try_tournament_value_3bet(
        hand_class="AKs", position="BB", in_position=False,
        call_chips=60, pot=90, allowed=_allowed(),
        available=["fold", "call", "raise"],
        hero_stack_chips=3000, big_blind=20,
    )
    assert out is not None and out[0] == "raise"


def test_value_3bet_trash_folds(monkeypatch):
    monkeypatch.setenv("CEMINI_TOURNAMENT_3BET", "1")
    assert try_tournament_value_3bet(
        hand_class="72o", position="BTN", in_position=True,
        call_chips=60, pot=90, allowed=_allowed(),
        available=["fold", "call", "raise"],
        hero_stack_chips=3000, big_blind=20,
    ) is None


def test_value_3bet_blocked_5bb_open(monkeypatch):
    monkeypatch.setenv("CEMINI_TOURNAMENT_3BET", "1")
    assert try_tournament_value_3bet(
        hand_class="QQ", position="BTN", in_position=True,
        call_chips=100, pot=150, allowed=_allowed(),
        available=["fold", "call", "raise"],
        hero_stack_chips=3000, big_blind=20,
    ) is None


def test_value_3bet_blocked_short_stack(monkeypatch):
    monkeypatch.setenv("CEMINI_TOURNAMENT_3BET", "1")
    assert try_tournament_value_3bet(
        hand_class="QQ", position="BTN", in_position=True,
        call_chips=60, pot=90, allowed=_allowed(),
        available=["fold", "call", "raise"],
        hero_stack_chips=200, big_blind=20,
    ) is None


def test_value_3bet_blocked_oop_sb(monkeypatch):
    monkeypatch.setenv("CEMINI_TOURNAMENT_3BET", "1")
    assert try_tournament_value_3bet(
        hand_class="QQ", position="SB", in_position=False,
        call_chips=60, pot=90, allowed=_allowed(),
        available=["fold", "call", "raise"],
        hero_stack_chips=3000, big_blind=20,
    ) is None


def test_polar_off_by_default_even_when_value_on(monkeypatch):
    monkeypatch.setenv("CEMINI_TOURNAMENT_3BET", "1")
    assert try_tournament_polar_3bet(
        hand_class="A5s", position="BTN", in_position=True,
        call_chips=60, pot=90, allowed=_allowed(),
        available=["fold", "call", "raise"],
        hero_stack_chips=3000, big_blind=20, opener_position="CO",
    ) is None


def test_polar_3bet_a5s_btn_vs_co(monkeypatch):
    monkeypatch.setenv("CEMINI_TOURNAMENT_3BET_POLAR", "1")
    out = try_tournament_polar_3bet(
        hand_class="A5s", position="BTN", in_position=True,
        call_chips=60, pot=90, allowed=_allowed(),
        available=["fold", "call", "raise"],
        hero_stack_chips=3000, big_blind=20, opener_position="CO",
    )
    assert out is not None and out[0] == "raise"


def test_polar_3bet_k9s_co_vs_btn(monkeypatch):
    monkeypatch.setenv("CEMINI_TOURNAMENT_3BET_POLAR", "1")
    out = try_tournament_polar_3bet(
        hand_class="K9s", position="CO", in_position=True,
        call_chips=60, pot=90, allowed=_allowed(),
        available=["fold", "call", "raise"],
        hero_stack_chips=3000, big_blind=20, opener_position="BTN",
    )
    assert out is not None and out[0] == "raise"


def test_polar_3bet_not_vs_utg_open(monkeypatch):
    monkeypatch.setenv("CEMINI_TOURNAMENT_3BET_POLAR", "1")
    assert try_tournament_polar_3bet(
        hand_class="A5s", position="BTN", in_position=True,
        call_chips=60, pot=90, allowed=_allowed(),
        available=["fold", "call", "raise"],
        hero_stack_chips=3000, big_blind=20, opener_position="UTG",
    ) is None


def test_polar_3bet_not_value_hand(monkeypatch):
    monkeypatch.setenv("CEMINI_TOURNAMENT_3BET_POLAR", "1")
    assert try_tournament_polar_3bet(
        hand_class="AKs", position="BTN", in_position=True,
        call_chips=60, pot=90, allowed=_allowed(),
        available=["fold", "call", "raise"],
        hero_stack_chips=3000, big_blind=20, opener_position="CO",
    ) is None


def test_preflop_opener_position_helper():
    table = {
        "selfSeatNumber": 2,
        "seats": [
            {"seatNumber": 0, "currentBetChips": 60, "position": "UTG"},
            {"seatNumber": 1, "currentBetChips": 0, "position": "MP"},
            {"seatNumber": 2, "currentBetChips": 0, "position": "BTN"},
        ],
    }
    assert preflop_opener_position(table) == "UTG"
