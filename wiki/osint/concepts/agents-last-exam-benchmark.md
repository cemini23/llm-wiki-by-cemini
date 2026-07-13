---
title: Agents' Last Exam (ALE) — long-horizon professional agent benchmark
type: concept
tags: [concept, agent-evaluation, benchmark, reference, k101]
keywords: [ale, agents-last-exam, 2606.05405, gdp-relevant, verifiable-workflows, quant-finance-slice]
related:
  - concepts/psychological-competence-ai-evaluation.md
  - sources/arxiv-psychological-competence-ai-eval-2607.08285-2026-07-13.md
  - sources/arxiv-agents-last-exam-2606.05405-2026-06-06.md
  - concepts/system-scaling-harness-evaluation.md
  - concepts/agent-memory-pipeline-eval-rubric.md
  - concepts/conductor-orchestrator.md
  - concepts/high-signal-paper-patterns.md
  - concepts/cemini-knowledge-application-architecture.md
maturity: draft
created: 2026-06-06
updated: 2026-07-13
---

## Relations

- @sources/arxiv-agents-last-exam-2606.05405-2026-06-06.md — arXiv 2606.05405 (deep-read quant slice 2026-06-06)
- @concepts/system-scaling-harness-evaluation.md — subsystem harness vs whole-workflow pass rate

## Narrative

**REFERENCE** [CONFIRMED] — Berkeley RDI + 300+ experts; **1,490 task instances** / 55 subdomains / 13 domains; **deterministic scoring** (not holistic LLM-judge) on expert-shipped workflows. Public eval set: **150 tasks** in three tiers ($3–10 per task run).

**Saturation [CONFIRMED]:** mainstream harness average **full pass 2.6%**; Last-Exam tier often **0%** for Claude Code + Opus 4.7. **Model choice ≈ 3× harness spread** among well-engineered systems (Appendix D.4). Dominant failure mode: **domain knowledge** (~75% Understanding + Approach) — agents script around GUI tools instead of using intended professional software.

### Business & Finance slice — 5 public tasks [CONFIRMED]

Task specs from `rdi-berkeley/agents-last-exam` (`tasks/business_finance/*/task_card.json`, Apache-2.0, 2026-06-06).

| Task ID | Tier | Subdomain | Workflow | Cemini mapping |
|---------|------|-----------|----------|----------------|
| `financial_stmt_reconstruction_aapl_fy2024` | Near-Term | Accounting & Finance | Extract AAPL FY2024 balance sheet from staged 10-K → `balance_sheet.json` (exact field match) | **Steal-from** — structured filing extraction discipline for wiki entity updates; not live trading |
| `equity_research_summary` | Full-Spectrum | Enterprise Analytics | Windows VM: LibreOffice Calc + Yahoo Finance live + SEC FY2023 Tesla workbook; formula gates via `openpyxl` | **REFERENCE** — parallels earnings-preview / yfinance skills; live Yahoo cells scored for presence only |
| `american_option_pricing_ls` | Full-Spectrum | **Quantitative Finance & Trading** | 3-tier MC + Longstaff-Schwartz American put + 5-asset basket Greeks; NumPy/SciPy only | **REFERENCE** — quant code quality bar; **no PM alpha**; only 1 task tagged `quant_finance` in repo |
| `sec_10k_financial_parsing` | Last-Exam | Accounting & Finance | 100-filing corpus → normalized JSON + raw evidence + 3 analytical Qs + deterministic rerun subset; weighted verifier (pass ≥0.75) | **Steal-from** — bulk SEC ingest + evidence trail ≈ librarian bulk + source pages; too heavy for prod cadence |
| `sse_northbound_programmatic_trading_01` | Near-Term | Compliance & Regulatory | Closed-book Chinese SSE northbound reporting Q&A → structured JSON with exact citation snippets | **REFERENCE** — regulatory memo pattern; **not** Polymarket/Kalshi execution |

**OSINT verdict:** ALE quant/finance tasks test **research analyst + compliance + numerical implementation** workflows — not prediction-market microstructure. Use as **internal harness labels** for wiki ingest / federation / cross-venue rituals, not prod leaderboard optimization.

### Cemini "mini-ALE" smoke candidates [TENTATIVE]

| Ritual | ALE analogue |
|--------|----------------|
| Full wiki ingest (preingest → 3–15 pages → `ingest_session_gate`) | Structured deliverable + gate-and-score |
| Federation morning summary triage | Long-horizon multi-tool VM workflow |
| `cross-venue-scan --once` + fee-adjusted gate | Tabular manifest tolerance scoring |
| `skill_audit.py` before prod brief | Hard gates before partial credit |

**Do not:** run full ALE public set on prod paths; adversarial benchmark gaming is an active research topic (Dawn Song BenchJack note, 2026).

## Snippets

> "Structured tabular / numeric… dominant in finance, accounting, and clinical-data-standards task workflows."

> — [Source: arxiv-2606.05405-agents-last-exam.pdf Appendix C.3.2, retrieved 2026-06-06]

> "Understanding and Approach failures together account for roughly three quarters of cases, indicating that the dominant bottleneck is domain knowledge rather than execution capability."

> — [Source: arxiv-2606.05405-agents-last-exam.pdf §4.2, retrieved 2026-06-06]
