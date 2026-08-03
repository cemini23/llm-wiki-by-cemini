"""Position labels must stay fixed for the hand (folded seats stay in geometry)."""
from __future__ import annotations

import sys
from pathlib import Path

_EXAMPLES = Path(__file__).resolve().parent.parent / "examples"
if str(_EXAMPLES) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES))

from position_utils import hero_position_label, infer_button_seat  # noqa: E402


def _six_max_table(*, hero_seat: int, button: int = 1) -> dict:
    seats = []
    for n in range(1, 7):
        seats.append({
            "seatNumber": n,
            "status": "Active",
            "stackChips": 1000,
            "currentBetChips": 0,
            "holeCards": ["Ad", "Qs"] if n == hero_seat else [],
        })
    # SB / BB posts relative to button
    order = list(range(1, 7))
    btn_i = order.index(button)
    sb = order[(btn_i + 1) % 6]
    bb = order[(btn_i + 2) % 6]
    for s in seats:
        if s["seatNumber"] == sb:
            s["currentBetChips"] = 1
            s["postedBlindChips"] = 1
        elif s["seatNumber"] == bb:
            s["currentBetChips"] = 2
            s["postedBlindChips"] = 2
    return {
        "selfSeatNumber": hero_seat,
        "buttonSeatNumber": button,
        "smallBlindChips": 1,
        "bigBlindChips": 2,
        "seats": seats,
    }


def test_hero_position_stable_when_early_seats_fold():
    # Seat 5 = MP with button on 1 (BTN=1,SB=2,BB=3,UTG=4,MP=5,CO=6)
    table = _six_max_table(hero_seat=5, button=1)
    assert hero_position_label(table) == "MP"

    # UTG folds — old code shrunk active set and relabeled hero
    for s in table["seats"]:
        if s["seatNumber"] == 4:
            s["status"] = "Folded"
    assert hero_position_label(table) == "MP"

    # CO also folds; hero still MP for the hand
    for s in table["seats"]:
        if s["seatNumber"] == 6:
            s["status"] = "Folded"
    assert hero_position_label(table) == "MP"


def test_sb_label_stable_after_raise_past_blinds():
    # Hero SB (seat 2), button 1
    table = _six_max_table(hero_seat=2, button=1)
    assert hero_position_label(table) == "SB"

    # BTN opens to 6; early seats fold — SB must not flip to another label
    for s in table["seats"]:
        if s["seatNumber"] == 1:
            s["currentBetChips"] = 6
        if s["seatNumber"] in (4, 5, 6):
            s["status"] = "Folded"
    assert hero_position_label(table) == "SB"


def test_infer_button_prefers_explicit_field():
    # button=3 → BTN=3,SB=4,BB=5,UTG=6,MP=1,CO=2
    table = _six_max_table(hero_seat=6, button=3)
    assert infer_button_seat(table) == 3
    assert hero_position_label(table) == "UTG"
