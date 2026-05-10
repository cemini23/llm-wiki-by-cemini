---
title: "Stirling PDF — Enterprise Document Processing Platform"
type: entity
tags: [tool, pdf, document-processing, deferred, license-verification]
keywords: [Stirling PDF, PDF processing, OCR, enterprise, license verification, AGPL risk]
related:
  - sources/evaluating-links-trading-wiki-stacks.md
  - concepts/tool-evaluation-framework.md
maturity: draft
created: 2026-05-10
updated: 2026-05-10
---

## Relations
- `@sources/evaluating-links-trading-wiki-stacks.md` — source evaluation brief (URL 19)

## Raw Concept

Enterprise-grade PDF processing platform (OCR, redaction, conversion, merging) designed for military/healthcare deployment environments. 25M+ downloads.

- **Site**: `stirling.com`
- **License**: Unknown — SPDX identifier not retrievable during evaluation
- **Stack**: Java/Spring, local LLM extraction models
- **Footprint**: Significant; designed for enterprise server deployment

## Narrative

**Verdict: Defer** — gated on license verification. The platform's capabilities (OCR, redaction, large-PDF manipulation) are directly useful for research PDF processing, but the license ambiguity is blocking. If the repo carries AGPL or PolyForm, it must be rejected. If MIT/Apache-2.0, re-evaluate for Workflow deployment only (too heavy for server surfaces).

[Source: Evaluating Links for Trading and Wiki Stacks.docx, URL 19]
