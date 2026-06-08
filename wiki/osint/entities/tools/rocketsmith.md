---
title: RocketSmith (CMU agentic rocketry plugin)
type: entity
tags: [entity, tool, llm-agents, agent-harness, mcp, physical-domain, phase-0]
keywords: [rocketsmith, ppak10, openrocket, build123d, claude-code-plugin, gemini-cli, cmu]
related:
  - sources/arxiv-rocketsmith-agentic-rocketry-2606.00097-2026-06-08.md
  - concepts/code-as-agent-harness.md
  - concepts/llm-agent-systems.md
  - sources/agentic-harness-engineering.md
maturity: draft
created: 2026-06-08
updated: 2026-06-08
phase_0_verdict: REFERENCE 2026-06-08 — wrong domain for Cemini prod; steal harness patterns only
adoption_status: NO-GO
---

## Relations

- @sources/arxiv-rocketsmith-agentic-rocketry-2606.00097-2026-06-08.md — primary source (arXiv 2606.00097)
- @concepts/code-as-agent-harness.md — exemplar of domain-specific harness over fixed LLM

## Raw Concept

| Field | Value |
|-------|-------|
| **Repo** | https://github.com/ppak10/RocketSmith |
| **License** | MIT [CONFIRMED 2026-06-08 via `gh api`] |
| **Harness targets** | Claude Code, Gemini CLI (plugin) |
| **Domain stack** | OpenRocket → build123d → PrusaSlicer |
| **Prompted by** | K105 daily digest fetch (arXiv 2606.00097) |

## Narrative

MIT-licensed **domain harness** for Class-2 high-power rocketry: six scoped subagents, seven procedural skills, MCP tool calls, optional read-only GUI. CMU Mechanical Engineering + Tripoli Rocketry Association; four flight-tested rockets May 2026.

**Phase-0 verdict: REFERENCE / NO-GO for install.** Cemini has no rocketry surface. **Steal-from:** subagent compartmentalization, skill-trigger playbooks, deterministic parametric codegen with programmatic verification oracles, OpenRocket-as-source-of-truth pipeline ordering.

## Snippets

> Plugin release for Claude Code and Gemini-CLI; MCP-standard tool orchestration across OpenRocket, build123d, PrusaSlicer. [Source: arxiv-2606.00097…pdf + github.com/ppak10/RocketSmith]
