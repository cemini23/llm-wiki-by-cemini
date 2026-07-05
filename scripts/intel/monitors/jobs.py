#!/usr/bin/env python3
"""ICE facility hiring anomaly monitor for CoreCivic and GEO.

Fetches live CoreCivic Phenom and GEO/Jibe job feeds, groups postings around
target ICE facility clusters, compares against same-operator baselines, writes
a local snapshot/report, and optionally sends Discord alerts for new high-signal
roles after the first run.
"""

from __future__ import annotations

import argparse
import datetime as dt
import math
import re
import statistics
import urllib.parse
from pathlib import Path
from typing import Any

from scripts.intel.core.config import load_yaml
from scripts.intel.core.discord import post_discord, post_test_ping, resolve_webhook_url
from scripts.intel.core.http import fetch_json
from scripts.intel.core.state import read_json, write_json
from scripts.intel.paths import data_dir, report_dir, thesis_config

CONFIG_PATH = thesis_config("jobs.yaml")
REPORT_DIR = report_dir("ice-facility-jobs")
SNAPSHOT_ROOT = data_dir("ice-jobs-daily")
STATE_PATH = REPORT_DIR / "last_run_state.json"


def load_config(path: Path = CONFIG_PATH) -> dict[str, Any]:
    return load_yaml(path)


def slugify(value: str) -> str:
    value = re.sub(r"[^A-Za-z0-9]+", "-", value.strip()).strip("-")
    return value or "job"


def haversine_miles(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    radius_miles = 3958.8
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)
    a = math.sin(dphi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2) ** 2
    return radius_miles * 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))


def clean_date(value: str | None) -> str:
    if not value:
        return ""
    return value[:10]


def first_present(raw: dict[str, Any], candidates: list[str]) -> Any:
    for key in candidates:
        value = raw.get(key)
        if value not in (None, ""):
            return value
    return ""


def lifecycle_date_fields(raw: dict[str, Any]) -> dict[str, str]:
    fields: dict[str, str] = {}
    for key, value in raw.items():
        key_lower = str(key).lower()
        if any(token in key_lower for token in ("date", "open", "expir", "close")):
            cleaned = clean_date(str(value)) if value not in (None, "") else ""
            if cleaned:
                fields[str(key)] = cleaned
    return fields


