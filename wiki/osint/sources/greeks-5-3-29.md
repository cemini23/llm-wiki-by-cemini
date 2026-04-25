---
title: TraderBench — How Robust Are AI Agents in Adversarial Capital Markets?
type: source
tags: [pdf, llm-agents, portfolio-strategy, quant-finance, benchmark, adversarial, ai-agents, robustness]
clusters: [llm-agents, portfolio-strategy, quant-finance]
related: []
maturity: validated
created: 2026-04-23
updated: 2026-04-23
---

## Relations

*(Cross-references will be added in Phase 2.)*

## Raw Concept

- **Original title**: TraderBench: How Robust Are AI Agents in Adversarial Capital Markets?
- **Author(s)**: Unspecified in metadata captured
- **Type**: PDF
- **Length**: 12p
- **Location**: research for cemini/greeks 5 3:29.pdf
- **Retrieved**: 2026-04-23
- **Read status**: read-skim (preview + title only)
- **Primary cluster**: llm-agents
- **All clusters**: llm-agents, portfolio-strategy, quant-finance

## Narrative

Benchmark paper introducing TraderBench. Problem statement (per preview): existing AI-agent-in-finance evaluation has two failure modes — (1) static benchmarks require costly expert annotation and miss dynamic decision-making; (2) LLM-based judges introduce uncontrolled variance on domain-specific tasks. TraderBench claims to address both, implying a dynamic, non-LLM-judge evaluation protocol.

Honest assessment: the two diagnosed problems are real and well-posed, which is a good sign. A dynamic benchmark that doesn't rely on LLM-judged scoring is the right design for trading agents, because trading decisions have natural ground-truth scoring (PnL, drawdown, Sharpe) that doesn't require an LLM to adjudicate. "Adversarial" in the title suggests the benchmark includes adversarial perturbations (e.g., information-manipulation, market-regime changes) — if true, that's a meaningful contribution. 12 pages is short but appropriate for a benchmark paper.

Relevance to Cemini: potentially high as an evaluation harness for the suite's agent-based strategies. If the benchmark is open-source-released, it's worth testing the Cemini strategies against it directly. At minimum, the adversarial perturbation catalog is a useful checklist for robustness testing.

## Key findings

- Diagnoses two failure modes in AI-agent-in-finance evaluation: static benchmarks, LLM-judge variance.
- Proposes TraderBench as a dynamic, non-LLM-judge evaluation protocol.
- "Adversarial" framing suggests adversarial perturbations are part of the test set.
- Benchmark paper, 12p scope — concise.

## Snippets

- **p.1 (abstract)** — "Evaluating AI agents in finance faces two key challenges: static benchmarks re- quire costly expert annotation yet miss the dynamic decision-making central to real-world trading, while LLM-based judges introduce uncontrolled variance on domain-specific tasks. We introduce TraderBench, a benchmark that addresses both issues." — Defines the problem and pitch.
