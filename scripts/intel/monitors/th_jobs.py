#!/usr/bin/env python3
"""Target Hospitality (TH) hiring watcher — Tier-A jobs lane.

TH is the closest CXW/GEO operational analog in the government single-buyer
asset-rerating thesis: modular / family-residential housing for ICE & HHS
(Dilley / South Texas Family Residential Center, Pecos Children's Center) on
top of its Permian-Basin workforce-hospitality base. A hiring surge at the
*government / family-residential* sites is a reactivation signal that precedes
occupancy and contract-award disclosure.

TH's careers ATS is UKG/UltiPro (tenant TAR1004TARG). Postings carry named
sites (e.g. "West Texas", "Dilley") rather than lat/lon, so this lane matches
by site/term rather than the geo-cluster model used by the CXW/GEO jobs
monitor. New postings that match a watched government site or term are diffed
against prior state and alerted (Discord).

API: POST https://recruiting2.ultipro.com/<tenant>/JobBoard/<board>/JobBoardView/LoadSearchResults
Concept: wiki/concepts/government-single-buyer-asset-rerating.md
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
from pathlib import Path
from typing import Any

from scripts.intel.core.config import load_yaml
from scripts.intel.core.discord import post_discord, resolve_webhook_url
from scripts.intel.core.http import fetch_json
from scripts.intel.core.state import read_json, write_json
from scripts.intel.paths import report_dir, thesis_config

DEFAULT_THESIS = "gov-asset-rerate"
REPORT_LANE = "gov-asset-th-jobs"
ULTIPRO_HOST = "https://recruiting2.ultipro.com"


def config_path(thesis_id: str = DEFAULT_THESIS) -> Path:
    return thesis_config("th-jobs.yaml", thesis_id=thesis_id)


def load_config(path: Path) -> dict[str, Any]:
    return load_yaml(path)


def search_url(settings: dict[str, Any]) -> str:
    tenant = settings.get("tenant", "TAR1004TARG")
    board = settings["board_id"]
    return f"{ULTIPRO_HOST}/{tenant}/JobBoard/{board}/JobBoardView/LoadSearchResults"


def opportunity_url(settings: dict[str, Any], opp_id: str) -> str:
    tenant = settings.get("tenant", "TAR1004TARG")
    board = settings["board_id"]
    return f"{ULTIPRO_HOST}/{tenant}/JobBoard/{board}/OpportunityDetail?opportunityId={opp_id}"


def build_payload(top: int, skip: int) -> dict[str, Any]:
    return {
        "opportunitySearch": {
            "Top": top,
            "Skip": skip,
            "QueryString": "",
            "OrderBy": [{"Value": "postedDateDesc", "PropertyName": "PostedDate", "Ascending": False}],
            "Filters": [],
        },
        "matchCriteria": {
            "PreferredJobs": [],
            "Educations": [],
            "LicenseAndCertifications": [],
            "Skills": [],
            "hasNoLicenses": False,
            "SkippedSkills": [],
        },
    }


def _location_text(raw: dict[str, Any]) -> str:
    parts: list[str] = []
    for loc in raw.get("Locations") or []:
        if not isinstance(loc, dict):
            continue
        parts.append(str(loc.get("LocalizedName") or ""))
        parts.append(str(loc.get("LocalizedLocationId") or ""))
        addr = loc.get("Address") or {}
        if isinstance(addr, dict):
            parts.append(str(addr.get("City") or ""))
            state = addr.get("State") or {}
            if isinstance(state, dict):
                parts.append(str(state.get("Code") or ""))
    return " ".join(p for p in parts if p)


def parse_opportunity(raw: dict[str, Any], settings: dict[str, Any]) -> dict[str, Any]:
    opp_id = str(raw.get("Id", ""))
    return {
        "id": opp_id,
        "req": raw.get("RequisitionNumber", ""),
        "title": (raw.get("Title") or "").strip(),
        "category": raw.get("JobCategoryName", ""),
        "full_time": bool(raw.get("FullTime")),
        "posted": (raw.get("PostedDate") or "")[:10],
        "brief": (raw.get("BriefDescription") or "").strip(),
        "location": _location_text(raw),
        "url": opportunity_url(settings, opp_id),
    }


def parse_results(response: dict[str, Any], settings: dict[str, Any]) -> list[dict[str, Any]]:
    opps = response.get("opportunities") or response.get("Opportunities") or []
    return [parse_opportunity(o, settings) for o in opps if isinstance(o, dict)]


def _term_hit(haystack: str, term: str) -> bool:
    """Word-boundary match so short tokens like "ICE" don't hit "servICEs"."""
    return re.search(rf"\b{re.escape(term.lower())}\b", haystack) is not None


