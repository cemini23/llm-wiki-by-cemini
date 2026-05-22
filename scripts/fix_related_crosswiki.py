#!/usr/bin/env python3
"""Remove @wiki-alias entries from related: frontmatter; fix @concepts/ to local paths.

Also provides add_related_backlink() for bidirectional repair — use that instead of
regex on `maturity:` (which strips the key name).
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

WIKI_ROOTS = [
    Path("/Users/claudiobarone/Desktop/projects/SEO:GEO B&M Business/wiki"),
]


def split_frontmatter(text: str) -> tuple[str | None, str]:
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return None, text
    return text[4:end], text[end + 5 :]


def fix_frontmatter(fm: str) -> tuple[str, bool]:
    changed = False
    out: list[str] = []
    for line in fm.split("\n"):
        if re.match(r"^  - @\w+-wiki/", line) or re.match(r'^  - "@\w+-wiki/', line):
            changed = True
            continue
        m = re.match(r"^  - @concepts/(.+)$", line)
        if m:
            out.append(f"  - concepts/{m.group(1)}")
            changed = True
            continue
        if re.match(r"^  - @image-gen-wiki/", line) or re.match(r'^  - "@image-gen-wiki/', line):
            changed = True
            continue
        out.append(line)
    return "\n".join(out), changed


def fix_file(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    fm, body = split_frontmatter(text)
    if fm is None:
        return False
    new_fm, changed = fix_frontmatter(fm)
    if not changed:
        return False
    path.write_text(f"---\n{new_fm}\n---\n{body}", encoding="utf-8")
    return True


def main() -> int:
    changed: list[Path] = []
    for root in WIKI_ROOTS:
        if not root.is_dir():
            continue
        for path in sorted(root.rglob("*.md")):
            if fix_file(path):
                changed.append(path)
    print(f"Fixed {len(changed)} files")
    for p in changed:
        print(f"  {p}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
