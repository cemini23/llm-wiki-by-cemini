---
title: STOCKBENCH — Standardized Trading Agent Benchmark
type: concept
tags: [concept, backtesting, benchmark, trading-agent, evaluation, cemini-adopt]
keywords: [stockbench, trading benchmark, composite Z-score, return, max drawdown, sortino, multi-regime, reproducibility]
related:
  - sources/4-4-link-re.md
  - concepts/quant-finance.md
  - concepts/rl-marl-research.md
maturity: validated
created: 2026-04-30
updated: 2026-04-30
---

## Relations

- @sources/4-4-link-re.md — K12 deep-read; primary source. STOCKBENCH evaluated as Top Steal.
- @concepts/quant-finance.md — Quantitative Finance corpus-index hub
- @concepts/rl-marl-research.md — RL/MARL hub; STOCKBENCH provides the standardized evaluation layer the MAPPO agent currently lacks

## Raw Concept

Surfaced as a Top Steal in @sources/4-4-link-re.md. STOCKBENCH (Apache-2.0) is a standardized benchmark for evaluating stock trading agents across multiple market regimes. It addresses a genuine gap in the Cemini stack: currently there is no reproducible backtesting benchmark — strategy performance is evaluated ad-hoc against whatever historical window the developer picks.

## Narrative

### What it is

STOCKBENCH is a standardized evaluation framework for trading agents. It defines a composite Z-score metric:

```
Score = (Return_Z + MDD_Z + Sortino_Z) / 3
```

Where each component is a Z-score normalized against a baseline (e.g., buy-and-hold, equal-weight portfolio). The composite covers three dimensions:
- **Return_Z**: absolute performance
- **MDD_Z**: risk (Maximum Drawdown)
- **Sortino_Z**: risk-adjusted return (downside deviation only, unlike Sharpe which penalizes upside)

Agents are evaluated across four market regimes: bull, bear, sideways, volatile. This multi-regime design prevents overfitting to a single market condition — an agent that crushes bull markets but collapses in bear markets gets a low composite score.

### Why Cemini needs it

The Cemini MAPPO agent is currently evaluated ad-hoc. The developer picks a historical window, runs a backtest, and eyeballs the equity curve. There is no:
- Standardized metric that's comparable across strategy versions
- Multi-regime evaluation (does the agent work in bear markets?)
- Baseline comparison (is the agent beating buy-and-hold?)
- Reproducibility (different windows, different conclusions)

STOCKBENCH fills all four gaps. It turns strategy evaluation from "looks good" to a reproducible number.

### Integration path

1. **Install**: Clone the Apache-2.0 repo, extract the evaluation harness (Python)
2. **Adapter**: Write a thin adapter that wraps the Cemini backtesting engine to match STOCKBENCH's agent interface
3. **Baseline**: Run the current MAPPO agent through STOCKBENCH to establish a baseline composite Z-score
4. **Gate**: Every MAPPO retrain window (April 14–17 schedule) produces a new STOCKBENCH score. If the new score is lower than the baseline, the retrained policy is blocked from hot-swap promotion
5. **CI**: Add STOCKBENCH evaluation as a step in the RL retrain pipeline

### Risk assessment

- **License**: Apache-2.0 — zero toxicity
- **Data requirements**: STOCKBENCH may assume US equity data. Adapter needed for crypto (BTC-USD) and prediction-market (Kalshi) contracts
- **Overfitting to the benchmark**: If the agent is optimized against STOCKBENCH's specific regimes, it may not generalize. Mitigate by periodically adding new regimes or out-of-sample periods
- **CPU cost**: Backtesting is CPU-bound but runs offline during retrain windows, not in the live trading path

## Snippets

> "STOCKBENCH: Standardized benchmark for stock trading agents. Composite Z-score: (Return_Z + MDD_Z + Sortino_Z) / 3. Evaluates agents across multiple market regimes (bull, bear, sideways, volatile). Provides a reproducible evaluation framework the Cemini MAPPO agent currently lacks." [Source: 4_4 link re.docx §STOCKBENCH]
