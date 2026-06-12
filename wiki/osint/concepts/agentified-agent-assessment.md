---
title: Agentified Agent Assessment (AAA) — judge agents via A2A + MCP
type: concept
tags: [concept, agent-evaluation, benchmark, a2a, mcp, agentbeats, k112]
keywords: [aaa, agentified-assessment, agentbeats, a2a-protocol, test-production-mismatch]
related:
  - sources/arxiv-agentbeats-aaa-assessment-2606.13608-2026-06-12.md
  - entities/tools/agentbeats.md
  - concepts/llm-agent-systems.md
  - concepts/code-as-agent-harness.md
maturity: draft
created: 2026-06-12
updated: 2026-06-12
---

## Relations

- @sources/arxiv-agentbeats-aaa-assessment-2606.13608-2026-06-12.md
- @entities/tools/agentbeats.md
- @concepts/llm-agent-systems.md — eval methodology cluster
- @concepts/code-as-agent-harness.md — reduces N×M harness integration

## Raw Concept

K112 — paradigm shift: benchmarks are agents assessing agents through production protocols.

## Narrative

| Traditional | AAA (Agentified) |
|-------------|------------------|
| Fixed LLM harness | Judge agent + subject agent |
| N×M integrations | A2A task mgmt + MCP tools |
| Test–production mismatch | Production-aligned protocols |

**AgentBeats** — open competition validating AAA at scale (298 judges, 467 subjects).

**Cemini mapping:** Evolve `.local/reports/mcp-smoke-*` toward AAA-shaped judge agents; CONDITIONAL-GO laptop pilot via `agentbeats` repo after license check. Not a replacement for `skill_audit.py` on briefs — complementary agent-capability eval.

## Snippets

> "Administering an agent benchmark … is itself a well-defined agentic task."

> — [Source: arxiv-2606.13608-agentbeats-agentifying-agent-assessment-for-open.pdf §1, retrieved 2026-06-12]
