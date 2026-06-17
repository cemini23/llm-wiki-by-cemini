---
title: WikiKV — hierarchical path-indexed wiki storage (REFERENCE)
type: entity
tags: [tool, wiki, rag, reference, k121]
keywords: [WikiKV, path-indexed, Tencent, hierarchical knowledge base]
related:
  - sources/arxiv-wikikv-hierarchical-kv-2606.14275-2026-06-17.md
  - concepts/wiki-tooling-evaluation.md
  - meta/librarian-decommission-2026-06-14.md
  - concepts/federated-daily-research-digest.md
maturity: draft
created: 2026-06-17
updated: 2026-06-17
phase_0_verdict: REFERENCE
license_verified: n/a
repo: n/a
cross-wiki-source: "@seo-wiki/entities/tools/wikikv.md"
---

## Relations

- @sources/arxiv-wikikv-hierarchical-kv-2606.14275-2026-06-17.md
- @concepts/wiki-tooling-evaluation.md
- @meta/librarian-decommission-2026-06-14.md
- @concepts/federated-daily-research-digest.md — federation digest read path
- @seo-wiki/entities/tools/wikikv.md

## Raw Concept

Cross-wiki entity from SEO K121 ingest. Tencent WikiKV — production hierarchical wiki KV; **REFERENCE** until OSS release.

## Narrative

### Phase-0 (2026-06-17)

| Check | Result |
|-------|--------|
| Code | None public |
| Verdict | **REFERENCE** — pattern steal for federation wikis |
| vs llm-wiki-compiler | WikiKV assumes hierarchy-native storage; compiler blocked on flat-layout — orthogonal problems |
| vs Deep GraphRAG | Both hierarchy-first; WikiKV is storage layer not graph-community retrieval |

Prod brief: @seo-wiki/briefs/2026-06-17_k121-wikikv-hierarchical-wiki-storage-cemini-prod.md
