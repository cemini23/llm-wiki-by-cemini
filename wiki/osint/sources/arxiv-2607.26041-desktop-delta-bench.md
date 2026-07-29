---
title: "arXiv 2607.26041 — Desktop-Delta Bench (DDB)"
type: source
tags: [source, arxiv, gui-agent, benchmark, nvidia, ccc, k206]
keywords: [DDB, Desktop-Delta, OSWorld, temporal ordering, presentation-order bias]
related:
  - sources/arxiv-2607.25904-interactive-reward-agent-gui.md
maturity: draft
created: 2026-07-29
updated: 2026-07-29
read_status: skimmed
---

## Relations

- @sources/arxiv-2607.25904-interactive-reward-agent-gui.md — IRA env-state eval pair

## Raw Concept

| Field | Value |
|-------|--------|
| Title | Desktop-Delta Bench: Do Computer-Use Models Understand Desktop GUI Transitions? |
| Authors | Pillai / Nayak / Chen (NVIDIA) |
| arXiv | 2607.26041 |
| Filename | `arxiv-2607.26041-desktop-delta-bench-do-computer-use-models-under.pdf` |
| sha256 | `b57aa90e964dcfd91bad96e03bd833b6a907d4ca2ffff16bf7393f2b3a04c635` |
| Retrieved | 2026-07-29 |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2607.26041-desktop-delta-bench-do-computer-use-models-under.pdf` |
| Repo | https://github.com/abhipi/DDB — **404 as of 2026-07-29**; Phase-0 deferred |

## Narrative

End-task OSWorld scores hide whether VLMs understand causal GUI transitions (stale-obs rejection, progress verify, recovery). Offline step-level bench: **2,013** human-verified instances; ~15 Linux apps; 50 domains. Ordering unsaturated (~65% best exact-match); systematic **A→B→C presentation-order copying** bias (37–45% of some failures). Diagnostic layer between grounding and end-task success.

**Route:** CCC. Recheck size before any future clone (screenshots risk).

## Snippets

> Ordering unsaturated: best exact-match ~65%; chronology still weak under decoys.

[Source: arXiv:2607.26041]
