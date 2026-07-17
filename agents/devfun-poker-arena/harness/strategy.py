"""Arena static-agent entrypoint — cemini_decide or gin hu004 (Option A)."""
from __future__ import annotations

import os
import signal
import sys
import time
from pathlib import Path
from typing import Any, Callable, Optional

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
    os.environ.setdefault("CEMINI_POSTFLOP_BUCKETS", "1")
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

_USE_SIGALRM = hasattr(signal, "SIGALRM")

_EXAMPLES = Path(__file__).resolve().parent.parent / "examples"
if _EXAMPLES.is_dir() and str(_EXAMPLES) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES))


def _warm_cemini_caches() -> None:
    """Preload MAFP overlay + postflop buckets so first Action is not cold I/O."""
    if _ENGINE not in ("cemini", "cemini_decide", "default"):
        return
    try:
        from research_static_chart import _hu_chart_for_lookup  # noqa: WPS433

        _hu_chart_for_lookup()
    except Exception:
        pass
    try:
        from postflop_buckets import get_buckets_payload  # noqa: WPS433

        get_buckets_payload()
    except Exception:
        pass


_warm_cemini_caches()


class _DecideTimeout(Exception):
    """Wall-clock guard fired before decide() returned."""


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
            if remaining <= 0.2:
                return 0.0
            if remaining > 0:
                return max(0.5, min(10.0, remaining - 0.15))
        except (TypeError, ValueError, OSError):
            pass
    try:
        floor = float(os.environ.get("CEMINI_DEADLINE_FLOOR_S", "2.0"))
    except ValueError:
        floor = 2.0
    # Timeout harden v2: missing Arena deadline → assume 5s, not 8s.
    return max(floor, min(10.0, float(os.environ.get("CEMINI_DECIDE_DEADLINE_S", "5.0"))))


def _guard_s(deadline_s: float) -> float:
    """Earlier SIGALRM so emergency check/fold trips before Arena 422.

    Leaves 0.5s headroom, hard-caps wall time at 4.5s, and scales with
    0.6 * deadline so mid budgets still bail early.
    """
    if deadline_s <= 0:
        return 0.0
    raw = min(deadline_s - 0.5, 4.5, 0.6 * deadline_s)
    if raw <= 0:
        return 0.0
    return max(0.35, raw)


def _emergency_action(table: dict) -> dict[str, Any]:
    """Fail closed when wall-clock guard fires — avoid Arena 422 static timeout."""
    allowed = table.get("allowedActions") or {}
    avail = {str(a).lower() for a in (allowed.get("availableActions") or [])}
    if "check" in avail or allowed.get("canCheck"):
        return {"action": "check", "message": "wall-clock guard — free check"}
    if "fold" in avail or allowed.get("canFold"):
        return {"action": "fold", "message": "wall-clock guard — fold"}
    if "call" in avail or allowed.get("canCall"):
        payload: dict[str, Any] = {"action": "call", "message": "wall-clock guard — call"}
        if allowed.get("callChips") is not None:
            payload["amount"] = allowed.get("callChips")
        return payload
    return {"action": "fold", "message": "wall-clock guard — fold (fallback)"}


def _run_decide_guarded(
    decide: Callable[..., dict[str, Any]],
    table: dict,
    *,
    deadline_s: float,
    guard_s: float,
) -> dict[str, Any]:
    if guard_s <= 0:
        return _emergency_action(table)
    if not _USE_SIGALRM:
        return decide(table, deadline_s=deadline_s)

    def _on_alarm(_signum: int, _frame: Any) -> None:
        raise _DecideTimeout()

    previous = signal.signal(signal.SIGALRM, _on_alarm)
    signal.setitimer(signal.ITIMER_REAL, guard_s)
    try:
        return decide(table, deadline_s=deadline_s)
    except _DecideTimeout:
        print(
            f"sandbox wall-clock guard tripped ({guard_s:.1f}s deadline={deadline_s:.1f}s)",
            file=sys.stderr,
        )
        return _emergency_action(table)
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
        signal.signal(signal.SIGALRM, previous)


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
    deadline = _deadline_s(table)
    guard = _guard_s(deadline)
    out = _run_decide_guarded(decide, table, deadline_s=deadline, guard_s=guard)
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
