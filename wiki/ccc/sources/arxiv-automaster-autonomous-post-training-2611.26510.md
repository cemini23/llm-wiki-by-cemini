---
title: "AutoMaster — Skill-FT and the teacher-rollout shaping loop"
type: source
related:
  - concepts/skill-guided-teacher-rollout.md
  - concepts/skillhone-continual-skill-decision-history.md
  - concepts/curated-vs-self-generated-skills.md
  - concepts/agent-skills-taxonomy.md
updated: 2026-11-22
read_status: read
maturity: draft
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | AutoMaster: Autonomous Post-Training by Making the Same Model a Better Teacher |
| Author | Guoxin Chen, Shuang Sun, Fanzhe Meng et al. (Renmin University of China) |
| Type | arXiv paper (cs.CL), 2611.26510 |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2611.26510-automaster-autonomous-post-training-by-making-th.pdf` |
| Retrieved | 2026-11-22 |
| Pages | 21 |
| Read status | read |

## Narrative

AutoMaster starts from a narrow claim: task success alone does not say which behaviours post-training should reinforce. A successful teacher trajectory can still contain unsupported assumptions, repetition, or superficial verification.

The method is **Skill-FT**. A natural-language skill guides the teacher's rollouts, suppressing bad habits and eliciting behaviours that were underrepresented. A target model is then fine-tuned on the resulting trajectories. An LLM agent develops the interventions through trajectory analysis, skill design, data selection, and feedback.

Reported gains over vanilla SFT on successful unguided teacher trajectories: +1.42 to +8.99 points, across Terminal, Search and software-engineering tasks with 4B and 9B targets, with teacher, task pool, training-set size and SFT recipe held fixed. On Terminal-Bench 2.1 the gain is +5.62 (4B) and +8.99 (9B).

A second finding is more surprising. Keeping the skill instructions inside the SFT data gives higher mean performance than removing them, in all six settings, even though the skills are absent at evaluation and the supervised outputs are identical.

For CCC the useful part is the skill-design loop, not the fine-tuning. A skill written as a behavioural instruction improves data far more cheaply than a weight update, and the skill can be audited and edited by a human. This is a second argument that skills belong in the harness layer. [TENTATIVE] single source.

## Snippets

> "Task success alone does not specify which behaviors post-training should reinforce." [Source: arxiv-2611.26510-automaster-autonomous-post-training-by-making-th.pdf p.1]

> "Retaining skill instructions during SFT yields higher mean performance than removing them across all six settings, despite their absence at evaluation and identical supervised outputs." [Source: arxiv-2611.26510-automaster-autonomous-post-training-by-making-th.pdf p.1]
