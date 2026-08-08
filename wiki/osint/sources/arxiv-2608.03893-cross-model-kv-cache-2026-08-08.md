---
title: "arXiv 2608.03893 — Cross-model KV cache transfer (prefill reuse)"
type: source
tags: [arxiv, k228, ccc, inference]
keywords: [KV cache, cross-model, prefill, Qwen3]
related:
  - concepts/cross-model-kv-cache-transfer.md
  - concepts/code-as-agent-harness.md
maturity: draft
created: 2026-08-08
updated: 2026-08-08
read_status: skimmed
---

## Relations

- @concepts/cross-model-kv-cache-transfer.md
- @concepts/code-as-agent-harness.md

## Raw Concept

| Field | Value |
|-------|--------|
| Title | Cross-Model KV Cache Transfer in LLM Families |
| arXiv | 2608.03893 |
| sha256 | `27ed1e7447d4981136d39e133c249b3e34e7345460f1a1efcfa5f1a4c452dc2a` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/2608.03893v1.pdf` |
| Filename | 2608.03893v1.pdf |
| retrieved | 2026-08-08 |

## Narrative

Closed-form ridge mapper reuses source-model KV for a larger sibling in-family (matched heads/dims), skipping receiver prefill — cost-quality cascading / mid-conversation model swap. NVIDIA. **CCC / serving awareness** — no deploy claim; pairs harness/routing cost discipline.

[Source: arXiv:2608.03893]
