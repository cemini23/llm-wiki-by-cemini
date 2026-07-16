"""Filesystem work queue: pending → running → done | failed."""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

_SCRIPTS = Path(__file__).resolve().parents[1]
if str(_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS))

from intel.core.state import read_json, write_json  # noqa: E402

from xsp_ops.brain import utc_now_iso  # noqa: E402
from xsp_ops.paths import (  # noqa: E402
    QUEUE_DONE,
    QUEUE_FAILED,
    QUEUE_PENDING,
    QUEUE_RUNNING,
    ensure_layout,
    queue_path,
)

VALID_STATUSES = ("pending", "running", "done", "failed")


def _status_dir(status: str, root: Path | None) -> Path:
    if root is None:
        return {
            "pending": QUEUE_PENDING,
            "running": QUEUE_RUNNING,
            "done": QUEUE_DONE,
            "failed": QUEUE_FAILED,
        }[status]
    return root / "queue" / status


def list_jobs(status: str, root: Path | None = None) -> list[dict[str, Any]]:
    ensure_layout(root)
    d = _status_dir(status, root)
    jobs: list[dict[str, Any]] = []
    if not d.is_dir():
        return jobs
    for path in sorted(d.glob("*.json")):
        data = read_json(path, {})
        if isinstance(data, dict):
            data.setdefault("slug", path.stem)
            data["_path"] = str(path)
            jobs.append(data)
    return jobs


def count_jobs(status: str, root: Path | None = None) -> int:
    ensure_layout(root)
    d = _status_dir(status, root)
    if not d.is_dir():
        return 0
    return len(list(d.glob("*.json")))


def find_job(slug: str, root: Path | None = None) -> tuple[str, dict[str, Any]] | None:
    """Return (status, job) if slug exists in any queue bucket."""
    ensure_layout(root)
    for status in VALID_STATUSES:
        path = queue_path(status, slug, root)
        if path.is_file():
            data = read_json(path, {})
            if isinstance(data, dict):
                data.setdefault("slug", slug)
                return status, data
    return None


def write_pending(slug: str, root: Path | None = None, extra: dict[str, Any] | None = None) -> Path:
    """Create pending job if not already queued anywhere."""
    ensure_layout(root)
    existing = find_job(slug, root)
    if existing is not None:
        status, _ = existing
        return queue_path(status, slug, root)

    job: dict[str, Any] = {
        "slug": slug,
        "created_at": utc_now_iso(),
        "status": "pending",
    }
    if extra:
        job.update(extra)
    path = queue_path("pending", slug, root)
    write_json(path, job)
    return path


def move_job(
    slug: str,
    from_status: str,
    to_status: str,
    root: Path | None = None,
    updates: dict[str, Any] | None = None,
) -> Path:
    """Move job JSON between queue buckets; merge optional updates."""
    if from_status not in VALID_STATUSES or to_status not in VALID_STATUSES:
        raise ValueError(f"invalid status: {from_status} → {to_status}")
    ensure_layout(root)
    src = queue_path(from_status, slug, root)
    if not src.is_file():
        raise FileNotFoundError(f"queue job not found: {src}")
    job = read_json(src, {})
    if not isinstance(job, dict):
        job = {"slug": slug}
    if updates:
        job.update(updates)
    job["slug"] = slug
    job["status"] = to_status
    job["updated_at"] = utc_now_iso()
    dst = queue_path(to_status, slug, root)
    write_json(dst, job)
    if src.resolve() != dst.resolve():
        src.unlink(missing_ok=True)
    return dst


def pending_to_running(slug: str, root: Path | None = None, updates: dict[str, Any] | None = None) -> Path:
    return move_job(slug, "pending", "running", root=root, updates=updates)


def running_to_done(slug: str, root: Path | None = None, updates: dict[str, Any] | None = None) -> Path:
    return move_job(slug, "running", "done", root=root, updates=updates)


def running_to_failed(slug: str, root: Path | None = None, updates: dict[str, Any] | None = None) -> Path:
    return move_job(slug, "running", "failed", root=root, updates=updates)
