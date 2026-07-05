import datetime as dt
import unittest
from pathlib import Path

from scripts.intel.monitors.detention_stats import (
    discover_latest_xlsx_url,
    implied_adp,
    match_targets,
    parse_filename_date,
    staleness_metrics,
)


SAMPLE_HTML = """
<a href="/doclib/detention/FY25_detentionStats09242025.xlsx">FY25</a>
<a href="/doclib/detention/FY26_detentionStats_04092026.xlsx">FY26</a>
"""


class IceDetentionStatsMonitorTests(unittest.TestCase):
    def test_discover_latest_xlsx_url_prefers_fy26(self):
        url = discover_latest_xlsx_url(SAMPLE_HTML)
        self.assertIn("FY26_detentionStats_04092026.xlsx", url)

    def test_parse_filename_date(self):
        self.assertEqual(
            parse_filename_date("https://www.ice.gov/doclib/detention/FY26_detentionStats_04092026.xlsx"),
            "2026-04-09",
        )

    def test_implied_adp(self):
        record = {
            "Male Crim": "100",
            "Male Non-Crim": "200",
            "Female Crim": "10",
            "Female Non-Crim": "5",
            "Guaranteed Minimum": "250",
        }
        self.assertEqual(implied_adp(record), 315.0)

    def test_match_targets(self):
        config = {
            "targets": [
                {"id": "otay", "label": "Otay", "match": "OTAY MESA", "thesis_lane": "test"},
                {"id": "missing", "label": "Missing", "match": "NO SUCH FACILITY", "thesis_lane": "test"},
            ]
        }
        facilities = [
            {
                "Name": "OTAY MESA DETENTION CENTER",
                "Male Crim": "200",
                "Male Non-Crim": "900",
                "Female Crim": "10",
                "Female Non-Crim": "20",
                "Guaranteed Minimum": "750",
                "FY26 ALOS": "60",
                "Type Detailed": "CDF",
                "State": "CA",
            }
        ]
        rows = match_targets(config, facilities)
        self.assertTrue(rows[0]["found"])
        self.assertAlmostEqual(rows[0]["implied_adp"], 1130.0)
        self.assertAlmostEqual(rows[0]["delta_vs_min"], 380.0)
        self.assertFalse(rows[1]["found"])

    def test_staleness_metrics(self):
        today = dt.date(2026, 7, 4)
        metrics = staleness_metrics("2026-04-09", today, 14)
        self.assertEqual(metrics["days_since_publish"], 86)
        self.assertEqual(metrics["status"], "stale")
        self.assertEqual(metrics["missed_cycles"], 5)

    def test_parse_live_workbook_if_present(self):
        archive = Path("/tmp/FY26_detentionStats_04092026.xlsx")
        if not archive.is_file():
            self.skipTest("live workbook fixture not present")
        import zipfile

        from scripts.intel.monitors.detention_stats import parse_facilities, parse_sheet_rows, sheet_path_by_name

        with zipfile.ZipFile(archive) as zf:
            sheet = sheet_path_by_name(zf, "Facilities")
            self.assertIsNotNone(sheet)
            meta, facilities = parse_facilities(parse_sheet_rows(zf, sheet))
        self.assertTrue(meta.get("pull_date"))
        self.assertGreater(len(facilities), 50)


if __name__ == "__main__":
    unittest.main()
