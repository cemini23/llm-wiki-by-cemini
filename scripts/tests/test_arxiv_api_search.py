#!/usr/bin/env python3
"""Tests for arXiv API fallback helpers."""

from __future__ import annotations

import fcntl
import sys
import tempfile
import unittest
import urllib.error
from email.message import Message
from pathlib import Path
from unittest.mock import MagicMock, patch

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from arxiv_api_search import (  # noqa: E402
    arxiv_id_from_entry_id,
    arxiv_search,
    natural_query_to_arxiv_search,
    parse_arxiv_atom,
)

SAMPLE_ATOM = """<?xml version='1.0' encoding='UTF-8'?>
<feed xmlns="http://www.w3.org/2005/Atom">
  <entry>
    <id>http://arxiv.org/abs/2607.05396v1</id>
    <title>Poker Agent Test Paper</title>
    <published>2026-07-06T17:59:59Z</published>
    <updated>2026-07-06T17:59:59Z</updated>
  </entry>
  <entry>
    <id>http://arxiv.org/abs/2501.00001v1</id>
    <title>Old Paper</title>
    <published>2025-01-01T00:00:00Z</published>
  </entry>
</feed>
"""


class TestArxivApiSearch(unittest.TestCase):
    def test_natural_query_strips_research_paper_prefix(self):
        q = natural_query_to_arxiv_search(
            "research paper poker reinforcement learning opponent modeling",
            max_terms=4,
        )
        self.assertIn("all:poker", q)
        self.assertIn("all:reinforcement", q)
        self.assertNotIn("research", q)
        # Must not AND every token — that starves short windows.
        self.assertIn(" OR ", q)

    def test_natural_query_or_branches(self):
        q = natural_query_to_arxiv_search(
            "LLM agent harness OR poker heads-up",
            max_terms=3,
        )
        self.assertIn(" OR ", q)

    def test_passthrough_atom_syntax(self):
        q = natural_query_to_arxiv_search(
            'all:poker AND all:reinforcement',
            max_terms=4,
        )
        self.assertEqual(q, "all:poker AND all:reinforcement")

    def test_arxiv_id_from_entry_id(self):
        self.assertEqual(
            arxiv_id_from_entry_id("http://arxiv.org/abs/2607.05396v1"),
            "2607.05396",
        )

    def test_parse_arxiv_atom_filters_by_date(self):
        hits = parse_arxiv_atom(SAMPLE_ATOM, from_date="2026-06-30")
        self.assertEqual(len(hits), 1)
        self.assertEqual(hits[0]["url"], "https://arxiv.org/abs/2607.05396")
        self.assertEqual(hits[0]["title"], "Poker Agent Test Paper")
        self.assertEqual(hits[0]["publishedDate"], "2026-07-06")

    def test_arxiv_search_retries_429_then_succeeds(self):
        err = _http_error(429)
        resp = _atom_response(SAMPLE_ATOM)
        with tempfile.TemporaryDirectory() as td:
            home = Path(td)
            with (
                patch("arxiv_api_search.Path.home", return_value=home),
                patch(
                    "arxiv_api_search.urllib.request.urlopen",
                    side_effect=[err, resp],
                ) as mock_open,
                patch("arxiv_api_search.time.sleep") as mock_sleep,
                patch("arxiv_api_search.fcntl.flock") as mock_flock,
            ):
                hits = arxiv_search(
                    "poker",
                    "2026-06-30",
                    request_interval_seconds=0,
                )
        self.assertEqual(len(hits), 1)
        self.assertEqual(hits[0]["url"], "https://arxiv.org/abs/2607.05396")
        self.assertEqual(mock_open.call_count, 2)
        mock_sleep.assert_called()
        self.assertTrue(
            any(c.args[1] == fcntl.LOCK_EX for c in mock_flock.call_args_list)
        )

    def test_arxiv_search_three_429s_returns_empty(self):
        err = _http_error(429)
        with tempfile.TemporaryDirectory() as td:
            home = Path(td)
            with (
                patch("arxiv_api_search.Path.home", return_value=home),
                patch(
                    "arxiv_api_search.urllib.request.urlopen",
                    side_effect=[err, err, err],
                ) as mock_open,
                patch("arxiv_api_search.time.sleep"),
                patch("arxiv_api_search.fcntl.flock"),
            ):
                hits = arxiv_search(
                    "poker",
                    "2026-06-30",
                    request_interval_seconds=0,
                )
        self.assertEqual(hits, [])
        self.assertEqual(mock_open.call_count, 3)

    def test_arxiv_search_creates_lock_file(self):
        resp = _atom_response(SAMPLE_ATOM)
        with tempfile.TemporaryDirectory() as td:
            home = Path(td)
            with (
                patch("arxiv_api_search.Path.home", return_value=home),
                patch("arxiv_api_search.urllib.request.urlopen", return_value=resp),
                patch("arxiv_api_search.time.sleep"),
            ):
                arxiv_search("poker", "2026-06-30", request_interval_seconds=0)
            lock = home / ".cemini" / "arxiv-api.lock"
            self.assertTrue(lock.is_file())


def _http_error(code: int, retry_after: str | None = None) -> urllib.error.HTTPError:
    hdrs = Message()
    if retry_after is not None:
        hdrs["Retry-After"] = retry_after
    return urllib.error.HTTPError(
        "https://export.arxiv.org/api/query",
        code,
        "Too Many Requests" if code == 429 else "Service Unavailable",
        hdrs,
        None,
    )


def _atom_response(xml_text: str) -> MagicMock:
    resp = MagicMock()
    resp.read.return_value = xml_text.encode("utf-8")
    resp.__enter__.return_value = resp
    resp.__exit__.return_value = False
    return resp


if __name__ == "__main__":
    unittest.main()
