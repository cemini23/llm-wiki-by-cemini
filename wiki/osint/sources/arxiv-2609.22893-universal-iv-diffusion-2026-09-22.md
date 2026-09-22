---
title: "Universal Diffusion Models for Implied Volatility Surfaces"
type: source
tags: [arxiv, source, k269, vol]
keywords: [k269, IVS, diffusion, VolGAN]
related:
  - concepts/k269-vol-quant-wave.md
maturity: draft
created: 2026-09-22
updated: 2026-09-22
read_status: skimmed
---

## Relations

- @concepts/k269-vol-quant-wave.md

## Raw Concept

| Paper | arXiv:2609.22893 |
| File | `arxiv-2609.22893-universal-diffusion-models-for-implied-volatilit.pdf` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2609.22893-universal-diffusion-models-for-implied-volatilit.pdf` |
| Retrieved | 2026-09-22 |
| Dual-ID | **OSINT K269** |
| sha256 | `08e263fc8933b303ae64b5cf7c3ea2576c2c36d0a6ebed4613a8ff88664368b8` |

## Narrative

Universal conditional diffusion jointly generates **next-day IVS increments + underlying returns**, trained on pooled data from **50 stocks**, tested on 50 in-sample + 50 OOS stocks. Beats VolGAN on arbitrage violations / risk prediction / PC explained variance. Shared dynamics across stocks. **Wiki FILE only. No xsp scp. 0 product Integrate GO.**
