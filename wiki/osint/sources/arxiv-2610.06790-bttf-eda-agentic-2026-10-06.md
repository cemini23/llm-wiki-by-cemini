---
title: "BTTF: Rethinking EDA infrastructure for agentic systems in chip design verification (arXiv 2610.06790)"
type: source
tags: [source, k283, arxiv, agents, harness, text-to-sql]
keywords: [bttf, eda, waveform, sqlite, multi-agent, text-to-sql, coverage-pruning]
related:
  - concepts/k283-arxiv-wave.md
  - concepts/agent-native-research-artifacts.md
maturity: draft
created: 2026-10-06
updated: 2026-10-06
read_status: read
---

## Relations

- @concepts/k283-arxiv-wave.md
- @concepts/agent-native-research-artifacts.md

## Raw Concept

| Title | Back to the Future: Rethinking EDA Infrastructure for Agentic Systems in Chip Design Verification |
| Authors | Je Yang (Columbia), Ivan Lobov (Google DeepMind), Thomas Karpati (Google) |
| Type | arXiv preprint (cs.AI) |
| Venue | NeurIPS 2026 AI-for-Chip-Design workshop |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2610.06790-back-to-the-future-rethinking-eda-infrastructure.pdf` |
| Retrieved | 2026-10-06 |
| arXiv | 2610.06790v1 |
| read-status | read |

## Narrative

Chip-design waveform dumps run to **terabytes** of VCD/FSDB. An LLM cannot read them. **BTTF** recasts the dump into a **normalised relational SQLite database** (`waves.db`: `signal_metadata` + `signal_changes`) and lets a multi-agent engine answer natural-language verification questions with **schema-aware SQL**.

### Pipeline

- **Offline:** coverage-aware pruning — clock pruning, on-the-fly ZERO/AVG **inactive-signal** pruning, batched insertion.
- **Online:** an **Orchestration Agent** routes to an **Analysis Agent** (multi-query SQL), a **Verification Agent** (SVA rules via REGEX), and an **Evaluation Agent** (5-criteria audit), over a shared session context.

### Results

- **95.33% execution accuracy** on a 150-query benchmark.
- Clock pruning: **−66.20% footprint**, **3.28× lower latency**, 98.51% coverage retained.
- ZERO pruning: **−72.18% footprint** at 100% coverage.
- Below-average pruning: −86.97% footprint but only 64.23% coverage.
- Batched insertion: **2.89×** faster DB build.
- **Multi-agent beats single-agent by 17.3%** on a quality audit (single-agent 3.35/5.00), at 1.96× latency overhead.

### Why it matters here

The transferable idea is **"put the data in a queryable relation, then let agents write SQL."** That is exactly the shape of a research-corpus interface — and it echoes `agent-native-research-artifacts`. Note: "EDA" here is electronic design automation, **not** exploratory data analysis. No finance, prediction-market, security, or Minecraft hook.

**No license stated; no code.**

## Snippets

> "Multi-agent orchestration beats a single-agent baseline by 17.3% on a quality audit, at 1.96× latency overhead." [Source: arxiv-2610.06790-back-to-the-future-rethinking-eda-infrastructure.pdf]

> "Clock pruning cut footprint by 66.20% with 3.28× lower latency while retaining 98.51% coverage." [Source: arxiv-2610.06790-back-to-the-future-rethinking-eda-infrastructure.pdf]
