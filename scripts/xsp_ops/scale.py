"""Scale / escalate when queue backlog or failures cross thresholds."""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path
from typing import Any

_SCRIPTS = Path(__file__).resolve().parents[1]
if str(_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS))

from intel.core.state import write_json  # noqa: E402

from xsp_ops.brain import utc_now_iso  # noqa: E402
from xsp_ops.paths import EVENTS_DIR, ensure_layout  # noqa: E402
from xsp_ops.queue import count_jobs  # noqa: E402

DEFAULT_PENDING_THRESHOLD = 5


def pending_threshold() -> int:
    raw = os.environ.get("XSP_OPS_SCALE_PENDING", str(DEFAULT_PENDING_THRESHOLD))
    try:
        return max(1, int(raw))
    except ValueError:
        return DEFAULT_PENDING_THRESHOLD


def should_escalate(root: Path | None = None, *, threshold: int | None = None) -> dict[str, Any]:
    thr = threshold if threshold is not None else pending_threshold()
    pending = count_jobs("pending", root)
    failed = count_jobs("failed", root)
    running = count_jobs("running", root)
    escalate = pending >= thr or failed >= 1
    return {
        "escalate": escalate,
        "pending": pending,
        "failed": failed,
        "running": running,
        "threshold": thr,
        "reasons": (
            (["pending_ge_threshold"] if pending >= thr else [])
            + (["failed_ge_1"] if failed >= 1 else [])
        ),
    }


def _events_dir(root: Path | None) -> Path:
    return (root / "events") if root is not None else EVENTS_DIR


def _macos_notify(title: str, message: str) -> bool:
    try:
        script = f'display notification "{message}" with title "{title}"'
        subprocess.run(
            ["osascript", "-e", script],
            check=False,
            capture_output=True,
            timeout=10,
        )
        return True
    except (OSError, subprocess.SubprocessError):
        return False


def _try_discord(message: str) -> bool:
    try:
        from intel.core.discord import post_discord, resolve_webhook_url  # noqa: E402

        url = resolve_webhook_url()
        if not url:
            return False
        post_discord(message)
        return True
    except Exception:  # noqa: BLE001
        return False


def run_scale(*, dry_run: bool = False, root: Path | None = None) -> dict[str, Any]:
    ensure_layout(root)
    snap = should_escalate(root)
    if not snap["escalate"]:
        print(
            f"[scale] ok pending={snap['pending']} failed={snap['failed']} "
            f"(threshold={snap['threshold']})"
        )
        return {**snap, "event_path": None, "notified": False}

    msg = (
        f"XSP ops escalate: pending={snap['pending']} failed={snap['failed']} "
        f"running={snap['running']} reasons={snap['reasons']}"
    )

    if dry_run:
        print(f"[scale] dry-run would-escalate: {msg}")
        return {**snap, "event_path": None, "notified": False, "dry_run": True}

    ts = utc_now_iso().replace(":", "").replace("+", "Z")
    event = {
        "type": "escalate",
        "at": utc_now_iso(),
        "pending": snap["pending"],
        "failed": snap["failed"],
        "running": snap["running"],
        "threshold": snap["threshold"],
        "reasons": snap["reasons"],
        "message": msg,
    }
    event_path = _events_dir(root) / f"escalate_{ts}.json"
    write_json(event_path, event)

    notified = _try_discord(msg)
    if not notified:
        notified = _macos_notify("XSP Ops Escalate", msg[:180])

    print(f"[scale] escalate event={event_path} notified={notified}")
    return {**snap, "event_path": str(event_path), "notified": notified}
