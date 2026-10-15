#!/usr/bin/env python3
"""Move the archived repos' inboxes into the merged wiki (migration plan 5.5).

Each absorbed repository kept its own `research to be indexed/`. That directory is
gitignored, so the merge did not touch it and the archived repo is its only home. Plan
5.5 makes emptying it a precondition of deleting the repo:

    "No archived repository is deleted until its inbox is empty."

This moves each domain's drops to `research to be indexed/<domain>/` in the merged repo.
Duplicates are reported, not silently merged: plan 5.5 hazard 2 names three arXiv PDFs
that sit in two inboxes each, and ingesting both copies makes two source pages.

Usage: python3 scripts/merge_migrate_inboxes.py [--check]
"""

from __future__ import annotations

import hashlib
import shutil
import sys
from pathlib import Path

PROJ = Path.home() / "Projects"
MERGED = PROJ / "OSINT WORKSPACE"
INBOX = MERGED / "research to be indexed"

SIBLINGS = [
    ("Cemini claude code CCC", "ccc"),
    ("Cybersecurity wiki", "cybersec"),
    ("SEO:GEO B&M Business", "seo"),
    ("Image gen", "image-gen"),
    ("Gambling wiki", "gambling"),
    ("Game Dev wiki", "game-dev"),
    ("3d printing", "3d-printing"),
]


def sha256(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def items(d: Path) -> list[Path]:
    if not d.is_dir():
        return []
    return sorted(p for p in d.iterdir() if p.is_file() and not p.name.startswith("."))


def main() -> int:
    check = "--check" in sys.argv

    known: dict[str, str] = {}  # sha256 -> "domain/name" already placed
    for p in items(INBOX / "osint"):
        known[sha256(p)] = f"osint/{p.name}"

    moves: list[tuple[Path, Path]] = []
    dupes: list[tuple[str, str, str]] = []

    for repo, dom in SIBLINGS:
        src = PROJ / repo / "research to be indexed"
        dst = INBOX / dom
        for p in items(src):
            h = sha256(p)
            if h in known:
                dupes.append((f"{dom}/{p.name}", known[h], h[:12]))
                continue
            target = dst / p.name
            known[h] = f"{dom}/{p.name}"
            moves.append((p, target))

    print(f"{'would move' if check else 'moving'}: {len(moves)} file(s)")
    for p, t in moves:
        print(f"  {p.parent.parent.name:<24} -> research to be indexed/{t.parent.name}/{t.name}")
    if dupes:
        print()
        print(f"DUPLICATES not moved ({len(dupes)}) — same content already in the inbox:")
        for a, b, h in dupes:
            print(f"  {a}  ==  {b}  (sha256 {h}…)")
        print("  Decide at ingest time which copy becomes the source page (plan 5.5 hazard 2).")

    if check:
        print("\n--check only; nothing written")
        return 0

    for _p, t in moves:
        t.parent.mkdir(parents=True, exist_ok=True)
    for p, t in moves:
        shutil.move(str(p), str(t))

    print()
    for repo, dom in SIBLINGS:
        src = PROJ / repo / "research to be indexed"
        left = len(items(src))
        print(f"  {dom:<12} left in archived inbox: {left}")

    print()
    print("per-domain inbox now:")
    for d in sorted(p for p in INBOX.iterdir() if p.is_dir()):
        print(f"  {d.name:<12} {len(items(d))} file(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
