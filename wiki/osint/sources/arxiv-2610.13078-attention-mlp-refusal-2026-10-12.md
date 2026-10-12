---
title: "Attention sees, MLP refuses: the attention-to-MLP safety pathway (arXiv 2610.13078)"
type: source
tags: [source, k289, arxiv, safety, interpretability, refusal, agents]
keywords: [attention-mlp-pathway, harmfulness-recognition, refusal-writing, residual-stream-probing, sentinel, conditional-routing]
related:
  - concepts/k289-arxiv-wave.md
  - concepts/agent-safety-executable-evaluation.md
maturity: draft
created: 2026-10-12
updated: 2026-10-12
read_status: read
---

## Relations

- @concepts/k289-arxiv-wave.md
- @concepts/agent-safety-executable-evaluation.md

## Raw Concept

| Title | Attention Sees, MLP Refuses: Tracing the Attention-to-MLP Safety Pathway in LLMs |
| Authors | Zixuan Weng (Georgia Tech), Haoqi He, Yang Bai, Weifei Jin (Duke), Yue Huang (Notre Dame) |
| Type | arXiv preprint (cs.AI) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2610.13078-attention-sees-mlp-refuses-tracing-the-attention.pdf` |
| Retrieved | 2026-10-12 |
| arXiv | 2610.13078v1 |
| read-status | read |

## Narrative

Reframes alignment failure as a **pathway** problem: **recognition** of harm is separate from the **computation that writes refusal**.

### The finding

Residual-stream probing across **18 Base–Instruct pairs** (Qwen, Llama, Gemma):

- **Attention updates carry harmfulness** — especially in early layers.
- **MLP updates write refusal** — concentrating deeper after post-training.

**Causal test:** resetting downstream MLP updates **reduces the refusal shift** caused by upstream attention edits. So the two stages are separable, not one behaviour.

### The tool — Sentinel

Two scores: **perception P** (an attention harmfulness-probe logit) and **decision D** (MLP refusal writing), with **conditional routing on both**. Joint P–D routing **beats single-signal routing and fixed reminders across 8 models** on aggregate error. The pattern holds in all 18 pairs and in **6 reasoning models** (refusal writing peaks at answer onset).

### Why it matters here

A **mechanistic handle for the safety lane**: **a model can recognise harm and still not refuse.** That distinction — perception vs decision — is the same seam the wiki's verifier and gate threads keep finding. Relevant to jailbreak-vs-over-refusal diagnosis on the local lab. **No PoC.**

## Snippets

> "Attention updates carry harmfulness (especially early layers); MLP updates write refusal (concentrating deeper after post-training)." [Source: arxiv-2610.13078-attention-sees-mlp-refuses-tracing-the-attention.pdf]

> "Joint P–D conditional routing beats single-signal routing and fixed reminders across 8 models." [Source: arxiv-2610.13078-attention-sees-mlp-refuses-tracing-the-attention.pdf]
