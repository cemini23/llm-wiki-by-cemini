---
title: "When Agents Fail: Model or Harness —Who's to Blame?"
type: source
tags: [source, arxiv, harness-evaluation, agent-benchmarks]
related: []
maturity: draft
read_status: skimmed
created: 2026-10-27
updated: 2026-10-27
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | When Agents Fail: Model or Harness—Who's to Blame? |
| Authors | Shao Zhang, Hangfan Zhang, Yuanyuan Shi, Hao Li, Min-Le Su, Kangcong Li, Jingping Wang, Chunjiang Mu, Chen Zhang, Yang Chen, Bo Zhang, Shuyue Hu (Shanghai Artificial Intelligence Laboratory) |
| arXiv | 2610.32483 |
| File | `arxiv-2610.32483-when-agents-fail-model-or-harness-who-s-to-blame.pdf` |
| Retrieved | 2026-10-27 |
| URL | https://arxiv.org/abs/2610.32483 |
| Read status | skimmed (abstract + intro) |

## Narrative

The paper argues that an agent is a **model plus a harness**, so a benchmark score measures the pair, not the model. A good model in a poor harness scores badly. A weak model in a good harness can score well.

The authors build a framework with five complementary measures:

- **Valid Completion Rate (VCR)** — how reliably an agent finishes normally and returns an evaluable result, regardless of correctness.
- **Model–Harness Fit** — how well a given harness lets a given model complete tasks validly.
- **Cross-Model Fit** — a harness's overall suitability across all evaluated models.
- **Interaction Residuals** — pairing-specific execution strengths that a model-only or harness-only score misses.
- A fifth measure is introduced in the body of the paper.

Cross-model fit ranks OpenCode first at 87.5, then Pi CLI at 77.1, Codex CLI at 73.6, and Deep Agents at 64.2. Model–harness fit uses four models on four shared benchmarks: SWE-bench-45, Terminal-Bench 2, VitaBench, and LOCA-Bench. The cross-model study uses three models on six benchmarks.

The paper reports that greater token use does not necessarily correspond to better outcomes. Relative token load moves independently of win rate.

**Why it matters.** The result gives a vocabulary for the recurring question in this workspace: when an agent fails, is the model or the harness at fault? The VCR measure is the useful one for a wiki or coding workflow — a harness that produces non-evaluable results hides model quality entirely.

All numbers here come from one paper and are reported as the paper states them. None are independently reproduced.

## Snippets

> "LLM agents combine models with execution harnesses, so agentic benchmark performance reflects their joint behavior. We argue that harnesses should therefore be evaluated through their interactions with underlying models." [Source: `arxiv-2610.32483-when-agents-fail-model-or-harness-who-s-to-blame.pdf` p.1 (arXiv 2610.32483), retrieved 2026-10-27]
