---
title: "SIE (Superlinked) — semantic entity index for Atto"
type: entity
tags: [tool, integrate, apache-2, k225, atto]
keywords: [superlinked, sie, semantic index, genealogy, KG]
related:
  - sources/eval-url-batch-project-fit-2026-08-07.md
  - sources/eval-url-batch-agentic-osint-integrations-2026-08-06.md
  - entities/tools/book-to-skill.md
  - concepts/gpuology-genealogy-agent-kit.md
  - concepts/wiki-tooling-evaluation.md
  - entities/tools/pi-llm-wiki.md
maturity: draft
created: 2026-08-06
updated: 2026-08-07
phase_0_verdict: INTEGRATE — Apache-2.0 K225 (~158MB)
wire_status: pending
---

## Relations

- @sources/eval-url-batch-project-fit-2026-08-07.md — K226 Watch reaffirm (already Integrate K225)

- @entities/tools/pi-llm-wiki.md

- @sources/eval-url-batch-agentic-osint-integrations-2026-08-06.md
- @entities/tools/book-to-skill.md
- @concepts/gpuology-genealogy-agent-kit.md
- @concepts/wiki-tooling-evaluation.md

## Raw Concept

| Field | Value |
|-------|--------|
| **Repo** | https://github.com/superlinked/sie |
| **License** | Apache-2.0 `[CONFIRMED]` gh api K225 |
| **Local** | `.local/adopts/sie` (~158MB) |
| **Eval** | Integrate → Atto semantic entity retrieval |

## Narrative

**SIE** builds semantic indexes over structured + unstructured entity fields — candidate backbone for Atto parish/civil-record KG queries (names, places, dates) without naive vector-only RAG.

**Integration plan:** shallow Phase-0 clone; benchmark against existing Atto retrieval path; PII containment unchanged (local-first). **Not** a prod cemini wire.

## Snippets

> gh SPDX: Apache-2.0 — eval Integrate tier confirmed K225. [Source: eval-url-batch-agentic-osint-integrations-2026-08-06.md]
