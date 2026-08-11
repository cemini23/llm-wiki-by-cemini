---
title: "Agentic Harnesses — LLM-Driven Verification Layers for Robot Autonomy"
type: source
tags: [arxiv, k232, ccc, cyber]
keywords: [2608.09857, verification-layer, llm-as-judge, robot-autonomy, mcp, accept-escalate-reject]
related:
  - concepts/agent-harness-auditing-a2e.md
maturity: draft
created: 2026-08-11
updated: 2026-08-11
read_status: skimmed
---

## Relations

- @concepts/agent-harness-auditing-a2e.md

## Raw Concept

| Field | Value |
|-------|--------|
| arXiv | 2608.09857 |
| sha256 | `874fec66793d53932c764127f679c5dabfdce399507a87fba951d6223073ebcd` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2608.09857-agentic-harnesses-llm-driven-verification-layers.pdf` |
| retrieved | 2026-08-11 |

## Narrative

PNNL (Bhagra, Halapannavar, Bhattarai — Richland, WA, 8 pp) proposes an **LLM-driven verification layer between planning and execution** for robot autonomy: an LLM-as-a-Judge ensemble gates plans from the planning module before they reach the MCP server / low-level controls. Decisions are **accept**, **reject** (send back for reformulation), or **escalate** (human review).

Judging architecture is two-prong: (1) an async ensemble of five public frontier models (e.g., Claude Sonnet 4.5, OpenAI o3, Grok-4.1-fast) each rendering accept/reject/escalate with reasoning against safety/alignment/security decision rules and a knowledge-graph context; (2) a **chief judge** (Claude Sonnet 4.6) that never sees the plan — it evaluates the quality of each judge's reasoning and risk weighting, escalating automatically if it conflicts with ≥3 judges. Latency ~24.2s per judging roundtrip (58-run test). Results: ~85% precision across accept/escalate/reject, 97% containment of adversarial attacks, errors mostly at the escalate boundary.

**Routing:** CCC/cyber verification-gate middleware pattern (LLM-as-judge ensemble + chief-judge meta-evaluation applies to tool/MCP gating generally). Robot runtime **wont_wire** — pattern brief only; no robotics stack adoption.

[Source: arXiv:2608.09857]
