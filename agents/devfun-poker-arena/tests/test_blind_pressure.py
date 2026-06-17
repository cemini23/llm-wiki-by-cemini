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
