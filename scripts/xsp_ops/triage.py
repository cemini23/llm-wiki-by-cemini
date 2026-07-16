"""Triage role: pending → running → apply rules → done; update post JSON."""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

_SCRIPTS = Path(__file__).resolve().parents[1]
if str(_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS))

from intel.core.state import read_json, write_json  # noqa: E402

from xsp_ops.brain import utc_now_iso  # noqa: E402
from xsp_ops.paths import ensure_layout, posts_path  # noqa: E402
from xsp_ops.queue import list_jobs, pending_to_running, running_to_done  # noqa: E402
from xsp_ops.triage_rules import triage_post  # noqa: E402


def _load_post(slug: str, root: Path | None) -> dict[str, Any]:
    path = posts_path(slug, root)
    data = read_json(path, {}) if path.is_file() else {}
    if not isinstance(data, dict):
        data = {}
    data.setdefault("slug", slug)
    return data


def _save_post(post: dict[str, Any], root: Path | None) -> Path:
    slug = post["slug"]
    path = posts_path(slug, root)
    write_json(path, post)
    return path


def run_triage(*, dry_run: bool = False, root: Path | None = None) -> list[dict[str, Any]]:
    ensure_layout(root)
    pending = list_jobs("pending", root)
    results: list[dict[str, Any]] = []

    if dry_run:
        print(f"[triage] dry-run: {len(pending)} pending job(s)")
        for job in pending:
            slug = job.get("slug") or ""
            post = _load_post(slug, root)
            decision = triage_post(post)
            print(f"  - {slug}: action={decision['action']} priority={decision['priority']}")
            results.append({"slug": slug, **decision})
        return results

    for job in pending:
        slug = job.get("slug") or ""
        if not slug:
            continue
        pending_to_running(slug, root)
        post = _load_post(slug, root)
        decision = triage_post(post)
        post["priority"] = decision["priority"]
        post["action"] = decision["action"]
        post["matched_keywords"] = decision["matched_keywords"]
        post["triage_reason"] = decision["reason"]
        post["triaged_at"] = utc_now_iso()
        _save_post(post, root)
        running_to_done(
            slug,
            root,
            updates={
                "priority": decision["priority"],
                "action": decision["action"],
                "matched_keywords": decision["matched_keywords"],
                "triage_reason": decision["reason"],
                "triaged_at": post["triaged_at"],
            },
        )
        results.append({"slug": slug, **decision})
        print(f"[triage] {slug}: {decision['action']}/{decision['priority']}")

    print(f"[triage] processed {len(results)} job(s)")
    return results
