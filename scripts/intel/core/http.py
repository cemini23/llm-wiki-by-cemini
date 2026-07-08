"""HTTP fetch helpers.

All fetchers retry on transient failures (HTTP 5xx / 429 and network errors)
with exponential backoff. This matters for unattended 24/7 monitors: e.g. the
SEC EFTS endpoint intermittently returns 500 on otherwise-valid queries, and a
single-attempt fetch would drop that lane's query for the whole cycle.
"""

from __future__ import annotations

import json
import time
import urllib.error
import urllib.request
from typing import Any

BROWSER_UA = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
)

# Statuses worth retrying: transient server errors + rate limiting.
RETRYABLE_STATUS = frozenset({429, 500, 502, 503, 504})
DEFAULT_RETRIES = 2
DEFAULT_BACKOFF = 1.0


def request_headers(*, accept: str = "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8") -> dict[str, str]:
    return {
        "User-Agent": BROWSER_UA,
        "Accept": accept,
        "Accept-Language": "en-US,en;q=0.9",
    }


def _sleep_backoff(attempt: int, backoff: float, retry_after: str | None = None) -> None:
    if retry_after:
        try:
            time.sleep(min(float(retry_after), 30.0))
            return
        except (TypeError, ValueError):
            pass
    time.sleep(backoff * (2 ** attempt))


def open_with_retry(
    req: urllib.request.Request,
    *,
    timeout: int,
    retries: int = DEFAULT_RETRIES,
    backoff: float = DEFAULT_BACKOFF,
) -> Any:
    """urlopen with retry on 5xx/429 and transient network errors.

    Returns the response object (a context manager). Raises the final error
    after exhausting retries, or immediately for non-retryable HTTP errors
    (e.g. 400/403/404).
    """
    attempt = 0
    while True:
        try:
            return urllib.request.urlopen(req, timeout=timeout)
        except urllib.error.HTTPError as exc:
            if exc.code in RETRYABLE_STATUS and attempt < retries:
                _sleep_backoff(attempt, backoff, exc.headers.get("Retry-After") if exc.headers else None)
                attempt += 1
                continue
            raise
        except (urllib.error.URLError, TimeoutError) as exc:  # noqa: PERF203
            # URLError wraps DNS/refused/reset/timeout; retry transient ones.
            if attempt < retries:
                _sleep_backoff(attempt, backoff)
                attempt += 1
                continue
            raise


def fetch_text(url: str, *, timeout: int = 60, retries: int = DEFAULT_RETRIES) -> str:
    req = urllib.request.Request(url, headers=request_headers())
    with open_with_retry(req, timeout=timeout, retries=retries) as resp:
        return resp.read().decode("utf-8", errors="replace")


def fetch_bytes(url: str, *, timeout: int = 120, retries: int = DEFAULT_RETRIES) -> bytes:
    req = urllib.request.Request(
        url,
        headers=request_headers(accept="application/octet-stream,*/*;q=0.8"),
    )
    with open_with_retry(req, timeout=timeout, retries=retries) as resp:
        return resp.read()


def fetch_json(
    url: str,
    *,
    method: str = "GET",
    payload: dict[str, Any] | None = None,
    timeout: int = 45,
    user_agent: str = "cemini-intel-monitor/1.0",
    retries: int = DEFAULT_RETRIES,
) -> dict[str, Any]:
    data = None
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "User-Agent": user_agent,
    }
    if payload is not None:
        data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    with open_with_retry(req, timeout=timeout, retries=retries) as resp:
        return json.loads(resp.read().decode("utf-8"))
