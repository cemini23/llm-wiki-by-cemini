---
title: Vectify OpenKB — local-first markdown wiki retrieval layer
type: entity
tags: [entity, tool, knowledge-base, markdown, pageindex, apache-2.0, adopt-eligible, k68]
keywords: [openkb, vectify, pageindex, local wiki, retrieval, markdown graph]
related:
  - sources/multi-wiki-tool-eval-22url-2026-05-26.md
maturity: draft
created: 2026-05-26
updated: 2026-05-26
---

## Relations

- @sources/multi-wiki-tool-eval-22url-2026-05-26.md — K68 doc-level evaluation source

## Raw Concept

Repository: `VectifyAI/OpenKB` (Apache-2.0, ~1.9k★, active 2026-05-25). Surfaced in K68 as an OSINT-primary Adopt candidate due to local markdown retrieval and PageIndex-style indexing.

## Narrative

**Verdict: CONDITIONAL-GO (Phase-0 pending).**

OpenKB is promising for laptop-side wiki tooling and query ergonomics, but Cemini already runs a production `kb-server` retrieval path on `cemini-librarian`. Adoption scope should be **steal-from retrieval/index patterns first**, not serving-path replacement.

Phase-0 checks required:
1. Verify nested-wiki support and path assumptions (known failure mode for this tool class).
2. Benchmark retrieval quality/latency against current kb-server on real corpus.
3. Confirm no hidden coupling to cloud PageIndex features for core local workflow.

## Snippets

> "OpenKB … local markdown retrieval with PageIndex integration." [Source: Tool Evaluation Prompt Analysis.docx — URL 1]
