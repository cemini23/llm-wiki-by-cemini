"""P1-1 named-nemesis vs archetype split.

Named handles alone must NOT force tight margins by default
(CEMINI_NAMED_NEMESIS_TIGHT=0). Archetype evidence (premium_nit /
linear_aggro / …) stays tight on its own.
"""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

_EXAMPLES = Path(__file__).resolve().parent.parent / "examples"
if str(_EXAMPLES) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES))

from cemini_decide import (  # noqa: E402
    _named_nemesis_tight_enabled,
    _nemesis_tight_enabled,
    _preflop_vs_bet,
)
from nemesis_seed import (  # noqa: E402
    table_archetype_nemesis,
    table_nemesis_opener,
)


def _allowed() -> dict:
    return {
        "canCall": True,
        "canRaise": True,
        "raiseRange": {"min": 120, "max": 400},
        "availableActions": ["fold", "call", "raise"],
    }


def _named_nemesis_table() -> dict:
    """Hero MP; a seeded named nemesis (no stats) opened from UTG."""
    return {
        "selfSeatNumber": 0,
        "bigBlindChips": 20,
        "seats": [
            {"seatNumber": 0, "currentBetChips": 0},
            {"seatNumber": 1, "agentHandle": "hunterguy102", "currentBetChips": 60},
        ],
    }


def _premium_nit_table() -> dict:
    return {
        "selfSeatNumber": 0,
        "bigBlindChips": 20,
        "seats": [
            {"seatNumber": 0, "currentBetChips": 0},
            {
                "seatNumber": 1,
                "agentHandle": "nitty_mike",
                "currentBetChips": 60,
                "stats": {"vpip": 0.10, "pfr": 0.04, "sampleSize": 50},
            },
        ],
    }


def test_named_nemesis_tight_default_off(monkeypatch):
    monkeypatch.delenv("CEMINI_NAMED_NEMESIS_TIGHT", raising=False)
    assert _named_nemesis_tight_enabled() is False


def test_named_nemesis_tight_on_when_env_set(monkeypatch):
    monkeypatch.setenv("CEMINI_NAMED_NEMESIS_TIGHT", "1")
    assert _named_nemesis_tight_enabled() is True


def test_legacy_nemesis_tight_default_on():
    # Legacy CEMINI_NEMESIS_TIGHT still defaults on; P1-1 only decouples NAMED.
    assert _nemesis_tight_enabled() is True


def test_named_handle_alone_no_archetype_not_tight(monkeypatch):
    monkeypatch.delenv("CEMINI_NEMESIS_ARCHETYPE", raising=False)
    assert table_nemesis_opener(_named_nemesis_table()) is True
    assert table_archetype_nemesis(_named_nemesis_table()) is False


def test_archetype_evidence_still_tight(monkeypatch):
    monkeypatch.setenv("CEMINI_NEMESIS_ARCHETYPE", "1")
    monkeypatch.setenv("CEMINI_NEMESIS_PREMIUM_NIT", "1")
    assert table_archetype_nemesis(_premium_nit_table()) is True


def test_archetype_evidence_tight_off_when_toggles_off(monkeypatch):
    monkeypatch.setenv("CEMINI_NEMESIS_ARCHETYPE", "0")
    assert table_archetype_nemesis(_premium_nit_table()) is False


def test_named_tight_off_ep_suited_broadway_kept(monkeypatch):
    """nemesis_opener=False → KQs MP does NOT hit the nemesis EP fold."""
    monkeypatch.delenv("CEMINI_NAMED_NEMESIS_TIGHT", raising=False)
    monkeypatch.delenv("CEMINI_TOURNAMENT_3BET", raising=False)
    act, _amt = _preflop_vs_bet(
        {"hand_class": "KQs", "position": "MP", "suggested_action": "call"},
        _allowed(), ["fold", "call", "raise"],
        equity=0.55, pot_odds=0.3, call_chips=40, pot=100,
        in_position=True, nemesis_opener=False,
    )
    assert act == "call"


def test_named_tight_on_ep_suited_broadway_folds(monkeypatch):
    """nemesis_opener=True → KQs MP folds via the EP nemesis suited-broadway block."""
    monkeypatch.delenv("CEMINI_NAMED_NEMESIS_TIGHT", raising=False)
    monkeypatch.delenv("CEMINI_TOURNAMENT_3BET", raising=False)
    act, _amt = _preflop_vs_bet(
        {"hand_class": "KQs", "position": "MP", "suggested_action": "call"},
        _allowed(), ["fold", "call", "raise"],
        equity=0.55, pot_odds=0.3, call_chips=40, pot=100,
        in_position=True, nemesis_opener=True,
    )
    assert act == "fold"
