---
title: Optimal prediction of resistance and support under CEV (2607.08531)
type: source
tags: [source, arxiv, options, optimal-stopping, k161]
keywords: [CEV, resistance, support, aspiration level, optimal prediction, free boundary]
clusters: [k161-ingest, xsp]
related:
  - concepts/xsp-lane-trading-framework.md
  - concepts/cev-resistance-support-optimal-prediction.md
  - sources/sabr-geometry-aware-correction-2605.06604.md
maturity: validated
read_status: deep-read
created: 2026-07-13
updated: 2026-07-13
---

## Raw Concept

| Field | Value |
|-------|-------|
| **arXiv** | [2607.08531](https://arxiv.org/abs/2607.08531) |
| **sha256** | `b3e90a37566cb002…` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2607.08531-2607-08531v1-optimal-prediction-of-resistance-an.pdf` |
| **Author** | Ruibo Ma (University of Manchester) |

## Relations

- @concepts/cev-resistance-support-optimal-prediction.md — K161 concept
- @concepts/xsp-lane-trading-framework.md — Lane A/B level awareness
- Extends De Angelis–Peskir GBM aspiration-level framework to **CEV**

## Narrative

Asset price follows a **CEV** diffusion (elasticity beta > 0; beta = 0 recovers GBM). Optimal prediction minimizes expected distance to a hidden **aspiration level** ell (resistance/support as trader targets).

| Drift | Stopping region |
|-------|-----------------|
| Positive mu | **Band** between two time-dependent boundaries a(t), c(t) |
| Negative mu | Single increasing boundary |
| beta → 0 | Recovers GBM one-sided limit |

Boundaries characterized by nonlinear integral equations; elasticity beta materially shifts band width.

**XSP steal:** treat overnight swing / LEAPS hedge levels as aspiration-conditioned bands under level-dependent vol — not static GBM pivots. Operator brief → prod.

## Snippets

> "Under positive drift the stopping set is a band between two curves, and under negative drift a single boundary." [Source: arXiv:2607.08531 abstract]
