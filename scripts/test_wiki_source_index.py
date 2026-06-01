#!/usr/bin/env python3
"""Smoke tests for wiki_source_index (no network)."""

import unittest
from pathlib import Path
import sys

_SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(_SCRIPTS))

from wiki_source_index import (  # noqa: E402
    arxiv_id_from_url,
    normalize_url,
    verdict_for_remote_hit,
)


class TestWikiSourceIndex(unittest.TestCase):
    def test_arxiv_id_from_url(self):
        self.assertEqual(
            arxiv_id_from_url("https://arxiv.org/abs/2604.24366"),
            "2604.24366",
        )
        self.assertIsNone(arxiv_id_from_url("https://example.com/paper"))

    def test_verdict_new_when_empty_index(self):
        idx = {
            "arxiv": {},
            "doi": {},
            "url": {},
            "location_basename": {},
            "title_norm": {},
            "all_titles": [],
        }
        v, _ = verdict_for_remote_hit(
            "https://arxiv.org/abs/9999.99999",
            "Totally Novel Paper Title",
            idx,
            set(),
        )
        self.assertEqual(v, "NEW")

    def test_verdict_dup_when_in_wiki(self):
        idx = {
            "arxiv": {"2604.24366": ["sources/foo.md"]},
            "doi": {},
            "url": {},
            "location_basename": {},
            "title_norm": {},
            "all_titles": [],
        }
        v, notes = verdict_for_remote_hit(
            "https://arxiv.org/pdf/2604.24366.pdf",
            "Some title",
            idx,
            set(),
        )
        self.assertEqual(v, "DUPLICATE")
        self.assertTrue(notes)


if __name__ == "__main__":
    unittest.main()
