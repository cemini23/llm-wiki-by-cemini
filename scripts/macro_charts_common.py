"""Shared helpers for Macro Charts RSS + email inbox drops."""

from __future__ import annotations

import html
import json
import re
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

REPO_ROOT = Path(__file__).resolve().parent.parent
INBOX = REPO_ROOT / "research to be indexed"
DEFAULT_STATE_PATH = REPO_ROOT / ".local/state/macro-charts-posts.json"


def slugify(text: str, max_len: int = 48) -> str:
    s = re.sub(r"[^\w\s-]", "", text.lower())
    s = re.sub(r"[\s_]+", "-", s).strip("-")
    return (s[:max_len] or "issue").rstrip("-")


def html_to_text(fragment: str) -> str:
    text = re.sub(r"(?is)<(script|style).*?>.*?</\1>", " ", fragment)
    text = re.sub(r"(?i)<br\s*/?>", "\n", text)
    text = re.sub(r"(?i)</p>", "\n\n", text)
    text = re.sub(r"(?i)</h[1-6]>", "\n\n", text)
    text = re.sub(r"<[^>]+>", " ", text)
    return html.unescape(re.sub(r"[ \t]+\n", "\n", text)).strip()


def normalize_post_url(url: str) -> str:
    parsed = urlparse(url.strip())
    path = parsed.path.rstrip("/")
    return f"{parsed.netloc.lower()}{path}"


def post_slug_from_url(url: str) -> str:
    m = re.search(r"/p/([a-zA-Z0-9_-]+)", url)
    return m.group(1) if m else slugify(url)


def read_post_state(path: Path = DEFAULT_STATE_PATH) -> dict[str, Any]:
    if not path.is_file():
        return {"posts": {}}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        if "posts" not in data:
            data["posts"] = {}
        return data
    except (json.JSONDecodeError, OSError):
        return {"posts": {}}


def write_post_state(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True), encoding="utf-8")


def post_already_exported(state: dict[str, Any], url: str, *, prefer_source: str | None = None) -> bool:
    """Return True if we should skip exporting this URL.

    Email (paid) exports win over RSS when the same post URL was only captured as RSS.
    """
    key = normalize_post_url(url)
    entry = (state.get("posts") or {}).get(key)
    if not entry:
        return False
    if prefer_source == "email" and entry.get("source") == "rss":
        return False
    return True


def record_post_export(
    state: dict[str, Any],
    url: str,
    *,
    source: str,
    filename: str,
) -> None:
    key = normalize_post_url(url)
    state.setdefault("posts", {})[key] = {
        "source": source,
        "filename": filename,
        "url": url,
    }


def inbox_has_url(url: str) -> bool:
    slug = post_slug_from_url(url)
    if not INBOX.is_dir():
        return False
    for path in INBOX.glob("macro-charts-*.md"):
        text = path.read_text(encoding="utf-8", errors="replace")
        if url in text or slug in path.name:
            return True
    return False


def trigger_inbox_notify() -> None:
    import subprocess

    script = REPO_ROOT / "scripts" / "inbox_notify.sh"
    if script.is_file():
        subprocess.run(["/bin/bash", str(script)], check=False)


def is_rss_teaser_only(html_content: str, plain: str) -> bool:
    """Substack free RSS items end with a Read more link; paid posts are absent from feed."""
    blob = f"{html_content}\n{plain}".lower()
    return "read more" in blob and "macrocharts.com/p/" in blob
