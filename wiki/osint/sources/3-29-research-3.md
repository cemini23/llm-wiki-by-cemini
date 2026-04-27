---
title: "Targeted Extraction Audit: Cemini Financial Suite Architecture"
type: source
tags: [docx, rl-marl, llm-agents, ml-methods, prediction-markets, cemini-internal, infrastructure, langgraph, gat, mappo, pytorch]
clusters: [rl-marl, llm-agents, ml-methods, prediction-markets, cemini-internal, infrastructure]
related:
  - concepts/rl-marl-research.md
maturity: validated
read_status: read-skim
created: 2026-04-23
updated: 2026-04-26
---

## Relations

- @concepts/rl-marl-research.md — cluster hub for RL/MARL research in the Cemini corpus

## Raw Concept

- **Original title**: Targeted Extraction Audit: Cemini Financial Suite Architecture
- **Author(s)**: Cemini internal research audit (no attributed author)
- **Type**: DOCX (internal)
- **Location**: research for cemini/3_29 research 3.docx
- **Length**: ~4721 words, 147 paragraphs
- **Retrieved**: 2026-04-23 (filename date 2026-03-29)
- **Read status**: read-skim
- **Primary cluster**: ml-methods
- **All clusters**: rl-marl, llm-agents, ml-methods, prediction-markets, cemini-internal, infrastructure

## Narrative

A "targeted extraction" style audit that surveys several external sources (LangGraph docs, PyTorch optimization guides, arXiv:2511.00039 Graph-Attentive MAPPO paper, others) and for each produces four deliverables: (1) what architectural patterns to extract, (2) what code/logic to study, (3) dev workflow/tooling wins, (4) what to explicitly not take and why. Each section ends with a verdict table.

Key extractions: (a) LangGraph `AsyncShallowRedisSaver` as the drop-in for the 5-agent Devil's Advocate cyclical orchestration, binding thread_id to Kalshi market tickers to isolate concurrent debates in Redis without cross-contamination; explicitly rejects `langgraph-checkpoint-postgres` and full RedisSaver (memory bloat vs 128GB). (b) PyTorch CPU patterns: gradient accumulation (simulate batch=128 with memory=8), `.item()` on loss tensors to prevent autograd graph retention, `torch.compile` inductor + max-autotune, `param.grad = None` over zero_grad, FX CPU profiler; explicitly rejects AMP/bfloat16 on CPU as counterproductive without AMX/AVX512. (c) Graph-Attentive MAPPO (arXiv:2511.00039, MIT-licensed): CTDE + GAT layer inside actor/critic, rolling-covariance-matrix-derived asset graph from TimescaleDB as edges, stability reward penalty on absolute relative step-over-step position change to regularize turnover — translates cleanly to Cemini; Common Random Numbers (CRN) for variance-controlled A/B evaluation in CI/CD.

Relevant to Cemini as a compact prescriptive digest of external sources. Honest limits: consulting-style "WHAT IT IS / WHAT'S NOT USEFUL" framing; effort estimates ("two hours", "three hours") are ungrounded; some recommendations are over-confident (e.g., dismissing the GAT paper's CatBoost oracle as "redundant" with Alpaca paper trading conflates offline RL demand simulation with live paper-trading — different purposes).

## Key findings

- LangGraph `AsyncShallowRedisSaver` is the prescribed checkpointer — only stores latest checkpoint (RAM-friendly), thread_id → Kalshi market ticker isolation.
- PostgreSQL checkpointer and full-history RedisSaver both rejected (overhead + 128GB ceiling).
- PyTorch CPU wins: gradient accumulation (batch=128 on RAM=8), `.item()` on logged loss tensors, `torch.compile(backend="inductor", mode="max-autotune")`, `param.grad = None`, FX CPU profiler.
- Mixed precision (bfloat16/fp16) explicitly counterproductive on CPUs without AMX/AVX512.
- Graph-Attentive MAPPO (arXiv:2511.00039v1, MIT license) — CTDE + single sparse GAT layer; asset graph from rolling TimescaleDB covariance matrix.
- Stability penalty reward = -coef × |Δprice / price| — directly translates to turnover/slippage regularization for Cemini portfolio weights.
- Common Random Numbers (CRN) for A/B evaluation — seeds identical env rollouts across baseline and experimental policies; CI/CD gate.
- MIT license explicitly flagged as IP-sale-safe.

## Snippets

- **Sec 1** — "the shallow variant is mandatory" — avoids storing full checkpoint lineage under 128GB RAM.
- **Sec 2** — "replacing the traditional model zero-gradient call with param.grad = None eliminates individual memory zeroing operations" — specific CPU memory bandwidth win.
- **Sec 2** — "Native mixed precision is engineered to leverage GPU Tensor Cores; applying bfloat16 or float16 indiscriminately on standard CPUs without native AMX or AVX512 support often degrades performance due to continuous casting overhead."
- **Sec 3 (MAPPO+GAT)** — "the profit and stability reward function… subtracts a stability penalty coefficient multiplied by the absolute relative price change between time steps" — reward logic directly portable.
- **Sec 3 CRN** — "the environment is seeded identically using CRN for both the baseline policy and the experimental policy across multiple rollouts. This mechanism ensures that performance deltas are strictly attributable to policy improvements."
