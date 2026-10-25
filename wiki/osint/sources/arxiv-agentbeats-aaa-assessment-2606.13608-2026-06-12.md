---
title: AgentBeats — agentified agent assessment AAA (arXiv 2606.13608)
type: source
tags: [source, arxiv, agent-evaluation, benchmark, a2a, mcp, agentbeats]
keywords: [2606.13608, AgentBeats, AAA, agentified-assessment, A2A, MCP, reproducibility]
related:
  - concepts/agentified-agent-assessment.md
  - entities/tools/agentbeats.md
  - concepts/llm-agent-systems.md
  - concepts/code-as-agent-harness.md
  - sources/arxiv-metanym-game-llm-benchmark-2606.21008-2026-06-25.md
maturity: validated
read_status: skimmed
created: 2026-06-12
updated: 2026-10-25
---

## Relations

- @concepts/agentified-agent-assessment.md — AAA paradigm synthesis
- @entities/tools/agentbeats.md — Phase-0 CONDITIONAL-GO (license null; ~80 stars)
- @concepts/llm-agent-systems.md — eval cluster

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | AgentBeats: Agentifying Agent Assessment for Openness, Standardization, and Reproducibility |
| **arXiv** | 2606.13608 |
| **Repo** | https://github.com/AgentBeats/AgentBeats |
| **sha256** | `60e7b69feb80464627d01915698eff82b0c867a2358cdc8fc8a7f429140b43e4` |
| **Location** | `cemini-librarian:/opt/cemini-bulk/research/arxiv-2606.13608-agentbeats-agentifying-agent-assessment-for-open.pdf` |
| **Retrieved** | 2026-06-12 |
| **Read status** | skimmed — abstract, AAA vs traditional table, competition scale |

## Narrative

**Agentified Agent Assessment (AAA):** treat benchmarks as **judge agents**; subjects interact via **A2A** (task management) + **MCP** (tool access) — one protocol surface instead of N×M bespoke integrations.

**AgentBeats** realization: five operation modes for openness/privacy/reproducibility; 5-month competition with **298 judge agents / 467 subject agents** across 12 categories.

**Cemini mapping:** REFERENCE for **lazy-tool / conductor smoke matrix** evolution — evaluate production-shaped agents without harness rewrite. Phase-0: CONDITIONAL-GO laptop pilot after license verify. Steal: judge-as-agent + A2A/MCP mediation for MCP smoke GTFA runs.

## Snippets

> "Evaluating M agents on N benchmarks essentially requires N * M bespoke integration efforts."

> — [Source: arxiv-2606.13608-agentbeats-agentifying-agent-assessment-for-open.pdf §1, retrieved 2026-06-12]
