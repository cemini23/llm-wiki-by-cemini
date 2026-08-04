---
title: "arXiv 2608.02464 — Real-time detection and repair of LLM agent failures"
type: source
tags: [arxiv, agents, harness, ccc, atto, k222]
keywords: [ESN, CUSUM, Mahalanobis, telemetry, fabrication, agent monitor]
related:
  - sources/arxiv-2608.02505-abduction-loop-representational-grounding.md
  - sources/arxiv-2608.02287-skt-skill-use-training.md
  - concepts/llm-agent-failure-telemetry-monitors.md
  - concepts/gpuology-genealogy-agent-kit.md
maturity: draft
created: 2026-08-04
updated: 2026-08-04
read_status: deep-read
---

## Relations

- @sources/arxiv-2608.02505-abduction-loop-representational-grounding.md

- @sources/arxiv-2608.02287-skt-skill-use-training.md
- @concepts/llm-agent-failure-telemetry-monitors.md
- @concepts/gpuology-genealogy-agent-kit.md

## Raw Concept

| Field | Value |
|-------|--------|
| Title | Real-Time Detection and Repair of LLM Agent Failures |
| Author | Sunny Dubey |
| arXiv | 2608.02464 |
| sha256 | `788c825fc0cad65c109dd39da9efef8499bd96c557f388fa2998049dd592db5d` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2608.02464-real-time-detection-and-repair-of-llm-agent-fail.pdf` |
| retrieved | 2026-08-04 |
| read_status | deep-read |
| Code | none found in abstract (paper-only Phase-0) |

## Narrative

Argues against judging every agent step with a second LLM. Builds cheap monitors from **observable step telemetry** (embeddings, token uncertainty, action metadata) trained on healthy runs: one-class **ESN** + CUSUM → ESN+Mahalanobis hybrid → content-grounding channel for corruption. Validated on 2,823 episodes across frameworks/models. Organic failures: completion checks catch silent aborts; fabrication/commission needs escalation / deterministic grounding; organic transfer without recalibration is weak.

**Cemini:** CCC + Atto harness Extract **patterns** (telemetry + escalation layers). No clone this batch.

## Snippets

> LLM agents fail mid-episode—they loop, cascade tool errors, drift off their goal, fabricate results, or silently absorb corrupted content—and the standard remedy, judging every step with a second LLM, costs more than the agent itself. [Source: arXiv 2608.02464]
