---
title: "CLIFT: Conformal self-verification for web agent training and test-time scaling (arXiv 2610.06829)"
type: source
tags: [source, k283, arxiv, agents, eval, verification, conformal]
keywords: [clift, conformal-prediction, web-agent, grpo, verifier, test-time-scaling, mondrian]
related:
  - concepts/k283-arxiv-wave.md
  - concepts/agent-tool-use-verification.md
  - entities/tools/llm-as-a-verifier.md
maturity: draft
created: 2026-10-06
updated: 2026-10-06
read_status: read
---

## Relations

- @concepts/k283-arxiv-wave.md
- @concepts/agent-tool-use-verification.md
- @entities/tools/llm-as-a-verifier.md

## Raw Concept

| Title | CLIFT: Conformal Self-Verification for Web Agent Training and Test-Time Scaling |
| Authors | Zhang, Dai, Prabhu, Hu, Xu, Chen (Salesforce AI Research) |
| Type | arXiv preprint (cs.CL) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2610.06829-clift-conformal-self-verification-for-web-agent.pdf` |
| Retrieved | 2026-10-06 |
| arXiv | 2610.06829v1 |
| read-status | read |

## Narrative

An LLM judge is expensive and noisy. CLIFT turns judge feedback into a **reusable, judge-free verifier** for web agents, and uses it for both training and test-time selection.

### Method

Build a **bank of URL-scoped verification questions**. Each question q carries a URL pattern π_q and a polarity σ_q ∈ {−1, 0, +1}. The verifier score is

    R^VQ_i(u) = Σ_q w^q_{τ★} · 1[y = YES] ∈ [−1, 1]

A **Compositional Conformal Certifier** runs a **Mondrian-ACI** tracker per URL tier (global / host / URL-path), giving trust weight

    w^q_τ = σ_q · |lift| · max(0, 1 − α/α⋆)

Training reward: **r̃ = r_judge + β · max(0, R^VQ)** — the verifier term only ever *adds*, never subtracts. Advantages are URL-stratified. At test time, **Conformal Trajectory Selection** uses a conservative majority vote (m = 3) over greedy and diverse rollouts.

### Results

- **WAI 9-app:** CLIFT + CTS = **74.6%**. Base Gemma-4 61.8, vanilla GRPO 64.7, Opus 4.6 69.8, Gemini 3 Flash 70.1.
- **VWA:** GPT-5.5 + CTS (K=4) 53.7 vs WALT 52.9.
- **OM2W:** GPT-5.5 high 49.7 → **61.0 (+11.3 pp) at K=4, with zero policy training.**

### Why it matters here

The **+11.3 pp with zero training** is the striking result: conformal self-verification buys accuracy at test time without touching weights. The pattern — a certified question bank, a lift-weighted score, additive-only reward — is a concrete recipe for the `agent-tool-use-verification` and `llm-as-a-verifier` threads. Route to CCC and cybersecurity (agent-eval lane).

**No license stated (preprint); no code.**

## Snippets

> "On OM2W, GPT-5.5 high improved from 49.7 to 61.0 (+11.3 pp) at K=4 with zero policy training." [Source: arxiv-2610.06829-clift-conformal-self-verification-for-web-agent.pdf]

> "r̃ = r_judge + β · max(0, R^VQ) — the verifier term only ever adds, never subtracts." [Source: arxiv-2610.06829-clift-conformal-self-verification-for-web-agent.pdf]
