"""Preflop guardrails — block trash open-steals (J2o CO leak)."""
from __future__ import annotations

import sys
from pathlib import Path

_EXAMPLES = Path(__file__).resolve().parents[1] / "examples"
if str(_EXAMPLES) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES))

from cemini_decide import (  # noqa: E402
    _blocks_open_steal,
    _preflop_open,
    _preflop_pot_committed_should_call,
    _preflop_vs_bet,
)


def test_blocks_j2o_co_steal():
    assert _blocks_open_steal("J2o", "CO") is True
    assert _blocks_open_steal("72o", "BTN") is True
    assert _blocks_open_steal("A5s", "CO") is False


def test_j2o_chart_fold_not_open_stolen_vs_rock():
    allowed = {"canBet": True, "betRange": {"min": 20, "max": 100}}
    available = ["fold", "check", "bet"]
    margins = {"open_steal_equity": 0.34}
    action, amount = _preflop_open(
        "fold", allowed, available, pot=40, equity=0.55,
        hand_class="J2o", position="CO", hud_mode="rock", margins=margins,
    )
    assert action in ("fold", "check")
    assert action != "bet"


def test_ep_no_steal_74o_mp():
    from cemini_decide import _preflop_open

    allowed = {"canBet": True, "betRange": {"min": 20, "max": 100}}
    available = ["fold", "check", "bet"]
    margins = {"open_steal_equity": 0.34}
    action, _ = _preflop_open(
        "fold", allowed, available, pot=40, equity=0.60,
        hand_class="74o", position="MP", hud_mode="rock", margins=margins,
    )
    assert action == "fold"


def test_overcommit_fold_weak_hand():
    from cemini_decide import _overcommit_should_fold

    table = {"selfSeatNumber": 1, "seats": [{"seatNumber": 1, "stackChips": 500}]}
    assert _overcommit_should_fold(table, "74o", 0.35, 200) is True
    assert _overcommit_should_fold(table, "AKs", 0.60, 200) is False


def test_preflop_pot_committed_call_guard():
    assert _preflop_pot_committed_should_call(50, 1900, ["fold", "call"]) is True
    assert _preflop_pot_committed_should_call(200, 300, ["fold", "call"]) is False


def test_preflop_vs_bet_calls_when_pot_committed_with_weak_ace():
    allowed = {
        "canFold": True,
        "canCall": True,
        "availableActions": ["fold", "call"],
        "callChips": 50,
    }
    table = {
        "selfSeatNumber": 1,
        "bigBlindChips": 20,
        "potChips": 1900,
        "allowedActions": allowed,
        "seats": [{"seatNumber": 1, "stackChips": 50}],
    }
    chart = {"hand_class": "A6o", "position": "SB", "suggested_action": "fold"}

    action, amount = _preflop_vs_bet(
        chart,
        allowed,
        ["fold", "call"],
        equity=0.25,
        pot_odds=50 / 1950,
        call_chips=50,
        pot=1900,
        in_position=False,
        table=table,
        hero_stack_chips=50,
        big_blind=20,
    )

    assert (action, amount) == ("call", None)
