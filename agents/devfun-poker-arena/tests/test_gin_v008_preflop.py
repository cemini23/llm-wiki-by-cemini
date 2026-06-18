"""gin/poker-bot v008 preflop loose-call + blind-defense port."""
from __future__ import annotations

import os
import sys
from pathlib import Path

_EXAMPLES = Path(__file__).resolve().parents[1] / "examples"
if str(_EXAMPLES) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES))

from gin_style import (  # noqa: E402
    try_preflop_blind_defense,
    try_preflop_loose_call,
    try_preflop_v008_rescue,
)


def _seat(num: int, cards: list[str], stack: int = 1800, folded: bool = False) -> dict:
    seat = {
        "seatNumber": num,
        "holeCards": cards,
        "stackChips": stack,
        "currentBetChips": 0,
    }
    if folded:
        seat["folded"] = True
    return seat


def _table(
    hero_seat: dict,
    *,
    pot: int,
    call_amount: int,
    position_label: str = "BTN",
    live_opponents: int = 1,
) -> dict:
    seats = [
        _seat(1, [], folded=True),
        _seat(2, [], folded=True),
        _seat(3, [], folded=True),
        _seat(4, [], folded=True),
        hero_seat,
        _seat(6, [], folded=True),
    ]
    button = 1
    if position_label == "BB":
        hero_seat["seatNumber"] = 3
        seats[2] = hero_seat
        seats[4] = _seat(5, [], folded=True)
    elif position_label == "SB":
        hero_seat["seatNumber"] = 2
        seats[1] = hero_seat
        seats[4] = _seat(5, [], folded=True)
    # Unfold villain seats for multiway (default: one live villain = seat 4)
    for num in range(1, 7):
        if num == hero_seat["seatNumber"]:
            continue
        if live_opponents <= 0:
            break
        for s in seats:
            if s["seatNumber"] == num:
                s.pop("folded", None)
                live_opponents -= 1
                break

    return {
        "street": "Preflop",
        "potChips": pot,
        "currentBet": call_amount,
        "buttonSeatNumber": button,
        "selfSeatNumber": hero_seat["seatNumber"],
        "seats": seats,
        "allowedActions": {
            "availableActions": ["fold", "call"],
            "callChips": call_amount,
            "callAmount": call_amount,
            "minBet": 20,
            "maxCommit": hero_seat["stackChips"],
        },
    }


def test_loose_call_btn_j9o_at_reasonable_price():
    hero = _seat(5, ["Jh", "9d"])
    table = _table(hero, pot=140, call_amount=40, position_label="BTN")
    out = try_preflop_loose_call(
        table, table["allowedActions"], ["fold", "call"], ["Jh", "9d"], "BTN",
    )
    assert out == ("call", 40)


def test_loose_call_rejects_expensive_price():
    hero = _seat(5, ["Jh", "9d"])
    table = _table(hero, pot=60, call_amount=80, position_label="BTN")
    out = try_preflop_loose_call(
        table, table["allowedActions"], ["fold", "call"], ["Jh", "9d"], "BTN",
    )
    assert out is None


def test_blind_defense_bb_aqo_steal():
    hero = _seat(3, ["Ah", "Qd"])
    table = _table(hero, pot=50, call_amount=20, position_label="BB")
    out = try_preflop_blind_defense(
        table, table["allowedActions"], ["fold", "call"], ["Ah", "Qd"], "BB",
    )
    assert out == ("call", 20)


def test_v008_rescue_disabled_when_env_off():
    os.environ["CEMINI_GIN_V008"] = "0"
    os.environ["CEMINI_GIN_STYLE_PREFLOP"] = "0"
    hero = _seat(5, ["Jh", "9d"])
    table = _table(hero, pot=140, call_amount=40, position_label="BTN")
    out = try_preflop_v008_rescue(
        table, table["allowedActions"], ["fold", "call"],
        ["Jh", "9d"], "BTN", "fold",
    )
    assert out is None
    os.environ.pop("CEMINI_GIN_V008", None)


def test_cemini_vs_bet_applies_v008_on_weak_preflop_fold():
    os.environ["CEMINI_GIN_V008"] = "1"
    from cemini_decide import _preflop_vs_bet  # noqa: E402

    chart = {
        "suggested_action": "fold",
        "hand_class": "J9o",
        "position": "BTN",
    }
    allowed = {
        "availableActions": ["fold", "call"],
        "callChips": 40,
        "canRaise": False,
    }
    table = _table(_seat(5, ["Jh", "9d"]), pot=140, call_amount=40, position_label="BTN")
    action, amount = _preflop_vs_bet(
        chart, allowed, ["fold", "call"],
        equity=0.32,
        pot_odds=40 / 180,
        call_chips=40,
        pot=140,
        in_position=True,
        margins={},
        table=table,
        lane_tight=False,
    )
    assert action == "call"
    os.environ.pop("CEMINI_GIN_V008", None)
