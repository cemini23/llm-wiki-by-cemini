---
title: "STEMBench — postdoc-level science problems scored by field figures of merit"
type: source
related:
  - concepts/specification-anchored-benchmark-anchors.md
  - concepts/benchmark-maintenance-debt.md
  - concepts/eval-integrity-minimum-standards.md
  - concepts/harness-as-eval-artifact.md
updated: 2026-11-22
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Benchmarking LLM Abilities on Postdoc-Level Natural Science Problems |
| Author | Alina Avanesyan, Alexey Boldyrev et al. (HSE University and partners) |
| Type | arXiv paper (cs.AI), 2611.24321 |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2611.24321-benchmarking-llm-abilities-on-postdoc-level-natu.pdf` |
| Retrieved | 2026-11-22 |
| Pages | 22 |
| Read status | read |

## Narrative

The paper starts from a benchmark-design question: scientific problems have no answer key, so what counts as a better solution must be decided before any agent runs.

STEMBench answers with the criterion each field already uses. Twelve research problems in high-energy physics, astrophysics and neuroscience are each scored by their community's figure of merit — from background rejection at fixed signal efficiency to coverage-penalised interval width.

Each problem carries two measured anchors, both from code shipped with the benchmark:

- a **floor** from a submission that uses no domain knowledge;
- a **ceiling** from an expert reference that reproduces a published method.

The interval between them shows how much of the problem requires scientific insight rather than engineering. Scores are read against that interval, not against a perfect score.

Results across eight frontier models: task-level wins and domain-level leadership dissociate. A model that wins five of twelve tasks leads no domain mean. In the high-effort comparison, at least one model beats the expert anchor on seven of twelve tasks. The five remaining tasks cover uncertainty estimation, latent and causal inference, and cross-site clinical classification.

The transferable methodology is the two-anchor design. A raw score hides how hard the task is. A floor and a ceiling make the score interpretable, and they come from code that can be re-run.

## Snippets

> "Each of its twelve research problems is scored by its own field's figure of merit, and each comes with two measured anchors: a submission that uses no domain knowledge, and an expert reference reproducing a published method." [Source: arxiv-2611.24321-benchmarking-llm-abilities-on-postdoc-level-natu.pdf p.1]

> "A model that wins five of the twelve tasks leads no domain mean." [Source: arxiv-2611.24321-benchmarking-llm-abilities-on-postdoc-level-natu.pdf p.1]
