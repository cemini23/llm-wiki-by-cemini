---
title: "Differentiable topology optimization for acoustic holography — thick lenses, not thin elements"
type: source
tags: [source, arxiv, topology-optimization, acoustics, additive-manufacturing]
related: []
maturity: draft
read_status: skimmed
created: 2026-11-05
updated: 2026-11-05
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Differentiable topology optimization for high-fidelity acoustic holography beyond the thin-element approximation |
| Authors | Pradosh P. Dash, Costas D. Arvanitis (Georgia Tech) |
| arXiv | 2611.04251 |
| Pages | 32 |
| Read status | skimmed (abstract and title page) |

## Narrative

Acoustic holography in the megahertz range matters for manufacturing, non-destructive testing, and transcranial ultrasound. Designing lens topologies for complex holograms in the sub-megahertz to low-megahertz band is hard **because wave propagation through an acoustically thick lens cannot be ignored**.

The **thin-element approximation (TEA)** — treat the lens as a phase screen — is the standard simplification, and this paper quantifies where it fails.

### The method

**HASA**, a heterogeneous angular spectrum approach that admits **in-plane varying speed-of-sound maps** and supports rapid **differentiable optimisation with ADAM**, generating **three-dimensional lens topologies directly**.

That is the notable shift: the lens is not a 2D phase pattern printed at some thickness. It is a **3D material distribution**, optimised as such.

### Why it is filed here

A topology-optimised acoustic lens is a **3D-printed part** — that is the fabrication route for a heterogeneous speed-of-sound distribution. The paper is a genuine additive-manufacturing application in the medical and NDT space, which is what this wiki is for.

It is also a clean example of a methodological point worth keeping: **a differentiable surrogate that respects the real physics beats a faster approximation that does not**, and the paper's contribution is partly showing how much the approximation costs.

**Caveat.** Abstract only. No bandwidth, efficiency, or fabrication-tolerance figures reproduced.

## Snippets

> "Designing lens topologies for complex holograms in the sub-megahertz to low-megahertz regime most relevant to transcranial therapy is difficult, because wave propagation through an acoustically thick lens cannot be ignored." [Source: arxiv-2611.04251 p.1]

## Dead Ends

- **Citing a performance figure.** Abstract only.
