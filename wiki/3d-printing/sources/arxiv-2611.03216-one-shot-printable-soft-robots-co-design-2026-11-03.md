---
title: "One-shot printable soft robots — co-designing shape, actuators and control for FDM"
type: source
tags: [source, arxiv, soft-robotics, fdm, co-design, simulation]
related: []
maturity: draft
read_status: skimmed
created: 2026-11-03
updated: 2026-11-03
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Towards end-to-end co-design for one-shot printable task-specific soft robots |
| Authors | James Wood, André Farinha, Will Browne, Josh Pinskier, Krishna Manaswi Digumarti |
| arXiv | 2611.03216 |
| Pages | 7 |
| Read status | skimmed (abstract) |

## Narrative

Soft-robot co-design usually optimises morphology and control together and produces something that is hard to manufacture. Manufacturable approaches go the other way and restrict actuator placement or need manual assembly.

This paper closes that gap with a simulation-based framework that optimises **material distribution, pneumatic actuator placement and orientation, and control as one problem**, and outputs designs that are **monolithic FDM prints** — actuators integrated, no post-assembly.

The machinery:

- A **differentiable 2D plane-stress Material Point Method** simulator, so gradients flow through the physics.
- An experimentally validated material model.
- An empirically derived surrogate for a **3D-printed inflatable actuator**.

Demonstration: gradient-based optimisation of soft robotic arms for prescribed tip trajectories. Designed in simulation, printed in one shot, and the physical arms reproduce the simulated behaviour.

**Why this is the strongest of the three printing papers for this wiki.** The constraint is FDM, the output is one printed part, and the design loop closes from task objective to physical object. The surrogate model is the honest part — a printed inflatable actuator does not behave like an idealised one, and modelling that empirically is what makes the simulation predictive rather than decorative.

**Caveat.** Abstract only. No material, layer height, wall thickness, or actuator pressure is established here.

## Snippets

> "We present a simulation-based co-design framework that jointly optimises material distribution, pneumatic actuator placement and orientation, and control, while producing designs that can be fabricated monolithically using fused deposition modelling." [Source: arxiv-2611.03216 p.1]

> "Optimised designs are transferred directly from simulation to one-shot monolithic FDM fabrication, with integrated actuators and no post-assembly. Physical experiments demonstrate that the resulting arms reproduce the behaviour predicted in simulation." [Source: arxiv-2611.03216 p.1]

## Dead Ends

- **Citing print settings.** Abstract only.
