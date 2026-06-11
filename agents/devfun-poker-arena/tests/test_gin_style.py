"""Unit tests for gin_style scoring lanes."""
from __future__ import annotations

import os

import pytest

from gin_style import (
    gin_style_preflop_enabled,
    preflop_score,
    try_preflop,
)


def test_preflop_score_premium():
    assert preflop_score(["As", "Ah"]) > 88


def test_gin_preflop_open_bet_on_btn(monkeypatch):
    monkeypatch.setenv("CEMINI_GIN_STYLE_PREFLOP", "1")
    assert gin_style_preflop_enabled()
    table = {
        "potChips": 30,
        "seats": [
            {"seatNumber": 1, "holeCards": ["Kd", "Qd"], "stackChips": 500},
            {"seatNumber": 2, "holeCards": None, "stackChips": 500},
        ],
        "selfSeatNumber": 1,
        "actingSeatNumber": 1,
        "allowedActions": {
            "availableActions": ["fold", "bet", "check"],
            "canBet": True,
            "canCheck": True,
            "callChips": 0,
            "betRange": {"min": 40, "max": 500},
            "maxCommit": 500,
        },
    }
    act, amt = try_preflop(
        table,
        table["allowedActions"],
        table["allowedActions"]["availableActions"],
        ["Kd", "Qd"],
        "BTN",
        in_position=True,
    )
    assert act == "bet"
    assert amt is not None and amt >= 40
