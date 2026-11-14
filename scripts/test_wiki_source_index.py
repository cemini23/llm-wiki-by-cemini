#!/usr/bin/env python3
"""Smoke tests for wiki_source_index (no network)."""

import tempfile
import unittest
from pathlib import Path
import sys

_SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(_SCRIPTS))

from wiki_source_index import (  # noqa: E402
    arxiv_id_from_url,
    build_repo_wiki_index,
    doi_from_url,
    inbox_arxiv_ids,
    normalize_url,
    verdict_for_remote_hit,
)

SOURCE_PAGE = """---
title: "A Gambling Paper"
type: source
---

## Raw Concept

| Field | Value |
|-------|-------|
| arXiv | 2611.10152v1 |
| DOI | 10.1234/example.5678 |
"""


class TestMergedWikiIndex(unittest.TestCase):
    def test_reads_sources_from_domain_folders(self):
        with tempfile.TemporaryDirectory() as tmp:
            wiki = Path(tmp) / "wiki"
            domain = wiki / "gambling" / "sources"
            domain.mkdir(parents=True)
            (domain / "paper.md").write_text(SOURCE_PAGE)
            idx = build_repo_wiki_index(wiki)
            self.assertIn("2611.10152", idx["arxiv"])
            self.assertIn("10.1234/example.5678", idx["doi"])

    def test_duplicate_verdict_uses_domain_sources(self):
        with tempfile.TemporaryDirectory() as tmp:
            wiki = Path(tmp) / "wiki"
            domain = wiki / "gambling" / "sources"
            domain.mkdir(parents=True)
            (domain / "paper.md").write_text(SOURCE_PAGE)
            idx = build_repo_wiki_index(wiki)
            v, notes = verdict_for_remote_hit(
                "https://arxiv.org/abs/2611.10152", "Some title", idx, set()
            )
            self.assertEqual(v, "DUPLICATE")
            self.assertTrue(notes)

    def test_doi_url_matches_wiki_doi(self):
        with tempfile.TemporaryDirectory() as tmp:
            wiki = Path(tmp) / "wiki"
            domain = wiki / "osint" / "sources"
            domain.mkdir(parents=True)
            (domain / "paper.md").write_text(SOURCE_PAGE)
            idx = build_repo_wiki_index(wiki)
            v, _ = verdict_for_remote_hit(
                "https://doi.org/10.1234/example.5678", "Some title", idx, set()
            )
            self.assertEqual(v, "DUPLICATE")


class TestArchiveScan(unittest.TestCase):
    def test_recursive_scan_reaches_holding_area(self):
        with tempfile.TemporaryDirectory() as tmp:
            archive = Path(tmp) / "_ingested-awaiting-archive"
            nested = archive / "gambling"
            nested.mkdir(parents=True)
            (nested / "arxiv-2611.10152-modeling.pdf").write_bytes(b"%PDF-1.4")
            self.assertEqual(inbox_arxiv_ids(archive), set())
            self.assertEqual(inbox_arxiv_ids(archive, recursive=True), {"2611.10152"})


class TestDoiFromUrl(unittest.TestCase):
    def test_extracts_doi(self):
        self.assertEqual(
            doi_from_url("https://doi.org/10.1234/example.5678"),
            "10.1234/example.5678",
        )
        self.assertIsNone(doi_from_url("https://example.com/paper"))


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
