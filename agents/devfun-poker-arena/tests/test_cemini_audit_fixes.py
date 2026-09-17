"""Regression tests from multi-model cursor audit (2026-06-04)."""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "examples"))
sys.path.insert(0, str(ROOT))

from cemini_decide import _apply_chip_reserve, _hero_made_hand_exempt, decide  # noqa: E402
from tests.helpers.cemini_tables import (  # noqa: E402
    co_72o_boat_paired_river,
    co_j2o_paired_river,
    mp_77_set_flop,
    nuts_quads_facing_bet,
    sb_jj_boat_paired_river,
    sb_qq_top_set_connected_river,
    six_max_table,
    _allowed,
)


@pytest.fixture(autouse=True)
def _nuts_off(monkeypatch: pytest.MonkeyPatch) -> None:
    """Guard fixes must work without river enumeration."""
    monkeypatch.setenv("CEMINI_NUTS_DETECT", "0")


def test_sb_jj_boat_not_folded_by_underpair_guard():
    table = sb_jj_boat_paired_river()
    out = decide(table, deadline_s=10.0)
    assert out["action"] != "fold", out.get("message")


def test_co_72o_boat_not_folded_on_paired_board():
    table = co_72o_boat_paired_river()
    out = decide(table, deadline_s=10.0)
    assert out["action"] != "fold", out.get("message")


def test_j2o_bottom_trips_still_folds_on_paired_river():
    table = co_j2o_paired_river()
    out = decide(table, deadline_s=10.0)
    assert out["action"] == "fold", out.get("message")


def test_77_set_not_folded_on_paired_flop():
    table = mp_77_set_flop()
    out = decide(table, deadline_s=10.0)
    assert out["action"] != "fold", out.get("message")


def test_hero_made_hand_exempt_bottom_trips_false():
    hole = ["Jd", "2d"]
    board = ["Kc", "Ah", "Td", "2h", "2s"]
    assert _hero_made_hand_exempt(hole, board) is False
    assert _hero_made_hand_exempt(["As", "9c"], ["Ac", "Ad", "2c"]) is True


def test_sb_qq_top_set_not_folded_on_connected_board():
    table = sb_qq_top_set_connected_river()
    out = decide(table, deadline_s=10.0)
    assert out["action"] != "fold", out.get("message")


def test_nuts_call_under_clock_pressure(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setenv("CEMINI_NUTS_DETECT", "1")
    table = nuts_quads_facing_bet()
    out = decide(table, deadline_s=1.5)
    assert out["action"] in {"call", "raise", "all-in"}, out.get("message")


def test_chip_reserve_degrades_illegal_bet():
    table = six_max_table(
        name="cap_bet",
        hero_seat=1,
        button_seat=1,
        street="River",
        board=["Kh", "Qd", "7c", "2h", "3s"],
        pot=200,
        hero_hole=["Ac", "Ad"],
        hero_stack=500,
        allowed=_allowed(
            can_check=True,
            can_bet=True,
            bet_range={"min": 100, "max": 500},
        ),
    )
    raw = {"action": "bet", "amount": 400, "message": "value"}
    out = _apply_chip_reserve(raw, max_playable=30, table=table, hand_class="AA")
    assert out["action"] in {"check", "call", "fold"}
    assert out.get("amount") is None or out["amount"] >= 100


def test_chip_reserve_zero_playable_folds_allin():
    table = six_max_table(
        name="empty_reserve_jam",
        hero_seat=4,
        button_seat=1,
        street="Preflop",
        board=[],
        pot=30,
        hero_hole=["7h", "7s"],
        hero_stack=80,
        allowed=_allowed(
            can_fold=True,
            can_raise=True,
            raise_range={"min": 40, "max": 80},
        ),
    )
    raw = {"action": "all-in", "amount": 80, "message": "jam"}
    out = _apply_chip_reserve(raw, max_playable=0, table=table, hand_class="77")
    assert out["action"] in {"fold", "check"}
    none_amt = {"action": "all-in", "message": "short-stack jam"}
    out_none = _apply_chip_reserve(none_amt, max_playable=0, table=table, hand_class="77")
    assert out_none["action"] in {"fold", "check"}
    aa = _apply_chip_reserve(
        {"action": "all-in", "amount": 80, "message": "aa"},
        max_playable=0,
        table=table,
        hand_class="AA",
    )
    assert aa["action"] == "all-in"


def test_qualification_guard_malformed_env(monkeypatch: pytest.MonkeyPatch):
    from qualification_guard import _buffer_threshold, _first_max_playable_frac

    monkeypatch.setenv("CEMINI_QUAL_BUFFER_CHIPS", "not-a-number")
    monkeypatch.setenv("CEMINI_FIRST_MAX_PLAYABLE_FRAC", "bad")
    assert _buffer_threshold() == 1000
    assert _first_max_playable_frac() == 0.28
