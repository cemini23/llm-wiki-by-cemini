"""TAG widen — halloran-class VPIP lift without gin."""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

_EXAMPLES = Path(__file__).resolve().parent.parent / "examples"
if str(_EXAMPLES) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES))

from research_static_chart import research_static_chart  # noqa: E402
from tag_widen import (  # noqa: E402
    apply_tag_widen_margins,
    tag_facing_raise_to_call,
    tag_skip_broadway_auto_fold,
    tag_widen_allowed,
    tag_widen_enabled,
    tag_widen_margins,
    try_tag_bb_sb_defend,
)


@pytest.fixture(autouse=True)
def _clear_tag_env(monkeypatch):
    monkeypatch.delenv("CEMINI_TAG_WIDEN", raising=False)


def test_tag_widen_off_by_default():
    assert tag_widen_enabled() is False
    assert tag_widen_allowed() is False


def test_tag_widen_margins_stronger_than_gin_floor(monkeypatch):
    monkeypatch.setenv("CEMINI_TAG_WIDEN", "1")
    m = tag_widen_margins()
    assert m["preflop_fold_margin_delta"] == pytest.approx(-0.04)
    assert m["open_steal_equity"] == pytest.approx(0.40)
    # Still not gin-era postflop spew stack
    assert m["fold_slack_delta"] > -0.05


def test_tag_widen_skipped_when_short(monkeypatch):
    monkeypatch.setenv("CEMINI_TAG_WIDEN", "1")
    assert tag_widen_allowed(short_stack=True) is False
    out = apply_tag_widen_margins({"call_margin_delta": 0.0}, short_stack=True)
    assert out.get("call_margin_delta", 0.0) == 0.0


def test_tag_widen_lowers_steal_bar_only(monkeypatch):
    monkeypatch.setenv("CEMINI_TAG_WIDEN", "1")
    out = apply_tag_widen_margins({"open_steal_equity": 0.99})
    assert out["open_steal_equity"] == pytest.approx(0.40)
    out2 = apply_tag_widen_margins({"open_steal_equity": 0.34})
    assert out2["open_steal_equity"] == pytest.approx(0.34)


def test_tag_skips_broadway_auto_fold(monkeypatch):
    monkeypatch.setenv("CEMINI_TAG_WIDEN", "1")
    assert tag_skip_broadway_auto_fold("KQo", "BB") is True
    assert tag_skip_broadway_auto_fold("AJo", "BB") is True
    assert tag_skip_broadway_auto_fold("KQo", "SB") is True
    assert tag_skip_broadway_auto_fold("72o", "BB") is False
    assert tag_facing_raise_to_call("88", "BB") is True
    assert tag_facing_raise_to_call("72o", "BB") is False


def test_tag_bb_defend_steal_sized(monkeypatch):
    monkeypatch.setenv("CEMINI_TAG_WIDEN", "1")
    out = try_tag_bb_sb_defend(
        hand_class="KQo",
        position="BB",
        call_chips=40,
        big_blind=20,
        available=["fold", "call", "raise"],
        hero_stack_chips=1000,
    )
    assert out == ("call", None)
    # Bomb pot — no defend
    assert try_tag_bb_sb_defend(
        hand_class="KQo",
        position="BB",
        call_chips=200,
        big_blind=20,
        available=["fold", "call"],
        hero_stack_chips=1000,
    ) is None


def _six_max_bb_table(hole: list[str]) -> dict:
    seats = [{"seatNumber": i, "holeCards": [], "chips": 1000} for i in range(6)]
    seats[0] = {"seatNumber": 0, "holeCards": hole, "chips": 1000, "position": "BB"}
    return {
        "street": "Preflop",
        "tableFormat": "6max",
        "selfSeatNumber": 0,
        "buttonSeatNumber": 5,
        "seats": seats,
    }


def test_tag_bb_chart_defend(monkeypatch):
    monkeypatch.setenv("CEMINI_TAG_WIDEN", "1")
    chart = research_static_chart(_six_max_bb_table(["Kh", "Qd"]))
    assert chart.get("table_format") == "6max"
    assert chart.get("hand_class") == "KQo"
    assert chart.get("preflop_action") in ("call", "raise")
    assert "tag" in (chart.get("source") or "")


def test_tag_off_bb_still_folds_pairs(monkeypatch):
    monkeypatch.setenv("CEMINI_TAG_WIDEN", "0")
    chart = research_static_chart(_six_max_bb_table(["8h", "8d"]))
    assert chart.get("table_format") == "6max"
    assert chart.get("preflop_action") == "fold"
