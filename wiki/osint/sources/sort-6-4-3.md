---
title: ChatGPT in Systematic Investing — Enhancing Risk-Adjusted Returns with LLMs
type: source
tags: [pdf, llm-agents, portfolio-strategy, market-microstructure, momentum, sentiment, news-analysis, chatgpt]
related:
  - concepts/llm-agent-systems.md
  - concepts/market-microstructure.md
  - concepts/portfolio-strategy.md
maturity: validated
read_status: read-skim
created: 2026-04-23
updated: 2026-04-26
clusters:
  - llm-agents
  - portfolio-strategy
  - market-microstructure
---

## Relations

- @concepts/llm-agent-systems.md — cluster hub for LLM agent-systems research in the Cemini corpus
- @concepts/market-microstructure.md — Market Microstructure corpus-index hub (Q 2026-04-27)
- @concepts/portfolio-strategy.md — Portfolio Strategy corpus-index hub (Q 2026-04-27)

## Raw Concept

- **Original title**: ChatGPT in Systematic Investing: Enhancing Risk-Adjusted Returns with LLMs
- **Author(s)**: Nikolas Anic (Finreon AG), Andrea Barbon (University of St. Gallen, corresponding), Ralf Seiz (Finreon / St. Gallen), Carlo Zarattini (Concretum Group)
- **Affiliation**: Finreon AG, University of St. Gallen, Concretum Group
- **Type**: PDF
- **Location**: research for cemini/sort 6 4:3.pdf
- **Length**: 26p
- **Retrieved**: 2026-04-23 (download date, not publication)
- **Publication date**: arXiv:2510.26228v1, 30 Oct 2025
- **Read status**: read-skim
- **Primary cluster**: llm-agents
- **All clusters**: llm-agents, portfolio-strategy, market-microstructure

## Narrative

Peer-review-adjacent academic paper testing whether ChatGPT 4.0 mini can extract predictive signals from firm-specific news to enhance a Carhart cross-sectional momentum strategy on S&P 500 constituents. Methodology is disciplined: validation set Oct 2019 – Dec 2023 (1,070 daily obs), test set Jan 2024 – Mar 2025 (312 obs) — crucially, test set starts after the model's Oct 2023 pre-training cutoff, mitigating information leakage concerns. Hyperparameter grid search over 512 configurations using a U(θ) = 0.75·Sharpe − 0.25·MDD objective.

The LLM is prompted with firm-specific news from Stock News API (minute-timestamped), told the stock is entering a momentum portfolio, and asked to output a 0–1 continuation probability. Scores then condition both selection (ranking) and weight tilts via W_i = E · η^LLM_Score_i with η=5 optimal. Baseline uses top-decile of 12-month returns (ex-last-month).

Honest assessment: this is genuine academic work (arXiv q-fin.PM, not vendor marketing), but it has important limits the authors acknowledge — 15-month out-of-sample window, alpha of 3.26% only significant at 10% level, single-model single-universe (SPX only), no robustness to crisis regimes. The news-data dependency on Stock News API is a non-trivial infrastructure cost. Relevance: directly applicable to Cemini's watchlist-driven strategies; prompt-engineering patterns are reusable.

## Key findings

- LLM-enhanced portfolio Sharpe 1.06 vs baseline 0.79 out-of-sample (Jan 2024 – Mar 2025); Sortino 1.28 vs 0.93.
- Optimal hyperparameters: monthly rebalancing (not weekly), 1-day news lookback (not 5), basic prompt (not advanced), 50 stocks, value-weighted base, η=5 tilt, 15% per-stock cap.
- Performance concentrated: Sharpe ~1.3 with 25 holdings, declining to ~0.9 at 100 holdings — LLM edge is in high-conviction identification, not broad coverage.
- Basic prompt beats Advanced prompt (Sharpe 1.1 vs 0.95); simpler framing sufficient.
- Out-of-sample (post-training-cutoff) gains exceed in-sample, undermining pre-training leakage as a confound — but OOS alpha only significant at 10%.
- Transaction costs assumed 2 bps (conservative for SPX liquidity); turnover 0.80 LLM vs 0.48 baseline OOS.

## Snippets

- **p.1 (abstract)** — "An LLM-enhanced momentum strategy outperforms a standard long-only momentum benchmark, delivering higher Sharpe and Sortino ratios both in-sample and in a truly out-of-sample period after the model's pre-training cut-off." — Core claim.
- **p.18 (Table 3)** — "OOS Sharpe 0.79 baseline vs 1.06 LLM-enhanced; Sortino 0.93 vs 1.28; Return 0.24 vs 0.30" — Headline result, net of 2 bps costs.
- **p.18** — "a time-series regression of LLM-enhanced returns on baseline returns yields a positive annualized alpha of 3.26%, but the estimate is statistically significant only at the 10% level" — Candid stat-significance caveat.
- **p.17 (Table 2)** — "Optimal: τ=Month, k=1 day, l=21 days, π=Basic, m=50, c=True, w=Value, η=5" — Reproducible config.
- **p.20** — "Expanding the input window from 1 to 5 days of news only marginally improves the Sharpe ratio." — Practical cost-saver: less news needed.
- **p.8** — "ChatGPT 4.0 mini was trained on data only up to October 2023, the Test Set, which extends from January 2024 to March 2025, lies in a truly out-of-sample regime" — Leakage mitigation rationale.
