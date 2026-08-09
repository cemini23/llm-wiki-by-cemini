"""Blind-orbit pressure helpers."""
from __future__ import annotations

from blind_pressure import (
    avg_blind_tax_per_hand,
    hands_to_erosion,
    lead_blind_steal,
)


def test_avg_blind_tax_6max():
    assert avg_blind_tax_per_hand() == 5.0


def test_hands_to_erosion():
    assert hands_to_erosion(7000) == 1400


def test_lead_blind_steal_btn():
    assert lead_blind_steal("ATo", "BTN")
    assert not lead_blind_steal("72o", "BTN")


def test_lead_blind_steal_co_tighter():
    assert lead_blind_steal("JTs", "CO")
    assert not lead_blind_steal("A9o", "CO")


def test_placement_chase_steal_mp():
    from blind_pressure import placement_chase_steal

    assert placement_chase_steal("98s", "MP")
    assert not placement_chase_steal("72o", "MP")


def test_placement_chase_sb_force_open():
    from blind_pressure import placement_chase_sb_force_open

    # Unopened SB force set
    for hc in ("QJo", "KTo", "A9o", "22", "KQs", "JTs", "AKo"):
        assert placement_chase_sb_force_open(hc, "SB"), hc
    # Not force-open trash / wrong position
    assert not placement_chase_sb_force_open("72o", "SB")
    assert not placement_chase_sb_force_open("QJo", "BB")
    assert not placement_chase_sb_force_open("QJo", "BTN")
    assert not placement_chase_sb_force_open("A8o", "SB")


def test_placement_chase_sb_force_open_before_equity_gate():
    """placement_chase + unopened SB opens QJo even when equity is below chase floor."""
    from cemini_decide import _preflop_open

    allowed = {
        "canBet": True,
        "canRaise": False,
        "betRange": {"min": 30, "max": 800},
        "availableActions": ["fold", "check", "bet"],
        "callChips": 0,
    }
    available = ["fold", "check", "bet"]
    for hc in ("QJo", "KTo", "A9o", "22"):
        act, _amt = _preflop_open(
            "fold",
            allowed,
            available,
            pot=30,
            equity=0.15,  # below chase_open_equity ~0.38
            hand_class=hc,
            position="SB",
            placement_chase=True,
        )
        assert act == "bet", (hc, act)
