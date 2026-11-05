---
title: "v10.11 late skips — no lane for these inbox PDFs"
type: source
related:
  - sources/eval-multi-wiki-link-revenue-v10-11-2026-11-05.md
maturity: draft
read_status: skimmed
created: 2026-11-05
updated: 2026-11-05
---

## Raw Concept

| Field | Value |
|-------|-------|
| arXiv | 2611.05092, 2611.05258 |
| Retrieved | 2026-11-05 |
| Read status | skimmed (title and abstract only) |

## Narrative

| arXiv | Inbox | Why it is skipped |
|---|---|---|
| 2611.05092 | ccc | **Search and Verification for Strategyproof Facility Location on Metric Graphs.** Computational social choice: computing upper and lower bounds on the approximation ratio achievable by strategyproof mechanisms, via cost-preserving reductions and linear-programming dual certificates. Rigorous, and about mechanism design on graphs — not about agents, harnesses, or retrieval. No Cemini surface. |
| 2611.05258 | image-gen | **Universality in Anomalous Diffusion: Power Laws and Faster-Decaying Tails.** Statistical physics. Hyper-scaling relations between the exponents of strong anomalous diffusion, and finite-time corrections. The diffusion machinery has no image-generation or trading application within this estate. |

Two papers, two unrelated fields, one shared reason: the digest query is global and the inbox is per domain, so a topic with no lane still arrives.

Filing the ids here makes the next `preingest_check.py` call them duplicates.

## Snippets

> "Our theory provides universal hyper-scaling relations between the exponents characterizing strong anomalous diffusion." [Source: arxiv-2611.05258 p.1]

## Dead Ends

- **Routing 2611.05092 to CCC because it says "strategyproof".** It is facility location on metric graphs, not agent strategy.
