---
title: "LSTM Stock Prediction Baseline — methodology reference from Stanford CS 230"
type: concept
tags: [methodology, deep-learning, lstm, stock-prediction, time-series, baseline, reference]
keywords: [LSTM, stock prediction, RMSE, hyperparameter tuning, dropout, batch size, baseline model]
related:
  - sources/stanford-cs230-lstm-stock-prediction.md
maturity: draft
created: 2026-05-16
updated: 2026-05-16
---

## Relations

- `@sources/stanford-cs230-lstm-stock-prediction.md` — source paper establishing this baseline

## Raw Concept

A reference baseline for LSTM-based stock price prediction, extracted from a Stanford CS 230 project. Serves as a minimal viable starting point — useful for comparing more sophisticated architectures against a known-simple LSTM.

## Narrative

### Model architecture

Standard LSTM: 50 neurons, MSE loss, Adam optimizer, 100 epochs. Input: 30-day sliding window of OHLC data. Output: next-day close price prediction. Data: AMZN, GOOG, FB daily prices (2015–2020, 1260 entries each, 800/460 train/test split). Min-max normalization applied.

### Hyperparameter sweep results

| Parameter | Best | Worse |
|-----------|------|-------|
| Layers | 3 | 4 |
| Dropout | 0.1 | 0.2 |
| Batch size | 32 | 64 |

Best model (3 layers, dropout 0.1, batch 32) RMSE: FB 4.89, GOOG 22.23, AMZN 48.66.

### Limitations as a baseline

- **Single-stock input**: No cross-asset features, no market-wide signals, no macro indicators
- **OHLC only**: No volume, no order-book depth, no sentiment, no alternatives data
- **3-stock universe**: All large-cap tech — no sector/asset-class diversity
- **No regime awareness**: 2015–2020 includes a low-vol bull market; no stress-test on 2020 COVID crash or 2022 bear
- **Point prediction only**: No uncertainty quantification, no probabilistic forecast

### Value as a reference point

Despite these limitations, this serves as a useful "hello world" calibration point. Any proposed architecture claiming superiority should first demonstrate improvement over this simple 3-layer LSTM baseline on the same or comparable OHLC-only setup. If a complex model (transformer, RL, ensemble) can't beat a tuned 3-layer LSTM on this task, the complexity isn't justified.
