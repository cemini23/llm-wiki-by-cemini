"""Fetch multi-platform WC R16 prices from TicketWave comparison pages."""

from __future__ import annotations

import re
import urllib.error
import urllib.request
from dataclasses import dataclass
from typing import Optional

USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
)
SNAPSHOT_RE = re.compile(
    r"Current prices[^<]*</strong><ul>(.*?)</ul>",
    re.IGNORECASE | re.DOTALL,
)
LINE_RE = re.compile(
    r"<li>([^:]+): from \$(\d+(?:,\d+)*) USD</li>",
    re.IGNORECASE,
)
TITLE_MIN_RE = re.compile(r"<title>[^$]*from \$(\d+(?:,\d+)*)", re.IGNORECASE)
TREND_RE = re.compile(
    r"Price trend:\s*<strong>([^<]+)</strong>",
    re.IGNORECASE,
)
UPDATED_RE = re.compile(r"(\d{2}\.\d{2}\.\d{4}\s+\d{2}:\d{2})", re.IGNORECASE)


@dataclass(frozen=True)
class PlatformQuote:
    platform: str
    price_usd: float
    source: str
    url: str


@dataclass(frozen=True)
class EventScan:
    event_id: str
    label: str
    quotes: list[PlatformQuote]
    trend: Optional[str]
    updated_at: Optional[str]
    page_url: str
    error: Optional[str] = None

    @property
    def min_quote(self) -> Optional[PlatformQuote]:
        if not self.quotes:
            return None
        return min(self.quotes, key=lambda q: q.price_usd)


def _fetch_html(url: str, timeout: int = 30) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read().decode("utf-8", "replace")


def _parse_price(raw: str) -> float:
    return float(raw.replace(",", ""))


def scan_ticketwave(
    *,
    event_id: str,
    label: str,
    slug: str,
) -> EventScan:
    page_url = f"https://ticketwave.io/events/{slug}/"
    try:
        html = _fetch_html(page_url)
    except (urllib.error.URLError, TimeoutError) as exc:
        return EventScan(
            event_id=event_id,
            label=label,
            quotes=[],
            trend=None,
            updated_at=None,
            page_url=page_url,
            error=str(exc),
        )

    quotes: list[PlatformQuote] = []
    snap = SNAPSHOT_RE.search(html)
    if snap:
        for platform, price_raw in LINE_RE.findall(snap.group(1)):
            quotes.append(
                PlatformQuote(
                    platform=platform.strip(),
                    price_usd=_parse_price(price_raw),
                    source="ticketwave",
                    url=page_url,
                )
            )

    if not quotes:
        title_min = TITLE_MIN_RE.search(html)
        if title_min:
            quotes.append(
                PlatformQuote(
                    platform="TicketWave (page min)",
                    price_usd=_parse_price(title_min.group(1)),
                    source="ticketwave",
                    url=page_url,
                )
            )

    trend_match = TREND_RE.search(html)
    updated_match = UPDATED_RE.search(html)
    return EventScan(
        event_id=event_id,
        label=label,
        quotes=quotes,
        trend=trend_match.group(1).strip() if trend_match else None,
        updated_at=updated_match.group(1) if updated_match else None,
        page_url=page_url,
    )
