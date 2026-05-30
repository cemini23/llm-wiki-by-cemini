---
title: Production trading blind spots — slow-discovery failure catalog
type: concept
tags: [concept, operations, trading-bot, debugging, lightbulb-moments, cemini-prod, k75]
keywords: [blind-spots, phantom-win, logic_version, over-logging, reconciliation, duplicate-fill, source-of-truth, months-to-find]
related:
  - concepts/pnl-attribution-versioning.md
  - concepts/trading-bot-logging-discipline.md
  - concepts/polymarket-bot-architecture.md
  - concepts/multi-module-bot-conflict-detector-pattern.md
  - concepts/perps-dex-funding-carry-strategy.md
  - concepts/trading-dashboard-api-wiring.md
  - sources/x-polymarket-bot-playbook-punisher-2026-05.md
  - sources/trading-posts-2-time-series-openhuman-conflict-detector-lp-tactics-2026-05.md
  - concepts/zero-trade-edge-signal-diagnostics.md
  - sources/algorithmic-trading-pipeline-zero-trade-analysis-2026-05-28.md
  - concepts/shadow-to-live-transition-engineering.md
  - sources/algorithmic-trading-live-transition-strategies-2026-05-28.md
  - concepts/equity-fair-value-evaluation.md
  - concepts/tick-staleness-ingestion-diagnosis.md
  - sources/low-latency-tick-staleness-diagnosis-2026-05-28.md
  - entities/tools/world-cup-bot.md
  - sources/gemini-wc-inplay-pregame-lp-risks-2026-05-30.md
  - sources/gemini-wc-tournament-phase-router-2026-05-30.md
  - sources/gemini-github-sports-betting-repos-landscape-2026-05-30.md
maturity: validated
created: 2026-05-28
updated: 2026-05-29
---

## Relations

- @concepts/pnl-attribution-versioning.md — prod fix for the months-long PnL version mixing case
- @concepts/trading-bot-logging-discipline.md — over-logging hides the signals needed to spot these early
- @concepts/polymarket-bot-architecture.md — execution > strategy; reconciliation cadence
- @concepts/multi-module-bot-conflict-detector-pattern.md — broken-data corrupts gates silently
- @concepts/perps-dex-funding-carry-strategy.md — one-leg-open failure mode
- @concepts/trading-dashboard-api-wiring.md — UI without version metadata reinforces false confidence
- @sources/x-polymarket-bot-playbook-punisher-2026-05.md — 30s reconciliation minimum
- @sources/trading-posts-2-time-series-openhuman-conflict-detector-lp-tactics-2026-05.md — journal vs CSV truth
- @concepts/zero-trade-edge-signal-diagnostics.md — silent zero-trade aborts (K76)
- @sources/algorithmic-trading-pipeline-zero-trade-analysis-2026-05-28.md — three-domain framework source

## Raw Concept

What prompted this page: repeated pattern where Cemini (and independent Polymarket operators) spent **weeks to months** discovering operational bugs that look like strategy failure. Goal: a checklist wiki page that shortens time-to-diagnosis by naming failure classes before you feel them in PnL.

## Narrative

### How to use this page

When headline PnL "doesn't make sense," scan the table **top to bottom** before tuning alpha. Most rows are infrastructure/attribution — not model edge.

