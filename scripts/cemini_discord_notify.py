#!/usr/bin/env python3
"""Post alerts to Discord via incoming webhook (no bot token).

Webhook URL resolution (first match wins):
  1. DISCORD_WEBHOOK_URL env
  2. ~/.cemini/recorder-discord-webhook.url  (recorder-specific)
  3. ~/.cemini/inbox-webhook.url             (shared Cemini inbox hook)

Discord API expects JSON with ``content`` and/or ``embeds`` — not Slack ``text``.
"""

from __future__ import annotations

import json
import os
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any


def resolve_webhook_url() -> str | None:
    env = os.environ.get("DISCORD_WEBHOOK_URL", "").strip()
    if env:
        return env
    for path in (
        Path.home() / ".cemini/recorder-discord-webhook.url",
        Path.home() / ".cemini/inbox-webhook.url",
    ):
        if path.is_file():
            url = path.read_text(encoding="utf-8").strip()
            if url:
                return url
    return None


def post_discord(
    webhook_url: str,
    *,
    content: str = "",
    embeds: list[dict[str, Any]] | None = None,
    username: str | None = "Cemini Recorder",
) -> None:
    payload: dict[str, Any] = {}
    if content:
        payload["content"] = content[:2000]
    if embeds:
        payload["embeds"] = embeds[:10]
    if username:
        payload["username"] = username[:80]

    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        webhook_url,
        data=data,
        headers={
            "Content-Type": "application/json",
            "User-Agent": "cemini-recorder-watch/1.0",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            if resp.status >= 400:
                raise RuntimeError(f"Discord webhook HTTP {resp.status}")
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")[:500]
        raise RuntimeError(f"Discord webhook failed ({exc.code}): {body}") from exc


def post_recorder_sale_alert(
    webhook_url: str,
    *,
    site_label: str,
    county: str,
    state: str,
    doc_number: str,
    doc_date: str,
    description: str,
    party_searched: str = "",
    report_path: str = "",
) -> None:
    fields = [
        {"name": "Site", "value": site_label, "inline": False},
        {"name": "County", "value": f"{county}, {state}", "inline": True},
        {"name": "Recorded", "value": doc_date or "—", "inline": True},
        {"name": "Doc #", "value": doc_number or "—", "inline": True},
        {"name": "Index description", "value": description[:1024] or "—", "inline": False},
    ]
    if party_searched:
        fields.append(
            {"name": "Party searched", "value": party_searched[:256], "inline": False}
        )
    if report_path:
        fields.append({"name": "Report", "value": report_path[:256], "inline": False})

    embeds = [
        {
            "title": "ICE turnkey — county recorder sale signal",
            "description": (
                "Grant-deed-class filing indexed with federal grantee pattern. "
                "**Verify grantor/grantee on the recorded instrument** — index text alone is not confirmation."
            ),
            "color": 0xE74C3C,
            "fields": fields,
        }
    ]
    post_discord(
        webhook_url,
        content="@here **Recorder watch — possible facility deed transfer**",
        embeds=embeds,
    )


def post_test_ping(webhook_url: str) -> None:
    post_discord(
        webhook_url,
        content="Cemini ICE recorder watch — Discord webhook test OK.",
        embeds=[
            {
                "title": "Recorder watch armed",
                "description": "You will get pinged here when a new grant-deed sale signal appears in the county index.",
                "color": 0x2ECC71,
            }
        ],
    )