def normalized_text(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", value.lower()).strip()


def keyword_hit(value: str, keywords: list[str]) -> bool:
    haystack = normalized_text(value)
    return any(normalized_text(keyword) in haystack for keyword in keywords)


def facility_matches_target(facility: str, targets: list[str]) -> bool:
    facility_norm = normalized_text(facility)
    if not facility_norm:
        return False
    for target in targets:
        target_norm = normalized_text(target)
        if target_norm and (target_norm in facility_norm or facility_norm in target_norm):
            return True
    return False


def classify_roles(title: str, category: str, role_keywords: dict[str, list[str]]) -> list[str]:
    haystack = f"{title} {category}".lower()
    roles = [
        role
        for role, keywords in role_keywords.items()
        if any(keyword.lower() in haystack for keyword in keywords)
    ]
    return roles or ["other"]


def role_score(roles: list[str], role_weights: dict[str, int]) -> int:
    return sum(int(role_weights.get(role, 0)) for role in set(roles))


def normalize_corecivic_job(raw: dict[str, Any]) -> dict[str, Any] | None:
    try:
        lat = float(raw.get("latitude"))
        lon = float(raw.get("longitude"))
    except (TypeError, ValueError):
        return None
    job_id = raw.get("jobId") or raw.get("reqId")
    title = raw.get("title") or ""
    facility = raw.get("facility") or raw.get("location") or ""
    return {
        "source": "corecivic",
        "operator": "CoreCivic",
        "ticker": "CXW",
        "job_id": job_id,
        "title": title,
        "category": raw.get("category") or "",
        "facility": facility,
        "city": (raw.get("city") or "").title(),
        "state": raw.get("state") or "",
        "location": raw.get("location") or "",
        "lat": lat,
        "lon": lon,
        "posted_date": clean_date(raw.get("postedDate")),
        "created_date": clean_date(raw.get("dateCreated")),
        "open_date": clean_date(str(first_present(raw, ["openDateLocal", "openDate", "jobOpenDate"]))),
        "expiration_date": clean_date(
            str(first_present(raw, ["expirationDate", "expiryDate", "expireDate", "validThrough"]))
        ),
        "lifecycle_dates": lifecycle_date_fields(raw),
        "employment_type": raw.get("type") or "",
        "url": f"https://jobs.corecivic.com/us/en/job/{job_id}/{slugify(title)}",
        "apply_url": raw.get("applyUrl") or "",
        "raw_ats": raw,
    }


def normalize_geo_job(raw: dict[str, Any]) -> dict[str, Any] | None:
    try:
        lat = float(raw.get("latitude"))
        lon = float(raw.get("longitude"))
    except (TypeError, ValueError):
        return None
    job_id = str(raw.get("req_id") or raw.get("slug") or "")
    categories = raw.get("categories") or []
    category = ", ".join(c.get("name", "") for c in categories if isinstance(c, dict))
    tags6 = raw.get("tags6")
    if isinstance(tags6, list):
        tags6 = tags6[0] if tags6 else ""
    facility = raw.get("location_name") or tags6 or raw.get("full_location") or ""
    return {
        "source": "geo",
        "operator": "GEO Group",
        "ticker": "GEO",
        "job_id": job_id,
        "title": raw.get("title") or "",
        "category": category or ", ".join(raw.get("category") or []),
        "facility": facility,
        "city": raw.get("city") or "",
        "state": raw.get("state") or "",
        "location": raw.get("full_location") or raw.get("short_location") or "",
        "lat": lat,
        "lon": lon,
        "posted_date": clean_date(raw.get("posted_date")),
        "created_date": clean_date(raw.get("create_date")),
        "open_date": clean_date(str(first_present(raw, ["open_date", "openDate", "job_open_date"]))),
        "expiration_date": clean_date(
            str(first_present(raw, ["expiration_date", "expires_at", "valid_through", "close_date"]))
        ),
        "lifecycle_dates": lifecycle_date_fields(raw),
        "employment_type": raw.get("employment_type") or "",
        "url": f"https://jobs.geogroup.com/working-at-geo/jobs/{job_id}/job?lang=en-us",
        "apply_url": raw.get("apply_url") or "",
        "raw_ats": raw,
    }


def fetch_corecivic_jobs(source_cfg: dict[str, Any]) -> list[dict[str, Any]]:
    endpoint = source_cfg["endpoint"]
    ref_num = source_cfg["ref_num"]
    all_jobs: list[dict[str, Any]] = []
    base_payload = {
        "lang": "en_us",
        "deviceType": "desktop",
        "country": "us",
        "pageName": "search-results",
        "jobs": True,
        "counts": True,
        "all_fields": ["category", "country", "city", "type", "facility_name", "state", "location"],
        "clearAll": False,
        "jdsource": "facets",
        "isSliderEnable": False,
        "pageId": "page452-prod",
        "siteType": "external",
        "keywords": "",
        "global": True,
        "selected_fields": {},
        "sort": {"order": "desc", "field": "postedDate"},
        "locationData": {},
        "refNum": ref_num,
        "ddoKey": "refineSearch",
    }
    for start in range(0, 1000, 100):
        payload = dict(base_payload, size=100, **{"from": start})
        data = fetch_json(endpoint, method="POST", payload=payload).get("refineSearch", {})
        jobs = data.get("data", {}).get("jobs", [])
        all_jobs.extend(j for j in (normalize_corecivic_job(job) for job in jobs) if j)
        if len(jobs) < 100:
            break
    return all_jobs


def fetch_geo_jobs(source_cfg: dict[str, Any]) -> list[dict[str, Any]]:
    endpoint = source_cfg["endpoint"]
    all_jobs: list[dict[str, Any]] = []
    page = 1
    while True:
        url = f"{endpoint}?{urllib.parse.urlencode({'page': page})}"
        data = fetch_json(url)
        jobs = data.get("jobs", [])
        all_jobs.extend(
            j for j in (normalize_geo_job(wrap.get("data", {})) for wrap in jobs) if j
        )
        if not jobs or page * 10 >= int(data.get("totalCount") or 0):
            break
        page += 1
    return all_jobs


def fetch_all_jobs(config: dict[str, Any]) -> list[dict[str, Any]]:
    jobs: list[dict[str, Any]] = []
    sources = config.get("sources", {})
    if sources.get("corecivic", {}).get("enabled", False):
        jobs.extend(fetch_corecivic_jobs(sources["corecivic"]))
    if sources.get("geo", {}).get("enabled", False):
        jobs.extend(fetch_geo_jobs(sources["geo"]))
    return jobs


def annotate_jobs(config: dict[str, Any], jobs: list[dict[str, Any]]) -> list[dict[str, Any]]:
    role_keywords = config["role_keywords"]
    role_weights = config["role_weights"]
    settings = config.get("settings", {})
    default_radius = float(settings.get("default_radius_miles", 40))
    excluded_context_keywords = settings.get("excluded_context_keywords", {})
    clusters = config.get("clusters", [])

    annotated: list[dict[str, Any]] = []
    for job in jobs:
        roles = classify_roles(job["title"], job.get("category", ""), role_keywords)
        enriched = dict(job)
        enriched["roles"] = roles
        enriched["signal_score"] = role_score(roles, role_weights)
        enriched["key"] = f"{job['source']}:{job['job_id']}"
        matched_clusters = []
        for cluster in clusters:
            if cluster.get("operator_source") != job["source"]:
                continue
            anchor = cluster["anchor"]
            distance = haversine_miles(anchor["lat"], anchor["lon"], job["lat"], job["lon"])
            if distance <= float(cluster.get("radius_miles") or default_radius):
                target_match = facility_matches_target(job.get("facility", ""), cluster.get("target_facilities", []))
                source_exclusions = list(excluded_context_keywords.get(job["source"], []))
                source_exclusions.extend(cluster.get("excluded_context_keywords", []))
                excluded_context = not target_match and keyword_hit(
                    " ".join(
                        [
                            job.get("facility", ""),
                            job.get("location", ""),
                            job.get("title", ""),
                            job.get("category", ""),
                        ]
                    ),
                    source_exclusions,
                )
                match_type = "target" if target_match else "excluded_context" if excluded_context else "radius_context"
                matched_clusters.append(
                    {
                        "id": cluster["id"],
                        "label": cluster["label"],
                        "distance_miles": round(distance, 1),
                        "match_type": match_type,
                        "thesis_read": cluster.get("thesis_read", ""),
                        "signal_category": cluster.get("signal_category", "watch_only"),
                        "acquisition_relevance": cluster.get("acquisition_relevance", "low"),
                    }
                )
        enriched["clusters"] = matched_clusters
        annotated.append(enriched)
    return annotated


def percentile(values: list[int], pct: float) -> float:
    if not values:
        return 0.0
    values = sorted(values)
    pos = (len(values) - 1) * pct
    lower = math.floor(pos)
    upper = math.ceil(pos)
    if lower == upper:
        return float(values[int(pos)])
    return values[lower] + (values[upper] - values[lower]) * (pos - lower)


def baseline_by_source(config: dict[str, Any], jobs: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    target_facilities = {
        (cluster["operator_source"], facility.lower())
        for cluster in config.get("clusters", [])
        for facility in cluster.get("target_facilities", [])
    }
    grouped: dict[tuple[str, str], list[dict[str, Any]]] = {}
    for job in jobs:
        grouped.setdefault((job["source"], job["facility"]), []).append(job)

    result: dict[str, dict[str, Any]] = {}
    for source in ("corecivic", "geo"):
        counts = []
        for (job_source, facility), facility_jobs in grouped.items():
            if job_source != source:
                continue
            if (source, facility.lower()) in target_facilities:
                continue
            counts.append(len(facility_jobs))
        result[source] = {
            "facility_count": len(counts),
            "median": statistics.median(counts) if counts else 0,
            "p75": round(percentile(counts, 0.75), 2),
            "p90": round(percentile(counts, 0.90), 2),
            "max": max(counts) if counts else 0,
        }
    return result


def cluster_summaries(
    config: dict[str, Any],
    jobs: list[dict[str, Any]],
    baselines: dict[str, dict[str, Any]],
    today: dt.date,
) -> list[dict[str, Any]]:
    recent_days = int(config.get("settings", {}).get("recent_days", 45))
    recent_cutoff = today - dt.timedelta(days=recent_days)
    summaries: list[dict[str, Any]] = []

    for cluster in config.get("clusters", []):
        cluster_jobs = [job for job in jobs if any(c["id"] == cluster["id"] for c in job["clusters"])]
        target_jobs = [
            job
            for job in cluster_jobs
            if any(c["id"] == cluster["id"] and c.get("match_type") == "target" for c in job["clusters"])
        ]
        radius_context_jobs = [
            job
            for job in cluster_jobs
            if any(c["id"] == cluster["id"] and c.get("match_type") == "radius_context" for c in job["clusters"])
        ]
        excluded_context_jobs = [
            job
            for job in cluster_jobs
            if any(c["id"] == cluster["id"] and c.get("match_type") == "excluded_context" for c in job["clusters"])
        ]
        scoring_jobs = target_jobs
        facilities = sorted({job["facility"] for job in scoring_jobs if job["facility"]})
        context_facilities = sorted({job["facility"] for job in radius_context_jobs if job["facility"]})
        roles = sorted({role for job in scoring_jobs for role in job["roles"] if role != "other"})
        recent = [
            job
            for job in scoring_jobs
            if job.get("posted_date") and dt.date.fromisoformat(job["posted_date"]) >= recent_cutoff
        ]
        high_signal = [job for job in scoring_jobs if job["signal_score"] >= 4]
        jobs_per_facility = len(scoring_jobs) / max(len(facilities), 1)
        baseline = baselines.get(cluster["operator_source"], {})
        p75 = float(baseline.get("p75") or 0)
        p90 = float(baseline.get("p90") or 0)
        if (
            jobs_per_facility > p90
            and len(roles) >= 4
            and len(scoring_jobs) >= 4
            or len(recent) >= 8
            and len(roles) >= 6
            or len(high_signal) >= 4
            and len(roles) >= 4
        ):
            anomaly = "high"
        elif jobs_per_facility > p75 or len(roles) >= 4 or len(recent) >= 5:
            anomaly = "medium"
        else:
            anomaly = "low"
        summaries.append(
            {
                "id": cluster["id"],
                "label": cluster["label"],
                "operator_source": cluster["operator_source"],
                "ticker": cluster.get("ticker", ""),
                "jobs": len(scoring_jobs),
                "target_jobs": len(target_jobs),
                "radius_context_jobs": len(radius_context_jobs),
                "excluded_context_jobs": len(excluded_context_jobs),
                "all_matched_jobs": len(cluster_jobs),
                "facilities": facilities,
                "context_facilities": context_facilities,
                "jobs_per_facility": round(jobs_per_facility, 2),
                "recent_jobs": len(recent),
                "role_breadth": len(roles),
                "roles": roles,
                "high_signal_jobs": len(high_signal),
                "anomaly": anomaly,
                "signal_category": cluster.get("signal_category", "watch_only"),
                "acquisition_relevance": cluster.get("acquisition_relevance", "low"),
                "thesis_read": cluster.get("thesis_read", ""),
                "jobs_detail": sorted(
                    scoring_jobs + radius_context_jobs + excluded_context_jobs,
                    key=lambda job: (job.get("posted_date", ""), -job.get("signal_score", 0), job["title"]),
                ),
            }
        )
    return summaries


def delta_from_state(state: dict[str, Any], jobs: list[dict[str, Any]]) -> dict[str, Any]:
    current_keys = {job["key"] for job in jobs}
    previous_keys = set(state.get("active_job_keys", []))
    first_run = not bool(previous_keys)
    new_keys = current_keys - previous_keys if not first_run else set()
    gone_keys = previous_keys - current_keys if not first_run else set()
    by_key = {job["key"]: job for job in jobs}
    return {
        "first_run": first_run,
        "new_jobs": [by_key[key] for key in sorted(new_keys)],
        "gone_job_keys": sorted(gone_keys),
        "current_keys": sorted(current_keys),
    }


def render_report(
    *,
    config: dict[str, Any],
    today: dt.date,
    jobs: list[dict[str, Any]],
    summaries: list[dict[str, Any]],
    baselines: dict[str, dict[str, Any]],
    delta: dict[str, Any],
    snapshot_path: Path,
) -> str:
    lines = [
        f"# ICE Facility Jobs Sweep — {today.isoformat()}",
        "",
        "## Summary",
        "",
        f"- Active jobs fetched: **{len(jobs)}**",
        f"- New jobs vs previous snapshot: **{len(delta['new_jobs'])}**"
        + (" (first run baseline)" if delta["first_run"] else ""),
        f"- Disappeared jobs vs previous snapshot: **{len(delta['gone_job_keys'])}**",
        f"- Snapshot: `{snapshot_path}`",
        "- Raw ATS payloads: preserved in snapshot under `jobs[*].raw_ats`; lifecycle hints under `jobs[*].lifecycle_dates`.",
        "- Cluster anomaly scores use target-facility-name matches only; radius-only and excluded context stay visible but do not drive anomaly rank.",
        "",
        "## Baselines",
        "",
        "| Source | Non-target facilities | Median jobs/facility | P75 | P90 | Max |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for source, stats in baselines.items():
        lines.append(
            f"| {source} | {stats['facility_count']} | {stats['median']} | {stats['p75']} | {stats['p90']} | {stats['max']} |"
        )

    lines.extend(
        [
            "",
            "## Cluster Ranking",
            "",
            "| Rank | Cluster | Target jobs | Radius context | Excluded context | Recent | Roles | Anomaly | Category | Acq rel. | Read |",
            "|---:|---|---:|---:|---:|---:|---:|---|---|---|---|",
        ]
    )
    ranked = sorted(
        summaries,
        key=lambda row: (
            {"high": 3, "medium": 2, "low": 1}.get(row["anomaly"], 0),
            row["jobs_per_facility"],
            row["role_breadth"],
            row["recent_jobs"],
        ),
        reverse=True,
    )
    for idx, row in enumerate(ranked, 1):
        lines.append(
            f"| {idx} | {row['label']} | {row['target_jobs']} | {row['radius_context_jobs']} | "
            f"{row['excluded_context_jobs']} | {row['recent_jobs']} | {row['role_breadth']} | "
            f"{row['anomaly']} | {row['signal_category']} | {row['acquisition_relevance']} | {row['thesis_read']} |"
        )

    lines.extend(["", "## Cluster Details", ""])
    for row in ranked:
        lines.extend(
            [
                f"### {row['label']}",
                "",
                f"- Target jobs: {row['target_jobs']} active; {row['recent_jobs']} recent; {row['high_signal_jobs']} high-signal.",
                f"- Context: {row['radius_context_jobs']} radius-only; {row['excluded_context_jobs']} excluded from anomaly scoring.",
                f"- Signal category: {row['signal_category']}; acquisition relevance: {row['acquisition_relevance']}.",
                f"- Roles: {', '.join(row['roles']) or 'other only'}.",
                f"- Facilities: {', '.join(row['facilities']) or 'n/a'}.",
                f"- Context facilities: {', '.join(row['context_facilities']) or 'n/a'}.",
                f"- Read: {row['thesis_read']}",
                "",
                "| Posted | Open | Expires | ID | Score | Match | Roles | Title | Facility | Distance |",
                "|---|---|---|---|---:|---|---|---|---|---:|",
            ]
        )
        for job in sorted(row["jobs_detail"], key=lambda j: (j["posted_date"], j["title"]))[-30:]:
            cluster_match = next(c for c in job["clusters"] if c["id"] == row["id"])
            lines.append(
                f"| {job['posted_date']} | {job.get('open_date', '')} | {job.get('expiration_date', '')} | "
                f"[{job['job_id']}]({job['url']}) | {job['signal_score']} | {cluster_match.get('match_type', '')} | "
                f"{', '.join(job['roles'])} | {job['title']} | {job['facility']} | {cluster_match['distance_miles']} |"
            )
        lines.append("")

    lines.extend(["## New Jobs", ""])
    if delta["first_run"]:
        lines.append("First run: current active set stored as baseline; no alertable new-job delta yet.")
    elif not delta["new_jobs"]:
        lines.append("No new jobs since previous snapshot.")
    else:
        lines.extend(
            [
                "| Posted | Open | Expires | ID | Score | Roles | Title | Matched target clusters |",
                "|---|---|---|---|---:|---|---|---|",
            ]
        )
        for job in sorted(delta["new_jobs"], key=lambda j: (-j["signal_score"], j["posted_date"])):
            target_clusters = [
                c["label"] for c in job["clusters"] if c.get("match_type") == "target"
            ]
            lines.append(
                f"| {job['posted_date']} | {job.get('open_date', '')} | {job.get('expiration_date', '')} | "
                f"[{job['job_id']}]({job['url']}) | {job['signal_score']} | "
                f"{', '.join(job['roles'])} | {job['title']} | {', '.join(target_clusters)} |"
            )

    lines.extend(["", "## Vendor Lanes To Monitor", ""])
    for lane in config.get("vendor_lanes", []):
        terms = "; ".join(lane.get("search_terms", []))
        lines.append(f"- **{lane['label']}** (`{lane['id']}`): {terms}")

    lines.extend(["", "## Event Watch", ""])
    for item in config.get("event_watch", []):
        lines.append(f"- {item}")
    lines.append("")
    return "\n".join(lines)


def send_alerts(config: dict[str, Any], new_jobs: list[dict[str, Any]], report_path: Path) -> tuple[int, list[str]]:
    webhook_url = resolve_webhook_url()
    if not webhook_url:
        return 0, ["No Discord webhook — run: bash scripts/setup_recorder_discord_webhook.sh"]
    min_score = int(config.get("settings", {}).get("alert_min_signal_score", 6))
    alert_jobs = [
        job
        for job in new_jobs
        if job["signal_score"] >= min_score
        and any(c.get("match_type") == "target" for c in job["clusters"])
    ]
    if not alert_jobs:
        return 0, []
    fields = []
    for job in alert_jobs[:10]:
        clusters = ", ".join(c["label"] for c in job["clusters"] if c.get("match_type") == "target")
        fields.append(
            {
                "name": f"{job['job_id']} — {job['title']}"[:256],
                "value": (
                    f"{job['operator']} · {job['posted_date']} · score {job['signal_score']}\n"
                    f"{clusters}\n{job['url']}"
                )[:1024],
                "inline": False,
            }
        )
    post_discord(
        webhook_url,
        content="**ICE facility jobs watch — new high-signal hiring roles**",
        embeds=[
            {
                "title": "ICE facility hiring anomaly monitor",
                "description": f"{len(alert_jobs)} new high-signal role(s). Report: `{report_path}`",
                "color": 0x3498DB,
                "fields": fields,
            }
        ],
        username="Cemini Jobs Watch",
    )
    return len(alert_jobs), []


def run(config_path: Path, today: dt.date, notify: bool = False) -> dict[str, Any]:
    config = load_config(config_path)
    jobs = annotate_jobs(config, fetch_all_jobs(config))
    baselines = baseline_by_source(config, jobs)
    summaries = cluster_summaries(config, jobs, baselines, today)
    state = read_json(STATE_PATH, {})
    delta = delta_from_state(state, jobs)

    snapshot_dir = SNAPSHOT_ROOT / today.isoformat()
    snapshot_path = snapshot_dir / "snapshot.json"
    report_path = REPORT_DIR / f"{today.isoformat()}-jobs-sweep.md"
    snapshot_payload = {
        "date": today.isoformat(),
        "jobs": jobs,
        "cluster_summaries": [{k: v for k, v in row.items() if k != "jobs_detail"} for row in summaries],
        "baselines": baselines,
        "delta": {
            "first_run": delta["first_run"],
            "new_job_keys": [job["key"] for job in delta["new_jobs"]],
            "gone_job_keys": delta["gone_job_keys"],
        },
    }
    write_json(snapshot_path, snapshot_payload)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(
        render_report(
            config=config,
            today=today,
            jobs=jobs,
            summaries=summaries,
            baselines=baselines,
            delta=delta,
            snapshot_path=snapshot_path,
        ),
        encoding="utf-8",
    )

    notify_result = (0, [])
    if notify and not delta["first_run"]:
        notify_result = send_alerts(config, delta["new_jobs"], report_path)

    write_json(
        STATE_PATH,
        {
            "last_run": today.isoformat(),
            "active_job_keys": delta["current_keys"],
            "last_report": str(report_path),
            "last_snapshot": str(snapshot_path),
        },
    )
    return {
        "report_path": report_path,
        "snapshot_path": snapshot_path,
        "jobs": jobs,
        "summaries": summaries,
        "delta": delta,
        "notify_result": notify_result,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=CONFIG_PATH)
    parser.add_argument("--date", default=dt.date.today().isoformat())
    parser.add_argument("--notify", action="store_true", help="Send Discord alerts for new high-signal roles.")
    parser.add_argument("--test-discord", action="store_true", help="Send a Discord test ping and exit.")
    args = parser.parse_args()

    if args.test_discord:
        webhook_url = resolve_webhook_url()
        if not webhook_url:
            print("No Discord webhook configured.")
            return 2
        post_test_ping(webhook_url)
        print("Discord test ping sent.")
        return 0

    today = dt.date.fromisoformat(args.date)
    result = run(args.config, today, notify=args.notify)
    print(f"Report: {result['report_path']}")
    print(f"Snapshot: {result['snapshot_path']}")
    print(f"Active jobs: {len(result['jobs'])}")
    if result["delta"]["first_run"]:
        print("First run baseline stored; no new-job alerts emitted.")
    else:
        print(f"New jobs: {len(result['delta']['new_jobs'])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
