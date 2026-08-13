---
title: "FrontierFinance — 220-Query Finance-Agent Benchmark (Samaya AI)"
type: source
tags: [arxiv, k235, finance, benchmark, llm-agents, eval]
keywords: [2608.11683, FrontierFinance, Samaya, finance-agents, rubrics, investor-workflow, Fable-5, Kimi-K3]
related:
  - concepts/agent-toolkit-routing-research-backlog.md
  - concepts/active-project-research-routing.md
maturity: draft
created: 2026-08-13
updated: 2026-08-13
read_status: skimmed
---

## Relations

- @concepts/agent-toolkit-routing-research-backlog.md — K235 bump: harness-beats-model evidence
- @concepts/active-project-research-routing.md — eval posture, not a prod dump

## Raw Concept

| Field | Value |
|-------|--------|
| arXiv | 2608.11683 (cs.AI, 2026-08-12) |
| Authors | Zhang, Koyluoglu, Venkatesh, Diehl Martinez, Bhatia, Alidoust, Paranjape (Samaya AI) |
| sha256 | `8ef31c13b1ca0c248c40f446bad5c72143efcaed2d60dfcdcb09b9919aeda15b` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2608.11683-frontierfinance-a-challenging-benchmark-for-meas.pdf` |
| retrieved | 2026-08-13 |

## Narrative

Open benchmark of **220 expert-crafted queries + 11,543 source-attributed binary rubrics** across six investor-workflow use cases (screening & discovery, company/market research, financial data extraction, portfolio tracking, catalyst monitoring, sector/industry & macro). Four-stage expert curation (former buy-side/sell-side/IB analysts); scoring = rubric qualification rate via three independent LLM judges; common harness restricted to public data.

Headline results: **harness, not model, drives quality and efficiency** — Samaya in-house system 56.0% vs strongest frontier model under open harness (Claude Fable 5) 49.2% at ~2.2× lower cost; best open-weight (Kimi K3) 46.4% at ~4.5× lower cost. Hardest use cases: Screening & Discovery (best 33%) and Sector/Industry & Macro (best 39%).

**Routing: wiki/eval only — no prod scp.** No XSP/LEAPS hook (this is analyst-workflow benchmarking, not options-flow execution); do not dump into prod briefs MAPPO-style. Value for this workspace: (1) confirms the harness-over-model thesis the /route + CCC lanes already track; (2) a candidate eval surface if a finance-research agent layer ever gets built for xsp/GuruWatcher.

[Source: arXiv:2608.11683]

## Snippets

> "the tool harness, not the model alone, strongly shapes quality and efficiency" [Source: arXiv:2608.11683 p.1]

> "the best open-weight model (Kimi K3, 46.4%) nearly matches the best proprietary model at 4.5× lower cost" [Source: arXiv:2608.11683 p.1]
