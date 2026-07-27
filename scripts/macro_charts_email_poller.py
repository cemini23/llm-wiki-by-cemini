#!/usr/bin/env python3
"""Poll Gmail for cousin-forwarded Macro Charts Substack issues → inbox markdown.

Does NOT write wiki pages (Phase 4 human gate). Drops files into
`research to be indexed/` so inbox_notify.sh + preingest_check run as usual.

Usage:
  python3 scripts/macro_charts_email_poller.py --dry-run
  python3 scripts/macro_charts_email_poller.py
  bash scripts/run_macro_charts_email_poller.sh
"""

from __future__ import annotations

import argparse
import base64
import email
import json
import re
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from email.message import Message
from pathlib import Path
from typing import Any

import yaml

SCRIPTS = Path(__file__).resolve().parent
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from macro_charts_common import (  # noqa: E402
    INBOX,
    REPO_ROOT,
    html_to_text,
    post_slug_from_url,
    read_post_state,
    record_post_export,
    slugify,
    trigger_inbox_notify,
    write_post_state,
)

CONFIG_PATH = REPO_ROOT / "config" / "macro-charts-ingest.yaml"
LEGACY_CONFIG = REPO_ROOT / "config" / "macro-charts-email.yaml"
GMAIL_SCOPES = [
    "https://www.googleapis.com/auth/gmail.modify",
    "https://www.googleapis.com/auth/gmail.settings.basic",
]


def load_config(path: Path | None = None) -> dict[str, Any]:
    cfg_path = path or (CONFIG_PATH if CONFIG_PATH.is_file() else LEGACY_CONFIG)
    if not cfg_path.is_file():
        raise SystemExit(f"Missing config: {CONFIG_PATH}\nRun: bash scripts/setup_macro_charts_email_ingest.sh")
    return yaml.safe_load(cfg_path.read_text(encoding="utf-8")) or {}


def read_gmail_ids(path: Path) -> set[str]:
    if not path.is_file():
        return set()
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
        return set(payload.get("processed_message_ids") or [])
    except (json.JSONDecodeError, OSError):
        return set()


