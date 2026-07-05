#!/usr/bin/env python3
"""Poll configured finance Substack RSS feeds → inbox markdown.

Usage:
  python3 scripts/substack_rss_poller.py --dry-run
  python3 scripts/substack_rss_poller.py --feed klement
  bash scripts/run_substack_rss_poller.sh
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

CONFIG_PATH = REPO_ROOT / "config" / "substack-rss-ingest.yaml"
NS = {
    "content": "http://purl.org/rss/1.0/modules/content/",
    "dc": "http://purl.org/dc/elements/1.1/",
}


def load_config() -> dict[str, Any]:
    if not CONFIG_PATH.is_file():
        raise SystemExit(f"Missing config: {CONFIG_PATH}")
    return yaml.safe_load(CONFIG_PATH.read_text(encoding="utf-8")) or {}


@dataclass
class FeedItem:
    title: str
    link: str
    pub_date: datetime
    description: str
    content_html: str


@dataclass
class FeedConfig:
    id: str
    name: str
    feed_url: str
    filename_prefix: str
    tags: list[str]
    max_age_days: int | None = None
    cross_wiki: list[str] | None = None


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


def parse_feed_configs(cfg: dict[str, Any]) -> list[FeedConfig]:
    feeds: list[FeedConfig] = []
    for row in cfg.get("feeds") or []:
        if not row.get("enabled", True):
            continue
        feeds.append(
            FeedConfig(
                id=str(row["id"]),
                name=str(row["name"]),
                feed_url=str(row["feed_url"]),
                filename_prefix=str(row.get("filename_prefix") or f"substack-rss-{row['id']}"),
                tags=list(row.get("tags") or ["substack"]),
                max_age_days=row.get("max_age_days"),
                cross_wiki=list(row["cross_wiki"]) if row.get("cross_wiki") else None,
            )
        )
    return feeds


def build_markdown(
    feed: FeedConfig,
    item: FeedItem,
    body: str,
    teaser_only: bool,
) -> str:
    date_part = item.pub_date.astimezone(timezone.utc).strftime("%Y-%m-%d")
    tier = "free (RSS teaser)" if teaser_only else "free (RSS)"
    tag_yaml = ", ".join(feed.tags + ["inbox-auto", "rss"])
    lines = [
        "---",
        f'title: "{feed.name} — {item.title}"',
        "type: source-stub",
        f"tags: [{tag_yaml}]",
        f"retrieved: {date_part}",
        f"source_url: {item.link}",
        f"feed_id: {feed.id}",
        f"tier: {tier}",
    ]
    if feed.cross_wiki:
        lines.append(f"cross_wiki: [{', '.join(feed.cross_wiki)}]")
    lines.extend([
        "---",
        "",
        f"# {feed.name}",
        "",
        f"- **Title:** {item.title}",
        f"- **Published:** {item.pub_date.isoformat()}",
        f"- **URL:** {item.link}",
        f"- **Feed:** {feed.id} ({feed.feed_url})",
        "",
    ])
    if teaser_only:
        lines.append("_RSS teaser — full post may be paywalled on Substack._")
        lines.append("")
    lines.extend(["## Body", "", body, ""])
    return "\n".join(lines)


def poll_feed(
    feed: FeedConfig,
    cfg: dict[str, Any],
    state: dict[str, Any],
    *,
    dry_run: bool,
    default_max_age_days: int,
) -> tuple[int, int]:
    user_agent = cfg.get("user_agent", "CeminiOSINT-SubstackRSS/1.0")
    slug_max = int((cfg.get("inbox") or {}).get("slug_max_len", 48))
    max_age_days = feed.max_age_days if feed.max_age_days is not None else default_max_age_days
    cutoff = datetime.now(timezone.utc) - timedelta(days=max_age_days)

    exported = 0
    skipped = 0
    INBOX.mkdir(parents=True, exist_ok=True)

    try:
        xml_bytes = fetch_feed(feed.feed_url, user_agent)
    except OSError as exc:
        print(f"ERROR {feed.id}: fetch failed — {exc}")
        return 0, 1

    for item in parse_feed(xml_bytes):
        if item.pub_date < cutoff:
            skipped += 1
            continue
        if post_already_exported(state, item.link):
            skipped += 1
            continue
        if inbox_has_url(item.link):
            skipped += 1
            continue

        body = html_to_text(item.content_html) if item.content_html else item.description
        teaser_only = is_rss_teaser_only(item.content_html, body, item.link)
        date_part = item.pub_date.strftime("%Y-%m-%d")
        slug = slugify(item.title, slug_max) or post_slug_from_url(item.link)
        out_name = f"{feed.filename_prefix}-{date_part}-{slug}.md"
        out_path = INBOX / out_name
        if out_path.exists():
            out_name = f"{feed.filename_prefix}-{date_part}-{post_slug_from_url(item.link)}.md"
            out_path = INBOX / out_name

        md = build_markdown(feed, item, body, teaser_only)
        print(f"{'DRY-RUN' if dry_run else 'EXPORT'} [{feed.id}] {out_name} teaser={teaser_only}")

        if dry_run:
            exported += 1
            continue

        out_path.write_text(md, encoding="utf-8")
        record_post_export(
            state,
            item.link,
            source=f"rss:{feed.id}",
            filename=out_name,
        )
        exported += 1

    return exported, skipped


def migrate_legacy_state(state_path: Path) -> None:
    if state_path.is_file():
        return
    legacy = REPO_ROOT / ".local/state/macro-charts-posts.json"
    if legacy.is_file():
        state_path.parent.mkdir(parents=True, exist_ok=True)
        state_path.write_text(legacy.read_text(encoding="utf-8"), encoding="utf-8")


def poll_all(
    cfg: dict[str, Any],
    *,
    dry_run: bool,
    feed_id: str | None = None,
    max_age_days: int | None = None,
) -> int:
    state_path = REPO_ROOT / (cfg.get("state") or {}).get(
        "posts_registry", ".local/state/substack-rss-posts.json"
    )
    migrate_legacy_state(state_path)
    state = read_post_state(state_path)
    age = max_age_days if max_age_days is not None else int(cfg.get("max_age_days", 7))

    feeds = parse_feed_configs(cfg)
    if feed_id:
        feeds = [f for f in feeds if f.id == feed_id]
        if not feeds:
            raise SystemExit(f"Unknown feed id: {feed_id!r}")

    total_exported = 0
    total_skipped = 0
    for feed in feeds:
        exported, skipped = poll_feed(
            feed, cfg, state, dry_run=dry_run, default_max_age_days=age
        )
        total_exported += exported
        total_skipped += skipped

    if not dry_run and total_exported:
        write_post_state(state_path, state)
        trigger_inbox_notify()

    print(f"Done: exported={total_exported} skipped={total_skipped} feeds={len(feeds)}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Finance Substack RSS → inbox poller")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--feed", help="Poll single feed id from config")
    parser.add_argument("--max-age-days", type=int, default=None)
    args = parser.parse_args()
    return poll_all(
        load_config(),
        dry_run=args.dry_run,
        feed_id=args.feed,
        max_age_days=args.max_age_days,
    )


if __name__ == "__main__":
    sys.exit(main())
