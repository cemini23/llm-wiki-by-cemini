#!/usr/bin/env python3
"""Point federation_paths.yaml at the merged wiki (migration plan 5.4).

Each of the eight wiki entries used to name its own repository. After the merge they
share one root, so `wiki_dir` becomes `wiki/<id>` and `inbox_dir` becomes
`research to be indexed/<id>`.

Line-oriented on purpose: the file carries comments and unrelated entries (code repos,
prod monitors) that a YAML round-trip would reflow or drop.

Usage: python3 scripts/merge_fix_federation_paths.py [--check]
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

HUB = Path.home() / "Projects/cemini-federation-hub/federation_paths.yaml"
MERGED_ROOT = "/Users/claudiobarone/Projects/OSINT WORKSPACE"
WIKIS = ["osint", "ccc", "seo", "image-gen", "gambling", "game-dev", "cybersec", "3d-printing"]

ENTRY = re.compile(r"^\s*-\s*id:\s*(\S+)\s*$")


def main() -> int:
    check = "--check" in sys.argv
    if not HUB.is_file():
        print(f"ERROR: {HUB} not found", file=sys.stderr)
        return 2

    lines = HUB.read_text(encoding="utf-8").splitlines(keepends=True)
    out: list[str] = []
    current = None
    changed: list[str] = []

    for line in lines:
        m = ENTRY.match(line)
        if m:
            current = m.group(1)
        if current in WIKIS:
            stripped = line.rstrip("\n")
            if stripped.lstrip().startswith("root:"):
                new = f'    root: "{MERGED_ROOT}"\n'
                if line != new:
                    changed.append(f"{current}: root")
                out.append(new)
                continue
            if stripped.lstrip().startswith("wiki_dir:"):
                new = f"    wiki_dir: wiki/{current}\n"
                if line != new:
                    changed.append(f"{current}: wiki_dir")
                out.append(new)
                continue
            if stripped.lstrip().startswith("inbox_dir:"):
                new = f'    inbox_dir: "research to be indexed/{current}"\n'
                if line != new:
                    changed.append(f"{current}: inbox_dir")
                out.append(new)
                continue
            if stripped.lstrip().startswith("briefs_dir:"):
                # Only ccc merged an in-tree briefs/ (the others keep theirs at repo
                # root in the archived repositories). Point at it where it exists and
                # drop the field where it does not, so pending_briefs() does not look
                # in a directory that never existed.
                bdir = Path(MERGED_ROOT) / "wiki" / current / "briefs"
                if bdir.is_dir():
                    new = f"    briefs_dir: wiki/{current}/briefs\n"
                    if line != new:
                        changed.append(f"{current}: briefs_dir -> wiki/{current}/briefs")
                    out.append(new)
                else:
                    changed.append(f"{current}: dropped briefs_dir (none in-tree)")
                continue
        out.append(line)

    if not changed:
        print("already merged-shaped; nothing to change")
        return 0

    for c in changed:
        print(f"  {c}")
    print(f"\n{len(changed)} change(s)")
    if check:
        print("--check only; nothing written")
        return 0
    HUB.write_text("".join(out), encoding="utf-8")
    print(f"wrote {HUB}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
