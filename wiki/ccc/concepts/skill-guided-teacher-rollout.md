---
title: "Skill-guided teacher rollouts — design the behaviour before you train it"
type: concept
related:
  - sources/arxiv-automaster-autonomous-post-training-2611.26510.md
  - concepts/skillhone-continual-skill-decision-history.md
  - concepts/curated-vs-self-generated-skills.md
  - concepts/agent-skills-taxonomy.md
  - concepts/agent-skills-progressive-disclosure.md
updated: 2026-11-22
maturity: draft
---

## Raw Concept

Question this page answers: how does a natural-language skill change what a model learns, without moving the policy first?

Synthesised from one source: `@sources/arxiv-automaster-autonomous-post-training-2611.26510.md` (AutoMaster / Skill-FT, 2611.26510).

## Narrative

AutoMaster starts from a narrow observation: a successful trajectory does not show which behaviours deserve reinforcement. A teacher can succeed with unsupported assumptions, repeated work, or a check that only covers one configuration.

**Skill-FT** injects a natural-language skill into the teacher's rollouts. The skill suppresses bad habits and elicits behaviours the teacher would not show by itself. The target model is then fine-tuned on the resulting trajectories. An LLM agent designs the skills through trajectory analysis, data selection and feedback.

Example from the paper: given a task to fix a pipeline that freezes on 100 records, the unguided teacher tests only the default worker count. With the skill "test where the solution might fail", the teacher tries several worker counts.

Reported effect: +1.42 to +8.99 points over vanilla SFT in all six settings, with teacher, task pool, training-set size and SFT recipe held fixed.

### The surprising result

Keeping the skill text inside the training data helps, in all six settings, even though the skill is absent at evaluation and the supervised outputs are identical. The skill context appears to help behavioural internalisation.

### Why CCC cares

The skill is the cheap, auditable lever. A human can read and edit a skill; a weight delta cannot be read. Before any fine-tune, write the behaviour as a skill and check whether the harness already improves.

Caveat: the paper targets post-training, which is outside Cemini's daily path. The transferable part is the skill-design loop. [TENTATIVE]

## Snippets

> "Task success alone does not specify which behaviors post-training should reinforce." [Source: arxiv-2611.26510-automaster-autonomous-post-training-by-making-th.pdf p.1]

> "Retaining skill instructions during SFT yields higher mean performance than removing them across all six settings, despite their absence at evaluation and identical supervised outputs." [Source: arxiv-2611.26510-automaster-autonomous-post-training-by-making-th.pdf p.1]
