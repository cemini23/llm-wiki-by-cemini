#!/usr/bin/env python3
"""One-time Gmail OAuth + labels + Vincent Macro Charts filter.

Creates:
  - Label Cemini/Macro-Charts
  - Label Cemini/Macro-Charts/processed
  - Filter: from vinnyb64@gmail.com with macrocharts keywords → Cemini/Macro-Charts

Usage:
  python3 scripts/gmail_macro_charts_bootstrap.py
"""

from __future__ import annotations

import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import yaml  # noqa: E402
from macro_charts_email_poller import (  # noqa: E402
    ensure_label,
    gmail_service,
    list_label_id,
)

REPO_ROOT = SCRIPTS.parent
CONFIG = REPO_ROOT / "config" / "macro-charts-ingest.yaml"
GMAIL_SCOPES = [
    "https://www.googleapis.com/auth/gmail.modify",
    "https://www.googleapis.com/auth/gmail.settings.basic",
]


def load_cfg() -> dict:
    return yaml.safe_load(CONFIG.read_text(encoding="utf-8")) or {}


def gmail_service_with_settings():
    """Same as poller but includes settings.basic for filter create."""
    try:
        from google.auth.transport.requests import Request
        from google.oauth2.credentials import Credentials
        from google_auth_oauthlib.flow import InstalledAppFlow
        from googleapiclient.discovery import build
    except ImportError as exc:
        raise SystemExit(f"pip install google-auth-oauthlib google-api-python-client ({exc})") from exc

    token_path = Path.home() / ".cemini" / "gmail-oauth-token.json"
    client_path = Path.home() / ".cemini" / "gmail-oauth-client.json"
    if not client_path.is_file():
        raise SystemExit(
            f"Missing {client_path}\n"
            "Download Desktop OAuth JSON from Google Cloud Console → Gmail API enabled."
        )

    creds = None
    if token_path.is_file():
        creds = Credentials.from_authorized_user_file(str(token_path), GMAIL_SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(str(client_path), GMAIL_SCOPES)
            creds = flow.run_local_server(port=0)
        token_path.parent.mkdir(parents=True, exist_ok=True)
        token_path.write_text(creds.to_json(), encoding="utf-8")
    return build("gmail", "v1", credentials=creds)


def filter_exists(service, forwarder: str) -> bool:
    resp = service.users().settings().filters().list(userId="me").execute()
    for f in resp.get("filter", []):
        criteria = f.get("criteria", {})
        if criteria.get("from") == forwarder:
            return True
    return False


def create_vincent_filter(service, label_id: str, forwarder: str) -> None:
    if filter_exists(service, forwarder):
        print(f"Filter already exists for {forwarder}")
        return
    body = {
        "criteria": {
            "from": forwarder,
            "query": 'macrocharts OR "Macro Charts" OR macrocharts.com',
        },
        "action": {
            "addLabelIds": [label_id],
        },
    }
    service.users().settings().filters().create(userId="me", body=body).execute()
    print(f"Created Gmail filter: from {forwarder} → Cemini/Macro-Charts")


def main() -> int:
    cfg = load_cfg()
    gmail_cfg = cfg.get("gmail") or {}
    label_name = gmail_cfg.get("label", "Cemini/Macro-Charts")
    processed_name = gmail_cfg.get("processed_label", "Cemini/Macro-Charts/processed")
    forwarder = (cfg.get("forwarders") or ["vinnyb64@gmail.com"])[0]

    service = gmail_service_with_settings()
    label_id = ensure_label(service, label_name)
    ensure_label(service, processed_name)
    print(f"Labels OK: {label_name}, {processed_name}")

    create_vincent_filter(service, label_id, forwarder)

    # Smoke test poller can see the label
    if not list_label_id(service, label_name):
        raise SystemExit(f"Label missing after create: {label_name}")
    print("Gmail bootstrap complete. Run: bash scripts/run_macro_charts_email_poller.sh")
    return 0


if __name__ == "__main__":
    sys.exit(main())
