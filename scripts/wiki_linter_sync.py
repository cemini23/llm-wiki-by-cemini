#!/usr/bin/env python3
"""Keep the eight federation wiki linters identical.

Canon: this repository's scripts/wiki_lint.py and scripts/wiki_resolver.py.
Targets: the seven sibling wikis listed below.

  python3 scripts/wiki_linter_sync.py check   # exit 0 if identical, 1 if diverged
  python3 scripts/wiki_linter_sync.py sync    # copy the canon to every sibling

The linter is deliberately NOT carried by sync_federation_cursor_skills.sh. That
script's canon is the CCC repository, while the linter's canon is this one, and a
sync whose source and consumers disagree about which copy is canonical is a
plausible origin of the first divergence — which went unnoticed for about five
months, during which the seven siblings ran a linter predating the ambiguity check,
the basename navigation exemptions, and the gating of checks 4 and 8.

After the federation merge this whole problem disappears: one repository holds one
linter. This script covers the window before that.
"""

from __future__ import annotations

import argparse
import hashlib
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
CANON = HERE  # this repo's scripts/

# Sibling wiki repositories, relative to the projects root.
SIBLINGS = [
    "Cemini claude code CCC",
    "Cybersecurity wiki",
    "SEO:GEO B&M Business",
    "Image gen",
    "Gambling wiki",
    "Game Dev wiki",
    "3d printing",
]

FILES = ["wiki_lint.py", "wiki_resolver.py"]


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def targets(repos_root):
    for name in SIBLINGS:
        p = repos_root / name / "scripts"
        if p.is_dir():
            yield name, p


def cmd_check(args):
    repos_root = Path(args.repos_root).expanduser().resolve()
    canon_hashes = {f: sha256(CANON / f) for f in FILES}
    diverged = []
    print("canonical linter — this repository")
    for f in FILES:
        print(f"  {f:<20} {canon_hashes[f][:16]}")
    print("\nsiblings")
    for name, dst in targets(repos_root):
        problems = []
        for f in FILES:
            p = dst / f
            if not p.is_file():
                problems.append(f"{f}: missing")
            elif sha256(p) != canon_hashes[f]:
                problems.append(f"{f}: differs")
        if problems:
            diverged.append(name)
            print(f"  {name:<26} DIVERGED  ({'; '.join(problems)})")
        else:
            print(f"  {name:<26} identical")
    print()
    if diverged:
        print(f"DIVERGED: {len(diverged)} of {len(SIBLINGS)} sibling(s): {', '.join(diverged)}")
        print("Run: python3 scripts/wiki_linter_sync.py sync")
        return 1
    print(f"IN SYNC: all {len(SIBLINGS)} sibling(s) hold the canonical linter")
    return 0


def cmd_sync(args):
    repos_root = Path(args.repos_root).expanduser().resolve()
    changed = 0
    for name, dst in targets(repos_root):
        wrote = []
        for f in FILES:
            src, out = CANON / f, dst / f
            if out.is_file() and sha256(out) == sha256(src):
                continue
            shutil.copy2(src, out)
            wrote.append(f)
        if wrote:
            changed += 1
            print(f"  {name:<26} updated: {', '.join(wrote)}")
        else:
            print(f"  {name:<26} already identical")
    print(f"\n  {changed} sibling(s) updated")
    return cmd_check(args)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("cmd", choices=["check", "sync"])
    ap.add_argument("--repos-root", default=str(Path.home() / "Projects"))
    args = ap.parse_args()
    return {"check": cmd_check, "sync": cmd_sync}[args.cmd](args)


if __name__ == "__main__":
    sys.exit(main())
