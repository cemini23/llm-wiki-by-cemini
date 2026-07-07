#!/usr/bin/env python3
"""Tests for arXiv API fallback helpers."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from arxiv_api_search import (  # noqa: E402
    arxiv_id_from_entry_id,
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

    def test_natural_query_or_branches(self):
        q = natural_query_to_arxiv_search(
            "LLM agent harness OR poker heads-up",
            max_terms=3,
        )
        self.assertIn(" OR ", q)

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


if __name__ == "__main__":
    unittest.main()
