---
title: "Event-based prediction-market ML — why equity-style modeling breaks on Polymarket"
type: concept
tags: [concept, polymarket, neural-networks, machine-learning, lstm, time-series, validation, prediction-markets, event-based, k56]
keywords: [conditional-probability-modeling, event-rolling-adf-filter, cross-event-learning, synthetic-ornstein-uhlenbeck-trajectories, parameter-budget-rule, log-loss-kill-rule, temporal-split-by-start-date, alexo_0x, prediction-market-overfitting]
related:
  - sources/posts-prediction-markets-quant-frameworks-2026-05-21.md
  - concepts/time-series-arima-garch-framework.md
  - concepts/lstm-stock-prediction-baseline.md
  - concepts/markov-regime-switching-models.md
  - concepts/polymarket-bot-architecture.md
  - concepts/polymarket-microstructure-findings.md
  - concepts/monte-carlo-permutation-test-mcpt.md
  - concepts/prediction-market-historical-analysis.md
  - entities/people/alexo-0x.md
  - concepts/alpha-eval-formula-mining-framework.md
maturity: validated
created: 2026-05-21
updated: 2026-06-03
clusters: [polymarket, quant-finance, machine-learning]
---

## Relations

- @sources/posts-prediction-markets-quant-frameworks-2026-05-21.md — Post 0 (@Alexo_0x) primary source
- @concepts/time-series-arima-garch-framework.md — the *equity-style* time-series framework that this page extends with event-resolution caveats
- @concepts/lstm-stock-prediction-baseline.md — baseline LSTM page; this concept catalogs why the baseline fails when ported to prediction markets
- @concepts/markov-regime-switching-models.md — the "regime change near resolution" framing is structurally similar to a Markov regime switch with known transition timing
- @concepts/polymarket-bot-architecture.md — sets the operational context for any ML-driven Polymarket bot
- @concepts/polymarket-microstructure-findings.md — final-hour dynamics (thicker order books, algorithmic MMs arbing aggressively) are documented here
- @concepts/monte-carlo-permutation-test-mcpt.md — complementary strategy-validation framework (this page is event-aware, MCPT is randomization-based)
- @concepts/prediction-market-historical-analysis.md — cross-event learning requires a curated historical event corpus
- @entities/people/alexo-0x.md — author

## Raw Concept

What prompted this page: K56 Posts.docx Post 0 — @Alexo_0x's "Neural Networks for Polymarket & Crypto Prediction Markets: Why 94% of Signal Models Fail in Product." Synthesizes a five-part rejection-criteria framework specifically targeting the **event-resolution structure** that breaks equity-style ML modeling on Polymarket.

## Narrative

Equity-style time-series ML (ARIMA + GARCH on returns, LSTM on rolling windows) assumes a **continuous** observation stream. Prediction markets break this assumption in three specific ways:

1. The target is `P(Outcome=1 | X_t)`, a probability, not a price expectation.
2. The data distribution shifts qualitatively as resolution approaches — the same market is structurally different 60 days out vs 1 hour out.
3. Each event is its own independent sample. Three years of data ≠ 750 daily observations; it's 150-250 distinct events.

Together these mean that **the standard quant-trading playbook (rolling window backtest, Sharpe-ratio kill rule, train-test temporal split on price history) fails silently** — the backtest shows profit, the live deployment loses capital. The Alexo_0x framework is a rejection-criteria checklist designed to catch each of the three failure modes before deployment.

### 1. What a NN actually learns on prediction markets

Classical trading: `f(X) ≈ E[P_{t+1} | X_t]` (conditional price expectation).

Polymarket: `f(X) ≈ P(Outcome=1 | X_t)` (conditional outcome probability after `N` days/hours).

Seems simpler. **It's not.** The distribution `P(Outcome | X)` shifts qualitatively as the resolution date approaches:

| Time-to-resolution | Typical Polymarket price |
|---|---|
| 60 days before | ~0.6 (broad uncertainty) |
| 1 hour before | ~0.95 or ~0.05 (near-resolved) |
| Post-resolution | 1.0 or 0.0 |

A model trained on 60-day-out data **knows nothing** about the dynamics of the final hour. Compounding pressures in 2026:

