---
title: Option IV concavity parameterization (XSP)
type: concept
tags: [concept, options, xsp, k198]
keywords: [implied volatility, W-shaped, local concavity, SPX]
related:
  - sources/arxiv-2607.24680-option-pricing-scheme.md
  - concepts/xsp-lane-trading-framework.md
  - concepts/macro-charts-regime-signals.md
maturity: draft
created: 2026-07-28
updated: 2026-07-28
---

## Relations

- @sources/arxiv-2607.24680-option-pricing-scheme.md
- @concepts/xsp-lane-trading-framework.md
- @concepts/macro-charts-regime-signals.md

## Raw Concept

Classical U-shaped smiles miss event-driven local concavity (W / inverse-U / S).

## Narrative

Bloomberg (Lin, 2607.24680): parsimonious risk-neutral params with localized IV-shape control, calibrated on ~250k SPX curves. For XSP killer: treat scheduled-event concavity as first-class; do not force classical smile assumptions into Lane A overnight exits or Lane B LEAPS hedges without checking tenor/event calendar.
