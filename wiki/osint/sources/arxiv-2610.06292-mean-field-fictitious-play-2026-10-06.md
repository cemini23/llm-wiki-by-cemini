---
title: "Learning controls in mean field games: fictitious play and gradient descent (arXiv 2610.06292)"
type: source
tags: [source, k283, arxiv, math, control, game-theory]
keywords: [mean-field-games, fictitious-play, gradient-descent, potential-games, convergence, fbsde]
related:
  - concepts/k283-arxiv-wave.md
maturity: draft
created: 2026-10-06
updated: 2026-10-06
read_status: skimmed
---

## Relations

- @concepts/k283-arxiv-wave.md

## Raw Concept

| Title | Learning controls in mean field games: the fictitious play and related gradient descent |
| Author | Meynard Charles (ERC ELISA) |
| Type | arXiv preprint (math.OC) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2610.06292-learning-controls-in-mean-field-games-the-fictit.pdf` |
| Retrieved | 2026-10-06 |
| arXiv | 2610.06292v1 |
| read-status | skimmed |

## Narrative

A convergence proof for learning in **potential mean field games (MFGs)** — including MFGs of controls and, for the fictitious-play rule, common noise.

**Fictitious play on controls.** The update acts on players' controls directly:

    ᾱ^{n+1} = (1 − η^n) ᾱ^n + η^n α^n

where α^n is the best response to the current belief. With steps Ση^n = ∞ and Σ(η^n)² < ∞, the potential decreases:

    J(ᾱ^{n+1}) − J(ᾱ^n) ≤ (−c_L η^n + C_Lip(1+T)(η^n)²) ‖α^n − ᾱ^n‖²_T

Corollary 2.9 gives ‖α^n − ᾱ^n‖_T → 0. Theorem 2.13 proves the laws Q^n are precompact and every limit point is a measure-valued MFG equilibrium (with common noise). Theorem 2.16 gives strong convergence to the unique mean-field control (MFC) optimum under coupling convexity.

**Gradient descent** in MFC uses ∇J(α)_t = ∇_α L(X^α_t, α_t, ·) − U^α_t, where U^α solves a forward-backward SDE. Theorem 3.6: limit points solve the MFG (σ > 0).

**Relevance is weak and indirect.** MFGs model trade crowding (Cardaliaguet–Lehalle 2018), so the result is adjacent to market-impact learning — but there is **no options, prediction-market, LLM-agent, security, or game-dev hook.** The value is the *learning-in-games convergence* technique. No license stated; no code. Funded by ERC grant 101054746.

## Snippets

> "Under Ση^n = ∞ and Σ(η^n)² < ∞, the sequence of laws is precompact and every limit point is a measure-valued MFG equilibrium." [Source: arxiv-2610.06292-learning-controls-in-mean-field-games-the-fictit.pdf]
