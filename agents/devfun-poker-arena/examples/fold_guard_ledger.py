"""P2-3 fold-guard ledger — fail-open audit hook for fold early-returns.

When a named fold guard fires, append a jsonl row so the next climb loop can
see which guards are doing the folding. No behavior change — logging only.
"""
from __future__ import annotations

import json
import os
from pathlib import Path


def fold_guards_path() -> Path | None:
    """Resolve fold-guard jsonl path — CEMINI_FOLD_GUARD_LOG_PATH or export dir."""
    raw = os.environ.get("CEMINI_FOLD_GUARD_LOG_PATH", "").strip()
    if raw:
        return Path(raw)
    export = os.environ.get("CEMINI_EXPORT_DIR", "").strip()
    if export:
        return Path(export) / "fold_guards.jsonl"
    return None


def record_fold_guard(
    guard_id: str,
    *,
    hand_class: str = "",
    position: str = "",
    spot: str = "",
) -> None:
    """Fail-open append to fold_guards.jsonl. Never raises."""
    try:
        path = fold_guards_path()
        if path is None:
            return
        path.parent.mkdir(parents=True, exist_ok=True)
        row = {
            "guard_id": guard_id,
            "hand_class": hand_class or None,
            "position": position or None,
            "spot": spot or None,
            "agent_version": os.environ.get("AGENT_VERSION", ""),
        }
        with path.open("a", encoding="utf-8") as fh:
            fh.write(json.dumps(row, separators=(",", ":")) + "\n")
    except Exception:
        pass
