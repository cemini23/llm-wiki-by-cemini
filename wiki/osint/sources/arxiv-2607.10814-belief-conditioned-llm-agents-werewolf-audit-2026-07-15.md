---
title: "Auditing Belief-Conditioned LLM Agents in Hidden-Info Games (2607.10814)"
type: source
tags: [source, arxiv, poker, llm-agents, hidden-information, k167]
keywords: [Werewolf, belief layer, belief-action deviation, information isolation, offline improvement]
related:
  - concepts/belief-conditioned-agent-audit-hidden-info.md
  - concepts/hierarchical-bounded-agent-memory.md
  - concepts/generator-verifier-inference-time-steering.md
maturity: validated
read_status: deep-read
created: 2026-07-15
updated: 2026-07-15
clusters: [k167-ingest, poker]
---

## Raw Concept

| Field | Value |
|-------|-------|
| **arXiv** | [2607.10814](https://arxiv.org/abs/2607.10814) |
| **Authors** | Yuan Gao, Jiangyi Yang, Yao Zhao, Yichi Zhang (Melbourne) |
| **sha256** | `89b8b670fd17175428b1c8e3294c08f38df3a117c7088b254cc9c7165a9bde18` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2607.10814-auditing-belief-conditioned-llm-agents-in-hidden.pdf` |
| **Phase-0** | `scripts/adopt_k167_phase0.sh` (REFERENCE — no install) |

## Relations

- @concepts/belief-conditioned-agent-audit-hidden-info.md — K167 concept
- @concepts/hierarchical-bounded-agent-memory.md — complementary session-state caps

## Narrative

9-player Werewolf under **strict code-level information isolation**. External **belief layer** over hidden roles (shadow vs active injection); logs belief updates + **belief–action deviations**; defensive **offline** improvement loop (batch bad-case review before strategy change). 1,080 frozen games; A0/A1 active-belief associated with good-side win 0.205→0.390 (McNemar p<0.001) but **direct action–belief consistency ≈0.21** — do not claim causal belief-content benefit. Contribution = audit framework making high-noise hidden-info agents replayable.

**Steal for Poker Arena:** (1) external HUD/opponent-belief shadow vs `decide()` action; (2) deviation taxonomy (harmful / justified / strategic); (3) batch offline improvement — no single-hand online prompt rewrites; (4) isolation boundary for untrusted opponent streams.
