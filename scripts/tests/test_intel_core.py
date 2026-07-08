"""Staleness metric + HTTP retry unit tests."""

import datetime as dt
import io
import unittest
import urllib.error
from unittest import mock

from scripts.intel.core import http
from scripts.intel.core.staleness import staleness_metrics


class StalenessTests(unittest.TestCase):
    def test_stale_publish(self):
        metrics = staleness_metrics("2026-04-09", dt.date(2026, 7, 4), 14)
        self.assertEqual(metrics["status"], "stale")
        self.assertEqual(metrics["missed_cycles"], 5)


class _FakeResp(io.BytesIO):
    def __enter__(self):
        return self

    def __exit__(self, *exc):
        self.close()
        return False


def _http_error(code):
    return urllib.error.HTTPError(url="http://x", code=code, msg="err", hdrs=None, fp=None)


class HttpRetryTests(unittest.TestCase):
    def test_retries_5xx_then_succeeds(self):
        calls = []

        def side_effect(req, timeout):  # noqa: ANN001
            calls.append(1)
            if len(calls) < 3:
                raise _http_error(500)
            return _FakeResp(b'{"ok": true}')

        with mock.patch("urllib.request.urlopen", side_effect=side_effect), mock.patch(
            "scripts.intel.core.http.time.sleep"
        ) as sleep:
            out = http.fetch_json("http://x", retries=2)
        self.assertEqual(out, {"ok": True})
        self.assertEqual(len(calls), 3)  # 1 + 2 retries
        self.assertEqual(sleep.call_count, 2)

    def test_gives_up_after_retries(self):
        with mock.patch("urllib.request.urlopen", side_effect=lambda req, timeout: (_ for _ in ()).throw(_http_error(503))), mock.patch(
            "scripts.intel.core.http.time.sleep"
        ):
            with self.assertRaises(urllib.error.HTTPError):
                http.fetch_json("http://x", retries=2)

    def test_no_retry_on_404(self):
        calls = []

        def side_effect(req, timeout):  # noqa: ANN001
            calls.append(1)
            raise _http_error(404)

        with mock.patch("urllib.request.urlopen", side_effect=side_effect), mock.patch(
            "scripts.intel.core.http.time.sleep"
        ):
            with self.assertRaises(urllib.error.HTTPError):
                http.fetch_json("http://x", retries=2)
        self.assertEqual(len(calls), 1)  # no retries for non-retryable status

    def test_retries_transient_urlerror(self):
        calls = []

        def side_effect(req, timeout):  # noqa: ANN001
            calls.append(1)
            if len(calls) < 2:
                raise urllib.error.URLError("connection reset")
            return _FakeResp(b'{"ok": 1}')

        with mock.patch("urllib.request.urlopen", side_effect=side_effect), mock.patch(
            "scripts.intel.core.http.time.sleep"
        ):
            out = http.fetch_json("http://x", retries=2)
        self.assertEqual(out, {"ok": 1})
        self.assertEqual(len(calls), 2)


if __name__ == "__main__":
    unittest.main()
