#!/usr/bin/env python3
"""DoD / DOE catalyst watcher — Federal Register (keyless) lane.

Queries the Federal Register documents API for DoD/DOE re-rate catalysts —
Defense Production Act Title III determinations, offtake / price-floor /
strategic-reserve rules, minerals & uranium procurement notices — diffs
against prior state, and alerts (Discord) on NEW documents.

Lead time: days–weeks (rules/notices publish ahead of award flow). This is
lane 3 in the government single-buyer asset-rerating monitor map, aimed at
Tier-B critical-minerals / nuclear-fuel names (MP, USAR, PPTA, LAC, LEU).

API: GET https://www.federalregister.gov/api/v1/documents.json
Concept: wiki/concepts/government-single-buyer-asset-rerating.md
"""

from __future__ import annotations

import argparse
import datetime as dt
import urllib.parse
from pathlib import Path
from typing import Any

from scripts.intel.core.config import load_yaml
from scripts.intel.core.discord import post_discord, resolve_webhook_url
from scripts.intel.core.http import fetch_json
from scripts.intel.core.state import read_json, write_json
from scripts.intel.paths import report_dir, thesis_config

DEFAULT_THESIS = "gov-asset-rerate"
FEDREG_ENDPOINT = "https://www.federalregister.gov/api/v1/documents.json"
REPORT_LANE = "gov-asset-fedreg"
DOC_FIELDS = ["title", "document_number", "publication_date", "html_url", "type", "abstract"]


def config_path(thesis_id: str = DEFAULT_THESIS) -> Path:
    return thesis_config("fedreg.yaml", thesis_id=thesis_id)


def load_config(path: Path) -> dict[str, Any]:
    return load_yaml(path)


def build_query_url(
    query: dict[str, Any],
    *,
    startdt: str,
    enddt: str,
    settings: dict[str, Any],
) -> str:
    """Build a Federal Register documents.json request URL from a config query."""
    params: list[tuple[str, str]] = [
        ("per_page", str(settings.get("per_page", 20))),
        ("order", "newest"),
        ("conditions[term]", str(query.get("term", ""))),
        ("conditions[publication_date][gte]", startdt),
        ("conditions[publication_date][lte]", enddt),
    ]
    agencies = query.get("agencies") or settings.get("default_agencies") or []
    for agency in agencies:
        params.append(("conditions[agencies][]", str(agency)))
    for doc_type in query.get("type", []) or []:
        params.append(("conditions[type][]", str(doc_type)))
    for field in DOC_FIELDS:
        params.append(("fields[]", field))
    return FEDREG_ENDPOINT + "?" + urllib.parse.urlencode(params)


def parse_documents(response: dict[str, Any], query_id: str) -> list[dict[str, Any]]:
    """Flatten a Federal Register documents response into records."""
    docs: list[dict[str, Any]] = []
    for raw in response.get("results", []):
        docs.append(
            {
                "id": str(raw.get("document_number", "")),
                "query": query_id,
                "title": (raw.get("title") or "").strip(),
                "date": raw.get("publication_date", ""),
                "type": raw.get("type", ""),
                "url": raw.get("html_url", ""),
                "abstract": (raw.get("abstract") or "").strip(),
            }
        )
    return docs


def is_watched(doc: dict[str, Any], watch_terms: list[str]) -> bool:
    if not watch_terms:
        return False
    haystack = f"{doc.get('title', '')} {doc.get('abstract', '')}".lower()
    return any(term.lower() in haystack for term in watch_terms)


def dedupe_new(docs: list[dict[str, Any]], seen_ids: set[str]) -> list[dict[str, Any]]:
    new: list[dict[str, Any]] = []
    batch_seen: set[str] = set()
    for doc in docs:
        uid = doc.get("id", "")
        if not uid or uid in seen_ids or uid in batch_seen:
            continue
        batch_seen.add(uid)
        new.append(doc)
    return new


def search_query(
    query: dict[str, Any],
    *,
    startdt: str,
    enddt: str,
    settings: dict[str, Any],
) -> list[dict[str, Any]]:
    """Live Federal Register query for one config entry. Raises on network error."""
    url = build_query_url(query, startdt=startdt, enddt=enddt, settings=settings)
    response = fetch_json(url, timeout=45)
    return parse_documents(response, query.get("id", "query"))


