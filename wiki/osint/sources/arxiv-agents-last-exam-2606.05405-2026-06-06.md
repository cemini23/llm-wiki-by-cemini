---
title: Agents' Last Exam — GDP-scale agent benchmark (arXiv 2606.05405)
type: source
tags: [source, arxiv, agent-evaluation, benchmark, k101]
keywords: [2606.05405, ale, agents-last-exam, long-horizon, gdp-val, verifiable-workflows]
related:
  - concepts/agents-last-exam-benchmark.md
  - concepts/system-scaling-harness-evaluation.md
  - concepts/agent-memory-pipeline-eval-rubric.md
  - concepts/conductor-orchestrator.md
  - concepts/high-signal-paper-patterns.md
maturity: validated
read_status: deep-read
created: 2026-06-06
updated: 2026-06-06
---

## Relations

- @concepts/agents-last-exam-benchmark.md — OSINT synthesis (5-task finance slice deep-read)
- @concepts/system-scaling-harness-evaluation.md — harness is first-order; ALE scores full professional workflows
- @concepts/conductor-orchestrator.md — Cemini multi-tool fan-out is an ALE-class long-horizon harness candidate

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Agents' Last Exam |
| **Authors** | Sun et al. (UC Berkeley; Dawn Song lab + 250+ industry contributors) |
| **arXiv** | 2606.05405 |
| **Location** | `cemini-librarian:/opt/cemini-bulk/research/arxiv-2606.05405-agents-last-exam.pdf` |
| **Retrieved** | 2026-06-06 |
| **Read status** | **deep-read** — paper + `rdi-berkeley/agents-last-exam` task cards (quant/finance slice) |
| **Public repo** | https://github.com/rdi-berkeley/agents-last-exam (Apache-2.0) |

## Narrative

**Problem:** Benchmark wins have not translated into **GDP-relevant deployment**. ALE scores **Generalist CUA-agents** (GUI + CLI + long horizon) on expert-shipped workflows with **deterministic** `evaluate()` — not exam-style QA.

**Scale [CONFIRMED]:** 1,490 instances / 55 subdomains; public split **150 tasks** in Near-Term (59) / Full-Spectrum (55) / Last-Exam (35). ~$3–10 per task run.

**Finance evaluation modes [CONFIRMED]:** structured tabular manifests (`finance/sec_10k_financial_parsing`), workbook byte scoring + formula gates (`finance/equity_research_summary`), exact JSON field match (`financial_stmt_reconstruction_aapl_fy2024`). Finance tasks **avoid** holistic LLM-judge where possible (Appendix C.3.4).

**Business & Finance public tasks (5)** — see `@concepts/agents-last-exam-benchmark.md` for per-task specs. Only `american_option_pricing_ls` carries subdomain **Quantitative Finance & Trading**; others are accounting / enterprise analytics / compliance — still finance-relevant for Cemini harness design.

**Cemini routing:** **REFERENCE** — steal gate-and-score + evidence-on-deliverable discipline for ingest/federation/cross-venue smoke tests. **Not** a PM alpha or live-trading benchmark. Repo task cards browsable at https://agenthle.org/demo (ALE-V1 split).

Contrast: GDP-val (human judge, 16/55 domains), Terminal-Bench (Codex 82% vs ALE-CLI 25.2% pass).

## Snippets

> "This paper introduces Agents' Last Exam (ALE), a benchmark designed to evaluate AI agents on long horizon, economically valuable, real world tasks with verifiable outcomes."

> "Across mainstream harness and backbone configurations, the average full pass rate is 2.6%."

> — [Source: arxiv-2606.05405-agents-last-exam.pdf abstract, retrieved 2026-06-06]

> "Benchmarks do not merely record capability; they focus research attention, define engineering targets, and often determine which domains become tractable for rapid improvement."

> — [Source: arxiv-2606.05405-agents-last-exam.pdf §1, retrieved 2026-06-06]
