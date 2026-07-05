#!/usr/bin/env python3
"""Route newsletter RSS inbox drops to sibling wikis (batch).

Creates OSINT wiki/sources stubs + target wiki/sources pages with backlinks.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
REPO_ROOT = SCRIPTS.parent
INBOX = REPO_ROOT / "research to be indexed"
OSINT_WIKI = REPO_ROOT / "wiki"

sys.path.insert(0, str(SCRIPTS))

from cross_wiki_route import (  # noqa: E402
    add_backlink,
    append_to_index,
    append_to_log,
    create_page,
    load_wiki_aliases,
)

FEED_CROSS_WIKI = {
    "outlier-weekly": ["gambling-wiki"],
    "event-horizon": ["gambling-wiki"],
    "the-closing-line": ["gambling-wiki"],
}

GAMBLING_SLUG_KEYWORDS = (
    "prediction-market",
    "fundamental-flaw-of-prediction",
    "kalshi",
    "polymarket",
)


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end < 0:
        return {}
    block = text[3:end]
    data: dict[str, str] = {}
    for line in block.splitlines():
        if ":" not in line:
            continue
        key, val = line.split(":", 1)
        data[key.strip()] = val.strip()
    return data


def parse_cross_wiki_targets(meta: dict[str, str], filename: str) -> list[str]:
    raw = meta.get("cross_wiki", "")
    if raw:
        return re.findall(r"[\w-]+-wiki", raw)
    feed = meta.get("feed_id", "")
    if feed in FEED_CROSS_WIKI:
        return FEED_CROSS_WIKI[feed]
    if feed == "klement" and any(k in filename for k in GAMBLING_SLUG_KEYWORDS):
        return ["gambling-wiki"]
    return []


def extract_body(text: str) -> str:
    if "## Body" not in text:
        return text
    return text.split("## Body", 1)[1].strip()


def osint_source_slug(inbox_name: str) -> str:
    return Path(inbox_name).stem


def create_osint_source(inbox_path: Path, meta: dict[str, str], body: str) -> Path:
    slug = osint_source_slug(inbox_path.name)
    out = OSINT_WIKI / "sources" / f"{slug}.md"
    if out.exists():
        return out

    title = meta.get("title", slug).strip('"')
    source_url = meta.get("source_url") or meta.get("substack_url", "")
    feed_id = meta.get("feed_id", "")
    targets = parse_cross_wiki_targets(meta, inbox_path.name)
    target_note = ", ".join(f"@{t}" for t in targets) if targets else "osint-wiki (primary)"

    content = f"""---
title: {title}
type: source
tags: [source, newsletter-rss, inbox-auto, {feed_id}]
keywords: [rss, newsletter, {feed_id}]
related: []
maturity: draft
created: 2026-07-05
updated: 2026-07-05
read_status: skimmed
---

## Relations

## Raw Concept

Auto-dropped RSS newsletter stub from `research to be indexed/{inbox_path.name}`.
Cross-wiki route target: {target_note}.

| Field | Value |
|-------|-------|
| URL | {source_url} |
| Feed | {feed_id} |
| Inbox | `{inbox_path.name}` |

## Narrative

[TENTATIVE] Newsletter capture — routed to sibling wiki where `cross_wiki` applies; OSINT keeps trading-stack overlap only.

## Snippets

See inbox raw file and target wiki source page after cross-wiki route.
"""
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(content, encoding="utf-8")
    print(f"  OSINT source: {out.relative_to(REPO_ROOT)}")
    return out


def route_file(inbox_path: Path, aliases: dict[str, Path]) -> int:
    text = inbox_path.read_text(encoding="utf-8")
    meta = parse_frontmatter(text)
    targets = parse_cross_wiki_targets(meta, inbox_path.name)
    if not targets:
        return 0

    body = extract_body(text)
    title = meta.get("title", inbox_path.stem).strip('"')
    osint_slug = osint_source_slug(inbox_path.name)
    backlink = f"sources/{osint_slug}.md"
    create_osint_source(inbox_path, meta, body)

    routed = 0
    for target_alias in targets:
        if target_alias not in aliases:
            print(f"  SKIP {target_alias} — path not found")
            continue
        target_path = aliases[target_alias]
        result = create_page(
            target_path,
            "sources",
            osint_slug,
            title,
            "osint-wiki",
            backlink,
            body[:12000],
            force=False,
        )
        if result is None:
            continue
        append_to_index(target_path, "sources", osint_slug, title)
        append_to_log(target_path, title, osint_slug, "sources", "osint-wiki", backlink)
        add_backlink(OSINT_WIKI, backlink, target_alias, "sources", osint_slug)
        routed += 1
        print(f"  Routed → @{target_alias}/sources/{osint_slug}.md")
    return routed


def main() -> int:
    aliases = load_wiki_aliases()
    needed = {"gambling-wiki", "cybersecurity-wiki", "seo-wiki", "ccc-wiki"}
    missing = needed - set(aliases)
    if missing:
        print(f"ERROR: missing wiki aliases: {', '.join(sorted(missing))}")
        return 1

    patterns = ("newsletter-rss-*.md", "substack-rss-*.md")
    files: list[Path] = []
    for pattern in patterns:
        files.extend(INBOX.glob(pattern))
    files.sort()

    total = 0
    for path in files:
        meta = parse_frontmatter(path.read_text(encoding="utf-8"))
        if not parse_cross_wiki_targets(meta, path.name):
            continue
        print(f"\n{path.name}")
        total += route_file(path, aliases)

    print(f"\nDone: {total} target source pages created/linked")
    return 0


if __name__ == "__main__":
    sys.exit(main())
