---
title: "arXiv 2608.03779 — AgenticVAU multi-agent video anomaly"
type: source
tags: [arxiv, agents, ccc, k223]
keywords: [AgenticVAU, explore-verify, VAU-Bench, anchor registry]
related:
  - concepts/llm-agent-failure-telemetry-monitors.md
  - sources/arxiv-2608.02505-abduction-loop-representational-grounding.md
maturity: draft
created: 2026-08-05
updated: 2026-08-05
read_status: deep-read
---

## Relations

- @concepts/llm-agent-failure-telemetry-monitors.md
- @sources/arxiv-2608.02505-abduction-loop-representational-grounding.md

## Raw Concept

| Field | Value |
|-------|--------|
| Title | AgenticVAU: Multi-Agent Explore–Verify Reasoning for Video Anomaly Understanding |
| arXiv | 2608.03779 |
| sha256 | `9fb9b04759d0dc60d67d9f99e1a9c1af036fc1cd13a43e43563c64bd95d928cf` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2608.03779-agenticvau-multi-agent-explore-verify-reasoning.pdf` |
| read_status | deep-read |

## Narrative

Training-free multi-agent VAU: specialized agents for visual-rule construction, search planning, observation, decision; shared **anchor registry** evidence memory. Explore then verify. Beats zero-shot + RL baselines on VAU-Bench subsets. **CCC pattern** (explore–verify + evidence memory) — no code clone; not Atto HTR; not poker.
