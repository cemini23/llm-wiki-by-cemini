#!/usr/bin/env python3
"""Master scanner — run wiki_lint.py + wiki_gap_detect.py across every wiki.

This is a thin orchestrator: it adds no analysis logic of its own. It discovers
the wiki set from the "Related Wikis" table in CLAUDE.md (so new wikis are
picked up for free), runs the two existing scripts against each, parses their
summary lines, and prints one consolidated health table.

Usage:
  python3 scripts/wiki_scan_all.py                # consolidated table
  python3 scripts/wiki_scan_all.py --verbose      # + full per-wiki output
  python3 scripts/wiki_scan_all.py --wiki seo     # drill into one wiki
  python3 scripts/wiki_scan_all.py --write        # also write WIKI_HEALTH.md

Exit status is non-zero if any wiki has a structural finding (orphans,
dangling/missing links, bidirectional gaps, dangling cross-wiki links) so the
scanner can gate a pre-commit hook or a /loop run. Backlog-style findings
(cited-unread stubs, stale verification tags, thin concepts) do not fail the
run — they are tracked but not gating.
"""

import argparse
import os
import re
import subprocess
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CLAUDE_MD = ROOT / "CLAUDE.md"
LINT = ROOT / "scripts" / "wiki_lint.py"
GAP = ROOT / "scripts" / "wiki_gap_detect.py"

# Findings that indicate broken wiki structure — these gate the exit code.
GATING_KEYS = ("orphans", "dangling_related", "missing_path", "bidir_gaps", "xwiki_dangling")


def discover_wikis():
    """Parse the Related Wikis table in CLAUDE.md → list of (alias, abs_path).

    Same table regex wiki_lint.py uses. Paths in the table are relative to
    CLAUDE.md's directory; resolve them against ROOT.
    """
    if not CLAUDE_MD.exists():
        sys.exit(f"CLAUDE.md not found at {CLAUDE_MD}")
    text = CLAUDE_MD.read_text(errors="replace")
    table_re = re.compile(
        r"^\|\s*`([a-z0-9_-]+)`\s*\|\s*`?([^`\n\|]+)`?\s*\|", re.MULTILINE
    )
    wikis = []
    seen = set()
    for m in table_re.finditer(text):
        alias = m.group(1).strip()
        if alias in seen:
            continue
        path = (ROOT / m.group(2).strip().rstrip("/")).resolve()
        if path.is_dir():
            wikis.append((alias, path))
            seen.add(alias)
        elif (path / "wiki").is_dir():
            wikis.append((alias, path / "wiki"))
            seen.add(alias)
    return wikis


def run_lint(wiki_path):
    """Run wiki_lint.py against wiki_path; return (raw_output, parsed_dict)."""
    env = dict(os.environ, WIKI_DIR=str(wiki_path))
    proc = subprocess.run(
        [sys.executable, str(LINT)], capture_output=True, text=True, env=env
    )
    out = proc.stdout + proc.stderr
    return out, parse_lint(out)


def run_gap(wiki_path):
    """Run wiki_gap_detect.py against wiki_path; return (raw_output, parsed_dict)."""
    proc = subprocess.run(
        [sys.executable, str(GAP), "--wiki", str(wiki_path)],
        capture_output=True, text=True,
    )
    out = proc.stdout + proc.stderr
    return out, parse_gap(out)


def _first_int(pattern, text, default=None):
    m = re.search(pattern, text, re.MULTILINE)
    return int(m.group(1)) if m else default


def parse_lint(text):
    """Pull the numbered summary counts out of wiki_lint.py output."""
    return {
        "orphans": _first_int(r"^1\. Orphans\s*—\s*(\d+)", text),
        "bidir_gaps": _first_int(r"^2\. Bidirectional gaps\s*—\s*(\d+)", text),
        "dangling_related": _first_int(r"^3\. Dangling related:.*—\s*(\d+)", text),
        "missing_path": _first_int(r"^4\. @path body mentions.*—\s*(\d+)", text),
        "cited_unread": _first_int(r"^5\. Cited but unread.*—\s*(\d+)", text),
        "stale_verify": _first_int(r"^7\. Stale \[NEEDS VERIFICATION\].*—\s*(\d+)", text),
        "xwiki_dangling": _first_int(r"^8\. Cross-wiki.*—\s*(\d+) dangling", text),
        "fm_no": _first_int(r"no frontmatter at all:\s*(\d+)", text, 0),
        "fm_type": _first_int(r"missing 'type' field:\s*(\d+)", text, 0),
        "fm_maturity": _first_int(r"missing 'maturity' field[^:]*:\s*(\d+)", text, 0),
    }


