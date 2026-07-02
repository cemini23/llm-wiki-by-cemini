"""Arena static-agent entrypoint — cemini_decide or gin hu004 (Option A)."""
from __future__ import annotations

import os
import sys
import time
from pathlib import Path
from typing import Any, Optional

_ENGINE = os.environ.get("CEMINI_SANDBOX_ENGINE", "cemini").strip().lower()

if os.environ.get("CEMINI_SANDBOX_LOG_ENGINE") == "1":
    print(f"sandbox engine: {_ENGINE}", file=sys.stderr)

_ASSETS = Path(__file__).resolve().parent.parent / "assets"
_VENDOR = _ASSETS / "_vendor"
if _VENDOR.is_dir() and str(_VENDOR) not in sys.path:
    sys.path.insert(0, str(_VENDOR))
if _ASSETS.is_dir() and str(_ASSETS) not in sys.path:
    sys.path.insert(0, str(_ASSETS))

os.environ.setdefault("CEMINI_SANITIZE_OUTPUT", "0")
_DEFAULT_STRATEGY = "hu004" if _ENGINE in ("gin", "gin_hu004", "hu004") else "cemini_k131b"
os.environ.setdefault("POKER_BOT_STRATEGY", _DEFAULT_STRATEGY)

if _ENGINE in ("cemini", "cemini_decide", "default"):
    os.environ.setdefault("CEMINI_TABLE_FORMAT", "hu")
    os.environ.setdefault("CEMINI_RESEARCHER_MODE", "1")
    os.environ.setdefault("CEMINI_MAFP_CHART", "1")
    os.environ.setdefault("CEMINI_TRAJECTORY_BOUND", "1")
    os.environ.setdefault("CEMINI_VERIFIER_BON", "1")
    os.environ.setdefault("CEMINI_GIN_STYLE", "1")
    os.environ.setdefault("CEMINI_GIN_STYLE_PREFLOP", "1")
    os.environ.setdefault("CEMINI_GIN_STYLE_POSTFLOP", "1")
    os.environ.setdefault("CEMINI_GIN_V008", "1")
    os.environ.setdefault("CEMINI_GIN_V2_EXPLOITS", "1")
    os.environ.setdefault("CEMINI_MIX_POSTFLOP", "1")
    os.environ.setdefault("CEMINI_S1B_EXPLOIT", "1")
    os.environ.setdefault("CEMINI_NEMESIS_EXPLOIT", "1")
    os.environ.setdefault("CEMINI_ISO_PASSIVE_LP", "1")


def _import_decide():
    if _ENGINE in ("gin", "gin_hu004", "hu004"):
        from gin_hu004_bridge import decide  # noqa: WPS433

        return decide
    from cemini_decide import decide  # noqa: WPS433

    return decide


def _deadline_s(table: dict) -> float:
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


def _action_payload(out: dict[str, Any], action: str) -> dict[str, Any]:
    payload: dict[str, Any] = {"action": action}
    if out.get("amount") is not None:
        payload["amount"] = out["amount"]
    message = out.get("message")
    if message is not None:
        payload["message"] = message
    reasoning = out.get("reasoning") or out.get("reasoning_text")
    if reasoning is not None:
        payload["reasoning"] = reasoning
        payload["reasoning_text"] = reasoning
    return payload


def choose_action(table: dict) -> Any:
    decide = _import_decide()
    out = decide(table, deadline_s=_deadline_s(table))
    if _ENGINE in ("gin", "gin_hu004", "hu004"):
        return out
    try:
        from output_sanitize import maybe_sanitize_action  # noqa: WPS433

        out = maybe_sanitize_action(out)
    except ImportError:
        pass
    action = str(out.get("action") or "fold")
    if out.get("amount") is not None or out.get("message") or out.get("reasoning") or out.get(
        "reasoning_text"
    ):
        return _action_payload(out, action)
    return action


def act(table: dict) -> Any:
    return choose_action(table)
