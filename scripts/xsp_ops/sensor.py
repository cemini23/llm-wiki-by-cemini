"""Sensor role: Macro Charts RSS pull → brain audit."""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

_SCRIPTS = Path(__file__).resolve().parents[1]
if str(_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS))

from xsp_ops.brain import append_pull_log, load_brain, save_brain, utc_now_iso  # noqa: E402
from xsp_ops.paths import INBOX_DIR, ensure_layout  # noqa: E402


def _list_inbox_macro_paths() -> list[str]:
    if not INBOX_DIR.is_dir():
        return []
    paths: list[str] = []
    for pattern in ("macro-charts-*.md", "substack-rss-macrocharts-*.md"):
        for p in sorted(INBOX_DIR.glob(pattern)):
            paths.append(str(p))
    return paths


def run_sensor(*, dry_run: bool = False, root: Path | None = None) -> dict[str, Any]:
    """Pull Macro Charts feed (or dry-run audit only). Update brain.json."""
    ensure_layout(root)
    brain = load_brain(root)
    now = utc_now_iso()
    exit_code = 0
    items_seen = int(brain.get("items_seen") or 0)

    if dry_run:
        inbox_paths = _list_inbox_macro_paths()
        entry = {
            "at": now,
            "dry_run": True,
            "feed_id": "macrocharts",
            "items_seen": len(inbox_paths),
            "exit_code": 0,
            "note": "network skipped",
        }
        append_pull_log(brain, entry)
        brain["last_pull_at"] = now
        # Do not inflate items_seen on dry-run beyond current inbox count snapshot
        brain["inbox_paths"] = inbox_paths
        save_brain(brain, root)
        print(f"[sensor] dry-run: skip network; inbox_paths={len(inbox_paths)}; brain updated")
        return {"ok": True, "dry_run": True, "inbox_paths": inbox_paths, "exit_code": 0}

    try:
        from substack_rss_poller import load_config, poll_all  # noqa: E402

        cfg = load_config()
        feed = next((f for f in (cfg.get("feeds") or []) if f.get("id") == "macrocharts"), {})
        max_age = feed.get("max_age_days")
        exit_code = poll_all(
            cfg,
            dry_run=False,
            feed_id="macrocharts",
            max_age_days=int(max_age) if max_age is not None else None,
        )
    except Exception as exc:  # noqa: BLE001 — surface in pull_log
        exit_code = 1
        entry = {
            "at": now,
            "dry_run": False,
            "feed_id": "macrocharts",
            "error": str(exc),
            "exit_code": exit_code,
        }
        append_pull_log(brain, entry)
        brain["last_pull_at"] = now
        save_brain(brain, root)
        print(f"[sensor] poll failed: {exc}", file=sys.stderr)
        return {"ok": False, "dry_run": False, "exit_code": exit_code, "error": str(exc)}

    inbox_paths = _list_inbox_macro_paths()
    items_seen = len(inbox_paths)
    entry = {
        "at": now,
        "dry_run": False,
        "feed_id": "macrocharts",
        "items_seen": items_seen,
        "exit_code": int(exit_code or 0),
    }
    append_pull_log(brain, entry)
    brain["last_pull_at"] = now
    brain["items_seen"] = items_seen
    brain["inbox_paths"] = inbox_paths
    save_brain(brain, root)
    print(f"[sensor] pull done exit={exit_code} items_seen={items_seen}")
    return {
        "ok": int(exit_code or 0) == 0,
        "dry_run": False,
        "inbox_paths": inbox_paths,
        "items_seen": items_seen,
        "exit_code": int(exit_code or 0),
    }
