---
title: "Cooperative-ORCA* — proactive MAPF deadlock avoidance (arXiv 2606.22757)"
type: source
tags: [source, arxiv, pathfinding, mapf, robotics, k129]
keywords: [2606.22757, C-ORCA, ORCA-MAPF, deadlock, multi-agent navigation, flowtime]
related:
  - concepts/active-project-research-routing.md
  - sources/arxiv-continuum-robots-resilience-2606.20495-2026-06-22.md
maturity: draft
read_status: read
created: 2026-06-25
updated: 2026-06-25
clusters: [llm-agents]
---

## Relations

- @concepts/active-project-research-routing.md — castle-sim RTS pathfinding reference

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Cooperative-ORCA*: Real-Time Proactive Deadlock Avoidance for Continuous-Space Multi-Agent Navigation |
| **Authors** | Junfeng Wu, Jiaqi Chen, Hongkun Lyu, Kevin Zheng, Andy Li |
| **arXiv** | 2606.22757v1 (Jun 2026) |
| **sha256** | `037c9dac0cdeeb2ec2cbe5d88d147e1dd8e1388d4829f525926df279b490a8f4` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2606.22757-2606-22757v1-cooperative-orca-real-time-proactiv.pdf` |
| **Retrieved** | 2026-06-25 (inbox) |
| **Read status** | read (abstract + ORCA* comparison) |

## Narrative

**MAPF** in continuous space: **ORCA*** assigns per-timestep velocities but is **myopic** — future deadlocks from current decisions. **ORCA*-MAPF** adds fallback on detected deadlocks → high **flowtime** overhead.

**C-ORCA* / C-ORCA*-MAPF:** incorporate agents' full spatial trajectories + spatial dependencies to **proactively prevent** deadlocks vs post-hoc correction.

Outperforms prior SOTA on solve rate, runtime, flowtime [TENTATIVE — paper benchmarks].

**Cemini steal:** Proactive deadlock avoidance pattern for castle-sim unit crowding / siege lane conflicts — reference only (continuous ORCA ≠ grid A* without adaptation).

## Snippets

> "ORCA* is a real time MAPF solver … Due to its real time nature, it is myopic to future deadlocks that result from current decisions." [Source: arXiv:2606.22757 abstract (retrieved 2026-06-25)]

> "C-ORCA* … incorporate agents' entire spatial trajectory and their spatial dependencies to proactively prevent deadlocks from occurring." [Source: arXiv:2606.22757 abstract (retrieved 2026-06-25)]

> "The C-ORCA* family of algorithms significantly outperform previous state-of-the-art in terms of solve rate, runtime, and flowtime." [Source: arXiv:2606.22757 abstract (retrieved 2026-06-25)]

## Dead Ends

- Continuous-space velocity ORCA ≠ Godot NavigationAgent2D defaults — engineering gap for vertical slice.
