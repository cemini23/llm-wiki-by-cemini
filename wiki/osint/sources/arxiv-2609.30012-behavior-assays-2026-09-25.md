---
title: "Low-Cost Assays for Model Behavior Across Vendors"
type: source
tags: [arxiv, source, k272, harness]
keywords: [k272, behavior-assays, coding-atlas, modelun, cross-vendor]
related:
  - concepts/k272-harness-evolution-wave.md
  - entities/tools/modelun.md
maturity: draft
created: 2026-09-25
updated: 2026-09-25
read_status: skimmed
---

## Relations

- @concepts/k272-harness-evolution-wave.md
- @entities/tools/modelun.md

## Raw Concept

| Paper | arXiv:2609.30012 |
| File | `arxiv-2609.30012-low-cost-assays-for-measuring-model-behavior-acr.pdf` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2609.30012-low-cost-assays-for-measuring-model-behavior-acr.pdf` |
| Archive | egress-fi 2026-09-25 |
| Authors | Tapan Parikh (Cornell Tech) |
| Retrieved | 2026-09-25 |
| Pages | 6 |
| Dual-ID | **OSINT K272** |
| sha256 | `94463b28bfd2611d95d7a7bb5603bb72589630b83ce1ef61bc544c950e8d41bc` |
| Code | coding-atlas SPDX null; modelun MIT SIZE-SKIP |

## Narrative

The paper runs one frozen public stimulus on a cross-vendor panel. The stated cost is a few dollars per model. Each study reads the transcripts in one of three ways: an exact match on a clamped reply, a codebook applied by LLM judges, or an instrumented environment that records what the agent did.

| Repo | gh api 2026-09-25 | Verdict |
|------|-------------------|---------|
| tap2k/coding-atlas | SPDX null, 7401 KB | **NO-CLONE** |
| tap2k/modelun | MIT, 21956 KB | **SIZE-SKIP.** Size still blocks the clone. `wont_wire` stays |

No clone this wave. The 2026-09-23 SPDX-null note on modelun is superseded by this gh api read. The size block does not change.

**Cemini posture:** FILE. Never auto-evolve skills. **0 product Integrate GO.**
