#!/usr/bin/env python3
"""Tests for Macro Charts RSS helpers."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

from macro_charts_common import is_rss_teaser_only, normalize_post_url, post_already_exported  # noqa: E402

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
    assert is_rss_teaser_only(html, "Good morning.")


def test_post_url_dedup_email_overrides_rss():
    state = {
        "posts": {
            normalize_post_url("https://www.macrocharts.com/p/foo"): {
                "source": "rss",
                "filename": "macro-charts-rss-2026-07-05-foo.md",
            }
        }
    }
    assert post_already_exported(state, "https://www.macrocharts.com/p/foo")
    assert not post_already_exported(
        state, "https://www.macrocharts.com/p/foo", prefer_source="email"
    )


def test_parse_feed_sample():
    sample = b"""<?xml version="1.0"?>
    <rss xmlns:content="http://purl.org/rss/1.0/modules/content/" version="2.0">
      <channel>
        <item>
          <title>Test Issue</title>
          <link>https://www.macrocharts.com/p/test-issue</link>
          <pubDate>Sun, 05 Jul 2026 11:33:10 GMT</pubDate>
          <description>Teaser</description>
          <content:encoded><![CDATA[<p>Body</p>]]></content:encoded>
        </item>
      </channel>
    </rss>"""
    items = mod.parse_feed(sample)
    assert len(items) == 1
    assert items[0].title == "Test Issue"
    assert items[0].link.endswith("/p/test-issue")


if __name__ == "__main__":
    test_teaser_detection()
    test_post_url_dedup_email_overrides_rss()
    test_parse_feed_sample()
    print("ok")
