---
title: K252 harness evolution wave (Aug 2026)
type: concept
tags: [agents, harness, k252, ccc]
keywords: [EvoUndo, Logos, skill-routing, recoverability]
related:
  - sources/arxiv-2608.28363-evoundo-recoverability-2026-08-31.md
  - sources/arxiv-2608.28553-logos-cross-process-bus-2026-08-31.md
  - sources/arxiv-2608.28241-personalized-skill-routing-2026-08-31.md
  - sources/arxiv-2608.28433-prove2me-formalization-2026-08-31.md
  - concepts/k252-harness-evolution-wave.md
  - concepts/k253-harness-self-improvement-wave.md
maturity: draft
created: 2026-08-31
updated: 2026-09-01
---

## Relations

- @sources/arxiv-2608.28363-evoundo-recoverability-2026-08-31.md — recoverability-constrained self-evolution
- @sources/arxiv-2608.28553-logos-cross-process-bus-2026-08-31.md — cross-process plugin harness (AAMAS)
- @sources/arxiv-2608.28241-personalized-skill-routing-2026-08-31.md — personalized skill routing + counterfactual eval
- @sources/arxiv-2608.28433-prove2me-formalization-2026-08-31.md — collaborative Lean formalization harness
- @concepts/k250-harness-intelligence-wave.md — JIT/ReasoningBank prior wave

## Raw Concept

K252 harness cluster — recoverability (EvoUndo), distributed composability (Logos), skill routing (28241), formalization missions (Prove2Me).

## Narrative

Four papers extend the harness-intelligence thread from K250. **EvoUndo** makes recoverability an explicit invariant for runtime harness self-mutation — 197/600 capability-positive mutations fail recovery under naive repair; grounding + richer recovery language unlock most oracle cases (pairs **K282 AgentRewind**, **K237 skill misevolution**). **Logos** implements spatiotemporal-composability across processes via ROS-like bus + append-only transcript; 80 sessions resume with no repeated effect after kills at tool-cycle boundaries.

**Personalized skill routing** goes beyond task-only matching with counterfactual evaluation for per-user skill selection (pairs **BPS/skill-set-budget**). **Prove2Me** is a mission-based Lean formalization platform with agent-first collaboration and bounded human audit surface (pairs **K280 Vero** vocabulary). **0 Integrate GO** — no public SPDX clones this wave.
