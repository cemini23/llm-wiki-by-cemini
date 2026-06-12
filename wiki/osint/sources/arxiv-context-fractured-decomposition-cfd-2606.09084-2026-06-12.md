---
title: Context-Fractured Decomposition attacks on tool-using agents (arXiv 2606.09084)
type: source
tags: [source, arxiv, agent-security, prompt-injection, provenance, mcp, tool-using-agents]
keywords: [2606.09084, CFD, provenance-gap, artifact-mediated, jailbreak, multi-step]
related:
  - concepts/context-fractured-decomposition-attacks.md
  - concepts/seclaw-agent-security-evaluation.md
  - concepts/ems-execution-security-gaps.md
  - concepts/conductor-orchestrator.md
  - sources/trading-posts-compilation-9-2026-06-12.md
  - concepts/llm-agent-systems.md
maturity: validated
read_status: skimmed
created: 2026-06-12
updated: 2026-06-12
---

## Relations

- @concepts/context-fractured-decomposition-attacks.md — synthesis hub
- @concepts/seclaw-agent-security-evaluation.md — complementary trajectory-aware eval
- @concepts/conductor-orchestrator.md — MCP multi-hop provenance target
- @concepts/ems-execution-security-gaps.md — execution-security stack gap fill

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Context-Fractured Decomposition Attacks on Tool-Using LLM Agents: Exploiting Artifact Provenance Gaps |
| **arXiv** | 2606.09084 |
| **sha256** | `3f9f96bf00f8bd0d647826458dbca8e63deb5f328324b3fcdaea9bbd9689d5b3` |
| **Location** | `cemini-librarian:/opt/cemini-bulk/research/arxiv-2606.09084-context-fractured-decomposition-attacks-on-tool.pdf` |
| **Retrieved** | 2026-06-12 |
| **Read status** | skimmed — abstract, provenance gap definition, +28.14pp claim |

## Narrative

Introduces the **provenance gap**: agent pipelines fracture context across sessions/tools while **persistent artifacts** (files, logs, caches) carry state without lineage tracking.

**Context-Fractured Decomposition (CFD)** — cross-context multi-step jailbreaks: benign-looking early writes + individually innocuous later tool reads whose harm emerges only under delayed composition. Up to **+28.14 pp** success vs SOTA baselines even against strong single-turn judges.

Mitigation direction: **provenance lineage tagging** on artifacts (verifiable, not fully implemented in paper).

**Cemini mapping:** P0 concern for **conductor + kb-server + wiki ingest** paths where agents write briefs, configs, and MCP tool outputs across sessions. Pair with SeClaw eval and K19/K20/K22 execution-security stack. Prod brief: artifact lineage hooks REFERENCE.

## Snippets

> "Benign-looking writes can later be read and composed into harmful actions when provenance is not tracked."

> — [Source: arxiv-2606.09084-context-fractured-decomposition-attacks-on-tool.pdf Abstract, retrieved 2026-06-12]
