"""FIFA official resale prices via The Great Reviewer WC tracker public API."""

from __future__ import annotations

import json
import urllib.error
import urllib.request
from dataclasses import dataclass
from typing import Optional

from lib.ticketwave import PlatformQuote

DASHBOARD_URL = "https://thegreatreviewer.com/api/seat-alerts/get-dashboard.php"
MATCH_NUMBERS_URL = "https://thegreatreviewer.com/api/seat-alerts/match-numbers.json"
TRACKER_BASE = "https://thegreatreviewer.com/wc-tracker/"
USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
)


@dataclass(frozen=True)
class GreatReviewerMatch:
    match_number: int
    match_id: str
    label: str
    venue: str
    match_date: str
    min_price_usd: float
    seat_count: int
    scanned_at: Optional[str]
    cheapest_category: Optional[str]
    buy_url: str
    tracker_url: str
    error: Optional[str] = None


@dataclass
class GreatReviewerSnapshot:
    matches_by_number: dict[int, GreatReviewerMatch]
    generated_at: Optional[str]
    error: Optional[str] = None


def _get_json(url: str, timeout: int = 30) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8"))


def fetch_snapshot(*, match_numbers: set[int]) -> GreatReviewerSnapshot:
    try:
        dashboard = _get_json(DASHBOARD_URL)
        id_to_number_raw = _get_json(MATCH_NUMBERS_URL)
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
        return GreatReviewerSnapshot(matches_by_number={}, generated_at=None, error=str(exc))

    id_to_number: dict[str, int] = {
        str(k): int(v) for k, v in id_to_number_raw.items()
    }
    wanted = set(match_numbers)

    matches_by_number: dict[int, GreatReviewerMatch] = {}
    for row in dashboard.get("matches", []):
        match_id = str(row.get("matchId", ""))
        number = id_to_number.get(match_id)
        if number is None or number not in wanted:
            continue

        seats = row.get("seats") or []
        cheapest = seats[0] if seats else {}
        matches_by_number[number] = GreatReviewerMatch(
            match_number=number,
            match_id=match_id,
            label=str(row.get("matchLabel", f"Match {number}")),
            venue=str(row.get("venue", "")),
            match_date=str(row.get("matchDate", "")),
            min_price_usd=float(row.get("minPrice") or 0),
            seat_count=int(row.get("seatCount") or 0),
            scanned_at=str(row.get("scannedAt")) if row.get("scannedAt") else None,
            cheapest_category=str(cheapest.get("category")) if cheapest.get("category") else None,
            buy_url=str(cheapest.get("buyUrl") or "https://www.fifa.com/tickets"),
            tracker_url=TRACKER_BASE,
        )

    return GreatReviewerSnapshot(
        matches_by_number=matches_by_number,
        generated_at=dashboard.get("generatedAt"),
    )


def great_reviewer_quote(gr: GreatReviewerMatch) -> Optional[PlatformQuote]:
    if gr.error or gr.min_price_usd <= 0:
        return None
    detail = gr.cheapest_category or "FIFA official resale"
    return PlatformQuote(
        platform=f"FIFA Official — {detail}",
        price_usd=gr.min_price_usd,
        source="great_reviewer",
        url=gr.buy_url,
    )
