#!/usr/bin/env python3
"""Migrate wiki wire_status → harness_verb (FILE · KEEP · WIRE).

  python3 scripts/migrate_wire_status.py --dry-run
  python3 scripts/migrate_wire_status.py --apply
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"

# Old wire_status → harness_verb
MAP: dict[str, str] = {
    "policy_wired": "FILE",
    "wont_wire": "FILE",
    "watch": "FILE",
    "deferred": "FILE",
    "pending": "KEEP",
    "extract": "KEEP",
    "extract_only": "KEEP",
    "reference": "KEEP",
    "runtime_wired": "WIRE",
    "integrate": "WIRE",
}

WIRE_STATUS_RE = re.compile(r"^wire_status:\s*(\S+)\s*$", re.M)
WIRE_TARGET_RE = re.compile(r"^wire_target:.*\n", re.M)


def migrate_file(path: Path, *, apply: bool) -> tuple[str, str] | None:
    text = path.read_text(encoding="utf-8")
    if "---" not in text:
        return None
    m = WIRE_STATUS_RE.search(text)
    if not m:
        return None
    old = m.group(1)
    verb = MAP.get(old)
    if not verb:
        return (old, f"SKIP unknown wire_status={old}")
    new_text = WIRE_STATUS_RE.sub(f"harness_verb: {verb}", text, count=1)
    new_text = WIRE_TARGET_RE.sub("", new_text)
    if new_text == text:
        return (old, verb)
    if apply:
        path.write_text(new_text, encoding="utf-8")
    return (old, verb)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    if not args.apply:
        args.dry_run = True

    counts: dict[str, int] = {}
    changed = 0
    skipped: list[str] = []
    for md in sorted(WIKI.rglob("*.md")):
        if md.name in ("index.md", "log.md", "dashboard.md"):
            continue
        r = migrate_file(md, apply=args.apply)
        if not r:
            continue
        old, outcome = r
        if outcome.startswith("SKIP"):
            skipped.append(f"{md.relative_to(WIKI)}: {outcome}")
            continue
        counts[outcome] = counts.get(outcome, 0) + 1
        if args.apply:
            changed += 1
        else:
            print(f"  {md.relative_to(WIKI)}: {old} → {outcome}")

    mode = "APPLY" if args.apply else "DRY-RUN"
    print(f"{mode} harness_verb counts: {dict(sorted(counts.items()))}")
    if skipped:
        print(f"skipped {len(skipped)}")
        for s in skipped[:10]:
            print(f"  {s}")
    if args.apply:
        print(f"changed {changed} files")
    return 0


if __name__ == "__main__":
    sys.exit(main())
