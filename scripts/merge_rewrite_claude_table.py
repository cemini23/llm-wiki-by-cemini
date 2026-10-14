#!/usr/bin/env python3
"""Rewrite the CLAUDE.md federation table for the merged layout (plan 5.4).

Before the merge the table maps each alias to a sibling checkout (`../Image gen/wiki/`).
After it, every domain is in-tree at `wiki/<domain>/`, and the resolver reads THIS table
to decide whether a bare `concepts/x.md` binds to the source page's own domain.

Without this step the merge "succeeds" and then 97,271 links silently stop resolving:
`domain_of()` sees no local domains, so a bare `@concepts/x.md` in a 3d-printing page
looks for `wiki/concepts/x.md` instead of `wiki/3d-printing/concepts/x.md`.

The Description column is preserved. Only Path changes.

Usage: python3 scripts/merge_rewrite_claude_table.py <merged-repo-root> [--check]
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

# Alias as written in the table -> merged domain directory. Both link spellings of the
# cybersecurity wiki exist in the wild (486 vs 15), and both must land on `cybersec`.
ALIAS_TO_DOMAIN = {
    "osint-wiki": "osint",
    "ccc-wiki": "ccc",
    "cybersecurity-wiki": "cybersec",
    "cybersec-wiki": "cybersec",
    "seo-wiki": "seo",
    "image-gen-wiki": "image-gen",
    "gambling-wiki": "gambling",
    "game-dev-wiki": "game-dev",
    "3d-printing-wiki": "3d-printing",
}

ROW = re.compile(r"^\|\s*`(?P<alias>[a-z0-9_-]+)`\s*\|\s*`?(?P<path>[^`|\n]+)`?\s*\|(?P<rest>.*)$")


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__.split("\n")[2], file=sys.stderr)
        return 2
    root = Path(sys.argv[1]).expanduser().resolve()
    check = "--check" in sys.argv
    target = root / "CLAUDE.md"
    if not target.is_file():
        print(f"ERROR: {target} not found", file=sys.stderr)
        return 2

    lines = target.read_text(encoding="utf-8").splitlines(keepends=True)
    changed = 0
    out = []
    for line in lines:
        m = ROW.match(line.rstrip("\n"))
        if not m:
            out.append(line)
            continue
        dom = ALIAS_TO_DOMAIN.get(m.group("alias"))
        if dom is None:
            out.append(line)
            continue
        new_path = f"wiki/{dom}/"
        if m.group("path").strip() == new_path:
            out.append(line)
            continue
        # `related:` aliases keep their own column widths by rebuilding the row.
        out.append(f"| `{m.group('alias')}` | `{new_path}` |{m.group('rest')}\n")
        changed += 1

    print(f"{changed} table row(s) rewritten to wiki/<domain>/")
    if check:
        print("--check only; nothing written")
        return 0
    if changed:
        target.write_text("".join(out), encoding="utf-8")
        print(f"wrote {target}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
