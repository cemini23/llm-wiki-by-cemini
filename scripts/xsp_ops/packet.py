"""Packet role: emit markdown packets for action=packet posts."""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

_SCRIPTS = Path(__file__).resolve().parents[1]
if str(_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS))

from intel.core.state import read_json, write_json  # noqa: E402

from xsp_ops.packet_render import existing_packet_for_slug, write_packet  # noqa: E402
from xsp_ops.paths import PACKETS_DIR, POSTS_DIR, ensure_layout, posts_path  # noqa: E402


def _packets_dir(root: Path | None) -> Path:
    return (root / "packets") if root is not None else PACKETS_DIR


def _posts_dir(root: Path | None) -> Path:
    return (root / "state" / "posts") if root is not None else POSTS_DIR


def run_packet(*, dry_run: bool = False, root: Path | None = None) -> list[str]:
    ensure_layout(root)
    posts_dir = _posts_dir(root)
    packets_dir = _packets_dir(root)
    written: list[str] = []

    if not posts_dir.is_dir():
        print("[packet] no posts dir")
        return written

    candidates: list[dict[str, Any]] = []
    for path in sorted(posts_dir.glob("*.json")):
        post = read_json(path, {})
        if not isinstance(post, dict):
            continue
        if post.get("action") != "packet":
            continue
        slug = post.get("slug") or path.stem
        if existing_packet_for_slug(packets_dir, slug) or post.get("packet_path"):
            continue
        candidates.append(post)

    if dry_run:
        print(f"[packet] dry-run: would write {len(candidates)} packet(s)")
        for p in candidates:
            print(f"  - {p.get('slug')}")
        return [str(p.get("slug") or "") for p in candidates]

    for post in candidates:
        slug = str(post.get("slug") or "")
        out = write_packet(post, packets_dir)
        post["packet_path"] = str(out)
        write_json(posts_path(slug, root), post)
        written.append(str(out))
        print(f"[packet] wrote {out}")

    print(f"[packet] created {len(written)} packet(s)")
    return written
