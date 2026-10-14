#!/usr/bin/env python3
"""Remove the money lane from the Claude-desktop /route window skill (2026-10-14).

`~/.claude/skills/route/SKILL.md` is the parent doctrine for the DeepSeek-proxy window.
It still lists a `money` lane that agent-toolkit R1 deleted, so the two disagree.

Usage: python3 scripts/patch_route_window_skill.py [--check]
"""

from __future__ import annotations

import sys
from pathlib import Path

TARGET = Path.home() / ".claude/skills/route/SKILL.md"

REPLACEMENTS: list[tuple[str, str]] = [
    ("  Sort a task into easy, mid, hard, or money and outsource it with route-task.",
     "  Sort a task into easy, mid, or hard and outsource it with route-task."),
    ("## Hard and money plan", "## Hard plan"),
    ("| money | Scoring, payments, Greeks, P&L, LIVE, or ship. | Same path as hard. Do not go LIVE without LIVE OK. |\n", ""),
    ("| ambiguous | Unclear. | Ask: easy, mid, hard, or money? |",
     "| ambiguous | Unclear. | Ask: easy, mid, or hard? |"),
    ("| hard | Code, tests, or multi-file edits. | Write the Plan here on DeepSeek V4.1 Flash. Then `route-task` so Grok CLI implements. |",
     "| hard | Code, tests, or multi-file edits. | Write the Plan here on DeepSeek V4.1 Flash. Then `route-task` so Grok CLI implements. |\n| ~~money~~ | **Removed 2026-10-14.** Scoring, payments, Greeks, P&L, LIVE, ship. | Routes to **hard**. A live flip still needs LIVE OK. |"),
    ('metadata.version: "2026-10-01.1"', 'metadata.version: "2026-10-14.1"'),
]

CLASSIFIER_NOTE = """
**Lane comes from repository inspection, not prompt vocabulary (2026-10-14).** `route-task` reads
`WorkDir` and the named target files first. A documentation repository (`wiki/index.md`, no code
manifest) caps at **mid**, or **easy** for one or two markdown targets. A software repository is
**hard** at three or more executable source files, a schema or build signal, and **mid** below that.
The `money` lane was deleted; those tasks route to **hard**.
"""


def main() -> int:
    check = "--check" in sys.argv
    if not TARGET.is_file():
        print(f"ERROR: {TARGET} not found", file=sys.stderr)
        return 2
    text = TARGET.read_text(encoding="utf-8")
    original = text
    for i, (old, new) in enumerate(REPLACEMENTS, 1):
        n = text.count(old)
        if n == 1:
            text = text.replace(old, new, 1)
            print(f"  ok  {i}. applied")
            continue
        if n == 0 and (not new or new in text):
            # A deletion has no replacement text to look for; absent old text is the proof.
            print(f"  --  {i}. already applied")
            continue
        print(f"ERROR: replacement {i} matched {n} times (expected 1)", file=sys.stderr)
        print(f"  old: {old[:90]!r}", file=sys.stderr)
        return 1

    anchor = "\n## Close\n"
    if "Lane comes from repository inspection" not in text and anchor in text:
        text = text.replace(anchor, CLASSIFIER_NOTE + anchor, 1)
        print("  ok  +  classifier note")

    if check:
        print("\n--check only; nothing written")
        return 0
    if text == original:
        print("no change")
        return 0
    TARGET.write_text(text, encoding="utf-8")
    print(f"\nwrote {TARGET}  ({len(original)} -> {len(text)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