def render_report(
    *,
    today: dt.date,
    startdt: str,
    enddt: str,
    queries: list[dict[str, Any]],
    all_docs: list[dict[str, Any]],
    new_docs: list[dict[str, Any]],
    watch_terms: list[str],
    errors: list[str],
    first_run: bool,
) -> str:
    lines = [
        f"# DoD/DOE catalyst sweep (Federal Register) — {today.isoformat()}",
        "",
        "## Query",
        "",
        f"- Window: {startdt} → {enddt}",
        f"- Queries: {', '.join(q.get('id', '?') for q in queries)}",
        f"- Endpoint: {FEDREG_ENDPOINT}",
        f"- Watch terms: {', '.join(watch_terms) if watch_terms else 'none'}",
        "",
        "## New documents",
        "",
    ]
    if first_run:
        lines.append("First run: baseline stored (new documents suppressed to avoid backfill spam).")
    elif not new_docs:
        lines.append("No new matching documents since previous run.")
    else:
        lines.append("| Date | Type | Title | Query | Doc # |")
        lines.append("|---|---|---|---|---|")
        for d in sorted(new_docs, key=lambda r: r.get("date", ""), reverse=True):
            star = " ⭐" if is_watched(d, watch_terms) else ""
            title = d.get("title", "").replace("|", "\\|")[:90]
            lines.append(
                f"| {d.get('date', '')} | {d.get('type', '')} | [{title}]({d.get('url', '')}){star} "
                f"| {d.get('query', '')} | `{d.get('id', '')}` |"
            )

    watched = [d for d in all_docs if is_watched(d, watch_terms)]
    lines.extend(["", "## Watched-term matches this window", ""])
    if not watched:
        lines.append("No watched-term documents in window.")
    else:
        for d in sorted(watched, key=lambda r: r.get("date", ""), reverse=True):
            title = d.get("title", "")[:90]
            lines.append(f"- {d.get('date', '')} · {d.get('type', '')} · [{title}]({d.get('url', '')}) · _{d.get('query', '')}_")

    if errors:
        lines.extend(["", "## Errors", ""])
        lines.extend(f"- {e}" for e in errors)
    lines.append("")
    return "\n".join(lines)


def send_alert(new_docs: list[dict[str, Any]], watch_terms: list[str], report_path: Path) -> int:
    webhook_url = resolve_webhook_url()
    if not webhook_url:
        return 0
    top = new_docs[:8]
    desc = "\n".join(
        f"{d.get('date','')} · {d.get('type','')} · {d.get('title','')[:80]}"
        f"{' ⭐' if is_watched(d, watch_terms) else ''} (_{d.get('query','')}_)"
        for d in top
    )
    post_discord(
        webhook_url,
        content=f"**DoD/DOE catalysts — {len(new_docs)} new Federal Register doc(s)**",
        embeds=[
            {
                "title": "Federal Register DoD/DOE watcher",
                "description": f"{desc}\n\nReport: `{report_path}`",
                "color": 0x8E44AD,
            }
        ],
        username="Cemini DoD/DOE Watch",
    )
    return 1


def run(
    config_file: Path,
    today: dt.date,
    *,
    notify: bool = False,
    offline_payloads: dict[str, dict[str, Any]] | None = None,
) -> dict[str, Any]:
    config = load_config(config_file)
    settings = config.get("settings", {})
    queries: list[dict[str, Any]] = list(config.get("queries", []))
    watch_terms = [str(t) for t in config.get("watch_terms", [])]
    lookback = int(settings.get("lookback_days", 30))

    startdt = (today - dt.timedelta(days=lookback)).isoformat()
    enddt = today.isoformat()

    report_path = report_dir(REPORT_LANE) / f"{today.isoformat()}-fedreg-sweep.md"
    state_path = report_dir(REPORT_LANE) / "last_run_state.json"
    state = read_json(state_path, {})
    seen_ids = set(state.get("seen_ids", []))
    first_run = not state

    all_docs: list[dict[str, Any]] = []
    errors: list[str] = []
    for query in queries:
        qid = query.get("id", "query")
        try:
            if offline_payloads is not None:
                docs = parse_documents(offline_payloads.get(qid, {}), qid)
            else:
                docs = search_query(query, startdt=startdt, enddt=enddt, settings=settings)
        except Exception as exc:  # noqa: BLE001
            errors.append(f"{qid}: {exc}")
            continue
        all_docs.extend(docs)

    new_docs = dedupe_new(all_docs, seen_ids)

    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(
        render_report(
            today=today,
            startdt=startdt,
            enddt=enddt,
            queries=queries,
            all_docs=all_docs,
            new_docs=new_docs,
            watch_terms=watch_terms,
            errors=errors,
            first_run=first_run,
        ),
        encoding="utf-8",
    )

    alerts = 0
    if notify and new_docs and not first_run and settings.get("alert_on_new", True):
        alerts = send_alert(new_docs, watch_terms, report_path)

    write_json(
        state_path,
        {
            "last_run": today.isoformat(),
            "seen_ids": sorted(seen_ids | {d["id"] for d in all_docs if d.get("id")}),
            "last_report": str(report_path),
            "last_new_count": len(new_docs),
        },
    )
    return {
        "report_path": report_path,
        "all_docs": all_docs,
        "new_docs": new_docs,
        "errors": errors,
        "alerts": alerts,
        "first_run": first_run,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--thesis", default=DEFAULT_THESIS, help="Thesis id (config dir under config/theses/).")
    parser.add_argument("--config", type=Path, default=None, help="Explicit config path (overrides --thesis).")
    parser.add_argument("--date", default=dt.date.today().isoformat())
    parser.add_argument("--notify", action="store_true", help="Discord alert on new documents.")
    args = parser.parse_args()

    cfg = args.config or config_path(args.thesis)
    today = dt.date.fromisoformat(args.date)
    result = run(cfg, today, notify=args.notify)
    print(f"Report: {result['report_path']}")
    print(f"Docs this window: {len(result['all_docs'])}")
    print(f"New docs: {len(result['new_docs'])}")
    if result["first_run"]:
        print("First run: baseline stored.")
    if result["errors"]:
        print(f"Errors: {len(result['errors'])}")
        for err in result["errors"]:
            print(f"  - {err}")
    if result["alerts"]:
        print(f"Discord alerts sent: {result['alerts']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
