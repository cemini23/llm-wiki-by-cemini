---
title: Wiki gap detect Tier 1 cadence
type: concept
tags: [meta, wiki, gap-detect, cadence, k84]
keywords: [wiki-gap-detect, tier-1, needs-verification, cited-unread]
related:
  - concepts/cemini-workflow-tooling-audit-2026-05-30.md
  - concepts/exploration-graph-dead-ends.md
  - concepts/cemini-knowledge-application-architecture.md
maturity: core
created: 2026-05-30
updated: 2026-05-31
---

## Relations

- @concepts/cemini-workflow-tooling-audit-2026-05-30.md — K84 workflow adoption

## Narrative

| Field | Value |
|-------|-------|
| **Cadence** | Weekly (descriptive only — no auto Exa) |
| **Last run** | 2026-05-30 |
| **Next due** | 2026-06-06 |
| **Script** | `python3 scripts/wiki_gap_detect.py` |
| **Report** | `.local/reports/wiki-gap-detect-YYYY-MM-DD.txt` |

Run: `bash scripts/run_wiki_gap_detect.sh`  
Check due: `bash scripts/check_wiki_gap_detect_due.sh`

Tier 2 (proactive Exa) remains user-gated per ROADMAP.
