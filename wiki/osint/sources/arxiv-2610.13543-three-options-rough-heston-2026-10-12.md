---
title: "Three options are roughly enough: variance-optimal hedging in rough Heston (arXiv 2610.13543)"
type: source
tags: [source, k289, arxiv, options, volatility, hedging, quant, rough-vol]
keywords: [rough-heston, variance-optimal-hedging, semi-static, galtchouk-kunita-watanabe, variance-swap, hurst, forward-variance]
related:
  - concepts/k289-arxiv-wave.md
  - concepts/xsp-vol-regime-gates.md
maturity: draft
created: 2026-10-12
updated: 2026-10-12
read_status: read
---

## Relations

- @concepts/k289-arxiv-wave.md
- @concepts/xsp-vol-regime-gates.md

## Raw Concept

| Title | Three Options Are Roughly Enough — Variance-Optimal Semi-Static Hedging in the Rough Heston Model |
| Authors | Paolo Di Tella, Martin Keller-Ressel, Beatrice Ongarato (TU Dresden) |
| Type | arXiv preprint (q-fin.MF) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2610.13543-three-options-are-roughly-enough-variance-optima.pdf` |
| Retrieved | 2026-10-12 |
| arXiv | 2610.13543v1 |
| read-status | read |

## Narrative

**The headline is in the title.** In the **rough Heston** model, semi-static variance-optimal hedging of a variance swap needs very few vanillas.

### Method

A **Markovian lift via the forward variance curve**; Fourier representations of claims; a **Laplace-transform characterisation of the log-price**; and optimal strategies from the **Galtchouk–Kunita–Watanabe decomposition**. Semi-explicit formulas for both the strategies and the **residual hedging error**. The paper also solves the **optimal claim-selection problem** — which vanillas to hold.

### The result

Under the standard parametrisation, adding **three static vanilla options reduces the hedging error by more than 95%** versus a purely dynamic hedge — and it holds across roughness regimes **H ∈ {0.1, 0.3, 0.5}**. **The choice of which options depends on the Hurst index.**

### Why it matters here

A **practical hedging number** for the vol lane: **three well-chosen vanillas, >95% of the error removed**, with a **Hurst-dependent strike choice**. It also gives the GKW decomposition as the machinery. **No trade, no scp.**

## Snippets

> "Adding three static vanilla options reduces the hedging error by >95% vs. a purely dynamic hedge, for all roughness regimes H ∈ {0.1, 0.3, 0.5}." [Source: arxiv-2610.13543-three-options-are-roughly-enough-variance-optima.pdf]

> "Option choice depends on the Hurst index." [Source: arxiv-2610.13543-three-options-are-roughly-enough-variance-optima.pdf]
