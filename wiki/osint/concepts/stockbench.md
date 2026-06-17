---
title: STOCKBENCH — Standardized Trading Agent Benchmark
type: concept
tags: [concept, backtesting, benchmark, trading-agent, evaluation, cemini-adopt]
keywords: [stockbench, trading benchmark, composite Z-score, return, max drawdown, sortino, contamination-free, multi-month, llm-agent, buy-and-hold, reasoning-gap, variance-tracking]
related:
  - sources/sort-8-4-3.md
  - sources/4-4-link-re.md
  - concepts/quant-finance.md
  - concepts/rl-marl-research.md
  - concepts/llm-agent-systems.md
  - sources/arxiv-ensemble-rl-classifier-models-2502-17518-2026-06-17.md
  - concepts/classifier-assisted-rl-ensemble-trading.md
maturity: validated
created: 2026-04-30
updated: 2026-06-17
---

## Relations

- @sources/sort-8-4-3.md — canonical source: Chen, Yao et al., Tsinghua + BUPT, arXiv:2510.02209v2, March 2026 (K21 deep-read)
- @sources/4-4-link-re.md — K12 deep-read; surfaced STOCKBENCH as Top Steal candidate
- @concepts/quant-finance.md — Quantitative Finance corpus-index hub
- @concepts/rl-marl-research.md — RL/MARL hub; STOCKBENCH provides standardized evaluation layer the MAPPO agent currently lacks
- @concepts/llm-agent-systems.md — LLM agent-systems cluster hub; STOCKBENCH is the primary trading-agent benchmark entry
- @sources/arxiv-ensemble-rl-classifier-models-2502-17518-2026-06-17.md — K120: multi-regime gate before ensemble RL promotion
- @concepts/classifier-assisted-rl-ensemble-trading.md — variance-threshold policy gating sibling

## Raw Concept

What question does this page answer: **What is STOCKBENCH, what does it measure, and how should Cemini adopt it for MAPPO agent evaluation?**

Synthesized from @sources/sort-8-4-3.md (K21 deep-read, 2026-05-01) and @sources/4-4-link-re.md (K12 initial surfacing). The K21 deep-read of the actual STOCKBENCH paper corrected several claims from the K12 secondary-source sketch — most critically, STOCKBENCH does NOT define four named market regimes (bull/bear/sideways/volatile); it evaluates across two temporal windows (downturn Jan–Apr 2025, upturn May–Aug 2025) and finds that model rankings are regime-dependent.

## Narrative

### What STOCKBENCH actually is

STOCKBENCH is a contamination-free benchmark that embeds LLM agents in a realistic multi-month stock trading environment. Agents receive daily market signals (prices, fundamentals, up to 5 news articles per stock) and make sequential buy/sell/hold decisions over 82 trading days. Performance is measured via three financial metrics composited into a single z-score rank:

```
Composite Rank = (z(Return) − z(MaxDrawdown) + z(Sortino)) / 3
```

Three design principles distinguish it from all prior financial benchmarks:
1. **Realistic Market Interaction** — daily information flow mirroring a retail investor's screen
2. **Continuous Decision Making** — sequential daily decisions, not static QA
3. **Contamination-Free Data** — evaluation uses post-training-cutoff data (March–June 2025). Appendix A documents GPT-5 accurately predicting AAPL's 2021 trend without search — direct evidence contamination is real in pre-2024 windows

### What the 14-model benchmark found

The headline results from @sources/sort-8-4-3.md (Table 2):

- **Top model**: Kimi-K2 (Rank 1: 1.9% return, −11.8% drawdown, 0.0420 Sortino)
- **Best return**: Qwen3-235B-Think (2.5%) — but riskier (−14.9% drawdown)
- **Best risk-adjusted**: Qwen3-235B-Ins (2.4% return, −11.2% drawdown)
- **Passive baseline**: 0.4% return, −15.2% drawdown — Rank 12 of 14
- **Worst model**: GPT-OSS-20B (−2.8% return, dead last)

Five structural findings relevant to Cemini:

