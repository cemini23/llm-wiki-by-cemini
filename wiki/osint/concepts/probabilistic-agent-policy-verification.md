---
title: Probabilistic agent policy verification (trajectory risk bounds)
type: concept
tags: [concept, verifier, security, agents, k125]
keywords: [probabilistic verification, Datalog, derivation graph, DRO, trajectory risk, reference monitor]
related:
  - sources/arxiv-probabilistic-agent-verification-2606.20510-2026-06-21.md
  - sources/arxiv-relaxed-nfl-auto-formalization-2606.24443-2026-06-26.md
  - sources/arxiv-rlvf-formally-verified-law-2606.23913-2026-06-26.md
  - concepts/generator-verifier-inference-time-steering.md
  - concepts/red-queen-controlled-utility-evolution.md
  - concepts/rlvf-verifier-feedback-training.md
  - concepts/relaxed-nfl-auto-formalization.md
  - concepts/code-as-agent-harness.md
  - concepts/devfun-poker-agent-challenge-2026.md
  - concepts/poker-arena-multi-axis-cognitive-profile.md
  - concepts/llm-agent-systems.md
  - concepts/kuhn-poker-sft-curriculum-reference.md
maturity: draft
created: 2026-06-21
updated: 2026-06-26
---

## Relations

- @sources/arxiv-probabilistic-agent-verification-2606.20510-2026-06-21.md — Google DeepMind paper (K125)
- @concepts/generator-verifier-inference-time-steering.md — pointwise Best-of-N (K123) vs trajectory bound (K125)
- @concepts/code-as-agent-harness.md — deterministic harness tests as zero-error predicates

## Raw Concept

K125 ingest of arXiv **2606.20510**. Formalizes **probabilistic reference monitors** for tool-using agents: compile multi-step traces into a derivation graph; bound **global unsafe-state probability** with distributionally robust optimization when individual classifiers (PII, declassifiers) have known error rates and **unknown correlations**.

## Narrative

### Mechanism

1. **Trace → Datalog derivation graph** — each tool call maps to Propagate / Merge / Declassify / CreateClean / CreateTainted semantics.
2. **Marginal bounds** — upstream detectors supply ℓᵥ, uᵥ per atomic predicate (not point thresholds discarded at each step).
3. **Global risk R\*** — maximize consistent joint measure subject to transition constraints → **sound upper bound** on entering unsafe set U.
4. **Monitor decision** — block/allow proposed action when R\* exceeds global safety threshold.

### Contrast with K123 VERITAS

| Layer | VERITAS (2606.18247) | Probabilistic verification (2606.20510) |
|-------|----------------------|----------------------------------------|
| Unit | Single-step candidate ranking | Multi-step trajectory |
| Uncertainty | Visual verifier score | Noisy predicate marginals + correlation-robust bound |
| Output | Argmax action | Allow/block + risk certificate |

### Cemini steal list [TENTATIVE]

| Agent surface | Predicate examples | Trajectory unsafe set |
|---------------|-------------------|------------------------|
| Poker `decide()` | Legality oracle ε=0; MC equity estimator variance; M₈ regex false-positive rate | Cumulative lines violating regression + axis floor over hand |
| MCP / conductor | Tool allowlist classifier; path sandbox | Exfiltration / forbidden write chain |
| Prod brief staging | `skill_audit.py` veto gates | Ship brief with uncited NEEDS VERIFICATION |

**Posture:** REFERENCE — no Google code release. Poker brief stages **conservative trajectory gate** prototype (sum of per-street verifier failures capped before submit).

## Snippets

> "Forcing continuous probabilities into binary choices prematurely discards the exact context needed to guide enforcement decisions." [Source: arXiv:2606.20510 §1 (retrieved 2026-06-21)]

## Dead Ends

- Full Datalog monitor on Arena action clock — complexity vs latency [NEEDS VERIFICATION 2026-06-21].
- Treating independent MC sims as exact marginals — paper requires explicit ℓ/u bounds per predicate.
