#!/usr/bin/env python3
"""Daily research digest — Exa discovery + inbox triage → wiki/sweeps/YYYY-MM-DD-daily.md.

Collection only. Does NOT ingest, commit, or write wiki pages.
User reviews the sweep file and picks rows for a Cursor ingest session.
"""

from __future__ import annotations

import json
import os
import re
import subprocess
import sys
import urllib.error
import urllib.request
from datetime import date, timedelta
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML required — pip install pyyaml", file=sys.stderr)
    sys.exit(1)


def load_exa_key() -> str:
    if os.environ.get("EXA_API_KEY"):
        return os.environ["EXA_API_KEY"].strip()
    path = Path.home() / ".cemini" / "exa-api-key"
    if path.is_file():
        return path.read_text().strip()
    print("ERROR: set EXA_API_KEY or write ~/.cemini/exa-api-key", file=sys.stderr)
    sys.exit(1)


def normalize_url(url: str) -> str:
    u = (url or "").strip().lower().rstrip("/")
    u = re.sub(r"^https?://www\.", "https://", u)
    return u


def exa_search(api_key: str, query: str, from_date: str, category: str | None, num: int) -> dict:
    payload: dict = {
        "query": query,
        "startPublishedDate": from_date,
        "numResults": num,
        "type": "auto",
    }
    if category:
        payload["category"] = category
    body = json.dumps(payload).encode()
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


def title_from_result(r: dict) -> str:
    title = (r.get("title") or "").strip()
    if title:
        return title[:200]
    for line in (r.get("text") or "").splitlines():
        line = line.strip()
        if 30 <= len(line) <= 200 and not line.startswith(("[", "#")):
            return line
    return "(no title)"


def inbox_files(repo: Path) -> list[Path]:
    inbox = repo / "research to be indexed"
    if not inbox.is_dir():
        return []
    return sorted(
        p for p in inbox.iterdir()
        if p.is_file() and not p.name.startswith(".")
    )


def run_preingest(repo: Path) -> str:
    script = repo / "scripts" / "preingest_check.py"
    if not script.is_file():
        return "(preingest_check.py not found)"
    try:
        proc = subprocess.run(
            [sys.executable, str(script)],
            cwd=str(repo),
            capture_output=True,
            text=True,
            timeout=120,
            check=False,
        )
        return (proc.stdout or proc.stderr or "").strip() or "(no output)"
    except subprocess.TimeoutExpired:
        return "(preingest_check timed out after 120s)"
    except OSError as e:
        return f"(preingest_check failed: {e})"


def gap_detect_status(repo: Path) -> tuple[bool, str]:
    meta = repo / "wiki" / "meta" / "wiki-gap-detect-cadence.md"
    if not meta.is_file():
        return False, "no cadence file"
    text = meta.read_text(encoding="utf-8")
    last_m = re.search(r"\|\s*\*\*Last run\*\*\s*\|\s*(\d{4}-\d{2}-\d{2})", text)
    if not last_m:
        return True, "last run unknown — consider running gap detect"
    last = date.fromisoformat(last_m.group(1))
    age = (date.today() - last).days
    due = age >= 7
    msg = f"{age}d since last run ({last.isoformat()})"
    return due, msg


