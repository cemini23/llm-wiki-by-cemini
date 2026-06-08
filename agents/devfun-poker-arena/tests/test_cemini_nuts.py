"""River unbeatable integration — CEMINI_NUTS_DETECT=1 only."""
from __future__ import annotations

import os
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "examples"))
sys.path.insert(0, str(ROOT))

from cemini_decide import decide  # noqa: E402
from hand_nuts import treys_available  # noqa: E402
from tests.fixtures.regression_spots import (  # noqa: E402
    nuts_regression_spots,
    regression_spots,
)

pytestmark = pytest.mark.skipif(not treys_available(), reason="treys not installed")


@pytest.fixture(autouse=True)
def _nuts_on(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("CEMINI_NUTS_DETECT", "1")


def _run(spot_table: dict) -> dict:
    out = decide(spot_table, deadline_s=10.0)
    legal = set(spot_table["allowedActions"]["availableActions"])
    assert out["action"] in legal
    return out


def test_nuts_regression_spots():
    for spot in nuts_regression_spots():
        action = _run(spot.table)["action"]
        if spot.forbidden:
            assert action not in spot.forbidden, (
                f"{spot.id}: got {action!r}, forbidden={sorted(spot.forbidden)}"
            )
        if spot.required:
            assert action in spot.required, (
                f"{spot.id}: expected one of {sorted(spot.required)}, got {action!r}"
            )


def test_nuts_flag_off_matches_baseline_regression(monkeypatch: pytest.MonkeyPatch):
    """CEMINI_NUTS_DETECT=0 must not change existing leak guards."""
    monkeypatch.setenv("CEMINI_NUTS_DETECT", "0")
    for spot in regression_spots():
        action = decide(spot.table, deadline_s=10.0)["action"]
        if spot.forbidden:
            assert action not in spot.forbidden, spot.id
        if spot.required:
            assert action in spot.required, spot.id


def test_royal_equivalent_to_nuts_when_enabled():
    """Royal flush path and river_unbeatable agree on value line."""
    from tests.helpers.cemini_tables import six_max_table, _allowed

    table = six_max_table(
        name="royal_nuts_equiv",
        hero_seat=1,
        button_seat=1,
        street="River",
        board=["Ah", "Kh", "Th", "5d", "2c"],
        pot=200,
        hero_hole=["Qh", "Jh"],
        hero_stack=900,
        allowed=_allowed(
            can_check=True,
            can_bet=True,
            bet_range={"min": 20, "max": 900},
        ),
    )
    os.environ.setdefault("JACKPOT_ROYAL_SHOWDOWN", "1")
    out = decide(table, deadline_s=10.0)
    assert out["action"] == "check"
    assert "fold" not in out["action"]


def test_second_nut_flush_not_marked_unbeatable():
    """Kh Qd made flush is not nuts — enumeration must stay False."""
    from hand_nuts import river_unbeatable
    from tests.helpers.cemini_tables import six_max_table, _allowed

    hole, board = ["Kh", "Qd"], ["Jh", "Th", "5h", "2h", "3c"]
    ok, _, _ = river_unbeatable(hole, board)
    assert ok is False
    table = six_max_table(
        name="kh_qd_second_flush",
        hero_seat=1,
        button_seat=1,
        street="River",
        board=board,
        pot=450,
        hero_hole=hole,
        hero_stack=700,
        villain_bets={3: 200},
        allowed=_allowed(can_fold=True, can_call=True, call_chips=200, call_to=200),
    )
    out = decide(table, deadline_s=10.0)
    assert "river unbeatable" not in (out.get("message") or "").lower()


def test_nuts_skipped_under_clock_pressure(monkeypatch: pytest.MonkeyPatch):
    """deadline_s < 2 still acts on river nuts when CEMINI_NUTS_DETECT=1."""
    from tests.helpers.cemini_tables import board_quad_chop_river, nuts_quads_facing_bet

    monkeypatch.setenv("CEMINI_NUTS_DETECT", "1")
    table = nuts_quads_facing_bet()
    out = decide(table, deadline_s=1.5)
    assert out["action"] in {"call", "raise", "all-in"}
    chop = board_quad_chop_river()
    out_chop = decide(chop, deadline_s=1.5)
    assert out_chop["action"] in chop["allowedActions"]["availableActions"]