| # | Blind spot | Symptom | Early signal | Fix (Cemini prod where applicable) |
|---|------------|---------|--------------|-----|
| 1 | **PnL logic unversioned** | "Was profitable last month" after code change | Win rate shifts exactly at deploy date | @concepts/pnl-attribution-versioning.md — `logic_version` + `--scope current` |
| 2 | **Internal counter ≠ venue truth** | Bot journal WR >> exchange export | Polymarket CSV disagrees with bot stats | Reconcile to venue export; @Gustafssonkotte CSV rule |
| 3 | **Phantom WIN / assume-filled** | Risk gates no-op; ghost profits | "WIN" rows with no matching fill | Poll order status; never infer fill from timeout |
| 4 | **Duplicate fill events** | Double-counted position / 2× PnL | Same `order_id` twice in log window | Dedup in formatter (QuantPython trade-journal pattern) |
| 5 | **Silent fills post-API change** | State drift after CLOB upgrade | Positions wrong but no exceptions | Full reconciliation pass **≥ every 30s** [@0x_Punisher] |
| 6 | **One leg open (hedge break)** | "Market neutral" with directional bleed | Funding PnL OK, price PnL dominates | Treat partial fill as first-class; @concepts/perps-dex-funding-carry-strategy.md |
| 7 | **Broken upstream data** | Modules agree on nonsense | Chainlink vs exchange divergence | Multi-module conflict detector → SKIP |
| 8 | **Over-logging** | Can't find ERROR in GB/day noise | Debugging takes hours despite "full logs" | @concepts/trading-bot-logging-discipline.md |
| 9 | **Wrong profitability question** | Optimizing WR not expectancy | 70% WR at 57¢ entry still loses | Entry-price break-even math in @concepts/polymarket-bot-architecture.md |
| 10 | **UI shows stale/mock** | Dashboard green, prod red | `status: empty` vs `live` ignored | Envelope pattern on `/api/*`; @concepts/trading-dashboard-api-wiring.md |
| 11 | **Fair value change without version bump** | Sleeve attribution shifts | Hold/tactical mix changes after valuation deploy | Bump `brain_equity` in strategy registry |
| 12 | **Mixing Brinson daily attribution with trade PnL** | Two reports disagree | Step 60 portfolio report vs FIFO script | Different tables/questions — don't merge blindly |
| 13 | **Silent zero-trade abort** | Signal fired, nothing sent, no ERROR | Logs show decision but no `trade_aborted` reason | @concepts/zero-trade-edge-signal-diagnostics.md — tag `abort_reason` |

### Cross-domain confirmation

Three independent Polymarket operators (@0x_Punisher, @Gustafssonkotte, @adiix_official) plus @morpphhhaw perps carry converge: **80% of production code is plumbing** (fills, reconciliation, orphans, dust). Strategy is the smaller surface. Cemini's `logic_version` work (2026-05-27/28) is the **attribution-layer** expression of the same insight for multi-strategy prod.

### Pre-deploy checklist (minimal)

Before trusting a new strategy's paper PnL:

1. Registry entry exists with `version_id` + `deployed_at`
2. Writes stamp `logic_version` on insert
3. Report script defaults to `scope=current` and prints version banner
4. Reconciliation job or 30s poll documented for that venue
5. Logs use structured `event=` names for submit/fill/reconcile/error — not DEBUG spam
6. One manual compare: bot export vs venue CSV for ≥20 trades

### Research sources that accelerate discovery

| Topic | Where to look next |
|-------|-------------------|
| Event-sourced PnL replay | Event sourcing for trading systems (schema registry + projections) |
| Immutable audit metadata | Model/ruleset/deployment version on every decision event |
| Monitoring not grep | osquant JSON logs → time-series dashboard |
| Equity fair value drift | @concepts/equity-fair-value-evaluation.md |

## Snippets

> "For bot: the edge is in the plumbing, not the algorithm. Fill detection, position reconciliation, cancellation of orphaned orders, dust cleanup. 80% of the code isn't strategy, it's survival." [Source: Posts 2.docx — Post 4, @MatiasScalbi]

> "Never trust only the API exception to confirm a fill. After any timeout — poll the order status endpoint manually. Run a full reconciliation pass every 30 seconds minimum." [Source: x-polymarket-bot-playbook-punisher-2026-05.md]

> "Polymarket exports as source-of-truth for stats, never the bot's internal counter." [Source: trading-posts-2 — @Gustafssonkotte, K55]

## Dead Ends

- **More logging without structure** — increases cost and hides ERROR rows; see row 8.
- **Aggregate Sharpe on <30 version-pure trades** — insufficient sample; per-version scope first.
