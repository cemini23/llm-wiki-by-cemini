---
title: "Threshold cascades of interacting diffusions on unimodular trees (arXiv 2608.15987)"
type: source
tags: [arxiv, networks, cascades, k241]
keywords: [threshold-cascade, unimodular-tree, Galton-Watson, Perron-Frobenius]
related:
  - sources/arxiv-2608.16171-rare-event-sampling-2026-08-18.md
  - concepts/osint4all-catalog.md
maturity: draft
created: 2026-08-18
updated: 2026-08-18
read_status: read
---

## Relations

- @sources/arxiv-2608.16171-rare-event-sampling-2026-08-18.md — complementary rare-event / cascade sampling
- @concepts/osint4all-catalog.md — network-cascade locators stay catalog rows, not stub farms

## Raw Concept

| Field | Value |
|-------|--------|
| Paper | arXiv:2608.15987, "Threshold cascades of interacting diffusions on unimodular random trees" |
| Authors | Achyut Kumar |
| Retrieved | 2026-08-18 |
| File | `arxiv-2608.15987-threshold-cascades-of-interacting-diffusions-on.pdf` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2608.15987-threshold-cascades-of-interacting-diffusions-on.pdf` |
| Type | math.PR working manuscript |
| Dual-ID | **OSINT K241**. Thin source + related rare-event paper; no new cascade-theory concept. |

## Narrative

Coupled Ornstein–Uhlenbeck diffusions with an absorbing failure state on graphs that converge locally weakly to a unimodular Galton–Watson tree. A single failure can cascade. Under a front-decoupling / saturated-coupling hypothesis (exact on the Bethe lattice), the failed cluster of the root converges to a finite-type Galton–Watson genealogical tree whose mean matrix \(M\) comes from a many-to-one formula.

**Concrete claim `[TENTATIVE]`:** criticality is exactly \(\rho(M)=1\) (annealed Perron root). At criticality, total progeny obeys \(P(|S|=n)\sim C n^{-3/2}\) (Otter–Dwass + local CLT). In the supercritical regime the failed-cluster boundary has Hausdorff dimension \(\log\rho(M)\). The quenched/annealed growth-rate gap is a chord–tangent inequality on a single convex annealed pressure \(\varphi(\beta)=\log\rho(M(\beta))\).

Wiki use: awareness for cascade / rare-event sampling; not a trading rule and not a stub farm of network pages.

## Snippets

> "criticality occurs exactly at ρ(M) = 1, where ρ(M) is the annealed Perron root" [Source: arxiv-2608.15987 abstract]

> "at criticality the total progeny obeys P(|S|=n)∼Cn^{−3/2} with the universal mean-field exponent" [Source: arxiv-2608.15987 abstract]
