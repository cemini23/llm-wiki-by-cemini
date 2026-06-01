---
title: Architecture — briefs module
type: architecture-module
date: 2026-06-01
updated: 2026-06-01
project: "[[projects/osint-workspace/OSINT Workspace]]"
module: briefs
path: briefs/
scanned-commit: b960aae
tags: [architecture, briefs, distribution]
ai-first: true
related:
  - projects/osint-workspace/Architecture/Architecture - Overview.md
  - concepts/laptop-prod-research-split.md
maturity: validated
---

## Relations

- @projects/osint-workspace/Architecture/Architecture - Overview.md
- @concepts/laptop-prod-research-split.md

## For future Claude

**`briefs/`** is the **gitignored distribution staging area** (~300+ files locally): one-off deliverables for claude.ai copy-paste or `scp` to `cemini-prod:/opt/cemini/briefs/`. Not in git index; scan saw 2 tracked-adjacent references — treat as operational output, not library canon.

<!-- @generated:start -->

## Responsibility

**Deliberate exit ramp** from wiki research to consumers:

| Target | Mechanism |
| --- | --- |
| **claude.ai** | Operator copies brief body |
| **CeminiSuite** | Stage here → `skill_audit.py` PASS → user GO → server-Claude executes from `/opt/cemini/briefs/` |

Wiki pages hold durable truth; briefs hold **actionable, time-bound** instructions (engineering tasks, prod pulls, audits).

## Conventions

From root `CLAUDE.md`:

- Filename pattern: `YYYY-MM-DD_<slug>.md`
- Sections: `## Target`, `## Summary`, `## Body`, `## Sources`
- Pre-ship: `python3 scripts/skill_audit.py briefs/<file>.md`

## Boundaries

- **In scope from laptop:** write briefs, scp to `/opt/cemini/briefs/` only
- **Out of scope:** any other path under `/opt/cemini/` (read-only verify OK)

## Role in the whole

Completes the three-layer model (raw → wiki → **distribution**). Without briefs, ingest insights stay in the library and do not reach prod agents.

<!-- @generated:end -->
