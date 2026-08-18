---
title: "HarnessEval-W — agentifying visual-world evaluation (arXiv 2608.16859)"
type: source
tags: [arxiv, ccc, game-dev, harness, k241]
keywords: [HarnessEval-W, world-model, evidence-tree, sub-agents]
related:
  - sources/arxiv-2608.16798-clawgym-ii-2026-08-18.md
  - concepts/harness-optimization-bench.md
  - concepts/game-dev-wiki-federation.md
  - entities/tools/cursor-route.md
maturity: draft
created: 2026-08-18
updated: 2026-08-18
read_status: read
---

## Relations

- @sources/arxiv-2608.16798-clawgym-ii-2026-08-18.md — black-box RL through harnesses
- @concepts/harness-optimization-bench.md — harness-level eval
- @concepts/game-dev-wiki-federation.md — visual-world eval prefers game-dev/CCC brief over OSINT stub farm
- @entities/tools/cursor-route.md — planner/reviewer still human

## Raw Concept

| Field | Value |
|-------|--------|
| Paper | arXiv:2608.16859, "HarnessEval-W: Agentifying the Evaluation of Visual Worlds" |
| Authors | Weiliang Chen, Haowen Sun, Jun Gao, et al. |
| Retrieved | 2026-08-18 |
| File | `arxiv-2608.16859-harnesseval-w-agentifying-the-evaluation-of-visu.pdf` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2608.16859-harnesseval-w-agentifying-the-evaluation-of-visu.pdf` |
| Type | cs.CV preprint |
| Code | https://github.com/mirros-lab/harnesseval-w |
| Dual-ID | **OSINT K241**. CCC / game-dev brief preferred over a new OSINT stub. |

## Narrative

A world-model benchmark should justify its score: did physics, causality, and world state evolve correctly? Existing metrics are brute-force scalars with no examinable chain. HarnessEval-W brings the **harness paradigm** to world-model eval: interpret the case, decompose into measurable subproblems, spawn specialized sub-agents with diagnostic tools, then have the parent validate evidence into a final verdict. Every evaluation becomes a **transparent evidence tree**.

Applied to **18 world models / 330 cases**. Judgments align with human preference and give fine-grained diagnoses. Live benchmark; community can add skills and cases.

**Steal `[TENTATIVE]`:** score is not enough — require an evidence tree. Same HITL instinct as ClawGym II and cursor-route: planner/parent validates; workers diagnose. Prefer CCC + game-dev brief; do not farm OSINT stubs per eval case.

## Snippets

> "Rather than applying a fixed rubric, HarnessEval-W interprets the context of each evaluation case, decomposes the evaluation question into measurable subproblems, and spawns specialized sub-agents" [Source: arxiv-2608.16859 abstract]