def parse_gap(text):
    """Pull the Type A/D/E counts out of wiki_gap_detect.py output."""
    return {
        "gap_a": _first_int(r"Type A\b.*?\((\d+) found", text),
        "gap_d": _first_int(r"Type D\b.*?\((\d+) found", text),
        "gap_e": _first_int(r"Type E\b.*?\((\d+) found", text),
    }


def md_file_count(wiki_path):
    return sum(1 for _ in wiki_path.rglob("*.md"))


def fmt(v):
    return "-" if v is None else str(v)


# -- columns: (key, header) -------------------------------------------------
COLUMNS = [
    ("files", "Files"),
    ("orphans", "Orphan"),
    ("bidir_gaps", "Bidir"),
    ("dangling_related", "DangRel"),
    ("missing_path", "MissPath"),
    ("xwiki_dangling", "XWiki"),
    ("fm_issues", "FM"),
    ("cited_unread", "Unread"),
    ("stale_verify", "StaleVer"),
    ("gap_e", "Thin"),
]


def build_rows(results):
    rows = []
    for alias, _path, lint, gap, files in results:
        row = {"wiki": alias, "files": files}
        row.update(lint)
        row.update(gap)
        row["fm_issues"] = (lint.get("fm_no", 0) or 0) + (lint.get("fm_type", 0) or 0) \
            + (lint.get("fm_maturity", 0) or 0)
        rows.append(row)
    return rows


def render_table(rows):
    headers = ["Wiki"] + [h for _, h in COLUMNS]
    lines = ["| " + " | ".join(headers) + " |",
             "|" + "|".join(["---"] * len(headers)) + "|"]
    totals = {k: 0 for k, _ in COLUMNS}
    for r in rows:
        cells = [r["wiki"]] + [fmt(r.get(k)) for k, _ in COLUMNS]
        lines.append("| " + " | ".join(cells) + " |")
        for k, _ in COLUMNS:
            v = r.get(k)
            if isinstance(v, int):
                totals[k] += v
    lines.append("| **TOTAL** | " + " | ".join(f"**{totals[k]}**" for k, _ in COLUMNS) + " |")
    return "\n".join(lines)


def column_legend():
    return (
        "Orphan=no inbound refs · Bidir=asymmetric related: edges · "
        "DangRel=related: to missing file · MissPath=@path body mention to missing file · "
        "XWiki=dangling cross-wiki link · FM=frontmatter issues · "
        "Unread=cited-but-unread source stubs · StaleVer=[NEEDS VERIFICATION] >7d · "
        "Thin=concept page narrative <100 words"
    )


def main():
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("--wiki", metavar="ALIAS",
                    help="Scan only this wiki alias (and print its full lint+gap output)")
    ap.add_argument("--verbose", action="store_true",
                    help="Print full per-wiki lint + gap output below the table")
    ap.add_argument("--write", action="store_true",
                    help="Also write the consolidated report to WIKI_HEALTH.md")
    args = ap.parse_args()

    wikis = discover_wikis()
    if args.wiki:
        wikis = [(a, p) for a, p in wikis if a == args.wiki]
        if not wikis:
            sys.exit(f"No wiki alias '{args.wiki}' in CLAUDE.md Related Wikis table")

    results = []
    for alias, path in wikis:
        lint_out, lint = run_lint(path)
        gap_out, gap = run_gap(path)
        results.append((alias, path, lint, gap, md_file_count(path)))
        if args.verbose or args.wiki:
            print(f"\n{'#' * 30} {alias}  ({path}) {'#' * 30}")
            print(lint_out.rstrip())
            print(gap_out.rstrip())

    rows = build_rows(results)
    table = render_table(rows)

    report = [
        f"# Wiki Health Scan — {date.today().isoformat()}",
        "",
        table,
        "",
        column_legend(),
    ]
    print("\n" + "\n".join(report))

    if args.write:
        (ROOT / "WIKI_HEALTH.md").write_text("\n".join(report) + "\n")
        print(f"\nwrote {ROOT / 'WIKI_HEALTH.md'}")

    # Exit non-zero on any gating structural finding.
    gating = sum((r.get(k) or 0) for r in rows for k in GATING_KEYS)
    return 1 if gating else 0


if __name__ == "__main__":
    sys.exit(main())
