---
title: "SkillRAE — retrieval-augmented execution via skill-graph context compilation"
type: concept
tags: [concept, llm-agents, agent-skills, context-engineering, k59, ccc-routed]
keywords: [skillrae, rae, skill-graph, context-compilation, skillsbench, openclaw]
related:
  - sources/arxiv-skillrae-agent-skills-2605.10114.md
  - concepts/code-as-agent-harness.md
  - concepts/llm-agent-systems.md
  - sources/arxiv-code-as-agent-harness-survey-2605.18747.md
  - ccc-wiki/concepts/skillrae-retrieval-augmented-execution.md
  - ccc-wiki/sources/arxiv-skillrae-2605.10114.md
maturity: draft
created: 2026-05-23
updated: 2026-05-23
---

## Relations

- @sources/arxiv-skillrae-agent-skills-2605.10114.md — K59 source
- @concepts/code-as-agent-harness.md — harness substrate vs skill compilation
- @concepts/llm-agent-systems.md — corpus hub
- @sources/arxiv-code-as-agent-harness-survey-2605.18747.md — related harness survey
- @ccc-wiki/concepts/skillrae-retrieval-augmented-execution.md — Claude Code / lazy-tool / conductor mapping
- @ccc-wiki/sources/arxiv-skillrae-2605.10114.md — CCC source provenance page

## Raw Concept

K59 ingest stub for **SkillRAE** (arXiv:2605.10114). Full narrative expansion delegated to **ccc-wiki** via `@ccc-wiki/briefs/2026-05-23_k59-skillrae-graphflow-from-osint.md`.

## Narrative

**Problem:** Large skill libraries (SkillsBench, AgentSkillOS) make flat retrieval insufficient — executors need **compiled** context: which subunits, in what dependency order, with what constraints.

**SkillRAE pipeline:**
1. Offline **skill graph** (community → skill → subunit).
2. Online ranked retrieval + **rescue-aware compilation** into executor-ready context.

**Cemini relevance:** complements **lazy-tool** (tool schema compression) and **conductor** routing — addresses **context budget** after tools/skills are chosen. Not a prod adoption; research reference for wiki/ccc skill-library design.

See ccc-wiki for implementation-adjacent notes and relation to OpenSpec/skill audit workflows.

## Snippets

> "SKILLRAE compiles a coarse-ranked skill set into a task-specific context that is compact, grounded, and immediately usable." [Source: 2605.10114_skillrae-agent-skills.pdf p.1]
