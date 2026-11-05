---
title: "pagesift — document-to-Markdown engine (AGPL-3.0, not 'not found')"
type: entity
tags: [tool, extraction, pdf, markdown, agpl, licence-trap]
keywords: [pagesift, document extraction, firecrawl compatible, jina reader, mcp, rust, agpl]
related:
  - sources/eval-multi-wiki-link-revenue-v10-11-2026-11-05.md
maturity: draft
created: 2026-11-05
updated: 2026-11-05
---

## Raw Concept

Surfaced by @sources/eval-multi-wiki-link-revenue-v10-11-2026-11-05.md, URL 17, **Extract** tier. Routed to Collectibles, Atto, and CCC.

The question this page answers: **can a local extractor replace a paid extraction API, and at what licence cost?**

## Narrative

### What it is

A self-hosted document-and-page-to-Markdown/JSON engine for agents, shipped as a **single Rust binary**. 229 stars, 614 commits.

Coverage is unusually broad:

| Class | Formats |
|-------|---------|
| Web | URLs, HTML |
| Documents | PDF (with OCR for scanned pages), Word, Excel, PowerPoint, OpenDocument, RTF, WordPerfect, HWP |
| E-books | EPUB, MOBI, FB2 |
| Mail and archives | .eml, .mbox, .msg; zip, tar, gz, bz2, xz, 7z |
| Data and text | SQLite, dBASE, CSV, Markdown, "373 source-code and config languages", WARC |

It serves **Firecrawl v1/v2 and Jina Reader-compatible routes** locally, exposes an MCP server and a `/v2/agent` endpoint, and renders JavaScript only when that actually adds content.

The pitch is that it replaces a metered SaaS extraction API with a local binary. For a pipeline converting thousands of scanned comp listings or archival PDFs, that is a real cost argument.

### Phase-0, 2026-11-05 — the licence is the finding

**The report records the licence as "NOT FOUND — verify license in repository root before deploying binary."**

It is **AGPL-3.0**, with a commercial licence available for proprietary use.

That changes the routing completely. The report sends it to **Collectibles** and **Atto**, both of which have commercial SKUs and one of which (game-time) runs a zero-copyleft rule. **AGPL cannot go into either as a dependency.**

It is usable in exactly two ways:

1. **As an operator-side tool** on loopback, never shipped, never offered as a service.
2. **Under the commercial licence**, which is a purchase decision rather than a technical one.

### The caveat worth noting

OCR works on **scanned pages inside PDFs, not standalone images** — even though image files appear in the input-type list. For a Collectibles pipeline that scans card fronts, that distinction matters: a PDF of scans works, a folder of JPEGs does not.

### What to take

The idea of a **local, Firecrawl-compatible endpoint** is genuinely good — it means an existing extraction pipeline can point at `localhost` instead of a paid API without a rewrite.

But the licence means you would be building a dependency on AGPL software, and the alternative is a commercial purchase. Neither is a casual adopt.

**For Atto specifically:** an archival-PDF pipeline is exactly where this would help, and exactly where ban 4 makes a cloud extractor unacceptable. A local AGPL binary solves the privacy question and creates a licence one.

### Status

Extract, **operator tool or paid licence only**. Not a dependency.

## Snippets

> pagesift is **AGPL-3.0**, "with an option to buy a commercial licence for proprietary use". [repository page, fetched 2026-11-05]

> The README says OCR works on scanned pages inside PDFs, "not standalone images". [fetched 2026-11-05]

## Dead Ends

- **Treating the licence as unknown.** It is AGPL-3.0 and that disqualifies it from commercial builds.
- **Assuming image files are OCR'd.** PDFs only, per the README.
