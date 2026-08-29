---
title: "JIT-Agent — just-in-time harness evolution (arXiv 2608.25593)"
type: source
tags: [arxiv, harness, ccc, k250]
keywords: [JIT-Agent, harness-intelligence, HarnessFactory, Evo-GDPO]
related:
  - concepts/k250-harness-intelligence-wave.md
  - entities/tools/jit-agent.md
  - sources/arxiv-2608.27311-verify-smarter-harness-evolution-2026-08-28.md
  - sources/source-harness-final-anonymous-2026-08-29.md
maturity: draft
created: 2026-08-29
updated: 2026-08-29
read_status: read
---

## Relations

- @sources/source-harness-final-anonymous-2026-08-29.md — anonymous harness note

- @concepts/k250-harness-intelligence-wave.md — K250 harness cluster
- @entities/tools/jit-agent.md — bingreeky/JIT REFERENCE
- @sources/arxiv-2608.27311-verify-smarter-harness-evolution-2026-08-28.md — HarnessLens K248 sibling

## Raw Concept

| Field | Value |
|-------|--------|
| Paper | arXiv:2608.25593, "JIT-Agent: Scaling Harness Intelligence via Just-in-Time Harness Evolution" |
| Authors | LV-NUS Lab et al. |
| Repo | https://github.com/bingreeky/JIT |
| File | `2608.25593v1.pdf` |
| Retrieved | 2026-08-29 |

## Narrative

JIT-Agent formalizes the agent harness as a composable four-module artifact (memory, planning, action, capability orchestration) and trains a **harness intelligence model** to synthesize task-specific harnesses at inference time. Three training stages: **customize** (task adaptivity), **repair** (executable recovery), **evolve** (Evo-GDPO archive distillation).

Reported: DeepSeek-V4-Flash + JIT beats GPT-5.6 on DeepSearchQA (+9.1) and OdysseyBench (+4.3); GLM-5.2 gains up to +20.2 pts; JIT harnesses competitive with OpenCode/Claude Code. Establishes harness intelligence as trainable axis **orthogonal to model scaling**. Runtime **`wont_wire`** — do not PATH-swap `/route`.

## Snippets

> "Agent capability is not determined by the model alone. The agent harness … can dominate the contribution of the underlying foundation model." [Source: arxiv 2608.25593 abstract]
