"""HU ladder S1 guards — postflop stack-off + wide preflop (premium audit Jul 2026)."""
from __future__ import annotations

import sys
from pathlib import Path

_EXAMPLES = Path(__file__).resolve().parents[1] / "examples"
if str(_EXAMPLES) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES))

from cemini_decide import (  # noqa: E402
    _board_four_in_straight_window,
    _board_four_to_flush,
    _hero_set_vulnerable_on_four_straight,
    _hu_ladder_bb_defend,
    _hu_wide_open_hand,
)


def test_board_four_in_straight_window():
    board = ["9s", "Jd", "5d", "Ts", "8c"]
    assert _board_four_in_straight_window(board) is True
    assert _board_four_in_straight_window(["2c", "7s", "3c"]) is False


def test_jj_set_vulnerable_on_straight_runout():
    hole = ["Jc", "Js"]
    board = ["9s", "Jd", "5d", "Ts", "8c"]
    assert _hero_set_vulnerable_on_four_straight(hole, board) is True
    hole_aa = ["As", "Ad"]
    assert _hero_set_vulnerable_on_four_straight(hole_aa, board) is False
    hole_qq = ["Qs", "Qd"]
    board_qjt = ["Qh", "Jc", "Td", "8s", "2c"]
    assert _hero_set_vulnerable_on_four_straight(hole_qq, board_qjt) is False


def test_four_flush_board_detect():
    board = ["Qd", "Td", "7d", "6c", "9d"]
    assert _board_four_to_flush(board) is True


def test_hu_wide_open_covers_sb_steal_range():
    assert _hu_wide_open_hand("K8o") is True
    assert _hu_wide_open_hand("J7o") is True
    assert _hu_wide_open_hand("72o") is False


def test_hu_bb_defend_vs_minraise_price():
    assert _hu_ladder_bb_defend("K8o", 20, 60) is True
    assert _hu_ladder_bb_defend("72o", 20, 60) is False
    assert _hu_ladder_bb_defend("K8o", 200, 250) is False
