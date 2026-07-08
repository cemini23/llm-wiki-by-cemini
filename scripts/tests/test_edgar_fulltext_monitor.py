"""EDGAR full-text watcher — unit + offline lifecycle tests (no network)."""

import datetime as dt
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from scripts.intel import paths
from scripts.intel.monitors.edgar_fulltext import (
    build_efts_url,
    dedupe_new,
    filter_hits,
    matches_watch,
    parse_efts_hits,
    run,
)

SAMPLE_CXW = {
    "hits": {
        "total": {"value": 1},
        "hits": [
            {
                "_id": "0001070985-26-000045:doc.htm",
                "_source": {
                    "ciks": ["0001070985"],
                    "display_names": ["CoreCivic, Inc. (CXW)"],
                    "file_date": "2026-07-06",
                    "form": "8-K",
                    "root_forms": ["8-K"],
                },
            }
        ],
    }
}

SAMPLE_UNRELATED = {
    "hits": {
        "hits": [
            {
                "_id": "0000999999-26-000001:doc.htm",
                "_source": {
                    "ciks": ["0000999999"],
                    "display_names": ["Unrelated Widgets Corp (WDGT)"],
                    "file_date": "2026-07-05",
                    "form": "8-K",
                    "root_forms": ["8-K"],
                },
            }
        ]
    }
}

CONFIG_YAML = """
settings:
  lookback_days: 3
  forms: [8-K]
  alert_on_new: true
query_terms:
  - turnkey
watch_ciks:
  - "1070985"
watch_names:
  - CoreCivic
"""


class EdgarUrlTests(unittest.TestCase):
    def test_build_url_quotes_phrase_and_dates(self):
        url = build_efts_url(
            "sale of facility", forms=["8-K"], startdt="2026-07-04", enddt="2026-07-07"
        )
        self.assertIn("q=%22sale+of+facility%22", url)
        self.assertIn("forms=8-K", url)
        self.assertIn("startdt=2026-07-04", url)
        self.assertIn("enddt=2026-07-07", url)
        self.assertIn("dateRange=custom", url)

    def test_build_url_ciks(self):
        url = build_efts_url("turnkey", ciks=["1070985", "923796"])
        self.assertIn("ciks=1070985%2C923796", url)


class EdgarParseTests(unittest.TestCase):
    def test_parse_efts_hits(self):
        hits = parse_efts_hits(SAMPLE_CXW, "turnkey")
        self.assertEqual(len(hits), 1)
        self.assertEqual(hits[0]["id"], "0001070985-26-000045:doc.htm")
        self.assertEqual(hits[0]["form"], "8-K")
        self.assertEqual(hits[0]["file_date"], "2026-07-06")
        self.assertEqual(hits[0]["term"], "turnkey")

    def test_parse_empty(self):
        self.assertEqual(parse_efts_hits({}, "turnkey"), [])


class EdgarFilterTests(unittest.TestCase):
    def test_matches_watch_by_cik(self):
        hit = parse_efts_hits(SAMPLE_CXW, "turnkey")[0]
        self.assertTrue(matches_watch(hit, {"1070985"}, []))

    def test_matches_watch_by_name(self):
        hit = parse_efts_hits(SAMPLE_CXW, "turnkey")[0]
        self.assertTrue(matches_watch(hit, set(), ["corecivic"]))

    def test_no_filter_passes_all(self):
        hit = parse_efts_hits(SAMPLE_UNRELATED, "turnkey")[0]
        self.assertTrue(matches_watch(hit, set(), []))

    def test_filter_excludes_unwatched(self):
        hits = parse_efts_hits(SAMPLE_UNRELATED, "turnkey")
        self.assertEqual(filter_hits(hits, {"1070985"}, ["CoreCivic"]), [])


class EdgarDedupeTests(unittest.TestCase):
    def test_dedupe_excludes_seen_and_batch_dupes(self):
        hits = parse_efts_hits(SAMPLE_CXW, "turnkey") * 2  # same id twice
        new = dedupe_new(hits, seen_ids=set())
        self.assertEqual(len(new), 1)
        seen = {"0001070985-26-000045:doc.htm"}
        self.assertEqual(dedupe_new(hits, seen_ids=seen), [])


class EdgarRunLifecycleTests(unittest.TestCase):
    def test_first_run_then_diff(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmpdir = Path(tmp)
            cfg = tmpdir / "edgar-fulltext.yaml"
            cfg.write_text(CONFIG_YAML, encoding="utf-8")
            today = dt.date(2026, 7, 7)

            with mock.patch(
                "scripts.intel.monitors.edgar_fulltext.report_dir",
                return_value=tmpdir,
            ):
                # Run 1 — first run stores baseline, alerts suppressed.
                r1 = run(cfg, today, offline_payloads={"turnkey": SAMPLE_CXW})
                self.assertTrue(r1["first_run"])
                self.assertEqual(r1["alerts"], 0)
                self.assertTrue(r1["report_path"].is_file())

                # Run 2 — same payload, nothing new.
                r2 = run(cfg, today, offline_payloads={"turnkey": SAMPLE_CXW})
                self.assertFalse(r2["first_run"])
                self.assertEqual(r2["new_hits"], [])

                # Run 3 — a new filing appears.
                new_payload = {
                    "hits": {
                        "hits": [
                            {
                                "_id": "0001070985-26-000099:doc.htm",
                                "_source": {
                                    "ciks": ["0001070985"],
                                    "display_names": ["CoreCivic, Inc. (CXW)"],
                                    "file_date": "2026-07-07",
                                    "form": "8-K",
                                    "root_forms": ["8-K"],
                                },
                            }
                        ]
                    }
                }
                r3 = run(cfg, today, offline_payloads={"turnkey": new_payload})
                self.assertEqual(len(r3["new_hits"]), 1)
                self.assertEqual(r3["new_hits"][0]["id"], "0001070985-26-000099:doc.htm")

    def test_network_error_is_captured(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmpdir = Path(tmp)
            cfg = tmpdir / "edgar-fulltext.yaml"
            cfg.write_text(CONFIG_YAML, encoding="utf-8")
            with mock.patch(
                "scripts.intel.monitors.edgar_fulltext.report_dir",
                return_value=tmpdir,
            ), mock.patch(
                "scripts.intel.monitors.edgar_fulltext.search_term",
                side_effect=RuntimeError("boom"),
            ):
                result = run(cfg, dt.date(2026, 7, 7))
                self.assertEqual(result["all_hits"], [])
                self.assertTrue(any("boom" in e for e in result["errors"]))


class ThesisPathTests(unittest.TestCase):
    def test_default_thesis_is_ice_turnkey(self):
        self.assertEqual(paths.DEFAULT_THESIS_ID, "ice-turnkey")

    def test_thesis_config_override(self):
        p = paths.thesis_config("edgar-fulltext.yaml", thesis_id="gov-asset-rerate")
        self.assertTrue(str(p).endswith("config/theses/gov-asset-rerate/edgar-fulltext.yaml"))

    def test_thesis_config_default(self):
        p = paths.thesis_config("jobs.yaml")
        self.assertIn("config/theses/", str(p))
        self.assertTrue(str(p).endswith("jobs.yaml"))


if __name__ == "__main__":
    unittest.main()
