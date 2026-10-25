#!/usr/bin/env python3
"""Generate wiki source-stub pages from RSS newsletter files in the inbox.

Deterministic: reads each inbox file's frontmatter, writes one source page in
the owning wiki, and prints the archived path for the caller to move.

Usage: python3 scripts/gen_newsletter_stubs.py [--apply]
Without --apply it prints what it would write.
"""
from __future__ import annotations

import argparse
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
INBOX = ROOT / "research to be indexed"

# feed_id -> (wiki domain, related page or None)
FEEDS = {
    "latent-space": ("ccc", None),
    "sterling-sky": ("seo", None),
    "capital-flows": ("osint", None),
    "secpro": ("cybersec", None),
    "wublock": ("osint", None),
}


def parse_frontmatter(text: str) -> dict:
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    block = text[3:end]
    out: dict[str, str] = {}
    for line in block.splitlines():
        m = re.match(r"^([a-zA-Z_]+):\s*(.*)$", line)
        if m:
            out[m.group(1)] = m.group(2).strip().strip('"')
    return out


def slugify(name: str) -> str:
    stem = name[:-3] if name.endswith(".md") else name
    return stem


def body_pages(inbox_file: pathlib.Path) -> str:
    text = inbox_file.read_text(encoding="utf-8", errors="replace")
    return text


def render(inbox_file: pathlib.Path) -> tuple[str, str, str] | None:
    text = body_pages(inbox_file)
    fm = parse_frontmatter(text)
    feed = fm.get("feed_id", "")
    if feed not in FEEDS:
        return None
    wiki, _ = FEEDS[feed]
    title = fm.get("title", inbox_file.stem)
    url = fm.get("source_url", "")
    retrieved = fm.get("retrieved", "")
    slug = slugify(inbox_file.name)

    page = f"""---
title: {title}
type: source
tags: [source, rss, inbox-auto, {feed}]
keywords: [rss, {feed}]
related: []
maturity: draft
created: {retrieved}
updated: 2026-10-25
read_status: skimmed
---

## Raw Concept

Auto-dropped RSS newsletter stub from `research to be indexed/{inbox_file.name}`.

| Field | Value |
|-------|-------|
| URL | {url} |
| Feed | {feed} |
| Retrieved | {retrieved} |
| Inbox | `{inbox_file.name}` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/{wiki}/{inbox_file.name}` |

## Narrative

[TENTATIVE] Newsletter capture from the `{feed}` feed. Ingested as a skimmed stub.
No substantive claim below is verified against a second source.

## Snippets

See the inbox raw file.
"""
    return wiki, slug, page


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    files = sorted(p for p in INBOX.glob("*.md") if p.is_file())
    if not files:
        print("no newsletter files at inbox root")
        return 1

    written = 0
    for f in files:
        result = render(f)
        if result is None:
            print(f"skip (unknown feed): {f.name}")
            continue
        wiki, slug, page = result
        dest = ROOT / "wiki" / wiki / "sources" / f"{slug}.md"
        if dest.exists():
            print(f"EXISTS: {dest.relative_to(ROOT)}")
            continue
        print(f"{'WRITE' if args.apply else 'DRY  '}: {dest.relative_to(ROOT)}")
        if args.apply:
            dest.write_text(page, encoding="utf-8")
            written += 1

    print(f"\n{'wrote' if args.apply else 'would write'} {written if args.apply else 'N'} pages")
    return 0


if __name__ == "__main__":
    sys.exit(main())
