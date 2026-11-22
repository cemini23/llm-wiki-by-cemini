#!/usr/bin/env python3
"""Scan Phase-0 adoption scripts for blocked licenses.

Every `scripts/adopt_k*_phase0.sh` and `scripts/adopt-waves/adopt_k*_phase0.sh`
records the licence it saw for each repository. Those recordings are claims, not
readings, so this scanner re-classifies every one with `scripts/license_gate.py`
and prints the blocked hits.

Recognised row shapes:
  repo<TAB>tier<TAB>licence            (heredoc or array tables)
  | repo | tier | licence |           (markdown tables inside the report body)

Scripts are read, never executed. No network calls.

Usage:
  python3 scripts/check_phase0_licenses.py

Exit codes:
  0 — no blocked licence claim found
  1 — at least one blocked licence claim found
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))

from license_gate import classify, is_noncommercial  # noqa: E402

SCRIPT_PATTERNS = (
    "scripts/adopt_k*_phase0.sh",
    "scripts/adopt-waves/adopt_k*_phase0.sh",
)

# repo<TAB>tier<TAB>licence
TAB_ROW_RE = re.compile(
    r"^(?P<repo>[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)\t(?P<tier>[^\t]*)\t(?P<license>.+)$"
)
# | repo | tier | licence |
TABLE_ROW_RE = re.compile(
    r"^\s*\|\s*(?P<repo>[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)\s*\|"
    r"\s*(?P<tier>[^|]*)\|"
    r"\s*(?P<license>[^|]*)\|"
)

NONCOMMERCIAL_NOTE = "non-commercial model license — excluded from revenue repos"


def clean_license_cell(cell: str) -> str:
    """Drop markdown escapes, code ticks, and stray whitespace from a cell."""
    text = cell.replace("\\`", "").replace("`", "")
    text = text.replace("\\|", "|")
    return text.strip()


def iter_rows(path: Path):
    """Yield (line_number, repo, tier, license) for every licence row."""
    try:
        lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    except OSError:
        return
    for lineno, line in enumerate(lines, start=1):
        if line.lstrip().startswith("#"):
            continue
        match = TAB_ROW_RE.match(line)
        if match is None:
            match = TABLE_ROW_RE.match(line)
        if match is None:
            continue
        license_cell = clean_license_cell(match.group("license"))
        # Skip markdown separator rows: |---|---|
        if set(license_cell) <= {"-", ":", " "}:
            continue
        yield lineno, match.group("repo"), match.group("tier").strip(), license_cell


def main() -> int:
    scripts = sorted(
        path for pattern in SCRIPT_PATTERNS for path in ROOT.glob(pattern)
    )

    blocked = 0
    scanned = 0
    for path in scripts:
        rel = path.relative_to(ROOT)
        for lineno, repo, _tier, license_cell in iter_rows(path):
            scanned += 1
            if classify(license_cell) != "blocked":
                continue
            blocked += 1
            line = f"BLOCK  {rel}:{lineno}  {repo}  {license_cell}"
            if is_noncommercial(license_cell):
                line = f"{line}  — {NONCOMMERCIAL_NOTE}"
            print(line)

    print(
        f"check_phase0_licenses: {len(scripts)} script(s), "
        f"{scanned} licence row(s) scanned, {blocked} blocked"
    )
    return 1 if blocked else 0


if __name__ == "__main__":
    sys.exit(main())
