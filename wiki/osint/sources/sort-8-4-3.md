---
title: 'STOCKBENCH: Can LLM Agents Trade Stocks Profitably In Real-world Markets?'
type: source
tags: [pdf, deep-read, llm-agents, quant-finance, benchmark, trading-agent]
keywords: [stockbench, llm-trading-agent, benchmark, contamination-free, djia, composite-z-score, cumulative-return, max-drawdown, sortino-ratio, back-trading, buy-and-hold, kimi-k2, qwen3, deepseek, gpt-oss, temporal-separation, realistic-market-interaction]
related:
  - concepts/stockbench.md
  - concepts/llm-agent-systems.md
  - concepts/quant-finance.md
  - concepts/rl-marl-research.md
maturity: validated
read_status: deep-read
created: 2026-04-23
updated: 2026-05-01
clusters:
  - llm-agents
  - quant-finance
---
## Relations

- @concepts/stockbench.md — canonical concept page; STOCKBENCH as standardized trading agent benchmark
- @concepts/llm-agent-systems.md — cluster hub for LLM agent-systems research
- @concepts/quant-finance.md — Quantitative Finance corpus-index hub
- @concepts/rl-marl-research.md — RL/MARL hub; STOCKBENCH provides evaluation layer for MAPPO agent

## Raw Concept

- **Original title**: STOCKBENCH: Can LLM Agents Trade Stocks Profitably In Real-world Markets?
- **Author(s)**: Yanxu Chen, Zijun Yao, Yantao Liu, Amy Xin (Tsinghua University); Jin Ye, Jianing Yu (Beijing University of Posts and Telecommunications); Lei Hou, Juanzi Li (Tsinghua University)
- **Type**: PDF (arXiv preprint)
- **Location**: `cemini-librarian:/opt/cemini-bulk/research/sort 8 4:3.pdf`
- **Retrieved**: 2026-04-23
- **Pages / length**: 12p
- **Read status**: deep-read (K21, 2026-05-01)
- **arXiv**: 2510.02209v2 (submitted September 2025, revised March 2026)
- **Project**: https://stockbench.github.io/ | GitHub: https://github.com/ChenYXxxx/stockbench

## Narrative

**[K21 DEEP-READ — 2026-05-01]** STOCKBENCH is the first contamination-free benchmark for LLM trading agents operating in realistic multi-month stock markets. It evaluates 14 models (open-weight + closed APIs) on 20 DJIA stocks over 82 trading days (March–June 2025, post-training-cutoff), using three financial metrics composited into a z-score rank. The headline finding: most LLM agents outperform the passive buy-and-hold baseline on absolute return AND risk, but reasoning-tuned models don't consistently beat instruction-tuned counterparts — static reasoning benchmarks don't translate to dynamic trading environments.

### Three benchmark design principles

The authors identify three principles absent from prior financial benchmarks:

1. **Realistic Market Interaction** — agents receive daily prices, fundamentals, and up to 5 news articles per stock (via Finnhub API), mirroring what a retail investor sees at market open
2. **Continuous Decision Making** — agents make sequential buy/sell/hold decisions each trading day, adapting over time rather than answering static QA
3. **Contamination-Free Data** — evaluation uses March–June 2025 data, strictly post-training-cutoff for all tested models. Appendix A documents that GPT-5 (without search) could accurately predict AAPL's 2021 trend, confirming contamination risk in pre-2024 evaluation windows

Table 1 compares STOCKBENCH against 8 prior benchmarks — only STOCKBENCH satisfies all five desired properties (Market Simulation, Multi Month, Continuous Decision, Contamination Free, Direct Economic Value).

### Back-trading environment

- **Universe**: 20 highest-weighted DJIA stocks, diverse sector representation
- **Period**: March 3–June 30, 2025 (82 trading days)
- **Starting capital**: $100,000 cash, zero holdings
- **Data feed**: historical prices (daily OHLCV), fundamentals (market cap, P/E, dividend yield, 52-week high/low, recent quarterly dividends), news (Finnhub API, top-5 articles from prior 48 hours per stock)
- **Decision frequency**: once per day at market open

### Agent workflow — 4 steps

1. **Portfolio Overview** — scan all stocks: recent news, current holdings, historical actions, opening prices
2. **In-Depth Stock Analysis** — select stocks for deeper fundamental analysis (market cap, P/E ratio, dividend yield)
3. **Decision Generation** — for each stock: increase, decrease, or hold position. Three discrete actions, no continuous sizing
4. **Execution and Validation** — convert dollar targets to share quantities at opening price; liquidity validation (flag + retry if decisions exceed available cash)

### Evaluation metrics

- **Final Return** = (V_T − V_0) / V_0 — absolute profitability
- **Maximum Drawdown** = min_t∈[0,T] (V_t − max_{s≤t} V_s) / max_{s≤t} V_s — worst peak-to-trough decline
- **Sortino Ratio** = R_p / σ_d where σ_d uses only downside deviation — risk-adjusted return penalizing only negative volatility (preferred over Sharpe when returns are asymmetric)
- **Composite Rank** = (z(Return) − z(MDD) + z(Sortino)) / 3

