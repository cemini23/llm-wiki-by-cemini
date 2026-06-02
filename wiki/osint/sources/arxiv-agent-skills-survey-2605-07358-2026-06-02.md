---
title: "Agent skills taxonomy survey (arXiv:2605.07358)"
type: source
tags: [source, arxiv, agent-skills, harness, k94]
keywords: [agent skills, taxonomy, openclaw, procedural gap, ccc]
related:
  - concepts/llm-agent-systems.md
  - "@ccc-wiki/concepts/thin-harness-fat-skills-garrytan.md"
maturity: draft
read_status: read
created: 2026-06-02
updated: 2026-06-02
clusters: [agent-harness, ccc-routed]
---

## Relations
- @ccc-wiki/briefs/2026-06-02_2026-06-02_k94-ccc-agent-skills-agyn-toolforge-from-osint.md  (cross-wiki brief)

- @concepts/llm-agent-systems.md — agent paradigm context
- @ccc-wiki/concepts/thin-harness-fat-skills-garrytan.md — skills/harness posture (CCC expand agent-skills taxonomy on brief)

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | A Comprehensive Survey on Agent Skills: Taxonomy, Techniques, and Applications |
| **Author** | Zhou et al. (CUHK Shenzhen) |
| **arXiv ID** | 2605.07358 |
| **Location** | `cemini-librarian:/opt/cemini-bulk/research/arxiv-2605.07358-a-comprehensive-survey-on-agent-skills-taxonomy.pdf` |
| **Retrieved** | 2026-06-02 |
| **Read status** | read (abstract + introduction) |

## Narrative

K94 daily-digest fetch. Surveys **agent skills** as reusable procedural packages that close the gap between LLM reasoning and reliable tool/memory workflows — cites OpenClaw-style systems where re-deriving steps per task causes brittleness and latency.

**Cemini relevance:** directly supports **thin harness / fat skills** posture and CCC wiki skill libraries. Routed to `@ccc-wiki` for domain synthesis; OSINT keeps provenance only.

## Snippets

> "This 'procedural gap' has emerged as a major bottleneck." [Source: arxiv-2605.07358…pdf, Abstract]

> "Recent systems such as OpenClaw … reason, plan, and act through tools, memory, and structured interaction." [Source: arxiv-2605.07358…pdf, Abstract]

## Dead Ends

- Treating skills as ad-hoc prompt paragraphs without versioning — survey motivates structured skill catalogs (align with Cemini skill_audit / harness patterns).
