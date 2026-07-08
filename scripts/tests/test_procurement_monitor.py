"""Federal procurement (USASpending) watcher — unit + offline lifecycle tests."""

import datetime as dt
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from scripts.intel.monitors.procurement import (
    build_payload,
    dedupe_new,
    is_alertable_award,
    is_detention_ops_noise,
    is_watched_recipient,
    parse_awards,
    partition_alertable,
    run,
)

SAMPLE_RESPONSE = {
    "results": [
        {
            "internal_id": 307253818,
            "generated_internal_id": "CONT_AWD_HSCEMS_1",
            "Award ID": "HSCEMS26F0001",
            "Recipient Name": "FIRST AMERICAN TITLE INSURANCE COMPANY",
            "Awarding Agency": "Department of Homeland Security",
            "Awarding Sub Agency": "Immigration and Customs Enforcement",
            "Award Amount": 1250000.0,
            "Start Date": "2026-06-15",
            "Description": "TITLE AND ESCROW SERVICES - DETENTION REAL PROPERTY",
            "Award Type": "DEFINITIVE CONTRACT",
        }
    ],
    "page_metadata": {"page": 1, "hasNext": False},
}

CONFIG_YAML = """
settings:
  lookback_days: 120
  award_type_codes: [A, B, C, D]
  limit: 50
  alert_on_new: true
  operator_recipients:
    - CoreCivic
    - GEO Group
  diligence_terms:
    - escrow
    - title
    - appraisal
    - real property
    - turnkey
    - purchase
  suppress_description_patterns:
    - comprehensive detention
    - detention and transportation
    - housing criminal aliens
queries:
  - id: title_escrow_dhs
    keywords: [escrow, "title services"]
    agencies: [Department of Homeland Security]
  - id: detention_facility_acquisition
    keywords: ["facility acquisition", turnkey]
    agencies: [Department of Homeland Security]
    require_diligence_terms: true
  - id: first_american_vendor
    recipient: "First American"
watch_recipients:
  - First American
"""

CAL_CITY_OPS_AWARD = {
    "id": "CONT_AWD_70CDCR25FR0000122",
    "query": "detention_facility_acquisition",
    "award_id": "70CDCR25FR0000122",
    "recipient": "CORECIVIC, INC.",
    "agency": "Department of Homeland Security",
    "sub_agency": "U.S. Immigration and Customs Enforcement",
    "amount": 94720144.0,
    "start_date": "2025-09-01",
    "description": (
        "THE PURPOSE OF THIS TASK ORDER IS FOR COMPREHENSIVE DETENTION AND "
        "TRANSPORTATION SERVICES FOR HOUSING CRIMINAL ALIENS AT CALIFORNIA CITY "
        "DETENTION CENTER IN CALIFORNIA CITY, CA."
    ),
    "award_type": "DELIVERY ORDER",
}


class PayloadTests(unittest.TestCase):
    def test_build_payload_keywords_and_agency(self):
        query = {"id": "q", "keywords": ["escrow"], "agencies": ["Department of Homeland Security"]}
        body = build_payload(query, startdt="2026-03-01", enddt="2026-07-07", settings={"limit": 50})
        self.assertEqual(body["filters"]["keywords"], ["escrow"])
        self.assertEqual(
            body["filters"]["agencies"],
            [{"type": "awarding", "tier": "toptier", "name": "Department of Homeland Security"}],
        )
        self.assertEqual(body["filters"]["time_period"], [{"start_date": "2026-03-01", "end_date": "2026-07-07"}])
        self.assertEqual(body["limit"], 50)
        self.assertEqual(body["filters"]["award_type_codes"], ["A", "B", "C", "D"])

    def test_build_payload_recipient(self):
        body = build_payload({"id": "q", "recipient": "First American"}, startdt="a", enddt="b", settings={})
        self.assertEqual(body["filters"]["recipient_search_text"], ["First American"])
        self.assertNotIn("keywords", body["filters"])


class ParseTests(unittest.TestCase):
    def test_parse_awards(self):
        awards = parse_awards(SAMPLE_RESPONSE, "title_escrow_dhs")
        self.assertEqual(len(awards), 1)
        a = awards[0]
        self.assertEqual(a["id"], "CONT_AWD_HSCEMS_1")
        self.assertEqual(a["award_id"], "HSCEMS26F0001")
        self.assertEqual(a["amount"], 1250000.0)
        self.assertEqual(a["query"], "title_escrow_dhs")

    def test_parse_empty(self):
        self.assertEqual(parse_awards({}, "q"), [])

    def test_uid_fallback_to_award_id(self):
        resp = {"results": [{"Award ID": "X1", "Recipient Name": "ACME"}]}
        self.assertEqual(parse_awards(resp, "q")[0]["id"], "X1")


class WatchTests(unittest.TestCase):
    def test_is_watched_recipient(self):
        award = parse_awards(SAMPLE_RESPONSE, "q")[0]
        self.assertTrue(is_watched_recipient(award, ["First American"]))
        self.assertFalse(is_watched_recipient(award, ["CBRE"]))
        self.assertFalse(is_watched_recipient(award, []))


