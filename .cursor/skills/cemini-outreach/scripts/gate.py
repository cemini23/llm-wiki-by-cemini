#!/usr/bin/env python3
"""Mechanical send gate. Exit 0 iff every sendable row passes (forms may remain)."""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sys
from pathlib import Path

EMAIL_RE = re.compile(r"^[A-Z0-9._%+\-]+@[A-Z0-9.\-]+\.[A-Z]{2,}$", re.I)
ATTO_COM = re.compile(r"(?<![a-z])atto\.com", re.I)
BANNED = re.compile(
    r"legal advice|i am an attorney|you qualify|forward (?:us |me )?(?:your )?paid|"
    r"scrape your list|place orders|i.?m a lawyer",
    re.I,
)
TRACKED_URL = {
    "atto": "https://youratto.com/?utm_source=email&utm_medium=outreach&utm_campaign=atto",
    "gw": "https://guruwatcher.com/?utm_source=email&utm_medium=outreach&utm_campaign=gw",
}


def workspace_outreach() -> Path:
    here = Path(__file__).resolve()
    for p in [here] + list(here.parents):
        cand = p / ".local" / "outreach"
        if (p / "CLAUDE.md").exists() or cand.exists():
            cand.mkdir(parents=True, exist_ok=True)
            return cand
    d = Path.home() / "Projects" / "OSINT WORKSPACE" / ".local" / "outreach"
    d.mkdir(parents=True, exist_ok=True)
    return d


def is_email(s: str) -> bool:
    return bool(EMAIL_RE.match((s or "").strip()))


def contact_of(row: dict, campaign: str) -> str:
    if campaign == "gw":
        return (row.get("public_email") or row.get("contact") or "").strip()
    return (row.get("contact") or row.get("public_email") or "").strip()


def detect_campaign(path: Path, rows: list[dict], forced: str | None) -> str:
    if forced in ("atto", "gw"):
        return forced
    name = path.name.lower()
    if name.startswith("gw") or "guru" in name:
        return "gw"
    if name.startswith("atto"):
        return "atto"
    if rows and ("newsletter" in rows[0] or "public_email" in rows[0]):
        return "gw"
    return "atto"


def load_sent(data: Path) -> set[str]:
    out: set[str] = set()
    log = data / "send-log.json"
    if log.exists():
        try:
            blob = json.loads(log.read_text())
        except json.JSONDecodeError:
            blob = []
        for e in blob:
            if e.get("ok") and e.get("to") and is_email(str(e["to"])):
                out.add(str(e["to"]).lower())
    sup = data / "suppress.json"
    if sup.exists():
        try:
            s = json.loads(sup.read_text())
        except json.JSONDecodeError:
            s = []
        if isinstance(s, dict):
            s = s.get("emails") or []
        for a in s:
            out.add(str(a).lower())
    return out


def gate_row(row: dict, campaign: str, seen_bodies: dict[str, str], sent: set[str]) -> dict:
    name = row.get("name") or ""
    contact = contact_of(row, campaign)
    body = (row.get("draft_body") or "").strip()
    subject = (row.get("draft_subject") or "").strip()
    status = (row.get("status") or "").strip()
    domain = "youratto.com" if campaign == "atto" else "guruwatcher.com"
    if not is_email(contact):
        return {"name": name, "to": contact, "verdict": "form", "reasons": []}
    reasons: list[str] = []
    cl = contact.lower()
    if cl in sent:
        reasons.append("already_sent_or_suppressed")
    if not subject:
        reasons.append("empty_subject")
    if not body:
        reasons.append("empty_body")
    if "claudio barone" not in body.lower():
        reasons.append("missing_signature")
    if domain not in body.lower():
        reasons.append(f"missing_{domain}")
    tracked = TRACKED_URL[campaign]
    if tracked not in body:
        reasons.append("missing_tracked_url")
    if ATTO_COM.search(body) or ATTO_COM.search(subject):
        reasons.append("atto.com_domain")
    if BANNED.search(body) or BANNED.search(subject):
        reasons.append("banned_phrase")
    h = hashlib.sha256(body.encode()).hexdigest()
    if h in seen_bodies:
        reasons.append(f"dup_body:{seen_bodies[h]}")
    else:
        seen_bodies[h] = name
    if status in ("sent", "form", "fail", "skipped_dup", "suppressed"):
        reasons.append(f"status_{status}")
    verdict = "fail" if reasons else "pass"
    if "already_sent_or_suppressed" in reasons:
        verdict = "suppressed"
    if any(r.startswith("dup_body:") for r in reasons) and verdict == "fail":
        verdict = "skipped_dup"
    return {"name": name, "to": contact, "verdict": verdict, "reasons": reasons}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", required=True)
    ap.add_argument("--campaign", choices=["atto", "gw", "auto"], default="auto")
    args = ap.parse_args()
    path = Path(args.csv).expanduser()
    data = workspace_outreach()
    with path.open(newline="") as f:
        rows = list(csv.DictReader(f))
    campaign = detect_campaign(path, rows, None if args.campaign == "auto" else args.campaign)
    sent = load_sent(data)
    seen: dict[str, str] = {}
    results = [gate_row(r, campaign, seen, sent) for r in rows]
    sendable_fail = [r for r in results if r["verdict"] in ("fail",)]
    out = {
        "campaign": campaign,
        "rows": results,
        "ok_to_send": [r["to"] for r in results if r["verdict"] == "pass"],
        "fail": sendable_fail,
    }
    print(json.dumps(out, indent=2))
    return 1 if sendable_fail else 0


if __name__ == "__main__":
    sys.exit(main())
