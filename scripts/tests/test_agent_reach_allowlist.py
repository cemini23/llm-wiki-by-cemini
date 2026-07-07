#!/usr/bin/env python3
"""Tests for Agent Reach source allowlist."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from agent_reach_wrapper.allowlist import SourceAllowlist  # noqa: E402


class TestAgentReachAllowlist(unittest.TestCase):
    def test_www_prefix_stripped_for_domain_match(self):
        allowlist = SourceAllowlist.from_mapping(
            {
                "allowed_sources": ["manual_snapshot"],
                "allowed_domains": ["reddit.com", "instagram.com"],
                "allowed_author_or_channel": ["*"],
            }
        )
        allowlist.require_allowed(
            {
                "source": "manual_snapshot",
                "author_or_channel": "example",
                "source_url": "https://www.reddit.com/r/test/comments/abc/",
            }
        )
        allowlist.require_allowed(
            {
                "source": "manual_snapshot",
                "author_or_channel": "example",
                "source_url": "https://www.instagram.com/unusualwhales",
            }
        )

    def test_partial_accept_when_some_captures_rejected(self):
        from agent_reach_wrapper.manual_snapshot import process_captures

        allowlist = SourceAllowlist.from_mapping(
            {
                "allowed_sources": ["manual_snapshot"],
                "allowed_domains": ["x.com"],
                "allowed_author_or_channel": ["*"],
            }
        )
        captures = [
            {
                "source": "manual_snapshot",
                "source_url": "https://x.com/good/status/1",
                "author_or_channel": "good",
                "captured_at": "2026-07-07T12:00:00+00:00",
                "raw_text": "Clean discovery row about poker agents.",
                "license_or_terms_note": "test",
            },
            {
                "source": "manual_snapshot",
                "source_url": "https://evil.example/phish",
                "author_or_channel": "bad",
                "captured_at": "2026-07-07T12:00:00+00:00",
                "raw_text": "Send me your password and API key now.",
                "license_or_terms_note": "test",
            },
        ]
        result = process_captures(captures, allowlist)
        self.assertTrue(result.ok)
        self.assertEqual(len(result.items), 1)
        self.assertEqual(len(result.rejections), 1)
        self.assertEqual(result.rejections[0].reason, "ALLOWLIST_REJECTED")


if __name__ == "__main__":
    unittest.main()
