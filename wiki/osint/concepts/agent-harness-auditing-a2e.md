---
title: Agent harness auditing (A2E / ATP)
type: concept
tags: [concept, agent-harness, evaluation, k230]
keywords: [A2E, ATP, harness-audit]
related:
  - sources/arxiv-2608.07346-a2e-agent-auditing-2026-08-10.md
  - concepts/code-as-agent-harness.md
  - concepts/agentic-code-quality-gates.md
  - sources/eval-github-repository-evaluation-plan-2026-08-10.md
  - sources/arxiv-2608.09485-diffcoop-civic-2026-08-11.md
  - sources/arxiv-2608.09857-agentic-harnesses-robot-2026-08-11.md
maturity: draft
created: 2026-08-10
updated: 2026-08-20
---

## Relations

- @sources/arxiv-2608.07346-a2e-agent-auditing-2026-08-10.md
- @concepts/code-as-agent-harness.md
- @concepts/agentic-code-quality-gates.md
- @sources/eval-github-repository-evaluation-plan-2026-08-10.md

## Raw Concept

Pattern from A2E (2608.07346) — Agent Task Protocol + instrumented Monitor + multidimensional harness metrics beyond correctness.

## Narrative

A2E (Agent Auditing Engine) is a three-layer stack: **ATP** (Agent Task Protocol) so benchmarks and harnesses compose without pairwise adapters; an instrumented **Monitor** (OpenInference / OpenTelemetry spans) that records native traces; and **lifecycle-aligned evaluation** (planning, tool use, recovery, efficiency, safety — not correctness alone). Paper campaign: **23 benchmarks × 9 harnesses**. Correctness means across harnesses sat in a narrow band (~0.57–0.68) while planning / tool-use / runtime petals were much wider. **No single model–harness pair won every task** (GDPVal vs MMLU-Pro vs τ³-bench frontiers differ).

Repo `github.com/datamllab/A2E` is **MIT** (`gh api` 2026-08-20). CCC: steal the *metric set + ATP idea* as REFERENCE; **do not** swap `/route` or PATH `claude-ds` for A2E. Runtime `wont_wire` unless a later Phase-0 says otherwise. Pairs Osmani quality gates: worker ≠ verifier; score the trajectory, not the vibes.

[Sources: arXiv:2608.07346; https://github.com/datamllab/A2E (retrieved 2026-08-20)]
