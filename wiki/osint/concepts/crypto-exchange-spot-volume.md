---
title: Crypto exchange spot volume — tracking and caveats
type: concept
tags: [crypto, spot-volume, venue-concentration, market-structure]
keywords: [spot-volume, wublock, binance, okx, coinbase, venue-share, wash-trading, concentration]
related:
  - sources/substack-rss-wublock-2026-10-13-september-spot-volume.md
  - concepts/crypto-derivatives-volume-2026.md
  - concepts/crypto-venue-website-traffic.md
  - concepts/xsp-lane-trading-framework.md
maturity: draft
created: 2026-10-13
updated: 2026-10-13
---

## Relations

- @sources/substack-rss-wublock-2026-10-13-september-spot-volume.md
- @concepts/crypto-derivatives-volume-2026.md
- @concepts/crypto-venue-website-traffic.md
- @concepts/xsp-lane-trading-framework.md

## Raw Concept

**The question this page answers:** what does the monthly spot-volume series measure, how reliable is it, and what can it be used for?

## Narrative

Wu Blockchain publishes a **monthly spot-volume table** for a **fixed 14-exchange sample** (`data.wublockchain.xyz/dashboard/exchange_volume`). It is the **spot** counterpart to the derivatives-volume series in `@concepts/crypto-derivatives-volume-2026.md` and the web-attention series in `@concepts/crypto-venue-website-traffic.md`.

### September 2026 reading

| Metric | Value |
|--------|-------|
| Total spot volume | **$696.7B** |
| August 2026 | $510.4B |
| MoM change | **+36.5%** |
| Venues up / down | **14 / 0** |
| Top-3 concentration | **62.4%** (August 64.8%) |
| Binance | $307.8B (**44.2%**) |
| OKX | $65.8B (9.5%) |
| Coinbase | $61.3B (8.8%) |

### How to use it

**Broad direction, not levels.** Three independent venue measures — spot volume, derivatives notional, and website traffic — agreeing on a month is a **strong attention signal**. The September agreement is a **broad risk-on rebound**.

**Concentration is the more interesting variable.** Top-3 share **fell to 62.4%** while **all 14 venues grew** — that means the **smaller venues grew faster than Binance**, a share shift rather than a flight to the largest venue.

### Caveats (stated by the publisher, and they matter)

- **Wash trading and bot activity may be significant.**
- The figures are **preprocessed** — **outlier removal, calibration, standardization**. They are **not raw exchange-reported totals**.
- The sample is **fixed at 14 venues**, so the series measures **share within the sample**, not global volume.
- **No venue-level audit.** Treat single-venue numbers as `[TENTATIVE]`.

### Why it matters here
A **venue-liquidity and attention proxy**, not a tradeable signal on its own. It informs **xsp venue context** (`@concepts/xsp-lane-trading-framework.md`) and **market-regime reads**. **No trade, no scp.**

## Snippets

> In September 2026, spot trading volume across major exchanges totaled about $696.7 billion, up approximately 36.5% from $510.4 billion in August 2026. The sample covers 14 exchanges, of which 14 rose and 0 fell month over month. [Source: https://wublock.substack.com/p/september-2026-exchange-spot-volume (retrieved 2026-10-13)]
