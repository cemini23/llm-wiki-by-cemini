#!/usr/bin/env python3
"""Tests for unified Substack RSS poller."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

from macro_charts_common import is_rss_teaser_only, normalize_post_url, post_already_exported  # noqa: E402

SPEC = importlib.util.spec_from_file_location(
    "substack_rss_poller",
    SCRIPTS / "substack_rss_poller.py",
)
mod = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules["substack_rss_poller"] = mod
SPEC.loader.exec_module(mod)


def test_teaser_detection_substack():
    html = '<p>Snippet</p><p><a href="https://klementoninvesting.substack.com/p/foo">Read more</a></p>'
    assert is_rss_teaser_only(html, "Snippet.", "https://klementoninvesting.substack.com/p/foo")


def test_teaser_detection_macrocharts():
    html = '<p>Good morning.</p><p><a href="https://www.macrocharts.com/p/foo">Read more</a></p>'
    assert is_rss_teaser_only(html, "Good morning.", "https://www.macrocharts.com/p/foo")


def test_post_url_dedup_email_overrides_rss():
    state = {
        "posts": {
            normalize_post_url("https://www.macrocharts.com/p/foo"): {
                "source": "rss:macrocharts",
                "filename": "macro-charts-rss-2026-07-05-foo.md",
            }
        }
    }
    assert post_already_exported(state, "https://www.macrocharts.com/p/foo")
    assert not post_already_exported(
        state, "https://www.macrocharts.com/p/foo", prefer_source="email"
    )


def test_parse_feed_configs_count():
    cfg = mod.load_config()
    feeds = mod.parse_feed_configs(cfg)
    ids = {f.id for f in feeds}
    assert "macrocharts" in ids
    assert "klement" in ids
    assert "moontower" in ids
    assert "glitchspx" in ids
    assert len(feeds) >= 19


def test_parse_feed_sample():
    sample = b"""<?xml version="1.0"?>
    <rss xmlns:content="http://purl.org/rss/1.0/modules/content/" version="2.0">
      <channel>
        <item>
          <title>Test Issue</title>
          <link>https://klementoninvesting.substack.com/p/test-issue</link>
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
    test_teaser_detection_substack()
    test_teaser_detection_macrocharts()
    test_post_url_dedup_email_overrides_rss()
    test_parse_feed_configs_count()
    test_parse_feed_sample()
    print("ok")
