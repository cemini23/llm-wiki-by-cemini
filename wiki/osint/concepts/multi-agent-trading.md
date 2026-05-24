---
title: Multi-agent trading — LLM agent teams for financial decision-making
type: concept
tags: [concept, multi-agent, trading, agent-orchestration, llm-trading, cemini-relevant]
keywords: [multi-agent trading, agent orchestration, tradingagents, analyst-trader pattern, debate framework, hierarchical agents]
related:
  - sources/tradingagents.md
  - sources/multi-wiki-tool-eval-36url-wiki-ingestion-2026-05-24.md
  - entities/tools/tradingagents-cn.md
  - sources/toolformer-schick-2023.md
  - sources/react-yao-2022.md
  - sources/generative-agents-park-2023.md
  - concepts/agent-cost-routing-model-orchestra.md
  - concepts/conductor-orchestrator.md
  - sources/controlled-study-of-multi-agent-debate-in-logical-reasoning.md
maturity: draft
created: 2026-05-13
updated: 2026-05-16
---

## Relations

- `@sources/tradingagents.md` — primary literature source: TradingAgents multi-LLM framework
- `@sources/multi-wiki-tool-eval-36url-wiki-ingestion-2026-05-24.md` — K63 TradingAgents-CN fork eval
- `@entities/tools/tradingagents-cn.md` — Chinese implementation fork (~27k★, CONDITIONAL-GO)
- `@concepts/agent-cost-routing-model-orchestra.md` — adjacent: multi-model cost-routing pattern
- `@concepts/conductor-orchestrator.md` — Cemini's own orchestrator pattern that hosts multi-agent flows
- `@sources/controlled-study-of-multi-agent-debate-in-logical-reasoning.md` — controlled study of the Debater role: debate gains are bounded by the strongest reasoner; homogeneous agent pools risk echo-chamber consensus

## Raw Concept

What prompted this page: tradingagents source flagged a gap for a hub on the multi-agent trading topic. Worth a concept page given the Cemini orchestrator pattern uses related primitives (Planner / Generator / Evaluator trinity).

## Narrative

Multi-agent trading frameworks split a trading decision across specialized LLM roles instead of stuffing everything into a single prompt. Common roles:

- **Analyst** — produces a directional view from a slice of evidence (fundamentals, technicals, news)
- **Debater** — challenges the analyst's view to surface failure modes
- **Risk officer** — enforces risk-budget constraints before any commit
- **Trader** — translates the surviving conviction into a position size + entry/exit

The TradingAgents framework (see `@sources/tradingagents.md`) implements one version of this. The Anthropic Planner/Generator/Evaluator trinity (see `@entities/tools/anthropic-harness-design.md`) is a more general pattern that hosts the same idea.

**Cemini relevance**: high — this is precisely the orchestrator-architecture decision space. The cost-routing orchestra (`@concepts/agent-cost-routing-model-orchestra.md`) layers on top: pick which role gets which model tier.

**Open questions**:
- Where does debate stop adding value vs. just adding tokens?
- Risk officer as a hard veto vs. a soft penalty in the optimization objective?
- Replay-and-audit: how do you reconstruct the decision chain three months later when you need to explain a loss?

This is a stub.
