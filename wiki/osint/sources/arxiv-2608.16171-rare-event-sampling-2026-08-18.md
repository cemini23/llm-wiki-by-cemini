---
title: "Rare-event sampling via cluster updates (arXiv 2608.16171)"
type: source
tags: [arxiv, networks, rare-events, k241]
keywords: [CPMC, cluster-update, Gillespie, cascade]
related:
  - sources/arxiv-2608.15987-threshold-cascades-2026-08-18.md
  - concepts/osint4all-catalog.md
maturity: draft
created: 2026-08-18
updated: 2026-08-18
read_status: read
---

## Relations

- @sources/arxiv-2608.15987-threshold-cascades-2026-08-18.md — cascade criticality complements rare-event sampling
- @concepts/osint4all-catalog.md — do not operationalize crimeware cascade tools from public directories

## Raw Concept

| Field | Value |
|-------|--------|
| Paper | arXiv:2608.16171, "Rare-event sampling for stochastic dynamics in network systems using cluster updates" |
| Authors | Jiazheng Sun, James Moody, Thomas Barthel (Duke / Maryland) |
| Retrieved | 2026-08-18 |
| File | `arxiv-2608.16171-rare-event-sampling-for-stochastic-dynamics-in-n.pdf` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2608.16171-rare-event-sampling-for-stochastic-dynamics-in-n.pdf` |
| Type | cond-mat / network dynamics preprint |
| Dual-ID | **OSINT K241**. Wiki awareness. |

## Narrative

Consequential macroscopic events on networks — cascading failures, epidemic outbreaks, opinion shifts — come from rare localized coincidences that must pass bottlenecks. Gillespie forward-time simulation dies on rejection rates. Splitting and transition-path sampling trap, degenerate, or slow down on heterogeneous graphs.

**Concrete claim `[TENTATIVE]`:** **conditional-path Monte Carlo (CPMC)** borrows loop/cluster algorithms from equilibrium condensed matter. Non-local spacetime cluster updates with **no rejections** generate a Markov chain of trajectories that all obey the targeted macroscopic boundary condition (e.g. a massive network failure). Demo: risk-factor analysis of rare large-scale SIS outbreaks on kinship networks.

Wiki use: methodology bookmark for rare-event / cascade work. Not a prod trading sampler and not a cyber PoC.

## Snippets

> "By employing non-local updates on spacetime clusters without rejections, CPMC generates a Markov chain of trajectories that all strictly respect the targeted macroscopic boundary conditions" [Source: arxiv-2608.16171 abstract]
