---
title: Turbovec (TurboQuant vector index)
type: entity
tags: [tool, k170]
keywords: [turbovec]
related:
  - concepts/xsp-lane-trading-framework.md
  - sources/eval-revenue-opportunity-url-analysis-2026-07-16.md
  - concepts/wiki-tooling-evaluation.md
  - concepts/kb-server-retrieval-scaling.md
  - entities/infrastructure/conductor-librarian-architecture.md
  - entities/tools/leann.md
  - sources/multi-wiki-link-eval-v4-2026-05-15.md
maturity: draft
created: 2026-07-16
updated: 2026-10-25
---

## Narrative

| Field | Value |
|-------|-------|
| **Repo / docs** | RyanCodrai/turbovec |
| **License** | MIT (~12.9k★; ~5MB) |
| **Verdict** | **Integrate** |
| **Routing** | xsp / CCC RAG |

Rust vector index with Python bindings; online ingest without FAISS training phase. Candidate for local sentiment/RAG under tight RAM. Soak before replacing any prod index.
