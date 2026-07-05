"""Staleness metric unit tests."""

import datetime as dt
import unittest

from scripts.intel.core.staleness import staleness_metrics


class StalenessTests(unittest.TestCase):
    def test_stale_publish(self):
        metrics = staleness_metrics("2026-04-09", dt.date(2026, 7, 4), 14)
        self.assertEqual(metrics["status"], "stale")
        self.assertEqual(metrics["missed_cycles"], 5)


if __name__ == "__main__":
    unittest.main()
