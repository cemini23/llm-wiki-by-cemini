---
title: "langchain-ai/deepagents"
type: entity
tags: [tool, phase-0, k224, atto]
keywords: [deepagents, LangGraph, write_todos, subagents, planning-first]
related:
  - sources/eval-url-batch-agentic-edge-security-2026-08-05.md
  - entities/tools/hermes-office.md
  - concepts/wiki-tooling-evaluation.md
  - concepts/cemini-license-posture.md
  - concepts/gpuology-genealogy-agent-kit.md
maturity: draft
created: 2026-08-05
updated: 2026-08-05
harness_verb: FILE
---

## Relations

- @sources/eval-url-batch-agentic-edge-security-2026-08-05.md
- @entities/tools/hermes-office.md
- @concepts/wiki-tooling-evaluation.md
- @concepts/cemini-license-posture.md
- @concepts/gpuology-genealogy-agent-kit.md

## Raw Concept

K224 eval URL 4 Extract. Repo: https://github.com/langchain-ai/deepagents

## Narrative

| Field | Value |
|-------|--------|
| **Repo** | https://github.com/langchain-ai/deepagents |
| **License** | **MIT** [CONFIRMED gh 2026-08-05] |
| **Verdict** | **GO Extract** → Atto (combo with Atto MCP) |
| **Local** | `.local/adopts/deepagents` (~79MB) |
| **Stars / push** | 27.4k / 2026-08-05 |

Planning-first LangGraph harness: `write_todos` before tool chaos, filesystem backends, isolated sub-agents for long-horizon FIND/extract. **Preview patterns — not a production pin.** Vault PII isolation mandatory; Magika + PII strip unchanged; Transkribus sole HTR. Do not auto-write `truth.ged`.
