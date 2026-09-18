---
title: "arXiv 2510.03215 — Cache-to-Cache (C2C) KV projection between LLMs"
type: source
tags: [source, k264, ccc, arxiv]
keywords: [k264, C2C, KV-cache, thu-nics]
related:
  - concepts/k264-ccc-harness-wave.md
  - concepts/k264-eval-github-wave.md
  - entities/tools/c2c.md
maturity: draft
created: 2026-09-18
updated: 2026-09-18
read_status: read
---

## Relations

- @concepts/k264-ccc-harness-wave.md
- @concepts/k264-eval-github-wave.md
- @entities/tools/c2c.md

## Raw Concept

| File | `2510.03215v2.pdf` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/2510.03215v2.pdf` |
| Retrieved | 2026-09-18 |
| Dual-ID | **OSINT K264** |
| sha256 | `8846282656963fc48f72596f2d26c5f9f59bd6cc30c0d832b9fbe03904a34990` |
| URL | https://arxiv.org/abs/2510.03215 |
| Pages | 29 |

## Narrative

Fu, Min, Zhang et al. (ICLR 2026). Cache-to-Cache projects and fuses a source LLM KV-cache into a target model instead of text-to-text handoff. Learnable gating selects target layers. Paper claims 6.4–14.2% higher average accuracy than individual models, ~3.1–5.4% over text communication, and ~2.5× latency speedup. Code at thu-nics/C2C. Apache-2.0 `[CONFIRMED]` gh api 2026-09-18 (~5MB). CCC FILE. **Do not swap `/route`. 0 Integrate GO.**

## Snippets

> C2C uses a neural network to project and fuse the source model’s KV-cache with that of the target model to enable direct semantic transfer. [Source: 2510.03215v2.pdf p.1]
