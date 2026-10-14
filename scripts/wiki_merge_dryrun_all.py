#!/usr/bin/env python3
"""Rehearse the eight-wiki merge into a scratch tree and verify the link graph.

Builds the tree the merge would produce, then compares it against the union of the
eight pre-merge snapshots taken with --as-domain. Writes only inside --scratch.

This is the rehearsal the migration plan's 5.6 requires. It answers one question:
does every reference that resolved in the eight-repository layout resolve to the
same page in the merged layout. It does NOT exercise git history, which the
per-repository `dryrun` subcommand covers, and it does not touch a live repository.

Usage:
  python3 scripts/wiki_merge_dryrun_all.py [--scratch DIR] [--repos-root DIR]
"""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
HARNESS = HERE / "wiki_merge_manifest.py"

# Repository directory name -> federation id. The id is the domain name AND the key
# the egress cold store is built from, so it is not free to choose.
WIKIS = [
    ("OSINT WORKSPACE", "osint"),
    ("Cemini claude code CCC", "ccc"),
    ("Cybersecurity wiki", "cybersec"),
    ("SEO:GEO B&M Business", "seo"),
    ("Image gen", "image-gen"),
    ("Gambling wiki", "gambling"),
    ("Game Dev wiki", "game-dev"),
    ("3d printing", "3d-printing"),
]

SKIP = {".obsidian", ".git", "__pycache__", ".pytest_cache"}

# The CLAUDE.md whose federation table defines the ids. Any wiki's copy works; the
# osint one is canonical.
TABLE_SOURCE = ("OSINT WORKSPACE", "CLAUDE.md")


def run(*args):
    return subprocess.run([sys.executable, "-I", str(HARNESS), *args],
                          capture_output=True, text=True)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--scratch",
                    default=str(Path(tempfile.gettempdir()) / "cemini-merge-dryrun"),
                    help="scratch tree; removed and rebuilt on each run")
    ap.add_argument("--repos-root", default=str(Path.home() / "Projects"))
    args = ap.parse_args()

    scratch = Path(args.scratch).resolve()
    repos = Path(args.repos_root).resolve()
    work = scratch.parent / (scratch.name + "-snapshots")

    if scratch.exists():
        shutil.rmtree(scratch)
    work.mkdir(parents=True, exist_ok=True)
    (scratch / "wiki").mkdir(parents=True)

    print("STEP 1 — snapshot each wiki in its current layout")
    pre = []
    for repo, dom in WIKIS:
        src = repos / repo / "wiki"
        if not src.is_dir():
            print(f"  SKIP {repo}: no wiki/")
            continue
        out = work / f"pre-{dom}.json"
        r = run("snapshot", "--wiki", str(src), "--as-domain", dom, "--out", str(out))
        print(f"  {dom:<12} {r.stdout.strip() or r.stderr.strip()}")
        pre.append(out)

    print("\nSTEP 2 — union the pre-merge snapshots")
    union = work / "pre-union.json"
    print(f"  {run('concat', '--out', str(union), *[str(p) for p in pre]).stdout.strip()}")

    print("\nSTEP 3 — build the merged tree in scratch")
    for repo, dom in WIKIS:
        src = repos / repo / "wiki"
        if not src.is_dir():
            continue
        shutil.copytree(src, scratch / "wiki" / dom, ignore=shutil.ignore_patterns(*SKIP))
        print(f"  wiki/{dom:<12} {sum(1 for _ in (scratch / 'wiki' / dom).rglob('*.md'))} pages")

    src_claude = repos / TABLE_SOURCE[0] / TABLE_SOURCE[1]
    if not src_claude.is_file():
        print(f"ERROR: cannot read {src_claude}", file=sys.stderr)
        return 2
    rows = "\n".join(f"| `{dom}-wiki` | `wiki/{dom}/` | Public | merged domain |"
                     for _r, dom in WIKIS)
    table = re.compile(
        r"(\| Alias \| Path \| Visibility \| Description \|\n\|[-| ]+\|\n)(?:\|.*\|\n)+"
    )
    rewritten, n = table.subn(lambda m: m.group(1) + rows + "\n",
                              src_claude.read_text(encoding="utf-8"), count=1)
    if n != 1:
        print(f"  WARNING: federation table not rewritten (matches={n})")
    (scratch / "CLAUDE.md").write_text(rewritten, encoding="utf-8")
    print("  CLAUDE.md federation table rewritten to wiki/<domain>/")

    print("\nSTEP 4 — snapshot the merged tree")
    merged = work / "merged.json"
    print(f"  {run('snapshot', '--wiki', str(scratch / 'wiki'), '--label', 'merged', '--out', str(merged)).stdout.strip()}")

    print("\nSTEP 5 — compare")
    r = run("compare", "--before", str(union), "--after", str(merged))
    print(r.stdout)
    if r.stderr.strip():
        print(r.stderr, file=sys.stderr)
    return r.returncode


if __name__ == "__main__":
    sys.exit(main())
