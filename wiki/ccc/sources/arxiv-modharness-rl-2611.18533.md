---
title: "ModHarness-RL: Recasting Harnesses as Learnable and Evolving Programs (2611.18533)"
type: source
maturity: draft
related:
  - concepts/learnable-agent-harness.md
updated: 2026-11-16
read_status: read
---

## Raw Concept

- **Title:** ModHarness-RL: Recasting Harnesses as Learnable and Evolving Programs for Agentic RL
- **Authors:** Zelin He, Siyu Zhu, Jacob Helwig et al. (Penn State, LinkedIn, UCSB)
- **Type:** arXiv preprint, cs.AI
- **Location:** `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2611.18533-modharness-rl-recasting-harnesses-as-learnable-a.pdf`
- **Retrieved:** 2026-11-16
- **arXiv:** 2611.18533
- **Read status:** full — 27 pages extracted 2026-11-16

## Narrative

Most agentic RL trains the model under a hand-written harness that stays fixed. The paper argues the harness depends on domain, data and model, and changes as the model trains — so the harness itself should be learned.

The construction: record the interaction as structured state (typed blocks), then express two harness components as programs over those blocks. A compression program assembles accumulated history into the model's context; a steering program supplies guidance when behaviour deviates. During RL, candidate programs are proposed from recent trajectories, verified by execution, and replayed over past trajectories.

Evaluation: CodeSearch in depth, plus ALFWorld and BIRD SQL, with models from 1.5B to 8B. The learned compression and steering components improve held-out performance over the fixed-harness baseline in most settings.

Directly relevant to the harness-tuning question in this workspace: the finding is that context assembly and deviation guidance are learnable parameters, not fixed scaffolding.

[Source: arxiv-2611.18533-modharness-rl-recasting-harnesses-as-learnable-a.pdf]

## Snippets

> "a COMPRESSION program that assembles the accumulated history into the model's context and a STEERING program that supplies guidance when behavior deviates."

## Dead Ends

- **Full-read note (2026-11-16):** The harness is learned as programs over structured state, proposed from recent trajectories and verified by execution; improvement holds in most, not all, settings. [Source: arxiv-modharness-rl-2611.18533.md full text, 27pp]
