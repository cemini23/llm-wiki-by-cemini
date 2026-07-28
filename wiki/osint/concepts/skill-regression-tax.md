---
title: Skill regression tax — skills help and hurt agent success
type: concept
tags: [concept, agent-skills, harness, evaluation, k196]
keywords: [regression tax, residual failure, skill self-play, before-after matrix]
related:
  - sources/arxiv-2607.22520-regression-tax-llm-skills.md
  - sources/arxiv-2607.22529-skill-self-play.md
  - sources/arxiv-2607.22511-causalforge-lean-causal-research.md
  - sources/arxiv-2607.21936-historical-doc-rag-restoration.md
  - sources/substack-rss-klement-2026-07-27-graduating-in-the-age-of-ai.md
  - concepts/code-as-agent-harness.md
  - concepts/harness-updating-vs-benefit-nonmonotonic.md
  - concepts/cemini-wiki-ingest-workflow.md
  - concepts/continual-harness-online-self-improvement.md
  - concepts/gpuology-genealogy-agent-kit.md
  - concepts/computational-genealogy-archival-automation.md
  - concepts/verifier-deployment-gap.md
  - sources/arxiv-2607.24300-self-authored-verification.md
maturity: draft
created: 2026-07-27
updated: 2026-07-28
clusters: [k196-ingest]
---

## Relations

- @sources/arxiv-2607.24300-self-authored-verification.md — K198

- @concepts/verifier-deployment-gap.md — K198 sibling failure mode

- @sources/arxiv-2607.22520-regression-tax-llm-skills.md — primary K196 paper
- @sources/arxiv-2607.22529-skill-self-play.md — co-evolve only behind regression gates
- @sources/arxiv-2607.22511-causalforge-lean-causal-research.md — machine-checkable acceptors > LLM-as-judge
- @sources/arxiv-2607.21936-historical-doc-rag-restoration.md — Atto/HTR skill surface inherits same tax
- @sources/substack-rss-klement-2026-07-27-graduating-in-the-age-of-ai.md — labor incidence parallel (skills ≠ even gains)
- @concepts/code-as-agent-harness.md
- @concepts/harness-updating-vs-benefit-nonmonotonic.md
- @concepts/cemini-wiki-ingest-workflow.md
- @concepts/continual-harness-online-self-improvement.md
- @concepts/gpuology-genealogy-agent-kit.md — Atto MCP/skills allowlist
- @concepts/computational-genealogy-archival-automation.md

## Raw Concept

Average task-success after adding procedural skills hides a **regression tax**: tasks that were solved without skills and fail after skills are added. Residual failures (fail both ways) are a different bucket. Empirically (arXiv 2607.22520, ~6k runs), top skills win mainly by **regressing less**, not by unlocking more new wins.

## Narrative

### Operator rule (Cemini / Atto / CCC)

1. Treat every new Cursor skill / MCP tool / Atto allowlist entry as a **harness change**, not a free upgrade.
2. Require a small **before/after matrix** on a fixed task set (even 10–20 cases) before Promote.
3. Pair Skill Self-Play / auto-skill generation with the same gate — co-evolution without regression accounting pollutes the loop (same failure mode as unreliable LLM reviewers in CausalForge).
4. Aligns with harness-updating non-monotonicity: more harness surface ≠ more benefit.

### Out of scope

Do not confuse with retracted `skill-vetting` ledger fiction — this is empirical evaluation posture, not a Postgres registry.
