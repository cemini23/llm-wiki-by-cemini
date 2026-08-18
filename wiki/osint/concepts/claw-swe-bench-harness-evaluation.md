---
title: Claw-SWE-Bench — harness as controlled variable in SWE-style eval
type: concept
tags: [concept, llm-agents, benchmark, harness, evaluation, k119]
keywords: [claw-swe-bench, harness-attribution, swe-bench, api-cost, lite-80]
related:
  - sources/arxiv-claw-swe-bench-2606.12344-2026-06-16.md
  - entities/tools/claw-swe-bench.md
  - concepts/code-as-agent-harness.md
  - concepts/mcp-tool-calling-eval-scaffold.md
  - concepts/conductor-orchestrator.md
  - concepts/openclaw-security-taxonomy.md
  - concepts/llm-agent-systems.md
  - sources/arxiv-2608.16798-clawgym-ii-2026-08-18.md
maturity: draft
created: 2026-06-16
updated: 2026-06-16
---

## Relations

- @sources/arxiv-claw-swe-bench-2606.12344-2026-06-16.md — K119 primary source
- @entities/tools/claw-swe-bench.md — MIT repo stub
- @concepts/code-as-agent-harness.md — harness engineering hub
- @concepts/mcp-tool-calling-eval-scaffold.md — GTFA smoke matrix sibling
- @concepts/conductor-orchestrator.md — orchestration harness under test

## Raw Concept

K119 arXiv 2606.12344 — first SWE-bench-style benchmark treating **agent harness** as explicit experimental factor with fixed outer budget + **cost accounting**.

## Narrative

### Decomposition

| Fixed (base protocol) | Swappable (claw slot) |
|-----------------------|------------------------|
| Task instances, Docker eval, patch contract, timeout, evaluator | OpenClaw, NanoBot, ZeroClaw, Hermes, Generic adapters |

### Steal-for-Cemini

1. **Never publish agent scores without harness + budget + cost** — adapter spread can exceed model spread.
2. **Lite subset pattern** — cost-aware rank-stable 80/350 for regression loops (maps to MCP smoke matrix size).
3. **Laptop smoke** — `opensquilla/claw-swe-bench` MIT; Lite-80 only; no prod install.

**Verdict:** REFERENCE benchmark; CONDITIONAL-GO for quarterly harness regression on Lite-80 when conductor coding tasks resume.

## Snippets

> "Claw-SWE-Bench therefore treats harness and cost accounting as first-class axes of SWE-style coding-agent evaluation." [Source: arxiv-2606.12344-tier2-sweep.pdf abstract]
