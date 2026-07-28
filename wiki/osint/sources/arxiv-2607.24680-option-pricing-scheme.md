---
title: "One Other Option Pricing Scheme (arXiv 2607.24680)"
type: source
tags: [source, arxiv, options, xsp, k198]
keywords: [implied volatility, concavity, W-shaped, risk-neutral, SPX]
related:
  - concepts/option-iv-concavity-parameterization.md
  - concepts/xsp-lane-trading-framework.md
maturity: draft
read_status: read
created: 2026-07-28
updated: 2026-07-28
clusters: [k198-ingest]
---

## Relations

- @concepts/option-iv-concavity-parameterization.md
- @concepts/xsp-lane-trading-framework.md

## Raw Concept

| Field | Value |
|-------|-------|
| **Filename** | `arxiv-2607.24680-one-other-option-pricing-scheme.pdf` |
| **sha256** | `7d612141b14d92ae26477de889f50f272dc8402d8e70c832cd8c969fdc4af46c` |
| **arXiv** | [2607.24680](https://arxiv.org/abs/2607.24680) |
| **Author** | Jimin Lin (Bloomberg) |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2607.24680-one-other-option-pricing-scheme.pdf` |

## Narrative

Parsimonious risk-neutral parameterization with localized control of IV shape including **local concavity** (W / inverse-U / S). Calibrated on ~250k SPX curves over 2y; stable tenor parameters → term-structure interpolation without static arb.

**Steal (XSP):** event-day concave IV shapes are first-class — Lane A/B should not assume classical U-smile; watch for scheduled-event W-shapes. No code this cycle.

## Snippets

> "captures a wide variety of shapes, including those with local concavity"
