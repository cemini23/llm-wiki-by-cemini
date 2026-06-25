---
title: "False Summit and Silent Drift — LLM multiphysics failure taxonomy (arXiv 2606.21841)"
type: source
tags: [source, arxiv, llm-verification, simulation, failure-taxonomy, k129]
keywords: [2606.21841, false summit, silent drift, MOOSE, multiphysics, stage-gated workflow]
related:
  - concepts/high-signal-paper-patterns.md
  - sources/arxiv-probabilistic-agent-verification-2606.20510-2026-06-21.md
  - sources/arxiv-harnessfix-trace-repair-2606.06324-2026-06-16.md
  - concepts/devfun-poker-agent-challenge-2026.md
maturity: draft
read_status: read
created: 2026-06-25
updated: 2026-06-25
clusters: [llm-agents]
---

## Relations

- @sources/arxiv-probabilistic-agent-verification-2606.20510-2026-06-21.md — agent verification cluster (K128)
- @concepts/devfun-poker-agent-challenge-2026.md — stage-gated validation steal for game-dev / poker harness

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | False Summit and Silent Drift: A Failure Taxonomy and Efficiency Analysis of LLM-Assisted Multiphysics Simulation in an Open-Source Framework |
| **Authors** | Chi-Chun Chiang, Shih-Ming He |
| **arXiv** | 2606.21841v1 (Jun 2026) |
| **sha256** | `97c441405bef45df3f7be4fc528ea814b79ed42fba96b2610a84d927c86dd9b3` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2606.21841-2606-21841v1-false-summit-and-silent-drift-a-fai.pdf` |
| **Retrieved** | 2026-06-25 (inbox) |
| **Read status** | read (abstract + failure definitions) |

## Narrative

Case study: LLM-assisted **LPCVD graphene** model in open-source **MOOSE** multiphysics framework. Compares GPT vs Claude under direct prompt, staged dev without literature, and staged dev **with literature guidance**.

**Failure classes:**

| Term | Definition |
|------|------------|
| **False summit** | Simulation converges and looks plausible but implements **wrong physics** |
| **Silent drift** | Unverified assumptions propagate undetected across stages |

Examples: non-conservative species transport → spurious methane depletion; omitted self-limiting surface reaction → LLM rationalizes invalid growth [TENTATIVE — paper case details].

**Literature guidance:** cut prompt counts **91% (GPT)** and **64% (Claude)** on hardest stage [TENTATIVE].

**Deliverables:** eight-category failure taxonomy, model-specific oversight strategies, **stage-gated workflow** for hidden modeling errors.

**Cemini steal:** **False summit / silent drift** vocabulary for agentic game-dev + poker sim validation — maps to castle-sim playtest gates and poker harness regression checks.

## Snippets

> "We define a false summit as a simulation that converges and appears physically plausible while implementing incorrect physics." [Source: arXiv:2606.21841 abstract (retrieved 2026-06-25)]

> "Silent drift as the undetected propagation of unverified assumptions through successive development stages." [Source: arXiv:2606.21841 abstract (retrieved 2026-06-25)]

> "Literature guidance substantially reduced interaction burden … decreasing prompt counts by 91% for GPT and 64% for Claude." [Source: arXiv:2606.21841 abstract (retrieved 2026-06-25)]

## Dead Ends

- Multiphysics MOOSE ≠ Godot RTS — taxonomy transfer only; no MOOSE install on Cemini stack.
