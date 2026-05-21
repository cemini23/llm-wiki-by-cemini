#!/usr/bin/env python3
"""Run Tier-2 arXiv sweep (Exa API) and write wiki/sweeps/YYYY-MM-DD.md."""

from __future__ import annotations

import json
import os
import re
import sys
import urllib.error
import urllib.request
from datetime import date, timedelta
from pathlib import Path

QUERIES = [
    ("agent-harness", "research paper on coding agent harness optimization, LLM agent orchestration framework, or autonomous agent observability"),
    ("options-pricing", "research paper presenting closed-form solution or computational breakthrough in options pricing, implied volatility, or Greeks calculation"),
    ("moe-scaling-parameter-estimation", "research paper on mixture of experts scaling laws, LLM parameter count estimation, or DeepSeek model evaluation"),
    ("financial-rl-multi-agent", "research paper on reinforcement learning for algorithmic trading, multi-agent financial systems, or RL portfolio optimization"),
    ("prediction-markets-microstructure", "research paper on prediction market microstructure, event contract pricing, Kalshi or Polymarket order-book analysis"),
]


def load_exa_key() -> str:
    if os.environ.get("EXA_API_KEY"):
        return os.environ["EXA_API_KEY"].strip()
    path = Path.home() / ".cemini" / "exa-api-key"
    if path.is_file():
        return path.read_text().strip()
    print("ERROR: set EXA_API_KEY or write ~/.cemini/exa-api-key", file=sys.stderr)
    sys.exit(1)


def exa_search(api_key: str, query: str, from_date: str) -> dict:
    body = json.dumps(
        {
            "query": query,
            "category": "research paper",
            "startPublishedDate": from_date,
            "numResults": 5,
            "type": "auto",
        }
    ).encode()
    req = urllib.request.Request(
        "https://api.exa.ai/search",
        data=body,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.loads(resp.read().decode())


def arxiv_id(url: str) -> str | None:
    m = re.search(r"arxiv\.org/(?:abs|pdf|html)/(\d{4}\.\d{4,5})", url)
    return m.group(1) if m else None


def title_from_result(r: dict) -> str:
    title = (r.get("title") or "").strip()
    if title:
        return title[:200]
    for line in (r.get("text") or "").splitlines():
        line = line.strip()
        if 30 <= len(line) <= 200 and not line.startswith(("[", "#")):
            return line
    return "(no title)"


def main() -> int:
    repo = Path(__file__).resolve().parent.parent
    today = date.today()
    from_date = (today - timedelta(days=14)).isoformat()
    sweeps_dir = repo / "wiki" / "sweeps"
    sweeps_dir.mkdir(parents=True, exist_ok=True)
    report = sweeps_dir / f"{today.isoformat()}.md"

    api_key = load_exa_key()
    partial = False
    sections: list[tuple[str, str, list[dict]]] = []

    for label, query in QUERIES:
        try:
            data = exa_search(api_key, query, from_date)
            results = data.get("results", [])
        except urllib.error.HTTPError as e:
            partial = True
            results = []
            print(f"WARNING: {label} HTTP {e.code}", file=sys.stderr)
        except Exception as e:
            partial = True
            results = []
            print(f"WARNING: {label} {e}", file=sys.stderr)
        sections.append((label, query, results))

    lines = [
        f"# Tier-2 arXiv Sweep — {today.isoformat()}",
        "",
        f"5 cluster queries × 5 hits. Category: `research paper`, window: `{from_date}` → `{today.isoformat()}` (14 days).",
        "",
        "Reference rubric: `@concepts/high-signal-paper-patterns.md`. Tier-2 is descriptive only — this report does NOT ingest.",
        "",
        "---",
        "",
    ]

    total = 0
    for i, (label, query, results) in enumerate(sections, 1):
        lines.append(f"## Q{i}: {label} ({len(results)} results)")
        lines.append("")
        lines.append(f"Query: `{query}`")
        lines.append("")
        lines.append("| # | Date | Title | arXiv | Notes |")
        lines.append("|---|------|-------|-------|-------|")
        for j, r in enumerate(results, 1):
            url = r.get("url", "")
            aid = arxiv_id(url) or ""
            d = (r.get("publishedDate") or "")[:10]
            title = title_from_result(r)
            notes = ""
            if aid:
                notes = f"`{aid}`"
            lines.append(f"| {j} | {d} | [{title[:120]}]({url}) | {notes} | |")
        lines.append("")
        total += len(results)

    lines.extend(
        [
            "---",
            "",
            "## Sweep summary",
            "",
            f"| Metric | Count |",
            f"|--------|-------|",
            f"| Total hits (raw) | {total} |",
            "",
            "### Next steps",
            "",
            "1. Score against `@concepts/high-signal-paper-patterns.md` (Tier-A / Tier-B / Skip).",
            "2. Dedupe via `scripts/preingest_check.py`.",
            "3. User approves ingest list.",
            "",
            f"### Discard",
            "",
            f"`rm wiki/sweeps/{today.isoformat()}.md` if nothing worth acting on.",
            "",
        ]
    )

    report.write_text("\n".join(lines), encoding="utf-8")
    print(f"Report: {report}")
    return 3 if partial else 0


if __name__ == "__main__":
    raise SystemExit(main())
