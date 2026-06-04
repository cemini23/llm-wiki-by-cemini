---
title: "SeClaw — Spec-Driven Security Task Synthesis for Evaluating Autonomous Agents (arXiv:2606.02302)"
type: source
tags: [source, arxiv, agent-security, evaluation, k98]
keywords: [2606.02302, seclaw, openclaw, trajectory-aware, docker-testbed, skill-injection]
related:
  - concepts/seclaw-agent-security-evaluation.md
  - sources/arxiv-cli-anything-2606-03854-2026-06-03.md
  - concepts/ems-execution-security-gaps.md
  - "@cybersecurity-wiki/briefs/2026-06-04_k98-seclaw-agent-eval-from-osint.md"
  - sources/trading-posts-compilation-18-2026-06-04.md
read_status: skimmed
maturity: draft
created: 2026-06-04
updated: 2026-06-04
---

## Relations

- @concepts/seclaw-agent-security-evaluation.md — OSINT synthesis
- @concepts/ems-execution-security-gaps.md — prod EMS/RBAC gaps (orthogonal: code audit vs agent benchmark)
- @cybersecurity-wiki/briefs/2026-06-04_k98-seclaw-agent-eval-from-osint.md — cross-wiki handoff

## Raw Concept

| Field | Value |
|-------|-------|
| Title | SeClaw: Spec-Driven Security Task Synthesis for Evaluating Autonomous Agents |
| Authors | Hao Cheng et al. (HKUST, Ant, XJTU, Oxford, …) |
| arXiv | 2606.02302 |
| Code | https://github.com/seclaw-eval/seclaw-eval |
| Retrieved | 2026-06-04 |
| Location | `cemini-librarian:/opt/cemini-bulk/research/arxiv-2606.02302-seclaw-spec-driven-security-task-synthesis-for-e.pdf` |
| read_status | skimmed |

## Narrative

Benchmark framework for **tool-using LLM agents** in stateful environments. Two pillars: (1) **spec-driven task synthesis** — scalable security tasks from structured risk specs; (2) **SeClaw docker testbed** — reproducible evaluation across resource/user/environment/intrinsic agent risk classes. Emphasizes **trajectory-aware** unsafe-action detection, not final-answer-only scoring. Cites OpenClaw-style agent stacks as motivation.

**Cemini relevance:** CONDITIONAL-GO for **pre-release harness regression** on conductor/kb MCP tool policies — not a prod runtime dependency. Pair with K96 EMS audit: SeClaw measures agent misuse; EMS audit measures trading bypass. Cross-wiki → cybersecurity-wiki for eval methodology depth.

## Snippets

> "Current agent security benchmarks often rely on manually curated tasks … focus primarily on final outcomes rather than the execution processes"

> "trajectory-aware assessment of unsafe actions beyond final responses"

[Source: arxiv-2606.02302-seclaw-spec-driven-security-task-synthesis-for-e.pdf p.1, retrieved 2026-06-04]
