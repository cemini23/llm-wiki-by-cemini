---
title: "deepeval — LLM Evaluation Framework (Confident AI)"
type: entity
tags: [dev-tooling, llm-evaluation, testing, ragas, langgraph, apache, adopted-tier]
keywords: [deepeval, llm-unit-testing, ragas-metrics, answer-relevancy, contextual-precision, vibe-coder, langgraph]
related:
  - sources/multi-wiki-tool-evaluation-v3.md
  - concepts/counterfactual-prompting-baselines.md
maturity: draft
created: 2026-05-14
updated: 2026-05-14
---

## Relations

- @sources/multi-wiki-tool-evaluation-v3.md — v3 batch eval: Adopt tier, OSINT wiki primary fit
- @concepts/counterfactual-prompting-baselines.md — complementary evaluation methodology; deepeval provides the metrics infrastructure, counterfactual-baselines provides the null-distribution framework

## Raw Concept

From the Cemini Multi-Wiki Link Evaluation Report v3 (May 2026). Apache-2.0 licensed, v4.0, 15.4k stars. Pure Python framework for LLM unit testing with RAGAS, Answer Relevancy, and Contextual Precision metrics.

## Narrative

DeepEval provides quantitative infrastructure to audit the OSINT wiki's kb-server response quality. Key capabilities: RAGAS metrics via `@observe()` tracing decorator, LangGraph agent evaluation, and the Vibe-Coder skill that enables Claude Code to auto-generate test suites around failing metrics.

**Tier: Adopt** — Apache-2.0, 100% Python, explicit LangGraph support. Directly integrates into /opt/cemini for evaluating kb-server response faithfulness. Cross-wiki routing: deploy DAG-based LLM-as-a-judge metrics against NLP sentiment layer in Cemini financial; evaluate Toxicity/Bias metrics in Cybersec wiki; adopt Vibe-Coder in CCC wiki for automated regression test generation.

**NEEDS VERIFICATION:** Performance degradation under high-throughput, low-latency financial prediction queries.
