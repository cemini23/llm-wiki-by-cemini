---
title: "A Deep Learning Approach for Stock Market Prediction — Stanford CS 230 (Yan Miao)"
type: source
tags: [source, paper, stanford, lstm, stock-prediction, deep-learning, reference]
keywords: [LSTM, stock market prediction, RMSE, AMZN, GOOG, FB, time-series, Keras]
related:
  - concepts/lstm-stock-prediction-baseline.md
maturity: draft
created: 2026-05-16
updated: 2026-05-22
read_status: skimmed
---

## Relations

- `@concepts/lstm-stock-prediction-baseline.md` — baseline methodology extracted from this source

## Raw Concept

- **Title**: A Deep Learning Approach for Stock Market Prediction
- **Author**: Yan Miao, Stanford University CS 230
- **Type**: Academic course project paper
- **Location**: `cemini-librarian:/opt/cemini-bulk/research/55614857.pdf`
- **Retrieved**: 2026-05-16
- **Pages**: 6
- **Read status**: read

## Narrative

Stanford CS 230 project testing LSTM networks for daily stock price prediction on AMZN, GOOG, FB (2015-01-28 to 2020-01-29). 1260 daily entries per stock: 800 train, 460 test. Features: date, open, close, low, high. Target: close price. Min-max normalization, 30-day timestep window.

Six model variants tested across 3 hyperparameters:
- Layers: 3 vs 4
- Dropout: 0.1 vs 0.2
- Batch size: 32 vs 64

All models: 50 neurons, MSE loss, Adam optimizer, 100 epochs.

**Best model (Model 4)**: 3 layers, dropout 0.1, batch size 32. RMSE: GOOG 22.23, FB 4.89, AMZN 48.66. FB predictions were most accurate; AMZN least.

**Key findings**: 3-layer > 4-layer; dropout 0.1 > 0.2; batch size 32 > 64. The paper is a solid baseline reference for LSTM-based stock prediction but limited by single-stock input (no cross-asset features), short feature set (OHLC only), and small universe (3 tech stocks).

## Snippets

> "The best performing algorithm is a LSTM network with 50 neurons, 3 layers, dropout rate 0.1 and batch size 32." [Source: 55614857.pdf p.5]

> "The model used in this project seems to work particularly well on Facebook's stock price, while models to predict Amazon's stock price often produce the highest error." [Source: 55614857.pdf p.5]
