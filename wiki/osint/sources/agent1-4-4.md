---
title: "Sovereign-OS: A Charter-Governed Operating System for Autonomous AI Agents with Verifiable Fiscal Discipline"
type: source
tags: [pdf, llm-agents, k49]
clusters: [llm-agents]
related:
  - concepts/llm-agent-systems.md
maturity: validated
read_status: deep-read
created: 2026-04-23
updated: 2026-05-16
---

## Relations

- @concepts/llm-agent-systems.md — cluster hub for LLM agent-systems research in the Cemini corpus

## Raw Concept

- **Original title**: Sovereign-OS: A Charter-Governed Operating System for Autonomous AI Agents with Verifiable Fiscal Discipline
- **Author(s)**: Aojie Yuan, Haiyue Zhang, Yue Zhao (University of Southern California); Ziyi Wang (University of Maryland)
- **Type**: PDF
- **Location**: research for cemini/agent1 4:4.pdf
- **Retrieved**: 2026-04-23 (filename date reflects download date, not publication)
- **Length**: 12p
- **Read status**: deep-read
- **Primary cluster**: llm-agents
- **All clusters**: llm-agents

## Narrative

As AI agents evolve from text generators into autonomous economic actors that accept jobs, manage budgets, and delegate to sub-agents, the absence of *runtime* governance becomes a critical gap. Orchestration frameworks (LangChain, CrewAI, AutoGen, MetaGPT) impose no fiscal constraints, require no earned permissions, and offer no tamper-evident audit trail. The paper introduces **Sovereign-OS**, a governance-first operating system that places every agent action under constitutional control.

The architecture has five layers. A declarative **Charter** (Pydantic-validated YAML, `extra="forbid"`) defines mission scope, core competencies, fiscal boundaries (daily burn cap, total budget, minimum job margin — default 0.35), and measurable success KPIs. A **CEO/Strategist** decomposes goals into dependency-aware task DAGs. A **CFO/Treasury** gates every expenditure against balance, daily burn cap, and per-job profitability floor (`cost > revenue × (1 − min_margin)` → reject) before any tokens are consumed, and runs an auction-based BiddingEngine scored by a utility function `U = (confidence/cost) × P × (TrustScore/100)`. **Workers** operate under a dynamic **TrustScore** (0–100, base 50, asymmetric +5 success / −15 failure) with tiered capability thresholds — READ_FILES at 10, EXECUTE_SHELL at 60, SPEND_USD at 80. An **Auditor/ReviewEngine** verifies outputs against Charter KPIs and seals each report with a SHA-256 proof hash in an append-only ledger.

Evaluation: 100% block rate on 30 fiscal-violation scenarios, 94% correct permission gating over 200 trust-escalation missions, and zero integrity failures across 1,200+ audit reports. Stripe integration closes the loop to real payment.

For Cemini, Sovereign-OS is directly relevant to **autonomous trading-agent governance**: the Charter-driven fiscal-discipline pipeline, earned-autonomy TrustScore gating, and cryptographically verifiable audit trail are a concrete blueprint for constraining an autonomous economic agent's spend, permissions, and accountability at runtime.

## Snippets

> "A declarative Charter (YAML) defines mission scope, fiscal boundaries, and success criteria. A CEO (Strategist) decomposes goals into dependency-aware task DAGs; a CFO (Treasury) gates each expenditure against budget caps, daily burn limits, and profitability floors via an auction-based bidding engine."
> [Source: agent1 4:4.pdf p.1]

> "Across our evaluation suite, Sovereign-OS blocks 100% of fiscal violations (30 scenarios), achieves 94% correct permission gating (200 trust-escalation missions), and maintains zero integrity failures over 1,200+ audit reports."
> [Source: agent1 4:4.pdf p.1]

> "TrustScore updates are asymmetric: each audit success adds +5 (capped at 100), each failure subtracts −15 (floored at 0), and budget overruns subtract −10."
> [Source: agent1 4:4.pdf p.3]
