---
title: "polymarketanalytics.com — free third-party wallet-filter platform"
type: entity
tags: [entity, tool, polymarket, wallet-analytics, smart-money, third-party, free, prediction-markets, k56]
keywords: [polymarketanalytics-com, wallet-filter, polymarket-leaderboard-alternative, win-rate-filter, pnl-filter, dexterssolab]
related:
  - sources/posts-prediction-markets-quant-frameworks-2026-05-21.md
  - concepts/polymarket-copy-trading-strategy.md
  - entities/tools/pretracer.md
  - entities/tools/kreopolybot.md
  - entities/people/dexterssolab.md
maturity: draft
created: 2026-05-21
updated: 2026-05-21
phase_0_verdict: USE-AS-INPUT — free read-only filter platform; useful as alternative-data source, not an adoption target
---

## Relations

- @sources/posts-prediction-markets-quant-frameworks-2026-05-21.md — Post 3 (@DextersSolab) introduces the platform
- @concepts/polymarket-copy-trading-strategy.md — primary use-case
- @entities/tools/pretracer.md, @entities/tools/kreopolybot.md — downstream consumers (the platform identifies wallets; the bots execute the copy)

## Raw Concept

What prompted this page: K56 Posts.docx Post 3 — @DextersSolab uses `polymarketanalytics.com` as his wallet-discovery layer ahead of running KreoPolyBot setup. The platform exposes Polymarket wallet metadata that Polymarket itself doesn't surface natively.

## Narrative

**polymarketanalytics.com** is a third-party web platform that aggregates Polymarket wallet activity into searchable, filterable form. Free per the source post.

### Exposed metadata (per @DextersSolab usage)

- Overall PnL
- Current account value
- Active positions count
- Total positions count
- Win rate
- Historical PnL chart
- Trade history
- Deposit / withdrawal log
- Per-trade position sizes

This is meaningfully more than Polymarket's own leaderboard, which sorts by monthly profit but exposes none of the per-trade granularity.

### Recommended filter parameters (per @DextersSolab)

For wallet-discovery suitable for copy-trading:

- Overall PnL: $15,000 - $400,000
- Current value: ≥ $5,000
- Active positions: ≥ 2
- Total positions: ≥ 20
- Win rate: ≥ 70%

Three clicks: Traders → Filters → Apply.

### Cemini relevance

Useful as a **read-only alternative-data source** for two Cemini workstreams:

1. **Adversary modeling on Polymarket markets** — identify which markets have heavy smart-wallet activity (top-N wallets filtered as above, then per-market position lookup). Markets saturated with smart money have less alpha extractable and worse fill quality. The @concepts/polymarket-microstructure-findings.md page would benefit from this.
2. **Wallet-quality scoring as input feature** — if any future Cemini ML model predicts Polymarket directional outcomes, a feature like "smart-wallet net position size on this market" derived from polymarketanalytics could be informative.

Not an adoption target — Cemini doesn't host third-party-data-aggregator sites; we consume them.

### Verification follow-ups

- `[NEEDS VERIFICATION 2026-05-21]` Whether polymarketanalytics.com has a public API or only a web UI. If web-UI-only, our consumption requires either scraping or manual lookup. Per the K56 GitHub-projects report, pmxt's open-source 1TB orderbook dataset may render polymarketanalytics's wallet-tracking duplicative for any aggregated query (pmxt has the raw data, polymarketanalytics has the curated view).
- `[NEEDS VERIFICATION 2026-05-21]` Operator identity and funding model — "free" platforms often monetize via referral or data-sale to the very bots (Pretracer, KreoPolyBot) that downstream consume them.

## Dead Ends

- The source post doesn't document the platform's coverage completeness. It's likely a sample of high-activity wallets, not the full Polymarket trader base — confirm before relying on absence-of-wallet as a signal.
