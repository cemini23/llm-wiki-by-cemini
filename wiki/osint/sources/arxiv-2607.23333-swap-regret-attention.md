---
title: "Training with (Swap) Regret Loss in Single-Layer Attention (arXiv 2607.23333)"
type: source
tags: [source, arxiv, poker, game-theory, k198]
keywords: [swap regret, fictitious play, self-attention, correlated equilibrium]
related:
  - concepts/swap-regret-attention-fictitious-play.md
  - concepts/code-as-agent-harness.md
maturity: draft
read_status: read
created: 2026-07-28
updated: 2026-07-28
clusters: [k198-ingest]
---

## Relations

- @concepts/swap-regret-attention-fictitious-play.md
- @concepts/code-as-agent-harness.md

## Raw Concept

| Field | Value |
|-------|-------|
| **Filename** | `arxiv-2607.23333-training-with-swap-regret-loss-in-a-single-layer.pdf` |
| **sha256** | `23674f0c36d805ddd553936a206ea9d1515faf0e01c0e73a6b10e3b19243598e` |
| **arXiv** | [2607.23333](https://arxiv.org/abs/2607.23333) |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2607.23333-training-with-swap-regret-loss-in-a-single-layer.pdf` |

## Narrative

Park & Ozdaglar (MIT): single-layer self-attention trained with **regret loss** admits stationary points whose forward pass matches **smoothed fictitious play**; new **swap-regret loss** realizes Blum–Mansour-style updates (heads = external-regret FP). External-regret → CCE; swap-regret → CE.

**Steal (poker):** differentiable regret objectives for HU decide() / MAFP lanes — equilibrium-seeking updates without supervised algorithm traces. Theory paper; no code drop.

## Snippets

> "regret-trained attention can realize differentiable mechanisms whose deployment induces equilibrium behavior in games"
