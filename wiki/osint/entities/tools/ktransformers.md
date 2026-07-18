---
title: "KTransformers"
type: entity
tags: [tool, k173]
keywords: [ktransformers]
related:
  - sources/eval-revenue-opportunity-url-evaluation-2026-07-18.md
  - concepts/wiki-tooling-evaluation.md
maturity: draft
created: 2026-07-18
updated: 2026-07-18
---

## Relations

- @sources/eval-revenue-opportunity-url-evaluation-2026-07-18.md
- @concepts/wiki-tooling-evaluation.md

## Narrative

| Field | Value |
|-------|-------|
| **Repo / docs** | kvcache-ai/ktransformers |
| **License** | Apache-2.0 (~64MB) |
| **Verdict** | **Extract** |
| **Routing** | PM/local MoE |

Optimized MoE/local serve stack. Extract patterns; shallow clone OK under 500MB.

## Wired (K173 local)

- Clone reference only on Darwin (CUDA-primary upstream)
- Note: `.local/reports/k173-ktransformers-use.md`

