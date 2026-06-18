---
title: "LeWorldModel: Stable End-to-End Joint-Embedding Predictive Architecture from Pixels"
type: source
tags: [leworldmodel, world-model, reinforcement-learning, computer-vision, joint-embedding-predictive-architecture]
keywords: [LeWorldModel, JEPA, world model, reinforcement learning, computer vision, stable training, representation collapse]
related:
  - concepts/exploration-graph-dead-ends.md
  - concepts/moverse-panoramic-video-world-model.md
  - concepts/multi-agent-embodied-autonomous-driving-survey.md
  - sources/arxiv-moverse-panoramic-world-model-2606.13376-2026-06-18.md
  - sources/arxiv-maead-shared-world-models-2606.13840-2026-06-18.md
  - entities/frameworks/pettingzoo.md
  - entities/tools/blade-github.md
maturity: draft
read_status: read
created: 2026-05-09
updated: 2026-05-09
---

## Relations

- @concepts/exploration-graph-dead-ends.md — potential dead-end tracking for world-model research line
- @entities/frameworks/pettingzoo.md — PettingZoo multi-agent RL framework; LeWM could be evaluated with PettingZoo environments
- @sources/arxiv-maead-shared-world-models-2606.13840-2026-06-18.md — MAEAD survey sibling
- @sources/arxiv-moverse-panoramic-world-model-2606.13376-2026-06-18.md — MoVerse visual world model sibling

## Raw Concept

**Title**: LeWorldModel: Stable End-to-End Joint-Embedding Predictive Architecture from Pixels
**Authors**: Lucas Maes*, Quentin Le Lidec*, Damien Scieur, Yann LeCun, Randall Balestriero
**Affiliation**: Mila & Université de Montréal; New York University; Samsung SAIL; Brown University
**Date**: 2026-05-09 (arXiv v1)
**arXiv**: 2603.19312 [cs.CV]
**Canonical location**: `cemini-librarian:/opt/cemini-bulk/research/2603.19312v2.pdf`
**Retrieved**: 2026-05-09 via preingest pipeline
**Read status**: read (full paper, 15 pages + appendices)

**Why this matters for Cemini**: Introduces a stable end-to-end JEPA world model trained from raw pixels — relevant to Cemini's long-term autonomy stack (RL-based strategy execution, visual environment modeling). The two-term loss (prediction + Gaussian regularization) and 15M-parameter footprint make it deployable on single-GPU setups relevant to Cemini's Hetzner infrastructure.

## Narrative

### Paper Summary

LeWorldModel (LeWM) is a Joint Embedding Predictive Architecture (JEPA) that trains stably end-to-end from raw pixels using only two loss terms: a next-embedding prediction loss and a SIGReg regularizer enforcing Gaussian-distributed latent embeddings. This reduces tunable hyperparameters from six to one compared to the only existing end-to-end alternative (PLDM).

**Key claims:**
- 15M trainable parameters, trainable on a single GPU in a few hours
- Plans up to 48× faster than foundation-model-based world models (DINO-WM)
- Competitive across diverse 2D and 3D control tasks (Push-T, OGBench-Cube, TwoRoom, Reacher)
- Latent space encodes meaningful physical structure (verified via probing)
- Surprise evaluation confirms reliable detection of physically implausible events

### Architecture

- **Encoder**: ViT-Tiny (patch size 14, 12 layers, 3 heads, hidden dim 192) →  token → MLP projection → 192-dim latent
- **Predictor**: ViT-S with 6 layers, 16 attention heads, 10% dropout (~10M params). Actions injected via Adaptive Layer Normalization (AdaLN).
- **Training objective**: `L = L_pred + λ * SIGReg(Z)` where:
  - `L_pred` = MSE between predicted and actual next embeddings
  - `SIGReg` = Sketched-Isotropic-Gaussian Regularizer (projects embeddings onto M random directions, applies Epps-Pulley normality test)
- **Only hyperparameter to tune**: λ (regularization weight). Default: λ=0.1, M=1024 projections.

### Key Results

| Environment | LeWM SR | DINO-WM SR | PLDM SR |
|-------------|---------|------------|---------|
| Push-T | 96.0% | ~78% (w/ proprio: ~92%) | 78.0% |
| OGBench-Cube | Competitive | Slightly better | Lower |
| TwoRoom | Lower | Higher | Higher |
| Reacher | Competitive | Competitive | Competitive |

- Planning time: **48× faster** than DINO-WM (sub-second full planning)
- Physical probing: LeWM matches/exceeds PLDM on all physical quantity probes; competitive with DINO-WM
- Temporal straightening emerges naturally without explicit regularization

### Limitations Noted by Authors
- Planning restricted to short horizons (5-step MPC)
- Requires offline datasets with sufficient coverage
- SIGReg less effective in very simple/low-dimensionality environments (TwoRoom)
- Still requires action labels (future work: inverse dynamics modeling)

## Snippets

- "the first method to learn a stable JEPA end-to-end from raw pixels without heuristic, principled, and simple" [Source: 2603.19312, Abstract]
- "reduces tunable loss hyperparameters from six to one compared to the only existing end-to-end alternative" [Source: 2603.19312, Abstract]
- "plans up to 48× faster than foundation-model-based world models while remaining competitive across diverse 2D and 3D control tasks" [Source: 2603.19312, Abstract]
- "the model reliably detects physically implausible events" [Source: 2603.19312, Abstract]
- "LeWM achieves higher temporal straightness than PLDM, despite PLDM employing a dedicated temporal smoothness regularization term" [Source: 2603.19312, §5.1]

## Dead Ends

- TwoRoom environment: SIGReg regularization conflicts with low intrinsic dimensionality → less structured latent representations → worse planning performance. Potential mitigation: environment-specific regularization tuning or pre-training on diverse natural video datasets.
- No immediate Cemini integration path identified — world-model research is upstream of any current Cemini use case. Watch for Causal-JEPA (2602.11389) as next evolution.