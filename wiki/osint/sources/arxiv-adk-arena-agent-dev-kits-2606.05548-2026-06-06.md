---
title: ADK Arena — agent development kit evaluation (arXiv 2606.05548)
type: source
tags: [source, arxiv, agent-harness, evaluation, k101, cross-wiki-route]
keywords: [2606.05548, adk-arena, llm-as-a-developer, mcp-atlas, swe-bench, framework-comparison]
related:
  - concepts/adk-arena-framework-evaluation.md
  - entities/tools/adk-arena.md
  - concepts/mcp-tool-calling-eval-scaffold.md
  - concepts/system-scaling-harness-evaluation.md
  - concepts/conductor-orchestrator.md
  - "@ccc-wiki/concepts/adk-arena-agent-framework-benchmark.md"
maturity: validated
read_status: deep-read
created: 2026-06-06
updated: 2026-06-06
---

## Relations

- @concepts/adk-arena-framework-evaluation.md — OSINT synthesis
- @entities/tools/adk-arena.md — Phase-0 NO-GO entity
- @concepts/mcp-tool-calling-eval-scaffold.md — MCP-Atlas adapter in benchmark suite
- @ccc-wiki/concepts/adk-arena-agent-framework-benchmark.md — CCC harness-primary stub (K101)

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | ADK Arena: Evaluating Agent Development Kits via LLM-as-a-Developer |
| **Authors** | Huang et al. (Ohio State + Microsoft CoreAI) |
| **arXiv** | 2606.05548 |
| **Repo** | https://github.com/jintao-h/ADK-Arena |
| **Location** | `cemini-librarian:/opt/cemini-bulk/research/arxiv-2606.05548-adk-arena-evaluating-agent-development-kits-via.pdf` |
| **Retrieved** | 2026-06-06 |
| **Read status** | **deep-read** — paper + Phase-0 repo audit (`/tmp/adk-arena-audit`) |

## Narrative

**Method — LLM-as-a-Developer:** Replace human framework experts with one **LLM coding agent** that learns each ADK from docs, writes agent code, and iterates through validate-and-feedback until tests pass. Holds the developer constant; varies only the **Agent Development Kit** (Python SDK-level framework).

**ADK Arena pipeline:** per-framework Docker isolation; three-level validation; benchmark adapters for **SWE-bench**, **τ²-bench**, **Terminal-Bench**, **MCP-Atlas**.

**Scale:** 51 popular Python ADK frameworks → 204 agent–benchmark pairs.

**Key findings [CONFIRMED]:**

| Finding | Detail |
|---------|--------|
| Generation success | 57% of runs succeed |
| API complexity proxy | Generation cost **5.6×** spread ($0.6–$3.4 per agent) — cost alone does not predict success |
| No single winner | Best single-benchmark agents to **80%** task resolution; can beat frontier general coding agents at lower cost; **median framework 32%** |
| Info-source ablation | Genuine framework usage **28–40%** band; **33%** even with no reference material — docs/source/params largely substitutable |

**Cemini routing:** **REFERENCE** — do not re-benchmark 51 frameworks locally. Steal:

1. **Framework choice is first-order** alongside model choice (corroborates grep-harness / kb-server eval posture).
2. **MCP-Atlas** as named adapter — extend `@concepts/mcp-tool-calling-eval-scaffold.md` smoke matrix.
3. **LLM-as-a-Developer** pattern for Phase-0 tool audits (lazy-tool catalog vs raw MCP) without human re-implementation per framework.

**Phase-0 (2026-06-06):** `@entities/tools/adk-arena.md` — **NO-GO adopt**, MIT [CONFIRMED], 1★/1-commit repo; steal MCP-Atlas GTFA + token-proxy patterns only.

## Snippets

> "By holding the developer constant and varying only the framework, generation effort becomes a quantitative proxy for API usability and the resulting agents provide a controlled measure of framework effectiveness."

> — [Source: arxiv-2606.05548-adk-arena-evaluating-agent-development-kits-via.pdf §1, retrieved 2026-06-06]

> "Evaluating all 51 popular Python ADK frameworks (204 agent–benchmark pairs)… no single framework dominates."

> — [Source: arxiv-2606.05548-adk-arena-evaluating-agent-development-kits-via.pdf abstract, retrieved 2026-06-06]
