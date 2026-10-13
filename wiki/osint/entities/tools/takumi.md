---
title: takumi — JSX/HTML/CSS to OG image and paged PDF in pure Rust
type: entity
tags: [tools, rendering, pdf, rust, dev-tooling]
keywords: [takumi, jsx-render, og-image, paged-pdf, rust, no-headless-chrome]
related:
  - sources/eval-url-revenue-opportunity-2026-10-13.md
  - concepts/k290-eval-wave.md
  - entities/tools/html-effectiveness-pattern.md
maturity: draft
created: 2026-10-13
updated: 2026-10-13
wire_status: deferred
---

## Relations

- @sources/eval-url-revenue-opportunity-2026-10-13.md
- @concepts/k290-eval-wave.md
- @entities/tools/html-effectiveness-pattern.md

## Raw Concept

**What prompted this page:** K290 tool eval (2026-10-13), entry 15 — **Integrate tier**. `github.com/kane50613/takumi`.

## Narrative

Renders **JSX / HTML / CSS** to **OG (Open Graph) images** and **paged PDF**, in **pure Rust**, **without headless Chrome**. The value is the removed dependency: no browser binary in the render path, so no Chrome deploy, no per-render browser process, and a much smaller attack surface.

**License:** **MIT OR Apache-2.0** — `[CONFIRMED]`.

**Docx tier: Integrate** (high value, now) — *"faster Atto client PDF binders / share-card conversion."*

**Why it matters here:** the workspace already treats **HTML as the output medium** for client-facing artifacts (`@entities/tools/html-effectiveness-pattern.md`). `takumi` is a **rendering primitive** for that pipeline: HTML in, **print-ready PDF or share card** out, deterministic and dependency-light. Pairs with the existing `@entities/tools/typst.md` and `@entities/tools/stirling-pdf.md` pages as an alternative PDF path.

**Phase-0 status:** not run — licence confirmation and clone require the **Terminal panel**.

## Snippets

> Render JSX/HTML/CSS to OG images + paged PDF in pure Rust (no headless Chrome). [Source: Repository Revenue Opportunity Analysis.docx — entry 15]
