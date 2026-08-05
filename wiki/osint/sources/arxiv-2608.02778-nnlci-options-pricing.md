---
title: "arXiv 2608.02778 — NNLCI efficient options pricing"
type: source
tags: [arxiv, options, xsp, k223]
keywords: [NNLCI, Black-Scholes, Heston, barrier, multi-asset]
related:
  - concepts/xsp-lane-trading-framework.md
  - concepts/vix-first-joint-spx-vix-calibration.md
maturity: draft
created: 2026-08-05
updated: 2026-08-05
read_status: deep-read
---

## Relations

- @concepts/xsp-lane-trading-framework.md
- @concepts/vix-first-joint-spx-vix-calibration.md

## Raw Concept

| Field | Value |
|-------|--------|
| Title | Neural Networks with Local Converging Inputs for Efficient Options Pricing Models |
| Authors | Harris Cobb, Wenbo Hao, Yingjie Liu |
| arXiv | 2608.02778 |
| sha256 | `654aa3f6c6c4824bcb5e5e0b8423e5920b3503b131dda22bff2242215f55e4a6` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2608.02778-neural-networks-with-local-converging-inputs-for.pdf` |
| read_status | deep-read |

## Narrative

NNLCI locally corrects coarse+refined PDE mesh solutions with little high-fidelity training data. Demo: cash-or-nothing BS 1–3D; Heston down-and-out barrier. Claims ~4–12× RMSE cut on refined mesh with small param subsets. **xsp awareness only** — no live pricer wire; no Phase-0 code.
