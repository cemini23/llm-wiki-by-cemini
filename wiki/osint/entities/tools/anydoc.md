---
title: Anydoc — Rust doc-to-Markdown parser (Firecrawl)
type: entity
tags: [entity, tool, document-parsing, rust, mit, atto-fit, k233]
keywords: [anydoc, firecrawl, docx, pdf, markdown, rust, llm-ready, atto]
related:
  - sources/eval-url-revenue-opportunity-2026-08-12.md
  - concepts/atto-genealogy-agent-kit.md
maturity: draft
created: 2026-08-12
updated: 2026-08-12
---

## Relations

- @sources/eval-url-revenue-opportunity-2026-08-12.md — K233 20-URL eval, Integrate tier
- @concepts/atto-genealogy-agent-kit.md

## Raw Concept

Repo `firecrawl/anydoc` (formerly BaseBlocks-HQ/anydoc). MIT, 14,856★, ~0.7MB, active (pushed 2026-08-10). Rust library + CLI + Node.js/Python bindings + WebAssembly + an Agent Skill (`npx skills add firecrawl/anydoc`). Converts Word, PowerPoint, Excel, OpenDocument, RTF, EPUB, CSV, PDF → GitHub-Flavored Markdown in single-digit milliseconds, fully local.

## Narrative

**Verdict: GO Integrate (Atto).** Solves Atto's unstructured-document ingestion bottleneck: text-layer PDFs, DOCX, XLSX (civil-record scans where a text layer exists, FamilySearch export packets, comune correspondence) normalize to one predictable Markdown format that feeds the M1–M14 ingest modules. Zero-dependency local Rust binary — no data leaves the machine, consistent with Atto's local-first posture.

**Critical caveat — this is NOT an OCR/HTR tool.** It reads internal byte structures and ignores rasterized images. Italian civil records are typically *scanned* images (Antenati/FamilySearch cassettes) with no text layer — those still require the HTR path (Transkribus, per Atto constraints). Use anydoc for born-digital / text-layer PDFs + structured office files; keep a fallback branch for flattened archival scans.

Ship note: GFM output preserves merged table cells, nested list counters, footnotes — good for mapping civil-record tables into structured constraints. Adopt as a subprocess/binding dependency (MIT allows embedding; Rust core, use Node/Py bindings or the CLI).

[Source: firecrawl/anydoc README (retrieved 2026-08-12)]
