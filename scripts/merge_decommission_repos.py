#!/usr/bin/env python3
"""Decommission the 7 absorbed repositories (migration plan 5.7.2, operator GO 2026-10-14).

Guards, in order. Every one must pass before anything moves.

  1. each archived inbox is empty, or holds only files byte-identical to a copy that
     already exists in the merged inbox (plan 5.5: no repo leaves with un-ingested work)
  2. the repo is clean and in sync with its own GitHub remote
  3. a backup tar exists for the domain

Then the repos move to ~/.Trash, not to oblivion: macOS keeps them until the Trash is
emptied, which is the local undo. The GitHub remotes are the real rollback, because the
merge rewrote this repository's history with git filter-repo and the pre-merge commit
SHAs exist nowhere else.

Usage: python3 scripts/merge_decommission_repos.py [--check]
"""

from __future__ import annotations

import hashlib
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path

PROJ = Path.home() / "Projects"
MERGED = PROJ / "OSINT WORKSPACE"
INBOX = MERGED / "research to be indexed"
TRASH = Path.home() / ".Trash"
BACKUPS = sorted(Path.home().glob(".cemini/wiki-merge-backup-*"))

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


def files(d: Path) -> list[Path]:
    if not d.is_dir():
        return []
    return sorted(p for p in d.iterdir() if p.is_file() and not p.name.startswith("."))


def main() -> int:
    check = "--check" in sys.argv
    problems: list[str] = []
    dupes: list[Path] = []

    print("1. inboxes")
    known = {sha256(p) for d in sorted(INBOX.iterdir()) if d.is_dir() for p in files(d)}
    for repo, dom in SIBLINGS:
        inbox = PROJ / repo / "research to be indexed"
        left = files(inbox)
        if not left:
            print(f"  ok    {dom:<12} empty")
            continue
        for p in left:
            if sha256(p) in known:
                dupes.append(p)
                print(f"  dupe  {dom:<12} {p.name[:56]} (identical copy already in the inbox)")
            else:
                problems.append(f"{dom}: {p.name} is not a duplicate and not migrated")
                print(f"  FAIL  {dom:<12} {p.name[:56]} NOT a duplicate")

    print()
    print("2. repos clean and pushed")
    for repo, dom in SIBLINGS:
        d = PROJ / repo
        if not (d / ".git").is_dir():
            print(f"  --    {dom:<12} no git")
            continue
        st = subprocess.run(["git", "-C", str(d), "status", "--porcelain"],
                            capture_output=True, text=True).stdout.strip()
        sb = subprocess.run(["git", "-C", str(d), "status", "-sb"],
                            capture_output=True, text=True).stdout.splitlines()
        head = sb[0] if sb else ""
        ok = not st and "ahead" not in head and "behind" not in head
        print(f"  {'ok  ' if ok else 'FAIL'}  {dom:<12} {head}")
        if not ok:
            problems.append(f"{dom}: dirty or not in sync ({head})")

    print()
    print("3. backups")
    if not BACKUPS:
        problems.append("no backup tar found")
        print("  FAIL  no ~/.cemini/wiki-merge-backup-* found")
    else:
        b = BACKUPS[-1]
        tars = sorted(b.glob("*.tar.gz"))
        print(f"  {b}")
        print(f"  {len(tars)} tar(s), {sum(t.stat().st_size for t in tars) / 1e6:.0f} MB")
        if len(tars) < 7:
            problems.append(f"only {len(tars)} backup tar(s)")

    print()
    if problems:
        print("BLOCKED:")
        for p in problems:
            print(f"  - {p}")
        return 1

    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    plan = [(PROJ / repo, TRASH / f"{repo} (archived-{stamp})") for repo, _d in SIBLINGS]
    print(f"READY. {'would delete' if check else 'deleting'} {len(dupes)} duplicate(s) "
          f"and move {len(plan)} repos to ~/.Trash")
    for p in dupes:
        print(f"  dupe  {p}")
    for src, dst in plan:
        print(f"  move  {src.name}  ->  ~/.Trash/{dst.name}")
    if check:
        print("\n--check only; nothing changed")
        return 0

    for p in dupes:
        p.unlink()
    TRASH.mkdir(exist_ok=True)
    for src, dst in plan:
        shutil.move(str(src), str(dst))
        print(f"  moved {src.name}")

    print()
    print("Done. Empting the Trash frees the disk; the GitHub remotes are the rollback.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
