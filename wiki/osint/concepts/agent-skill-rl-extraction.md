---
title: Agent-Skill RL Extraction — learning reusable skills for small LMs
type: concept
tags: [concept, agent-skills, rl, k233, ccc]
keywords: [skill-extraction, rl-via-natural-language, skill-compilation, small-lm, skilling]
related:
  - sources/arxiv-2608.10538-skiller-2026-08-12.md
  - sources/newsletter-latent-space-ainews-reasoning-trace-2026-08-12.md
  - entities/tools/skiller.md
  - entities/tools/skilllens.md
maturity: draft
created: 2026-08-12
updated: 2026-08-12
---

## Relations

- @sources/arxiv-2608.10538-skiller-2026-08-12.md — SKILLER
- @sources/newsletter-latent-space-ainews-reasoning-trace-2026-08-12.md — skill-compilation paragraph
- @entities/tools/skiller.md
- @entities/tools/skilllens.md — visual sibling

## Raw Concept

What this page answers: how agent skills — reusable procedural-knowledge packages for constraining an LM's behavior space — can be *generated*, not hand-written, for small local models. Synthesized from SKILLER (arXiv 2608.10538) + the AINews skill-compilation result (2026-08-12).

## Narrative

Agent skills are the harness primitive that turns procedural knowledge into repeatable behavior constraints (Anthropic-style skill format; the CCC `/route` family). Hand-writing executor-specific skills for small open models is the bottleneck: strong closed-source models are expensive to run as executors, and naive prompts don't transfer.

**Two convergent results (K233):**

1. **SKILLER (arXiv 2608.10538)** — natural-language-driven RL loop: a *strong model is the actor and critic*, the *small-model agent system is the environment*, and all RL signals propagate via natural language (no gradient flow). Skill artifact is language, so it generalizes across model internals. On Qwen3.5-9B/4B: +4.3–20.4pp / +1.8–13.3pp over open+closed skill-generation baselines; matches strong closed models on single-skill SkillsBench tasks.

2. **Skill compilation (AINews 2026-08-12)** — compact natural-language skills distilled from prior trajectories recover **55% to >100%** of the gap between non-reasoning and reasoning modes on multi-step agentic tasks with **2.7–6× fewer output tokens**. Independent, lightweight corroboration that language-level skill extraction is high-leverage.

**Steal for CCC `/route`:** use a strong model to author route-style skills for small local executors (the workspace already runs DeepSeek-v4 + local small models). SkillsBench-style single-skill tasks are a cheap eval. SKILLER repo is NOASSERTION → pattern only. SkillLens (arXiv 2608.10775) extends the same idea to *visual* skills for GUI agents.

[Source: arXiv:2608.10538; AINews 2026-08-12]
