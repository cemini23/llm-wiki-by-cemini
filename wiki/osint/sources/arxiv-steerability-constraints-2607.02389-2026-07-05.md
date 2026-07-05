---
title: "Steerability via constraints — coding-agent oversight substrate (arXiv 2607.02389)"
type: source
tags: [source, arxiv, agent-harness, coding-agents, security, k146]
keywords: [2607.02389, substrate constraints, backdoor detection, Gemma, docs CLI, scalable oversight]
related:
  - concepts/coding-agent-substrate-steerability.md
  - concepts/generator-verifier-inference-time-steering.md
  - concepts/probabilistic-agent-policy-verification.md
  - concepts/poker-arena-multi-axis-cognitive-profile.md
  - concepts/wiki-tooling-evaluation.md
maturity: draft
read_status: read
created: 2026-07-05
updated: 2026-07-05
clusters: [agent-harness, poker]
---

## Relations

- @concepts/coding-agent-substrate-steerability.md — K146 synthesis
- @concepts/generator-verifier-inference-time-steering.md — verifier/steering sibling line (K123)
- @concepts/probabilistic-agent-policy-verification.md — trajectory verification cluster
- @concepts/poker-arena-multi-axis-cognitive-profile.md — auditability axis for decide() harness

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Steerability via constraints: a substrate for scalable oversight of coding agents |
| **Author** | Thomas Winninger (Télécom SudParis, ENS Paris-Saclay) |
| **arXiv** | 2607.02389v1 (2026) |
| **sha256** | `0a12612bd1b9036ac44565cd187733cba2c0527c7ecbd887b04d9b99fccb7f3f` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2607.02389-2607-02389v1-steerability-via-constraints-a-subs.pdf` |
| **Retrieved** | 2026-07-05 daily digest + morning inbox restore |
| **Read status** | read (abstract, stance, experiment §5) |

## Narrative

Argues human oversight — not model capability — is the bottleneck for high-stakes coding agents. **Substrate constraints** (linters, type checkers, frozen pydantic models, VM/network isolation) are non-advisory: they refuse bad code before execution. Contrasts with prompt-only and heavy MCP retrieval, which bloat context and weaken review discipline.

Controlled 2×2 on 11 stratified Python backdoors: small reviewer (Gemma 4 e4b, 8B class) recall rises **54.5% → 90.9%** with constrained substrate plus ~200 LoC docs CLI (`docs module`, `docs symbol`, AST projection). Substrate and tools contribute independently.

For Poker Arena / CCC: steal the **projection-layer** pattern (topological map without raw implementation) for verifier prompts and sandbox audit CLIs — not the full security VM stack. Complements `@concepts/generator-verifier-inference-time-steering.md` with enforceable non-prompt guardrails.

## Snippets

> "Substrate constraints, in contrast, are not advisory: linters, type checkers, runtime contract validators, and frozen data classes … refuse to run code that violates them." [Source: arxiv-2607.02389 PDF §3.1 (retrieved 2026-07-05)]

> "Recall rises from 54.5% (unconstrained, no tools) to 90.9% (constrained substrate plus a 200 LoC docs CLI)." [Source: arxiv-2607.02389 PDF abstract (retrieved 2026-07-05)]
