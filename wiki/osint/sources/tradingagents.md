---
title: "TradingAgents: Multi-Agents LLM Financial Trading Framework"
type: source
tags: [multi-agent-systems, LLM-trading, financial-ai, agent-architecture, debate-driven]
keywords: [TradingAgents, multi-agent trading, LLM finance, agent debate, risk management, bull-bear, structured communication, ReAct]
clusters: [llm-agents]
related:
  - sources/3-25-git-research.md
  - concepts/multi-agent-trading.md
  - sources/generative-agents-park-2023.md
maturity: validated
read_status: deep-read
created: 2026-04-30
updated: 2026-05-13
---

## Relations
- `@sources/3-25-git-research.md` — sibling research source
- `@concepts/multi-agent-trading.md` — concept hub

## Raw Concept
- Original title: TradingAgents: Multi-Agents LLM Financial Trading Framework
- Author(s): Yijia Xiao, Edward Sun (UCLA + Tauric Research), Di Luo (UCLA + MIT), Wei Wang (UCLA + Tauric Research)
- Type: PDF — conference paper (arXiv:2412.20138v7, Jun 2025)
- Location: cemini-librarian:/opt/cemini-bulk/research/TradingAgents- Multi-Agents LLM Financial Trading Framework.pdf
- Retrieved: 2026-04-30
- Pages: 38p (22p main + 16p supplementary)
- Read status: deep-read
- Code: https://github.com/TauricResearch/TradingAgents

## Narrative

TradingAgents proposes a multi-agent LLM financial trading framework that models a real-world trading firm's organizational structure. Seven specialized agent roles across five teams collaborate via structured communication protocols to produce trading decisions. The framework runs entirely on API credits (no GPU required) and supports plug-and-play model substitution.

**Architecture — Five teams, seven roles**:

1. **Analyst Team** (4 agents): Fundamentals Analyst (financial statements, intrinsic value), Sentiment Analyst (social media, insider sentiment), News Analyst (macro, regulatory events), Technical Analyst (MACD, RSI, Bollinger Bands, 60 indicators). Each produces a structured analysis report.

2. **Researcher Team** (2 agents + facilitator): Bullish Researcher and Bearish Researcher engage in multi-round natural-language debate. A facilitator agent selects the prevailing perspective after n rounds and records it as structured state.

3. **Trader Agent** (1 agent): Synthesizes analyst reports + researcher debate outcome → buy/sell/hold decision with sizing. Uses ReAct prompting framework (Yao et al. 2023).

4. **Risk Management Team** (3 agents + facilitator + fund manager): Risk-seeking, Neutral, and Risk-conservative agents debate the trader's decision. Fund manager reviews, adjusts, and approves the final order.

**Communication protocol** (Section 4): Structured documents and diagrams are the primary communication medium — agents query the global state rather than maintaining long chat histories. Natural language is reserved for debate rounds only (Researcher and Risk teams). This avoids the "telephone effect" (information loss over long message histories). Inspired by MetaGPT's structured communication approach. [Source: TradingAgents.pdf pp.8-9]

**Backbone LLMs** (Section 4.3): Analyst nodes + Researchers + Traders use deep-thinking models (o1-preview); data retrieval from APIs uses quick-thinking models (gpt-4o-mini, gpt-4o). Auxiliary expert models handle sentiment analysis. Architecture is model-agnostic — any API-accessible or locally-hosted model can be substituted. [Source: TradingAgents.pdf p.9]

**Experiments** (Section 5-6): Backtest Jan 1 – Mar 29, 2024 on AAPL, GOOGL, AMZN (NVDA, MSFT, META also in dataset). Benchmarked against Buy & Hold, MACD, KDJ+RSI, ZMR, SMA. Metrics: Cumulative Return, Annualized Return, Sharpe Ratio, Maximum Drawdown.

Key results (Table 1): AAPL: +26.62% CR (vs best baseline KDJ&RSI at +2.05%). GOOGL: +24.36% CR (vs best baseline SMA at +6.23%). AMZN: +23.21% CR (vs best baseline SMA at +11.01%). Sharpe ratios: 8.21 / 6.39 / 5.60 across the three stocks. Maximum drawdown: 0.91-2.11%. Improvement over best baseline: 6.1-24.6% in cumulative return. [Source: TradingAgents.pdf pp.10-12]

The authors note the Sharpe ratios are exceptionally high (above 3 = excellent by convention) and attribute this to few pullbacks during the 3-month test window. Each trading decision consumes ~11 LLM calls + 20+ tool calls. [Source: TradingAgents.pdf p.12 footnote]

**Explainability**: All decisions include natural-language reasoning traces (ReAct-style thought/action/observation), providing full audit trail — a key advantage over deep-learning trading systems. [Source: TradingAgents.pdf p.13]

**Relevance to Cemini**: Directly applicable architecture for Cemini's multi-agent trading layer. The structured-communication + limited-debate pattern addresses the same "telephone effect" problem Cemini's orchestrator would face with long agent chains. The model-agnostic plug-and-play design (no GPU dependency, API-credit-only) mirrors Cemini's deployment constraints. The 11-LLM-call-per-decision cost profile is a budget consideration for live deployment.

## Snippets

"Our framework bridges the gap by simulating the multi-agent decision-making processes typical of professional trading teams. It incorporates specialized agents tailored to distinct aspects of trading, inspired by the organizational structure of real-world trading firms." [Source: TradingAgents.pdf p.2]

"TradingAgents achieves at least a 23.21% cumulative return and a 24.90% annual return on the three sampled stocks, surpassing the best-performing baselines by a margin of 6.1%." [Source: TradingAgents.pdf p.11]

"Each decision includes detailed reasoning, tool usage, and thought processes, enabling traders to understand and debug the system. This transparency empowers traders to fine-tune the framework." [Source: TradingAgents.pdf p.13]
