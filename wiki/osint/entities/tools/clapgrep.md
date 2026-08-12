---
title: Clapgrep — Rust deep-file search CLI
type: entity
tags: [entity, tool, search, rust, gpl-3.0, atto-fit, k233]
keywords: [clapgrep, rust, cli, pdf-search, docx-search, atto, deep-search]
related:
  - sources/eval-url-revenue-opportunity-2026-08-12.md
  - concepts/atto-genealogy-agent-kit.md
maturity: draft
created: 2026-08-12
updated: 2026-08-12
---

## Relations

- @sources/eval-url-revenue-opportunity-2026-08-12.md — K233 eval, Extract tier
- @concepts/atto-genealogy-agent-kit.md

## Raw Concept

Repo `luleyleo/clapgrep`. GPL-3.0, ~274★. Fast Rust CLI searching inside text files, PDFs, and Office documents, reporting exact page/line numbers of matches.

## Narrative

**Verdict: GO Extract (Atto).** Deep search across sprawling genealogy archives for surnames / regional markers without a heavy OCR pipeline (works on text-layer PDFs). GPL-3.0 = high friction: **must run as an isolated CLI subprocess**, never static-linked into proprietary Atto binaries. Steal-from: the localized search + page/line-exact output pattern to route into Atto's M1 ingest shell scripts.

[Source: luleyleo/clapgrep (retrieved 2026-08-12)]
