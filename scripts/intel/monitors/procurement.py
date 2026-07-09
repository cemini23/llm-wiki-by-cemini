#!/usr/bin/env python3
"""Federal procurement watcher — earliest (pre-deal diligence) lane.

Queries the USASpending.gov award-search API (keyless) for pre-close
diligence signals — appraisal, escrow, title, survey, environmental-site
awards tied to target operators/agencies — diffs against prior state, and
alerts (Discord) on NEW awards.

This is the *earliest* lane in the government single-buyer asset-rerating
monitor map: title/escrow/appraisal spend precedes a facility sale by weeks
to months. Precedent signal shape: First American title/escrow J&A for
Florence/Krome/Batavia (@sources/ice-ja-26-0143-first-american-escrow-2026).

SAM.gov contract-opportunities is a documented extension but requires an API
key (data.gov registration); USASpending needs none, so it is the default.

API: POST https://api.usaspending.gov/api/v2/search/spending_by_award/
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
USASPENDING_ENDPOINT = "https://api.usaspending.gov/api/v2/search/spending_by_award/"
REPORT_LANE = "gov-asset-procurement"
AWARD_FIELDS = [
    "Award ID",
    "Recipient Name",
    "Awarding Agency",
    "Awarding Sub Agency",
    "Award Amount",
    "Start Date",
    "Description",
    "Award Type",
]


def config_path(thesis_id: str = DEFAULT_THESIS) -> Path:
    return thesis_config("usaspending.yaml", thesis_id=thesis_id)


def load_config(path: Path) -> dict[str, Any]:
    return load_yaml(path)


def build_payload(
    query: dict[str, Any],
    *,
    startdt: str,
    enddt: str,
    settings: dict[str, Any],
) -> dict[str, Any]:
    """Build a USASpending spending_by_award request body from a config query."""
    filters: dict[str, Any] = {
        "time_period": [{"start_date": startdt, "end_date": enddt}],
        "award_type_codes": list(settings.get("award_type_codes", ["A", "B", "C", "D"])),
    }
    keywords = query.get("keywords")
    if keywords:
        filters["keywords"] = list(keywords)
    recipient = query.get("recipient")
    if recipient:
        filters["recipient_search_text"] = [recipient] if isinstance(recipient, str) else list(recipient)
    agencies = query.get("agencies")
    if agencies:
        filters["agencies"] = [
            {"type": "awarding", "tier": "toptier", "name": name} for name in agencies
        ]
    return {
        "filters": filters,
        "fields": AWARD_FIELDS,
        "page": 1,
        "limit": int(settings.get("limit", 100)),
        "sort": "Award Amount",
        "order": "desc",
    }


def _normalize_key(value: str) -> str:
    return value.strip().upper()


def migrate_seen_id(uid: str) -> str:
    """Map legacy USASpending keys (CONT_AWD_* / numeric internal_id) to PIID."""
    key = _normalize_key(uid)
    if key.startswith("CONT_AWD_"):
        piid = key.removeprefix("CONT_AWD_").split("_", 1)[0]
        if piid:
            return piid
    return key


def award_uid(raw: dict[str, Any]) -> str:
    """Stable dedupe key — PIID (Award ID), not generated_internal_id."""
    award_id = raw.get("Award ID")
    if award_id:
        return _normalize_key(str(award_id))
    legacy = raw.get("generated_internal_id") or raw.get("internal_id")
    if legacy:
        return migrate_seen_id(str(legacy))
    return ""


def canonical_award_key(award: dict[str, Any]) -> str:
    award_id = award.get("award_id")
    if award_id:
        return _normalize_key(str(award_id))
    return migrate_seen_id(str(award.get("id") or ""))


def parse_awards(response: dict[str, Any], query_id: str) -> list[dict[str, Any]]:
    """Flatten a USASpending award-search response into records."""
    awards: list[dict[str, Any]] = []
    for raw in response.get("results", []):
        awards.append(
            {
                "id": award_uid(raw),
                "query": query_id,
                "award_id": raw.get("Award ID", ""),
                "recipient": raw.get("Recipient Name", ""),
                "agency": raw.get("Awarding Agency", ""),
                "sub_agency": raw.get("Awarding Sub Agency", ""),
                "amount": raw.get("Award Amount"),
                "start_date": raw.get("Start Date", ""),
                "description": (raw.get("Description") or "").strip(),
                "award_type": raw.get("Award Type", ""),
            }
        )
    return awards


def is_watched_recipient(award: dict[str, Any], watch_recipients: list[str]) -> bool:
    if not watch_recipients:
        return False
    recipient = (award.get("recipient") or "").upper()
    return any(w.upper() in recipient for w in watch_recipients)


def _award_text(award: dict[str, Any]) -> str:
    return " ".join(
        str(award.get(field) or "")
        for field in ("description", "award_type", "recipient", "award_id")
    ).lower()


def is_operator_recipient(award: dict[str, Any], operator_recipients: list[str]) -> bool:
    if not operator_recipients:
        return False
    recipient = (award.get("recipient") or "").upper()
    return any(op.upper() in recipient for op in operator_recipients)


def is_detention_ops_noise(award: dict[str, Any], suppress_patterns: list[str]) -> bool:
    if not suppress_patterns:
        return False
    text = _award_text(award)
    return any(pattern.lower() in text for pattern in suppress_patterns)


def has_diligence_terms(award: dict[str, Any], diligence_terms: list[str]) -> bool:
    if not diligence_terms:
        return True
    text = _award_text(award)
    for term in diligence_terms:
        if " " in term.strip():
            if term.lower() in text:
                return True
        elif re.search(rf"\b{re.escape(term.lower())}\b", text):
            return True
    return False


def _award_amount(award: dict[str, Any]) -> float | None:
    try:
        return float(award.get("amount"))
    except (TypeError, ValueError):
        return None


def passes_min_amount(award: dict[str, Any], min_amount: float | None) -> bool:
    if min_amount is None:
        return True
    amount = _award_amount(award)
    if amount is None:
        return False
    return amount >= min_amount


def matches_sub_agency(
    award: dict[str, Any],
    *,
    include: list[str] | None = None,
    exclude: list[str] | None = None,
) -> bool:
    sub = (award.get("sub_agency") or "").upper()
    if exclude and any(ex.upper() in sub for ex in exclude):
        return False
    if include:
        return any(inc.upper() in sub for inc in include)
    return True


def apply_query_filters(award: dict[str, Any], query: dict[str, Any]) -> bool:
    """Post-parse filters from per-query config (sub-agency, min amount)."""
    if not passes_min_amount(award, query.get("min_amount")):
        return False
    return matches_sub_agency(
        award,
        include=query.get("include_sub_agencies"),
        exclude=query.get("exclude_sub_agencies"),
    )


def is_alertable_award(award: dict[str, Any], config: dict[str, Any], queries_by_id: dict[str, dict[str, Any]]) -> bool:
    """Return True when an award is thesis-relevant enough to alert on."""
    settings = config.get("settings", {})
    watch_recipients = [str(r) for r in config.get("watch_recipients", [])]
    operator_recipients = [str(r) for r in settings.get("operator_recipients", [])]
    diligence_terms = [str(t) for t in settings.get("diligence_terms", [])]
    suppress_patterns = [str(p) for p in settings.get("suppress_description_patterns", [])]

    if is_detention_ops_noise(award, suppress_patterns):
        return False

    query = queries_by_id.get(str(award.get("query", "")))
    if query and not apply_query_filters(award, query):
        return False

    if query and query.get("require_diligence_terms"):
        return has_diligence_terms(award, diligence_terms)

    if is_watched_recipient(award, watch_recipients):
        return True

    if is_operator_recipient(award, operator_recipients):
        return has_diligence_terms(award, diligence_terms)

    return True


def partition_alertable(
    awards: list[dict[str, Any]], config: dict[str, Any], queries: list[dict[str, Any]]
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    queries_by_id = {str(q.get("id", "")): q for q in queries}
    alertable: list[dict[str, Any]] = []
    suppressed: list[dict[str, Any]] = []
    for award in awards:
        if is_alertable_award(award, config, queries_by_id):
            alertable.append(award)
        else:
            suppressed.append(award)
    return alertable, suppressed


def dedupe_new(awards: list[dict[str, Any]], seen_ids: set[str]) -> list[dict[str, Any]]:
    seen = {migrate_seen_id(uid) for uid in seen_ids if uid}
    new: list[dict[str, Any]] = []
    batch_seen: set[str] = set()
    for award in awards:
        key = canonical_award_key(award)
        if not key or key in seen or key in batch_seen:
            continue
        batch_seen.add(key)
        new.append(award)
    return new


def search_query(
    query: dict[str, Any],
    *,
    startdt: str,
    enddt: str,
    settings: dict[str, Any],
) -> list[dict[str, Any]]:
    """Live USASpending query for one config entry. Raises on network error."""
    payload = build_payload(query, startdt=startdt, enddt=enddt, settings=settings)
    response = fetch_json(USASPENDING_ENDPOINT, method="POST", payload=payload, timeout=45)
    awards = parse_awards(response, query.get("id", "query"))
    return [a for a in awards if apply_query_filters(a, query)]


def _fmt_amount(amount: Any) -> str:
    try:
        return f"${float(amount):,.0f}"
    except (TypeError, ValueError):
        return "n/a"


def render_report(
    *,
    today: dt.date,
    startdt: str,
    enddt: str,
    queries: list[dict[str, Any]],
    all_awards: list[dict[str, Any]],
    new_awards: list[dict[str, Any]],
    suppressed_awards: list[dict[str, Any]],
    watch_recipients: list[str],
    errors: list[str],
    first_run: bool,
) -> str:
    lines = [
        f"# Federal procurement sweep (USASpending) — {today.isoformat()}",
        "",
        "## Query",
        "",
        f"- Window: {startdt} → {enddt}",
        f"- Queries: {', '.join(q.get('id', '?') for q in queries)}",
        f"- Endpoint: {USASPENDING_ENDPOINT}",
        f"- Watch recipients: {', '.join(watch_recipients) if watch_recipients else 'none'}",
        "",
        "## New awards",
        "",
    ]
    if first_run:
        lines.append("First run: baseline stored (new awards suppressed to avoid backfill spam).")
    elif not new_awards:
        lines.append("No new diligence-relevant awards since previous run.")
    else:
        lines.append("| Start | Amount | Recipient | Agency / sub | Query | Award ID |")
        lines.append("|---|---:|---|---|---|---|")
        for a in sorted(new_awards, key=lambda r: r.get("start_date", ""), reverse=True):
            star = " ⭐" if is_watched_recipient(a, watch_recipients) else ""
            agency = f"{a.get('agency', '')} / {a.get('sub_agency', '')}".strip(" /")
            lines.append(
                f"| {a.get('start_date', '')} | {_fmt_amount(a.get('amount'))} | "
                f"{a.get('recipient', '')}{star} | {agency} | {a.get('query', '')} | `{a.get('award_id', '')}` |"
            )

    lines.extend(["", "## Suppressed (detention ops noise)", ""])
    if not suppressed_awards:
        lines.append("No new operator detention-services task orders filtered this run.")
    else:
        for a in sorted(suppressed_awards, key=lambda r: r.get("start_date", ""), reverse=True)[:15]:
            lines.append(
                f"- {a.get('start_date', '')} · {_fmt_amount(a.get('amount'))} · "
                f"{a.get('recipient', '')} · `{a.get('award_id', '')}` · _{a.get('query', '')}_"
            )

    watched = [a for a in all_awards if is_watched_recipient(a, watch_recipients)]
    lines.extend(["", "## Watched-recipient matches this window", ""])
    if not watched:
        lines.append("No awards to watched diligence vendors in window.")
    else:
        for a in sorted(watched, key=lambda r: r.get("start_date", ""), reverse=True):
            lines.append(
                f"- {a.get('start_date', '')} · {_fmt_amount(a.get('amount'))} · "
                f"{a.get('recipient', '')} · {a.get('agency', '')} · _{a.get('query', '')}_"
            )

    if errors:
        lines.extend(["", "## Errors", ""])
        lines.extend(f"- {e}" for e in errors)
    lines.append("")
    return "\n".join(lines)


def send_alert(new_awards: list[dict[str, Any]], watch_recipients: list[str], report_path: Path) -> int:
    webhook_url = resolve_webhook_url()
    if not webhook_url:
        return 0
    top = new_awards[:8]
    desc = "\n".join(
        f"{a.get('start_date','')} · {_fmt_amount(a.get('amount'))} · {a.get('recipient','')}"
        f"{' ⭐' if is_watched_recipient(a, watch_recipients) else ''} (_{a.get('query','')}_)"
        for a in top
    )
    post_discord(
        webhook_url,
        content=f"**Federal procurement — {len(new_awards)} new diligence award(s)**",
        embeds=[
            {
                "title": "USASpending diligence-signal watcher",
                "description": f"{desc}\n\nReport: `{report_path}`",
                "color": 0xE67E22,
            }
        ],
        username="Cemini Procurement Watch",
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
    watch_recipients = [str(r) for r in config.get("watch_recipients", [])]
    lookback = int(settings.get("lookback_days", 120))

    startdt = (today - dt.timedelta(days=lookback)).isoformat()
    enddt = today.isoformat()

    report_path = report_dir(REPORT_LANE) / f"{today.isoformat()}-procurement-sweep.md"
    state_path = report_dir(REPORT_LANE) / "last_run_state.json"
    state = read_json(state_path, {})
    seen_ids = {migrate_seen_id(uid) for uid in state.get("seen_ids", []) if uid}
    first_run = not state

    all_awards: list[dict[str, Any]] = []
    errors: list[str] = []
    for query in queries:
        qid = query.get("id", "query")
        try:
            if offline_payloads is not None:
                awards = [
                    a
                    for a in parse_awards(offline_payloads.get(qid, {}), qid)
                    if apply_query_filters(a, query)
                ]
            else:
                awards = search_query(query, startdt=startdt, enddt=enddt, settings=settings)
        except Exception as exc:  # noqa: BLE001
            errors.append(f"{qid}: {exc}")
            continue
        all_awards.extend(awards)

    new_awards = dedupe_new(all_awards, seen_ids)
    alertable_new, suppressed_new = partition_alertable(new_awards, config, queries)

    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(
        render_report(
            today=today,
            startdt=startdt,
            enddt=enddt,
            queries=queries,
            all_awards=all_awards,
            new_awards=alertable_new,
            suppressed_awards=suppressed_new,
            watch_recipients=watch_recipients,
            errors=errors,
            first_run=first_run,
        ),
        encoding="utf-8",
    )

    alerts = 0
    if notify and alertable_new and not first_run and settings.get("alert_on_new", True):
        alerts = send_alert(alertable_new, watch_recipients, report_path)

    write_json(
        state_path,
        {
            "last_run": today.isoformat(),
            "seen_ids": sorted(
                seen_ids | {canonical_award_key(a) for a in all_awards if canonical_award_key(a)}
            ),
            "last_report": str(report_path),
            "last_new_count": len(alertable_new),
            "last_suppressed_count": len(suppressed_new),
        },
    )
    return {
        "report_path": report_path,
        "all_awards": all_awards,
        "new_awards": alertable_new,
        "suppressed_awards": suppressed_new,
        "errors": errors,
        "alerts": alerts,
        "first_run": first_run,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--thesis", default=DEFAULT_THESIS, help="Thesis id (config dir under config/theses/).")
    parser.add_argument("--config", type=Path, default=None, help="Explicit config path (overrides --thesis).")
    parser.add_argument("--date", default=dt.date.today().isoformat())
    parser.add_argument("--notify", action="store_true", help="Discord alert on new awards.")
    args = parser.parse_args()

    cfg = args.config or config_path(args.thesis)
    today = dt.date.fromisoformat(args.date)
    result = run(cfg, today, notify=args.notify)
    print(f"Report: {result['report_path']}")
    print(f"Awards this window: {len(result['all_awards'])}")
    print(f"New awards: {len(result['new_awards'])}")
    if result.get("suppressed_awards"):
        print(f"Suppressed (ops noise): {len(result['suppressed_awards'])}")
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
