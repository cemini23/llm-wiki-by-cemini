---
title: Agent-reactive (AR) bugs — model–harness interaction failures
type: concept
tags: [concept, agent-harness, reliability, k177, ccc]
keywords: [agent-reactive-bugs, AR-bugs, silent-failures, harness-guardrails, reproduction]
related:
  - sources/arxiv-2607.15684-agent-reactive-bugs-model-harness.md
  - concepts/code-as-agent-harness.md
maturity: draft
created: 2026-07-20
updated: 2026-07-20
---

## Relations

- @sources/arxiv-2607.15684-agent-reactive-bugs-model-harness.md — primary empirical study
- @concepts/code-as-agent-harness.md — parent harness model

## Raw Concept

AR bugs = defects that require a specific LLM response *and* a harness reaction; neither side alone explains the failure.

## Narrative

| Axis | Cemini steal |
|------|----------------|
| **Silent errors** | Prefer oracles that catch wrong tool routing / wrong submit without crash |
| **Reproduction** | Pin model outputs / fixtures; do not rely on live stochastic replay alone |
| **Fix locus** | Default to harness guardrails + clearer contracts; avoid "blame the model" stalls |
| **Poker Arena** | decide()/capability-tree regressions should include AR-class fixtures |
| **CCC / Cursor** | Agent loops (fork_context, subagent handoff) are known AR hotspots |

Maturity stays **draft** until Cemini has an internal AR fixture corpus.
