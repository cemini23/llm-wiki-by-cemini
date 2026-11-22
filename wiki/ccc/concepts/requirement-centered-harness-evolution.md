---
title: "Requirement-centered harness evolution — merge on evidence, score afterwards"
type: concept
related:
  - sources/arxiv-agentic-harness-engineering-beta-2611.24924.md
  - concepts/harness-evolution-vs-test-time-scaling-baseline.md
  - concepts/continual-harness-online-self-improvement.md
  - concepts/failed-trajectory-harness-repair.md
  - concepts/measurement-gated-agent-harness-optimization.md
updated: 2026-11-22
---

## Raw Concept

Question this page answers: what should select a harness change, if not the benchmark score?

Synthesised from one source: `@sources/arxiv-agentic-harness-engineering-beta-2611.24924.md` (AHE-Beta, 2611.24924).

## Narrative

Automatic harness evolution usually has one agent edit the harness and the benchmark score pick the winner. The AHE-Beta paper argues this produces narrow patches that fit one benchmark.

Its alternative is a three-stage loop taken from ordinary software engineering:

1. **User-driven evaluation.** Simulated personas work with the harness over multi-turn sessions in a real repository. They file requirements as issues and rate the process, not the completion.
2. **Team-based modification.** Separate Triage, Architect, PM and Developer roles convert admitted requirements into a PRD, ordered tasks, and a PR.
3. **Requirement-driven selection.** A change merges only when it resolves a verified requirement and passes review.

The ordering is the point. No verifier runs during evolution. Benchmark scores are computed after the change lands, so they cannot select it.

Reported results: pass@1 rises from 21.9% to 33.3% with 40.8% fewer tokens, and the gain transfers to GLM-5.3 (+15.8%) and DeepSeek-V4.1-Flash (+5.3%) without further evolution. A blind human A/B prefers the result in 31 of 48 valid pairs. [TENTATIVE] all numbers are author-reported.

### Why transfer is the interesting part

A change selected by benchmark score overfits that benchmark. A change selected by a stated requirement can help a different model, because the requirement did not name a model. This is the test `@concepts/harness-evolution-vs-test-time-scaling-baseline.md` asks for.

For Cemini: `/route` and skill edits should cite the requirement they fix. "It scored better on one sweep" is not a requirement.

## Snippets

> "A change merges only when it resolves a verified requirement and passes review." [Source: arxiv-2611.24924-agentic-harness-engineering-beta-requirement-cen.pdf p.1]

> "Without further evolution, the gains transfer to GLM-5.3 and DeepSeek-V4.1-Flash with pass@1 improvements of 15.8% and 5.3% over Base Harness." [Source: arxiv-2611.24924-agentic-harness-engineering-beta-requirement-cen.pdf p.1]