1. **Reasoning ≠ trading skill.** Qwen3-235B-Ins (instruct) beats Qwen3-235B-Think (reasoning) on risk-adjusted basis. Strong math/coding benchmarks don't predict trading performance. [Source: sort-8-4-3.md §3.2]
2. **All models fail in downturns.** Every tested LLM underperforms buy-and-hold during the Jan–Apr 2025 downturn window. Rankings shift dramatically between regimes — an agent that looks great in a bull run can be the worst performer in a bear market. [Source: sort-8-4-3.md §4.4]
3. **Schema errors are the reasoning-model tax.** Thinking models make fewer arithmetic errors but MORE schema errors (invalid JSON) — they produce overly complex outputs that violate format constraints. This is a structural tradeoff for any reasoning-model-based trading pipeline. [Source: sort-8-4-3.md §4.2]
4. **Larger models handle portfolio complexity better.** Kimi-K2 maintains stable risk-return up to 20 stocks; GPT-OSS-120B deteriorates sharply. Production trading agents should use the largest feasible backbone. [Source: sort-8-4-3.md §4.1]
5. **Return variance is a first-class metric.** DeepSeek-V3 is the most stable (Var = 0.074×10⁻⁴); GPT-OSS-120B is 138× more volatile. A high-variance agent that sometimes wins big and sometimes loses catastrophically is worse in production than a consistently mediocre one. [Source: sort-8-4-3.md Table 5]

### Corrected: what STOCKBENCH does NOT do

The K12 secondary-source sketch described STOCKBENCH as evaluating "across four market regimes: bull, bear, sideways, volatile." The actual paper uses two temporal windows (downturn Jan–Apr 2025, upturn May–Aug 2025) — not four named regimes. The multi-regime insight is directionally correct but the specific framing was an artifact of the secondary source. The key finding — regime-dependence of model rankings — holds regardless.

### Why Cemini needs it

The Cemini MAPPO agent is currently evaluated ad-hoc: pick a historical window, run a backtest, eyeball the equity curve. There is no:
- **Standardized metric** comparable across strategy versions
- **Multi-regime evaluation** — STOCKBENCH's downturn finding (all models fail in bear markets) is a direct warning: ad-hoc window selection can hide catastrophic regime sensitivity
- **Baseline comparison** — is the agent beating buy-and-hold?
- **Variance tracking** — is performance stable across runs or seed-dependent?
- **Reproducibility** — different windows, different conclusions

STOCKBENCH fills all five gaps.

### Integration path

1. **Install**: Clone the Apache-2.0 repo, extract the evaluation harness (Python)
2. **Adapter**: Write a thin adapter wrapping the Cemini backtesting engine to match STOCKBENCH's agent interface
3. **Baseline**: Run the current MAPPO agent through STOCKBENCH to establish a baseline composite z-score AND return variance
4. **Multi-regime gate**: Every MAPPO retrain window produces a STOCKBENCH score across at least two market regimes. If the new score is lower than baseline OR variance increases beyond a threshold, block hot-swap promotion
5. **CI**: Add STOCKBENCH evaluation as a step in the RL retrain pipeline

### Risk assessment

- **License**: Apache-2.0 — zero toxicity
- **Data requirements**: STOCKBENCH assumes US equity data. Adapter needed for crypto (BTC-USD) and prediction-market (Kalshi) contracts
- **Overfitting to the benchmark**: The paper's own finding — GPT-OSS-120B ranks 1st in upturns and last in downturns — demonstrates why single-regime optimization is dangerous. Mitigate by requiring multi-regime evaluation as a hard gate
- **Schema-error rate**: If Cemini adopts a reasoning-model backbone, the execution-validation layer must handle schema deviations (per §4.2 finding)
- **CPU cost**: Backtesting is CPU-bound but runs offline during retrain windows, not in the live trading path

### When to consult this page

- Designing MAPPO agent evaluation pipelines
- Choosing an LLM backbone for trading agents (consult the model ranking table in @sources/sort-8-4-3.md)
- Debugging why a trading agent performs well in backtest but not in production (start with regime-dependence and variance)
- Evaluating whether a new financial benchmark paper is worth ingesting (compare against STOCKBENCH's three design principles)

## Snippets

**S1 — Reasoning-gap finding** (from @sources/sort-8-4-3.md S4):
> "Although reasoning-tuned models such as Qwen3-235B-Think and Qwen3-30B-Think exhibit strong performance in tasks requiring complex reasoning, including math and coding, they do not consistently outperform instruction-tuned counterparts in this trading task."

**S2 — Universal downturn failure** (from @sources/sort-8-4-3.md S9):
> "Notably, all LLM agents underperform the passive baseline during the downturn but outperform it in the upturn, highlighting a key weakness in bearish markets."

**S3 — Original K12 surfacing** (from @sources/4-4-link-re.md):
> "STOCKBENCH: Standardized benchmark for stock trading agents. Composite Z-score: (Return_Z + MDD_Z + Sortino_Z) / 3. Evaluates agents across multiple market regimes. Provides a reproducible evaluation framework the Cemini MAPPO agent currently lacks."
