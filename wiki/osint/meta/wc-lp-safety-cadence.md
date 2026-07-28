---
title: WC LP safety re-run cadence
type: concept
tags: [meta, world-cup, lp-safety, cadence, k84, retired]
keywords: [wc-lp-safety, gemini-dr, conviction-yaml, weekly, retired]
related:
  - concepts/cemini-workflow-tooling-audit-2026-05-30.md
  - sources/gemini-wc-lp-team-safety-assessments-2026-05-30.md
  - sources/gemini-wc-conviction-config-audit-2026-05-31.md
  - concepts/polymarket-sports-lp-operating-rules.md
  - entities/tools/world-cup-bot.md
  - projects/world-cup-bot/Architecture/OPEN-GAPS.md
maturity: draft
created: 2026-05-30
updated: 2026-07-28
---

## Relations

- @concepts/cemini-workflow-tooling-audit-2026-05-30.md — K84 workflow adoption
- @sources/gemini-wc-lp-team-safety-assessments-2026-05-30.md — source verdicts
- @sources/gemini-wc-conviction-config-audit-2026-05-31.md — full-matrix stale configuration audit input
- @entities/tools/world-cup-bot.md — former `conviction.yaml` consumer

## Narrative

| Field | Value |
|-------|-------|
| **Status** | **RETIRED 2026-07-28** — World Cup window over; operator dropped world-cup-bot |
| **Cadence** | ~~Weekly through FIFA WC window~~ — **disabled** |
| **Last run** | 2026-07-28 |
| **Next due** | — (never) |
| **Owner** | — |
| **Prompt** | historical: `world-cup-bot` `prompts/gemini-deep-research/03-team-lp-risk.md` |

`check_wc_lp_safety_due.sh` always exits **1** (not due). `run_wc_lp_safety_reminder.sh` is a no-op. LaunchAgent `com.cemini.wc-lp-safety-reminder` unloaded.

Historical DR: `@sources/gemini-wc-lp-team-safety-assessments-2026-05-30.md`. Do not prompt session-start for this cadence.
