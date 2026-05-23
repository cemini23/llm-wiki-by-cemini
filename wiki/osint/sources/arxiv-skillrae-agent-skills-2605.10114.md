---
title: "SkillRAE — agent skill-based context compilation (arXiv:2605.10114)"
type: source
tags: [source, arxiv, agent-skills, rae, context-compilation, llm-agents, k59]
keywords: [skillrae, retrieval-augmented-execution, skill-graph, openclaw, skillsbench, context-compilation]
related:
  - concepts/skillrae-retrieval-augmented-execution.md
  - concepts/code-as-agent-harness.md
  - concepts/llm-agent-systems.md
  - sources/arxiv-code-as-agent-harness-survey-2605.18747.md
  - concepts/llm-agent-systems.md
maturity: draft
created: 2026-05-23
updated: 2026-05-23
read_status: skimmed
---

## Relations

- @concepts/skillrae-retrieval-augmented-execution.md — OSINT stub; full treatment → ccc-wiki brief
- @concepts/code-as-agent-harness.md — harness vs skill-library compilation layer
- @concepts/llm-agent-systems.md — RAE as third axis beyond RAG
- @sources/arxiv-code-as-agent-harness-survey-2605.18747.md — code-as-harness taxonomy

## Raw Concept

- **Title**: SkillRAE: Agent Skill-Based Context Compilation for Retrieval-Augmented Execution
- **Authors**: Xiangcheng Meng, Shu Wang, Yixiang Fang (CUHK Shenzhen)
- **Type**: arXiv:2605.10114v1 [cs.CL], May 2026
- **Location**: `cemini-librarian:/opt/cemini-bulk/research/2605.10114_skillrae-agent-skills.pdf`
- **Retrieved**: 2026-05-23 (K59 sweep Tier-B)
- **Read status**: skimmed (16 pp)

## Narrative

**Retrieval-Augmented Execution (RAE)** extends RAG from facts to **procedural skills** (OpenClaw-style SKILL.md bundles with scripts/assets). Prior work optimizes **which** skills to retrieve or how to plan execution; SkillRAE targets **compilation** — turning a coarse skill set into a **compact, grounded, task-specific context** for the executor.

**Offline:** multi-level **skill graph** — communities, skills, reusable **subunits** (scripts, steps, conventions) with dependency edges.

**Online:** skill-ranked retrieval + subunit export → **rescue-aware compact compilation** to recover dropped evidence.

**Results:** +11.7% on SkillsBench vs prior SOTA; ablations attribute gains to compilation, not prompt stuffing.

**Cross-wiki:** primary home is **ccc-wiki** (agent skills, lazy-tool, conductor context budget). OSINT page is a stub + routing brief.

## Snippets

> "A retrieved skill set may be globally relevant, but still under-resolved for execution." [Source: 2605.10114_skillrae-agent-skills.pdf p.2]

> "On SkillsBench, it achieves an improvement of 11.7% over the SOTA method." [Source: 2605.10114_skillrae-agent-skills.pdf p.1]
