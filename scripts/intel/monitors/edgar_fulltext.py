#!/usr/bin/env python3
"""SEC EDGAR full-text watcher — coincident (day-of) filing catch.

Queries the EDGAR full-text search API (efts.sec.gov) for thesis phrases
("turnkey", "definitive agreement", "sale of facility", …) over a recent
date window, optionally filtered to watched CIKs/tickers and form types,
diffs against prior state, and alerts (Discord) on NEW filings.

This is the highest-value cheap lane for the government single-buyer
asset-rerating thesis: it would have flagged CoreCivic's Jul 6 8-K the
same day, unlike the lagging county-recorder lane.

Docs: https://efts.sec.gov/LATEST/search-index?q=...
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
EFTS_ENDPOINT = "https://efts.sec.gov/LATEST/search-index"
# SEC fair-access policy requires a descriptive UA with a contact.
SEC_USER_AGENT = "Cemini OSINT Research edgar-monitor (admin@cemini.local)"
REPORT_LANE = "gov-asset-edgar"


def config_path(thesis_id: str = DEFAULT_THESIS) -> Path:
    return thesis_config("edgar-fulltext.yaml", thesis_id=thesis_id)


def load_config(path: Path) -> dict[str, Any]:
    return load_yaml(path)


def build_efts_url(
    term: str,
    *,
    forms: list[str] | None = None,
    startdt: str = "",
    enddt: str = "",
    ciks: list[str] | None = None,
) -> str:
    """Build an EDGAR full-text search request URL.

    ``term`` is wrapped in double quotes to force an exact-phrase match.
    """
    params: dict[str, str] = {"q": f'"{term}"'}
    if forms:
        params["forms"] = ",".join(forms)
    if startdt and enddt:
        params["dateRange"] = "custom"
        params["startdt"] = startdt
        params["enddt"] = enddt
    if ciks:
        params["ciks"] = ",".join(ciks)
    return f"{EFTS_ENDPOINT}?{urllib.parse.urlencode(params)}"


def parse_efts_hits(payload: dict[str, Any], term: str) -> list[dict[str, Any]]:
    """Flatten an EDGAR full-text search JSON response into hit records."""
    hits: list[dict[str, Any]] = []
    for hit in payload.get("hits", {}).get("hits", []):
        source = hit.get("_source", {}) or {}
        hits.append(
            {
                "id": hit.get("_id", ""),
                "term": term,
                "form": source.get("root_forms", [source.get("form", "")])[0]
                if source.get("root_forms")
                else source.get("form", ""),
                "file_date": source.get("file_date", ""),
                "display_names": source.get("display_names", []),
                "ciks": source.get("ciks", []),
            }
        )
    return hits


def matches_watch(hit: dict[str, Any], watch_ciks: set[str], watch_names: list[str]) -> bool:
    """True if no watch filter set, or the hit matches a watched CIK / name substring."""
    if not watch_ciks and not watch_names:
        return True
    hit_ciks = {str(c).lstrip("0") for c in hit.get("ciks", [])}
    if watch_ciks & hit_ciks:
        return True
    joined = " ".join(hit.get("display_names", [])).upper()
    return any(name.upper() in joined for name in watch_names)


def filter_hits(hits: list[dict[str, Any]], watch_ciks: set[str], watch_names: list[str]) -> list[dict[str, Any]]:
    return [h for h in hits if matches_watch(h, watch_ciks, watch_names)]


def dedupe_new(hits: list[dict[str, Any]], seen_ids: set[str]) -> list[dict[str, Any]]:
    """Return hits whose id has not been seen, de-duplicated within this batch."""
    new: list[dict[str, Any]] = []
    batch_seen: set[str] = set()
    for hit in hits:
        hid = hit.get("id", "")
        if not hid or hid in seen_ids or hid in batch_seen:
            continue
        batch_seen.add(hid)
        new.append(hit)
    return new


def search_term(
    term: str,
    *,
    forms: list[str],
    startdt: str,
    enddt: str,
    ciks: list[str] | None = None,
) -> list[dict[str, Any]]:
    """Live EFTS query for a single phrase. Raises on network error."""
    url = build_efts_url(term, forms=forms, startdt=startdt, enddt=enddt, ciks=ciks)
    payload = fetch_json(url, user_agent=SEC_USER_AGENT, timeout=45)
    return parse_efts_hits(payload, term)


def render_report(
    *,
    today: dt.date,
    startdt: str,
    enddt: str,
    forms: list[str],
    terms: list[str],
    all_hits: list[dict[str, Any]],
    new_hits: list[dict[str, Any]],
    errors: list[str],
    first_run: bool,
) -> str:
    lines = [
        f"# EDGAR full-text sweep — {today.isoformat()}",
        "",
        "## Query",
        "",
        f"- Window: {startdt} → {enddt}",
        f"- Forms: {', '.join(forms) if forms else 'any'}",
        f"- Terms: {', '.join(terms)}",
        f"- Endpoint: {EFTS_ENDPOINT}",
        "",
        "## New filings",
        "",
    ]
    if first_run:
        lines.append("First run: baseline stored (new filings suppressed to avoid backfill spam).")
    elif not new_hits:
        lines.append("No new matching filings since previous run.")
    else:
        lines.append("| Date | Form | Filer | Term | Accession |")
        lines.append("|---|---|---|---|---|")
        for h in sorted(new_hits, key=lambda r: r.get("file_date", ""), reverse=True):
            names = "; ".join(h.get("display_names", [])) or "?"
            lines.append(
                f"| {h.get('file_date', '')} | {h.get('form', '')} | {names} | {h.get('term', '')} | `{h.get('id', '')}` |"
            )

    lines.extend(["", "## All matches this window", ""])
    if not all_hits:
        lines.append("No matches in window.")
    else:
        for h in sorted(all_hits, key=lambda r: r.get("file_date", ""), reverse=True):
            names = "; ".join(h.get("display_names", [])) or "?"
            lines.append(f"- {h.get('file_date', '')} · {h.get('form', '')} · {names} · _{h.get('term', '')}_")

    if errors:
        lines.extend(["", "## Errors", ""])
        lines.extend(f"- {e}" for e in errors)
    lines.append("")
    return "\n".join(lines)


def send_alert(new_hits: list[dict[str, Any]], report_path: Path) -> int:
    webhook_url = resolve_webhook_url()
    if not webhook_url:
        return 0
    top = new_hits[:8]
    desc = "\n".join(
        f"{h.get('file_date','')} · {h.get('form','')} · {'; '.join(h.get('display_names', [])) or '?'} (_{h.get('term','')}_)"
        for h in top
    )
    post_discord(
        webhook_url,
        content=f"**EDGAR full-text — {len(new_hits)} new thesis filing(s)**",
        embeds=[
            {
                "title": "SEC EDGAR full-text watcher",
                "description": f"{desc}\n\nReport: `{report_path}`",
                "color": 0x3498DB,
            }
        ],
        username="Cemini EDGAR Watch",
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
    terms: list[str] = list(config.get("query_terms", []))
    forms: list[str] = list(settings.get("forms", ["8-K"]))
    lookback = int(settings.get("lookback_days", 3))
    watch_ciks = {str(c).lstrip("0") for c in config.get("watch_ciks", [])}
    watch_names = [str(n) for n in config.get("watch_names", [])]
    watch_cik_list = [str(c) for c in config.get("watch_ciks", [])] or None

    startdt = (today - dt.timedelta(days=lookback)).isoformat()
    enddt = today.isoformat()

    report_path = report_dir(REPORT_LANE) / f"{today.isoformat()}-edgar-sweep.md"
    state_path = report_dir(REPORT_LANE) / "last_run_state.json"
    state = read_json(state_path, {})
    seen_ids = set(state.get("seen_ids", []))
    first_run = not state

    all_hits: list[dict[str, Any]] = []
    errors: list[str] = []
    for term in terms:
        try:
            if offline_payloads is not None:
                hits = parse_efts_hits(offline_payloads.get(term, {}), term)
            else:
                hits = search_term(
                    term, forms=forms, startdt=startdt, enddt=enddt, ciks=watch_cik_list
                )
        except Exception as exc:  # noqa: BLE001
            errors.append(f"{term}: {exc}")
            continue
        all_hits.extend(filter_hits(hits, watch_ciks, watch_names))

    new_hits = dedupe_new(all_hits, seen_ids)

    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(
        render_report(
            today=today,
            startdt=startdt,
            enddt=enddt,
            forms=forms,
            terms=terms,
            all_hits=all_hits,
            new_hits=new_hits,
            errors=errors,
            first_run=first_run,
        ),
        encoding="utf-8",
    )

    alerts = 0
    if notify and new_hits and not first_run:
        alerts = send_alert(new_hits, report_path)

    write_json(
        state_path,
        {
            "last_run": today.isoformat(),
            "seen_ids": sorted(seen_ids | {h["id"] for h in all_hits if h.get("id")}),
            "last_report": str(report_path),
            "last_new_count": len(new_hits),
        },
    )
    return {
        "report_path": report_path,
        "all_hits": all_hits,
        "new_hits": new_hits,
        "errors": errors,
        "alerts": alerts,
        "first_run": first_run,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--thesis", default=DEFAULT_THESIS, help="Thesis id (config dir under config/theses/).")
    parser.add_argument("--config", type=Path, default=None, help="Explicit config path (overrides --thesis).")
    parser.add_argument("--date", default=dt.date.today().isoformat())
    parser.add_argument("--notify", action="store_true", help="Discord alert on new filings.")
    args = parser.parse_args()

    cfg = args.config or config_path(args.thesis)
    today = dt.date.fromisoformat(args.date)
    result = run(cfg, today, notify=args.notify)
    print(f"Report: {result['report_path']}")
    print(f"Matches this window: {len(result['all_hits'])}")
    print(f"New filings: {len(result['new_hits'])}")
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
