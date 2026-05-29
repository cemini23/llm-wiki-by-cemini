---
title: Claude AI trading operational workflows (SMB five practices)
type: concept
tags: [concept, claude, trading-workflow, operational-edge, k79]
keywords: [pine-script-alerts, pre-market-game-plan, performance-analytics, trailing-stop, trade-autopsy]
related:
  - entities/organizations/smb-capital.md
  - sources/smb-capital-youtube-week-2026-04-01.md
  - concepts/claude-code-trading-assistant-workflow-smb.md
  - concepts/pre-market-ai-research-briefing-smb.md
  - concepts/claude-code-skills-md-workflow.md
  - sources/smb-capital-youtube-week-2026-03-14.md
  - concepts/smb-elite-trader-summit-lessons.md
maturity: draft
created: 2026-05-29
updated: 2026-05-29
---

## Relations

- @entities/organizations/smb-capital.md — Garrett walkthrough
- @sources/smb-capital-youtube-week-2026-04-01.md — `Rqmdw4xyIMM` (2026-03-31)
- @concepts/claude-code-trading-assistant-workflow-smb.md — four-step dashboard build (Apr batch)
- @concepts/pre-market-ai-research-briefing-smb.md — email briefing variant
- @concepts/claude-code-skills-md-workflow.md — persistent skills vs ad-hoc prompts
- @sources/smb-capital-youtube-week-2026-03-14.md — summit lesson 7 (10 hrs/day Claude)
- @concepts/smb-elite-trader-summit-lessons.md — AI productivity bar

## Raw Concept

What prompted this page: SMB Capital YouTube *How to use Claude To Gain a Huge Day Trading Edge* (2026-03-31) — **operational infrastructure** (not prediction); five Claude-powered workflows.

## Narrative

Thesis: edge shifts from strategy access → **operating efficiency** (prep speed, alert precision, self-analysis quality). <10% of traders use AI; most use it wrong (market prediction) [TENTATIVE — SMB claim].

### Five practices [TENTATIVE]

| # | Practice | Output |
|---|----------|--------|
| **1** | **Custom price alerts** | Claude → Pine Script (or TOS) multi-condition alerts (e.g. ORH break + 1.5× OR volume + above VWAP + first 2h) |
| **2** | **Pre-market game plan** | Reusable template: watchlist + headlines + PM data → priority-ranked table + market context (~5 min) |
| **3** | **Custom performance analytics** | Python/pandas script on broker CSV — by setup type, time-of-day, day-of-week; pattern flags |
| **4** | **Custom exit logic** | Non-standard trailing stops (e.g. 2-bar high trail) as platform scripts |
| **5** | **AI trade autopsy** | EOD chart screenshot + full playbook context → objective rule-violation + coaching report |

### Prompting discipline

Specificity + complete context (entry/exit rules, emotional state, trade sequence) separates "10% better" from "10x" AI use [TENTATIVE].

### Cemini relevance

- Practice 2 overlaps pre-market briefing concepts — prod steal-from for prioritized watchlist generation.
- Practice 3 overlaps backtest/report kit — tag trades by setup for walk-forward discipline.
- Practice 5 parallels skill_audit / post-trade review — laptop workflow only unless playbook encoded in prod.
- TradingView Pine generation: note **TOS/licensing** constraints from prior evals (@sources/gemini-dr-wave4a-cemini-stack-2026-04-29.md tradingview-mcp TOS caveat).

## Snippets

> "This isn't prediction… This is operational infrastructure." [Source: SMB Capital YouTube Rqmdw4xyIMM, 2026-03-31]

> "The edge in trading isn't what you trade anymore… The edge is in how efficiently you operate." [Source: SMB Capital YouTube Rqmdw4xyIMM, 2026-03-31]
