---
title: CosMAP-dr — contrastive DR implementation (BSD-2-Clause)
type: entity
tags: [entity, tool, dimensionality-reduction, bsd, watch, k235, omics]
keywords: [CosMAP-dr, UMAP, cosine-affinity, scRNA, kinship-embedding]
related:
  - sources/arxiv-2608.11269-cosmap-dr-2026-08-13.md
maturity: draft
created: 2026-08-13
updated: 2026-08-13
---

## Relations

- @sources/arxiv-2608.11269-cosmap-dr-2026-08-13.md — paper; OOD → WATCH routing

## Raw Concept

Repo `FenosoaRandrianjatovo/CosMAP-dr` (3★, last push 2026-07-29). Reference implementation of CosMAP (arXiv 2608.11269). **BSD-2-Clause verified** via gh api; cloned `.local/adopts/CosMAP-dr` (109M).

## Narrative

**Verdict: WATCH — reference clone only.** BSD-2-Clause is clean and the repo is small, so a reference clone is cheap; but the domain (single-cell omics DR) is out-of-scope for current product surfaces. The one in-domain hook: CosMAP was validated on a **BALSAC-CARTaGENE genealogical kinship dataset** — if kinship/cluster visualization ever becomes an Atto-adjacent question, this is the pre-audited candidate. `wont_wire` until then.

[Source: FenosoaRandrianjatovo/CosMAP-dr (retrieved 2026-08-13)]