def write_gmail_ids(path: Path, ids: set[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps({"processed_message_ids": sorted(ids)}, indent=2),
        encoding="utf-8",
    )


def normalize_email(addr: str) -> str:
    m = re.search(r"<([^>]+)>", addr)
    if m:
        return m.group(1).strip().lower()
    return addr.strip().lower()


def message_text_parts(msg: Message) -> tuple[str, str]:
    """Return (plain_text, html_text) from an email.message.Message."""
    plain_parts: list[str] = []
    html_parts: list[str] = []
    if msg.is_multipart():
        for part in msg.walk():
            ctype = part.get_content_type()
            disp = str(part.get("Content-Disposition", ""))
            if "attachment" in disp:
                continue
            payload = part.get_payload(decode=True)
            if not payload:
                continue
            charset = part.get_content_charset() or "utf-8"
            try:
                text = payload.decode(charset, errors="replace")
            except LookupError:
                text = payload.decode("utf-8", errors="replace")
            if ctype == "text/plain":
                plain_parts.append(text)
            elif ctype == "text/html":
                html_parts.append(text)
    else:
        payload = msg.get_payload(decode=True) or b""
        charset = msg.get_content_charset() or "utf-8"
        try:
            text = payload.decode(charset, errors="replace")
        except LookupError:
            text = payload.decode("utf-8", errors="replace")
        if msg.get_content_type() == "text/html":
            html_parts.append(text)
        else:
            plain_parts.append(text)
    return "\n".join(plain_parts), "\n".join(html_parts)


def extract_substack_url(text: str) -> str | None:
    for pat in (
        r"https?://(?:www\.)?macrocharts\.com/p/[a-zA-Z0-9_-]+",
        r"https?://macrocharts\.substack\.com/p/[a-zA-Z0-9_-]+",
    ):
        m = re.search(pat, text, re.I)
        if m:
            return m.group(0)
    return None


def strip_subject_prefix(subject: str) -> str:
    return re.sub(r"^(?:(?:fwd?|re):\s*)+", "", subject, flags=re.I).strip()


@dataclass
class ParsedForward:
    subject: str
    received_at: str
    from_header: str
    body: str
    substack_url: str | None
    matched_signals: list[str]


def classify_macro_charts(
    subject: str,
    from_header: str,
    body: str,
    signals: list[str],
    forwarders: list[str],
    deny_senders: list[str],
) -> tuple[bool, list[str]]:
    from_addr = normalize_email(from_header)
    forwarder_set = {normalize_email(x) for x in forwarders}
    deny_set = {normalize_email(x) for x in deny_senders}

    if from_addr not in forwarder_set:
        return False, []
    if from_addr in deny_set:
        return False, []

    haystack = f"{subject}\n{from_header}\n{body}".lower()
    matched = [sig for sig in signals if sig.lower() in haystack]
    return bool(matched), matched


def parse_gmail_payload(raw: str) -> Message:
    return email.message_from_bytes(base64.urlsafe_b64decode(raw))


def build_markdown(parsed: ParsedForward, gmail_id: str, forwarder: str) -> str:
    title = strip_subject_prefix(parsed.subject) or "Macro Charts forward"
    lines = [
        "---",
        f"title: \"Macro Charts paid forward — {title}\"",
        "type: source-stub",
        "tags: [macro-charts, substack, email-forward, paid, inbox-auto]",
        f"retrieved: {parsed.received_at[:10]}",
        f"gmail_message_id: {gmail_id}",
        f"forwarded_by: {forwarder}",
        "tier: paid (Vincent forward)",
        "---",
        "",
        "# Macro Charts — paid forward (Vincent)",
        "",
        f"- **Subject:** {parsed.subject}",
        f"- **Received:** {parsed.received_at}",
        f"- **Forwarded by:** {forwarder}",
        f"- **Detection signals:** {', '.join(parsed.matched_signals)}",
    ]
    if parsed.substack_url:
        lines.append(f"- **Substack URL:** {parsed.substack_url}")
    lines.extend(
        [
            "",
            "_Prefer this file over `macro-charts-rss-*` for the same URL when ingesting._",
            "",
            "## Body",
            "",
            parsed.body,
            "",
        ]
    )
    return "\n".join(lines)


def gmail_service():
    try:
        from google.auth.transport.requests import Request
        from google.oauth2.credentials import Credentials
        from google_auth_oauthlib.flow import InstalledAppFlow
        from googleapiclient.discovery import build
    except ImportError as exc:
        raise SystemExit(
            "Gmail dependencies missing. Run:\n"
            "  pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib\n"
            f"({exc})"
        ) from exc

    token_path = Path.home() / ".cemini" / "gmail-oauth-token.json"
    client_path = Path.home() / ".cemini" / "gmail-oauth-client.json"
    if not client_path.is_file():
        raise SystemExit(
            f"Missing OAuth client: {client_path}\n"
            "See: bash scripts/setup_macro_charts_email_ingest.sh"
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


def list_label_id(service, name: str) -> str | None:
    resp = service.users().labels().list(userId="me").execute()
    for label in resp.get("labels", []):
        if label.get("name") == name:
            return label["id"]
    return None


def ensure_label(service, name: str) -> str:
    existing = list_label_id(service, name)
    if existing:
        return existing
    body = {
        "name": name,
        "labelListVisibility": "labelShow",
        "messageListVisibility": "show",
    }
    created = service.users().labels().create(userId="me", body=body).execute()
    return created["id"]


def poll_gmail(cfg: dict[str, Any], *, dry_run: bool, backfill_days: int | None = None) -> int:
    service = gmail_service()
    label_name = cfg["gmail"]["label"]
    processed_label_name = cfg["gmail"]["processed_label"]
    forwarders = cfg["forwarders"]
    signals = cfg["macro_charts_signals"]
    deny = cfg.get("deny_senders") or []
    slug_max = int((cfg.get("inbox") or {}).get("slug_max_len") or 48)
    prefix = (cfg.get("inbox") or {}).get("email_filename_prefix", "macro-charts-paid-forward")
    state_cfg = cfg.get("state") or {}
    gmail_state_path = REPO_ROOT / state_cfg.get("gmail_message_ids", ".local/state/macro-charts-email.json")
    posts_state_path = REPO_ROOT / state_cfg.get("posts_registry", ".local/state/substack-rss-posts.json")
    processed_ids = read_gmail_ids(gmail_state_path)
    posts_state = read_post_state(posts_state_path)

    label_id = list_label_id(service, label_name)
    if not label_id:
        raise SystemExit(
            f"Gmail label not found: {label_name!r}\n"
            "Create the filter + label via setup_macro_charts_email_ingest.sh"
        )

    processed_label_id = ensure_label(service, processed_label_name)
    from_clause = " OR ".join(f"from:{addr}" for addr in forwarders)
    # Do not require Cemini/Macro-Charts label — Gmail filters are not retroactive.
    signal_query = " OR ".join(
        f'"{sig}"' if " " in sig else sig
        for sig in ("macrocharts", "Macro Charts", "macrocharts.com")
    )
    query = f"-label:{processed_label_name} ({from_clause}) ({signal_query})"
    if backfill_days:
        query += f" newer_than:{backfill_days}d"
    resp = service.users().messages().list(userId="me", q=query, maxResults=50).execute()
    messages = resp.get("messages") or []

    exported = 0
    skipped = 0
    INBOX.mkdir(parents=True, exist_ok=True)

    for item in messages:
        mid = item["id"]
        if mid in processed_ids:
            continue

        full = service.users().messages().get(userId="me", id=mid, format="raw").execute()
        msg = parse_gmail_payload(full["raw"])
        subject = msg.get("Subject", "")
        from_header = msg.get("From", "")
        plain, html_blob = message_text_parts(msg)
        body = plain.strip() or html_to_text(html_blob)
        internal_ms = int(full.get("internalDate", "0"))
        received_at = datetime.fromtimestamp(internal_ms / 1000, tz=timezone.utc).isoformat()

        ok, matched = classify_macro_charts(subject, from_header, body, signals, forwarders, deny)
        if not ok:
            print(f"SKIP {mid}: from {from_header!r} — no Macro Charts signals")
            skipped += 1
            continue

        parsed = ParsedForward(
            subject=subject,
            received_at=received_at,
            from_header=from_header,
            body=body,
            substack_url=extract_substack_url(body),
            matched_signals=matched,
        )
        date_part = received_at[:10]
        slug = slugify(strip_subject_prefix(subject), slug_max)
        url_slug = post_slug_from_url(parsed.substack_url) if parsed.substack_url else slug
        out_name = f"{prefix}-{date_part}-{url_slug or slug}.md"
        out_path = INBOX / out_name
        if out_path.exists():
            out_name = f"{prefix}-{date_part}-{slug}-{mid[:8]}.md"
            out_path = INBOX / out_name

        md = build_markdown(parsed, mid, normalize_email(from_header))
        print(f"{'DRY-RUN' if dry_run else 'EXPORT'} {out_name} ({', '.join(matched)})")

        if dry_run:
            exported += 1
            continue

        out_path.write_text(md, encoding="utf-8")
        if parsed.substack_url:
            record_post_export(
                posts_state,
                parsed.substack_url,
                source="email",
                filename=out_name,
            )
        service.users().messages().modify(
            userId="me",
            id=mid,
            body={"addLabelIds": [processed_label_id], "removeLabelIds": [label_id]},
        ).execute()
        processed_ids.add(mid)
        exported += 1

    if not dry_run and exported:
        write_gmail_ids(gmail_state_path, processed_ids)
        write_post_state(posts_state_path, posts_state)
        trigger_inbox_notify()
        # Rolling Macro Charts params → GuruWatcher (best-effort)
        try:
            import subprocess

            hook = REPO_ROOT / "scripts" / "guru_watcher_inbox_hook.sh"
            if hook.is_file():
                subprocess.run(["bash", str(hook)], check=False, timeout=600)
        except Exception as exc:  # noqa: BLE001
            print(f"WARN: GuruWatcher hook skipped: {exc}")

    print(f"Done: exported={exported} skipped={skipped}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Macro Charts cousin-forward → inbox poller")
    parser.add_argument("--dry-run", action="store_true", help="Classify only; do not write files")
    parser.add_argument(
        "--backfill-days",
        type=int,
        default=None,
        metavar="N",
        help="Limit search to mail newer than N days (default: no limit)",
    )
    args = parser.parse_args()
    cfg = load_config()
    return poll_gmail(cfg, dry_run=args.dry_run, backfill_days=args.backfill_days)


if __name__ == "__main__":
    sys.exit(main())
