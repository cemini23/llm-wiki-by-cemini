---
title: Chronos-Bolt — CPU-Optimized Time-Series Foundation Model
type: entity
tags: [entity, ml-model, time-series, forecasting, cpu-inference, cemini-adopt]
keywords: [chronos-bolt, amazon, time-series, foundation model, T5, probabilistic forecasting, quantile, CPU inference, Apache-2.0]
related:
  - sources/4-4-link-re.md
  - concepts/quant-finance.md
  - concepts/rl-marl-research.md
  - concepts/dlinear.md
  - entities/models/timesfm.md
  - sources/4-3-link-re-2.md
maturity: validated
created: 2026-04-30
updated: 2026-05-01
---

## Relations

- @sources/4-4-link-re.md — K12 deep-read; primary source. Chronos-Bolt evaluated as Top Steal for Cemini stack.
- @concepts/quant-finance.md — Quantitative Finance corpus-index hub
- @concepts/rl-marl-research.md — RL/MARL hub; Chronos-Bolt could serve as pretrained feature extractor for MAPPO
- @concepts/dlinear.md — DLinear trend-seasonal model; lightweight sibling CPU-time-series option
- @entities/models/timesfm.md — Google Research 200M-param time-series foundation model (Apache-2.0); complementary: Chronos-Bolt as fast-path (~8M), TimesFM as deep-forecast (~200M)
- @sources/4-3-link-re-2.md — K14 deep-read 2026-05-01; reinforces Chronos-Bolt Apache-2.0 + CPU-viability with explicit license confirmation; adds TimesFM 2.5 as secondary Apache-2.0 candidate and Moirai CC-BY-NC-4.0 as explicit reject

## Raw Concept

Surfaced as a Top Steal in the K12 deep-read of @sources/4-4-link-re.md (Cemini-internal link-evaluation audit). Amazon's Chronos-Bolt is a pretrained time-series foundation model optimized for CPU inference, making it uniquely suitable for the Hetzner VPS constraint (7 GB RAM, CPU-only — see @entities/infrastructure/hetzner.md).

## Narrative

### What it is

Chronos-Bolt is a time-series foundation model developed by Amazon, distributed under the Apache-2.0 license. It uses a T5-small backbone (~8M parameters) with patch-based tokenization, pretrained on approximately 80 million time series. It produces probabilistic forecasts as quantile outputs, not point predictions — giving it native uncertainty quantification.

### Why it fits Cemini

1. **CPU-optimized**: Unlike most foundation models that assume GPU inference, Chronos-Bolt is explicitly designed for CPU execution. The ~8M parameter count is small enough to run on the 7 GB Hetzner VPS without competing with the 62K-param MAPPO model for memory.

2. **Pretrained feature extraction**: Instead of hand-crafting 11 technical indicators (SMA, EMA, Bollinger, RSI, MACD, etc. — as done in @sources/forex-1-4-4.md), Chronos-Bolt can produce a dense latent representation of the price series. This latent representation becomes input features for the MAPPO policy network, potentially capturing patterns the hand-crafted indicators miss.

3. **Probabilistic outputs**: Quantile forecasts give the agent a distribution over future prices, not just a point estimate. This maps naturally to risk-aware decision making — the agent can size positions based on forecast dispersion.

4. **Apache-2.0 license**: Zero license toxicity. Compatible with Cemini's proprietary stack. No GPL/AGPL risk.

5. **Transfer learning**: Pretrained on 80M diverse time series (finance, weather, energy, retail, etc.). The model has already learned general temporal patterns before seeing any Cemini market data. Fine-tuning on Cemini's specific assets (BTC-USD, SPY, Kalshi contracts) requires far less data than training from scratch.

### Technical specs

| Property | Value |
|----------|-------|
| Architecture | T5-small encoder-decoder |
| Parameters | ~8M |
| Pretraining corpus | ~80M time series |
| Output | Probabilistic (quantiles) |
| Tokenization | Patch-based (not point-by-point) |
| License | Apache-2.0 |
| Inference | CPU-optimized |
| Python API | `pip install chronos` |

### Integration path

1. **Install**: `pip install chronos` into the Cemini Python 3.12 environment
2. **Load**: `ChronosBoltPipeline.from_pretrained("amazon/chronos-bolt-small")` — downloads ~30 MB
3. **Feature extraction**: On each MAPPO observation step, feed the last N price bars through Chronos-Bolt → extract the encoder's latent representation → concatenate with the existing 34-dim feature vector
4. **Optional fine-tuning**: During the MAPPO retrain window (April 14–17 schedule), fine-tune Chronos-Bolt on Cemini-specific asset data alongside the policy network
5. **Fallback**: If Chronos-Bolt inference is too slow for live trading, use it only during retrain windows as a feature-engineering step, caching the latent representations

### Risk assessment

- **Inference latency**: ~8M params on CPU should produce features in <100ms for typical lookback windows, but needs benchmarking on the actual Hetzner VPS (7 GB, 2 vCPU)
- **Memory**: ~30 MB model weights + inference overhead — fits within 7 GB alongside existing containers
- **Diminishing returns**: Hand-crafted indicators already capture many of the patterns Chronos-Bolt would learn. The marginal gain may be modest. A/B test: MAPPO with vs. without Chronos-Bolt features over the same backtest period
- **Dependency**: Adds a new Python dependency to the stack. Mitigated by Apache-2.0 license and pip installability

## Snippets

> "Chronos-Bolt: Amazon's CPU-optimized time-series foundation model. Pretrained on ~80M time series; produces probabilistic forecasts (quantile outputs). T5-small backbone (~8M params) with patch-based tokenization, optimized for CPU inference. Apache-2.0. Could serve as a pretrained feature extractor feeding the MAPPO model, reducing the need for hand-crafted technical indicators." [Source: 4_4 link re.docx §Chronos-Bolt]
