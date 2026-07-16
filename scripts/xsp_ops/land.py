"""Land parsed signals as post JSON under state/posts/."""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

_SCRIPTS = Path(__file__).resolve().parents[1]
if str(_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS))

from intel.core.state import read_json, write_json  # noqa: E402

from xsp_ops.brain import load_brain, mark_landed, save_brain, utc_now_iso  # noqa: E402
from xsp_ops.paths import ensure_layout, posts_path  # noqa: E402


def land_signal(signal: dict[str, Any], root: Path | None = None) -> Path:
    ensure_layout(root)
    slug = signal["slug"]
    path = posts_path(slug, root)
    existing = read_json(path, {}) if path.is_file() else {}
    post: dict[str, Any] = {
        "slug": slug,
        "title": signal.get("title") or "",
        "url": signal.get("url") or "",
        "published": signal.get("published") or "",
        "source_path": signal.get("source_path") or "",
        "regime_tags": list(signal.get("regime_tags") or []),
        "excerpt": signal.get("excerpt") or "",
        "landed_at": utc_now_iso(),
        "priority": existing.get("priority"),
        "action": existing.get("action"),
        "triaged_at": existing.get("triaged_at"),
        "packet_path": existing.get("packet_path"),
    }
    # Preserve triage fields if re-landing
    write_json(path, post)
    return path


def run_land(
    *,
    dry_run: bool = False,
    root: Path | None = None,
    signals: list[dict[str, Any]] | None = None,
) -> list[str]:
    """Write post JSON for each signal; update brain post_ids / known_paths."""
    ensure_layout(root)
    brain = load_brain(root)
    if signals is None:
        signals = list(brain.get("last_parse_signals") or [])

    if dry_run:
        print(f"[land] dry-run: would land {len(signals)} post(s)")
        for s in signals:
            print(f"  - {s.get('slug')}")
        return [str(s.get("slug") or "") for s in signals]

    landed: list[str] = []
    for signal in signals:
        slug = signal.get("slug")
        if not slug:
            continue
        # Skip if already a post file and in brain
        pp = posts_path(slug, root)
        if pp.is_file() and slug in (brain.get("post_ids") or []):
            continue
        land_signal(signal, root)
        mark_landed(brain, slug, signal.get("source_path") or "")
        landed.append(slug)

    save_brain(brain, root)
    print(f"[land] landed {len(landed)} post(s)")
    return landed
