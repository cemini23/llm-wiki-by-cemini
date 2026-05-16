---
title: "Coordination as an Architectural Layer for LLM-Based Multi-Agent Systems (arXiv:2605.03310)"
type: source
tags: [source, arxiv, multi-agent, coordination, llm-orchestration, prediction-markets, k48]
keywords: [coordination-layer, multi-agent-failure-rate, brier-score, murphy-decomposition, polymarket-testbed, foresight-arena, nechepurenko]
related:
  - concepts/conductor-orchestrator.md
  - concepts/polymarket-microstructure-findings.md
maturity: validated
read_status: skimmed
created: 2026-05-15
updated: 2026-05-15
---

## Relations

- @concepts/conductor-orchestrator.md — treats coordination as a separable, configurable architectural layer — directly relevant to the conductor's multi-agent orchestration design
- @concepts/polymarket-microstructure-findings.md — the paper's empirical testbed is 100 Polymarket binary markets

## Raw Concept

- **Title**: Coordination as an Architectural Layer for LLM-Based Multi-Agent Systems
- **Authors**: Maksym Nechepurenko, Pavel Shuvalov
- **Type**: arXiv preprint — arXiv:2605.03310
- **Submitted**: 2026-05-05
- **Retrieved**: 2026-05-15 (Tier-2 arXiv sweep `@sweeps/2026-05-15.md`, Q1 #2)
- **Read status**: skimmed (abstract-level)

## Narrative

Argues that multi-agent LLM systems fail in production at **41–87%** rates mostly from *coordination defects*, not base-model capability — and that coordination should therefore be treated as a separate, configurable architectural layer rather than baked into agent logic or information access.

Method: holds everything constant (single LLM, fixed tools, output caps, prompts) and varies five coordination configurations, using a Murphy decomposition of the Brier score to separate calibration from discriminative power. Testbed: 100 Polymarket binary markets; production agents on "Foresight Arena". Three of five pre-specified predictions validated directionally; two configurations dominate the cost-quality Pareto frontier.

**Caveat**: explicitly framed as proof-of-concept methodology, not a generalizable cross-model claim. Single research group (Nechepurenko is the most prolific author in the 2026-05-15 sweep's prediction-markets cluster — see `@sweeps/2026-05-15.md` Q4) — treat as a methodology contribution, single-source.

**Why it matters here**: the conductor is a multi-agent orchestration layer; "coordination as a configurable layer" + the Brier/Murphy evaluation method are directly applicable design references.

## Snippets

> "Multi-agent LLM systems fail in production at rates between 41% and 87%, mostly due to coordination defects rather than base-model capability."
> — [Source: https://arxiv.org/abs/2605.03310 (retrieved 2026-05-15)]
