#!/usr/bin/env python3
"""Tests for Macro Charts RSS helpers."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

from macro_charts_common import is_rss_teaser_only  # noqa: E402

SPEC = importlib.util.spec_from_file_location(
    "macro_charts_rss_poller",
    SCRIPTS / "macro_charts_rss_poller.py",
)
mod = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules["macro_charts_rss_poller"] = mod
SPEC.loader.exec_module(mod)


def test_teaser_detection():
    html = '<p>Good morning.</p><p><a href="https://www.macrocharts.com/p/foo">Read more</a></p>'
    assert is_rss_teaser_only(html, "Good morning.", "https://www.macrocharts.com/p/foo")


def test_macro_charts_wrapper_feed():
    assert mod.main is not None


if __name__ == "__main__":
    test_teaser_detection()
    test_macro_charts_wrapper_feed()
    print("ok")
