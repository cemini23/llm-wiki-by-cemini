#!/usr/bin/env python3
"""Tests for Macro Charts forward classification."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location(
    "macro_charts_email_poller",
    ROOT / "scripts" / "macro_charts_email_poller.py",
)
mod = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules["macro_charts_email_poller"] = mod
SPEC.loader.exec_module(mod)

classify = mod.classify_macro_charts
SIGNALS = [
    "macrocharts.com",
    "macrocharts.substack.com",
    "from: macro charts",
]
COUSIN = ["vinnyb64@gmail.com"]


def test_marco_charts_forward_matches():
    body = """
    ---------- Forwarded message ---------
    From: Macro Charts <macrocharts@substack.com>
    Subject: A DECISIVE turn in markets

    Read on macrocharts.com:
    https://www.macrocharts.com/p/decisive-turn
    """
    ok, matched = classify(
        "Fwd: A DECISIVE turn",
        "Vincent Barone <vinnyb64@gmail.com>",
        body,
        SIGNALS,
        COUSIN,
        [],
    )
    assert ok
    assert "macrocharts.com" in matched


def test_cousin_other_email_rejected():
    body = "Hey, dinner Saturday?"
    ok, _ = classify(
        "Weekend plans",
        "Vincent Barone <vinnyb64@gmail.com>",
        body,
        SIGNALS,
        COUSIN,
        [],
    )
    assert not ok


def test_wrong_sender_rejected_even_with_signals():
    body = "See https://macrocharts.com/p/foo"
    ok, _ = classify(
        "Fwd: markets",
        "stranger@example.com",
        body,
        SIGNALS,
        COUSIN,
        [],
    )
    assert not ok


if __name__ == "__main__":
    test_marco_charts_forward_matches()
    test_cousin_other_email_rejected()
    test_wrong_sender_rejected_even_with_signals()
    print("ok")
