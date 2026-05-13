"""Unit tests for ``conductor.reviewer.cost_telemetry``."""

from __future__ import annotations

import json
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path

from conductor.reviewer.cost_telemetry import TelemetryWriter, record
from conductor.reviewer.trigger_policy import Bucket


class TelemetryWriterTests(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.path = Path(self._tmp.name) / "telemetry.ndjson"

    def tearDown(self) -> None:
        self._tmp.cleanup()

    def _read_log(self) -> list:
        with self.path.open("r", encoding="utf-8") as fh:
            return [json.loads(line) for line in fh if line.strip()]

    def test_single_record_round_trips(self) -> None:
        fixed_ts = datetime(2026, 5, 13, 12, 0, 0, tzinfo=timezone.utc)
        with TelemetryWriter(path=self.path, buffer_size=1) as writer:
            writer.record(
                "place_order", Bucket.ALWAYS_REVIEW,
                input_tokens=100, output_tokens=50, ts=fixed_ts,
            )
        entries = self._read_log()
        self.assertEqual(len(entries), 1)
        entry = entries[0]
        self.assertEqual(entry["tool"], "place_order")
        self.assertEqual(entry["bucket"], "always-review")
        self.assertEqual(entry["in_tokens"], 100)
        self.assertEqual(entry["out_tokens"], 50)
        self.assertEqual(entry["ts"], fixed_ts.isoformat())

    def test_buffer_size_delays_write(self) -> None:
        writer = TelemetryWriter(path=self.path, buffer_size=3)
        writer.record("t1", Bucket.ALWAYS_REVIEW, 10, 5)
        writer.record("t2", Bucket.ALWAYS_REVIEW, 10, 5)
        # Buffer below threshold -> nothing on disk yet.
        self.assertFalse(self.path.exists())
        writer.record("t3", Bucket.ALWAYS_REVIEW, 10, 5)
        # Threshold hit -> auto-flushed.
        entries = self._read_log()
        self.assertEqual(len(entries), 3)
        self.assertEqual([e["tool"] for e in entries], ["t1", "t2", "t3"])

    def test_explicit_flush_writes_buffer(self) -> None:
        writer = TelemetryWriter(path=self.path, buffer_size=100)
        writer.record("t", Bucket.ALWAYS_REVIEW, 10, 5)
        self.assertFalse(self.path.exists())
        flushed = writer.flush()
        self.assertEqual(flushed, 1)
        self.assertEqual(len(self._read_log()), 1)

    def test_flush_empty_buffer_returns_zero(self) -> None:
        writer = TelemetryWriter(path=self.path, buffer_size=100)
        self.assertEqual(writer.flush(), 0)
        self.assertFalse(self.path.exists())

    def test_context_manager_flushes_on_exit(self) -> None:
        with TelemetryWriter(path=self.path, buffer_size=100) as writer:
            writer.record("t", Bucket.ALWAYS_REVIEW, 10, 5)
        # __exit__ flushed.
        self.assertEqual(len(self._read_log()), 1)

    def test_append_does_not_overwrite_existing(self) -> None:
        with TelemetryWriter(path=self.path, buffer_size=1) as w:
            w.record("t1", Bucket.ALWAYS_REVIEW, 10, 5)
        with TelemetryWriter(path=self.path, buffer_size=1) as w:
            w.record("t2", Bucket.ALWAYS_REVIEW, 20, 10)
        entries = self._read_log()
        self.assertEqual(len(entries), 2)
        self.assertEqual(entries[0]["tool"], "t1")
        self.assertEqual(entries[1]["tool"], "t2")

    def test_creates_parent_directories(self) -> None:
        nested = Path(self._tmp.name) / "a" / "b" / "c" / "log.ndjson"
        with TelemetryWriter(path=nested, buffer_size=1) as writer:
            writer.record("t", Bucket.ALWAYS_REVIEW, 1, 1)
        self.assertTrue(nested.exists())

    def test_record_function_convenience(self) -> None:
        record(
            "place_order",
            Bucket.ALWAYS_REVIEW,
            input_tokens=50,
            output_tokens=25,
            path=self.path,
        )
        entries = self._read_log()
        self.assertEqual(len(entries), 1)
        self.assertEqual(entries[0]["tool"], "place_order")
        self.assertEqual(entries[0]["in_tokens"], 50)
        self.assertEqual(entries[0]["out_tokens"], 25)

    def test_bucket_value_serialized_as_string(self) -> None:
        with TelemetryWriter(path=self.path, buffer_size=1) as writer:
            writer.record("t", Bucket.REVIEW_ON_UNCERTAINTY, 1, 1)
        entries = self._read_log()
        self.assertEqual(entries[0]["bucket"], "review-on-uncertainty")

    def test_each_record_is_single_line_compact_json(self) -> None:
        """NDJSON invariant: each record is exactly one line, no whitespace runs."""
        with TelemetryWriter(path=self.path, buffer_size=10) as writer:
            for i in range(5):
                writer.record(f"t{i}", Bucket.ALWAYS_REVIEW, i, i * 2)
        raw_lines = self.path.read_text(encoding="utf-8").splitlines()
        self.assertEqual(len(raw_lines), 5)
        for line in raw_lines:
            # Compact separators -> no `", "` or `": "` substrings.
            self.assertNotIn(", ", line)
            self.assertNotIn(": ", line)

    def test_buffer_size_below_one_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "buffer_size must be >= 1"):
            TelemetryWriter(path=self.path, buffer_size=0)


if __name__ == "__main__":
    unittest.main()
