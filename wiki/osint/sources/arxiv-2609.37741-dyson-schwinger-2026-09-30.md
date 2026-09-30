---
title: "Dyson-Schwinger effective-action methods for rough volatility (2609.37741)"
type: source
tags: [source, k276, quant, volatility, rough-vol]
keywords: [k276, effective-action, rough-bergomi, vega, FILE]
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

| File | `arxiv-2609.37741-dyson-schwinger-effective-action-methods-for-rou.pdf` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2609.37741-dyson-schwinger-effective-action-methods-for-rou.pdf` |
| Archive | egress-fi 2026-09-30 |
| Retrieved | 2026-09-30 |
| Dual-ID | **OSINT K276** |
| sha256 | `3a8b8059983ebd3bf27d88536a3cb46ff95cd4f5b4d0b31052232329092c1b89` |
| arXiv | 2609.37741 |
| Author | Frederic Pauquay (DRW, Global Quantitative Modelling and Analytics) |

## Narrative

The paper organizes stochastic-volatility pricing with the two-particle-irreducible effective action from quantum field theory. The joint law of the state variables is approximated by a self-consistent Gaussian. The method is non-perturbative, so it stays accurate beyond the small-vol-of-vol regime where asymptotic expansions fail.

The authors match the Hartree one-loop truncation against PDE and quasi-Monte-Carlo references. Reported errors: exp-OU 0.1 to 0.2 basis points; SABR grid-mean 7.4 basis points; rough Bergomi 1 to 3 basis points, with a wing check at about 14; rough SABR about 17; rough Heston 1 to 5.

One number is useful for our own desk notes. Bucketed vega in one contraction matches bump-and-revalue to machine precision (RMSE about 1e-12) at about 70 to 80 times lower cost. That is a vega-speed claim, not a signal.

The authors admit that every accuracy result is model-to-model. They report no live-market calibration. There are no convergence proofs for the Hartree closure. The speed advantage is narrow. One near-freezing corner is not reachable to one basis point.

No code URL found. A technical supplement is an ancillary file on the arXiv page. No clone. Method note only. Do not wire it.