### Main results (Table 2, 20-stock setting)

| Rank | Model | Return % | Max DD % | Sortino |
|------|-------|----------|----------|---------|
| 1 | Kimi-K2 | 1.9 | −11.8 | 0.0420 |
| 2 | Qwen3-235B-Ins | 2.4 | −11.2 | 0.0299 |
| 3 | GLM-4.5 | 2.3 | −13.7 | 0.0295 |
| 4 | Qwen3-235B-Think | 2.5 | −14.9 | 0.0309 |
| 5 | OpenAI-O3 | 1.9 | −13.2 | 0.0267 |
| 6 | Qwen3-30B-Think | 2.1 | −13.5 | 0.0255 |
| 7 | Claude-4-Sonnet | 2.2 | −14.2 | 0.0245 |
| 8 | DeepSeek-V3.1 | 1.1 | −14.1 | 0.0210 |
| 9 | GPT-5 | 0.3 | −13.1 | 0.0132 |
| 10 | Qwen3-Coder | 0.2 | −13.9 | 0.0137 |
| 11 | DeepSeek-V3 | 0.2 | −14.1 | 0.0144 |
| 12 | **Passive Baseline** | **0.4** | **−15.2** | **0.0155** |
| 13 | GPT-OSS-120B | −0.9 | −14.0 | 0.0156 |
| 14 | GPT-OSS-20B | −2.8 | −14.4 | −0.0069 |

Three key observations from the authors:

1. **LLM agents can trade profitably.** 11 of 14 models beat or matched the baseline on return; top models delivered 2–2.5% over 4 months.
2. **LLM agents manage downside risk.** ALL tested models achieved lower max drawdown than the baseline (−15.2%). Best agents limit drawdowns to ~−11% to −14%.
3. **Reasoning doesn't guarantee better trading.** Qwen3-235B-Ins (instruct) outperformed Qwen3-235B-Think (reasoning) on risk-adjusted basis (−11.2% vs −14.9% drawdown), despite Think's stronger math/coding benchmark scores.

### Analysis findings

**Portfolio size scaling (§4.1)** — All models degrade as the investment universe expands from 5→30 stocks: mean returns decline, return volatility rises. Kimi-K2 maintains positive expected returns up to 20 stocks; GPT-OSS-120B deteriorates sharply (CV of 10.2 at 20 stocks). Larger models are more robust.

**Error types (§4.2)** — Two error modes: arithmetic errors (miscalculated share quantities) and schema errors (invalid JSON output). Thinking models make fewer arithmetic errors but MORE schema errors — they generate overly complex outputs that violate format constraints. This is a structural tension: stronger reasoning → more complex outputs → higher schema failure rate in structured decision tasks.

**Ablation on data sources (§4.3)** — Removing news and fundamentals progressively degrades returns. Kimi-K2 drops from 1.9% → 1.4% (w/o News) → 0.6% (w/o both). GPT-OSS-120B drops from −1.2% → −3.4%. Both modalities matter; Kimi-K2 is more robust to information removal.

**Market regime sensitivity (§4.4)** — Ranked models over two windows: downturn (Jan–Apr 2025) and upturn (May–Aug 2025). Critical finding: ALL models underperform the passive baseline during the downturn but outperform it during the upturn. Model rankings shift significantly between regimes — GPT-OSS-120B goes from last in downturn to first in upturn. Kimi-K2 maintains the most stable rank across both.

### Return variance (Table 5, Appendix B)

Each model was run 3× with different random seeds. DeepSeek-V3 is the most stable (Var = 0.074×10⁻⁴); GPT-OSS-120B is the most volatile (10.19×10⁻⁴, ~138× more variable). High variance is problematic for production deployment — an agent that sometimes wins and sometimes loses catastrophically is worse than one that consistently ties the baseline.

### Cemini relevance

STOCKBENCH provides direct evidence for several design decisions in the Cemini trading stack:

- **Benchmark infrastructure gap confirmed.** The Cemini MAPPO agent currently has no standardized evaluation — @concepts/stockbench.md's integration path (clone → adapter → baseline → gate → CI) is the right architecture. STOCKBENCH's composite z-score methodology is directly portable.
- **Reasoning-model skepticism validated.** K17's debate-cycle framework assumes stronger reasoning → better decisions. STOCKBENCH shows this doesn't hold in trading — Qwen3-Think underperforms Qwen3-Ins on risk-adjusted basis. The "reasoning gap" in dynamic environments is real.
- **Multi-regime evaluation is non-negotiable.** All models fail in downturns. An agent optimized on a bull-run window would look great and lose money in production. The Cemini MAPPO agent must be evaluated across at least two market regimes.
- **News + fundamentals both matter.** The ablation study confirms Cemini's dual-signal architecture (market data + news feeds) — removing either degrades performance.
- **Variance tracking is a first-class metric.** Return variance across runs (Table 5) should be tracked alongside mean return. A high-variance agent is a production risk regardless of mean performance.
- **Schema-error tradeoff is an architectural constraint.** Thinking/reasoning models produce more format errors — if Cemini adopts a reasoning-model backbone, the execution-validation layer (Step 4) must be robust to schema deviations.
- **Scale matters for multi-asset trading.** Larger models handle portfolio expansion better. The 235B Qwen3 variants outperform all smaller models; GPT-OSS-20B is dead last. Production deployment should use the largest feasible model.

