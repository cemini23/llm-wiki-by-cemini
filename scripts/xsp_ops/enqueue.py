"""Enqueue landed posts that lack a queue job."""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

_SCRIPTS = Path(__file__).resolve().parents[1]
if str(_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS))

from intel.core.state import read_json  # noqa: E402

from xsp_ops.brain import load_brain  # noqa: E402
from xsp_ops.paths import POSTS_DIR, ensure_layout  # noqa: E402
from xsp_ops.queue import find_job, write_pending  # noqa: E402


def _list_post_slugs(root: Path | None) -> list[str]:
    ensure_layout(root)
    if root is None:
        posts_dir = POSTS_DIR
    else:
        posts_dir = root / "state" / "posts"
    if not posts_dir.is_dir():
        return []
    return sorted(p.stem for p in posts_dir.glob("*.json"))


def run_enqueue(*, dry_run: bool = False, root: Path | None = None) -> list[str]:
    ensure_layout(root)
    brain = load_brain(root)
    slugs = set(_list_post_slugs(root))
    slugs |= set(brain.get("post_ids") or [])

    to_enqueue: list[str] = []
    for slug in sorted(slugs):
        if find_job(slug, root) is not None:
            continue
        to_enqueue.append(slug)

    if dry_run:
        print(f"[enqueue] dry-run: would enqueue {len(to_enqueue)}")
        for s in to_enqueue:
            print(f"  - {s}")
        return to_enqueue

    created: list[str] = []
    for slug in to_enqueue:
        write_pending(slug, root)
        created.append(slug)
    print(f"[enqueue] enqueued {len(created)} job(s)")
    return created
