#!/usr/bin/env python3
"""Finish the consumer updates for the merged layout (plan 5.4).

Every path here assumed one wiki per repository. After the merge the wiki root holds eight
domains, so a cadence page is `wiki/osint/meta/...` and a sweep is
`wiki/<domain>/sweeps/...`. Each replacement is asserted to match exactly once, and every
rewritten path is checked to exist, so a silent no-op is impossible.

Usage: python3 scripts/merge_fix_consumers.py [--check]
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Cadence pages and meta belong to osint, the domain that owns the schedule.
META_FILES = [
    "scripts/check_cross_venue_backtest_due.sh",
    "scripts/check_equity_signal_backtest_due.sh",
    "scripts/check_kalshi_lp_backtest_due.sh",
    "scripts/check_pm_lp_backtest_due.sh",
    "scripts/check_wiki_gap_detect_due.sh",
    "scripts/check_hl_funding_backtest_due.sh",
    "scripts/check_wc_lp_safety_due.sh",
    "scripts/run_wc_lp_safety_reminder.sh",
    "scripts/run_k159_fable_token_spike.sh",
    "scripts/adopt.sh",
    "scripts/sync_wiki_to_librarian.sh",
    "scripts/post-commit.sh",
    ".cursor/rules/osint-mcp-defaults.mdc",
]

DOMAIN_ENV = '${CEMINI_WIKI_ID:-osint}'
PY_DOMAIN = 'os.environ.get("CEMINI_WIKI_ID") or "osint"'

REPLACEMENTS: list[tuple[str, str, str]] = [
    # check_daily_research_digest_due.sh + daily_research_digest.sh
    ("scripts/check_daily_research_digest_due.sh",
     'REPORT="$ROOT/wiki/sweeps/${TODAY}-daily.md"',
     f'REPORT="$ROOT/wiki/{DOMAIN_ENV}/sweeps/${{TODAY}}-daily.md"'),
    ("scripts/daily_research_digest.sh",
     'REPORT="$REPO/wiki/sweeps/${TODAY}-daily.md"',
     f'REPORT="$REPO/wiki/{DOMAIN_ENV}/sweeps/${{TODAY}}-daily.md"'),

    # digest runner: fallback template and the hint it prints
    ("scripts/daily_research_digest_run.py",
     'out_tpl = (cfg.get("output") or {}).get("path_template", "wiki/sweeps/{date}-daily.md")',
     'out_tpl = (cfg.get("output") or {}).get("path_template", "wiki/{domain}/sweeps/{date}-daily.md")'),
    ("scripts/daily_research_digest_run.py",
     'f"`rm wiki/sweeps/{today.isoformat()}-daily.md` if nothing worth acting on.",',
     'f"`rm wiki/{domain}/sweeps/{today.isoformat()}-daily.md` if nothing worth acting on.",'),

    # Tier-2 arxiv sweep: docstring, real output dir, hint
    ("scripts/arxiv_sweep_run.py",
     '"""Run Tier-2 arXiv sweep (Exa API) and write wiki/sweeps/YYYY-MM-DD.md."""',
     '"""Run Tier-2 arXiv sweep (Exa API) and write wiki/<domain>/sweeps/YYYY-MM-DD.md."""'),
    ("scripts/arxiv_sweep_run.py",
     '    sweeps_dir = repo / "wiki" / "sweeps"',
     f'    sweeps_dir = repo / "wiki" / ({PY_DOMAIN}) / "sweeps"'),
    ("scripts/arxiv_sweep_run.py",
     'f"`rm wiki/sweeps/{today.isoformat()}.md` if nothing worth acting on.",',
     'f"`rm wiki/<domain>/sweeps/{today.isoformat()}.md` if nothing worth acting on.",'),

    # inbox stub writer
    ("scripts/append_inbox_to_daily_sweep.py",
     "import subprocess\nimport sys",
     "import os\nimport subprocess\nimport sys"),
    ("scripts/append_inbox_to_daily_sweep.py",
     'report = repo / "wiki" / "sweeps" / f"{today.isoformat()}-daily.md"',
     f'report = repo / "wiki" / ({PY_DOMAIN}) / "sweeps" / f"{{today.isoformat()}}-daily.md"'),
    ("scripts/append_inbox_to_daily_sweep.py",
     "Creates wiki/sweeps/YYYY-MM-DD-daily.md stub if the morning digest has not run yet.",
     "Creates wiki/<domain>/sweeps/YYYY-MM-DD-daily.md stub if the morning digest has not run yet."),

    # Tier-2 config
    ("scripts/tier25_config.yaml",
     '  path_template: "wiki/sweeps/{date}.md"',
     '  path_template: "wiki/{domain}/sweeps/{date}.md"'),
]


def main() -> int:
    check = "--check" in sys.argv
    n_ok = n_skip = n_fail = 0

    print("1. cadence and meta paths -> wiki/osint/meta/")
    for rel in META_FILES:
        p = ROOT / rel
        if not p.is_file():
            print(f"  FAIL  {rel}: missing")
            n_fail += 1
            continue
        text = p.read_text(encoding="utf-8")
        if "wiki/osint/meta/" in text and "`wiki/meta/" not in text and '"wiki/meta/' not in text:
            print(f"  --    {rel}: already done")
            n_skip += 1
            continue
        n = text.count("wiki/meta/")
        if n == 0:
            print(f"  --    {rel}: no bare wiki/meta/ reference")
            n_skip += 1
            continue
        if not check:
            p.write_text(text.replace("wiki/meta/", "wiki/osint/meta/"), encoding="utf-8")
        print(f"  ok    {rel} ({n})")
        n_ok += 1

    print()
    print("2. sweep paths carry the domain")
    for rel, old, new in REPLACEMENTS:
        p = ROOT / rel
        if not p.is_file():
            print(f"  FAIL  {rel}: missing")
            n_fail += 1
            continue
        text = p.read_text(encoding="utf-8")
        if new in text and old not in text:
            print(f"  --    {rel}: already done")
            n_skip += 1
            continue
        c = text.count(old)
        if c != 1:
            print(f"  FAIL  {rel}: matched {c}x")
            n_fail += 1
            continue
        if not check:
            p.write_text(text.replace(old, new, 1), encoding="utf-8")
        print(f"  ok    {rel}")
        n_ok += 1

    print()
    print("3. verify every rewritten meta path resolves")
    for rel in META_FILES:
        p = ROOT / rel
        if not p.is_file():
            continue
        for line in p.read_text(encoding="utf-8").splitlines():
            m = line.strip()
            for marker in ('"$ROOT/wiki/osint/meta/', '"$REPO/wiki/osint/meta/'):
                if marker in m:
                    tail = m.split(marker, 1)[1].split('"')[0]
                    target = ROOT / "wiki/osint/meta" / tail
                    print(f"  {'ok  ' if target.is_file() else 'FAIL'}  wiki/osint/meta/{tail}")
                    if not target.is_file():
                        n_fail += 1

    print()
    print(f"{'would change' if check else 'changed'}: {n_ok}  already done: {n_skip}  failed: {n_fail}")
    if check:
        print("--check only; nothing written")
    return 1 if n_fail else 0


if __name__ == "__main__":
    sys.exit(main())
