#!/usr/bin/env python3
"""Poll Macro Charts Substack RSS for free posts → inbox markdown.

Paid issues are not in the public feed — those arrive via cousin Gmail forwards.
Dedupes against paid-forward exports so the same URL is not dropped twice.

Usage:
  python3 scripts/macro_charts_rss_poller.py --dry-run
  bash scripts/run_macro_charts_rss_poller.sh
"""

from __future__ import annotations

import argparse
import sys
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path
from typing import Any
from urllib.request import Request, urlopen

import yaml

SCRIPTS = Path(__file__).resolve().parent
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from macro_charts_common import (  # noqa: E402
    INBOX,
    REPO_ROOT,
    html_to_text,
    inbox_has_url,
    is_rss_teaser_only,
    post_already_exported,
    post_slug_from_url,
    read_post_state,
    record_post_export,
    slugify,
    trigger_inbox_notify,
    write_post_state,
)

CONFIG_PATH = REPO_ROOT / "config" / "macro-charts-ingest.yaml"
LEGACY_CONFIG = REPO_ROOT / "config" / "macro-charts-email.yaml"
NS = {
    "content": "http://purl.org/rss/1.0/modules/content/",
    "dc": "http://purl.org/dc/elements/1.1/",
}


def load_config() -> dict[str, Any]:
    path = CONFIG_PATH if CONFIG_PATH.is_file() else LEGACY_CONFIG
    if not path.is_file():
        raise SystemExit(f"Missing config: {CONFIG_PATH}")
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


@dataclass
class FeedItem:
    title: str
    link: str
    pub_date: datetime
    description: str
    content_html: str


def parse_feed(xml_bytes: bytes) -> list[FeedItem]:
    root = ET.fromstring(xml_bytes)
    items: list[FeedItem] = []
    for item in root.findall("./channel/item"):
        title = (item.findtext("title") or "").strip()
        link = (item.findtext("link") or "").strip()
        if not link:
            continue
        desc = item.findtext("description") or ""
        content_el = item.find("content:encoded", NS)
        content_html = content_el.text if content_el is not None and content_el.text else ""
        pub_raw = item.findtext("pubDate") or ""
        try:
            pub_date = parsedate_to_datetime(pub_raw)
            if pub_date.tzinfo is None:
                pub_date = pub_date.replace(tzinfo=timezone.utc)
        except (TypeError, ValueError):
            pub_date = datetime.now(timezone.utc)
        items.append(FeedItem(title, link, pub_date, desc, content_html))
    return items


def fetch_feed(url: str, user_agent: str) -> bytes:
    req = Request(url, headers={"User-Agent": user_agent})
    with urlopen(req, timeout=60) as resp:
        return resp.read()


def build_markdown(item: FeedItem, body: str, teaser_only: bool) -> str:
    date_part = item.pub_date.astimezone(timezone.utc).strftime("%Y-%m-%d")
    tier = "free (RSS teaser)" if teaser_only else "free (RSS full)"
    lines = [
        "---",
        f'title: "Macro Charts — {item.title}"',
        "type: source-stub",
        "tags: [macro-charts, substack, rss, inbox-auto]",
        f"retrieved: {date_part}",
        f"substack_url: {item.link}",
        f"tier: {tier}",
        "---",
        "",
        f"# Macro Charts — {item.title}",
        "",
        f"- **Published:** {item.pub_date.isoformat()}",
        f"- **URL:** {item.link}",
        f"- **Capture:** RSS ({tier})",
        "",
    ]
    if teaser_only:
        lines.append(
            "_RSS teaser only — paid/full body may arrive via Vincent forward; "
            "prefer the `macro-charts-paid-forward-*` inbox file when present._"
        )
        lines.append("")
    lines.extend(["## Body", "", body, ""])
    return "\n".join(lines)


def poll_rss(cfg: dict[str, Any], *, dry_run: bool) -> int:
    rss_cfg = cfg.get("rss") or {}
    feed_url = rss_cfg.get("feed_url", "https://www.macrocharts.com/feed")
    user_agent = rss_cfg.get("user_agent", "CeminiOSINT-MacroCharts/1.0")
    max_age_days = int(rss_cfg.get("max_age_days", 14))
    slug_max = int((cfg.get("inbox") or {}).get("slug_max_len", 48))
    prefix = (cfg.get("inbox") or {}).get("rss_filename_prefix", "macro-charts-rss")
    state_path = REPO_ROOT / (cfg.get("state") or {}).get(
        "posts_registry", ".local/state/macro-charts-posts.json"
    )

    state = read_post_state(state_path)
    cutoff = datetime.now(timezone.utc) - timedelta(days=max_age_days)
    xml_bytes = fetch_feed(feed_url, user_agent)
    items = parse_feed(xml_bytes)

    exported = 0
    skipped = 0
    INBOX.mkdir(parents=True, exist_ok=True)

    for item in items:
        if item.pub_date < cutoff:
            skipped += 1
            continue
        if post_already_exported(state, item.link):
            print(f"SKIP {item.link} — already captured")
            skipped += 1
            continue
        if inbox_has_url(item.link):
            print(f"SKIP {item.link} — already in inbox")
            skipped += 1
            continue

        body = html_to_text(item.content_html) if item.content_html else item.description
        teaser_only = is_rss_teaser_only(item.content_html, body)
        date_part = item.pub_date.strftime("%Y-%m-%d")
        slug = slugify(item.title, slug_max) or post_slug_from_url(item.link)
        out_name = f"{prefix}-{date_part}-{slug}.md"
        out_path = INBOX / out_name
        if out_path.exists():
            out_name = f"{prefix}-{date_part}-{post_slug_from_url(item.link)}.md"
            out_path = INBOX / out_name

        md = build_markdown(item, body, teaser_only)
        print(f"{'DRY-RUN' if dry_run else 'EXPORT'} {out_name} teaser={teaser_only}")

        if dry_run:
            exported += 1
            continue

        out_path.write_text(md, encoding="utf-8")
        record_post_export(state, item.link, source="rss", filename=out_name)
        exported += 1

    if not dry_run and exported:
        write_post_state(state_path, state)
        trigger_inbox_notify()

    print(f"Done: exported={exported} skipped={skipped}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Macro Charts RSS → inbox poller")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    return poll_rss(load_config(), dry_run=args.dry_run)


if __name__ == "__main__":
    sys.exit(main())
