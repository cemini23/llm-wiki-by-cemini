"""Target Hospitality hiring watcher — unit + offline lifecycle tests."""

import datetime as dt
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from scripts.intel.monitors.th_jobs import (
    dedupe_new,
    is_relevant,
    match_sites,
    parse_opportunity,
    parse_results,
    run,
)

SETTINGS = {"tenant": "TAR1004TARG", "board_id": "board123", "top": 50}

RAW_DILLEY = {
    "Id": "opp-dilley-1",
    "RequisitionNumber": "SEC007001",
    "Title": "Security Officer",
    "JobCategoryName": "Security",
    "FullTime": True,
    "PostedDate": "2026-07-01T15:10:56.539Z",
    "BriefDescription": "Family residential center support.",
    "Locations": [
        {
            "LocalizedName": "Target Hospitality - Dilley",
            "LocalizedLocationId": "Dilley",
            "Address": {"City": None, "State": {"Code": "TX", "Name": "Texas"}},
        }
    ],
}

RAW_PERMIAN = {
    "Id": "opp-permian-1",
    "RequisitionNumber": "HOUSE007248",
    "Title": "Housekeeper",
    "JobCategoryName": "Hospitality",
    "FullTime": True,
    "PostedDate": "2026-07-02T00:00:00.000Z",
    "BriefDescription": "Lodge housekeeping.",
    "Locations": [
        {
            "LocalizedName": "Target Hospitality - West Texas",
            "LocalizedLocationId": "West Texas",
            "Address": {"City": None, "State": {"Code": "TX", "Name": "Texas"}},
        }
    ],
}

RESPONSE = {"opportunities": [RAW_DILLEY, RAW_PERMIAN], "totalCount": 2}

CONFIG_YAML = """
settings:
  tenant: TAR1004TARG
  board_id: board123
  top: 50
  alert_on_new: true
target_sites:
  - id: dilley_stfrc
    label: Dilley
    ticker: TH
    match_terms: [Dilley, South Texas Family, STFRC]
watch_terms:
  - government
  - security officer
"""


class ParseTests(unittest.TestCase):
    def test_parse_opportunity(self):
        rec = parse_opportunity(RAW_DILLEY, SETTINGS)
        self.assertEqual(rec["id"], "opp-dilley-1")
        self.assertEqual(rec["posted"], "2026-07-01")
        self.assertIn("Dilley", rec["location"])
        self.assertIn("board123", rec["url"])

    def test_parse_results(self):
        recs = parse_results(RESPONSE, SETTINGS)
        self.assertEqual(len(recs), 2)


class MatchTests(unittest.TestCase):
    def test_match_sites_hits_dilley(self):
        sites = [{"id": "dilley_stfrc", "match_terms": ["Dilley", "STFRC"]}]
        rec = parse_opportunity(RAW_DILLEY, SETTINGS)
        self.assertEqual(match_sites(rec, sites), ["dilley_stfrc"])

    def test_match_sites_misses_permian(self):
        sites = [{"id": "dilley_stfrc", "match_terms": ["Dilley", "STFRC"]}]
        rec = parse_opportunity(RAW_PERMIAN, SETTINGS)
        self.assertEqual(match_sites(rec, sites), [])

    def test_is_relevant_site_wins(self):
        rec = parse_opportunity(RAW_DILLEY, SETTINGS)
        self.assertTrue(is_relevant(rec, [], ["dilley_stfrc"]))

    def test_is_relevant_watch_term_fallback(self):
        rec = parse_opportunity(RAW_DILLEY, SETTINGS)  # title "Security Officer"
        self.assertTrue(is_relevant(rec, ["security officer"], []))
        self.assertFalse(is_relevant(parse_opportunity(RAW_PERMIAN, SETTINGS), ["security officer"], []))


class DedupeTests(unittest.TestCase):
    def test_dedupe(self):
        recs = parse_results(RESPONSE, SETTINGS)
        self.assertEqual(len(dedupe_new(recs, set())), 2)
        self.assertEqual(len(dedupe_new(recs, {"opp-dilley-1"})), 1)


class RunLifecycleTests(unittest.TestCase):
    def test_first_run_then_new_relevant(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmpdir = Path(tmp)
            cfg = tmpdir / "th-jobs.yaml"
            cfg.write_text(CONFIG_YAML, encoding="utf-8")
            today = dt.date(2026, 7, 7)

            with mock.patch("scripts.intel.monitors.th_jobs.report_dir", return_value=tmpdir):
                r1 = run(cfg, today, offline_records=[RAW_DILLEY, RAW_PERMIAN])
                self.assertTrue(r1["first_run"])
                self.assertEqual(r1["alerts"], 0)
                self.assertTrue(r1["report_path"].is_file())

                r2 = run(cfg, today, offline_records=[RAW_DILLEY, RAW_PERMIAN])
                self.assertFalse(r2["first_run"])
                self.assertEqual(r2["new_relevant"], [])

                new_dilley = dict(RAW_DILLEY, Id="opp-dilley-2", Title="Case Manager")
                r3 = run(cfg, today, offline_records=[RAW_DILLEY, RAW_PERMIAN, new_dilley])
                # new_dilley matches site -> relevant; permian already seen
                self.assertEqual(len(r3["new_relevant"]), 1)
                self.assertEqual(r3["new_relevant"][0]["id"], "opp-dilley-2")

    def test_network_error_is_captured(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmpdir = Path(tmp)
            cfg = tmpdir / "th-jobs.yaml"
            cfg.write_text(CONFIG_YAML, encoding="utf-8")
            with mock.patch("scripts.intel.monitors.th_jobs.report_dir", return_value=tmpdir), mock.patch(
                "scripts.intel.monitors.th_jobs.fetch_opportunities", side_effect=RuntimeError("boom")
            ):
                result = run(cfg, dt.date(2026, 7, 7))
                self.assertEqual(result["all_records"], [])
                self.assertIn("boom", result["error"])


if __name__ == "__main__":
    unittest.main()
