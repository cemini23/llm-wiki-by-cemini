---
title: "Repository Revenue Opportunity Analysis (2026-07-19)"
type: source
tags: [source, tool-eval, k174]
keywords: [k174, code-review-graph, i-have-adhd, wigolo]
related:
  - concepts/wiki-tooling-evaluation.md
  - concepts/cemini-license-posture.md
  - entities/tools/code-review-graph.md
  - entities/tools/i-have-adhd.md
  - entities/tools/wigolo.md
  - entities/tools/ktransformers.md
maturity: draft
read_status: read
created: 2026-07-19
updated: 2026-07-19
clusters: [k174-ingest]
---

## Relations

- @concepts/wiki-tooling-evaluation.md
- @concepts/cemini-license-posture.md
- @entities/tools/code-review-graph.md · @entities/tools/i-have-adhd.md
- @entities/tools/wigolo.md · @entities/tools/ktransformers.md

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Repository Revenue Opportunity Analysis |
| **Type** | Gemini tool-eval docx (20 URLs) |
| **sha256** | `88ed406f9c7b010705aab7292d391731f9e0781e9633e5c75cfa4c7290a3219e` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/Repository Revenue Opportunity Analysis.docx` |
| **retrieved** | 2026-07-19 |

## Narrative

20-URL developer-tools / agent batch. **Licenses verified via `gh api` + LICENSE files (never trust docx alone).**

| Tier | Item | Verified license | Cemini decision |
|------|------|------------------|-----------------|
| Extract | tirth8205/code-review-graph | MIT (~16MB clone) | CCC/TipDrop/XSP — AST blast-radius MCP |
| Extract | ayghri/i-have-adhd | MIT (~0.3MB) | CCC/TipDrop — action-first Claude skill |
| Extract→**Pass** | KnockOutEZ/wigolo | **AGPL-3.0** (K173 verified) | Eval said Extract; AGPL blocks SaaS — Pass |
| Watch | kvcache-ai/ktransformers | Apache-2.0 | Already K173; weights → David PC |
| Watch | GLM 5.2 quant / DGX Spark | NOT FOUND | David PC hardware Watch — no Mac download |
| Context | jamiepine/voicebox | MIT (~108MB) | CCC Context only — no clone this batch |
| Context | github/copilot-sdk, jcode, zapret-discord | MIT / mixed | CCC/cybersec Context |
| Context | unsloth gemma-4 GGUF | Gemma terms | David PC Watch — no Mac weight download |
| Pass | terminal, build-your-own-x, cs-self-learning, lime, textmate, a11y tools, jellium | various | Already covered / no revenue hook |

**Combo:** code-review-graph + i-have-adhd = low-token / action-first agent loop for TipDrop + xsp.
