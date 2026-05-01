---
title: DLinear — Trend-Seasonal Decomposition Model for Time-Series Forecasting
type: concept
tags: [concept, time-series, forecasting, trend-seasonal, lightweight-ml, cpu-inference, cemini-adopt]
keywords: [dlinear, trend-seasonal decomposition, linear model, time-series forecasting, lightweight, transformer-alternative, CPU inference]
related:
  - sources/4-4-link-re-2.md
  - concepts/quant-finance.md
  - concepts/rl-marl-research.md
  - entities/models/chronos-bolt.md
  - entities/models/timesfm.md
maturity: validated
created: 2026-04-30
updated: 2026-05-01
---

## Relations

- @sources/4-4-link-re-2.md — K12 deep-read §Target Domain 4; primary source. DLinear evaluated as Top Steal.
- @concepts/quant-finance.md — Quantitative Finance corpus-index hub
- @concepts/rl-marl-research.md — RL/MARL hub; DLinear could serve as lightweight feature extractor for MAPPO
- @entities/models/chronos-bolt.md — sibling model entity; Chronos-Bolt is the heavyweight pretrained option, DLinear is the lightweight from-scratch alternative
- @entities/models/timesfm.md — Google Research 200M-param foundation model (Apache-2.0); TimesFM occupies the tier above DLinear (foundation-model vs. ~1K-param linear)

## Raw Concept

Surfaced as a Top Steal in @sources/4-4-link-re-2.md §Target Domain 4 (Decomposable Reward Modeling). DLinear is a strikingly simple architecture: decompose a time series into trend and seasonal components using moving averages, then apply separate linear layers to each. Despite ~1,000 parameters, it beats Transformer-based forecasters on many benchmarks. CPU inference cost is negligible.

## Narrative

### What it is

DLinear is a time-series forecasting model that challenges the "more complexity = better performance" assumption. Its architecture is:

1. **Decomposition**: A moving average separates the input series into trend (smooth, long-term) and seasonal (residual, cyclical) components
2. **Separate linear layers**: One linear layer processes the trend component; another processes the seasonal component
3. **Summation**: The two outputs are summed to produce the forecast

That's it. ~1,000 parameters. No attention, no recurrence, no convolutions. Just decomposition + linear projection.

Despite this simplicity, DLinear outperforms Transformer-based models (Informer, Autoformer, FEDformer) on standard time-series benchmarks. The reason: time-series forecasting is often dominated by trend and seasonality, and Transformers overfit to noise when the signal is this simple.

### Why it fits Cemini

1. **CPU-trivial inference**: ~1K parameters × 4 bytes = ~4 KB of weights. A forward pass is a few matrix multiplications. This runs in microseconds on the Hetzner VPS (7 GB, 2 vCPU) with zero memory pressure.

2. **Interpretable**: Trend and seasonal components are human-readable. A human can inspect the decomposition and understand WHY the model made a prediction. This directly supports the glass-box IP-sale narrative.

3. **Complements Chronos-Bolt**: Chronos-Bolt (@entities/models/chronos-bolt.md) is the heavyweight pretrained option (~8M params, 80M-series pretraining). DLinear is the lightweight from-scratch option. They can coexist: DLinear for fast feature extraction on every MAPPO observation step; Chronos-Bolt for deeper analysis during retrain windows.

4. **No license issues**: DLinear is an academic paper, not a software library. The architecture is public domain. Implementation is ~100 lines of PyTorch.

### Integration path

1. Implement DLinear in ~100 lines of PyTorch (`services/features/dlinear.py`)
2. Train on Cemini-specific assets (BTC-USD, SPY) — training is fast (<1 minute on CPU for years of daily data)
3. Extract trend/seasonal features on each MAPPO observation step
4. Add 2–4 features to the MAPPO observation space: trend_slope, seasonal_amplitude, seasonal_period, residual_std
5. A/B test: MAPPO with vs. without DLinear features

### Risk assessment

- **Too simple?**: If the market regime is dominated by non-linear dynamics (e.g., volatility events), DLinear may underperform. Mitigate by using DLinear as one of many features, not the sole predictor
- **Implementation quality**: ~100 lines of custom PyTorch carries maintenance burden. Mitigate by writing tests that verify the decomposition matches reference implementation
- **Diminishing returns**: Hand-crafted trend/seasonal indicators may already capture what DLinear extracts. A/B test will determine marginal value

## Snippets

> "DLinear: ~1,000-parameter linear model decomposing time series into trend and seasonal components. Despite simplicity, beats Transformer-based forecasters on many benchmarks. CPU inference cost negligible. The trend-seasonal decomposition is inherently interpretable — directly supporting the glass-box IP-sale narrative." [Source: 4_4 link re 2.docx §Target Domain 4]
