---
title: "Disorder-blind Mpemba acceleration of quantum state preparation (arXiv:2611.08424)"
type: source
tags: [source, arxiv, quantum, physics, relaxation, peripheral]
keywords: [Mpemba effect, strong Mpemba, disordered XX chain, resistor chain, slow mode, dephasing, state preparation, peripheral]
related:
  - concepts/fokker-planck-stationary-distributions.md
read_status: read
created: 2026-11-10
updated: 2026-11-10
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Disorder-blind Mpemba acceleration of quantum state preparation |
| Author | M Nishanth, Shreyas Sadugol, Payman Mahmoudi, Alexander Yosifov, Aditya Iyer, Roopayan Ghosh, Jinzhao Sun (IIT Bhubaneswar, QMUL, MCLA, Oxford) |
| Type | arXiv:2611.08424, 21 pages |
| Location | `research to be indexed/image-gen/arxiv-2611.08424-disorder-blind-mpemba-acceleration-of-quantum-st.pdf` |
| Retrieved | 2026-11-10 |
| File | `arxiv-2611.08424-disorder-blind-mpemba-acceleration-of-quantum-st.pdf` |
| Read status | read (abstract, mechanism, thresholds) |

## Narrative

**Peripheral to image generation.** This is quantum statistical mechanics. Nothing in it can be run on an image model today. The page exists so a later search for "Mpemba" or "mode cancellation" resolves to an honest stub rather than a false lead.

**The physics.** The strong Mpemba effect shortens relaxation time by preparing an initial state whose overlap with the slowest decaying mode is zero. Normally this needs knowledge of the system, because the slow mode has to be suppressed on purpose. In a disordered system the slow mode differs per sample, so a fixed preparation usually keeps some overlap.

**The result.** A "blind" preparation, designed from the clean chain without knowledge of the disorder, can still win in typical samples. It needs only the chain geometry and the particle number. In the dephased disordered XX chain at strong dephasing, the density dynamics map to a resistor chain. An exact inverse-generator identity links the residual overlap to the spatial resistance profile.

**Two thresholds.** A finite mean resistance is enough for diffusion. The residual overlap decays as L^(−1/2) with chain length L only when the resistance variance is also finite. Rare weak links slow the decay.

The paper predicts the fraction of samples where the blind preparation wins, and finite-size calculations support both scaling regimes.

**Why it is in this wiki at all.** The mathematical shape — a stationary state reached by relaxation, where initial-condition design changes the convergence rate — is the same shape as sampler schedule design. The connection is analogical only. No image, video or diffusion-model experiment is present, and no transfer is claimed.

## Snippets

> "We show that a 'blind' preparation, designed from the clean chain without knowledge of the disorder realisation or its distribution, can start farther from stationarity yet overtake a reference in typical samples of a dephased disordered XX chain." [Source: arxiv-2611.08424 p.1]

> "A finite mean resistance suffices for diffusion, but the residual overlap decays as L−1/2 with chain length L only when the resistance variance is finite; rare weak links slow this decay." [Source: arxiv-2611.08424 p.1]
