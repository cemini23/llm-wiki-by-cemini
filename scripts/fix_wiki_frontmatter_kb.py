#!/usr/bin/env python3
"""Fix wiki frontmatter patterns that break kb-server vault YAML parse."""

from __future__ import annotations

import re
import sys
from pathlib import Path

WIKI_ROOTS = [
    Path("/Users/claudiobarone/Desktop/OSINT WORKSPACE/wiki"),
    Path("/Users/claudiobarone/Desktop/projects/Cemini claude code CCC/wiki"),
    Path("/Users/claudiobarone/Desktop/projects/Image gen/wiki"),
    Path("/Users/claudiobarone/Desktop/projects/3d printing/wiki"),
    Path("/Users/claudiobarone/Desktop/projects/SEO:GEO B&M Business/wiki"),
]

# Keys whose scalar values often contain colons and must be quoted for YAML 1.1
QUOTE_SCALAR_KEYS = frozenset(
    {"phase_0_verdict", "cross-wiki-source", "title", "summary", "note"}
)


def split_frontmatter(text: str) -> tuple[str | None, str]:
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return None, text
    return text[4:end], text[end + 5 :]


def _quoted(s: str) -> bool:
    s = s.strip()
    return (s.startswith('"') and s.endswith('"')) or (s.startswith("'") and s.endswith("'"))


def _yaml_quote(s: str) -> str:
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def fix_keywords_line(line: str) -> tuple[str, bool]:
    if "[" not in line or "@" not in line:
        return line, False
    prefix, rest = line.split("[", 1)
    inner, suffix = rest.rsplit("]", 1)
    items = [x.strip() for x in inner.split(",")]
    changed = False
    new_items: list[str] = []
    for it in items:
        if "@" in it and not _quoted(it):
            new_items.append(_yaml_quote(it))
            changed = True
        else:
            new_items.append(it)
    if not changed:
        return line, False
    return f"{prefix}[{', '.join(new_items)}]{suffix}", True


def fix_scalar_line(key: str, val: str) -> tuple[str, bool]:
    val = val.strip()
    if not val or _quoted(val) or val.startswith(">"):
        return f"{key}: {val}", False
    # Quote if value has @ (YAML alias) or colon after first token (mapping confusion)
    needs = val.startswith("@") or (":" in val and key in QUOTE_SCALAR_KEYS)
    if key == "phase_0_verdict" and ":" in val:
        needs = True
    if not needs:
        return f"{key}: {val}", False
    return f"{key}: {_yaml_quote(val)}", True


def fix_frontmatter(fm: str) -> tuple[str, bool]:
    changed = False
    out: list[str] = []
    for line in fm.split("\n"):
        if re.match(r"^  - @", line):
            changed = True
            continue
        m = re.match(r"^([\w-]+):\s*(.*)$", line)
        if not m:
            out.append(line)
            continue
        key, val = m.group(1), m.group(2)
        if key == "keywords":
            new_line, ch = fix_keywords_line(line)
            if ch:
                changed = True
            out.append(new_line)
            continue
        if key in QUOTE_SCALAR_KEYS or key == "phase_0_verdict":
            new_line, ch = fix_scalar_line(key, val)
            if ch:
                changed = True
            out.append(new_line)
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
            print(f"skip missing: {root}", file=sys.stderr)
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
