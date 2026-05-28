---
title: Vectify OpenKB — local-first markdown wiki retrieval layer
type: entity
tags: [entity, tool, knowledge-base, markdown, pageindex, apache-2.0, adopt-eligible, k68]
keywords: [openkb, vectify, pageindex, local wiki, retrieval, markdown graph]
related:
  - sources/multi-wiki-tool-eval-22url-2026-05-26.md
maturity: draft
created: 2026-05-26
updated: 2026-05-28
---

## Relations

- @sources/multi-wiki-tool-eval-22url-2026-05-26.md — K68 doc-level evaluation source

## Raw Concept

Repository: `VectifyAI/OpenKB` (Apache-2.0, ~1.9k★, active 2026-05-25). Surfaced in K68 as an OSINT-primary Adopt candidate due to local markdown retrieval and PageIndex-style indexing.

## Narrative

**Verdict: CONDITIONAL-GO (Phase-0 complete 2026-05-28).**

OpenKB is promising for laptop-side wiki tooling and query ergonomics, but Cemini already runs a production `kb-server` retrieval path on `cemini-librarian`. Adoption scope should be **steal-from retrieval/index patterns first**, not serving-path replacement.

Phase-0 results:
1. License/maturity verified (`VectifyAI/OpenKB`, Apache-2.0, ~1.9k★, active).
2. Repo architecture confirms heavy **PageIndex coupling** for long-doc retrieval; requires LLM API key (`LLM_API_KEY`) and local wiki scaffold (`raw/`, `wiki/`, `.openkb/`).
3. No immediate hardcoded Cemini paths found, but it is effectively a parallel wiki-compilation framework rather than a drop-in kb-server replacement.

Recommended posture: local-only evaluation / steal-from retrieval ideas; keep librarian `kb-server` as serving path until side-by-side benchmark is run.

## Snippets

> "OpenKB … local markdown retrieval with PageIndex integration." [Source: Tool Evaluation Prompt Analysis.docx — URL 1]
