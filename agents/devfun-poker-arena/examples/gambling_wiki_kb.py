"""Gambling-wiki RAG via librarian kb-server (same stack as Cemini prod brain).

Fail-open: missing key, timeout, or unreachable librarian → empty briefing.
Scoped with ``project=gambling-wiki`` (see OSINT ``sync_wiki_to_librarian.sh``).
"""
from __future__ import annotations

import os
import re
from pathlib import Path
from typing import Any

import httpx

_GAMBLING_PROJECT = "gambling-wiki"
_DEFAULT_BASE = "http://10.0.0.2:3838"
_MAX_BRIEFING_CHARS = 4500

# Static anchors + one dynamic slot from analyze posture.
_BASE_QUERIES = (
    "poker HL analyst loop devfun arena heuristic learning",
    "cemini devfun poker agent opponent modeling preflop guards",
)


def _enabled() -> bool:
    return os.environ.get("CEMINI_HL_WIKI_KB", "1").strip().lower() not in ("0", "false", "no")


def load_librarian_env() -> None:
    """Load LIBRARIAN_* from prod/laptop env files without overriding existing env."""
    candidates = (
        Path("/opt/cemini/.env"),
        Path.home() / ".cemini" / "llm-routing.env",
        Path(__file__).resolve().parent.parent / ".env",
    )
    keys = ("LIBRARIAN_API_KEY", "LIBRARIAN_BASE_URL", "LIBRARIAN_TIMEOUT_S", "CEMINI_HL_WIKI_KB")
    for path in candidates:
        if not path.is_file():
            continue
        for line in path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, _, v = line.partition("=")
            k, v = k.strip(), v.strip().strip('"').strip("'")
            if k in keys and k not in os.environ and v:
                os.environ[k] = v


def _headers() -> dict[str, str]:
    key = os.environ.get("LIBRARIAN_API_KEY", "").strip()
    h: dict[str, str] = {"Accept": "application/json"}
    if key:
        h["X-API-Key"] = key
    return h


def _base_url() -> str:
    return os.environ.get("LIBRARIAN_BASE_URL", _DEFAULT_BASE).rstrip("/")


def _timeout() -> float:
    try:
        return float(os.environ.get("LIBRARIAN_TIMEOUT_S", "8"))
    except ValueError:
        return 8.0


def _format_context_payload(payload: dict[str, Any]) -> str:
    briefing = (payload.get("briefing") or "").strip()
    sources = payload.get("sources") or []
    if not briefing and not sources:
        return ""
    parts: list[str] = []
    if briefing:
        parts.append(briefing)
    if sources:
        lines = []
        for s in sources:
            if not isinstance(s, dict):
                continue
            title = s.get("title") or s.get("path") or "Untitled"
            lines.append(f"- {title}")
        if lines:
            parts.append("**Sources:**\n" + "\n".join(lines))
    return "\n\n".join(parts)


def _is_gambling_path(hit: dict[str, Any]) -> bool:
    blob = " ".join(
        str(hit.get(k) or "")
        for k in ("path", "slug", "file", "filepath", "vault_path", "project", "title")
    ).lower()
    return "gambling-wiki" in blob or blob.startswith("entities/bots/cemini")


def fetch_context_detail(query: str, *, limit: int = 5) -> dict[str, Any]:
    """Single kb_context call scoped to gambling-wiki."""
    empty: dict[str, Any] = {"text": "", "sources": [], "query": query, "wiki_hits": []}
    if not _enabled():
        return {**empty, "skipped": "disabled"}
    if not os.environ.get("LIBRARIAN_API_KEY", "").strip():
        return {**empty, "skipped": "no_api_key"}

    params = {"q": query, "limit": str(limit), "project": _GAMBLING_PROJECT}
    try:
        r = httpx.get(
            f"{_base_url()}/api/v1/context",
            params=params,
            headers=_headers(),
            timeout=_timeout(),
        )
        if r.status_code != 200:
            return {**empty, "error": f"HTTP {r.status_code}"}
        payload = r.json()
        sources = [s for s in (payload.get("sources") or []) if isinstance(s, dict)]
        if sources and not all(_is_gambling_path(s) for s in sources):
            sources = [s for s in sources if _is_gambling_path(s)]
        text = _format_context_payload({**payload, "sources": sources})
        hits = []
        for s in sources:
            for key in ("path", "slug", "title"):
                val = s.get(key)
                if val:
                    hits.append(str(val))
                    break
        return {**empty, "text": text, "sources": sources, "wiki_hits": hits}
    except Exception as exc:
        return {**empty, "error": str(exc)}


def _dynamic_query(report_text: str, qual_summary: str) -> str:
    """One analyze-derived query (position leak or qualification posture)."""
    if qual_summary.strip():
        return f"devfun poker qualification protect survival {qual_summary[:120]}"
    m = re.search(r"(SB|BB|UTG|MP|CO|BTN).{0,40}(leak|worst|loss)", report_text, re.I)
    if m:
        return f"poker preflop {m.group(1)} leak guard devfun arena"
    return "devfun poker arena playground strategy preflop tight passive"


def fetch_gambling_wiki_briefing(
    *,
    report_text: str = "",
    qual_summary: str = "",
    max_chars: int = _MAX_BRIEFING_CHARS,
) -> dict[str, Any]:
    """Merge multiple scoped kb_context calls into one briefing block."""
    load_librarian_env()
    if not _enabled():
        return {"text": "", "queries": [], "wiki_hits": [], "skipped": "disabled"}

    queries = list(_BASE_QUERIES)
    queries.append(_dynamic_query(report_text, qual_summary))

    sections: list[str] = []
    all_hits: list[str] = []
    meta_queries: list[dict[str, Any]] = []

    for q in queries:
        detail = fetch_context_detail(q, limit=4)
        meta_queries.append(
            {
                "query": q,
                "char_count": len(detail.get("text") or ""),
                "wiki_hits": detail.get("wiki_hits") or [],
                "error": detail.get("error"),
                "skipped": detail.get("skipped"),
            }
        )
        text = (detail.get("text") or "").strip()
        if not text:
            continue
        block = f"### Query: {q}\n{text}"
        if sum(len(s) for s in sections) + len(block) > max_chars:
            remain = max_chars - sum(len(s) for s in sections)
            if remain > 200:
                sections.append(block[:remain] + "\n…")
            break
        sections.append(block)
        all_hits.extend(detail.get("wiki_hits") or [])

    combined = "\n\n".join(sections).strip()
    return {
        "text": combined,
        "queries": meta_queries,
        "wiki_hits": list(dict.fromkeys(all_hits)),
        "char_count": len(combined),
    }
