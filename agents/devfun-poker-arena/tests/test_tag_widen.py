"""TAG widen — halloran-class VPIP lift without gin."""
from __future__ import annotations

import os
import sys
from pathlib import Path

import pytest

_EXAMPLES = Path(__file__).resolve().parent.parent / "examples"
if str(_EXAMPLES) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES))

from research_static_chart import research_static_chart  # noqa: E402
from tag_widen import (  # noqa: E402
    apply_tag_widen_margins,
    tag_widen_allowed,
    tag_widen_enabled,
    tag_widen_margins,
)


@pytest.fixture(autouse=True)
def _clear_tag_env(monkeypatch):
    monkeypatch.delenv("CEMINI_TAG_WIDEN", raising=False)
    monkeypatch.delenv("CEMINI_GIN_KILL", raising=False)


def test_tag_widen_off_by_default():
    assert tag_widen_enabled() is False
    assert tag_widen_allowed() is False


def test_tag_widen_margins_mild(monkeypatch):
    monkeypatch.setenv("CEMINI_TAG_WIDEN", "1")
    m = tag_widen_margins()
    assert m["preflop_fold_margin_delta"] == pytest.approx(-0.025)
    assert m["open_steal_equity"] == pytest.approx(0.44)
    # Not gin-era spew
    assert m["fold_slack_delta"] > -0.04


def test_tag_widen_skipped_when_short(monkeypatch):
    monkeypatch.setenv("CEMINI_TAG_WIDEN", "1")
    assert tag_widen_allowed(short_stack=True) is False
    out = apply_tag_widen_margins({"call_margin_delta": 0.0}, short_stack=True)
    assert out.get("call_margin_delta", 0.0) == 0.0


def test_tag_widen_lowers_steal_bar_only(monkeypatch):
    monkeypatch.setenv("CEMINI_TAG_WIDEN", "1")
    out = apply_tag_widen_margins({"open_steal_equity": 0.99})
    assert out["open_steal_equity"] == pytest.approx(0.44)
    # Do not raise an already-low HUD steal bar
    out2 = apply_tag_widen_margins({"open_steal_equity": 0.34})
    assert out2["open_steal_equity"] == pytest.approx(0.34)


def test_tag_bb_chart_defend(monkeypatch):
    monkeypatch.setenv("CEMINI_TAG_WIDEN", "1")
    table = {
        "street": "Preflop",
        "tableFormat": "6max",
        "selfSeatNumber": 0,
        "buttonSeatNumber": 5,
        "seats": [
            {"seatNumber": 0, "holeCards": ["8h", "8d"]},  # BB vs need position
            {"seatNumber": 1, "holeCards": []},
            {"seatNumber": 2, "holeCards": []},
            {"seatNumber": 3, "holeCards": []},
            {"seatNumber": 4, "holeCards": []},
            {"seatNumber": 5, "holeCards": []},
        ],
    }
    # Force BB label via position_utils: seat 0 with button 5 → BB is usually seat 0 after SB
    # Use explicit selfPosition if chart uses hero_position_label
    table["selfPosition"] = "BB"
    chart = research_static_chart(table)
    assert chart.get("hand_class") == "88"
    assert chart.get("preflop_action") in ("call", "raise")
    assert "tag" in (chart.get("source") or "")


def test_tag_off_bb_still_folds_pairs(monkeypatch):
    monkeypatch.setenv("CEMINI_TAG_WIDEN", "0")
    table = {
        "street": "Preflop",
        "tableFormat": "6max",
        "selfSeatNumber": 0,
        "selfPosition": "BB",
        "buttonSeatNumber": 5,
        "seats": [{"seatNumber": 0, "holeCards": ["8h", "8d"]}],
    }
    chart = research_static_chart(table)
    # Base 6-max BB call set is empty — 88 folds without TAG
    assert chart.get("preflop_action") == "fold"
