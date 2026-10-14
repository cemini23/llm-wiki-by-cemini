#!/usr/bin/env python3
"""Run one full ingest cycle against a merged wiki tree (migration plan 5.7.3).

"The migration is not complete until a real ingest works." This drops a synthetic
source into the merged inbox, drives every ingest-path consumer in schema order, and
reports which one breaks. It writes only inside the target tree and cleans up after.

Usage: python3 scripts/merge_ingest_cycle.py <merged-tree>
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

TREE = Path(sys.argv[1]).expanduser().resolve()
SCRIPTS = TREE / "scripts"
DOMAIN = "seo"


def run(label, script, *args, timeout=120):
    p = SCRIPTS / script
    if not p.is_file():
        print(f"  {label:<32} SKIP   ({script} not present)")
        return None
    try:
        r = subprocess.run(
            [sys.executable, "-I", str(p), *args],
            cwd=str(TREE), capture_output=True, text=True, timeout=timeout,
        )
    except subprocess.TimeoutExpired:
        print(f"  {label:<32} TIMEOUT (>%ds)" % timeout)
        return None
    first = ""
    for line in (r.stdout + r.stderr).splitlines():
        s = line.strip()
        if s and len(s) > 8 and not s.startswith(("=", "-", " ", "+")):
            first = s
            break
    print(f"  {label:<32} {'ok' if r.returncode == 0 else 'EXIT %d' % r.returncode:<7} {first[:62]}")
    return r


print("=" * 74)
print("POST-MERGE INGEST CYCLE  (plan 5.7.3)")
print("=" * 74)
print(f"  tree: {TREE}")
doms = sorted(p.name for p in (TREE / "wiki").iterdir() if p.is_dir())
print(f"  domains: {doms}")
print()

inbox = TREE / "research to be indexed"
inbox.mkdir(parents=True, exist_ok=True)
src = inbox / "merge-smoke-test.md"
src.write_text("# Merge smoke test\n\nSynthetic source for the post-merge ingest cycle.\n",
               encoding="utf-8")
print(f"STEP 1  wrote {src.relative_to(TREE)}")
print()

print("STEP 2  preingest duplicate check")
run("preingest_check", "preingest_check.py")
print()

print(f"STEP 3  write a source page into {DOMAIN}")
page = TREE / "wiki" / DOMAIN / "sources" / "merge-smoke-test.md"
page.parent.mkdir(parents=True, exist_ok=True)
page.write_text(
    "---\ntitle: Merge smoke test\ntype: source\nread_status: read\nupdated: 2026-10-14\n"
    "related:\n  - concepts/geo-aeo.md\n---\n\n## Raw Concept\n\nSynthetic. Removed after the run.\n\n"
    "## Narrative\n\nExercises the merged layout.\n",
    encoding="utf-8",
)
print(f"        wrote {page.relative_to(TREE)}")
print()

print("STEP 4  lint")
run("wiki_lint --fail-on-graph", "wiki_lint.py", "--fail-on-graph", timeout=600)
run(f"wiki_lint --domain {DOMAIN}", "wiki_lint.py", "--domain", DOMAIN, timeout=600)
print()

print("STEP 5  ingest gate and gap detection")
run("ingest_session_gate", "ingest_session_gate.py")
r = run("wiki_gap_detect", "wiki_gap_detect.py", timeout=600)
print()

print("STEP 6  remaining consumers named in 5.4")
for label, script in [
    ("wire_ledger_check", "wire_ledger_check.py"),
    ("cross_doc_dedup", "cross_doc_dedup.py"),
    ("wiki_source_index", "wiki_source_index.py"),
    ("skill_audit (brief)", "skill_audit.py"),
]:
    args = ("CLAUDE.md",) if script == "skill_audit.py" else ()
    run(label, script, *args)

page.unlink(missing_ok=True)
src.unlink(missing_ok=True)
print()
print("  cleaned up the synthetic page and inbox item")
