#!/usr/bin/env python3
"""ICE biweekly detention statistics monitor.

Fetches the ICE detention-management page, downloads the latest FYTD workbook,
parses facility-level FY26 ADP vs guaranteed minimum for turnkey watchlist sites,
tracks publish staleness against the statutory biweekly cadence, and optionally
alerts on new ICE publishes.
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
import urllib.parse
import zipfile
from pathlib import Path
from typing import Any
from xml.etree import ElementTree as ET

from scripts.intel.core.config import load_yaml
from scripts.intel.core.discord import post_discord, resolve_webhook_url
from scripts.intel.core.http import fetch_bytes, fetch_text
from scripts.intel.core.staleness import staleness_metrics
from scripts.intel.core.state import read_json, write_json
from scripts.intel.paths import data_dir, report_dir, thesis_config

CONFIG_PATH = thesis_config("detention-stats.yaml")
REPORT_DIR = report_dir("ice-detention-stats")
ARCHIVE_DIR = data_dir("ice-detention-stats")
STATE_PATH = REPORT_DIR / "last_run_state.json"
XLSX_NS = {"m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
REL_NS = {"r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships"}
PKG_NS = {"p": "http://schemas.openxmlformats.org/package/2006/relationships"}

XLSX_LINK_RE = re.compile(
    r"(?:https?://www\.ice\.gov)?(/doclib/detention/FY\d+_detentionStats[_\w]*\.xlsx)",
    re.IGNORECASE,
)
FILENAME_DATE_RE = re.compile(r"detentionStats[_]?(\d{8})", re.IGNORECASE)
PULL_DATE_RE = re.compile(r"Data Source:.*?,?\s*(\d{2}/\d{2}/\d{4})", re.IGNORECASE)


def load_config(path: Path = CONFIG_PATH) -> dict[str, Any]:
    return load_yaml(path)


def newest_archive(archive_dir: Path) -> Path | None:
    if not archive_dir.is_dir():
        return None
    candidates = sorted(archive_dir.glob("FY*_detentionStats*.xlsx"), key=lambda p: p.stat().st_mtime, reverse=True)
    return candidates[0] if candidates else None


def acquire_workbook(
    *,
    settings: dict[str, Any],
    state: dict[str, Any],
    archive_dir: Path,
) -> tuple[str, bytes, Path, str]:
    """Return xlsx_url, bytes, archive_path, fetch_mode (live|cached)."""
    page_url = settings.get("page_url", "https://www.ice.gov/detain/detention-management")
    fallback_url = settings.get("fallback_xlsx_url", "")
    errors: list[str] = []

    for label, fetch in (
        ("ice_page", lambda: _fetch_live_workbook(page_url)),
        ("fallback_url", lambda: _fetch_direct_workbook(fallback_url)),
    ):
        try:
            return (*fetch(), "live")
        except Exception as exc:  # noqa: BLE001
            errors.append(f"{label}: {exc}")

    cached = newest_archive(archive_dir)
    if cached is None:
        last_archive = state.get("last_archive", "")
        if last_archive:
            cached = Path(last_archive)
    if cached and cached.is_file():
        url = state.get("last_xlsx_url") or f"file://{cached}"
        return url, cached.read_bytes(), cached, "cached"

    raise RuntimeError("ICE workbook fetch failed and no cached archive is available: " + "; ".join(errors))


def _fetch_live_workbook(page_url: str) -> tuple[str, bytes, Path]:
    page_html = fetch_text(page_url)
    xlsx_url = discover_latest_xlsx_url(page_html)
    if not xlsx_url:
        raise RuntimeError("Could not find FY detentionStats xlsx link on ICE page")
    xlsx_bytes = fetch_bytes(xlsx_url)
    archive_name = Path(urllib.parse.urlparse(xlsx_url).path).name
    archive_path = ARCHIVE_DIR / archive_name
    archive_path.parent.mkdir(parents=True, exist_ok=True)
    archive_path.write_bytes(xlsx_bytes)
    return xlsx_url, xlsx_bytes, archive_path


def _fetch_direct_workbook(url: str) -> tuple[str, bytes, Path]:
    if not url:
        raise RuntimeError("no fallback_xlsx_url configured")
    xlsx_url = absolute_ice_url(url)
    xlsx_bytes = fetch_bytes(xlsx_url)
    archive_name = Path(urllib.parse.urlparse(xlsx_url).path).name
    archive_path = ARCHIVE_DIR / archive_name
    archive_path.parent.mkdir(parents=True, exist_ok=True)
    archive_path.write_bytes(xlsx_bytes)
    return xlsx_url, xlsx_bytes, archive_path


def absolute_ice_url(path_or_url: str) -> str:
    if path_or_url.startswith("http"):
        return path_or_url
    return urllib.parse.urljoin("https://www.ice.gov", path_or_url)


def discover_latest_xlsx_url(page_html: str) -> str | None:
    matches = XLSX_LINK_RE.findall(page_html)
    if not matches:
        return None
    ranked: list[tuple[dt.date, str]] = []
    for rel in matches:
        if "FY25" in rel.upper() and "FY26" not in rel.upper():
            continue
        m = FILENAME_DATE_RE.search(rel)
        if m:
            ranked.append((dt.datetime.strptime(m.group(1), "%m%d%Y").date(), rel))
        elif "FY26" in rel.upper():
            ranked.append((dt.date.min, rel))
    if not ranked:
        return absolute_ice_url(matches[0])
    ranked.sort(key=lambda row: row[0], reverse=True)
    return absolute_ice_url(ranked[0][1])


def parse_filename_date(url: str) -> str:
    m = FILENAME_DATE_RE.search(url)
    if not m:
        return ""
    return dt.datetime.strptime(m.group(1), "%m%d%Y").date().isoformat()


def load_shared_strings(z: zipfile.ZipFile) -> list[str]:
    if "xl/sharedStrings.xml" not in z.namelist():
        return []
    root = ET.fromstring(z.read("xl/sharedStrings.xml"))
    shared: list[str] = []
    for si in root.findall("m:si", XLSX_NS):
        texts = [t.text or "" for t in si.findall(".//m:t", XLSX_NS)]
        shared.append("".join(texts))
    return shared


def sheet_path_by_name(z: zipfile.ZipFile, needle: str) -> str | None:
    wb = ET.fromstring(z.read("xl/workbook.xml"))
    rels = ET.fromstring(z.read("xl/_rels/workbook.xml.rels"))
    rid_to_target = {
        rel.get("Id"): rel.get("Target")
        for rel in rels.findall("p:Relationship", PKG_NS)
    }
    for sheet in wb.findall("m:sheets/m:sheet", XLSX_NS):
        name = sheet.get("name") or ""
        if needle.lower() in name.lower():
            rid = sheet.get(f"{{{REL_NS['r']}}}id")
            target = rid_to_target.get(rid or "")
            if target:
                return "xl/" + target.lstrip("/")
    return None


def cell_value(cell: ET.Element, shared: list[str]) -> str:
    cell_type = cell.get("t")
    value_el = cell.find("m:v", XLSX_NS)
    if value_el is None or value_el.text is None:
        return ""
    raw = value_el.text
    if cell_type == "s":
        return shared[int(raw)]
    return raw


def parse_sheet_rows(z: zipfile.ZipFile, sheet_path: str) -> list[list[str]]:
    shared = load_shared_strings(z)
    root = ET.fromstring(z.read(sheet_path))
    rows: list[list[str]] = []
    for row in root.findall(".//m:sheetData/m:row", XLSX_NS):
        vals: list[str] = []
        for cell in row.findall("m:c", XLSX_NS):
            vals.append(cell_value(cell, shared))
        if vals:
            rows.append(vals)
    return rows


def extract_pull_date(rows: list[list[str]]) -> str:
    for row in rows[:12]:
        text = " ".join(row)
        m = PULL_DATE_RE.search(text)
        if m:
            return dt.datetime.strptime(m.group(1), "%m/%d/%Y").date().isoformat()
    return ""


def parse_facilities(rows: list[list[str]]) -> tuple[dict[str, str], list[dict[str, Any]]]:
    header: list[str] = []
    facilities: list[dict[str, Any]] = []
    for row in rows:
        if not header and row and row[0] == "Name":
            header = row
            continue
        if not header or not row or row[0] in ("Facility Information", "ICE Facilities Data, FY26"):
            continue
        if len(row) < len(header):
            row = row + [""] * (len(header) - len(row))
        record = dict(zip(header, row))
        if record.get("Name"):
            facilities.append(record)
    pull_date = extract_pull_date(rows)
    meta = {"pull_date": pull_date}
    return meta, facilities


def to_float(value: str) -> float | None:
    if not value or value.strip().upper() == "ODO":
        return None
    try:
        return float(value)
    except ValueError:
        return None


def implied_adp(record: dict[str, Any]) -> float | None:
    parts = [
        to_float(str(record.get("Male Crim", ""))),
        to_float(str(record.get("Male Non-Crim", ""))),
        to_float(str(record.get("Female Crim", ""))),
        to_float(str(record.get("Female Non-Crim", ""))),
    ]
    if any(p is None for p in parts):
        return None
    return sum(parts)  # type: ignore[arg-type]


def match_targets(config: dict[str, Any], facilities: list[dict[str, Any]]) -> list[dict[str, Any]]:
    targets = config.get("targets", [])
    matched: list[dict[str, Any]] = []
    for target in targets:
        needle = target["match"].upper()
        record = next((f for f in facilities if needle in str(f.get("Name", "")).upper()), None)
        if not record:
            matched.append(
                {
                    **target,
                    "found": False,
                    "name": "",
                    "implied_adp": None,
                    "guaranteed_minimum": None,
                    "delta_vs_min": None,
                    "fy26_alos": None,
                    "type_detailed": "",
                    "state": "",
                }
            )
            continue
        adp = implied_adp(record)
        gmin = to_float(str(record.get("Guaranteed Minimum", "")))
        delta = (adp - gmin) if adp is not None and gmin is not None else None
        matched.append(
            {
                **target,
                "found": True,
                "name": record.get("Name", ""),
                "implied_adp": adp,
                "guaranteed_minimum": gmin,
                "delta_vs_min": delta,
                "fy26_alos": to_float(str(record.get("FY26 ALOS", ""))),
                "type_detailed": record.get("Type Detailed", ""),
                "state": record.get("State", ""),
            }
        )
    return matched


def render_report(
    *,
    config: dict[str, Any],
    today: dt.date,
    page_url: str,
    xlsx_url: str,
    publish_date: str,
    pull_date: str,
    staleness: dict[str, Any],
    targets: list[dict[str, Any]],
    archive_path: Path,
    delta: dict[str, Any],
    fetch_mode: str = "live",
) -> str:
    lines = [
        f"# ICE detention stats sweep — {today.isoformat()}",
        "",
        "## Source",
        "",
        f"- Page: {page_url}",
        f"- Workbook: {xlsx_url}",
        f"- Fetch mode: **{fetch_mode}**",
        f"- Filename publish date: {publish_date or 'unknown'}",
        f"- IIDS pull date (Facilities sheet): {pull_date or 'unknown'}",
        f"- Archive: `{archive_path}`",
        "",
        "## Publish cadence",
        "",
        f"- Statutory cadence: every {config.get('settings', {}).get('biweekly_days', 14)} days",
        f"- Days since last publish: {staleness.get('days_since_publish', 'n/a')}",
        f"- Missed biweekly cycles (approx.): {staleness.get('missed_cycles', 'n/a')}",
        f"- Status: **{staleness.get('status', 'unknown')}**",
        "",
        "## Method note",
        "",
        "Facilities sheet reports FY26 **year-to-date average daily population (ADP)**, not a live headcount.",
        "Guaranteed Minimum is a contract floor, not rated capacity. TRAC overcapacity work still needs FOIA capacity.",
        "",
        "## Target facilities",
        "",
        "| ID | Label | ADP | Gtd min | Δ vs min | ALOS | Type | State |",
        "|---|---|---:|---:|---:|---:|---|---|",
    ]
    for row in targets:
        adp = f"{row['implied_adp']:.1f}" if row.get("implied_adp") is not None else "n/a"
        gmin = (
            f"{row['guaranteed_minimum']:.0f}"
            if row.get("guaranteed_minimum") is not None
            else ("ODO" if row.get("found") else "n/a")
        )
        delta_vs = (
            f"{row['delta_vs_min']:+.1f}"
            if row.get("delta_vs_min") is not None
            else "n/a"
        )
        alos = f"{row['fy26_alos']:.1f}" if row.get("fy26_alos") is not None else "n/a"
        label = row["label"] + ("" if row.get("found") else " (missing)")
        lines.append(
            f"| {row['id']} | {label} | {adp} | {gmin} | {delta_vs} | {alos} | {row.get('type_detailed', '')} | {row.get('state', '')} |"
        )

    lines.extend(["", "## Delta", ""])
    if delta.get("new_publish"):
        lines.append(
            f"New ICE workbook detected: `{delta.get('previous_xlsx_url', 'none')}` → `{xlsx_url}`."
        )
    elif delta.get("first_run"):
        lines.append("First run: baseline stored.")
    else:
        lines.append("No new ICE workbook since previous run.")

    overcrowded = [
        row for row in targets if row.get("delta_vs_min") is not None and row["delta_vs_min"] > 0
    ]
    overcrowded.sort(key=lambda r: r["delta_vs_min"], reverse=True)
    lines.extend(["", "## Over-guaranteed-minimum (ADP)", ""])
    if not overcrowded:
        lines.append("No target facilities above guaranteed minimum on this file.")
    else:
        for row in overcrowded:
            lines.append(
                f"- **{row['label']}**: ADP {row['implied_adp']:.0f} vs min {row['guaranteed_minimum']:.0f} "
                f"({row['delta_vs_min']:+.0f}) — {row.get('thesis_lane', '')}"
            )
    lines.append("")
    return "\n".join(lines)


def send_publish_alert(xlsx_url: str, publish_date: str, report_path: Path) -> int:
    webhook_url = resolve_webhook_url()
    if not webhook_url:
        return 0
    post_discord(
        webhook_url,
        content="**ICE detention stats — new biweekly workbook published**",
        embeds=[
            {
                "title": "ICE detention statistics update",
                "description": (
                    f"New workbook: {xlsx_url}\n"
                    f"Publish date: {publish_date or 'unknown'}\n"
                    f"Report: `{report_path}`"
                ),
                "color": 0x2ECC71,
            }
        ],
        username="Cemini ICE Stats Watch",
    )
    return 1


def run(config_path: Path, today: dt.date, notify: bool = False) -> dict[str, Any]:
    config = load_config(config_path)
    settings = config.get("settings", {})
    page_url = settings.get("page_url", "https://www.ice.gov/detain/detention-management")
    biweekly_days = int(settings.get("biweekly_days", 14))

    state = read_json(STATE_PATH, {})
    xlsx_url, _xlsx_bytes, archive_path, fetch_mode = acquire_workbook(
        settings=settings,
        state=state,
        archive_dir=ARCHIVE_DIR,
    )
    publish_date = parse_filename_date(xlsx_url)
    previous_url = state.get("last_xlsx_url", "")
    new_publish = bool(previous_url and previous_url != xlsx_url and fetch_mode == "live")
    first_run = not previous_url

    with zipfile.ZipFile(archive_path) as zf:
        sheet_path = sheet_path_by_name(zf, "Facilities")
        if not sheet_path:
            raise RuntimeError("Facilities sheet not found in workbook")
        meta, facilities = parse_facilities(parse_sheet_rows(zf, sheet_path))

    pull_date = meta.get("pull_date", "")
    targets = match_targets(config, facilities)
    staleness = staleness_metrics(publish_date, today, biweekly_days)

    delta = {
        "first_run": first_run,
        "new_publish": new_publish,
        "previous_xlsx_url": previous_url,
    }

    report_path = REPORT_DIR / f"{today.isoformat()}-stats-sweep.md"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(
        render_report(
            config=config,
            today=today,
            page_url=page_url,
            xlsx_url=xlsx_url,
            publish_date=publish_date,
            pull_date=pull_date,
            staleness=staleness,
            targets=targets,
            archive_path=archive_path,
            delta=delta,
            fetch_mode=fetch_mode,
        ),
        encoding="utf-8",
    )

    alerts = 0
    if notify and new_publish and settings.get("alert_on_new_publish", True):
        alerts = send_publish_alert(xlsx_url, publish_date, report_path)

    write_json(
        STATE_PATH,
        {
            "last_run": today.isoformat(),
            "last_xlsx_url": xlsx_url,
            "last_publish_date": publish_date,
            "last_pull_date": pull_date,
            "staleness": staleness,
            "last_report": str(report_path),
            "last_archive": str(archive_path),
            "last_fetch_mode": fetch_mode,
        },
    )
    return {
        "report_path": report_path,
        "archive_path": archive_path,
        "xlsx_url": xlsx_url,
        "publish_date": publish_date,
        "pull_date": pull_date,
        "staleness": staleness,
        "targets": targets,
        "delta": delta,
        "alerts": alerts,
        "fetch_mode": fetch_mode,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=CONFIG_PATH)
    parser.add_argument("--date", default=dt.date.today().isoformat())
    parser.add_argument("--notify", action="store_true", help="Discord alert when ICE publishes a new workbook.")
    args = parser.parse_args()

    today = dt.date.fromisoformat(args.date)
    result = run(args.config, today, notify=args.notify)
    print(f"Report: {result['report_path']}")
    print(f"Archive: {result['archive_path']}")
    print(f"Workbook: {result['xlsx_url']}")
    print(f"Publish date: {result['publish_date']}")
    print(f"Pull date: {result['pull_date']}")
    print(f"Staleness: {result['staleness']['status']} ({result['staleness'].get('days_since_publish')}d)")
    print(f"Fetch mode: {result['fetch_mode']}")
    if result["delta"]["new_publish"]:
        print("New ICE workbook detected.")
    if result["alerts"]:
        print(f"Discord alerts sent: {result['alerts']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
