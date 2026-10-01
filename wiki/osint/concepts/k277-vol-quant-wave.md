---
title: K277 Vol Quant Wave (Oct 2026)
type: concept
tags: [quant, volatility, k277]
keywords: [k277, slv, sinkhorn, calibration, no-trade]
related:
  - concepts/k276-vol-quant-wave.md
  - sources/arxiv-2609.39256-sk-calibration-2026-10-01.md
maturity: draft
created: 2026-10-01
updated: 2026-10-01
harness_verb: FILE
wire_status: policy_wired
---

## Relations

- @concepts/k276-vol-quant-wave.md
- @sources/arxiv-2609.39256-sk-calibration-2026-10-01.md

## Raw Concept

K277 cluster hub. Dual-ID **OSINT K277**. Prior @concepts/k276-vol-quant-wave.md.

## Narrative

One paper. A calibration speed result.

The construction builds a martingale that matches the prescribed marginals exactly while staying close to a chosen reference model, then shows it converges to that model's stochastic local volatility form as the maturity grid refines. Each step is a Martingale Sinkhorn fixed point.

The number worth keeping: **0.273 seconds against 25.778 seconds** for a standard stochastic-local-volatility calibration on the same target, with close prices (122.000 against 122.139). Standalone times ran 0.0801s to 0.9204s across four reference models.

The authors admit the link to stochastic local volatility is a heuristic developed formally in one section, that convergence needs regularity assumptions, and that the multi-asset case is scalar and coordinate-wise.

**Cemini posture:** FILE. This is a pricing-engine method note, not a signal. No trade. No sizing change. No clone. **0 product Integrate GO.**
