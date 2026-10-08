---
title: "Learning to Act with Task Progress: distilling small agents (arXiv 2610.10332)"
type: source
tags: [source, k285, arxiv, agents, distillation, alfworld]
keywords: [task-progress-distillation, tpd, alfworld, small-agent, stage-action-scoring, qwen3]
related:
  - concepts/k285-arxiv-wave.md
  - concepts/agent-tool-use-verification.md
maturity: draft
created: 2026-10-08
updated: 2026-10-08
read_status: read
---

## Relations

- @concepts/k285-arxiv-wave.md
- @concepts/agent-tool-use-verification.md

## Raw Concept

| Title | Learning to Act with Task Progress: Distilling Small Agents from Compact Teacher Supervision |
| Author | Wenxi Gan (City University of Hong Kong; Shenzhen Loop Area Institute) |
| Type | arXiv preprint (cs.CL) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2610.10332-learning-to-act-with-task-progress-distilling-sm.pdf` |
| Retrieved | 2026-10-08 |
| arXiv | 2610.10332v1 |
| read_status | read |

## Narrative

**Task-Progress Distillation (TPD):** train a small agent by pairing each demonstrated action with a **compact task-stage label**, and learn to **score stage–action pairs** — instead of imitating long reasoning chains.

### Method

A frozen annotator assigns a stage `s_t = f(g, h_t) ∈ {locate, transform, deliver}`. The student trains with a completion-only SFT loss. At execution it scores candidate pairs `q_θ(s, a | h_t)` and picks `(ŝ, â) = argmax` over **3N** stage–action pairs; a **deterministic harness** executes the choice.

### Results (ALFWorld, Qwen3-1.7B)

- **TPD 72.4%** unseen success at 404 demos, **76.9%** at 808.
- At only **200 demos: TPD 67.7% vs action-only 48.0% (+19.7 pp)** — the low-data win.
- A reasoning-trained student: **5.0%** free-generation vs **48.3%** constrained.
- Teacher reference 88.1%. A **shuffled-stage control** drops seen success 55.2% → 37.6% — the stage label carries real signal.

### Why it matters here

A **small-agent recipe that beats imitation in the low-data regime** by giving each action a *progress* label, then **scoring** rather than generating. The "deterministic harness executes the choice" boundary is the same separation the wiki keeps pushing. **No code stated.** Route: CCC.

## Snippets

> "At 200 demos TPD 67.7% vs action-only 48.0% (+19.7 pp)." [Source: arxiv-2610.10332-learning-to-act-with-task-progress-distilling-sm.pdf]

> "Shuffled-stage control drops seen success 55.2%→37.6%." [Source: arxiv-2610.10332-learning-to-act-with-task-progress-distilling-sm.pdf]
