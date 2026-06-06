---
title: typst/typst — markup PDF compiler (Rust)
type: entity
tags: [entity, tool, document-generation, adopt, phase-0, k102]
keywords: [typst, pdf, briefs, typesetting, apache-2.0]
related:
  - sources/multi-wiki-tool-eval-50url-k102-2026-06-06.md
  - concepts/cemini-wiki-ingest-workflow.md
maturity: validated
created: 2026-06-06
updated: 2026-06-06
phase_0_verdict: CONDITIONAL-GO
license_verified: Apache-2.0
repo: https://github.com/typst/typst
---

## Relations

- @concepts/cemini-wiki-ingest-workflow.md — optional brief PDF export path

## Raw Concept

K102 Adopt; **Apache-2.0** verified; ~54k★. K93 v5 had Defer — promoted after K102 eval + Phase-0 (laptop-only).

## Narrative

Fast LaTeX alternative for compiling `briefs/` and wiki exports to stakeholder PDFs. **Not** on prod trading path or kb-server.

**Phase-0 verdict: CONDITIONAL-GO** — install binary on laptop (`brew install typst` or official release); wire optional `scripts/compile_brief_pdf.sh` later. No server deploy without separate brief.

**Failure mode (doc-gen class):** none — standalone CLI; no hardcoded wiki layout.

## Snippets

> "Incremental compilation magnitudes faster than LaTeX" [Source: Tool Evaluation Prompt Analysis K102 URL 13 — paraphrase]
