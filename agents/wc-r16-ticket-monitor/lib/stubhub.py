"""Optional direct StubHub listing scrape via Playwright (bypasses WAF)."""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Optional

from lib.ticketwave import PlatformQuote

RAW_PRICE_RE = re.compile(r'"rawPrice":([0-9.]+)')


@dataclass(frozen=True)
class StubHubScan:
    event_id: str
    label: str
    url: str
    min_price_usd: Optional[float]
    listing_count: int
    error: Optional[str] = None


def scan_stubhub_playwright(
    *,
    event_id: str,
    label: str,
    url: str,
    timeout_ms: int = 45000,
) -> StubHubScan:
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        return StubHubScan(
            event_id=event_id,
            label=label,
            url=url,
            min_price_usd=None,
            listing_count=0,
            error="playwright not installed",
        )

    html = ""
    error: Optional[str] = None
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page(user_agent=(
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            ))
            page.goto(url, wait_until="domcontentloaded", timeout=timeout_ms)
            page.wait_for_timeout(3000)
            html = page.content()
            browser.close()
    except Exception as exc:  # noqa: BLE001 — surface scrape failures
        error = str(exc)

    prices = [float(x) for x in RAW_PRICE_RE.findall(html)]
    return StubHubScan(
        event_id=event_id,
        label=label,
        url=url,
        min_price_usd=min(prices) if prices else None,
        listing_count=len(prices),
        error=error,
    )


def stubhub_quote(scan: StubHubScan) -> Optional[PlatformQuote]:
    if scan.min_price_usd is None:
        return None
    return PlatformQuote(
        platform="StubHub (direct)",
        price_usd=scan.min_price_usd,
        source="stubhub",
        url=scan.url,
    )
