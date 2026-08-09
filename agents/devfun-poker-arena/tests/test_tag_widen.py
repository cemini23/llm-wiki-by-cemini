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
    tag_blind_defend_enabled,
    tag_facing_raise_to_call,
    tag_skip_broadway_auto_fold,
    tag_widen_allowed,
    tag_widen_enabled,
    tag_widen_margins,
    try_tag_bb_sb_defend,
    try_tag_blind_defend,
)


@pytest.fixture(autouse=True)
def _clear_tag_env(monkeypatch):
    monkeypatch.delenv("CEMINI_TAG_WIDEN", raising=False)
    monkeypatch.delenv("CEMINI_TAG_BLIND_DEFEND", raising=False)


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


def test_tag_sb_defend_wider_v3(monkeypatch):
    monkeypatch.setenv("CEMINI_TAG_WIDEN", "1")
    # v3 set includes suited connectors / mid pairs OOP
    for hc in ("87s", "76s", "66", "QJo", "JTo", "KTs"):
        out = try_tag_bb_sb_defend(
            hand_class=hc,
            position="SB",
            call_chips=60,
            big_blind=20,
            available=["fold", "call", "raise"],
            hero_stack_chips=1500,
        )
        assert out == ("call", None), hc
    # Still fold true trash
    assert try_tag_bb_sb_defend(
        hand_class="72o",
        position="SB",
        call_chips=40,
        big_blind=20,
        available=["fold", "call"],
        hero_stack_chips=1500,
    ) is None
    # 4.5bb cap allows 4x opens; 5x still blocked
    assert try_tag_bb_sb_defend(
        hand_class="87s",
        position="SB",
        call_chips=80,
        big_blind=20,
        available=["fold", "call"],
        hero_stack_chips=1500,
    ) == ("call", None)
    assert try_tag_bb_sb_defend(
        hand_class="87s",
        position="SB",
        call_chips=120,
        big_blind=20,
        available=["fold", "call"],
        hero_stack_chips=1500,
    ) is None


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


def test_blind_defend_off_by_default():
    assert tag_blind_defend_enabled() is False
    assert try_tag_blind_defend(
        hand_class="KQo",
        position="BB",
        call_chips=40,
        big_blind=20,
        available=["fold", "call", "raise"],
        hero_stack_chips=1000,
    ) is None


def test_blind_defend_bb_steal_sized(monkeypatch):
    """CEMINI_TAG_BLIND_DEFEND alone (no TAG_WIDEN) defends BB vs ≤3bb / ≤10% stack."""
    monkeypatch.setenv("CEMINI_TAG_BLIND_DEFEND", "1")
    monkeypatch.setenv("CEMINI_TAG_WIDEN", "0")
    out = try_tag_blind_defend(
        hand_class="KQo",
        position="BB",
        call_chips=40,
        big_blind=20,
        available=["fold", "call", "raise"],
        hero_stack_chips=1000,
    )
    assert out == ("call", None)
    # 4bb open — over 3bb cap
    assert try_tag_blind_defend(
        hand_class="KQo",
        position="BB",
        call_chips=80,
        big_blind=20,
        available=["fold", "call"],
        hero_stack_chips=1000,
    ) is None
    # call > 10% stack blocked
    assert try_tag_blind_defend(
        hand_class="KQo",
        position="BB",
        call_chips=40,
        big_blind=20,
        available=["fold", "call"],
        hero_stack_chips=300,
    ) is None


def test_blind_defend_sb_no_qjo_cold_call(monkeypatch):
    """QJo is open-only under chase; blind defend must not cold-call QJo from SB."""
    monkeypatch.setenv("CEMINI_TAG_BLIND_DEFEND", "1")
    assert try_tag_blind_defend(
        hand_class="QJo",
        position="SB",
        call_chips=40,
        big_blind=20,
        available=["fold", "call"],
        hero_stack_chips=1000,
    ) is None
    # Suited broadway still defends
    assert try_tag_blind_defend(
        hand_class="QJs",
        position="SB",
        call_chips=40,
        big_blind=20,
        available=["fold", "call"],
        hero_stack_chips=1000,
    ) == ("call", None)


def test_blind_defend_skips_broadway_auto_fold(monkeypatch):
    monkeypatch.setenv("CEMINI_TAG_BLIND_DEFEND", "1")
    monkeypatch.setenv("CEMINI_TAG_WIDEN", "0")
    assert tag_skip_broadway_auto_fold("KQo", "BB") is True
    assert tag_facing_raise_to_call("88", "BB") is True
    assert tag_skip_broadway_auto_fold("QJo", "SB") is False  # not in SB defend set
