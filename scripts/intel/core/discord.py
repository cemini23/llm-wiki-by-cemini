"""Discord notifications — thin re-export of workspace helper."""

from __future__ import annotations

import sys
from pathlib import Path

_SCRIPTS = Path(__file__).resolve().parents[2]
if str(_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS))

from cemini_discord_notify import (  # noqa: E402
    post_discord,
    post_recorder_sale_alert,
    post_test_ping,
    resolve_webhook_url,
)

__all__ = [
    "post_discord",
    "post_recorder_sale_alert",
    "post_test_ping",
    "resolve_webhook_url",
]
