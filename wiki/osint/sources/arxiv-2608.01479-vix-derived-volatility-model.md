---
title: "arXiv 2608.01479 — VIX-Derived Volatility Model (VIX-first SPX–VIX)"
type: source
tags: [arxiv, vix, spx, volatility, xsp, k222]
keywords: [VDV, VIX futures, joint calibration, Utrecht, Rabobank]
related:
  - sources/arxiv-2608.01217-lsv-calibration-neural-operator.md
  - concepts/vix-first-joint-spx-vix-calibration.md
  - concepts/xsp-lane-trading-framework.md
maturity: draft
created: 2026-08-04
updated: 2026-08-04
read_status: deep-read
---

## Relations

- @sources/arxiv-2608.01217-lsv-calibration-neural-operator.md
- @concepts/vix-first-joint-spx-vix-calibration.md
- @concepts/xsp-lane-trading-framework.md

## Raw Concept

| Field | Value |
|-------|--------|
| Title | The VIX-Derived Volatility Model: A VIX-first Joint SPX-VIX Framework |
| Authors | Nicola F. Zaugg, Lech A. Grzelak |
| arXiv | 2608.01479 |
| sha256 | `e55fb5dd28d338432de0de4fdc68e0d47e2be8b4766f7b4fccb196664894cfc8` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2608.01479-the-vix-derived-volatility-model-a-vix-first-joi.pdf` |
| retrieved | 2026-08-04 |
| read_status | deep-read (abstract + intro) |

## Narrative

**VDV** calibrates explicit VIX dynamics to VIX futures/options first, then derives a coupling so SPX stochastic volatility is a latent process consistent with that VIX — SPX options can be fit without rewriting the VIX side. Framed as more interpretable than global black-box joint optimizers. Numerical experiment: local-vol + mean-reverting VIX fits VIX futures, VIX options, and SPX options together.

**Cemini routing:** Priority for **xsp** (VIX / index-options hedge monitor awareness). GuruWatcher may already poll VIX levels — this is model research, not a new Discord watch.

## Snippets

> Relative to existing joint-calibration approaches based on global optimization or highly flexible black-box dynamics, the method offers an interpretable and tractable decomposition of the joint problem by separating the calibration of the VIX from the calibration of the SPX. [Source: arXiv 2608.01479]
