#!/usr/bin/env python3
"""Send gated rows via Cloudflare Email Sending. Requires wrangler OAuth login."""
from __future__ import annotations

import argparse
import csv
import json
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from gate import (
    contact_of,
    detect_campaign,
    gate_row,
    is_email,
    load_sent,
    workspace_outreach,
)

ACCT = "dafb95ecefe3b5da945e3354a17de841"  # pragma: allowlist secret
FROM = {
    "atto": "claudio@youratto.com",
    "gw": "claudio@guruwatcher.com",
}
TOKEN_TOML = Path.home() / "Library/Preferences/.wrangler/config/default.toml"


def wrangler_token() -> str:
    text = TOKEN_TOML.read_text()
    for line in text.splitlines():
        if line.strip().startswith("oauth_token"):
            return line.split("=", 1)[1].strip().strip('"').strip("'")
    raise SystemExit("no wrangler oauth_token — run wrangler login")


def cf_send(token: str, from_addr: str, to_addr: str, subject: str, text: str) -> tuple[int, dict]:
    body = {
        "from": {"address": from_addr, "name": "Claudio Barone"},
        "to": to_addr,
        "subject": subject,
        "text": text,
        "reply_to": {"address": from_addr, "name": "Claudio Barone"},
    }
    req = urllib.request.Request(
        f"https://api.cloudflare.com/client/v4/accounts/{ACCT}/email/sending/send",
        data=json.dumps(body).encode(),
        method="POST",
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=45) as resp:
            return resp.status, json.loads(resp.read())
    except urllib.error.HTTPError as e:
        raw = e.read().decode("utf-8", "replace")
        try:
            return e.code, json.loads(raw)
        except json.JSONDecodeError:
            return e.code, {"raw": raw[:800]}


def append_log(data: Path, entry: dict) -> None:
    path = data / "send-log.json"
    blob = []
    if path.exists():
        try:
            blob = json.loads(path.read_text())
        except json.JSONDecodeError:
            blob = []
    blob.append(entry)
    path.write_text(json.dumps(blob, indent=2))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", required=True)
    ap.add_argument("--campaign", choices=["atto", "gw", "auto"], default="auto")
    ap.add_argument("--max", type=int, default=15)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    path = Path(args.csv).expanduser()
    data = workspace_outreach()
    with path.open(newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = list(reader.fieldnames or [])
        rows = list(reader)
    campaign = detect_campaign(path, rows, None if args.campaign == "auto" else args.campaign)
    from_addr = FROM[campaign]
    sent = load_sent(data)
    seen: dict[str, str] = {}
    token = None if args.dry_run else wrangler_token()
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    n_sent = 0
    for row in rows:
        g = gate_row(row, campaign, seen, sent)
        contact = contact_of(row, campaign)
        if g["verdict"] == "form":
            row["status"] = "form"
            continue
        if g["verdict"] == "suppressed":
            row["status"] = "suppressed"
            continue
        if g["verdict"] == "skipped_dup":
            row["status"] = "skipped_dup"
            continue
        if g["verdict"] != "pass":
            row["status"] = "fail"
            continue
        if n_sent >= args.max:
            break
        if args.dry_run:
            row["status"] = "dry"
            n_sent += 1
            print("DRY", row.get("name"), "->", contact)
            continue
        status, resp = cf_send(
            token, from_addr, contact, row.get("draft_subject") or "", row.get("draft_body") or ""
        )
        ok = status == 200 and isinstance(resp, dict) and resp.get("success")
        result = resp.get("result") if isinstance(resp, dict) else None
        mid = (result or {}).get("message_id") if isinstance(result, dict) else None
        row["status"] = "sent" if ok else f"error:{status}"
        append_log(
            data,
            {
                "sheet": campaign,
                "name": row.get("name"),
                "to": contact,
                "from": from_addr,
                "http": status,
                "ok": ok,
                "message_id": mid,
                "queued": (result or {}).get("queued") if isinstance(result, dict) else None,
                "delivered": (result or {}).get("delivered") if isinstance(result, dict) else None,
                "errors": resp.get("errors") if isinstance(resp, dict) else resp,
                "at": now,
            },
        )
        print(("OK" if ok else "FAIL"), row.get("name"), "->", contact, status, mid)
        if ok:
            n_sent += 1
            sent.add(contact.lower())
            time.sleep(0.8)
    with path.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore", lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    print(json.dumps({"campaign": campaign, "sent": n_sent, "max": args.max, "csv": str(path)}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
