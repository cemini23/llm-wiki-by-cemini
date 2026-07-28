---
title: "Sentiment-Driven Stochastic Volatility (arXiv 2607.22254)"
type: source
tags: [source, arxiv, options, volatility, k196, xsp]
keywords: [stochastic volatility, CIR, Heston, market attention, Feynman-Kac]
related:
  - concepts/xsp-lane-trading-framework.md
  - concepts/macro-charts-regime-signals.md
maturity: draft
read_status: skimmed
created: 2026-07-27
updated: 2026-07-27
clusters: [k196-ingest]
---

## Relations

- @concepts/xsp-lane-trading-framework.md
- @concepts/macro-charts-regime-signals.md

## Raw Concept

| Field | Value |
|-------|-------|
| **Filename** | `arxiv-2607.22254-sentiment-driven-stochastic-volatility-an-observ.pdf` |
| **sha256** | `f7f50992556c6d5337f7916f02c503befccc044df5c8b19b90240cf0021bf44a` |
| **arXiv** | [2607.22254](https://arxiv.org/abs/2607.22254) |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2607.22254-sentiment-driven-stochastic-volatility-an-observ.pdf` |

## Narrative

Two-factor SV where CIR mean-reversion speed is an **observable** functional of a market-attention field (exact Feynman–Kac), nesting Heston. Closed-form vol forecasts; mean-field particle convergence; sims show vol/option pricing shifts after attention shocks.

**Steal (xsp):** Watch-only math — attention as observable vol driver is adjacent to regime dashboards; no Lane change without calibration evidence.

## Snippets

> "the mean-reversion speed of a Cox–Ingersoll–Ross variance process is an observable functional of a market attention field rather than a latent factor"
