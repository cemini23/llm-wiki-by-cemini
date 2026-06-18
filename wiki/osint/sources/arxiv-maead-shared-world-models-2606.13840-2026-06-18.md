---
title: "Multi-Agent Embodied Autonomous Driving — Shared World Models survey — arXiv 2606.13840"
type: source
tags: [source, arxiv, survey, autonomous-driving, world-model, k122]
keywords: [2606.13840, MAEAD, V2X, shared world models, cooperative perception, embodied AI]
related:
  - concepts/multi-agent-embodied-autonomous-driving-survey.md
  - sources/leworldmodel-2603.19312v2.md
maturity: draft
read_status: read
created: 2026-06-18
updated: 2026-06-18
clusters: [llm-agents]
---

## Relations

- @concepts/multi-agent-embodied-autonomous-driving-survey.md — K122 synthesis
- @sources/leworldmodel-2603.19312v2.md — single-agent world-model contrast

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Multi-Agent Embodied Autonomous Driving: From V2X Information Exchange to Shared World Models |
| **Authors** | Senkang Hu, Zhengru Fang, Yihang Tao, Zihan Fang, Sam Tak Wu Kwong, Yuguang Fang |
| **arXiv** | 2606.13840 (11 Jun 2026) |
| **sha256** | `bee84131e4574581f39a78bd0372736f7ba80760b82220fd8e4830ed416cc673` |
| **Repo** | none (survey) |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2606.13840-2606-13840v1-multi-agent-embodied-autonomous-dri.pdf` |
| **Retrieved** | 2026-06-18 (daily digest inbox) |
| **Read status** | read (abstract + scope) |

## Narrative

Survey of **380+ publications** on the shift from isolated vehicle intelligence to **multi-agent embodied autonomous driving (MAEAD)** centered on **Shared World Models (SWMs)** — predictive cross-agent state maintained across vehicles, infrastructure, and traffic participants.

**Coverage:** V2X communication, collaborative perception, inter-agent cognition, cooperative planning, end-to-end cooperative driving, simulation/data engines for closed-loop validation.

**Organizing question:** how exchanged observations become **aligned state**, **intent-aware interaction**, and **coordinated action**.

**Gaps flagged:** evaluation still concentrated in simulation/offline benchmarks; foundation-model coordination lacks verified real-time safety guarantees in open traffic.

**Research priorities:** verifiable shared-state maintenance, robust intent/plan alignment, safe coordinated action under communication/latency constraints.

**Cemini posture:** **REFERENCE** — wiki catalog only. Tangential steal for multi-agent conductor orchestration (shared state vs message passing) but no prod brief unless WC/PM module explicitly reopens autonomous stack.

## Snippets

> "We review more than 380 publications spanning vehicle-to-everything (V2X) communication, collaborative perception, inter-agent cognition, cooperative planning, end-to-end cooperative driving, and simulation and data engines for closed-loop validation." [Source: arXiv:2606.13840 abstract (retrieved 2026-06-18)]

> "Foundation-model-based coordination also lacks verified real-time safety guarantees in open traffic." [Source: arXiv:2606.13840 abstract (retrieved 2026-06-18)]

## Dead Ends

- Not a primary OSINT/finance ingest — kept for world-model taxonomy completeness and daily-digest inbox clearance.
- No executable artifact — survey-only.
