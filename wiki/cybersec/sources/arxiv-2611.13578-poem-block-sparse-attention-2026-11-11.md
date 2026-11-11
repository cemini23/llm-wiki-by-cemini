---
title: "POEM — output-relative block-sparse attention for long-context prefill"
type: source
tags: [source, arxiv, attention, long-context, efficiency, inference]
related: []
maturity: draft
read_status: skimmed
created: 2026-11-11
updated: 2026-11-11
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | POEM: Output-Relative Block-Sparse Attention for Long-Context Prefilling |
| Authors | Haoyi Wu, Yunkai Dang, Wanyu Zhang, Lei Wang, Wenbin Li (Nanjing University; University of Wollongong) |
| arXiv | 2611.13578 |
| Pages | 28 |
| Read status | skimmed (abstract) |

## Narrative

Long-context prefill is expensive, and **block-sparse attention** is the standard lever: keep only the most important key-value blocks.

The paper names the flaw in existing importance proxies. They estimate a block's contribution to the **dense attention output** — the attention-weighted value — and implicitly assume that **removing the block loses only that contribution.**

That assumption is wrong, and the paper's title says what to use instead: importance **relative to the output**. A block's marginal contribution depends on what the rest of the retained set already provides. A block that looks unimportant next to the full dense attention can be essential once other blocks are dropped.

### Why the proxy flaw is the general lesson

Every sparsification, pruning, or summarisation scheme faces the same question: **importance measured against the whole is not importance measured against what remains.**

A block that is redundant in the presence of ten others may be the only source once nine are gone. Proxy-based pruning systematically discards those.

That is the same error as judging a wiki page by how much it duplicates versus how much it is the only source for — and the same error as an eval that scores a tool against the full stack rather than against what the stack lacks.

**Caveat.** Abstract only. No accuracy or speedup figure reproduced.

## Snippets

> "These proxies generally estimate a block's contribution to the dense attention output (i.e., attention-weighted value), implicitly assuming that removing the block loses…" [Source: arxiv-2611.13578 p.1]

## Dead Ends

- **Citing a speedup.** Abstract only.
