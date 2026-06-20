"""Discord webhook alerts."""

from __future__ import annotations

import json
import logging
import urllib.error
import urllib.request
from typing import Any, Optional

logger = logging.getLogger(__name__)


def send_discord_embed(
    *,
    webhook_url: str,
    username: str,
    title: str,
    description: str,
    color: int = 3066993,
    fields: Optional[list[dict[str, Any]]] = None,
) -> bool:
    payload = {
        "username": username,
        "embeds": [
            {
                "title": title[:256],
                "description": description[:4096],
                "color": color,
                "fields": (fields or [])[:25],
            }
        ],
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        webhook_url,
        data=data,
        headers={"Content-Type": "application/json", "User-Agent": "wc-r16-ticket-monitor/1.0"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            ok = resp.status in (200, 204)
            if not ok:
                logger.warning("discord webhook HTTP %s", resp.status)
            return ok
    except urllib.error.URLError as exc:
        logger.error("discord webhook failed: %s", exc)
        return False
