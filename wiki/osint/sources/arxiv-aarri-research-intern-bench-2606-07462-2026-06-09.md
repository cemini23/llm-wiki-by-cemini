---
title: "Act As a Real Researcher — AARRI-Bench (arXiv 2606.07462, 2026)"
type: source
tags: [source, agent-evaluation, harness, benchmark, k107]
keywords: [aarri-bench, aarr, research-intern, agentic-harness, mini-swe-agent, research-ethics, field-sensitivity]
related:
  - entities/tools/aarri-bench.md
  - concepts/conductor-orchestrator.md
  - sources/arxiv-agents-last-exam-2606.05405-2026-06-06.md
  - sources/agentic-harness-engineering.md
  - sources/trading-posts-compilation-7-2026-06-09.md
  - "@ccc-wiki/briefs/2026-06-09_k107-ccc-dynamic-workflows-skills-from-osint.md"
maturity: draft
read_status: read
created: 2026-06-09
updated: 2026-06-09
clusters: [llm-agents, agent-harness]
---

## Relations

- @entities/tools/aarri-bench.md — GitHub repo + Phase-0 verdict
- @concepts/conductor-orchestrator.md — eval discipline for routing/harness
- @sources/arxiv-agents-last-exam-2606.05405-2026-06-06.md — macro execution benchmark sibling
- @sources/agentic-harness-engineering.md — RocketSmith harness patterns (K105)

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Act As a Real Researcher: A Suite of Benchmarks Evaluating Frontier LLMs and Agentic Harnesses in Research Lifecycle |
| **Authors** | Wang et al. (Xi'an Jiaotong + Xidian) |
| **arXiv** | 2606.07462 |
| **Repo** | https://github.com/AARR-bench/AARRI-bench |
| **PDF** | `cemini-librarian:/opt/cemini-bulk/research/arxiv-aarri-research-intern-bench-2606-07462-2026-06-09.pdf` |
| **Retrieved** | 2026-06-09 |
| **Read status** | read (abstract + intro) |

## Narrative

**AARR** (Act As a Real Researcher) benchmark series targets **granular research professionalism** — ethics, field sensitivity, nuance — not macro coding throughput. **AARRI-Bench** (research intern tier) is first release.

Best config reported: Mini-SWE-Agent + Claude Opus 4.7 at **68.3%** — failures are "obvious to human researchers" detail misses. Conclusion: researcher-like AI needs **research behavior** exploration, not only scaffolding complexity.

**Phase-0 (2026-06-09):** repo **NO-GO** for install — **no LICENSE** on GitHub (`gh api` null; `/license` 404); ~2★; pushed 2026-06-09. **REFERENCE** benchmark only; track for license fix.

**Cemini steal:** use task rubric shape (field sensitivity + ethics gates) to extend `skill_audit.py` / brief-audit veto dimensions — do not clone repo until licensed [TENTATIVE 2026-06-09].

## Snippets

> "Even the best-performing configuration (Mini-SWE-Agent with Claude Opus 4.7) achieves only 68.3% success rate, frequently overlooking subtle yet critical details that are obvious to real human researchers." [Source: arxiv-2606-07462-act-as-a-real-researcher-a-suite-of-benchmarks-e.pdf Abstract]
