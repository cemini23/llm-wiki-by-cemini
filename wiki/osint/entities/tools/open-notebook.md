---
title: "Open Notebook — Self-Hosted NotebookLM Alternative"
type: entity
tags: [tool, rag, multimodal, surrealdb, langchain, reference-only, k39]
keywords: [open notebook, notebook lm, langchain, surrealdb, fastapi, nextjs, ram-overcap]
related:
  - sources/evaluating-project-links-stacks.md
  - concepts/tool-evaluation-framework.md
  - concepts/cemini-license-posture.md
maturity: draft
created: 2026-05-11
updated: 2026-05-11
---

## Relations
- `@sources/evaluating-project-links-stacks.md` — source evaluation brief (URL 3)
- `@concepts/tool-evaluation-framework.md` — three-surface methodology applied
- `@concepts/cemini-license-posture.md` — license posture context

## Raw Concept

- **Repo / URL** (per source brief): `github.com/lfnovo/open-notebook`
- **Tier (per source brief)**: **Reference-only**
- **License** (per source brief): MIT
- **Stack**: TypeScript 62.4% / Python 35.8%; FastAPI, Next.js, React, SurrealDB, LangChain, Docker
- **Maturity** (per source brief): 23.3K★ / 2.7K forks / active April 2026 roadmap

## Narrative

Self-hosted multi-modal research assistant — privacy-focused NotebookLM clone. Ingests PDFs / video / audio / web pages / Office docs into a vector space; provides chat + vector search + multi-speaker podcast generation. 18+ LLM providers including local Ollama.

### Integration vector

**Reference-only**:
- LangChain multi-model fallback matrix is a useful pattern study for Cemini's `wiki_lint.py` LLM router
- Multi-modal ingestion parsers (PDF / audio / video) provide reference architecture for any future Cemini audio/video research ingestion
- Wholesale deployment **disqualified** by: (a) 3-5 GB RAM baseline vs 2.5 GB Hetzner CPX21 headroom; (b) SurrealDB violates the PostgreSQL/TimescaleDB-only constraint

### NEEDS VERIFICATION

- Exact idle RAM consumption of the full Docker Compose stack

### Phase-0 audit status

Reference-only — no Phase-0 needed unless full deployment reconsidered.

[Source: Evaluating Project Links for Stacks.docx URL 3; retrieved 2026-05-11]
