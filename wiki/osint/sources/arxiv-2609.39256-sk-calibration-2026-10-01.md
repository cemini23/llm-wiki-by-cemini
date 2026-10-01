---
title: "Stochastic Knothe-Rosenblatt: light-speed SLV calibration (2609.39256)"
type: source
tags: [source, k277, quant, volatility, calibration]
keywords: [k277, slv, sinkhorn, bass-martingale, FILE]
related:
  - concepts/k277-vol-quant-wave.md
maturity: draft
created: 2026-10-01
updated: 2026-10-01
read_status: skimmed
---

## Relations

- @concepts/k277-vol-quant-wave.md

## Raw Concept

| File | `arxiv-2609.39256-stochastic-knothe-rosenblatt-light-speed-calibra.pdf` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2609.39256-stochastic-knothe-rosenblatt-light-speed-calibra.pdf` |
| Archive | egress-fi 2026-10-01 |
| Retrieved | 2026-10-01 |
| Dual-ID | **OSINT K277** |
| sha256 | `c36ed23a857d3d0b9a3fef7a840c276cf11b0a4ea3a8efd3c73cde869353dee1` |
| arXiv | 2609.39256 |
| Authors | M. Beiglbock, M. Hasenbichler, G. Pammer |

## Narrative

A calibration overlay for stochastic local volatility models. The construction builds a martingale that matches all prescribed marginal laws exactly, while staying as close as possible to a chosen reference model. As the maturity grid refines, it converges to the stochastic local volatility model of that reference.

The method defines R-Bass martingales: the Brownian reference of the Bass martingale is replaced by a general Markovian reference. Each bridge step is solved by a Martingale Sinkhorn fixed point.

The headline number is speed. On a reverse cliquet against SPX targets, the method took **0.273 seconds** against **25.778 seconds** for a standard Heston stochastic-local-volatility calibration, with close prices: 122.000 against 122.139. Standalone calibration times were 0.0801s for Bass local volatility, 0.1626s for the Heston variant, 0.1952s for the 3/2 variant, and 0.9204s for one-factor Bergomi.

Convergence is stated as strong order one half under the paper's assumptions.

The authors admit the link to SLV is presented as a heuristic developed formally in one section, that convergence holds only under regularity assumptions, and that the multi-asset extension is scalar and coordinate-wise.

This is a method note from three mathematicians. It is not a signal and not a trade. No code URL found. No clone. FILE only.