### Limitations (per authors)

Daily trading only (no intraday); 4-month window (misses full market cycles); 20 large US stocks only; no trading costs, slippage, or liquidity constraints modeled; agents trade once per day at market open. These simplifications make trading easier than reality — real-world performance would be worse.

### When to consult this page

- Evaluating whether a new LLM is suitable as a Cemini trading-agent backbone
- Designing MAPPO agent evaluation pipelines
- Understanding why reasoning benchmarks don't predict trading performance
- Assessing information-source contributions (news vs fundamentals) to agent decisions
- Comparing STOCKBENCH methodology against alternatives (InvestorBench, FinBench, FinQA)

## Snippets

**S1 — Abstract: reasoning-trading gap** (p.1):
> "Surprisingly, most models struggle to outperform the simple buy-and-hold baseline, while some models demonstrate the potential to achieve higher returns and stronger risk management. These findings highlight both the challenges and opportunities of LLM-based trading agents, showing that strong performance on static financial question-answering do not necessarily translate into effective trading behavior."

**S2 — Three design principles** (pp.2–3, §1):
> "Realistic Market Interaction: the benchmark must simulate the information flow and constraints faced by human traders... Continuous Decision Making: the benchmark should require agents to make sequential decisions over time, adapting to new information as it becomes available... Contamination-Free Data: the evaluation data must be temporally separated from the training data of evaluated models."

**S3 — Contamination evidence** (p.11, Appendix A):
> "When testing GPT-5 (without using the search function), we found that the model could accurately predict the stock trend of AAPL in 2021, and the model's response was consistent with the facts. This discovery indicates that if the evaluation time is relatively early, the model may have obtained future information that could not have been reasonably acquired at the time of evaluation."

**S4 — Reasoning doesn't guarantee performance** (pp.6–7, §3.2):
> "Although reasoning-tuned models such as Qwen3-235B-Think and Qwen3-30B-Think exhibit strong performance in tasks requiring complex reasoning, including math and coding, they do not consistently outperform instruction-tuned counterparts in this trading task. For example, Qwen3-235B-Ins outperforms its reasoning-tuned version with a lower maximum drawdown (−11.2% vs. −14.9%). This suggests there is still a gap between reasoning ability and effective decision-making in dynamic, noisy environments like financial markets."

**S5 — Portfolio scaling challenge** (p.7, §4.1):
> "All evaluated models exhibit performance degradation as the investment portfolio size increases, characterized by declining mean returns and rising return volatility. This indicates that scaling the number of tradable assets poses a non-trivial challenge for LLM agents."

**S6 — Model scale confers robustness** (p.7, §4.1):
> "The larger-scale model, Kimi-K2, demonstrates greater robustness to portfolio expansion, maintaining relatively stable risk-return profiles and achieving positive expected returns at moderate portfolio sizes (e.g., 10–20 stocks), whereas the smaller GPT-OSS-120B suffers from severe performance deterioration and excessive variability, suggesting that increased model capacity enhances generalization and stability in multi-asset decision-making contexts."

**S7 — Schema vs. arithmetic error tradeoff** (p.7, §4.2):
> "Thinking models make fewer arithmetic errors than instruct models, consistent with their stronger reasoning ability. Yet, they also incur more schema errors, likely due to their tendency to generate overly complex outputs that deviate from the expected format."

**S8 — Ablation confirms dual-signal value** (p.7, §4.3):
> "Cumulative returns drop as news and then fundamentals are removed, confirming their importance. This behavior matches our expectation that both information sources play an important role in guiding trading decisions."

**S9 — Downturn failure is universal** (p.8, §4.4):
> "Notably, all LLM agents underperform the passive baseline during the downturn but outperform it in the upturn, highlighting a key weakness in bearish markets."

**S10 — Model ranking instability across regimes** (p.8, §4.4):
> "GPT-OSS-120B moves from bottom-ranked in the downturn to top-ranked in the upturn, suggesting sensitivity to bullish markets, while Kimi-K2 remains relatively stable, indicating greater robustness to market fluctuations."

**S11 — Contamination-free as first-of-kind** (p.8, §5.2):
> "STOCKBENCH is the first benchmark to embed LLM agents in realistic, multi-stock trading environments with continuously updated market data. STOCKBENCH bridges the gap between static financial QA benchmarks and the practical challenges of real-world investment strategies."

**S12 — Return variance as stability signal** (p.11, Table 5):
> "Models with higher return variances may exhibit more unpredictable behaviors, which is undesirable in many real-world applications, especially in high-risk environments such as financial decision-making. DeepSeek-V3 exhibited the smallest performance fluctuation, indicating high stability. In contrast, GPT-OSS-120B exhibits the highest return variance."
