#!/usr/bin/env python3
"""Bring the private /route skill in line with agent-toolkit R1-R4 (2026-10-14).

The skill (v2.5.0) documents the money lane and the prose-keyword classifier. R1
deleted the money lane and replaced the classifier with repo inspection; R2-R4 added
an honest run log, a verify gate that can fail, and the scorecard. The skill is
`federation: true`, so the stale doctrine ships to every sibling repo.

Every replacement asserts it matched exactly once, so a silent no-op is impossible.

Usage: python3 scripts/patch_route_skill.py [--check]
"""

from __future__ import annotations

import sys
from pathlib import Path

TARGET = Path.home() / "Projects/agent-toolkit/.cursor/skills/route/SKILL.md"

OLD_DECISION = """### Pre-run decision rule (apply BEFORE announcing a lane)

Use only what is knowable **before** the run starts: `WorkDir`, target file types, target file count.

1. **money** — ONLY when `WorkDir` is a software repo AND the target touches live billing (Stripe / LicenseSeat), crypto or vault keys (`Ed25519` / `truth.ged`), `watches.json`, live Discord webhooks, or package publishing. **Markdown-only edits are never money.**
2. **easy** — all target paths are `.md` / `.txt`, count ≤ 2, and `## Verify` is a file-existence or static-lint check.
3. **mid (default)** — `WorkDir` is any wiki or hub repo, regardless of how many `.md` / `.mdc` files are touched; OR `WorkDir` is a software repo and the task changes **≤ 2** executable source files without touching a shared schema, state machine, or build config.
4. **hard** — ONLY when the task changes **≥ 3** executable source files, **or** alters a shared data schema / state machine / concurrency lock, **or** edits a build or packaging manifest (`pyproject.toml`, `Dockerfile`, `tauri.conf.json`).

**Why this rule exists.** A 295-run sample showed **48% of runs landing on `hard`** (141 of 295). The usual cause is the multi-file escalation heuristic firing on wiki ingests, which touch 3–15 markdown files by ingest rule — markdown volume is not implementation difficulty. In that same sample most `hard` runs executed inside markdown repos, and many `hard` runs exited non-zero having already fallen back from Grok to Flash: the premium lane bought nothing. Route wiki work and ≤2-file edits to **mid**.
"""

NEW_DECISION = """### Repo-aware classifier (Stage 1, v2.6)

Classification reads the **repository and the target files** before it reads the prompt. It runs in
Stage 1. There is no Stage-2 pass: the old escalation ran only when the lane was already `mid`, so it
never fired for the cases it was written for. It was deleted 2026-10-14.

1. **Inspect `WorkDir` first.** A *documentation repository* has `wiki/index.md` and **no** code
   manifest (`pyproject.toml`, `package.json`, `Cargo.toml`, `go.mod`, `Dockerfile`). Detect it that
   way — never by repository name against a list of wiki names, because the federation merge puts
   eight wiki domains under one `wiki/` directory.
2. **Documentation repository → capped at `mid`.** A task naming **at most two** markdown paths is
   `easy`. This is a cap, not a hint.
3. **Software repository → classify on target files, not verbs.** `hard` when the task changes
   **≥ 3** executable source files, alters a shared schema / state machine / concurrency lock, or
   edits a build or packaging manifest. **≤ 2** executable files is `mid`.
4. **Strip guardrail and NEVER blocks before any keyword test**, so `do not touch stripe` and
   `no tests needed` cannot fire the positive keyword. Anchored (`\\b`) keyword matching is a
   last-resort fallback only.

**Why the rewrite exists.** The old classifier matched unanchored substrings over prompt prose:
`bug` matched "bug bounty", `tests` matched "backtests", and `scoring` / `stripe` / `p&l` sent plain
markdown research to the premium lane. Negated guardrails poisoned it. The pre-merge docs-only guard
was unreachable dead code. Replayed over 60 real handoff prompts, the premium-lane share on unforced
prompts falls from **93% to 7%**, and `ambiguous` from 1 to 0.

**The `money` lane was removed 2026-10-14.** It was a thin wrapper around `hard` whose only distinct
behaviour was three duplicated guardrail bullets. Scoring, Stripe, Greeks, P&L, LIVE and ship tasks
now route to **hard**. The guardrail that mattered still applies: an explicit `LIVE OK` is required
before a live flip.
"""