class AlertFilterTests(unittest.TestCase):
    def setUp(self):
        import yaml

        self.config = yaml.safe_load(CONFIG_YAML)
        self.queries = self.config["queries"]
        self.queries_by_id = {q["id"]: q for q in self.queries}

    def test_suppresses_cal_city_detention_ops_task_order(self):
        self.assertTrue(is_detention_ops_noise(CAL_CITY_OPS_AWARD, self.config["settings"]["suppress_description_patterns"]))
        self.assertFalse(is_alertable_award(CAL_CITY_OPS_AWARD, self.config, self.queries_by_id))

    def test_allows_first_american_escrow(self):
        award = parse_awards(SAMPLE_RESPONSE, "title_escrow_dhs")[0]
        self.assertTrue(is_alertable_award(award, self.config, self.queries_by_id))

    def test_operator_requires_diligence_terms(self):
        geo_ops = {
            **CAL_CITY_OPS_AWARD,
            "description": "DETENTION CENTER OPERATIONS",
            "recipient": "THE GEO GROUP, INC.",
        }
        self.assertFalse(is_alertable_award(geo_ops, self.config, self.queries_by_id))
        geo_purchase = {**geo_ops, "description": "REAL PROPERTY ACQUISITION AND TURNKEY FACILITY PURCHASE"}
        self.assertTrue(is_alertable_award(geo_purchase, self.config, self.queries_by_id))

    def test_partition_alertable(self):
        escrow = parse_awards(SAMPLE_RESPONSE, "title_escrow_dhs")[0]
        alertable, suppressed = partition_alertable([escrow, CAL_CITY_OPS_AWARD], self.config, self.queries)
        self.assertEqual(len(alertable), 1)
        self.assertEqual(alertable[0]["award_id"], "HSCEMS26F0001")
        self.assertEqual(len(suppressed), 1)
        self.assertEqual(suppressed[0]["award_id"], "70CDCR25FR0000122")


class DedupeTests(unittest.TestCase):
    def test_dedupe_excludes_seen_and_batch_dupes(self):
        awards = parse_awards(SAMPLE_RESPONSE, "q") * 2
        self.assertEqual(len(dedupe_new(awards, set())), 1)
        self.assertEqual(dedupe_new(awards, {"CONT_AWD_HSCEMS_1"}), [])


class RunLifecycleTests(unittest.TestCase):
    def test_first_run_then_diff(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmpdir = Path(tmp)
            cfg = tmpdir / "usaspending.yaml"
            cfg.write_text(CONFIG_YAML, encoding="utf-8")
            today = dt.date(2026, 7, 7)
            payloads = {"title_escrow_dhs": SAMPLE_RESPONSE, "first_american_vendor": {}}

            with mock.patch(
                "scripts.intel.monitors.procurement.report_dir", return_value=tmpdir
            ):
                r1 = run(cfg, today, offline_payloads=payloads)
                self.assertTrue(r1["first_run"])
                self.assertEqual(r1["alerts"], 0)
                self.assertTrue(r1["report_path"].is_file())

                r2 = run(cfg, today, offline_payloads=payloads)
                self.assertFalse(r2["first_run"])
                self.assertEqual(r2["new_awards"], [])

                new_payload = {
                    "title_escrow_dhs": {
                        "results": [
                            {
                                "generated_internal_id": "CONT_AWD_NEW_2",
                                "Award ID": "HSCEMS26F0099",
                                "Recipient Name": "FIRST AMERICAN TITLE",
                                "Awarding Agency": "Department of Homeland Security",
                                "Award Amount": 500000.0,
                                "Start Date": "2026-07-01",
                                "Description": "ESCROW",
                                "Award Type": "DEFINITIVE CONTRACT",
                            }
                        ]
                    }
                }
                r3 = run(cfg, today, offline_payloads=new_payload)
                self.assertEqual(len(r3["new_awards"]), 1)
                self.assertEqual(r3["new_awards"][0]["id"], "CONT_AWD_NEW_2")

    def test_suppressed_ops_award_does_not_alert(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmpdir = Path(tmp)
            cfg = tmpdir / "usaspending.yaml"
            cfg.write_text(CONFIG_YAML, encoding="utf-8")
            today = dt.date(2026, 7, 8)
            baseline = {"title_escrow_dhs": SAMPLE_RESPONSE, "first_american_vendor": {}, "detention_facility_acquisition": {}}
            with mock.patch("scripts.intel.monitors.procurement.report_dir", return_value=tmpdir):
                run(cfg, today, offline_payloads=baseline)
                noisy = {
                    "detention_facility_acquisition": {
                        "results": [
                            {
                                "generated_internal_id": CAL_CITY_OPS_AWARD["id"],
                                "Award ID": CAL_CITY_OPS_AWARD["award_id"],
                                "Recipient Name": CAL_CITY_OPS_AWARD["recipient"],
                                "Awarding Agency": CAL_CITY_OPS_AWARD["agency"],
                                "Awarding Sub Agency": CAL_CITY_OPS_AWARD["sub_agency"],
                                "Award Amount": CAL_CITY_OPS_AWARD["amount"],
                                "Start Date": CAL_CITY_OPS_AWARD["start_date"],
                                "Description": CAL_CITY_OPS_AWARD["description"],
                                "Award Type": CAL_CITY_OPS_AWARD["award_type"],
                            }
                        ]
                    }
                }
                with mock.patch("scripts.intel.monitors.procurement.send_alert") as send_alert:
                    result = run(cfg, today, notify=True, offline_payloads=noisy)
                send_alert.assert_not_called()
                self.assertEqual(result["new_awards"], [])
                self.assertEqual(len(result["suppressed_awards"]), 1)

    def test_network_error_is_captured(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmpdir = Path(tmp)
            cfg = tmpdir / "usaspending.yaml"
            cfg.write_text(CONFIG_YAML, encoding="utf-8")
            with mock.patch(
                "scripts.intel.monitors.procurement.report_dir", return_value=tmpdir
            ), mock.patch(
                "scripts.intel.monitors.procurement.search_query",
                side_effect=RuntimeError("boom"),
            ):
                result = run(cfg, dt.date(2026, 7, 7))
                self.assertEqual(result["all_awards"], [])
                self.assertTrue(any("boom" in e for e in result["errors"]))


if __name__ == "__main__":
    unittest.main()
