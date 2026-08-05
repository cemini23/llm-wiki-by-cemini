---
title: LLM agent failure telemetry monitors (cheap ESN / escalation)
type: concept
tags: [concept, agents, harness, ccc, atto, k222]
keywords: [ESN, CUSUM, Mahalanobis, content-grounding, fabrication, SkillEval]
related:
  - entities/tools/gdpevo.md
  - sources/arxiv-2608.03836-resume-contract.md
  - sources/arxiv-2608.03779-agenticvau.md
  - sources/arxiv-2608.03764-gdpevo.md
  - sources/arxiv-2608.02464-llm-agent-failure-detection-repair.md
  - sources/arxiv-2608.02287-skt-skill-use-training.md
  - sources/arxiv-2608.02505-abduction-loop-representational-grounding.md
  - concepts/gpuology-genealogy-agent-kit.md
maturity: draft
created: 2026-08-04
updated: 2026-08-05
---

## Relations

- @entities/tools/gdpevo.md

- @sources/arxiv-2608.03836-resume-contract.md

- @sources/arxiv-2608.03779-agenticvau.md

- @sources/arxiv-2608.03764-gdpevo.md

- @sources/arxiv-2608.02464-llm-agent-failure-detection-repair.md — primary
- @sources/arxiv-2608.02287-skt-skill-use-training.md — verified skill trajectories (upstream quality)
- @sources/arxiv-2608.02505-abduction-loop-representational-grounding.md — abstention / adversarial verify kinship
- @concepts/gpuology-genealogy-agent-kit.md

## Raw Concept

Steal patterns for Mid-episode agent failure detection that do **not** require a second LLM judge on every step.

## Narrative

Dubey (2608.02464) stack: (1) one-class echo-state network + CUSUM on step telemetry; (2) calibrated ESN+Mahalanobis hybrid with regime-aware fusion; (3) content-grounding channel for corruption; (4) escalation / deterministic numeric grounding for fabrication (statistical monitors alone underpowered). Organic silent aborts caught by completion checks; commission/fabrication needs external reference.

Pair with **SKT** (2608.02287): verified skill-use trajectories reduce bad skill coordination upstream. For CCC/Atto harnesses: prefer cheap telemetry + HITL escalation over always-on LLM judges; recalibrate per deployment null.
