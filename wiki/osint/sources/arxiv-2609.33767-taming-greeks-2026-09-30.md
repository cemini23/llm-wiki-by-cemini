---
title: "Taming the Greeks: option portfolios with inductive biases (2609.33767)"
type: source
tags: [source, k276, quant, options, hedging]
keywords: [k276, greeks, delta, inductive-bias, FILE]
related:
  - concepts/k276-vol-quant-wave.md
maturity: draft
created: 2026-09-30
updated: 2026-09-30
read_status: skimmed
---

## Relations

- @concepts/k276-vol-quant-wave.md

## Raw Concept

| File | `arxiv-2609.33767-taming-the-greeks-option-portfolios-with-inducti.pdf` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2609.33767-taming-the-greeks-option-portfolios-with-inducti.pdf` |
| Archive | egress-fi 2026-09-30 |
| Retrieved | 2026-09-30 |
| Dual-ID | **OSINT K276** |
| sha256 | `4514b9790ff467509a2bb8eb4c3e39e2492a22e8ad14661d1f2f6901fd65ed79` |
| arXiv | 2609.33767 |
| Authors | Wee Ling Tan, Stephen Roberts, Stefan Zohren (Oxford / Oxford-Man) |

## Narrative

An LSTM maps option features to position weights. The training loss adds a penalty on the portfolio Greeks. The idea is to make the model hedge by construction, not by reward.

The authors test static delta-neutral at-the-money straddles. The penalty acts on first-order Delta. They test two penalty shapes: an exposure-normalized penalty and a Greek-ratio drift penalty.

The authors admit a failure mode. A naive Greek penalty just scales the position down. They call this regularization collapse and reformulate it as inefficient risk composition.

Data is OptionMetrics Ivy DB on Nasdaq-100 names, 2010 to 2023. The paper reports better out-of-sample risk-adjusted performance than an unregularized baseline, with lower realized directional exposure. No exact Sharpe or return figures appear in the main sections.

No code URL found. No clone. Method note only. Do not wire it.
