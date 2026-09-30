---
title: "When hedging changes the payoff: replication with price impact (2609.36257)"
type: source
tags: [source, k276, quant, options, hedging, market-impact]
keywords: [k276, price-impact, replication, effective-strike, FILE]
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

| File | `arxiv-2609.36257-when-hedging-changes-the-payoff-option-replicati.pdf` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2609.36257-when-hedging-changes-the-payoff-option-replicati.pdf` |
| Archive | egress-fi 2026-09-30 |
| Retrieved | 2026-09-30 |
| Dual-ID | **OSINT K276** |
| sha256 | `ba3618e947cc1f56d8088d2217ad9dbb5c018216cd772a92ed4a936eb8e5534c` |
| arXiv | 2609.36257 |
| Authors | David Itkin (LSE), Leandro Sanchez-Betancourt (Oxford / Oxford-Man) |

## Narrative

When the hedge trade moves the price, the hedge changes the payoff it was meant to copy. The paper calls this a moving-target problem. Strategy, settlement value, and price must be solved together.

The authors separate maturity from settlement. The payoff is fixed at maturity. The payoff is paid at settlement. A one-period binomial model reduces replication to one scalar fixed-point equation.

One result is a clean number. Price impact shifts the effective strike to K-tilde = K minus lambda times N. The replication cost always exceeds the frictionless cost. The premium is bounded by 0.5 times lambda times L_V squared times (1 minus e to the minus rT).

The authors give a sharp uniqueness condition: L_V times L_I is less than S_T(u) minus S_T(d). Per-contract quantities depend on N and lambda only through the product N times lambda in the midpoint-cost regime.

The authors admit the numerical examples use constant volatility. They prove well-posedness only in the midpoint regime. The other regime is heuristic.

One simulation detail is worth keeping. Of 1,000 paths, 9 had S_T below K below the replicating portfolio value. The hedger's own trading brought a worthless option into the money. That is the mechanism in one line.

No code URL found. No clone. Method note only. Do not wire it.
