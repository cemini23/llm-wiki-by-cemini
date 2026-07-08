"""DoD/DOE (Federal Register) watcher — unit + offline lifecycle tests."""

import datetime as dt
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from scripts.intel.monitors.fedreg import (
    build_query_url,
    dedupe_new,
    is_watched,
    parse_documents,
    run,
)

SAMPLE_RESPONSE = {
    "count": 2,
    "results": [
        {
            "title": "Defense Production Act Title III Determination: Rare Earth Magnets",
            "document_number": "2026-12825",
            "publication_date": "2026-06-25",
            "html_url": "https://www.federalregister.gov/documents/2026/06/25/2026-12825",
            "type": "Presidential Document",
            "abstract": "A price floor and offtake determination under Title III for rare earth magnets.",
        },
        {
            "title": "Uranium Enrichment Domestic Supply Notice",
            "document_number": "2026-13001",
            "publication_date": "2026-06-20",
            "html_url": "https://www.federalregister.gov/documents/2026/06/20/2026-13001",
            "type": "Notice",
            "abstract": "DOE strategic reserve for enrichment.",
        },
    ],
}

CONFIG_YAML = """
settings:
  lookback_days: 30
  per_page: 20
  alert_on_new: true
  default_agencies: [defense-department, energy-department]
queries:
  - id: dpa_title_iii
    term: "Defense Production Act Title III"
  - id: uranium_enrichment
    term: "uranium enrichment"
    agencies: [energy-department]
watch_terms:
  - Title III
  - uranium
"""


class UrlTests(unittest.TestCase):
    def test_build_query_url_defaults_and_fields(self):
        url = build_query_url(
            {"id": "q", "term": "Title III"},
            startdt="2026-06-01",
            enddt="2026-07-07",
            settings={"per_page": 20, "default_agencies": ["defense-department"]},
        )
        self.assertIn("conditions%5Bterm%5D=Title+III", url)
        self.assertIn("conditions%5Bpublication_date%5D%5Bgte%5D=2026-06-01", url)
        self.assertIn("conditions%5Bagencies%5D%5B%5D=defense-department", url)
        self.assertIn("fields%5B%5D=document_number", url)

    def test_query_agencies_override(self):
        url = build_query_url(
            {"id": "q", "term": "x", "agencies": ["energy-department"]},
            startdt="a",
            enddt="b",
            settings={"default_agencies": ["defense-department"]},
        )
        self.assertIn("energy-department", url)
        self.assertNotIn("defense-department", url)


class ParseTests(unittest.TestCase):
    def test_parse_documents(self):
        docs = parse_documents(SAMPLE_RESPONSE, "dpa_title_iii")
        self.assertEqual(len(docs), 2)
        self.assertEqual(docs[0]["id"], "2026-12825")
        self.assertEqual(docs[0]["type"], "Presidential Document")
        self.assertEqual(docs[0]["query"], "dpa_title_iii")

    def test_parse_empty(self):
        self.assertEqual(parse_documents({}, "q"), [])


class WatchTests(unittest.TestCase):
    def test_is_watched_title_and_abstract(self):
        docs = parse_documents(SAMPLE_RESPONSE, "q")
        self.assertTrue(is_watched(docs[0], ["Title III"]))
        self.assertTrue(is_watched(docs[1], ["uranium"]))
        self.assertFalse(is_watched(docs[0], ["antimony"]))
        self.assertFalse(is_watched(docs[0], []))


class DedupeTests(unittest.TestCase):
    def test_dedupe_excludes_seen_and_batch_dupes(self):
        docs = parse_documents(SAMPLE_RESPONSE, "q") * 2
        self.assertEqual(len(dedupe_new(docs, set())), 2)
        self.assertEqual(len(dedupe_new(docs, {"2026-12825"})), 1)


class RunLifecycleTests(unittest.TestCase):
    def test_first_run_then_diff(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmpdir = Path(tmp)
            cfg = tmpdir / "fedreg.yaml"
            cfg.write_text(CONFIG_YAML, encoding="utf-8")
            today = dt.date(2026, 7, 7)
            payloads = {"dpa_title_iii": SAMPLE_RESPONSE, "uranium_enrichment": {}}

            with mock.patch("scripts.intel.monitors.fedreg.report_dir", return_value=tmpdir):
                r1 = run(cfg, today, offline_payloads=payloads)
                self.assertTrue(r1["first_run"])
                self.assertEqual(r1["alerts"], 0)
                self.assertTrue(r1["report_path"].is_file())

                r2 = run(cfg, today, offline_payloads=payloads)
                self.assertFalse(r2["first_run"])
                self.assertEqual(r2["new_docs"], [])

                new_payload = {
                    "dpa_title_iii": {
                        "results": [
                            {
                                "title": "New Title III antimony determination",
                                "document_number": "2026-99999",
                                "publication_date": "2026-07-05",
                                "html_url": "https://example.gov/x",
                                "type": "Notice",
                                "abstract": "antimony strategic reserve",
                            }
                        ]
                    }
                }
                r3 = run(cfg, today, offline_payloads=new_payload)
                self.assertEqual(len(r3["new_docs"]), 1)
                self.assertEqual(r3["new_docs"][0]["id"], "2026-99999")

    def test_network_error_is_captured(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmpdir = Path(tmp)
            cfg = tmpdir / "fedreg.yaml"
            cfg.write_text(CONFIG_YAML, encoding="utf-8")
            with mock.patch("scripts.intel.monitors.fedreg.report_dir", return_value=tmpdir), mock.patch(
                "scripts.intel.monitors.fedreg.search_query", side_effect=RuntimeError("boom")
            ):
                result = run(cfg, dt.date(2026, 7, 7))
                self.assertEqual(result["all_docs"], [])
                self.assertTrue(any("boom" in e for e in result["errors"]))


if __name__ == "__main__":
    unittest.main()
