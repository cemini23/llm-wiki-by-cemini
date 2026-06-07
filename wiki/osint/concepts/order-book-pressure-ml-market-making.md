---
title: Order book pressure — ML directional overlay for market making
type: concept
tags: [concept, market-making, market-microstructure, k104]
keywords: [order-book-pressure, obp, lob-features, svm, random-forest, directional-skew, ldz14]
related:
  - sources/stanford-ml-orderbook-mm-gr4-2017.md
  - sources/stanford-avellaneda-stoikov-hf-mm-gr5-2018.md
  - concepts/polymarket-market-making-architectures.md
  - concepts/avellaneda-stoikov-market-making-baseline.md
  - concepts/market-informedness-market-making.md
  - sources/arxiv-grpo-lob-hft-trading-2605.25527.md
  - concepts/market-microstructure.md
maturity: validated
created: 2026-06-07
updated: 2026-06-07
---

## Relations

- @sources/stanford-ml-orderbook-mm-gr4-2017.md — primary deep-read (Stanford GR4, 2017)
- @concepts/polymarket-market-making-architectures.md — PM MM posture; do not bolt OBP skew without informedness
- @concepts/avellaneda-stoikov-market-making-baseline.md — inventory-skew baseline without LOB classifiers
- @concepts/market-informedness-market-making.md — informed-flow regime supersedes naive OBP skew when adverse selection spikes

## Raw Concept

K104 ingest 2026-06-07. Synthesizes GR4 + [LDZ+14] lineage for Cemini LP/MM design discipline.

## Narrative

**Order Book Pressure (OBP)** summarizes relative bid vs ask queue depth across L limit-order-book levels and rolling time windows. When ask-side size dominates at a threshold, mid-price is expected to fall (and vice versa). Li et al. [LDZ+14] combine OBP features with SVM direction classifiers and **news signals** for intelligent MM; Stanford GR4 replicates the LOB half on NASDAQ sim without news.

### Feature → quote pipeline

1. Sample book each minute (Thesys); build 6L OBP ratios.
2. Classify mid move: +1 / 0 / −1 vs θ threshold.
3. Skew quotes conservatively: never bid above best bid or ask below best ask when signal wrong-sided.
4. Post at **second-best** prices to widen captured spread.

### Model ranking (GR4 backtest)

| Model | Trend prediction | MM PnL vs naive |
|-------|------------------|-----------------|
| Random Forest | ~52% overall; stronger on up/down | **Slight edge** |
| SVM | High neutral accuracy; ~40% conditional up/down | **Worse than naive** |
| Linear SGD | ~83% neutral; ~14% up / ~7% down | **Worst** |

**Design lesson:** Accuracy metrics that reward neutral prediction mis-rank models for MM — wrong directional skew loses more than no skew. Custom SVM metrics (penalize adverse + reward bold-when-correct) partially address this but RF still wins empirically.

### Failure modes relevant to Cemini

| Gap | GR4 evidence | Cemini mapping |
|-----|--------------|----------------|
| No news / event layer | Tail-day PnL collapses | PM sports/macro: fuse `@concepts/market-informedness-market-making.md` + event calendars |
| Weak stop-loss on bad forecasts | Stop-loss < hold-to-close | WC/PM LP: prefer conviction gates over reactive inventory dumps |
| Market transfer | NIKKEI→NASDAQ; GOOG outlier | Backtest per venue; no cross-market OBP constants |
| Maker rebates omitted | Strategy looks unprofitable | PM LP rewards must enter breakeven math |

### Posture

| Use | Verdict |
|-----|---------|
| PM/Kalshi LP quote skew from raw OBP | **REFERENCE only** — RF edge is thin; pair with informedness + news |
| Equity HFT directional (GRPO paper) | Separate lane — `@sources/arxiv-grpo-lob-hft-trading-2605.25527.md` uses OFI, not MM |
| Avellaneda inventory skew | Complementary — GR5 `@sources/stanford-avellaneda-stoikov-hf-mm-gr5-2018.md` handles inventory; OBP handles short-horizon direction |

## Snippets

> "Generating wrong predictions when the trend is either going up or down hurts more than having no signal at all since going against the market makes us lose more money."

[Source: gr4.pdf p.12, retrieved 2026-06-07]

> "Signal generation helps generate PNL but can't fundamentally change the profitability of a trading algorithm."

[Source: gr4.pdf p.11, retrieved 2026-06-07]
