---
title: "Influence lineages in jazz trumpet — reconstructing a network from recordings"
type: source
tags: [source, arxiv, networks, lineage, methodology, cultural-data]
related: []
maturity: draft
read_status: skimmed
created: 2026-11-05
updated: 2026-11-05
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Follow or Surpass? Collaboration, Sound, and the Recognition of Influence in Lineages of Jazz Trumpet Players |
| Authors | Onur Tuncay Bala, Samuel Coavoux, Nathalia A. Loureiro, Balazs Vedres, Mark Wittek (Central European University, University of Geneva) |
| arXiv | 2611.05750 |
| Pages | 43 |
| Read status | skimmed (abstract) |

## Narrative

**Filed for the method, not the subject.** The domain is jazz; the problem is reconstructing a lineage from incomplete evidence — which is the same problem as genealogical reconstruction.

### The finding

Cultural fields cohere not only **horizontally**, through collaboration, but **vertically**, through lineages of influence. Horizontal networks are well studied; vertical influence is not.

They build an influence network over a **genealogy of 52 prominent jazz trumpet players**, combining:

- discographies,
- demographic characteristics,
- geographical locations,
- **audio analysis of more than 16,000 recordings**,
- and **exponential random graph models**.

Three signals each contribute: **direct collaboration**, **overlap in collaborators**, and **sonic context similarity** — the similarity of the recordings on which players appear.

### Why this is a genealogy-methodology reference

The transferable structure:

1. A **sparse, curated set of named individuals** with dates and places.
2. **Inferred links** — influence is never observed directly, only through proxies.
3. **Multiple weak signals combined**, rather than one strong one.
4. **A statistical model** (ERGM) that accounts for network structure rather than treating links as independent.

That is close to how one would model a family lineage where the direct evidence — a birth record naming a parent — is missing for many nodes, and the linkage must be inferred from co-location, naming patterns, and timing.

The honest caveat transfers too: **every edge is an inference from proxies**, and the model's job is to be explicit about which proxy carries it.

**Caveat.** Abstract only. No coefficient or model-fit figures reproduced.

## Snippets

> "Direct collaboration, overlap in collaborators, and sonic context similarity… are each…" — the three signals, per the abstract [Source: arxiv-2611.05750 p.1]

## Dead Ends

- **Reading this as an Atto source.** It is a method reference for lineage inference from proxies.
