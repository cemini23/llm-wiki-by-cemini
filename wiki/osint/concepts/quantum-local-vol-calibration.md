---
title: Quantum calibration of local-volatility surfaces — cost baseline
type: concept
maturity: draft
related:
  - sources/arxiv-quantum-local-vol-calibration-2611.25344.md
  - concepts/local-stochastic-volatility-calibration.md
updated: 2026-11-22
---

## Raw Concept

Question this page answers: what would a quantum-assisted volatility calibration actually cost, and is there any production case yet?

Built from one paper, Hoshisashi (UCL, arXiv 2611.25344, 2026-11).

## Narrative

**The problem.** Calibrating a Dupire local-volatility surface from sparse quotes is an inverse problem. It needs the pricing equation solved many times as the coefficients change.

**The loop.** Local variance is written in a positive-coefficient form. Linear combinations of Hamiltonian simulations approximate the pricing evolution. The circuit propagates through successive maturity intervals and checks the mismatch at observed strikes. Measurement counts give the objective value, and a classical optimiser updates the coefficients.

**What was run.** A logical gate simulator, not quantum hardware. Multiple-maturity synthetic examples reconstruct smiles and skews. A separate small circuit experiment runs the full measured calibration.

**What it measures.** The paper separates three error sources: model flexibility, pricing approximation, and measurement precision. It records gate counts and sampling budgets, which are the dominant costs.

**Verdict.** This is a resource-estimation study. It shows no production advantage over classical calibration. Its value is a cost baseline and a clear statement of the error decomposition.

**Contrast.** Classical local-stochastic-volatility calibration by fixed-point iteration (arXiv 2611.18214) is the practical benchmark. Any quantum claim should be measured against it on the same quote set, not against a toy model.
