#!/usr/bin/env python3
"""Phase 4 — mechanical pre-commit gates for wiki ingest sessions.

Does NOT replace human judgment (license claims, cross-wiki routing, takeaways
discussion). Flags common skip patterns before `git commit`.

Usage:
  python3 scripts/ingest_session_gate.py           # check staged + unstaged wiki changes
  python3 scripts/ingest_session_gate.py --strict  # exit 2 on any WARN
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from datetime import date
from pathlib import Path


def repo_root() -> Path:
    return Path(__file__).resolve().parent.parent


def git_lines(*args: str) -> list[str]:
    proc = subprocess.run(
        ["git", *args],
        cwd=repo_root(),
        capture_output=True,
        text=True,
        check=False,
    )
    if proc.returncode != 0:
        return []
    return [ln for ln in proc.stdout.splitlines() if ln.strip()]


def changed_files() -> list[Path]:
    repo = repo_root()
    paths: set[str] = set()
    for spec in (["diff", "--name-only"], ["diff", "--cached", "--name-only"]):
        paths.update(git_lines(*spec))
    return [repo / p for p in sorted(paths) if p.startswith("wiki/") or p.startswith("briefs/")]


def read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except OSError:
        return ""


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--strict", action="store_true", help="Exit 2 if any warning")
    args = parser.parse_args()

    repo = repo_root()
    today = date.today().isoformat()
    files = changed_files()
    wiki_files = [f for f in files if str(f).startswith(str(repo / "wiki"))]
    brief_files = [f for f in files if str(f).startswith(str(repo / "briefs"))]

    warns: list[str] = []
    infos: list[str] = []

    if not wiki_files and not brief_files:
        print("ingest_session_gate: no wiki/ or briefs/ changes — OK (nothing to gate)")
        return 0

    new_sources = [f for f in wiki_files if "/sources/" in str(f) and f.suffix == ".md"]
    new_tools = [f for f in wiki_files if "/entities/tools/" in str(f) and f.suffix == ".md"]
    log_path = repo / "wiki" / "log.md"
    index_path = repo / "wiki" / "index.md"
    log_text = read(log_path)
    index_text = read(index_path)

    if wiki_files:
        if f"## [{today}]" not in log_text and f"## {today}" not in log_text:
            warns.append(f"wiki/log.md: no entry dated {today} — append ingest log before commit")
        else:
            infos.append(f"wiki/log.md: dated entry found for {today}")

    for src in new_sources:
        slug = src.stem
        if slug not in index_text:
            warns.append(f"wiki/index.md: missing row for new source `{slug}`")

    for tool in new_tools:
        body = read(tool)
        if re.search(r"\bAdopt\b|\bCONDITIONAL-GO\b|\bSteal-from\b", body, re.I):
            if not re.search(
                r"MIT|Apache-2\.0|BSD|Unlicense|license|NO LICENSE|NO-GO|Phase-0|gh api|\[CONFIRMED|\[RETRACTED",
                body,
                re.I,
            ):
                warns.append(
                    f"{tool.relative_to(repo)}: adoption verdict without license verification anchor"
                )

    stale_nv = []
    for wf in wiki_files:
        # The log quotes old verification tags. Those lines are the record.
        if wf.name == "log.md":
            continue
        for m in re.finditer(r"\[NEEDS VERIFICATION (\d{4}-\d{2}-\d{2})\]", read(wf)):
            tag_date = date.fromisoformat(m.group(1))
            age = (date.today() - tag_date).days
            if age >= 7:
                stale_nv.append(f"{wf.relative_to(repo)} ({age}d)")
    if stale_nv:
        warns.append(f"Stale NEEDS VERIFICATION tags (≥7d): {', '.join(stale_nv[:5])}")

    for bf in brief_files:
        infos.append(f"Brief staged: {bf.relative_to(repo)} — run skill_audit before scp to prod")

    print("=== Ingest session gate (Phase 4 — mechanical only) ===")
    print("Human gates still required: discuss takeaways, cross-wiki routing, prod GO.")
    print("")
    for line in infos:
        print(f"  OK  {line}")
    for line in warns:
        print(f"  WARN  {line}")

    if warns:
        print("")
        print(f"{len(warns)} warning(s). Fix or acknowledge before commit.")
        return 2 if args.strict else 1
    print("")
    print("All mechanical checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
