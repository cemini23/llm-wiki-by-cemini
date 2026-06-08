"""Tests for S2 audit villain archetype module."""
from __future__ import annotations

import os

import sys
from pathlib import Path

import pytest

_EXAMPLES = Path(__file__).resolve().parent.parent / "examples"
if str(_EXAMPLES) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES))

from villain_archetype import (  # noqa: E402
    classify_villain_archetype,
    enrich_hud_from_table,
    jeff_nemesis_handle,
    phoenix_cluster_handle,
    premium_concentration_index,
    raise_gap,
)


def test_classify_premium_nit():
    stats = {"vpip": 0.10, "pfr": 0.04, "sampleSize": 200}
    assert classify_villain_archetype(stats, handle="alnitak") == "premium_nit"


def test_classify_wide_passive():
    stats = {"vpip": 0.42, "pfr": 0.05, "sampleSize": 200}
    assert classify_villain_archetype(stats, handle="ebay") == "wide_passive"


def test_classify_linear_aggro():
    stats = {"vpip": 0.41, "pfr": 0.27, "sampleSize": 500}
    assert classify_villain_archetype(stats, handle="0xJeff_ai") == "linear_aggro"


def test_phoenix_cluster_handle():
    assert phoenix_cluster_handle("phoenix-rises-nrkdhd-v10")
    assert not phoenix_cluster_handle("float_engine")


def test_premium_concentration_high_for_nit():
    assert premium_concentration_index({"vpip": 0.08, "pfr": 0.03}) >= 0.5


def test_raise_gap():
    assert raise_gap({"vpip": 0.40, "pfr": 0.05}) == pytest.approx(0.35)


def test_jeff_handle():
    assert jeff_nemesis_handle("0xJeff_ai")


def test_enrich_hud_from_table(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setenv("CEMINI_NEMESIS_ARCHETYPE", "1")
    table = {
        "selfSeatNumber": 1,
        "bigBlindChips": 20,
        "seats": [
            {"seatNumber": 1, "currentBetChips": 0, "stackChips": 1000},
            {
                "seatNumber": 2,
                "agentHandle": "alnitak",
                "currentBetChips": 60,
                "stats": {"vpip": 0.07, "pfr": 0.03, "sampleSize": 100},
            },
        ],
    }
    hud = enrich_hud_from_table({}, table)
    assert hud.get("archetype") == "premium_nit"
    assert hud.get("premium_concentration", 0) >= 0.45