def match_sites(record: dict[str, Any], target_sites: list[dict[str, Any]]) -> list[str]:
    haystack = f"{record.get('location', '')} {record.get('title', '')} {record.get('brief', '')}".lower()
    matched: list[str] = []
    for site in target_sites:
        terms = site.get("match_terms", [])
        if any(_term_hit(haystack, term) for term in terms):
            matched.append(site.get("id", "site"))
    return matched


def is_relevant(record: dict[str, Any], watch_terms: list[str], matched_sites: list[str]) -> bool:
    if matched_sites:
        return True
    if not watch_terms:
        return False
    haystack = f"{record.get('title', '')} {record.get('category', '')} {record.get('brief', '')} {record.get('location', '')}".lower()
    return any(_term_hit(haystack, term) for term in watch_terms)


def dedupe_new(records: list[dict[str, Any]], seen_ids: set[str]) -> list[dict[str, Any]]:
    new: list[dict[str, Any]] = []
    batch_seen: set[str] = set()
    for rec in records:
        uid = rec.get("id", "")
        if not uid or uid in seen_ids or uid in batch_seen:
            continue
        batch_seen.add(uid)
        new.append(rec)
    return new


def fetch_opportunities(settings: dict[str, Any]) -> list[dict[str, Any]]:
    """Live paged fetch of all TH UltiPro opportunities. Raises on network error."""
    top = int(settings.get("top", 50))
    url = search_url(settings)
    collected: list[dict[str, Any]] = []
    skip = 0
    for _ in range(20):  # hard page cap
        response = fetch_json(url, method="POST", payload=build_payload(top, skip), timeout=45)
        page = parse_results(response, settings)
        collected.extend(page)
        total = int(response.get("totalCount") or response.get("TotalCount") or 0)
        if not page or len(collected) >= total:
            break
        skip += top
    return collected


