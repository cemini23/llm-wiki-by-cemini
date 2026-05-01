---
title: Recency-Weighted Fundamental Data — Mixed-Frequency Macro Feature Engineering
type: concept
tags: [concept, feature-engineering, fundamental-data, macro, recency-weighting, timescaledb, cemini-adopt]
keywords: [recency weighting, fundamental data, macro variables, mixed frequency, days since publication, feature engineering, timescaledb]
related:
  - sources/forex-1-4-4.md
  - sources/4-4-link-re-2.md
  - concepts/quant-finance.md
maturity: validated
created: 2026-04-30
updated: 2026-04-30
---

## Relations

- @sources/forex-1-4-4.md — K12 deep-read; King & Amigó 2025. Primary source for recency-weighted macro data in EUR-USD LSTM.
- @sources/4-4-link-re-2.md — K12 deep-read §Target Domain 5; convergent source. Independently identifies recency weighting + directional index.
- @concepts/quant-finance.md — Quantitative Finance corpus-index hub

## Raw Concept

Two independent K12 sources converge on the same lightweight pattern: when mixing low-frequency fundamental data (quarterly GDP, monthly unemployment) with high-frequency price data (daily OHLCV), add a "days since last publication" feature so the model can weight stale macro data appropriately. This is the strongest cross-document convergence in K12 outside of Nomotic AI — two independently authored sources arrive at the identical mechanism. [CONFIRMED]

## Narrative

### The problem

Fundamental macroeconomic data (GDP, unemployment, inflation, debt/GDP) is published at low frequencies — quarterly or monthly. Price data is daily or intraday. When you merge them into a single dataset for an ML model, you face a structural problem: on day 45 of a quarter, the GDP figure you're feeding the model is 45 days stale. A naive merge treats it as equally fresh as yesterday's closing price.

This is not a theoretical edge case. King & Amigó (@sources/forex-1-4-4.md) found that fundamental-only models (AUC_min = 0.65) dramatically outperformed technical-only models (AUC_min = 0.57) for EUR-USD forecasting — but only when the recency problem was addressed. The Cemini MAPPO agent currently ingests macro data without recency awareness.

### The solution

Add a single column to the TimescaleDB feature table: `days_since_publication`. For each fundamental variable, this is the integer number of days between the observation date and the most recent publication date for that variable.

Example:
```
Date       | GDP_US | GDP_US_days_since | UNRATE_US | UNRATE_US_days_since | Close
2023-02-15 | 26.1   | 16                | 3.4       | 12                   | 1.0723
2023-02-16 | 26.1   | 17                | 3.4       | 13                   | 1.0687
```

The model learns to weight `GDP_US` by `GDP_US_days_since` — the staler the data, the less weight it gets. This is handled automatically by the neural network during training; no manual weighting function is needed.

### Implementation

1. Add `days_since_publication` columns to the TimescaleDB hypertable for each fundamental variable
2. Populate on each data ingestion: compute `(observation_date - last_publication_date).days`
3. No changes to the MAPPO architecture needed — the model learns recency-weighting from the data
4. CPU cost: one integer subtraction per row per variable — effectively free

### Cross-source convergence → [CONFIRMED]

This pattern appears independently in:
- @sources/forex-1-4-4.md — King & Amigó 2025: "A feature capturing the number of days since the latest release was included, allowing the model to weight information according to its recency during the training process."
- @sources/4-4-link-re-2.md §Target Domain 5: "Recency weighting — assigning decaying weights to fundamental data based on days since publication."

Two independent sources, same mechanism, same rationale. This is the highest-confidence adoption in the K12 batch.

### Directional index — companion pattern

Both sources also converge on the directional index target formulation (composite of max-profit-path, max-loss-path, terminal price). See @sources/forex-1-4-4.md for implementation. This is a second [CONFIRMED] pattern from the same convergent pair.

## Snippets

> "Due to the differences in the publication frequency of the data (annually, quarterly, monthly), for each variable we kept track of the number of days since the last publication date, so that the LSTM net could establish a relationship between each variable and the number of days since the corresponding data publication." [Source: forex 1 4:4.pdf p.4]

> "Recency weighting: assigning decaying weights to fundamental data based on days since publication. Identical mechanism to King & Amigó 2025 forex paper." [Source: 4_4 link re 2.docx §Target Domain 5]
