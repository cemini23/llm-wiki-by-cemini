---
title: "arXiv 2608.01217 — Amortizing the Calibration Triple (LSV neural operator)"
type: source
tags: [arxiv, volatility, lsv, xsp, k222]
keywords: [DeepONet, FNO, Dupire, local-stochastic volatility, Barclays]
related:
  - sources/arxiv-2608.01479-vix-derived-volatility-model.md
  - concepts/vix-first-joint-spx-vix-calibration.md
  - concepts/xsp-lane-trading-framework.md
maturity: draft
created: 2026-08-04
updated: 2026-08-04
read_status: deep-read
---

## Relations

- @sources/arxiv-2608.01479-vix-derived-volatility-model.md — companion VIX-first joint calibration
- @concepts/vix-first-joint-spx-vix-calibration.md
- @concepts/xsp-lane-trading-framework.md — Lane B vol/regime awareness (wiki + xsp brief; not auto-trade)

## Raw Concept

| Field | Value |
|-------|--------|
| Title | Amortizing the Calibration Triple: A Projection-Consistent Neural Operator for Local-Stochastic Volatility |
| Authors | Xiaozhen Wang, Anaïs Després, Martin Dureau, Francois Buet-Golfouse (Barclays / Dauphine / Évry) |
| arXiv | 2608.01217 |
| Type | PDF |
| sha256 | `d837849c37c0621e1817ec635b67eba21ba0fa7777cf539ce6d21e3a7c92eb91` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2608.01217-amortizing-the-calibration-triple-a-projection-c.pdf` |
| retrieved | 2026-08-04 |
| read_status | deep-read (abstract + intro) |

## Narrative

LSV calibration normally chains quote fit → Dupire local vol → leverage via a slow McKean–Vlasov / particle fixed point. This paper trains a **projection-consistent neural operator** (DeepONet / FNO) that jointly returns an arbitrage-admissible IV surface, Dupire local vol, LSV leverage, and the Gyöngy projection moment from finite quotes + an SV backbone. Synthetic tests claim forward-start/cliquet error within ~0.1–0.2 pp of a particle method while cutting calibration latency **98.5 → 0.6 ms**; local-vol RMSE −36%, leverage RMSE −7–16% vs baselines.

**Cemini routing:** wiki + **xsp** awareness for offline vol-surface / LEAPS hedge research — do **not** auto-scp into live Lane A exits without operator review. No Phase-0 code clone (paper-only).

## Snippets

> These results support amortizing the LSV fixed point: the expensive solve moves offline, while online calibration reduces to a single projection-consistent operator evaluation. [Source: arXiv 2608.01217]
