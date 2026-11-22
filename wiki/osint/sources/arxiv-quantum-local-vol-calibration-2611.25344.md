---
title: "Quantum calibration of local-volatility surfaces from sparse option quotes"
type: source
maturity: draft
related:
  - concepts/quantum-local-vol-calibration.md
  - concepts/local-stochastic-volatility-calibration.md
updated: 2026-11-22
---

## Raw Concept

| Field | Value |
|-------|--------|
| Title | Quantum Calibration of Local-Volatility Surfaces from Sparse Option Quotes |
| Author | Kentaro Hoshisashi (UCL) |
| Type | arXiv preprint, quantum computing / computational finance |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2611.25344-quantum-calibration-of-local-volatility-surfaces.pdf` |
| Retrieved | 2026-11-22 |
| arXiv | 2611.25344v1 |
| Pages | 7 |
| Read status | read |

## Narrative

Calibrating a volatility surface from sparse quotes means solving a pricing equation many times as the parameters change. This paper implements a hybrid quantum-classical loop for that inverse problem under the Dupire local-volatility model.

The local variance is written in a positive-coefficient form. Linear combinations of Hamiltonian simulations approximate the pricing evolution. The circuit propagates through successive maturity intervals and evaluates the mismatch at observed strikes. Measurement counts give the objective values that a classical optimiser uses to update the coefficients. [Source: arxiv-2611.25344-quantum-calibration-of-local-volatility-surfaces.pdf p.1]

The work runs on a logical gate simulator, not on hardware. It compares the loop against classical pricing solvers and alternative surface models. Multiple-maturity synthetic examples reconstruct smiles and skews. A separate small circuit experiment tests the full measured calibration.

Two useful outputs are the error decomposition and the cost accounting. The paper separates model flexibility, pricing approximation and measurement precision. It records gate counts and sampling budgets, which are the main costs of this approach.

The honest read: this is a resource-estimation study. It does not show a production advantage. Its value to the wiki is a clear statement of what quantum calibration would cost, and a baseline against classical local-vol work such as the fixed-point local-stochastic-volatility method.

## Snippets

> "The circuit propagates through successive maturity intervals and evaluates discrepancies at the observed strikes." [Source: arxiv-2611.25344-quantum-calibration-of-local-volatility-surfaces.pdf p.1]
