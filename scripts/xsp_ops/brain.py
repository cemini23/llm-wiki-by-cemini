"""Brain JSON: audit log, known posts/paths, pull history."""

from __future__ import annotations

import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

_SCRIPTS = Path(__file__).resolve().parents[1]
if str(_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS))

from intel.core.state import read_json, write_json  # noqa: E402

from xsp_ops.paths import brain_path, ensure_layout  # noqa: E402

PULL_LOG_MAX = 20

DEFAULT_BRAIN: dict[str, Any] = {
    "last_pull_at": None,
    "items_seen": 0,
    "inbox_paths": [],
    "pull_log": [],
    "parsed_slugs": [],
    "parsed_paths": [],
    "post_ids": [],
    "known_paths": [],
}


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def empty_brain() -> dict[str, Any]:
    return dict(DEFAULT_BRAIN)


def load_brain(root: Path | None = None) -> dict[str, Any]:
    ensure_layout(root)
    path = brain_path(root)
    data = read_json(path, empty_brain())
    if not isinstance(data, dict):
        return empty_brain()
    # Normalize expected keys
    out = empty_brain()
    out.update(data)
    for key in ("inbox_paths", "pull_log", "parsed_slugs", "parsed_paths", "post_ids", "known_paths"):
        if not isinstance(out.get(key), list):
            out[key] = []
    return out


def save_brain(brain: dict[str, Any], root: Path | None = None) -> Path:
    ensure_layout(root)
    path = brain_path(root)
    # Cap pull_log
    log = list(brain.get("pull_log") or [])
    if len(log) > PULL_LOG_MAX:
        brain = dict(brain)
        brain["pull_log"] = log[-PULL_LOG_MAX:]
    write_json(path, brain)
    return path


def append_pull_log(brain: dict[str, Any], entry: dict[str, Any]) -> dict[str, Any]:
    """Append one pull audit row; keep last PULL_LOG_MAX."""
    log = list(brain.get("pull_log") or [])
    log.append(entry)
    brain["pull_log"] = log[-PULL_LOG_MAX:]
    return brain


def mark_parsed(brain: dict[str, Any], slug: str, source_path: str) -> dict[str, Any]:
    slugs = list(brain.get("parsed_slugs") or [])
    paths = list(brain.get("parsed_paths") or [])
    if slug not in slugs:
        slugs.append(slug)
    if source_path not in paths:
        paths.append(source_path)
    brain["parsed_slugs"] = slugs
    brain["parsed_paths"] = paths
    return brain


def mark_landed(brain: dict[str, Any], slug: str, source_path: str) -> dict[str, Any]:
    ids = list(brain.get("post_ids") or [])
    paths = list(brain.get("known_paths") or [])
    if slug not in ids:
        ids.append(slug)
    if source_path not in paths:
        paths.append(source_path)
    brain["post_ids"] = ids
    brain["known_paths"] = paths
    return brain
