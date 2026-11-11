---
title: "Optimisation-based path planning for robotic additive manufacturing, validated on a UR10e"
type: source
tags: [source, arxiv, robotic-am, path-planning, optimisation, fibre-winding]
related: []
maturity: draft
read_status: skimmed
created: 2026-11-11
updated: 2026-11-11
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Optimization-Based Path Planning for Industrial Manipulators: Experimental Validation in Additive Manufacturing |
| Authors | Shiva Ganesh Murali, Valentin Bhend, and others |
| arXiv | 2611.13983 |
| Pages | 9 |
| Read status | skimmed (abstract) |

## Narrative

Robotic additive manufacturing needs joint paths that satisfy **robot feasibility** and **process geometry** at the same time. Those constraints pull in different directions: the process wants a specific toolpath, the arm wants joints it can actually reach and move through.

The paper's move is an **offline optimisation-based planner** that treats them as one problem:

- **Joint-path regularity** — smooth, even motion rather than jerky joint solutions.
- **Self-collision penalties.**
- **Process costs and constraints**, added through a **new process entering via its own reference, residuals, and tolerances**.

Two solving modes: **full-path** and **boundary-coupled chunked** optimisation, for references of different lengths. And **Iterative Weight Tuning (IWT)** sets the cost weights from the gaps between KPIs and their targets — rather than a human tuning weights by feel.

Validated in **carbon-fibre winding** and **robotic 3D printing**, both executed on a **UR10e**, with joint-level tracking recorded.

### Two ideas worth keeping

**IWT is the transferable one.** Setting cost weights from the measured gap between a KPI and its target turns weight selection from an art into a loop. It is the same principle as tuning against a metric rather than by intuition, applied inside an optimiser.

**The process plug-in shape** — a new process arrives as reference, residuals, and tolerances — is what makes one planner serve both winding and printing.

**Caveat.** Abstract only; no tolerance values or tracking-error figures reproduced.

## Snippets

> "Iterative Weight Tuning (IWT) determines the cost weights from the gaps between Key Performance Indicators (KPIs) and their targets." [Source: arxiv-2611.13983 p.1]

> "Both paths are executed on a UR10e, without extrusion for printing, with joint-level tracking recorded during execution." [Source: arxiv-2611.13983 p.1]

## Dead Ends

- **Citing a tolerance.** Abstract only.
