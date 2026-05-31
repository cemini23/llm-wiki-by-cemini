---
title: "Agentic Trading — LLM agents in financial markets survey + reproducibility audit (arXiv:2605.19337)"
type: source
tags: [source, arxiv, llm-agents, trading-agents, survey, reproducibility, k87]
keywords: [agentic-trading, evidence-mapping, closed-loop-evaluation, protocol-incomparability, architecture-capability-adaptation, expert-system-pipeline]
clusters: [llm-agents, quant-finance]
related:
  - concepts/llm-agent-systems.md
  - concepts/rl-marl-research.md
  - concepts/regime-conditioned-evaluation.md
  - sources/tradingagents.md
  - sources/arxiv-code-as-agent-harness-survey-2605.18747.md
maturity: validated
read_status: skimmed
created: 2026-05-30
updated: 2026-05-30
---

## Relations

- @concepts/llm-agent-systems.md — canonical audit-oriented survey of LLM trading agents (77-study ledger)
- @concepts/regime-conditioned-evaluation.md — protocol incomparability finding reinforces regime/split disclosure discipline
- @sources/tradingagents.md — primary empirical benchmark cited; classified under Architecture–Capability–Adaptation lens
- @sources/arxiv-code-as-agent-harness-survey-2605.18747.md — complementary harness survey (coding agents vs trading agents)

## Raw Concept

- **Title**: Agentic Trading: When LLM Agents Meet Financial Markets
- **Authors**: Yihan Xia, Panpan You, Taotao Wang (corresponding), Fang Liu, Han Qi, Xiaoxiao Wu, Shengli Zhang — Shenzhen University
- **Type**: arXiv preprint — arXiv:2605.19337 (59 pages)
- **Submitted**: 2026-05-19
- **Retrieved**: 2026-05-30 (Tier-2 sweep `@sweeps/2026-05-30.md`, Tier-A)
- **Pages**: 59
- **Read status**: skimmed (abstract + protocol + selection summary)
- **Location**: `cemini-librarian:/opt/cemini-bulk/research/2605.19337_agentic-trading-llm-survey.pdf`

## Narrative

Reframes LLM trading systems as **expert-system decision pipelines** (perception → memory → reasoning → action/execution → audit) and presents an **evidence map** of 77 included studies (92 candidate registry, screened through 2026-03-09). Primary empirical subset **n = 19** requires **Action Output + Closed-Loop Evaluation**; remaining 58 are background/design context.

**Central empirical finding [CONFIRMED — authors' coded audit]:** **protocol incomparability** in the primary subset: only **2/19** report extractable time-consistent splits; **1/19** explicit transaction-cost model; **1/19** universe/survivorship handling; **11/19** execution timing/semantics; **15/19** coded R0 reproducibility; **0/19** reach R3. Architecture–Capability–Adaptation (A-C-A) is offered as an exploratory analytical lens, not a validated taxonomy.

**Cemini relevance:** Reference standard for **promotion-gate design** — any CeminiSuite LLM-trading or copy-bot evaluation should meet the reporting checklist this paper derives (splits, costs, execution semantics, artifacts). Positions `@sources/tradingagents.md` as architecturally influential but empirically under-audited relative to the field's own bar. No code adoption — survey + checklist only.

## Snippets

> "The central empirical finding is protocol incomparability: within the primary subset, only 2/19 studies report extractable time-consistent split protocols, 1/19 reports an explicit transaction-cost model … 15/19 are coded as R0, and no study reaches R3 reproducibility."
> — [Source: 2605.19337_agentic-trading-llm-survey.pdf p.1]

> "We therefore use Architecture–Capability–Adaptation as a working analytical lens rather than a validated taxonomy, and we foreground the evidence ledger, reproducibility audit, and reporting checklist as the main contributions."
> — [Source: 2605.19337_agentic-trading-llm-survey.pdf p.1]

> "Included evidence-mapping set … partitioned into 19 primary empirical studies and 58 background/context records."
> — [Source: 2605.19337_agentic-trading-llm-survey.pdf p.5]
