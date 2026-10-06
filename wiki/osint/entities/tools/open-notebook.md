---
title: "Open Notebook — Self-Hosted NotebookLM Alternative"
type: entity
tags: [tool, rag, multimodal, surrealdb, langchain, atto, k39, k283, integrate]
keywords: [open notebook, notebook lm, langchain, surrealdb, fastapi, nextjs, genealogy, atto, local-ollama]
related:
  - sources/evaluating-project-links-stacks.md
  - concepts/tool-evaluation-framework.md
  - concepts/cemini-license-posture.md
  - sources/eval-github-repos-dev-tools-2026-10-06.md
  - concepts/k283-eval-wave.md
maturity: validated
created: 2026-05-11
updated: 2026-10-06
---

## Relations
- `@sources/evaluating-project-links-stacks.md` — source evaluation brief (URL 3)
- `@concepts/tool-evaluation-framework.md` — three-surface methodology applied
- `@concepts/cemini-license-posture.md` — license posture context
- @sources/eval-github-repos-dev-tools-2026-10-06.md — K283 re-evaluation (Integrate GO)
- @concepts/k283-eval-wave.md — K283 cluster hub

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

## K283 re-evaluation (2026-10-06) — tier moves to Integrate

The K39 disqualifiers were **prod-host constraints on `cemini-prod` (Hetzner CPX21, 2.5 GB headroom)**. **That host was deleted 2026-09-18.** Re-scored against the laptop, the constraints change:

- **Integrate GO** (docx A: 1 Integrate, 6 Extract). Scores `atto high`, `genealogy high`, `local-abliterated-lab high`.
- **Verified 2026-10-06** (WebFetch): repo exists, **MIT**, ≈**39.9k stars**, 4.6k forks, 125 open issues. Description: "An Open Source implementation of Notebook LM with more flexibility and features".
- Use case: let Atto Concierge operators query thousands of pages of municipal registry PDFs with **page-level citations**, with **local-only Ollama inference** — no client PII to a cloud model.

### Constraints that still hold

- **Atto privacy perimeter:** local-only inference; no client genealogical PII to third-party cloud models; **no automated write to `truth.ged`**.
- **SurrealDB** is still outside the PostgreSQL/TimescaleDB convention. That constraint was prod-side; on the laptop it is a deployment choice, not a blocker — but it is a maintenance question for any Atto-side deployment.
- **Human-gated.** This is an evaluated lead, not a deployed system. No install this session.

### Wires

Phase-1 FILE only — Atto brief `../atto/briefs/2026-10-06_k283-open-notebook-local-rag.md`. No install, no clone.

[Source: GitHub Repositories Revenue Evaluation.docx; K283; retrieved 2026-10-06]
