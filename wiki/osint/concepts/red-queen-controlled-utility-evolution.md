---
title: Red Queen controlled utility evolution (RQGM pattern)
type: concept
tags: [concept, self-improvement, verifier, co-evolution, k134]
keywords: [RQGM, epoch, selective erasure, non-stationary utility, evaluator promotion]
related:
  - sources/arxiv-red-queen-godel-machine-2606.26294-2026-06-29.md
  - concepts/wiki-tooling-evaluation.md
  - concepts/generator-verifier-inference-time-steering.md
  - concepts/continual-harness-online-self-improvement.md
  - concepts/probabilistic-agent-policy-verification.md
  - concepts/poker-arena-multi-axis-cognitive-profile.md
  - concepts/code-as-agent-harness.md
  - concepts/llm-agent-systems.md
maturity: draft
created: 2026-06-29
updated: 2026-06-29
---

## Relations

- @sources/arxiv-red-queen-godel-machine-2606.26294-2026-06-29.md — K134 primary source
- @concepts/generator-verifier-inference-time-steering.md — inference-time verifier vs epoch-co-evolved judge
- @concepts/continual-harness-online-self-improvement.md — harness self-edit vs evaluator replacement

## Raw Concept

K134 ingest of arXiv **2606.26294**. Names the **Red Queen** problem for self-improving agents: fixed benchmarks go stale as agents improve. **Controlled utility evolution** makes evaluation part of the search loop without breaking monotonic improvement guarantees within each epoch.

## Narrative

### Core loop

1. **Epoch** — one evaluator frozen; all task-agent utility uses that judge (stationary subproblem).
2. **Challenger evaluators** — co-evolve in shared workspace; scored on held-out **ground-truth anchor**.
3. **Promotion** — at checkpoint, challenger replaces incumbent iff ε-best-belief on GT improves.
4. **Selective erasure** — discard utility records that depended on the displaced evaluator; re-score under new epoch judge.

### Distinctions

| Pattern | What moves | RQGM difference |
|---------|------------|-----------------|
| VERITAS (K123) | Generator filtered at inference | Evaluator fixed; no epoch promotion |
| Continual harness (2605.09998) | Prompt/code harness edits | Utility criterion external |
| Raeth nine-axis (K122) | Post-hoc scoring | Can become **epoch-local frozen rubric** in RQGM framing |
| MAFP self-play (K124) | Opponent policy | Opponent ≠ evaluator utility |

### Poker Arena steal [TENTATIVE]

Use **versioned rubric epochs** for Researcher sandbox: bump `sandbox_tri_verifier` schema version only when hold-out spot GT improves; erase leaderboard rows tied to prior rubric generation. Pairs with K132 tri-verifier harness and K131 Relaxed NFL trace formalization.

**Posture:** REFERENCE until RQGM code ships. Brief → `agents/devfun-poker-arena/briefs/`.

## Snippets

> "The utility can change only at epoch boundaries." [Source: arXiv:2606.26294 §3 (retrieved 2026-06-29)]

## Dead Ends

- Treating LLM-as-judge drift as noise only — RQGM argues **promote or erase**, not average over stale scores.
- Reward hacking on co-evolved judge without GT anchor — paper requires challenger beat incumbent on GT before promotion.
