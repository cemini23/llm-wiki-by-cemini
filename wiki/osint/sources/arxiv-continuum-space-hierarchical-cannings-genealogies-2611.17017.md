---
title: "Continuum space hierarchical Cannings process II: genealogies and ancestral web (arXiv 2611.17017)"
type: source
related:
  - concepts/osint-inbox-wave-2026-11-14.md
updated: 2026-11-14
---

## Raw Concept

| Field | Value |
|-------|--------|
| Title | Continuum space hierarchical Cannings process: II. Genealogies and ancestral web |
| Author | A. Greven (Erlangen–Nürnberg), F. den Hollander (Leiden) |
| Type | arXiv preprint, probability (60K35) |
| arXiv | 2611.17017v1, 13 Nov 2026 |
| Pages | 54 |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2611.17017-continuum-space-hierarchical-cannings-process-ii.pdf` |
| Retrieved | 2026-11-14 |
| Read status | read |

## Narrative

### What the paper does

This is the second of three papers on a spatial multi-type population model. The model has four mechanisms: migration, Fleming–Viot resampling, Λ₀-Cannings resampling, and (Λ_k)-Cannings block-resampling. The geographic space is the continuum limit Ω∞_N of a discrete hierarchical group Ω_L^N.

Paper I built the measure-valued process for type frequencies on Ω∞_N. This paper builds the **genealogies** of that population, and then an **ancestral web**.

### The dichotomy

The genealogy process has two regimes.

| Regime | Ancestry | Type-frequency dynamics |
|---|---|---|
| (1) Stochastic | Population descends from a single ancestor, locally and over time-expanding sets | Non-trivial stochastic limit |
| (2) Deterministic | Descendants come from different ancestors | Deterministic; genealogy is "dust" |

Regime (1) holds for point-recurrent migration, and for Harris-recurrent migration when block-resampling is present. Regime (2) holds for transient migration. For recurrent migration the authors get a decomposition of Ω∞_N into random balls, each monotype.

### The ancestral web

The new object is the ancestral web. It replaces populations of individuals by populations of whole paths (lineages) in ancestral-type-geographic space. The dual object is a Lévy-web, the jump-process analogue of the Brownian web. The forward web and the backward dual sit in one grounded tree-like marked fibred metric measure space, in strong graphical duality.

The third paper will take a hierarchical mean-field limit and identify universality classes.

### Why it is filed here

**This paper has no practical Cemini project link.** It is pure probability theory. It concerns population genetics and interacting particle systems. No pricing model, no market microstructure, no agent harness, and no dataset here is a candidate for this workspace.

The paper is recorded because the digest query is global and the inbox is per domain. A reader should not mistake the word "genealogy" for the Atto genealogy product. Atto builds civil-record family trees from Italian archives. This paper studies the ancestry of a measure-valued population process. The two share one English word and nothing else.

[OPEN QUESTION 2026-11-14] No Cemini surface. Filed to keep the next `preingest_check.py` call from re-reading it.

## Snippets

> "The genealogical structure is degenerate: the family decomposition is dust." [Source: arxiv-2611.17017-continuum-space-hierarchical-cannings-process-ii.pdf p.1]

> "It replaces populations of individuals by populations of paths, and embeds two objects: the genealogical process on U and the measure-valued process on Ω∞_N × K." [Source: arxiv-2611.17017-continuum-space-hierarchical-cannings-process-ii.pdf p.1]
