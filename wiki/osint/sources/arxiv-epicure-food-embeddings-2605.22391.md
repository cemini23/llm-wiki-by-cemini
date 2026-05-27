---
title: "Epicure — food ingredient embeddings (arXiv 2605.22391)"
type: source
tags: [source, arxiv, food-science, embeddings, metapath2vec, filter-3-skip, k71]
keywords: [epicure, flavorgraph, ingredient embeddings, npmi, metapath2vec, culinary modes, slerp, kaikaku]
related:
  - concepts/high-signal-paper-patterns.md
  - concepts/llm-augmented-entity-consolidation.md
  - sources/multi-wiki-tool-eval-27url-2026-05-27.md
maturity: draft
read_status: deep-read
created: 2026-05-27
updated: 2026-05-27
clusters: [cross-domain-methodology]
---

## Relations

- @concepts/high-signal-paper-patterns.md — Filter 3 domain mismatch (food/culinary); methodology borrow only
- @concepts/llm-augmented-entity-consolidation.md — LLM string normalization 6,653→1,790 canonical ingredients [TENTATIVE cross-domain]
- @sources/multi-wiki-tool-eval-27url-2026-05-27.md — K71 batch (same ingest day)

## Raw Concept

- **Title**: Epicure: Navigating the Emergent Geometry of Food Ingredient Embeddings
- **Authors**: Jakub Radzikowski, Josef Chen (KAIKAKU.AI)
- **arXiv**: [2605.22391](https://arxiv.org/abs/2605.22391) (v1, May 2026)
- **Location**: `research to be indexed/2605.22391v1.pdf` → `cemini-librarian:/opt/cemini-bulk/research/2605.22391v1.pdf`
- **Retrieved**: 2026-05-27
- **Read status**: deep-read (abstract + methods skim; not Cemini trading domain)

## Narrative

**Filter 3:** No direct Cemini/OSINT financial overlap — prior sweep logged Epicure as food/flavor domain skip (2026-05-23). Ingested as **methodology reference** only, not prod adoption.

**Contribution:** Three sibling **Metapath2Vec** ingredient embeddings (300-D) on 4.14M multilingual recipes → 1,790 canonical ingredients via **LLM-augmented normalization**. Variants **Cooc** (recipe NPMI only), **Chem** (FlavorDB compound metapaths), **Core** (blended walks) — controllable chemistry-vs-context axis.

**Operators:** nearest-neighbour pairing + **SLERP** direction arithmetic toward supervised poles or emergent GMM modes (~150–200 modes/model).

**Cemini steal (patterns only):** LLM-assisted entity consolidation pipeline; multi-graph walk-schema ablation; unsupervised factor + mode naming for interpretable embedding navigation — analogies for wiki entity consolidation / concept factor analysis, not gastronomy product work.

**Release:** Code and trained artefacts **not released** at submission time.

## Snippets

> "We normalise the raw ingredient strings to 1,790 canonical entries via an LLM-augmented pipeline." [Source: 2605.22391v1.pdf, Abstract]

> "Code and trained artefacts are not released at this time." [Source: 2605.22391v1.pdf, Abstract]
