---
title: "Scheduling Mixed RL Rollouts Beyond Prefix Locality"
type: source
tags: [arxiv, k233, ccc, rl-infra, routing]
keywords: [2608.11152, misa-t, rollout-scheduling, kv-cache, rlvr, rlhf, agentic-rollouts, vllm]
related:
  - concepts/agent-toolkit-routing-research-backlog.md
  - concepts/llm-routing-deepseek-openrouter-failover.md
maturity: draft
created: 2026-08-12
updated: 2026-08-12
read_status: skimmed
---

## Relations

- @concepts/agent-toolkit-routing-research-backlog.md
- @concepts/llm-routing-deepseek-openrouter-failover.md
- @ccc-wiki/briefs/2026-08-12_k233-skiller-rollout-scheduling.md (cross-wiki brief)

## Raw Concept

| Field | Value |
|-------|--------|
| arXiv | 2608.11152 |
| sha256 | `cf0da0a167051dee752cee4bc27c4f4df8b403d87c0b6253388cfc8126210cd0` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2608.11152-scheduling-mixed-rl-rollouts-beyond-prefix-local.pdf` |
| retrieved | 2026-08-12 |
| authors | Zetao Hong, Song Yuan, et al. (Nanjing Univ. State Key Lab, StepFun) |

## Narrative

Addresses the scheduling problem when **heterogeneous RL rollout workloads** (RLVR, RLHF, agentic rollouts) share an asynchronous inference service. Prefix-aware routing optimizes cache reuse but doesn't control how heterogeneous sessions compete for **KV-cache capacity** — RLVR/RLHF/agentic rollouts differ in sequence structure, interaction pattern, and KV-residency time.

**MISA-T** is a routing-layer admission policy combining adaptive session admission, workload-aware KV-capacity allocation, and residency-time-aware KV accounting. Results (Step3.7 and Qwen3.6-35B-A3B): rollout throughput +53.3% / +43.6% over a sweep-tuned cache-aware vLLM Router while keeping high prefix-cache hit rates; in a matched 50-iteration Step3.7 run, +35.6% rollout throughput and −22.8% mean iteration time with the consumed workload mixture near the trainer target.

Relevance: research-backlog bump for the agent-toolkit routing lane (llm-routing-deepseek-openrouter-failover). No direct prod wiring — MISA-T is RL-post-training infra, not a Cemini runtime concern, but the *workload-aware KV/priority admission* idea informs how a multi-model routing layer should treat heterogeneous agentic sessions (vs. purely latency/cache optimized).

[Source: arXiv:2608.11152]
