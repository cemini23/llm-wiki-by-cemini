---
title: "Finance-informed operator learning for option pricing (2609.33213)"
type: source
tags: [source, k276, quant, options, operator-learning]
keywords: [k276, deeponet, local-volatility, no-arbitrage, FILE]
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

| File | `arxiv-2609.33213-finance-informed-operator-learning-for-option-pr.pdf` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2609.33213-finance-informed-operator-learning-for-option-pr.pdf` |
| Archive | egress-fi 2026-09-30 |
| Retrieved | 2026-09-30 |
| Dual-ID | **OSINT K276** |
| sha256 | `33c29e2db6bed0f3b96b75dd6f5feca1520b6e2b95d4fea943400fcfa79c2c36` |
| arXiv | 2609.33213 |
| Authors | Jiarui Feng, Bingyang Hu, Jiang Yu, Changhong Mou, Yeyu Zhang |

## Narrative

The paper prices European options under local volatility with a DeepONet. The authors split the solution into two parts. A closed-form Black-Scholes carrier holds the near-expiry curvature. A learned correction covers the residual. A smooth monotone layer keeps the price inside the no-arbitrage interval.

The paper reports a global relative price error of 0.965e-3. A plain DeepONet gets 5.99e-3. A physics-informed DeepONet gets 7.24e-3. Delta p95 drops from 0.152 to 0.0245.

The authors admit limits. The test uses one low-dimensional coefficient family, fixed sensors, and one horizon. Out-of-family extrapolation is unresolved. On Nasdaq-100 quotes the frozen model stays accurate but does not beat a constant-volatility Black-Scholes reference. The quantum circuit part is classical and ideal. No hardware speedup is measured.

No code URL found. No clone. This is a method note only. Do not wire it.
