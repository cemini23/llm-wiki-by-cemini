---
title: "quants.md — 50 backtested strategy library with order and risk templates"
type: entity
tags: [tool, trading, backtesting, walk-forward, risk, xsp, guruwatcher]
keywords: [quants.md, walk forward, circuit breaker, bracket order, trailing stop, risk parity, agenkit]
related:
  - sources/eval-multi-wiki-link-revenue-v10.10-batch-a-2026-11-01.md
  - concepts/regime-threshold-parameters.md
maturity: draft
created: 2026-11-01
updated: 2026-11-01
---

## Raw Concept

Surfaced by @sources/eval-multi-wiki-link-revenue-v10.10-batch-a-2026-11-01.md, URL 6, **Extract** tier. Routed to xsp-killer and GuruWatcher.

The question this page answers: **what execution and sizing mechanics are worth lifting into a trading stack, independent of the strategies themselves?**

## Narrative

### What it is

An open web library of about 50 Python trading strategies. Each carries dashboard statistics: CAGR, Sharpe, maximum drawdown, win rate, profit factor. The site targets AI coding harnesses through a component called AgenKit, which generates bots inside Claude Code, Cursor, Codex, and four other tools. There is an Excel portfolio export.

Categories: weight strategies, explicit order strategies, and walk-forward out-of-sample tests.

### The useful part is not the strategies

The report measures the catalog honestly and the result is not flattering: "Many baseline ETF strategies in the catalog post negative or sub-0.5 Sharpe ratios." The named examples — Market RSI Reversion, Trailing Stop Trend, Bracket Trend, Monthly Circuit Breaker — all sit below 0.5 Sharpe. Risk Parity Capped is the reported best case.

That is the expected outcome for a public catalog of textbook rules on liquid ETFs. **The strategies are not the asset. The scaffolding is.**

Three things are worth extracting:

1. **Walk-forward out-of-sample splits.** The validation harness, not the parameters. This is the same requirement that gates the @entities/tools/karpathy-autoresearch.md loop.
2. **Explicit order state machines.** Bracket, stop-limit protection, trailing stop-limit. Written as states rather than as conditions, so an invalid transition is a bug rather than a silent miss.
3. **Risk sizing rules.** The monthly circuit breaker and the risk-parity capped allocation. A circuit breaker is a drawdown gate; it costs return and buys survival.

### Routing

| Target | Take |
|--------|------|
| xsp-killer | The walk-forward split harness, the bracket and stop-limit state machines, the circuit breaker. |
| GuruWatcher | Threshold definitions for mean-reversion and momentum regime watches. **Documentation only** — GuruWatcher stays alert-only. Written at @concepts/regime-threshold-parameters.md. |

### The hard ban still applies

GuruWatcher is alert-only. It never places an order, and it never clobbers the production `watches.json` hold or trigger state. Nothing from this library changes that. The order state machines go to xsp-killer, not to GuruWatcher.

### Phase-0 status

**Not run.** GitHub egress is denied in this session, and the report itself could not locate the underlying repository: "NEEDS VERIFICATION: Exact GitHub repository URL hosting the underlying quants.md / AgenKit code bundle." The site is a web library; the report found no stated licence.

So the licence is unknown and the source repository is unknown. Treat everything here as a **pattern to re-implement**, not code to copy.

### Status

Extract, **pattern only**, licence unresolved.

## Snippets

> "quants.md exposes 50 tested trading strategies with full Python source code, dashboard statistics (CAGR, Sharpe, Max DD, Win rate, Profit factor), explicit order mechanics, and walk-forward stability tests built for AI coding harnesses via AgenKit." — report, URL 6

> "Many baseline ETF strategies in the catalog post negative or sub-0.5 Sharpe ratios … extract the walk-forward validation harness and order/sizing mechanics rather than deploying raw ETF parameters on XSP." — report, URL 6 business risk

## Dead Ends

- **Deploying the catalog parameters.** The report's own numbers put most of them below 0.5 Sharpe.
- **Copying code before the licence is known.** No repository URL and no licence were found. Re-implement from the description.
