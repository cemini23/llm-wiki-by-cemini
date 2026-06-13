#!/usr/bin/env python3
"""Quote @wiki-alias paths in YAML frontmatter so kb-server vault reindex parses them.

Unquoted `@alias/path` values are invalid YAML 1.1 (merge-key / alias syntax).
Fixes `related:` list items and `cross-wiki-*:` scalar fields only inside --- blocks.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
PROJECTS = REPO.parent / "projects"

WIKI_DIRS = [
    REPO / "wiki",
    PROJECTS / "Cemini claude code CCC" / "wiki",
    PROJECTS / "Image gen" / "wiki",
    PROJECTS / "3d printing" / "wiki",
    PROJECTS / "SEO:GEO B&M Business" / "wiki",
    PROJECTS / "Cybersecurity wiki" / "wiki",
    PROJECTS / "Gambling wiki" / "wiki",
    PROJECTS / "Game Dev wiki" / "wiki",
]

FM_RE = re.compile(r"\A(---\n)(.*?)(\n---\n)", re.DOTALL)
CROSS_WIKI_SCALAR = re.compile(r"^(cross-wiki-[a-z-]+):\s+(@\S+)\s*$")
RELATED_ITEM = re.compile(r"^(\s+-\s+)(@\S+)\s*$")
INLINE_ARRAY = re.compile(r"^(keywords|tags):\s*\[(.*)\]\s*$")


def _quote_inline_array_values(inner: str) -> tuple[str, int]:
    """Quote comma-separated inline list items that start with @."""
    parts = [p.strip() for p in inner.split(",")]
    changes = 0
    out: list[str] = []
    for part in parts:
        if part.startswith("@") and not (part.startswith('"') or part.startswith("'")):
            out.append(f'"{part}"')
            changes += 1
        else:
            out.append(part)
    return ", ".join(out), changes


def fix_frontmatter_block(fm: str) -> tuple[str, int]:
    changes = 0
    out: list[str] = []
    for line in fm.split("\n"):
        new_line = line
        m = CROSS_WIKI_SCALAR.match(line)
        if m:
            key, val = m.group(1), m.group(2)
            if not (val.startswith('"') and val.endswith('"')):
                new_line = f'{key}: "{val}"'
                changes += 1
        else:
            m2 = RELATED_ITEM.match(line)
            if m2:
                prefix, val = m2.group(1), m2.group(2)
                if not (val.startswith('"') and val.endswith('"')):
                    new_line = f'{prefix}"{val}"'
                    changes += 1
            else:
                m3 = INLINE_ARRAY.match(line)
                if m3 and "@" in m3.group(2):
                    key, inner = m3.group(1), m3.group(2)
                    fixed_inner, n = _quote_inline_array_values(inner)
                    if n:
                        new_line = f"{key}: [{fixed_inner}]"
                        changes += n
        out.append(new_line)
    return "\n".join(out), changes


def fix_file(path: Path) -> int:
    text = path.read_text(encoding="utf-8", errors="replace")
    m = FM_RE.match(text)
    if not m:
        return 0
    fixed_fm, n = fix_frontmatter_block(m.group(2))
    if n == 0:
        return 0
    path.write_text(m.group(1) + fixed_fm + m.group(3) + text[m.end() :], encoding="utf-8")
    return n


def main() -> int:
    total_files = 0
    total_edits = 0
    for wiki in WIKI_DIRS:
        if not wiki.is_dir():
            print(f"skip missing: {wiki}", file=sys.stderr)
            continue
        for md in sorted(wiki.rglob("*.md")):
            n = fix_file(md)
            if n:
                rel = md
                print(f"fixed {n} field(s): {rel}")
                total_files += 1
                total_edits += n
    print(f"done: {total_files} files, {total_edits} field(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
