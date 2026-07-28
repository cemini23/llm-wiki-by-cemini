---
title: WC LP safety re-run cadence
type: concept
tags: [meta, world-cup, lp-safety, cadence, k84]
keywords: [wc-lp-safety, gemini-dr, conviction-yaml, weekly]
related:
  - concepts/cemini-workflow-tooling-audit-2026-05-30.md
  - sources/gemini-wc-lp-team-safety-assessments-2026-05-30.md
  - sources/gemini-wc-conviction-config-audit-2026-05-31.md
  - concepts/polymarket-sports-lp-operating-rules.md
  - entities/tools/world-cup-bot.md
  - projects/world-cup-bot/Architecture/OPEN-GAPS.md
maturity: core
created: 2026-05-30
updated: 2026-05-31
---

## Relations

- @concepts/cemini-workflow-tooling-audit-2026-05-30.md — K84 workflow adoption
- @sources/gemini-wc-lp-team-safety-assessments-2026-05-30.md — source verdicts
- @sources/gemini-wc-conviction-config-audit-2026-05-31.md — full-matrix stale configuration audit input
- @entities/tools/world-cup-bot.md — `conviction.yaml` consumer

## Narrative

| Field | Value |
|-------|-------|
| **Cadence** | Weekly through 2026 FIFA World Cup window |
| **Last run** | 2026-07-28 |
| **Next due** | 2026-08-04 |
| **Owner** | world-cup-bot operator |
| **Prompt** | `world-cup-bot` repo `prompts/gemini-deep-research/03-team-lp-risk.md` |
| **Hard checkpoint** | 2026-06-06 pre-friendlies — update `conviction.yaml` if verdicts change |

Run: `bash scripts/run_wc_lp_safety_reminder.sh`  
Check due: `bash scripts/check_wc_lp_safety_due.sh`
