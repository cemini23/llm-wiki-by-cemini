#!/usr/bin/env python3
"""Run merge-plan gates 1, 4 and 5. Re-runnable after any resolver change.

Gate 1  file manifest       exact 1:1 match on (key, sha256) across every page
Gate 4  git history         filter-repo + merge of unrelated histories, then
                            `git log --follow` must reach pre-merge commits
Gate 5  byte-identical      direct re-hash of merged files against their sources,
                            independent of any snapshot

Gate 2 (resolved edges) and gate 3 (lint) are covered by wiki_merge_dryrun_all.py
and by wiki_lint.py itself.

Writes only inside --scratch and its sibling snapshots directory. Never writes to a
live repository.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
REHEARSAL = HERE / "wiki_merge_dryrun_all.py"

# Repository directory name -> federation id.
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

# Subdirectories to sample when looking for deep history. Probing only the first
# pages alphabetically finds recent briefs and understates history badly.
HISTORY_SUBDIRS = ("concepts", "entities", "meta", "sources", "briefs", "projects", "runbooks")
HISTORY_SAMPLE = 40


def sh(*args, cwd=None, check=False):
    return subprocess.run(args, cwd=cwd, capture_output=True, text=True, check=check)


def sha(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def gate1(snaps):
    print("=" * 72)
    print("GATE 1 — file manifest: exact 1:1 match on (key, sha256)")
    print("=" * 72)
    union, merged = snaps / "pre-union.json", snaps / "merged.json"
    if not (union.is_file() and merged.is_file()):
        print("  ERROR: snapshots missing")
        return 1
    b = {f["key"]: f["sha256"] for f in json.loads(union.read_text())["files"]}
    a = {f["key"]: f["sha256"] for f in json.loads(merged.read_text())["files"]}
    missing = sorted(set(b) - set(a))
    added = sorted(set(a) - set(b))
    changed = sorted(k for k in b if k in a and b[k] != a[k])
    print(f"  before {len(b)} files   after {len(a)} files")
    print(f"  missing {len(missing)}   added {len(added)}   hash-changed {len(changed)}")
    for k in (missing + changed)[:5]:
        print(f"    {k}")
    ok = not (missing or added or changed)
    print(f"  GATE 1: {'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


def gate5(repos, tree):
    print()
    print("=" * 72)
    print("GATE 5 — byte-identical: re-hash merged files against their sources")
    print("=" * 72)
    checked = mismatched = missing = 0
    for repo, dom in WIKIS:
        src = repos / repo / "wiki"
        dst = tree / "wiki" / dom
        if not src.is_dir():
            continue
        for p in sorted(src.rglob("*.md")):
            rel = p.relative_to(src)
            q = dst / rel
            checked += 1
            if not q.is_file():
                missing += 1
                if missing <= 3:
                    print(f"    MISSING {dom}/{rel}")
            elif sha(p) != sha(q):
                mismatched += 1
                if mismatched <= 3:
                    print(f"    DIFFERS {dom}/{rel}")
    print(f"  files compared: {checked}   missing: {missing}   differing: {mismatched}")
    ok = not (missing or mismatched)
    print(f"  GATE 5: {'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


def gate4(repos, scratch):
    print()
    print("=" * 72)
    print("GATE 4 — git history survives filter-repo and merge")
    print("=" * 72)
    if scratch.exists():
        shutil.rmtree(scratch)
    scratch.mkdir(parents=True)
    target = scratch / "merged"

    r = sh("git", "clone", "-q", str(repos / "OSINT WORKSPACE"), str(target))
    if r.returncode:
        print(f"  ERROR clone: {r.stderr.strip()}")
        return 1
    r = sh("git", "-C", str(target), "filter-repo", "--force",
           "--path", "wiki/", "--path-rename", "wiki/:wiki/osint/")
    if r.returncode:
        print(f"  ERROR filter-repo osint: {r.stderr.strip()}")
        return 1
    print("  osint renamed to wiki/osint/")

    for repo, dom in WIKIS:
        if dom == "osint":
            continue
        src_repo = repos / repo
        if not (src_repo / "wiki").is_dir():
            continue
        tmp = scratch / f"import-{dom}"
        sh("git", "clone", "-q", str(src_repo), str(tmp), check=True)
        r = sh("git", "-C", str(tmp), "filter-repo", "--force",
               "--path", "wiki/", "--path-rename", f"wiki/:wiki/{dom}/")
        if r.returncode:
            print(f"    FAIL filter-repo {dom}: {r.stderr.strip()[:120]}")
            continue
        sh("git", "-C", str(target), "remote", "add", dom, str(tmp), check=True)
        sh("git", "-C", str(target), "fetch", "-q", dom, check=True)
        m = sh("git", "-C", str(target), "merge", "--allow-unrelated-histories",
               "--no-edit", "-q", f"{dom}/main")
        print(f"    {dom:<12} {'merged' if m.returncode == 0 else 'CONFLICT'}")

    print()
    print("  deepest history found per domain:")
    ok = True
    for _repo, dom in WIKIS:
        d = target / "wiki" / dom
        if not d.is_dir():
            continue
        best, best_rel = 0, None
        for sub in HISTORY_SUBDIRS:
            p = d / sub
            if not p.is_dir():
                p = d
            for f in sorted(p.rglob("*.md"))[:HISTORY_SAMPLE]:
                rel = f.relative_to(target)
                r = sh("git", "-C", str(target), "log", "--follow", "--oneline", "--", str(rel))
                n = len([l for l in r.stdout.strip().splitlines() if l])
                if n > best:
                    best, best_rel = n, rel
        if best == 0:
            ok = False
        print(f"    {dom:<12} {best:>4} commit(s)   {best_rel}")
    total = sh("git", "-C", str(target), "rev-list", "--count", "HEAD").stdout.strip()
    print(f"\n  merged repository commits: {total}")
    print(f"  GATE 4: {'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--scratch", default=str(Path(tempfile.gettempdir()) / "cemini-gates"))
    ap.add_argument("--repos-root", default=str(Path.home() / "Projects"))
    ap.add_argument("--skip-rehearsal", action="store_true",
                    help="reuse the existing snapshots instead of re-running the rehearsal")
    args = ap.parse_args()

    scratch = Path(args.scratch).resolve()
    repos = Path(args.repos_root).resolve()
    snaps = scratch.parent / (scratch.name + "-snapshots")

    if not args.skip_rehearsal:
        print("Running the rehearsal first (produces the snapshots gates 1 and 5 use).\n")
        r = subprocess.run(
            [sys.executable, "-I", str(REHEARSAL),
             "--scratch", str(scratch / "tree"), "--repos-root", str(repos)],
            capture_output=True, text=True,
        )
        if r.returncode != 0:
            print(r.stdout[-2000:])
            print(r.stderr[-1000:], file=sys.stderr)
            return 1
        # The rehearsal writes snapshots beside its scratch tree.
        snaps = scratch / "tree-snapshots"

    fails = 0
    for fn, kwargs in (
        (gate1, {"snaps": snaps}),
        (gate5, {"repos": repos, "tree": scratch / "tree"}),
        (gate4, {"repos": repos, "scratch": scratch / "git"}),
    ):
        try:
            fails += 1 if fn(**kwargs) else 0
        except Exception as exc:  # noqa: BLE001
            print(f"  ERROR in {fn.__name__}: {exc}")
            fails += 1

    print()
    print(f"OVERALL: {'PASS' if fails == 0 else f'{fails} GATE(S) FAILED'}")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