def render_report(
    *,
    today: dt.date,
    target_sites: list[dict[str, Any]],
    watch_terms: list[str],
    all_records: list[dict[str, Any]],
    new_records: list[dict[str, Any]],
    first_run: bool,
    error: str | None,
) -> str:
    def relevant(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
        out = []
        for r in records:
            ms = match_sites(r, target_sites)
            if is_relevant(r, watch_terms, ms):
                r = dict(r, matched_sites=ms)
                out.append(r)
        return out

    lines = [
        f"# Target Hospitality hiring sweep — {today.isoformat()}",
        "",
        "## Query",
        "",
        f"- Openings fetched: {len(all_records)}",
        f"- Target sites: {', '.join(s.get('id', '?') for s in target_sites)}",
        f"- Watch terms: {', '.join(watch_terms) if watch_terms else 'none'}",
        "",
        "## New government / family-residential-relevant postings",
        "",
    ]
    new_relevant = relevant(new_records)
    if first_run:
        lines.append("First run: baseline stored (new postings suppressed to avoid backfill spam).")
    elif not new_relevant:
        lines.append("No new government/family-residential-relevant TH postings since previous run.")
    else:
        lines.append("| Posted | Title | Category | Site match | Location | Req |")
        lines.append("|---|---|---|---|---|---|")
        for r in sorted(new_relevant, key=lambda x: x.get("posted", ""), reverse=True):
            sites = ", ".join(r.get("matched_sites", [])) or "term"
            lines.append(
                f"| {r.get('posted','')} | [{r.get('title','')[:60]}]({r.get('url','')}) | "
                f"{r.get('category','')} | {sites} | {r.get('location','')[:40]} | `{r.get('req','')}` |"
            )

    site_hits = relevant(all_records)
    lines.extend(["", "## All target-site / watch-term postings this run", ""])
    if not site_hits:
        lines.append("No government/family-residential-relevant TH postings in current board.")
    else:
        for r in sorted(site_hits, key=lambda x: x.get("posted", ""), reverse=True):
            sites = ", ".join(r.get("matched_sites", [])) or "term"
            lines.append(f"- {r.get('posted','')} · {r.get('title','')} · _{sites}_ · {r.get('location','')[:40]}")

    if error:
        lines.extend(["", "## Errors", "", f"- {error}"])
    lines.append("")
    return "\n".join(lines)


def send_alert(new_relevant: list[dict[str, Any]], report_path: Path) -> int:
    webhook_url = resolve_webhook_url()
    if not webhook_url:
        return 0
    top = new_relevant[:8]
    desc = "\n".join(
        f"{r.get('posted','')} · {r.get('title','')[:60]} · {', '.join(r.get('matched_sites', [])) or 'term'}"
        for r in top
    )
    post_discord(
        webhook_url,
        content=f"**Target Hospitality — {len(new_relevant)} new gov/family-residential posting(s)**",
        embeds=[
            {
                "title": "TH hiring watch (Tier-A)",
                "description": f"{desc}\n\nReport: `{report_path}`",
                "color": 0x16A085,
            }
        ],
        username="Cemini TH Jobs Watch",
    )
    return 1


def run(
    config_file: Path,
    today: dt.date,
    *,
    notify: bool = False,
    offline_records: list[dict[str, Any]] | None = None,
) -> dict[str, Any]:
    config = load_config(config_file)
    settings = config.get("settings", {})
    target_sites: list[dict[str, Any]] = list(config.get("target_sites", []))
    watch_terms = [str(t) for t in config.get("watch_terms", [])]

    report_path = report_dir(REPORT_LANE) / f"{today.isoformat()}-th-jobs-sweep.md"
    state_path = report_dir(REPORT_LANE) / "last_run_state.json"
    state = read_json(state_path, {})
    seen_ids = set(state.get("seen_ids", []))
    first_run = not state

    all_records: list[dict[str, Any]] = []
    error: str | None = None
    try:
        if offline_records is not None:
            all_records = [parse_opportunity(r, settings) if "Id" in r else r for r in offline_records]
        else:
            all_records = fetch_opportunities(settings)
    except Exception as exc:  # noqa: BLE001
        error = str(exc)

    new_records = dedupe_new(all_records, seen_ids)
    new_relevant = [
        dict(r, matched_sites=match_sites(r, target_sites))
        for r in new_records
        if is_relevant(r, watch_terms, match_sites(r, target_sites))
    ]

    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(
        render_report(
            today=today,
            target_sites=target_sites,
            watch_terms=watch_terms,
            all_records=all_records,
            new_records=new_records,
            first_run=first_run,
            error=error,
        ),
        encoding="utf-8",
    )

    alerts = 0
    if notify and new_relevant and not first_run and settings.get("alert_on_new", True):
        alerts = send_alert(new_relevant, report_path)

    write_json(
        state_path,
        {
            "last_run": today.isoformat(),
            "seen_ids": sorted(seen_ids | {r["id"] for r in all_records if r.get("id")}),
            "last_report": str(report_path),
            "last_new_relevant": len(new_relevant),
        },
    )
    return {
        "report_path": report_path,
        "all_records": all_records,
        "new_records": new_records,
        "new_relevant": new_relevant,
        "error": error,
        "alerts": alerts,
        "first_run": first_run,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--thesis", default=DEFAULT_THESIS, help="Thesis id (config dir under config/theses/).")
    parser.add_argument("--config", type=Path, default=None, help="Explicit config path (overrides --thesis).")
    parser.add_argument("--date", default=dt.date.today().isoformat())
    parser.add_argument("--notify", action="store_true", help="Discord alert on new relevant postings.")
    args = parser.parse_args()

    cfg = args.config or config_path(args.thesis)
    today = dt.date.fromisoformat(args.date)
    result = run(cfg, today, notify=args.notify)
    print(f"Report: {result['report_path']}")
    print(f"Openings fetched: {len(result['all_records'])}")
    print(f"New relevant postings: {len(result['new_relevant'])}")
    if result["first_run"]:
        print("First run: baseline stored.")
    if result["error"]:
        print(f"Error: {result['error']}")
    if result["alerts"]:
        print(f"Discord alerts sent: {result['alerts']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
