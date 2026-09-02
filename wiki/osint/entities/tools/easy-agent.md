---
title: "easy-agent — 5-layer terminal agent (MIT Extract)"
type: entity
tags: [tool, ccc, atto, k242, mit, extract]
keywords: [easy-agent, mcp, claude-code-pattern]
related:
  - sources/eval-local-agent-infra-2026-08-19.md
  - concepts/cemini-license-posture.md
  - concepts/atto-genealogy-agent-kit.md
  - concepts/llm-routing-deepseek-openrouter-failover.md
  - sources/newsletter-rss-latent-space-2026-08-18-glean-model-routing.md
maturity: draft
created: 2026-08-19
updated: 2026-08-19
harness_verb: FILE
wire_note: Harness pattern Extract; do not swap /route worker
---

## Relations

- @sources/eval-local-agent-infra-2026-08-19.md — K242 eval
- @concepts/cemini-license-posture.md
- @concepts/atto-genealogy-agent-kit.md — human-gate `truth.ged` writes
- @concepts/llm-routing-deepseek-openrouter-failover.md — do not replace `claude-ds`
- @sources/newsletter-rss-latent-space-2026-08-18-glean-model-routing.md — enterprise routing demand

## Raw Concept

K242 Phase-0 Extract. Clone `.local/adopts/easy-agent` (~4.7MB). https://github.com/ConardLi/easy-agent

## Narrative

| Field | Value |
|-------|--------|
| License | **MIT** [CONFIRMED gh 2026-08-19] |
| Local | `.local/adopts/easy-agent` |
| Verdict | **Extract** |
| wire_status | `policy_wired` |

TypeScript 5-layer Claude-Code-like agent (Ink UI, query engine, loop, tool/permission, provider stream) with MCP, checkpoints, and token budgets. Steal permission gating and session compaction for atto-mcp. **Do not swap `/route` or PATH `claude-ds`.** Autonomous writes must stay behind the Atto human-gate.

## Snippets

> easy-agent MIT Extract. No /route worker swap. [Source: `.local/reports/license-k242-2026-08-19.md`]
