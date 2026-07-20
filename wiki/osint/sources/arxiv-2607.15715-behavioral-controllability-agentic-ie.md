---
title: "arXiv 2607.15715 — Behavioral Controllability of Agentic Models for IE"
type: source
tags: [source, arxiv, agent-harness, information-extraction, genealogy, k177]
keywords: [2607.15715, behavioral-controllability, reflective-agents, dataset-extraction, process-trace]
related:
  - concepts/computational-genealogy-archival-automation.md
  - concepts/code-as-agent-harness.md
  - concepts/cemini-wiki-ingest-workflow.md
maturity: draft
read_status: read
created: 2026-07-20
updated: 2026-07-20
clusters: [k177-ingest]
---

## Relations

- @concepts/computational-genealogy-archival-automation.md — archival IE / act extraction
- @concepts/code-as-agent-harness.md — agent vs fixed workflow
- @concepts/cemini-wiki-ingest-workflow.md — wiki ingest as IE pipeline

## Raw Concept

| Field | Value |
|-------|-------|
| **arXiv** | 2607.15715 |
| **sha256** | `77a56e97a63e5c99ee76baaaab175d09097a5423f471cc96a8baac69d15fe425` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2607.15715-behavioral-controllability-of-agentic-models-for.pdf` |

## Narrative

Compares fixed LLM workflows vs reflective/memory agents on scholarly **dataset-mention extraction** from PDFs. Emphasizes **behavioral controllability** — observable, configurable, reproducible process traces (tools, retries, reflection, memory, runtime, failure recovery) — with coverage as secondary. Optimized agent (S2) adds richer PDF tools + dynamic tool selection. **Steal:** for genealogy act extraction and wiki ingest, prefer process-level eval harnesses over coverage-only scores; agentic reflection is not free (runtime / harder debug).
