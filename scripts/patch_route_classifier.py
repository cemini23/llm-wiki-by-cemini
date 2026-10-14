#!/usr/bin/env python3
"""Fix the source-target counter in route-task.ps1 (R1 follow-up, 2026-10-14).

R1 replaced prose keywords with target-file inspection, and counts distinct source
targets to pick mid vs hard. But it counts `$_.Value` of `$RouteSourceExt`, which is
the matched EXTENSION, not the filename. Four `.ts` targets therefore collapse to one
unique value (".ts") and route to mid.

Observed before the fix:

    route-task -DryClassify "refactor src/cli.ts src/router.ts src/worker.ts src/pick.ts …"
      Lane: mid   Why: software repo; 1 source target(s)

Expected: hard, 4 source target(s).

Usage: python3 scripts/patch_route_classifier.py [--check]
"""

from __future__ import annotations

import sys
from pathlib import Path

TARGET = Path.home() / "Projects/agent-toolkit/scripts/route-task.ps1"

OLD_PATTERN = (
    "$RouteSourceExt = '(?i)\\.(py|pyi|ts|tsx|js|jsx|mjs|cjs|rs|go|java|rb|cpp|cc|cxx|hpp|cs|php|swift|kt|scala|sh|ps1|psm1|sql|proto)\\b'\n"
)

NEW_PATTERN = (
    "$RouteSourceExt = '(?i)\\.(py|pyi|ts|tsx|js|jsx|mjs|cjs|rs|go|java|rb|cpp|cc|cxx|hpp|cs|php|swift|kt|scala|sh|ps1|psm1|sql|proto)\\b'\n"
    "# Whole filename, not just the extension. Counting $RouteSourceExt alone collapses four\n"
    "# `.ts` targets into one unique value (\".ts\"), so every multi-file task routed to mid.\n"
    "# Fixed 2026-10-14.\n"
    "$RouteSourceFile = '(?i)[\\w./\\\\-]+\\.(py|pyi|ts|tsx|js|jsx|mjs|cjs|rs|go|java|rb|cpp|cc|cxx|hpp|cs|php|swift|kt|scala|sh|ps1|psm1|sql|proto)\\b'\n"
)

OLD_COUNT = """        $distinct = @(
            [regex]::Matches($body, $RouteSourceExt) |
                ForEach-Object { $_.Value.ToLowerInvariant() } |
                Sort-Object -Unique
        ).Count
"""

NEW_COUNT = """        $distinct = @(
            [regex]::Matches($body, $RouteSourceFile) |
                ForEach-Object { $_.Value.ToLowerInvariant() } |
                Sort-Object -Unique
        ).Count
"""

REPLACEMENTS = [(OLD_PATTERN, NEW_PATTERN), (OLD_COUNT, NEW_COUNT)]


def main() -> int:
    check = "--check" in sys.argv
    if not TARGET.is_file():
        print(f"ERROR: {TARGET} not found", file=sys.stderr)
        return 2
    text = TARGET.read_text(encoding="utf-8")
    original = text
    for i, (old, new) in enumerate(REPLACEMENTS, 1):
        n = text.count(old)
        if n != 1:
            print(f"ERROR: replacement {i} matched {n} times (expected 1)", file=sys.stderr)
            print(f"  old: {old[:100]!r}", file=sys.stderr)
            return 1
        text = text.replace(old, new, 1)
        print(f"  ok  {i}. matched once")
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
