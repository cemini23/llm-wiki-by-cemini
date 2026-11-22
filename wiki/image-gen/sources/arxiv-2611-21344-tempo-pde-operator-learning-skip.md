---
title: "TEMPO: regime-aware PDE operator learning (arXiv:2611.21344)"
type: source
related: []
updated: 2026-11-22
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | TEMPO: Regime-Aware Operator Learning with Locally Adapted POD Bases |
| Authors | Rodion Akinzhala, Alexander Terentyev, Alexey Golubev, Yury Maximov |
| Type | arXiv preprint, cs.LG |
| arXiv | 2611.21344v1, 16 Nov 2026 |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/image-gen/arxiv-2611.21344-tempo-regime-aware-operator-learning-with-locall.pdf` |
| URL | https://arxiv.org/abs/2611.21344 |
| Retrieved | 2026-11-22 |
| Pages | 31 |
| Read status | read |
| Domain fit | **Peripheral. SKIP.** Scientific-ML reduced-order modelling for PDEs. No image, video, diffusion, or LoRA content. |

## Narrative

### What it does

TEMPO learns the solution map of a parametric PDE from snapshots. A single global low-rank basis (POD) fails when snapshots span different solution shapes, from smooth diffusion to near-discontinuous shocks.

TEMPO splits the work in two phases:

1. **Offline.** Expectation-maximization (EM) recovers M latent regimes from unlabeled snapshots. It fits a dedicated POD or NeuralPOD basis to each regime.
2. **Online.** A gating network and M branch networks route new inputs to regimes. A KL penalty anchors routing to the offline partition.

An adaptive basis update monitors moment change in regime composition. It then chooses full retraining, incremental mode add/prune, or skip. The authors prove that per-regime rank-K bases never increase offline reconstruction error relative to one global rank-K basis (Proposition 1).

### Results

Six PDE benchmarks: Burgers' flow, Sod shock tubes, Coanda flow, Darcy flow, Navier–Stokes flow, and the heterogeneous Helmholtz equation. With 64 total POD modes, test error on Burgers' is 18.61% against 19.61% for global POD. TEMPO also gives lower error on Coanda and Helmholtz.

### Why it is skipped

The method is a mixture-of-experts reduced-order model for physics simulation. It has no diffusion transformer, no generative image model, and no adapter training. The regime-discovery idea is a clustering method and is not unique to this domain.

One transferable idea, held at TENTATIVE: a mixture of local bases beats one global basis when the data has qualitatively different regimes. This is the same intuition as mixture-of-experts layers. It does not change any image-gen workflow.

## Dead Ends

Not pursued. The paper is out of domain for this wiki.
