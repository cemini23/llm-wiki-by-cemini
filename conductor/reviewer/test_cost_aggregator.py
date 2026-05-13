"""Unit tests for ``conductor.reviewer.cost_aggregator``."""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path
from typing import List

from conductor.reviewer.cost_aggregator import (
    DEFAULT_PRICE_INPUT_PER_TOKEN_USD,
    DEFAULT_PRICE_OUTPUT_PER_TOKEN_USD,
    aggregate,
    main,
)


def _write_log(path: Path, records: List[dict]) -> None:
    with path.open("w", encoding="utf-8") as fh:
        for entry in records:
            fh.write(json.dumps(entry) + "\n")


class AggregateHappyPathTests(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.path = Path(self._tmp.name) / "log.ndjson"

    def tearDown(self) -> None:
        self._tmp.cleanup()

    def test_missing_log_yields_zero_report(self) -> None:
        missing = Path(self._tmp.name) / "does_not_exist.ndjson"
        report = aggregate(missing)
        self.assertEqual(report["total"]["count"], 0)
        self.assertEqual(report["by_tool"], {})
        self.assertEqual(report["monthly_estimate_usd"], 0.0)
        self.assertIsNone(report["period_start"])
        self.assertIsNone(report["period_end"])

    def test_empty_log_yields_zero_report(self) -> None:
        self.path.write_text("")
        report = aggregate(self.path)
        self.assertEqual(report["total"]["count"], 0)
        self.assertEqual(report["by_tool"], {})

    def test_single_record_aggregates(self) -> None:
        _write_log(self.path, [
            {
                "ts": "2026-05-13T12:00:00+00:00",
                "tool": "place_order",
                "bucket": "always-review",
                "in_tokens": 1000,
                "out_tokens": 500,
            },
        ])
        report = aggregate(self.path)
        self.assertEqual(report["total"]["count"], 1)
        self.assertEqual(report["total"]["in_tokens"], 1000)
        self.assertEqual(report["total"]["out_tokens"], 500)
        expected_cost = (
            1000 * DEFAULT_PRICE_INPUT_PER_TOKEN_USD
            + 500 * DEFAULT_PRICE_OUTPUT_PER_TOKEN_USD
        )
        self.assertAlmostEqual(report["total"]["cost_usd"], expected_cost, places=6)

    def test_multiple_tools_grouped(self) -> None:
        _write_log(self.path, [
            {"ts": "2026-05-13T12:00:00+00:00", "tool": "place_order",
             "bucket": "always-review", "in_tokens": 100, "out_tokens": 50},
            {"ts": "2026-05-13T12:01:00+00:00", "tool": "place_order",
             "bucket": "always-review", "in_tokens": 200, "out_tokens": 100},
            {"ts": "2026-05-13T12:02:00+00:00", "tool": "submit_research_query",
             "bucket": "review-on-uncertainty", "in_tokens": 50, "out_tokens": 25},
        ])
        report = aggregate(self.path)
        self.assertEqual(report["by_tool"]["place_order"]["count"], 2)
        self.assertEqual(report["by_tool"]["place_order"]["in_tokens"], 300)
        self.assertEqual(report["by_tool"]["place_order"]["out_tokens"], 150)
        self.assertEqual(
            report["by_tool"]["submit_research_query"]["count"], 1,
        )
        self.assertEqual(report["total"]["count"], 3)

    def test_period_bounds_captured(self) -> None:
        _write_log(self.path, [
            {"ts": "2026-05-13T08:00:00+00:00", "tool": "t",
             "bucket": "always-review", "in_tokens": 10, "out_tokens": 5},
            {"ts": "2026-05-13T12:00:00+00:00", "tool": "t",
             "bucket": "always-review", "in_tokens": 10, "out_tokens": 5},
            {"ts": "2026-05-13T18:00:00+00:00", "tool": "t",
             "bucket": "always-review", "in_tokens": 10, "out_tokens": 5},
        ])
        report = aggregate(self.path)
        self.assertEqual(report["period_start"], "2026-05-13T08:00:00+00:00")
        self.assertEqual(report["period_end"], "2026-05-13T18:00:00+00:00")

    def test_monthly_extrapolation_scales_observed_cost(self) -> None:
        # Two records exactly one hour apart -> 1 hour observed window.
        # 30-day extrapolation -> 720x scaling.
        _write_log(self.path, [
            {"ts": "2026-05-13T12:00:00+00:00", "tool": "t",
             "bucket": "always-review", "in_tokens": 100, "out_tokens": 50},
            {"ts": "2026-05-13T13:00:00+00:00", "tool": "t",
             "bucket": "always-review", "in_tokens": 100, "out_tokens": 50},
        ])
        report = aggregate(self.path)
        observed_cost = report["total"]["cost_usd"]
        # 720x window -> within 1% of 720 * observed (float rounding).
        expected_monthly = observed_cost * 24 * 30
        self.assertAlmostEqual(
            report["monthly_estimate_usd"], expected_monthly, places=2,
        )

    def test_extrapolation_floor_prevents_inflation_on_zero_duration(self) -> None:
        # All records same timestamp -> duration_days is floored at 1 hour.
        _write_log(self.path, [
            {"ts": "2026-05-13T12:00:00+00:00", "tool": "t",
             "bucket": "always-review", "in_tokens": 100, "out_tokens": 50}
        ] * 5)
        report = aggregate(self.path)
        # With 1-hour-floor, 30-day extrapolation = 720x observed.
        observed_cost = report["total"]["cost_usd"]
        self.assertAlmostEqual(
            report["monthly_estimate_usd"], observed_cost * 720, places=2,
        )

    def test_custom_pricing_overrides_default(self) -> None:
        _write_log(self.path, [
            {"ts": "2026-05-13T12:00:00+00:00", "tool": "t",
             "bucket": "always-review", "in_tokens": 1_000_000, "out_tokens": 0},
        ])
        report = aggregate(self.path, price_input_per_token_usd=1e-6)
        # 1M tokens at $1e-6/token = $1.00.
        self.assertAlmostEqual(report["total"]["cost_usd"], 1.0, places=4)
        # Pricing block reflects override.
        self.assertEqual(report["pricing"]["input_per_token_usd"], 1e-6)

    def test_deterministic_tool_ordering(self) -> None:
        _write_log(self.path, [
            {"ts": "2026-05-13T12:00:00+00:00", "tool": "zebra",
             "bucket": "always-review", "in_tokens": 1, "out_tokens": 1},
            {"ts": "2026-05-13T12:01:00+00:00", "tool": "apple",
             "bucket": "always-review", "in_tokens": 1, "out_tokens": 1},
            {"ts": "2026-05-13T12:02:00+00:00", "tool": "mango",
             "bucket": "always-review", "in_tokens": 1, "out_tokens": 1},
        ])
        report = aggregate(self.path)
        self.assertEqual(list(report["by_tool"].keys()), ["apple", "mango", "zebra"])

    def test_pricing_block_includes_source(self) -> None:
        _write_log(self.path, [
            {"ts": "2026-05-13T12:00:00+00:00", "tool": "t",
             "bucket": "always-review", "in_tokens": 1, "out_tokens": 1},
        ])
        report = aggregate(self.path)
        self.assertIn("source", report["pricing"])
        self.assertIn("DeepSeek-R1", report["pricing"]["source"])

    def test_blank_lines_skipped(self) -> None:
        self.path.write_text(
            '{"ts":"2026-05-13T12:00:00+00:00","tool":"t","bucket":"always-review","in_tokens":1,"out_tokens":1}\n'
            '\n'
            '   \n'
            '{"ts":"2026-05-13T12:01:00+00:00","tool":"t","bucket":"always-review","in_tokens":2,"out_tokens":2}\n',
            encoding="utf-8",
        )
        report = aggregate(self.path)
        self.assertEqual(report["total"]["count"], 2)
        self.assertEqual(report["total"]["in_tokens"], 3)


class AggregateMalformedLogTests(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.path = Path(self._tmp.name) / "log.ndjson"

    def tearDown(self) -> None:
        self._tmp.cleanup()

    def test_malformed_json_line_raises(self) -> None:
        self.path.write_text("this is not json\n", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "malformed telemetry record"):
            aggregate(self.path)

    def test_missing_tool_field_raises(self) -> None:
        _write_log(self.path, [
            {"ts": "2026-05-13T12:00:00+00:00", "in_tokens": 10, "out_tokens": 5},
        ])
        with self.assertRaisesRegex(ValueError, "missing 'tool' string field"):
            aggregate(self.path)


class CLIIntegrationTests(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.log_path = Path(self._tmp.name) / "log.ndjson"
        self.output_path = Path(self._tmp.name) / "report.json"
        _write_log(self.log_path, [
            {"ts": "2026-05-13T12:00:00+00:00", "tool": "place_order",
             "bucket": "always-review", "in_tokens": 100, "out_tokens": 50},
        ])

    def tearDown(self) -> None:
        self._tmp.cleanup()

    def test_cli_writes_output_file(self) -> None:
        rc = main([str(self.log_path), "--output", str(self.output_path)])
        self.assertEqual(rc, 0)
        self.assertTrue(self.output_path.exists())
        report = json.loads(self.output_path.read_text(encoding="utf-8"))
        self.assertEqual(report["total"]["count"], 1)
        self.assertEqual(report["by_tool"]["place_order"]["in_tokens"], 100)

    def test_cli_creates_output_parent_directories(self) -> None:
        nested = Path(self._tmp.name) / "reports" / "daily" / "out.json"
        rc = main([str(self.log_path), "--output", str(nested)])
        self.assertEqual(rc, 0)
        self.assertTrue(nested.exists())


if __name__ == "__main__":
    unittest.main()
