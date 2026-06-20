#!/usr/bin/env python3
"""World Cup 2026 Round of 16 ticket price monitor."""

from __future__ import annotations

import argparse
import json
import logging
import os
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

import yaml

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

from lib.discord import send_discord_embed
from lib.great_reviewer import (
    GreatReviewerMatch,
    GreatReviewerSnapshot,
    fetch_snapshot as fetch_great_reviewer,
    great_reviewer_quote,
)
from lib.state import StateStore
from lib.stubhub import scan_stubhub_playwright, stubhub_quote
from lib.ticketwave import EventScan, PlatformQuote, scan_ticketwave

logger = logging.getLogger("wc_r16_monitor")


def load_dotenv(path: Path) -> None:
    if not path.exists():
        return
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        os.environ.setdefault(key, value)


def load_yaml(path: Path) -> dict[str, Any]:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def scan_event(
    event: dict[str, Any],
    *,
    use_ticketwave: bool,
    use_stubhub: bool,
    gr_match: Optional[GreatReviewerMatch],
) -> tuple[EventScan | None, list[PlatformQuote], Optional[GreatReviewerMatch]]:
    quotes: list[PlatformQuote] = []
    tw_scan: EventScan | None = None

    if gr_match:
        gr_q = great_reviewer_quote(gr_match)
        if gr_q:
            quotes.append(gr_q)

    if use_ticketwave:
        tw_scan = scan_ticketwave(
            event_id=event["id"],
            label=event["label"],
            slug=event["ticketwave_slug"],
        )
        quotes.extend(tw_scan.quotes)
        if tw_scan.error:
            logger.warning("%s ticketwave error: %s", event["id"], tw_scan.error)

    if use_stubhub and event.get("stubhub_url"):
        sh = scan_stubhub_playwright(
            event_id=event["id"],
            label=event["label"],
            url=event["stubhub_url"],
        )
        q = stubhub_quote(sh)
        if q:
            quotes.append(q)
        if sh.error:
            logger.warning("%s stubhub error: %s", event["id"], sh.error)

    return tw_scan, quotes, gr_match


def format_hit_lines(
    event: dict[str, Any],
    hits: list[PlatformQuote],
    tw_scan: EventScan | None,
    gr_match: Optional[GreatReviewerMatch],
) -> str:
    lines = [
        f"**{event['label']}** — Match {event['match']}",
        f"{event['venue']}, {event['city']} · {event['date']}",
        "",
    ]
    for q in sorted(hits, key=lambda x: x.price_usd):
        suffix = ""
        if q.source == "great_reviewer":
            suffix = " · FIFA official"
        lines.append(f"• **{q.platform}**: ${q.price_usd:,.0f} ({q.source}{suffix})")

    lines.append("")
    if gr_match:
        lines.append(
            f"[Great Reviewer tracker]({gr_match.tracker_url}) · "
            f"[Buy on FIFA]({gr_match.buy_url})"
        )
        if gr_match.scanned_at:
            lines.append(f"_FIFA scan: {gr_match.scanned_at} · {gr_match.seat_count:,} seats_")
    if tw_scan and tw_scan.page_url:
        lines.append(f"[TicketWave compare]({tw_scan.page_url})")
    if event.get("stubhub_url"):
        lines.append(f"[StubHub event]({event['stubhub_url']})")
    return "\n".join(lines)


