---
title: "Implied volatility surface compilation and forecasting with survey sampling (NVDA panel)"
type: source
tags: [source, arxiv, volatility, options, sampling]
related: []
maturity: draft
read_status: skimmed
created: 2026-10-27
updated: 2026-10-27
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Compiling and forecasting implied volatility surfaces via survey sampling, tempered inverse-probability sequence learning, and causal activity clocks |
| Authors | Deepak Bastola, Eli Prushansky — Department of Mathematical Sciences, Salisbury University |
| arXiv | 2610.33438 |
| File | `arxiv-2610.33438-compiling-and-forecasting-implied-volatility-sur.pdf` |
| Retrieved | 2026-10-27 |
| URL | https://arxiv.org/abs/2610.33438 |
| Read status | skimmed (abstract + intro) |

## Narrative

The paper builds implied volatility surfaces from a noisy, heterogeneous vendor feed. It uses a multi-resolution, split-adjusted NVDA equity and options panel from 2018 through 2025. Three methods combine: finite-population survey sampling, tempered inverse-probability sequence learning, and causally recalibrated activity clocks.

Four empirical findings are reported.

1. **Sampling design must match the target functional.** Stratified plug-in allocations with lagged cell dispersion improve neutral equal-weighted surface reconstruction, with complete grid coverage. Liquidity-weighted probability-proportional-to-size (PPS) sampling excels on liquidity-weighted targets. PPS inflates variance when applied across objectives.

2. **Informative sampling helps sequence training.** In Encoder-Decoder LSTM training, PPS and Neyman designs retain substantially more tail-volatility windows than simple random sampling. All three designs stay inside chosen equivalence margins on full-census forecasting accuracy while cutting training time. The authors state that incremental forecasting gains of informative selection over simple random sampling remain unestablished.

3. **Out-of-sample predictability is horizon-dependent.** The abstract announces a "predictability contrast" across horizons, but the truncated text does not give the direction or size of the effect.

4. **The panel covers a single name.** One equity underlier limits how far the conclusions carry to a cross-sectional options book.

The trading implication is narrow and practical: tail-volatility windows are the scarce sample, and losing them through naive subsampling biases surface forecasts. The paper offers a sampling recipe for anyone who trains a vol forecaster on a vendor panel.

All figures are first-hand from this source. They are single-source claims and are not independently verified here.

## Snippets

> "cross-sectional surface accuracy depends critically on matching the sampling design to the target surface functional" [Source: `arxiv-2610.33438-compiling-and-forecasting-implied-volatility-sur.pdf` p.1 (arXiv 2610.33438), retrieved 2026-10-27]

> "informative PPS and Neyman designs retain substantially more tail-volatility windows than simple random sampling (SRS)" [Source: `arxiv-2610.33438-compiling-and-forecasting-implied-volatility-sur.pdf` p.1 (arXiv 2610.33438), retrieved 2026-10-27]
