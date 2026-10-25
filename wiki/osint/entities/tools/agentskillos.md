---
title: "AgentSkillOS — Skill Retrieval & Orchestration Framework"
type: entity
tags: [tool, skill-retrieval, orchestration, mcp, tool-bloat, ranking]
keywords: [AgentSkillOS, skill retrieval, Bradley-Terry, tool ranking, MCP tool bloat, embedding matching]
related:
  - sources/evaluating-links-trading-wiki-stacks.md
  - concepts/tool-evaluation-framework.md
maturity: draft
created: 2026-05-10
updated: 2026-05-10
---

## Relations
- `@sources/evaluating-links-trading-wiki-stacks.md` — source evaluation brief (URL 15)

## Raw Concept

AgentSkillOS resolves the tool-bloat problem in AI agent development by providing a scalable skill retrieval and orchestration hub. Houses 200,000+ skill definitions with dynamic retrieval algorithms.

- **Repo**: `github.com/ynulihao/AgentSkillOS`
- **License**: To verify
- **Stack**: Python, embedding-based retrieval, Bradley-Terry paired evaluation ranking

## Narrative

AgentSkillOS addresses a problem Cemini already faces: with ~130 FastMCP tools, injecting all tool schemas into every DeepSeek call wastes context tokens. AgentSkillOS dynamically retrieves only the relevant tools for each query using embedding matching and Bradley-Terry paired evaluation rankings.

### Integration vectors

- **Cemini prod (Steal-from)**: Extract the Bradley-Terry paired evaluation algorithm for ranking tool efficacy and the embedding-based retrieval logic. Port these into `agents/orchestrator.py` to dynamically select relevant MCP tools per inference call instead of injecting all 130 schemas.
- **Workflow (Adopt)**: Study the repository offline to understand tool ranking mathematics and apply to local testing environment tool pruning.

### Risks

- **Architectural over-engineering**: Implementing a dynamic retrieval pipeline for 130 tools adds a retrieval latency hop and a new point of failure before LLM inference begins. For a linear 4-node StateGraph, this may be premature optimization.
- **Embedding model compatibility**: The embedding model used for query→tool matching must be replicable within Cemini's PostgreSQL constraints.

### Open questions

- Exact embedding model size and vector architecture used by AgentSkillOS for matching queries to tool descriptions; verify replicability inside Cemini Postgres constraints `[OPEN QUESTION 2026-05-10]`

[Source: Evaluating Links for Trading and Wiki Stacks.docx, URL 15]