- **Algorithmic MMs** arbitrage final-hour price discrepancies aggressively (post K55 LP-rewards-farming context — they're chasing the same boosted-rewards window)
- **News-flow acceleration** (AI aggregators, X bots inject information at sub-minute cadence)
- **Thicker books late** — large players enter at the last moment

The model needs to either (a) condition explicitly on `time-to-resolution`, or (b) be trained only within a constant time-to-resolution slice (e.g., "always predict the next hour, never predict 60 days out").

### 2. Stability filter (event-aware ADF)

On equities, the Augmented Dickey-Fuller test runs once on a rolling window across one continuous series. On Polymarket, the filter must operate **per event** — events cannot be concatenated into one series.

```python
import numpy as np
import pandas as pd
from statsmodels.tsa.stattools import adfuller

def event_rolling_adf_filter(event_price_series, lookback_hours=168, step_hours=24):
    """
    Stability filter for a single Polymarket event.
    event_price_series: time series of contract price (probability)
    lookback_hours: window in hours for ADF test
    step_hours: shift step
    Returns True if the feature is sufficiently stable.
    """
    results = []
    for start in range(0, len(event_price_series) - lookback_hours, step_hours):
        window = event_price_series.iloc[start:start + lookback_hours].dropna()
        if len(window) < lookback_hours * 0.7:
            continue
        pval = adfuller(window)[1]
        results.append(pval)
    if len(results) == 0:
        return False
    unstable_ratio = sum(1 for p in results if p > 0.05) / len(results)
    return unstable_ratio < 0.2  # passes if <20% of windows non-stationary
```

The 168-hour (1-week) lookback and 24-hour step are reasonable defaults; tune to match market velocity.

### 3. Why LSTMs fail on Polymarket (and what works)

**Sample-count math**: daily equities give ~750 samples per 3-year history. Polymarket gives **one sample per resolved event**. You cannot train an LSTM on a single event.

Two approaches that actually work:

**Approach A — Cross-event learning** (150-250 events across categories):

```python
events = [
    {
        'event_id': 'us_election_2024',
        'time_series': pd.Series(...),  # contract price over time
        'outcome': 1,
        'start_date': '2024-01-01'
    },
    {
        'event_id': 'btc_100k_2026',
        'time_series': pd.Series(...),
        'outcome': 0,
        'start_date': '2025-06-01'
    },
    # ... 150-200 more events
]
```

Train across categories that share probability-trajectory structure (elections, crypto thresholds, regulatory decisions, AI events). Important: **a model trained on US elections does not automatically transfer to crypto.** Retraining required.

**Approach B — Synthetic data + transfer learning**:

1. Generate 10,000+ synthetic probability trajectories using **Ornstein-Uhlenbeck** processes with parameterized volatility / drift / end-of-life collapse behavior.
2. Train the model on synthetic data.
3. Fine-tune on 3-5 real events from the new category.

Without synthetic pre-training, LSTMs are useless on Polymarket due to sample-count starvation.

### 4. Hard parameter-budget rule

`max_params ≤ total_samples / 20`

Worked examples:

| Events | Avg event length | Total samples | Max params |
|---|---|---|---|
| 150 | 500h (~21d) | 75,000 | 3,750 |
| 80 | 200h (~8-9d) | 16,000 | 800 |
| 120 | 350h | 42,000 | 2,100 |

**Conclusion**: use very small networks for Polymarket. `hidden_size=8` or `16` is normal. `hidden_size=32` is risky. `hidden_size=64+` guarantees overfitting.

This is much tighter than equity-LSTM defaults (which routinely use 64-256). The "rule of 20" is reasonable for sample-efficiency on independent samples and matches the order-of-magnitude rule from VC-dimension bounds for small-data regression.

### 5. Honest validation — temporal split by `start_date`

```python
def event_temporal_split(events_list, train_ratio=0.7, val_ratio=0.15):
    """Sort by start_date, then train/val/test."""
    sorted_events = sorted(events_list, key=lambda x: x['start_date'])
    n = len(sorted_events)
    train_end = int(n * train_ratio)
    val_end = int(n * (train_ratio + val_ratio))
    return sorted_events[:train_end], sorted_events[train_end:val_end], sorted_events[val_end:]
```

**Must-do**:
- Sort by `start_date`
- Train only on older events
- Normalize features **within each event separately**

**Must NOT do**:
- Random shuffling (destroys temporal causality)
- Including future events in training
- Normalizing across the entire dataset (information leak across events)

**Lookahead pitfall**: any feature that uses information available *after* the prediction timestamp = cheating. Common failure mode: a Polymarket contract reflects rumors 2 days before official news; your "future news" feature accidentally uses the leaked rumor signal → backtest shows profit, live deployment doesn't.

### 6. Kill conditions for event-based models

On equities, the standard kill rule is Sharpe < 0.25 over 90 days. On Polymarket, **90 days is only 3-5 events** — far too small for statistics.

Two adapted thresholds:

**Threshold 1 — Log-loss gap vs market**:

```
LL = -(1/N)·Σ [y_i·log(p_i) + (1-y_i)·log(1-p_i)]
```

Kill rule: if model log-loss > market log-loss over the last 5-7 events, **the market is predicting better than your model**. Disable.

```python
def should_kill_model(predictions, outcomes, market_prices, lookback_events=7):
    import numpy as np
    last_pred = predictions[-lookback_events:]
    last_out = outcomes[-lookback_events:]
    last_prices = market_prices[-lookback_events:]
    eps = 1e-6
    model_ll = -np.mean([
        o*np.log(max(p, eps)) + (1-o)*np.log(max(1-p, eps))
        for o, p in zip(last_out, last_pred)
    ])
    market_ll = -np.mean([
        o*np.log(max(m, eps)) + (1-o)*np.log(max(1-m, eps))
        for o, m in zip(last_out, last_prices)
    ])
    return model_ll > market_ll  # True -> kill
```

**Threshold 2 — Bayesian factor** for small samples (truncated in source; the principle is to compare model's posterior likelihood under the data against a noise-baseline likelihood, with explicit small-sample correction).

### Operational implications for Cemini

The Cemini Polymarket workstream currently has:
- @concepts/polymarket-bot-architecture.md — taker-side bot architecture (no ML model layer yet)
- @concepts/polymarket-lp-rewards-farming.md — pure maker-side LP-farming (no ML required; pricing comes from order book + reward structure)
- @concepts/time-series-arima-garch-framework.md — equity-style time-series framework (would mis-fire on Polymarket if applied naively)

Any future Cemini ML model targeting Polymarket directional prediction (vs LP-farming, which doesn't need a model) **must** satisfy:

1. Per-event ADF stability filter before training inclusion.
2. Cross-event training corpus OR synthetic-OU pre-training + small fine-tune.
3. Parameter budget `≤ samples / 20`. For a 200-event corpus at 500h avg, this caps the model at ~5,000 trainable params (rules out anything LSTM-with-hidden-size>32).
4. Temporal split by event start-date. Per-event feature normalization.
5. Live kill rule: log-loss vs market over last 5-7 events.

The @phosphenq MCPT framework (@concepts/monte-carlo-permutation-test-mcpt.md) is complementary — MCPT validates that the *backtest* is real, the Alexo_0x framework validates that the *modeling assumptions* are appropriate to the event-resolution structure.

## Snippets

> "On Polymarket, you have a binary outcome after N days or hours: `f(X) ≈ P(Outcome=1 | X_t)`. Probability. Not price. Seems simpler. But it's not."
> — @Alexo_0x [Source: Posts.docx Post 0]

> "On equities, we use the ADF test on a rolling window. On Polymarket, the filter must work within each event separately, because events cannot be concatenated into a single series."
> — @Alexo_0x [Source: Posts.docx Post 0]

> "On daily equities: 750 samples over 3 years. On Polymarket: one sample per event (resolved yes/no). You cannot train an LSTM on a single event."
> — @Alexo_0x [Source: Posts.docx Post 0]

> "Maximum trainable parameters should not exceed the number of samples divided by 20."
> — @Alexo_0x [Source: Posts.docx Post 0]

> "If over the last 5-7 events your model's log-loss is worse than the market's log-loss […] the model is useless. The market predicts better on its own."
> — @Alexo_0x [Source: Posts.docx Post 0]