REPLACEMENTS: list[tuple[str, str]] = [
    # frontmatter
    ("  Sort any task into easy / mid / hard / money and outsource it via one unified",
     "  Sort any task into easy / mid / hard and outsource it via one unified"),
    ('metadata.version: "2.5.0"', 'metadata.version: "2.6.0"'),
    ("# /route - unified task sorter (easy · mid · hard · money)",
     "# /route - unified task sorter (easy · mid · hard)"),

    # parent-Cursor section
    ("4. **Hard/money:** write the **plan** in this session with a **premium** model",
     "4. **Hard:** write the **plan** in this session with a **premium** model"),

    # SIP section
    ("Mid execute and hard/money implement require a SIP handoff: **WorkDir**, **Success criteria**, **Verify**, **NEVER**; hard/money also need a real **Plan**.",
     "Mid execute and hard implement require a SIP handoff: **WorkDir**, **Success criteria**, **Verify**, **NEVER**; hard also needs a real **Plan**."),
    ("Mid tasks that look like multi-file/tests/LIVE/secrets auto-escalate to hard/money unless forced with `mid:` / `deepseek:`.",
     "Lane comes from repository inspection, not prompt vocabulary - see **Repo-aware classifier** below. A legacy `money:` prefix still forces **hard**."),

    # lane table
    ("| **money** | Scoring, Stripe, Greeks, P&L, LIVE / ship | **Same as hard** + stricter money guardrails. Do not auto-LIVE. |\n", ""),
    ("| **ambiguous** | Unclear | Ask: easy / mid / hard / money? |",
     "| **ambiguous** | Unclear | Ask: easy / mid / hard? |"),

    # decision rule
    (OLD_DECISION, NEW_DECISION),

    # force prefixes
    ("Force prefixes: `easy:`, `mid:` / `deepseek:` / `opencode:`, `hard:`, `money:` (first line of multi-line prompts).",
     "Force prefixes: `easy:`, `mid:` / `deepseek:` / `opencode:`, `hard:` (first line of multi-line prompts). A legacy `money:` prefix still forces **hard**."),

    # operating rules
    ("2. Hard **and money**: Cursor premium writes plan; Grok CLI implements.",
     "2. Hard: Cursor premium writes plan; Grok CLI implements."),
    ("3. Money: same execute path as hard; require LIVE OK for live flips.",
     "3. Scoring / Stripe / P&L / LIVE / ship route to **hard**; a live flip still requires `LIVE OK`. The `money` lane was removed 2026-10-14."),

    # version note on the SIP heading
    ("## SIP + verify gates (v2.1)",
     "## SIP + verify gates (v2.1; the verify gate can now FAIL a route - R2, 2026-10-14)"),
]

RUNLOG_NOTE = """
## Run log, scorecard and resilience (R3/R4, 2026-10-14)

- **The log is honest.** `ClassifierWhy` records why a lane was chosen, and the field is no longer
  overwritten. Without it a classifier change cannot be proven.
- **The scorecard reads `_route_runs/`** and reports lane x outcome, lane x executor, lane x workdir,
  the **Wasted Premium Rate**, and a month trend. It runs after a `route-task` command.
- **Grok circuit breaker.** Grok implement failures can trip a breaker so the chain stops retrying a
  dead premium leg and falls through to Flash / OpenCode.
"""


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
            print(f"  old: {old[:90]!r}", file=sys.stderr)
            return 1
        text = text.replace(old, new, 1)
        print(f"  ok  {i:>2}. {old.splitlines()[0][:72]}")

    if "## Run log, scorecard and resilience" not in text:
        anchor = "\n## Related\n"
        if anchor not in text:
            print("ERROR: cannot find '## Related' anchor", file=sys.stderr)
            return 1
        text = text.replace(anchor, RUNLOG_NOTE + anchor, 1)
        print("  ok   +  run log / scorecard / breaker section")

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
