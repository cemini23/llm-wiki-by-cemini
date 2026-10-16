---
title: xerj — local Elasticsearch-compatible passage indexer
type: entity
tags: [tools, retrieval, search, k292]
keywords: [xerj, elasticsearch-compatible, passage-indexer, rust, pdf, log-search, token-reduction]
related:
  - sources/eval-url-multi-wiki-repository-2026-10-16.md
maturity: draft
created: 2026-10-16
updated: 2026-10-16
wire_status: extract_only
---

## Relations

- @sources/eval-url-multi-wiki-repository-2026-10-16.md

## Raw Concept

**What prompted this page:** K292 tool eval (2026-10-16). Phase-0 licence read via `gh api`; shallow-cloned to `.local/adopts/k292/` as REFERENCE. **No install. 0 Integrate GO.**

## Narrative

A **Rust local passage indexer** that speaks the **Elasticsearch-compatible** API over code, PDFs and logs. The eval's stated payoff is a **2.7× to 5× reduction in agent output tokens** — retrieval returns passages rather than whole files.

**Licence:** **Apache-2.0** — `[CONFIRMED]` by `gh api` on 2026-10-16 (the docx agreed).

**Docx tier: Extract.** Cloned (275,112 KB — the second-largest clone and half the budget overrun).

**Why it is the most directly useful Extract of the batch:** it addresses retrieval over exactly this workspace's material — PDFs and logs — and the local-indexing shape matches the K292 Librarian Agents finding that **anticipatory retrieval beats fetching whole documents**. The Elasticsearch compatibility also means an existing client works against it.