def load_config(repo: Path) -> dict:
    path = repo / "scripts" / "daily_research_config.yaml"
    if not path.is_file():
        print(f"ERROR: missing {path}", file=sys.stderr)
        sys.exit(1)
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def main() -> int:
    repo = Path(__file__).resolve().parent.parent
    cfg = load_config(repo)
    loop = cfg.get("loop") or {}
    window = int(loop.get("recency_window_days", 7))
    per_query = int(loop.get("max_results_per_query", 3))
    today = date.today()
    from_date = (today - timedelta(days=window)).isoformat()

    out_tpl = (cfg.get("output") or {}).get("path_template", "wiki/sweeps/{date}-daily.md")
    report = repo / out_tpl.format(date=today.isoformat())
    report.parent.mkdir(parents=True, exist_ok=True)

    api_key = load_exa_key()
    queries = cfg.get("queries") or []
    active_topics = cfg.get("active_topics") or []
    social = cfg.get("social") or {}

    seen_urls: set[str] = set()
    sections: list[tuple[str, str, str | None, list[dict]]] = []
    partial = False

    for q in queries:
        cluster = q.get("cluster", "unknown")
        query = q.get("query", "")
        category = q.get("category")
        if not query:
            continue
        try:
            data = exa_search(api_key, query, from_date, category, per_query)
            raw = data.get("results") or []
        except urllib.error.HTTPError as e:
            partial = True
            raw = []
            print(f"WARNING: {cluster} HTTP {e.code}", file=sys.stderr)
        except Exception as e:
            partial = True
            raw = []
            print(f"WARNING: {cluster} {e}", file=sys.stderr)

        deduped: list[dict] = []
        for r in raw:
            url = r.get("url") or ""
            key = normalize_url(url)
            if not key or key in seen_urls:
                continue
            seen_urls.add(key)
            deduped.append(r)
        sections.append((cluster, query, category, deduped))

    inbox = inbox_files(repo)
    gap_due, gap_msg = gap_detect_status(repo)
    preingest_out = run_preingest(repo) if inbox else ""

    lines = [
        f"# Daily Research Digest — {today.isoformat()}",
        "",
        f"Discovery-only. Window: `{from_date}` → `{today.isoformat()}` ({window} days). "
        f"{len(queries)} Exa queries × up to {per_query} hits (deduped across queries).",
        "",
        "Reference: `@scripts/daily_research_config.yaml`. **Does NOT ingest.**",
        "",
        "---",
        "",
        "## Active topics (sync from ROADMAP)",
        "",
    ]
    for t in active_topics:
        lines.append(f"- {t}")
    lines.extend(["", "---", ""])

    # Inbox
    lines.extend(["## Inbox (`research to be indexed/`)", ""])
    if inbox:
        lines.append(f"**{len(inbox)} file(s) waiting** — triage before or alongside Exa picks:")
        lines.append("")
        for p in inbox:
            lines.append(f"- `{p.name}`")
        lines.extend(["", "### preingest_check", "", "```", preingest_out[:4000], "```", ""])
    else:
        lines.append("_Empty — no manual drops pending._")
        lines.append("")

    lines.extend(["---", "", "## Exa candidates", ""])

    total = 0
    row_id = 0
    for i, (cluster, query, category, results) in enumerate(sections, 1):
        cat_label = category or "auto"
        lines.append(f"### Q{i}: {cluster} ({len(results)} hits)")
        lines.append("")
        lines.append(f"Query: `{query}` · category: `{cat_label}`")
        lines.append("")
        lines.append("| Pick | Date | Title | Cluster | URL |")
        lines.append("|------|------|-------|---------|-----|")
        for r in results:
            row_id += 1
            url = r.get("url", "")
            d = (r.get("publishedDate") or "")[:10]
            title = title_from_result(r)
            safe_title = title.replace("|", "\\|")[:100]
            lines.append(
                f"| [ ] R{row_id} | {d} | [{safe_title}]({url}) | {cluster} | {url[:60]}… |"
                if len(url) > 60
                else f"| [ ] R{row_id} | {d} | [{safe_title}]({url}) | {cluster} | {url} |"
            )
        lines.append("")
        total += len(results)

    lines.extend(
        [
            "---",
            "",
            "## Wiki gap detect",
            "",
        ]
    )
    if gap_due:
        lines.append(f"**DUE** — {gap_msg}. Run: `bash scripts/run_wiki_gap_detect.sh`")
    else:
        lines.append(f"OK — {gap_msg}.")
    lines.append("")

    manual = social.get("manual_pass") or []
    if manual:
        lines.extend(["---", "", "## Social pass (Cursor session — not automated)", ""])
        for item in manual:
            tool = item.get("tool", "reader")
            prompt = item.get("prompt", "")
            lines.append(f"- **{tool}**: {prompt}")
        lines.append("")

    lines.extend(
        [
            "---",
            "",
            "## Ingest session prompt (copy into Cursor)",
            "",
            "```",
            f"Ingest selected rows from wiki/sweeps/{today.isoformat()}-daily.md:",
            "- Run preingest_check on any new URLs/files",
            "- Deep-read approved candidates; discuss takeaways before writing",
            "- Touch 3–15 wiki pages; lint; update ROADMAP + briefs if prod-touching",
            "```",
            "",
            "---",
            "",
            "## Summary",
            "",
            "| Metric | Count |",
            "|--------|-------|",
            f"| Exa hits (deduped) | {total} |",
            f"| Inbox files | {len(inbox)} |",
            f"| Gap detect due | {'yes' if gap_due else 'no'} |",
            "",
            "### Next steps",
            "",
            "1. Check boxes on rows worth fetching (`R1`, `R2`, …).",
            "2. Optional: run social pass tools above in the same session.",
            "3. Drop PDFs/docx into inbox or fetch URLs via Exa MCP in Cursor.",
            "4. Ingest approved items — do not auto-commit from this script.",
            "",
            f"### Discard",
            "",
            f"`rm wiki/sweeps/{today.isoformat()}-daily.md` if nothing worth acting on.",
            "",
        ]
    )

    report.write_text("\n".join(lines), encoding="utf-8")
    print(f"Report: {report}")

    meta = repo / "wiki" / "meta" / "daily-research-digest-cadence.md"
    if meta.is_file():
        text = meta.read_text(encoding="utf-8")
        text = re.sub(
            r"(\|\s*\*\*Last run\*\*\s*\|\s*)[^\|]+",
            rf"\g<1>{today.isoformat()} ",
            text,
            count=1,
        )
        meta.write_text(text, encoding="utf-8")

    return 3 if partial else 0


if __name__ == "__main__":
    raise SystemExit(main())
