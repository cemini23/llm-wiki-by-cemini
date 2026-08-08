---
title: Cross-model KV cache transfer for prefill reuse
type: concept
tags: [inference, kv-cache, ccc, k228]
keywords: [cross-model KV, prefill, model cascade]
related:
  - sources/arxiv-2608.03893-cross-model-kv-cache-2026-08-08.md
  - concepts/code-as-agent-harness.md
maturity: draft
created: 2026-08-08
updated: 2026-08-08
---

## Relations

- @sources/arxiv-2608.03893-cross-model-kv-cache-2026-08-08.md
- @concepts/code-as-agent-harness.md

## Raw Concept

From NVIDIA arXiv 2608.03893 — closed-form mapping to reuse KV across same-family models.

## Narrative

Relevant when Cemini routes cheap→strong models mid-session. Measure tokenization/TTFT + harness cost (TokTier/HarnessOpt) before claiming savings. No deploy without dedicated GO.

[Source: arXiv:2608.03893]
