"""Arena static-agent entrypoint — maps sandbox choose_action → cemini_decide."""
from __future__ import annotations

import os
import sys
import time
from pathlib import Path
from typing import Any, Optional

_ASSETS = Path(__file__).resolve().parent.parent / "assets"
_VENDOR = _ASSETS / "_vendor"
if _VENDOR.is_dir() and str(_VENDOR) not in sys.path:
    sys.path.insert(0, str(_VENDOR))
if _ASSETS.is_dir() and str(_ASSETS) not in sys.path:
    sys.path.insert(0, str(_ASSETS))

# Researcher HU sandbox posture (server-side; no prod .env on Arena runner).
os.environ.setdefault("CEMINI_TABLE_FORMAT", "hu")
os.environ.setdefault("CEMINI_RESEARCHER_MODE", "1")
os.environ.setdefault("CEMINI_MAFP_CHART", "1")
os.environ.setdefault("CEMINI_TRAJECTORY_BOUND", "1")
os.environ.setdefault("CEMINI_VERIFIER_BON", "1")
os.environ.setdefault("CEMINI_GIN_STYLE", "1")
os.environ.setdefault("CEMINI_GIN_STYLE_PREFLOP", "1")
os.environ.setdefault("CEMINI_GIN_STYLE_POSTFLOP", "1")
os.environ.setdefault("CEMINI_GIN_V2_EXPLOITS", "1")
os.environ.setdefault("CEMINI_SANITIZE_OUTPUT", "1")
os.environ.setdefault("CEMINI_MIX_POSTFLOP", "1")
os.environ.setdefault("CEMINI_S1B_EXPLOIT", "1")
os.environ.setdefault("CEMINI_NEMESIS_EXPLOIT", "1")
os.environ.setdefault("CEMINI_ISO_PASSIVE_LP", "1")


def _import_decide():
    from cemini_decide import decide  # noqa: WPS433

    return decide


def _deadline_s(table: dict) -> float:
    """Use table deadline when present; floor at 2s for sim budget."""
    raw = table.get("actionDeadlineAt") or table.get("deadlineAt")
    if raw is not None:
        try:
            if isinstance(raw, (int, float)):
                deadline_ts = float(raw)
                if deadline_ts > 1e12:
                    deadline_ts /= 1000.0
            else:
                from datetime import datetime

                text = str(raw).replace("Z", "+00:00")
                deadline_ts = datetime.fromisoformat(text).timestamp()
            remaining = deadline_ts - time.time()
            if remaining > 0:
                return max(2.0, min(10.0, remaining - 0.15))
        except (TypeError, ValueError, OSError):
            pass
    try:
        floor = float(os.environ.get("CEMINI_DEADLINE_FLOOR_S", "2.0"))
    except ValueError:
        floor = 2.0
    return max(floor, min(10.0, float(os.environ.get("CEMINI_DECIDE_DEADLINE_S", "8.0"))))


def choose_action(table: dict) -> Any:
    decide = _import_decide()
    out = decide(table, deadline_s=_deadline_s(table))
    try:
        from output_sanitize import maybe_sanitize_action  # noqa: WPS433

        out = maybe_sanitize_action(out)
    except ImportError:
        pass
    action = str(out.get("action") or "fold")
    amount = out.get("amount")
    payload_keys = ("action", "amount", "message", "reasoning")
    if amount is not None or out.get("message") or out.get("reasoning"):
        payload = {k: out[k] for k in payload_keys if k in out and out[k] is not None}
        payload["action"] = action
        return payload
    return action


def act(table: dict) -> Any:
    return choose_action(table)
