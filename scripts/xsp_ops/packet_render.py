"""Render research packet markdown stubs (never under briefs/)."""

from __future__ import annotations

import re
from datetime import date
from pathlib import Path
from typing import Any


def packet_filename(slug: str, day: date | None = None) -> str:
    d = day or date.today()
    safe = re.sub(r"[^\w\-]+", "-", slug).strip("-") or "post"
    return f"{d.isoformat()}_{safe}.md"


def render_packet_markdown(post: dict[str, Any]) -> str:
    title = post.get("title") or post.get("slug") or "untitled"
    slug = post.get("slug") or ""
    url = post.get("url") or ""
    published = post.get("published") or ""
    tags = ", ".join(post.get("regime_tags") or []) or "—"
    priority = post.get("priority") or "—"
    action = post.get("action") or "packet"
    keywords = ", ".join(post.get("matched_keywords") or []) or "—"
    excerpt = post.get("excerpt") or ""
    source_path = post.get("source_path") or ""

    return f"""# XSP packet: {title}

## Target

CeminiSuite / xsp-killer

## Summary

Macro Charts signal staged for XSP ops review.

| Field | Value |
|-------|-------|
| slug | `{slug}` |
| priority | {priority} |
| action | {action} |
| published | {published} |
| url | {url} |
| regime_tags | {tags} |
| matched_keywords | {keywords} |
| source_path | `{source_path}` |

## Body

### Excerpt

{excerpt}

### Operator notes

- Packet is **staging only** under `.local/ops/xsp/packets/`.
- Human promote ritual: copy to `briefs/xsp-YYYY-MM-DD_<slug>.md` after review.
- Do not auto-ship to prod or wiki.

### Next steps

1. Confirm XSP relevance vs full post body.
2. If keep: promote to briefs and route per post_ingest_workflow.
3. If skip: leave packet in place; no briefs write.
"""


def write_packet(
    post: dict[str, Any],
    packets_dir: Path,
    *,
    day: date | None = None,
) -> Path:
    packets_dir.mkdir(parents=True, exist_ok=True)
    name = packet_filename(str(post.get("slug") or "post"), day=day)
    path = packets_dir / name
    path.write_text(render_packet_markdown(post), encoding="utf-8")
    return path


def existing_packet_for_slug(packets_dir: Path, slug: str) -> Path | None:
    if not packets_dir.is_dir():
        return None
    for path in packets_dir.glob(f"*_{slug}.md"):
        return path
    # also match if slug has date prefix confusion
    for path in packets_dir.glob("*.md"):
        if path.stem.endswith(f"_{slug}") or path.stem == slug:
            return path
    return None
