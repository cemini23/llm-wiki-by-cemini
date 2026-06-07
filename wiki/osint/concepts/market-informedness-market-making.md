---
title: Market informedness — MM profitability and LP regime feature
type: concept
tags: [concept, market-making, microstructure, prediction-markets, k100]
keywords: [2606.05882, informedness, adverse-selection, spread, lp-risk, hawkes]
related:
  - sources/arxiv-market-informedness-mm-profitability-2606.05882-2026-06-05.md
  - sources/stanford-ml-orderbook-mm-gr4-2017.md
  - concepts/order-book-pressure-ml-market-making.md
  - concepts/polymarket-market-making-architectures.md
  - concepts/polymarket-microstructure-findings.md
  - concepts/polymarket-retail-trading-discipline.md
  - meta/pm-lp-backtest-cadence.md
  - concepts/avellaneda-stoikov-market-making-baseline.md
maturity: validated
created: 2026-06-05
updated: 2026-06-07
---

## Relations

- @sources/arxiv-market-informedness-mm-profitability-2606.05882-2026-06-05.md — arXiv 2606.05882 (deep-read)
- @sources/stanford-ml-orderbook-mm-gr4-2017.md — OBP-only MM fails on event days without news layer
- @concepts/order-book-pressure-ml-market-making.md — LOB classifier overlay; thin edge without informedness
- @concepts/polymarket-market-making-architectures.md — Cemini LP modules
- @meta/pm-lp-backtest-cadence.md — quarterly spread tier review hook

## Raw Concept

K100 federation ingest + deep-read 2026-06-05. Synthesizes Ochedzan & Antulov-Fantulin (2606.05882) for Cemini LP posture.

## Narrative

**Market informedness** is the share of order flow driven by superior fundamental information. It is a **regime coordinate**, not a one-way "tighten spreads" dial.

### Two-regime insight from 2606.05882

| Regime | Risk | Mechanism |
|--------|------|-----------|
| **Low informedness + informed burst** | Highest adverse selection | Unprepared MMs quote tight; informed takers extract |
| **Higher baseline informedness** | Net MM profitability can **rise** | Price discovery improves; offsets adverse selection |

This contradicts a simplistic "informed flow always hurts LPs" rule. Cemini spread tiers should be keyed on **(informedness level, event proximity, Hawkes intensity)** — not a static backtest spread alone.

**GR4 counterpoint [CONFIRMED]:** Stanford `@sources/stanford-ml-orderbook-mm-gr4-2017.md` shows OBP-only directional skew barely beats naive quoting; tail losses align with missing news/event layer — same failure mode as low-informedness bursts in 2606.05882.

### Cemini LP checklist (draft)

1. **Pre-event / poorly informed windows** — widen, shrink size (WC LP safety DR alignment)
2. **Mature / high-discovery markets** — do not auto-widen solely on informed-minority signals
3. **Backtest** — next `@meta/pm-lp-backtest-cadence.md` run should test informedness proxies vs PnL `[NEEDS VERIFICATION 2026-06-05]`

### Posture

| Scope | Verdict |
|-------|---------|
| PM / Kalshi LP bots | **STEAL-FROM** — regime feature + spread policy |
| Equity MM (Avellaneda baseline) | **REFERENCE** — simulation not calibrated to Cemini tickers |

## Snippets

> "Informed market order flow is particularly dangerous in poorly informed markets."

> — [Source: arxiv-2606.05882 p.1, retrieved 2026-06-05]
