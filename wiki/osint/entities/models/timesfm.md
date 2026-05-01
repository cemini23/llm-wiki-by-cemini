---
title: TimesFM — Google Research Time-Series Foundation Model (200M params, CPU-viable)
type: entity
tags: [entity, ml-model, time-series, forecasting, cpu-inference, foundation-model, cemini-adopt]
keywords: [timesfm, google-research, time-series, foundation model, zero-shot, forecasting, decoder-only, patch-tokenization, cpu-inference, Apache-2.0]
related:
  - sources/wave-5-1-link-eval-stacks.md
  - entities/models/chronos-bolt.md
  - concepts/dlinear.md
  - concepts/quant-finance.md
maturity: draft
created: 2026-05-01
updated: 2026-05-01
---

## Relations

- @sources/wave-5-1-link-eval-stacks.md — Wave 5.1 Adopt-tier recommendation; primary evaluation source
- @entities/models/chronos-bolt.md — sibling CPU-viable time-series foundation model (Amazon, T5-small ~8M params, Apache-2.0); TimesFM is larger (200M) but also CPU-viable
- @concepts/dlinear.md — lightweight trend-seasonal alternative (~1K params); TimesFM occupies the foundation-model tier above DLinear and below commercial APIs
- @concepts/quant-finance.md — Quantitative Finance corpus-index hub

## Raw Concept

Surfaced as an Adopt-tier recommendation in Wave 5.1 link evaluation (@sources/wave-5-1-link-eval-stacks.md). TimesFM 2.5 (Google Research) is a 200M-parameter decoder-only foundation model pretrained on 100 billion real-world time-points for zero-shot forecasting. Apache-2.0 license.

## Narrative

### What it is

TimesFM is a decoder-only foundation model engineered by Google Research exclusively for time-series forecasting. It was pretrained on a massive corpus of 100 billion real-world time-points including Google Trends and Wikipedia traffic data. The architecture uses patch-based tokenization — groups of contiguous time-points are treated as single "patch" tokens — which drastically reduces generation steps and enables long-horizon predictions from relatively small input windows.

Version 2.5 (released September 2025) supports a 16K context length and operates on both PyTorch and Flax backends. The model consistently outperforms traditional statistical methods (ARIMA, ETS) in zero-shot settings without requiring dataset-specific fine-tuning.

### Cemini integration vector

The concrete integration involves deploying TimesFM as a dedicated Docker container within the Cemini compose network. The container subscribes to Redis `intel:*` channels, consumes normalized CCXT and Polygon price arrays, executes zero-shot forecasting via PyTorch CPU inference, and writes predictive horizon arrays back to PostgreSQL for LangGraph agent consumption.

**RAM budget**: A 200M-parameter model at fp32/fp16 occupies approximately 400-800 MB of resident RAM — comfortably within the 7 GB Hetzner limit alongside PostgreSQL, Redis, and FastAPI.

**Limitations**: CPU inference latency on AMD EPYC precludes HFT use. Operational scope is medium-to-long-horizon forecasting where millisecond execution isn't required. Exact latency baselines on the target architecture need measurement (`[NEEDS VERIFICATION]`).

### Comparison with Chronos-Bolt

Both are Apache-2.0, CPU-viable time-series foundation models, but they occupy different tiers:
- **Chronos-Bolt**: ~8M params (T5-small), probabilistic quantile outputs, ~50 MB footprint. Ultra-lightweight feature extractor.
- **TimesFM**: 200M params, decoder-only, point forecasts with longer context (16K vs Chronos-Bolt's 512), ~400-800 MB footprint. Higher capacity, longer-horizon predictions.

The two models are complementary rather than competing: Chronos-Bolt as the fast-path feature extractor, TimesFM as the deeper forecast engine.

### License

Apache-2.0 — fully clean for IP-sale readiness. No copyleft, no commercial-use restrictions, no attribution requirements beyond the standard NOTICE file.

## Snippets

### Wave 5.1 Adopt rationale
"A 200 million parameter model quantized to standard fp32 or fp16 occupies roughly 400 MB to 800 MB of resident RAM. This exceptionally small footprint comfortably fits within the strict 7 GB server limitation, executing alongside the existing Postgres, Redis, and FastAPI stack without triggering Out-Of-Memory kills. Furthermore, the clean Apache-2.0 license ensures that integrating this deep learning model directly into the proprietary trading stack is fully compliant with all institutional IP-sale restrictions." [Source: wave-5-1-link-eval-stacks.md]

### From the Google Research repository
"TimesFM 2.5 is a 200M parameter foundation model for time-series forecasting, pretrained on 100B+ real-world time points. It supports zero-shot forecasting with context length up to 16K." [Source: github.com/google-research/timesfm, retrieved 2026-05-01]
