---
title: "The broadcast voter model: Stationary measures (arXiv 2610.04530)"
type: source
tags: [source, k283, arxiv, probability, math]
keywords: [voter-model, stationary-measures, coalescing-random-walk, duality, consensus]
related:
  - concepts/k283-arxiv-wave.md
maturity: draft
created: 2026-10-06
updated: 2026-10-06
read_status: skimmed
---

## Relations

- @concepts/k283-arxiv-wave.md

## Raw Concept

| Title | The broadcast voter model: Stationary measures |
| Authors | Jhon Astoquillca (USP), Adrián González Casanova (ASU), Renato S. dos Santos (UFMG) |
| Type | arXiv preprint (math.PR) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2610.04530-the-broadcast-voter-model-stationary-measures.pdf` |
| Retrieved | 2026-10-06 |
| arXiv | 2610.04530v1 |
| read-status | skimmed |

## Narrative

Pure probability. The classical voter model has each voter copy **one** neighbour. This paper introduces the **Λ-broadcast voter model**: a voter broadcasts its opinion to several neighbours at once, with the number chosen by a finite measure Λ on [0,1]. Λ = δ₀ recovers the classical model.

The dual process is a system of **coordinated coalescing random walks (Λ-CCRWs)**. The authors classify the stationary measures using the infinite/finite collision property of the walk:

- **Infinite collision** ⇒ the extremal invariant measures are only {δ₀, δ₁}.
- **Finite collision** ⇒ a family µ_{α,Λ} indexed by harmonic functions α ∈ H.

For finite-range graphs G_{d,R}: dimensions 1 and 2 give consensus; dimension d ≥ 3 admits non-trivial µ_{p,Λ}, ergodic under translation. The dependence on Λ enters only through normalised moments λ^(k)_Λ. Full characterisation is proved on bounded-degree trees and on nearest-neighbour Z^d (d ≥ 3).

**No finance, agent, security, or game-dev hook.** Ingested for completeness and for the duality technique (a coordinated-coalescing dual). No license stated; no code.

## Snippets

> "When Λ = δ₀ the model reduces to the classical voter model." [Source: arxiv-2610.04530-the-broadcast-voter-model-stationary-measures.pdf]
