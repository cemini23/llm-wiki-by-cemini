"""Parse Macro Charts inbox markdown into structured signals."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Any

_SCRIPTS = Path(__file__).resolve().parents[1]
if str(_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS))

from xsp_ops.brain import load_brain, mark_parsed, save_brain  # noqa: E402
from xsp_ops.paths import INBOX_DIR, ensure_layout  # noqa: E402

# Filename patterns for Macro Charts drops
INBOX_GLOBS = ("macro-charts-*.md", "substack-rss-macrocharts-*.md")

# Lightweight regime heuristics (no LLM)
REGIME_KEYWORDS: dict[str, tuple[str, ...]] = {
    "risk-on": ("risk-on", "risk on", "risk appetite", "bullish"),
    "risk-off": ("risk-off", "risk off", "flight to safety", "defensive"),
    "rates": ("rates", "yields", "treasury", "duration", "fed funds"),
    "inflation": ("cpi", "inflation", "pce", "deflator"),
    "semis": ("semiconductor", "semis", "sox", "nvidia", "tsmc", "asml"),
    "oil": ("oil", "crude", "brent", "wti"),
    "fx": ("yen", "dollar", "dxy", "eurusd"),
    "breadth": ("breadth", "advance-decline", "participation"),
    "fomc": ("fomc", "fed ", "federal reserve", "powell"),
}


def slug_from_filename(path: Path) -> str:
    stem = path.stem
    # strip common prefixes
    for prefix in ("macro-charts-", "substack-rss-macrocharts-"):
        if stem.startswith(prefix):
            stem = stem[len(prefix) :]
            break
    # collapse to safe slug
    s = re.sub(r"[^\w\s-]", "", stem.lower())
    s = re.sub(r"[\s_]+", "-", s).strip("-")
    return (s[:80] or "post").rstrip("-")


def _extract_frontmatter(text: str) -> dict[str, str]:
    """Parse simple YAML-ish frontmatter if present."""
    meta: dict[str, str] = {}
    if not text.startswith("---"):
        return meta
    end = text.find("\n---", 3)
    if end < 0:
        return meta
    block = text[3:end].strip()
    for line in block.splitlines():
        if ":" not in line:
            continue
        key, _, val = line.partition(":")
        key = key.strip().lower()
        val = val.strip().strip("\"'")
        if key and val:
            meta[key] = val
    return meta


def _first_heading(text: str) -> str | None:
    for line in text.splitlines():
        m = re.match(r"^#\s+(.+)$", line.strip())
        if m:
            return m.group(1).strip()
    return None


def _find_url(text: str, meta: dict[str, str]) -> str:
    for key in ("url", "link", "canonical", "source"):
        if meta.get(key) and meta[key].startswith("http"):
            return meta[key]
    m = re.search(r"https?://[^\s\)\]>\"']+", text)
    return m.group(0).rstrip(".,;") if m else ""


def _find_published(text: str, meta: dict[str, str], path: Path) -> str:
    for key in ("published", "date", "pub_date", "created"):
        if meta.get(key):
            return meta[key]
    m = re.search(r"\b(20\d{2}-\d{2}-\d{2})\b", text[:800])
    if m:
        return m.group(1)
    m2 = re.search(r"(20\d{2}-\d{2}-\d{2})", path.name)
    return m2.group(1) if m2 else ""


def _regime_tags(text: str) -> list[str]:
    lower = text.lower()
    tags: list[str] = []
    for tag, kws in REGIME_KEYWORDS.items():
        if any(k in lower for k in kws):
            tags.append(tag)
    return tags


def _excerpt(text: str, limit: int = 500) -> str:
    # Drop frontmatter for excerpt
    body = text
    if body.startswith("---"):
        end = body.find("\n---", 3)
        if end >= 0:
            body = body[end + 4 :]
    # strip markdown headings markers for density
    body = re.sub(r"^#+\s*", "", body, flags=re.M)
    body = re.sub(r"\s+", " ", body).strip()
    if len(body) <= limit:
        return body
    return body[: limit - 1].rstrip() + "…"


def parse_markdown_file(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8", errors="replace")
    meta = _extract_frontmatter(text)
    title = meta.get("title") or _first_heading(text) or path.stem
    slug = meta.get("slug") or slug_from_filename(path)
    url = _find_url(text, meta)
    published = _find_published(text, meta, path)
    return {
        "slug": slug,
        "title": title,
        "url": url,
        "published": published,
        "source_path": str(path),
        "regime_tags": _regime_tags(text),
        "excerpt": _excerpt(text, 500),
    }


def discover_inbox_files(inbox: Path | None = None) -> list[Path]:
    base = inbox if inbox is not None else INBOX_DIR
    if not base.is_dir():
        return []
    found: list[Path] = []
    for pattern in INBOX_GLOBS:
        found.extend(sorted(base.glob(pattern)))
    # de-dupe while preserving order
    seen: set[Path] = set()
    out: list[Path] = []
    for p in found:
        rp = p.resolve()
        if rp not in seen:
            seen.add(rp)
            out.append(p)
    return out


def run_parse(
    *,
    dry_run: bool = False,
    root: Path | None = None,
    inbox: Path | None = None,
) -> list[dict[str, Any]]:
    """Scan inbox for unparsed Macro Charts drops; return signal list."""
    ensure_layout(root)
    brain = load_brain(root)
    known_slugs = set(brain.get("parsed_slugs") or [])
    known_paths = set(brain.get("parsed_paths") or [])
    # Also treat landed post_ids as already handled for parse skip
    known_slugs |= set(brain.get("post_ids") or [])
    known_paths |= set(brain.get("known_paths") or [])

    signals: list[dict[str, Any]] = []
    for path in discover_inbox_files(inbox):
        sp = str(path)
        if sp in known_paths:
            continue
        try:
            signal = parse_markdown_file(path)
        except OSError as exc:
            print(f"[parse] skip unreadable {path}: {exc}", file=sys.stderr)
            continue
        if signal["slug"] in known_slugs:
            continue
        signals.append(signal)

    # Stash last parse results on brain for land step (non-dry)
    brain["last_parse_signals"] = signals if not dry_run else brain.get("last_parse_signals") or []
    if dry_run:
        print(f"[parse] dry-run: {len(signals)} new signal(s)")
        for s in signals:
            print(f"  - {s['slug']}: {s['title'][:60]} tags={s['regime_tags']}")
        return signals

    for s in signals:
        mark_parsed(brain, s["slug"], s["source_path"])
    brain["last_parse_signals"] = signals
    save_brain(brain, root)
    print(f"[parse] parsed {len(signals)} signal(s)")
    return signals
