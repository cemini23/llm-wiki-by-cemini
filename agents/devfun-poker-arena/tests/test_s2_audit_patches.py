"""Integration tests for S2 audit consensus patches."""
from __future__ import annotations

import importlib
import os
import sys
from pathlib import Path

import pytest

_EXAMPLES = Path(__file__).resolve().parent.parent / "examples"
if str(_EXAMPLES) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES))

from s1b_exploit import (  # noqa: E402
    try_iso_vs_wide_passive_limp,
    try_jeff_nemesis_4bet,
)
from nemesis_seed import nemesis_handles, table_nemesis_pressure  # noqa: E402


def _load_decide():
    import cemini_decide as mod  # noqa: WPS433

    return importlib.reload(mod).decide


def test_jagoan_neon_in_default_nemesis(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.delenv("CEMINI_NEMESIS_HANDLES", raising=False)
    assert "jagoan_neon" in nemesis_handles()


def test_jeff_4bet_jj(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setenv("CEMINI_NEMESIS_EXPLOIT", "1")
    out = try_jeff_nemesis_4bet(
        hand_class="JJ",
        call_chips=120,
        big_blind=20,
        allowed={"canAllIn": True, "canRaise": True},
        available=["fold", "call", "raise", "all-in"],
        hero_stack_chips=1000,
        villain_handle="0xJeff_ai",
    )
    assert out and out[0] == "all-in"


def test_iso_wide_passive_co(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setenv("CEMINI_ISO_PASSIVE_LP", "1")
    monkeypatch.setenv("CEMINI_NEMESIS_ARCHETYPE", "1")
    out = try_iso_vs_wide_passive_limp(
        hand_class="AKs",
        position="CO",
        call_chips=20,
        pot=50,
        allowed={"canBet": True, "betRange": {"min": 40, "max": 400}},
        available=["fold", "call", "bet"],
        hero_stack_chips=1000,
        big_blind=20,
        hud={"archetype": "wide_passive", "vpip": 0.42, "raise_gap": 0.35},
    )
    assert out and out[0] == "bet"


def test_premium_nit_fold_via_decide(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setenv("CEMINI_NEMESIS_ARCHETYPE", "1")
    monkeypatch.setenv("CEMINI_NEMESIS_PREMIUM_NIT", "1")
    decide = _load_decide()
    table = {
        "street": "Preflop",
        "board": [],
        "pot": 90,
        "selfSeatNumber": 3,
        "bigBlindChips": 20,
        "smallBlindChips": 10,
        "allowedActions": {
            "canFold": True,
            "canCall": True,
            "callChips": 60,
            "callTo": 60,
        },
        "seats": [
            {"seatNumber": 1, "stackChips": 1000, "holeCards": [], "currentBetChips": 0},
            {
                "seatNumber": 2,
                "agentHandle": "alnitak",
                "stackChips": 1000,
                "currentBetChips": 60,
                "stats": {"vpip": 0.07, "pfr": 0.03, "sampleSize": 500},
            },
            {
                "seatNumber": 3,
                "stackChips": 1000,
                "holeCards": ["Qd", "Ts"],
                "currentBetChips": 0,
            },
        ],
    }
    action = decide(
        table,
        research_context={
            "preflop_chart": {
                "suggested_action": "call",
                "hand_class": "QTo",
                "position": "CO",
            },
            "opponent_hud": {
                "archetype": "premium_nit",
                "premium_concentration": 0.6,
                "villain_handle": "alnitak",
                "stats": {"vpip": 0.07, "pfr": 0.03},
            },
        },
    )
    assert action.get("action") == "fold"


def test_seat_matrix_utg_trash_fold(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setenv("CEMINI_SEAT_MATRIX_V2", "1")
    decide = _load_decide()
    table = {
        "street": "Preflop",
        "board": [],
        "pot": 30,
        "selfSeatNumber": 4,
        "bigBlindChips": 20,
        "allowedActions": {"canFold": True, "canCheck": True},
        "seats": [
            {"seatNumber": 4, "stackChips": 1000, "holeCards": ["9h", "5h"], "currentBetChips": 0},
        ],
    }
    action = decide(
        table,
        research_context={
            "preflop_chart": {
                "suggested_action": "raise",
                "hand_class": "95o",
                "position": "UTG",
            },
        },
    )
    assert action.get("action") == "fold"


def test_table_nemesis_pressure_archetype(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setenv("CEMINI_NEMESIS_ARCHETYPE", "1")
    monkeypatch.setenv("CEMINI_NEMESIS_PREMIUM_NIT", "1")
    table = {
        "street": "Preflop",
        "bigBlindChips": 20,
        "selfSeatNumber": 1,
        "seats": [
            {"seatNumber": 1, "currentBetChips": 0},
            {
                "seatNumber": 2,
                "agentHandle": "einstein",
                "currentBetChips": 50,
                "stats": {"vpip": 0.11, "pfr": 0.04, "sampleSize": 300},
            },
        ],
    }
    assert table_nemesis_pressure(table)
