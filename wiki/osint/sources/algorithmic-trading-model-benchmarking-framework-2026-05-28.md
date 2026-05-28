---
title: Benchmarking Probabilistic Engines — Brier Score, Small-Sample Significance, Model Promotion
type: source
tags: [source, quant-validation, brier-score, model-promotion, walk-forward, k77]
keywords: [brier-score, brier-skill-score, murphy-decomposition, diebold-mariano, HLN, CPCV, PBO, ROPE]
related:
  - concepts/brier-score-model-promotion-framework.md
  - concepts/monte-carlo-permutation-test-mcpt.md
  - concepts/regime-conditioned-evaluation.md
  - concepts/lp-algorithm-live-promotion-gates.md
maturity: draft
created: 2026-05-28
updated: 2026-05-28
---

## Relations

- @concepts/brier-score-model-promotion-framework.md — synthesized framework
- @concepts/monte-carlo-permutation-test-mcpt.md — complementary permutation gate
- @concepts/regime-conditioned-evaluation.md — CPCV / regime splits
- @concepts/lp-algorithm-live-promotion-gates.md — LP promotion stack extension

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Benchmarking Probabilistic Engines in Algorithmic Trading |
| Author | Independent research (docx) |
| Type | docx |
| Location | `cemini-librarian:/opt/cemini-bulk/research/Algorithmic Trading Model Benchmarking Framework.docx` |
| Retrieved | 2026-05-28 |
| Read-status | deep-read |

## Narrative

Institutional six-stage promotion framework for **probabilistic** trading engines (binary event forecasts, PM fills, volatility breakouts):

1. **CPCV** with purge + embargo — no standard k-fold on autocorrelated labels
2. **Murphy/Yates decomposition** — resolution vs reliability (calibration) before comparing models
3. **Brier Skill Score** vs naive base rate — positive BSS required
4. **Small-sample frequentist** — HLN-corrected Diebold-Mariano + block bootstrap on BSS
5. **Bayesian ROPE** — posterior must beat incumbent *and* escape region of practical equivalence
6. **PBO / CSCV** — probability of backtest overfitting across full trial grid

Key Cemini hooks: brain v2 proxy outputs probabilities → evaluate with **Brier + calibration**, not accuracy @ fixed threshold; R7 walk-forward should report BSS and reliability bins, not only PnL pp.

## Snippets

> "A model with excellent resolution but catastrophic calibration will inevitably destroy capital due to over-leveraged Kelly sizing." [Source: Algorithmic Trading Model Benchmarking Framework.docx]

> "At 0.68, arbitrary accuracy thresholds destroy nuance; strictly proper scoring rules (Brier) evaluate beliefs without thresholding." [Source: Algorithmic Trading Model Benchmarking Framework.docx — paraphrase]
