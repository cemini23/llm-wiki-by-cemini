#!/usr/bin/env python3
"""Tests for Macro Charts watch condition engine + propose heuristics."""

from __future__ import annotations

import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[1]
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from macro_charts_watch import (  # noqa: E402
    Condition,
    Watch,
    condition_holds,
    eval_watch,
    propose_from_text,
    uw_ticker_for_symbol,
)


def test_condition_holds_basic():
    assert condition_holds("gt", 21.0, 20.0, None) is True
    assert condition_holds("gt", 19.0, 20.0, None) is False
    assert condition_holds("lt", 19.0, 20.0, None) is True
    assert condition_holds("gte", 20.0, 20.0, None) is True
    assert condition_holds("lte", 20.0, 20.0, None) is True


def test_cross_above_needs_prev():
    assert condition_holds("cross_above", 21.0, 20.0, 19.5) is True
    assert condition_holds("cross_above", 21.0, 20.0, 20.5) is False
    assert condition_holds("cross_below", 19.0, 20.0, 20.5) is True
    assert condition_holds("cross_below", 19.0, 20.0, 18.5) is False


def test_eval_watch_sustain():
    w = Watch(
        id="t1",
        symbol="^VIX",
        condition=Condition(op="gt", level=20.0, sustain_checks=2),
        status="armed",
        created_at="2026-07-27T00:00:00Z",
    )
    fire, w = eval_watch(w, 21.0)
    assert fire is False
    assert w.hold_count == 1
    fire, w = eval_watch(w, 22.0)
    assert fire is True
    assert w.hold_count == 2


def test_eval_watch_resets_hold():
    w = Watch(
        id="t2",
        symbol="^VIX",
        condition=Condition(op="gt", level=20.0, sustain_checks=2),
        status="armed",
        created_at="2026-07-27T00:00:00Z",
    )
    _, w = eval_watch(w, 21.0)
    fire, w = eval_watch(w, 19.0)
    assert fire is False
    assert w.hold_count == 0


def test_propose_vix_sustain():
    text = "VIX may have bottomed — watch sustain >20; asset managers hold large shorts."
    cands = propose_from_text(text, aliases={"VIX": "^VIX"})
    assert len(cands) >= 1
    assert cands[0]["symbol"] == "^VIX"
    assert cands[0]["condition"]["op"] == "gt"
    assert cands[0]["condition"]["level"] == 20.0


def test_propose_sox_defend():
    text = "SOX buyers defending ~$12k critical support."
    cands = propose_from_text(text, aliases={"SOX": "^SOX"})
    assert any(c["condition"]["level"] == 12000.0 and c["condition"]["op"] == "lt" for c in cands)


def test_propose_dxy_testing():
    text = "DXY broke May uptrend, testing ~100.50 — Sell active."
    cands = propose_from_text(text, aliases={"DXY": "DX-Y.NYB"})
    assert any(abs(c["condition"]["level"] - 100.50) < 1e-6 for c in cands)


def test_uw_ticker_map_skips_vix():
    cfg = {"uw_symbol_map": {"^VIX": "", "SPY": "SPY", "^GSPC": "SPY"}}
    assert uw_ticker_for_symbol("^VIX", cfg) is None
    assert uw_ticker_for_symbol("SPY", cfg) == "SPY"
    assert uw_ticker_for_symbol("^GSPC", cfg) == "SPY"
    assert uw_ticker_for_symbol("GDX", cfg) == "GDX"
