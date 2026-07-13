---
title: Hierarchical memory architecture for long-horizon multi-agent modeling (2607.07666)
type: source
tags: [source, arxiv, agent-memory, multi-agent, k161]
keywords: [Ensemble QSP, hierarchical memory, context bound, PI agent, project-state JSON]
clusters: [k161-ingest, agent-memory]
related:
  - concepts/agent-memory-critique.md
  - concepts/context-compression-resume-pattern.md
  - concepts/hierarchical-bounded-agent-memory.md
  - sources/arxiv-deepsearch-world-2607.07820-2026-07-13.md
maturity: validated
read_status: deep-read
created: 2026-07-13
updated: 2026-07-13
---

## Raw Concept

| Field | Value |
|-------|-------|
| **arXiv** | [2607.07666](https://arxiv.org/abs/2607.07666) |
| **sha256** | `f12f4357753e6f33…` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2607.07666-2607-07666v1-a-hierarchical-memory-architecture.pdf` |
| **Authors** | Tewari & Kimko (AstraZeneca Systems Medicine) |

## Relations

- @concepts/hierarchical-bounded-agent-memory.md — K161 steal concept
- @concepts/agent-memory-critique.md — selective encoding + eviction evidence
- @concepts/context-compression-resume-pattern.md — mid-term project-state vs CPR

## Narrative

**Ensemble QSP** — multi-agent scientific modeling with a **three-layer hierarchical memory** that keeps injected context **bounded and constant in project duration** (mid-term project state: median **301** tokens, IQR 215–478, max **4,050** across 104 runs) by capping each category and **evicting completed work**.

| Layer | Contents | Cap / eviction |
|-------|----------|----------------|
| Short-term | Recent turns (4–20), scratchpad, last 5 cross-agent outcomes | Scratchpad ≤20k chars (specialists) / ≤8k (PIs) |
| Mid-term | Project-state JSON slices + auto-summarizing decision log | Decision log ≤16k chars; selective field inject |
| Long-term | Domain handbook (~24k chars), physics checklists, paper/code retrieval | Project-independent |

Orchestrates **five specialist workers** under domain-expert **principal investigators**; physics checklists enforce constraints. Architecture is **domain-agnostic** — new domain = new PI config only. QSP/PK-PD results are domain proof, not Cemini product scope.

**Cemini steal:** poker HU session continuity + CCC harness — structured mid-term state with eviction beats naive history concat (O(N×T) growth). No public installable repo → **REFERENCE architecture** (Phase-0).

## Snippets

> "keeps injected context bounded and constant in project duration (mid-term project state: median 301 tokens, max 4,050, across 104 runs)" [Source: arXiv:2607.07666 abstract]
