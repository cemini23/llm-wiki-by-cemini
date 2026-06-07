---
title: "Market Making with Machine Learning Methods — Order Book Pressure (Stanford GR4, 2017)"
type: source
tags: [source, market-making, hft, academic, k104]
keywords: [gr4, stanford, order-book-pressure, obp, svm, random-forest, sgd, ldz14, thesys]
related:
  - concepts/order-book-pressure-ml-market-making.md
  - concepts/market-microstructure.md
  - concepts/polymarket-market-making-architectures.md
  - concepts/avellaneda-stoikov-market-making-baseline.md
  - sources/stanford-avellaneda-stoikov-hf-mm-gr5-2018.md
  - concepts/market-informedness-market-making.md
  - sources/arxiv-grpo-lob-hft-trading-2605.25527.md
read_status: deep-read
maturity: validated
created: 2026-06-07
updated: 2026-06-07
---

## Relations

- @concepts/order-book-pressure-ml-market-making.md — synthesized OBP + ML MM findings for Cemini
- @concepts/market-microstructure.md — LOB cluster hub
- @concepts/polymarket-market-making-architectures.md — PM MM architecture rubric; OBP overlay REFERENCE only
- @sources/stanford-avellaneda-stoikov-hf-mm-gr5-2018.md — sibling Stanford MM student project (inventory-skewed A-S baseline, K98)
- @concepts/avellaneda-stoikov-market-making-baseline.md — theoretical MM baseline; GR4 cites A-S for dynamic posting extensions
- @concepts/market-informedness-market-making.md — contrasts weak OBP classifiers with informed-flow regime (2606.05882)

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Market Making with Machine Learning Methods |
| Authors | Kapil Kanagal, Yu Wu, Kevin Chen (Stanford) |
| Filename | gr4.pdf |
| sha256 | `1af73951c6aa1c749b02c22f518877070b597bbf3c7c7c54512ed9b803471146` |
| Date | 2017-06-10 |
| Retrieved | 2026-06-07 |
| Pages | 14 |
| Location | `cemini-librarian:/opt/cemini-bulk/research/gr4.pdf` |
| read_status | deep-read |

## Narrative

Stanford student project implementing **Li et al. [LDZ+14]** intelligent market-making: sample limit-order-book state each minute, classify mid-price direction (+1 / 0 / −1) from **Order Book Pressure (OBP)** features, then skew bid/ask quotes before posting. Trained on Thesys simulator data for AAPL, FB, ORCL, MSFT, GOOG (GOOG later dropped for persistent PnL dips).

**Signal:** Mid-price change vs threshold θ ($0.03–$0.04). **Features:** 30 OBP ratios — bid/ask queue-size aggregates over windows n∈{1,2,3,5,10,15} minutes and L=5 book levels [CONFIRMED — gr4.pdf §2.2].

**Models compared:** SVM (RBF, C=10, γ=0.005), Random Forest (100 trees, min_samples_leaf=3), linear SGD (log-loss, 500 iterations). Training: 3-month parameter fit + 15-day rolling retrain per ticker.

**Quoting:** Conservative skew — `bid = b + μ·min(sign,0)`, `ask = a + μ·max(sign,0)` — beats aggressive symmetric skew because mispredictions otherwise leave one-sided inventory. **Second-best** bid/ask as reference prices materially improves spread capture vs best quotes without hurting fill rate [CONFIRMED — gr4.pdf §3.2].

**Results [CONFIRMED — gr4.pdf §4]:**

| Strategy | vs no-signal baseline |
|----------|----------------------|
| No signal (2nd-best quotes only) | Baseline |
| SVM | Worse |
| SGD | Worst (~39% overall accuracy; over-predicts neutral) |
| Random Forest | **Slightly better** (~52% overall; ~58% up / ~55% down conditional) |

Key negative findings: (1) SVM "accuracy" inflates via neutral-class cheating — custom metric penalizes adverse and bold-wrong predictions; (2) stop-loss inventory reduction **underperforms** hold-to-EOD given weak forecasts; (3) missing [LDZ+14] **news-aggregator signal** (Thesys could not ingest scraped news) likely explains tail-day PnL collapses; (4) NASDAQ IT names ≠ NIKKEI behavior in original paper — GOOG is an outlier.

**Cemini posture:** **REFERENCE** for LOB-feature MM overlays — do not assume OBP classifiers improve PM/Kalshi LP PnL without informedness/news layers. Pairs with `@concepts/market-informedness-market-making.md` (regime-aware spread) and `@sources/arxiv-grpo-lob-hft-trading-2605.25527.md` (directional RL, not MM). Not production-ready: 1-minute cadence, 2017 equities, no maker rebates modeled.

## Snippets

> "Only the Random Forest prediction yields a slightly higher cumulative PNL. SGD performs the worst out of all algorithms."

[Source: gr4.pdf p.11, retrieved 2026-06-07]

> "In practice we found that this stop loss strategy performs worse than even just holding on all inventory until the end of day to liquidate it."

[Source: gr4.pdf p.10, retrieved 2026-06-07]

> "We may get better performance with more dynamic stop loss mechanisms, such as the VPIN strategy suggested in [ELdPO10]."

[Source: gr4.pdf p.10, retrieved 2026-06-07]

> "Our model does not factor in that compensation" [for providing liquidity].

[Source: gr4.pdf p.13, retrieved 2026-06-07]
