#!/usr/bin/env python3
"""Deterministic bookkeeping for one wiki ingest batch.

Does the mechanical half of Steps 8-11 of the ingest SOP: bidirectional
`related[]` links, the domain `index.md` row, the domain `log.md` entry, raw
archive to egress, and the two gates. It does not judge content.

Usage:
  python3 scripts/wiki_finalize_batch.py --domain osint --summary "K297 — feeds"
  python3 scripts/wiki_finalize_batch.py --domain osint --archive-raw "research to be indexed/osint/a.pdf"
  python3 scripts/wiki_finalize_batch.py --domain osint --dry-run
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from datetime import date
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
REPO = SCRIPT_DIR.parent
WIKI = REPO / "wiki"

ALIASES = {
    "osint-wiki": "osint",
    "image-gen-wiki": "image-gen",
    "seo-wiki": "seo",
    "3d-printing-wiki": "3d-printing",
    "cybersecurity-wiki": "cybersec",
    "cybersec-wiki": "cybersec",
    "gambling-wiki": "gambling",
    "game-dev-wiki": "game-dev",
    "ccc-wiki": "ccc",
}
DOMAIN_ALIAS = {
    "osint": "osint-wiki",
    "image-gen": "image-gen-wiki",
    "seo": "seo-wiki",
    "3d-printing": "3d-printing-wiki",
    "cybersec": "cybersecurity-wiki",
    "gambling": "gambling-wiki",
    "game-dev": "game-dev-wiki",
    "ccc": "ccc-wiki",
}
PAGE_DIRS = ("sources", "entities", "concepts")


def git(*args: str) -> str:
    proc = subprocess.run(
        ["git", *args], cwd=REPO, capture_output=True, text=True, check=False
    )
    return proc.stdout if proc.returncode == 0 else ""


def touched_pages(domain: str) -> list[Path]:
    """New or modified .md pages under wiki/<domain>/{sources,entities,concepts}."""
    out = []
    for line in git("status", "--porcelain", "--", f"wiki/{domain}").splitlines():
        if len(line) < 4:
            continue
        status, path = line[:2], line[3:].strip()
        if status.strip() == "D":
            continue
        if " -> " in path:
            path = path.split(" -> ", 1)[1]
        rel = Path(path)
        if rel.suffix != ".md":
            continue
        parts = rel.parts
        if len(parts) < 4 or parts[0] != "wiki" or parts[1] != domain:
            continue
        if parts[2] not in PAGE_DIRS:
            continue
        out.append(REPO / rel)
    return sorted(set(out))


def split_frontmatter(text: str) -> tuple[list[str], list[str]]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return [], lines
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return lines[: i + 1], lines[i + 1 :]
    return [], lines


def parse_related(fm: list[str]) -> list[str]:
    rel: list[str] = []
    in_block = False
    for line in fm:
        if re.match(r"^related:\s*$", line):
            in_block = True
            continue
        if in_block:
            m = re.match(r"^\s+-\s*(.+?)\s*$", line)
            if m:
                rel.append(m.group(1).strip().strip("'\""))
                continue
            if line.strip() and not line.startswith(" "):
                in_block = False
    return rel


def resolve_target(value: str, domain: str) -> tuple[Path, str] | None:
    """(absolute path, target domain) for a related[] value, or None."""
    if value.startswith("@"):
        body = value[1:]
        if "/" not in body:
            return None
        alias, rest = body.split("/", 1)
        tdom = ALIASES.get(alias)
        if not tdom:
            return None
        return WIKI / tdom / rest, tdom
    return WIKI / domain / value, domain


def backlink_value(target_dom: str, target_rel: str, page_dom: str, page_rel: str) -> str:
    if target_dom == page_dom:
        return page_rel
    return f"@{DOMAIN_ALIAS.get(page_dom, page_dom + '-wiki')}/{page_rel}"


def add_related(text: str, value: str) -> str | None:
    """Insert value into the related[] block. None when already present."""
    fm, _ = split_frontmatter(text)
    if not fm:
        return None
    if value in parse_related(fm):
        return None
    for i, line in enumerate(fm):
        if re.match(r"^related:\s*$", line):
            j = i + 1
            last = i
            while j < len(fm) and re.match(r"^\s+-\s*", fm[j]):
                last = j
                j += 1
            if last == i:
                fm.insert(i + 1, f"  - {value}")
            else:
                fm.insert(last + 1, f"  - {value}")
            return "\n".join(fm + text.splitlines()[len(fm):]) + "\n"
    idx = len(fm) - 1  # before the closing ---
    fm[idx:idx] = ["related:", f"  - {value}"]
    body = text.splitlines()[len(fm) - 2:]
    return "\n".join(fm + body) + "\n"


def frontmatter_value(fm: list[str], key: str) -> str:
    for line in fm:
        m = re.match(rf"^{key}:\s*(.+?)\s*$", line)
        if m:
            return m.group(1).strip().strip("'\"")
    return ""


def ensure_index_row(domain: str, page: Path, dry_run: bool) -> bool:
    index = WIKI / domain / "index.md"
    if not index.exists():
        return False
    text = index.read_text(encoding="utf-8")
    if page.stem in text:
        return False
    section = {"sources": "## Sources", "entities": "## Entities", "concepts": "## Concepts"}[
        page.relative_to(WIKI / domain).parts[0]
    ]
    fm, _ = split_frontmatter(page.read_text(encoding="utf-8"))
    title = frontmatter_value(fm, "title") or page.stem
    rel = page.relative_to(WIKI / domain).as_posix()
    row = f"| [{title}]({rel}) | (added by wiki_finalize_batch) | draft |"
    lines = text.splitlines()
    try:
        start = next(i for i, ln in enumerate(lines) if ln.strip() == section)
    except StopIteration:
        idx = next(
            (i for i, ln in enumerate(lines) if ln.startswith("## Sources")),
            len(lines),
        )
        lines[idx:idx] = [section, "", "| Page | Summary | Maturity |", "|------|---------|----------|", row, ""]
    else:
        hdr = next((i for i in range(start, len(lines)) if lines[i].startswith("| Page |")), None)
        if hdr is None:
            lines[start + 1:start + 1] = ["", "| Page | Summary | Maturity |", "|------|---------|----------|", row]
        else:
            end = hdr
            while end + 1 < len(lines) and lines[end + 1].startswith("|"):
                end += 1
            lines.insert(end + 1, row)
    if not dry_run:
        index.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return True


def append_log(domain: str, summary: str, pages: list[Path], dry_run: bool) -> bool:
    log = WIKI / domain / "log.md"
    if not log.exists():
        return False
    today = date.today().isoformat()
    entry = [f"## [{today}] ingest | {summary}", ""]
    for p in pages:
        entry.append(f"- @{p.relative_to(WIKI / domain).as_posix()}")
    entry.append("")
    text = log.read_text(encoding="utf-8")
    if f"## [{today}] ingest | {summary}" in text:
        return False
    if not dry_run:
        log.write_text("\n".join(entry) + "\n" + text, encoding="utf-8")
    return True


def run(cmd: list[str]) -> int:
    print(f"==> {' '.join(cmd)}")
    return subprocess.run(cmd, cwd=REPO, check=False).returncode


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Deterministic bookkeeping for one wiki ingest batch."
    )
    ap.add_argument("--domain", required=True, help="wiki domain, e.g. osint")
    ap.add_argument("--summary", default="", help="1-line batch summary for log.md")
    ap.add_argument(
        "--archive-raw",
        nargs="+",
        default=[],
        metavar="FILE",
        help="raw source paths to archive to egress",
    )
    ap.add_argument("--dry-run", action="store_true", help="report, write nothing")
    ap.add_argument("--skip-gates", action="store_true", help="do not run lint/gate")
    args = ap.parse_args()

    if not (WIKI / args.domain).is_dir():
        print(f"error: no wiki domain {args.domain}", file=sys.stderr)
        return 2

    pages = touched_pages(args.domain)
    print(f"touched pages: {len(pages)}")
    for p in pages:
        print(f"  {p.relative_to(REPO)}")

    fixed = 0
    for page in pages:
        text = page.read_text(encoding="utf-8")
        fm, _ = split_frontmatter(text)
        page_rel = page.relative_to(WIKI / args.domain).as_posix()
        for value in parse_related(fm):
            resolved = resolve_target(value, args.domain)
            if not resolved:
                continue
            target, tdom = resolved
            if not target.exists():
                continue
            ttext = target.read_text(encoding="utf-8")
            tfm, _ = split_frontmatter(ttext)
            target_rel = target.relative_to(WIKI / tdom).as_posix()
            want = backlink_value(tdom, target_rel, args.domain, page_rel)
            new_text = add_related(ttext, want)
            if new_text is None:
                continue
            fixed += 1
            print(f"  backlink + {target.relative_to(REPO)}  <-  {want}")
            if not args.dry_run:
                target.write_text(new_text, encoding="utf-8")
    print(f"backlinks added: {fixed}")

    indexed = sum(ensure_index_row(args.domain, p, args.dry_run) for p in pages)
    print(f"index rows added: {indexed}")

    if args.summary:
        logged = append_log(args.domain, args.summary, pages, args.dry_run)
        print(f"log entry: {'added' if logged else 'skipped'}")
    else:
        print("log entry: skipped (no --summary)")

    for raw in args.archive_raw:
        if args.dry_run:
            print(f"  would archive: {raw}")
            continue
        rc = run(["bash", "scripts/archive_raw_to_egress.sh", "--wiki-id", args.domain, raw])
        if rc != 0:
            print(f"error: archive failed for {raw} (exit {rc})", file=sys.stderr)
            return rc

    if args.skip_gates or args.dry_run:
        print("gates: skipped")
        return 0
    lint = run([sys.executable, "scripts/wiki_lint.py", "--domain", args.domain])
    gate = run([sys.executable, "scripts/ingest_session_gate.py"])
    if lint != 0 or gate != 0:
        print("gates failed", file=sys.stderr)
        return 1
    print("gates passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
