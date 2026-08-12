---
title: "When the Fed Speaks — Dynamics and Forecasts of the Volatility Surface"
type: source
tags: [arxiv, k233, xsp, options, vol-surface, fomc]
keywords: [2608.10693, implied-volatility, iv-surface, fomc, pre-announcement-effect, convlstm, short-dated-otm]
related:
  - concepts/xsp-lane-trading-framework.md
  - concepts/fomc-iv-surface-dynamics.md
  - concepts/xsp-vol-regime-gates.md
maturity: draft
created: 2026-08-12
updated: 2026-08-12
read_status: skimmed
---

## Relations

- @concepts/fomc-iv-surface-dynamics.md
- @concepts/xsp-lane-trading-framework.md
- @briefs/xsp-k233-fed-speaks-vol-surface.md

## Raw Concept

| Field | Value |
|-------|--------|
| arXiv | 2608.10693 |
| sha256 | `2c13c2f7553d60232e3ab1dd9c4b9283f1530e6827e8eb01548a48e86a9f0142` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2608.10693-when-the-fed-speaks-dynamics-and-forecasts-of-th.pdf` |
| retrieved | 2026-08-12 |
| authors | Łukasz Adamski, Robert Ślepaczuk (Univ. of Warsaw, QFRG) |

## Narrative

Empirical + ML study of how the **implied volatility (IV) surface** evolves around scheduled **FOMC meetings**. Two questions: (1) does IV rise before the announcement, and is the effect stronger for short-dated OTM options in high-vol regimes; (2) can an ML framework beat the random-walk benchmark at forecasting this pre-announcement elevation.

Method: a **convolutional 2D LSTM (ConvLSTM)** applied directly to the IV surface without PCA-style dimensionality reduction — a relatively early attempt to model the surface as a spatio-temporal signal. A FOMC-meeting-date feature augments the model.

Findings: pre-announcement IV elevation is real and strongest for **short-dated OTM** options in **high-volatility regimes**; the ML edge is real but bounded by the noisy surface — however, ML can still forecast the IV surface during abnormal (announcement) days.

Relevance to XSP lane: the pre-FOMC short-dated OTM IV bid-up is directly exploitable in the XSP/killer-bot long-call lanes — timing long-call entry ahead of scheduled meetings into elevated short-dated vol, and the regime-dependent strength (high-vol regime amplifies it) feeds the vol-regime gates.

[Source: arXiv:2608.10693]
