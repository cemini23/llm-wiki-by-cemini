---
title: "CosMAP — Contrastive DR for Omics and Genealogical Data"
type: source
tags: [arxiv, k235, omics, dimensionality-reduction, genealogy, watch]
keywords: [2608.11269, CosMAP, UMAP, scRNA-seq, BALSAC, contrastive, manifold, embedding]
related:
  - entities/tools/cosmap-dr.md
  - concepts/computational-genealogy-archival-automation.md
maturity: draft
created: 2026-08-13
updated: 2026-08-13
read_status: skimmed
---

## Relations

- @entities/tools/cosmap-dr.md — BSD-2-Clause repo cloned to `.local/adopts/`
- @concepts/computational-genealogy-archival-automation.md — kinship-dataset genealogy angle

## Raw Concept

| Field | Value |
|-------|--------|
| arXiv | 2608.11269 (q-bio.GN, 2026-08-11) |
| Authors | Randrianjatovo, Saleh, Girard, Barry (INRS / UQAC) |
| sha256 | `80d42243e31993dd2e47392979a57d3dd0f3ebf9f20f0172b3e4bdd99f73ec6f` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2608.11269-cosmap-contrastive-manifold-approximation-and-pr.pdf` |
| retrieved | 2026-08-13 |

## Narrative

CosMAP extends UMAP's graph framework for **sparse, zero-dominated high-dimensional data**: cosine-similarity neighbourhoods + temperature-normalized contrastive affinities, optimized with an attractive–repulsive objective, plus a two-phase refinement (learn intermediate higher-dim representation → reconstruct neighbourhood graph → initialize final embedding). Benchmarks: MNIST/USPS digits, mouse retina + cortex scRNA-seq, Heart Cell Atlas, PBMC, and a **BALSAC-CARTaGENE genealogical kinship dataset** — the genealogy hook that justifies a Watch in this workspace (kinship/regional clustering parallels Atto-adjacent population-structure questions, though Atto's core is record retrieval, not embedding).

Better neighbourhood preservation + clearer global organization than SOTA DR baselines. Default config τ=0.5, k=15 fixed across datasets (no per-dataset tuning).

**Routing: OOD → WATCH.** Omics DR is out-of-domain for the trading/genealogy product surface; the repo is BSD-2-Clause and small (cloned `.local/adopts/CosMAP-dr`, 109M) so a reference clone is cheap. No prod wiring; no Atto pipeline integration without a concrete kinship-embedding use case.

[Source: arXiv:2608.11269]

## Snippets

> "Omics datasets, particularly single-cell RNA sequencing data, are high-dimensional, sparse, noisy, and dominated by zero values … with similar limitations arising in genealogical data." [Source: arXiv:2608.11269 p.1]
