---
title: CEV resistance/support optimal prediction (aspiration levels)
type: concept
tags: [concept, options, xsp, optimal-stopping, k161]
keywords: [CEV, aspiration level, resistance, support, free boundary, stopping band]
related:
  - sources/arxiv-cev-resistance-support-prediction-2607.08531-2026-07-13.md
  - concepts/xsp-lane-trading-framework.md
  - sources/sabr-geometry-aware-correction-2605.06604.md
maturity: draft
created: 2026-07-13
updated: 2026-07-13
---

## Relations

- @sources/arxiv-cev-resistance-support-prediction-2607.08531-2026-07-13.md — primary
- @concepts/xsp-lane-trading-framework.md — Lane A overnight / Lane B LEAPS levels

## Raw Concept

Resistance and support as **hidden aspiration levels**; under CEV dynamics the optimal trading region is a **band** (positive drift) or single boundary (negative drift), with elasticity shifting band geometry vs GBM.

## Narrative

**XSP operator mapping:**

1. Do not treat static pivot lines as GBM-optimal when vol is level-dependent.
2. Positive-drift regimes → expect **two-sided** continuation outside an interior stopping band.
3. Elasticity beta sensitivity → widen/narrow watch bands when index level moves into high/low vol-of-vol regimes.
4. Paper is math existence/characterization — use as **mental model**, not plug-in formula on Robinhood.

## Snippets

- Positive drift → stopping band; negative drift → one boundary [Source: 2607.08531]
