"""HU ladder S1 guards — postflop stack-off + wide preflop (premium audit Jul 2026).

Extended 2026-07-14: trip-board boat detect + underpair/air + IP 4-straight + ace-high.
"""
from __future__ import annotations

import sys
from pathlib import Path

_EXAMPLES = Path(__file__).resolve().parents[1] / "examples"
_TESTS = Path(__file__).resolve().parent
if str(_EXAMPLES) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES))
if str(_TESTS) not in sys.path:
    sys.path.insert(0, str(_TESTS))

from cemini_decide import (  # noqa: E402
    _board_four_in_straight_window,
    _board_four_to_flush,
    _board_has_trips,
    _hero_boat_or_quads_on_paired_board,
    _hero_set_vulnerable_on_four_straight,
    _hero_vulnerable_on_trip_board,
    _hu_ladder_bb_defend,
    _hu_wide_open_hand,
    _preflop_stackoff_should_fold,
    decide,
)
from helpers.cemini_tables import (  # noqa: E402
    bb_99_vs_large_6max_shove,
    hu_btn_88_underpair_trip_nines_river,
    hu_btn_aqo_ace_high_paired_river,
    hu_btn_k7_boat_on_trip_nines_river,
    hu_btn_qto_air_four_straight_river,
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


def test_board_trips_and_boat_kicker_on_trip_board():
    board = ["9c", "9s", "9h", "5d", "Kh"]
    assert _board_has_trips(board) is True
    assert _hero_boat_or_quads_on_paired_board(["Kc", "7c"], board) is True
    assert _hero_boat_or_quads_on_paired_board(["8c", "8s"], board) is False
    assert _hero_vulnerable_on_trip_board(["8c", "8s"], board, "88") is True
    assert _hero_vulnerable_on_trip_board(["Kc", "7c"], board, "K7s") is False


def test_decide_keeps_k7_boat_on_trip_nines():
    out = decide(hu_btn_k7_boat_on_trip_nines_river(), deadline_s=10.0)
    assert out["action"] != "fold", out


def test_decide_folds_88_underpair_on_trip_nines():
    out = decide(hu_btn_88_underpair_trip_nines_river(), deadline_s=10.0)
    assert out["action"] == "fold", out


def test_decide_folds_qto_air_on_four_straight():
    out = decide(hu_btn_qto_air_four_straight_river(), deadline_s=10.0)
    assert out["action"] == "fold", out


def test_decide_folds_aqo_ace_high_paired_river():
    out = decide(hu_btn_aqo_ace_high_paired_river(), deadline_s=10.0)
    assert out["action"] == "fold", out


def test_six_max_99_folds_large_preflop_commit():
    # 200/1000 = 0.20 ≥ 0.18 6-max mid-pair bar
    assert _preflop_stackoff_should_fold("99", 200, 1000, position="BB") is True
    # HU keeps looser 0.25 bar
    hu = {"maxPlayers": 2, "seats": [{"status": "Active"}, {"status": "Active"}]}
    assert _preflop_stackoff_should_fold(
        "99", 200, 1000, position="BB", table=hu,
    ) is False
    out = decide(bb_99_vs_large_6max_shove(), deadline_s=10.0)
    assert out["action"] == "fold", out