def run_once(
    *,
    config: dict[str, Any],
    events: list[dict[str, Any]],
    webhook_url: str,
    dry_run: bool,
    force_alert: bool,
    print_json: bool,
) -> int:
    threshold = float(
        os.getenv("PRICE_THRESHOLD_USD", config.get("price_threshold_usd", 1500))
    )
    cooldown = float(
        os.getenv("ALERT_COOLDOWN_HOURS", config.get("alert_cooldown_hours", 24))
    )
    drop_realert = float(config.get("price_drop_realert_usd", 50))
    username = config.get("discord_username", "WC R16 Ticket Monitor")
    sources = config.get("sources", {})
    use_ticketwave = sources.get("ticketwave", True)
    use_great_reviewer = sources.get("great_reviewer", True)
    use_stubhub = sources.get("stubhub_direct", False)

    state_path = ROOT / ".local" / "alert_state.json"
    store = StateStore(state_path)

    match_numbers = {int(e["match"]) for e in events}
    gr_snapshot: GreatReviewerSnapshot = GreatReviewerSnapshot({}, None)
    if use_great_reviewer:
        gr_snapshot = fetch_great_reviewer(match_numbers=match_numbers)
        if gr_snapshot.error:
            logger.warning("great reviewer error: %s", gr_snapshot.error)
        else:
            logger.info(
                "great reviewer: %d/%d R16 matches loaded (generated %s)",
                len(gr_snapshot.matches_by_number),
                len(match_numbers),
                gr_snapshot.generated_at,
            )

    all_results: list[dict[str, Any]] = []
    alerts_sent = 0

    def process_event(event: dict[str, Any]) -> dict[str, Any]:
        gr_match = gr_snapshot.matches_by_number.get(int(event["match"]))
        tw_scan, quotes, gr_row = scan_event(
            event,
            use_ticketwave=use_ticketwave,
            use_stubhub=use_stubhub,
            gr_match=gr_match,
        )
        hits = [q for q in quotes if q.price_usd < threshold]
        min_q = min(quotes, key=lambda q: q.price_usd) if quotes else None

        result = {
            "event_id": event["id"],
            "label": event["label"],
            "match": event["match"],
            "date": event["date"],
            "venue": event["venue"],
            "threshold_usd": threshold,
            "quotes": [
                {"platform": q.platform, "price_usd": q.price_usd, "source": q.source}
                for q in sorted(quotes, key=lambda x: x.price_usd)
            ],
            "min_price_usd": min_q.price_usd if min_q else None,
            "hits_under_threshold": len(hits),
            "ticketwave_error": tw_scan.error if tw_scan else None,
            "ticketwave_trend": tw_scan.trend if tw_scan else None,
            "great_reviewer": {
                "min_price_usd": gr_row.min_price_usd if gr_row else None,
                "seat_count": gr_row.seat_count if gr_row else None,
                "scanned_at": gr_row.scanned_at if gr_row else None,
                "category": gr_row.cheapest_category if gr_row else None,
            }
            if gr_row
            else None,
            "_hits": hits,
            "_tw_scan": tw_scan,
            "_gr_match": gr_row,
            "_event": event,
        }
        return result

    # TicketWave fetches run in parallel; Great Reviewer already fetched once above.
    with ThreadPoolExecutor(max_workers=min(8, len(events))) as pool:
        futures = {pool.submit(process_event, event): event for event in events}
        for fut in as_completed(futures):
            all_results.append(fut.result())

    all_results.sort(key=lambda r: int(r["match"]))

    for result in all_results:
        hits = result.pop("_hits")
        tw_scan = result.pop("_tw_scan")
        gr_match = result.pop("_gr_match")
        event = result.pop("_event")

        if not hits:
            continue

        pending: list[PlatformQuote] = []
        for hit in hits:
            if force_alert or store.should_alert(
                event_id=event["id"],
                platform=hit.platform,
                price_usd=hit.price_usd,
                cooldown_hours=cooldown,
                drop_realert_usd=drop_realert,
            ):
                pending.append(hit)

        if not pending:
            continue

        title = f"🎟 WC R16 under ${threshold:,.0f}: {event['label']}"
        body = format_hit_lines(event, pending, tw_scan, gr_match)
        logger.info("ALERT %s — %d platform(s) under threshold", event["id"], len(pending))

        if dry_run:
            print(f"\n--- DRY RUN ALERT ---\n{title}\n{body}\n")
        else:
            ok = send_discord_embed(
                webhook_url=webhook_url,
                username=username,
                title=title,
                description=body,
                color=3066993,
                fields=[
                    {
                        "name": "Cheapest",
                        "value": f"${min(pending, key=lambda q: q.price_usd).price_usd:,.0f}",
                        "inline": True,
                    },
                    {"name": "Threshold", "value": f"${threshold:,.0f}", "inline": True},
                ],
            )
            if ok:
                alerts_sent += 1
                for hit in pending:
                    store.mark_alerted(
                        event_id=event["id"],
                        platform=hit.platform,
                        price_usd=hit.price_usd,
                    )

    snapshot = {
        "scanned_at": datetime.now(timezone.utc).isoformat(),
        "threshold_usd": threshold,
        "great_reviewer_generated_at": gr_snapshot.generated_at,
        "great_reviewer_error": gr_snapshot.error,
        "events": all_results,
        "alerts_sent": alerts_sent,
    }
    store.write_scan_snapshot(ROOT / ".local", snapshot)
    if not dry_run:
        store.save()

    under = [r for r in all_results if r["hits_under_threshold"]]
    logger.info(
        "scan complete: %d events, %d under $%.0f, %d alerts sent",
        len(all_results),
        len(under),
        threshold,
        alerts_sent,
    )

    if print_json:
        print(json.dumps(snapshot, indent=2))

    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--dry-run", action="store_true", help="Print alerts, do not post Discord")
    p.add_argument("--force-alert", action="store_true", help="Ignore dedupe cooldown")
    p.add_argument("--json", action="store_true", help="Print scan snapshot JSON to stdout")
    p.add_argument("-v", "--verbose", action="store_true")
    return p


if __name__ == "__main__":
    args = build_parser().parse_args()
    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
    )

    load_dotenv(ROOT / ".env")
    config = load_yaml(ROOT / "config.yaml")
    events_doc = load_yaml(ROOT / "events.yaml")
    events = events_doc["events"]

    webhook = os.getenv("DISCORD_WEBHOOK_URL", "").strip()
    if not webhook and not args.dry_run:
        logger.error("DISCORD_WEBHOOK_URL not set — run: bash scripts/sync_env.sh")
        sys.exit(1)

    sys.exit(
        run_once(
            config=config,
            events=events,
            webhook_url=webhook,
            dry_run=args.dry_run,
            force_alert=args.force_alert,
            print_json=args.json,
        )
    )
