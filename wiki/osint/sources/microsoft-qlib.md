---
title: "microsoft/qlib — AI-Oriented Quantitative Investment Platform (Python, MIT, 40.3k ★)"
type: source
tags: [github, quant-finance, ml-platform, reinforcement-learning, supervised-learning, market-dynamics-modeling, microsoft, mit-license, cemini-adopt-candidate, ip-sale-clean, gemini-dr-wave4]
keywords: [qlib, microsoft-qlib, ai-quant-investment-platform, supervised-learning, market-dynamics, reinforcement-learning, rd-agent, llm-driven-auto-quant-factory, krnn-sandwich-models, hist-igmtf, point-in-time-database, arctic-provider-backend, meta-learning-ddg-da, planning-portfolio-optimization, cemini-rl-marl-retrain]
clusters: [quant-finance, ml-methods, infrastructure]
related:
  - sources/gemini-dr-wave4a-cemini-stack-2026-04-29.md
  - sources/gemini-dr-wave5a-cemini-stack-2026-04-30.md
  - sources/shiyu-coder-kronos.md
  - concepts/quant-finance.md
  - concepts/ip-sale-readiness.md
  - concepts/high-signal-paper-patterns.md
  - concepts/mappo.md
maturity: validated
read_status: read-skim
created: 2026-04-29
updated: 2026-04-30
---

## Relations

- @sources/gemini-dr-wave4a-cemini-stack-2026-04-29.md — Wave 4A canonical brief; URL 28 Adopt; promoted to dedicated source this session as the strongest Cemini-stack adoption candidate from Wave 4
- @concepts/quant-finance.md — primary cluster: quant-finance ML platform
- @concepts/ip-sale-readiness.md — MIT license clears IP-sale checks; Microsoft Corporation copyright holder; clean for institutional-grade adoption
- @concepts/high-signal-paper-patterns.md — rubric-validated: 40k stars + 23 releases + 8 months continuous active development + 120+ contributors = strongest maturity signals in Wave 4
- @concepts/mappo.md — qlib's RL framework provides off-the-shelf MAPPO/CTDE infrastructure that Cemini's current MAPPO-34-vector retrain pipeline could swap onto
- @sources/gemini-dr-wave5a-cemini-stack-2026-04-30.md — Wave 5A successor brief; flags qlib as the **operational pair for Kronos** (qlib does data-prep + backtest harness; Kronos does foundation-model layer)
- @sources/shiyu-coder-kronos.md — operational pair: Kronos's KronosTokenizer feeds discrete tokens into qlib's signal pipeline; both MIT-licensed; both Cemini-stack-aligned. Cemini integration recipe: Qlib data → KronosTokenizer → custom downstream predictor (NOT KronosPredictor as-shipped, per author production-readiness disclaimer).

## Raw Concept

- **URL**: https://github.com/microsoft/qlib
- **Type**: Open-source repository / Python library
- **License**: MIT (Exa-verified 2026-04-29 against `github.com/microsoft/qlib/blob/main/LICENSE` — Microsoft Corporation copyright)
- **Stars / Forks (Exa-verified 2026-04-29)**: 40,300 ★ / 6,300 forks / 23 releases
- **Latest release**: v0.9.7 (2025-08-15)
- **Stack**: Python primary; Linux/Windows/macOS supported
- **Org**: Microsoft (microsoft/qlib repo, AI4Science/Quant team)
- **Created**: 2020-08-14; very mature project (~5.5 years of development)
- **Companion**: https://github.com/microsoft/RD-Agent (LLM-driven Auto Quant Factory)
- **Discovered via**: Gemini DR Wave 4A 2026-04-29 (URL 28); promoted to dedicated source page same session
- **Read status**: read-skim (Exa-fetched README + LICENSE + recent feature highlights; deep-read deferred until Cemini integration scoping)

## Narrative

### What it is

Microsoft's open-source AI-oriented **quantitative investment platform**. Designed to let quant researchers go from idea exploration to production implementation using AI/ML techniques. Supports three modeling paradigms in a single integrated framework:

1. **Supervised learning** — KRNN, Sandwich models (May 2023), HIST + IGMTF models (Apr 2022), ADD model, ADARNN, TCN, Tabular RNN, etc.
2. **Market dynamics modeling** — meta-learning-based framework with DDG-DA (Jan 2022)
3. **Reinforcement learning** — full RL Learning Framework (Nov 2022) including PPO/DDPG/TD3 over financial environments; Nested Decision Framework (Oct 2021); planning-based portfolio optimization (Dec 2021)

### Recent feature evolution (per qlib/main README)

- **🔥 LLM-driven Auto Quant Factory** (released in companion RD-Agent, Aug 2024) — applies LLM agents to automate quant R&D. Direct precedent for Cemini's analyst-orchestrator pattern.
- **R&D-Agent-Quant** integration (in-progress, "Apply R&D-Agent to Qlib for quant trading")
- **BPQP for End-to-end learning** (under review)

### Why Cemini-direct

1. **RL-MARL retrain pipeline fit**: Cemini's MAPPO-34-vector retrain pipeline (per `@concepts/mappo.md`) is currently a custom implementation. qlib provides off-the-shelf RL infrastructure for financial environments — could either replace Cemini's custom pipeline OR be used as a methodology reference.
2. **Point-in-Time database** (released Mar 2022) — solves the standard "training-data-leakage from future-information" problem in backtesting. Useful methodology reference for Cemini's TimescaleDB-based backtest infrastructure.
3. **Arctic Provider Backend + Orderbook data example** (Jan 2022) — Cemini ingests Polygon options chains; qlib's orderbook data example provides a reference implementation for high-frequency data handling.
4. **LLM-driven Auto Quant Factory** (RD-Agent integration) — directly relevant to Cemini's analyst-orchestrator: "agent that automates quant R&D" is the same pattern as "agent that runs analyst-driven research". Cross-pollinate.
5. **License**: MIT, Microsoft-stewarded → IP-sale-readiness clean. No poison-pill family A or B concerns (per `@concepts/ip-sale-readiness.md`).

### Cemini-side adoption assessment

**Decision**: Watch + experiment, not full-replace. The Wave 4A brief recommends Adopt; the Cemini-pragmatic verdict is to start with experiments rather than wholesale dependency.

Concrete next-steps:
1. **Clone qlib + run the published examples** on a side environment (laptop, separate from production). ~half-day.
2. **Compare qlib's RL framework against Cemini's MAPPO-34-vector pipeline** on a held-out backtest period. Decide whether to swap or keep custom. ~1-2 days.
3. **Read R&D-Agent companion repo** (`github.com/microsoft/RD-Agent`) — particularly the Auto Quant Factory module. Compare the pattern against Cemini's analyst-orchestrator architecture. ~1 day.
4. **License audit + dependency tree audit** before any production use. Cemini's IP-sale-readiness threshold requires clean SBOM. ~half-day.
5. **If experiments validate**: brief to cemini-prod for formal adoption with specific module scope (RL framework + Point-in-Time DB pattern most likely; full platform replacement less likely).

### Risks & open questions

1. **Microsoft as upstream**: very stable, but very large project. Customization for Cemini's specific architecture (Hetzner CPX21, 7GB RAM, FastAPI orchestrator) may require non-trivial config work.
2. **Documentation depth vs Cemini-specific use cases**: qlib documents general quant-investment workflows; Cemini's specific (multi-agent orchestration + DeepSeek API + Kalshi/Polymarket coupling) isn't a standard qlib use case. Adaptation required.
3. **R&D-Agent dependency** [NEEDS VERIFICATION 2026-04-29] — RD-Agent integration is in-progress per the README. Maturity of the R&D-Agent companion repo + its license should be verified separately before relying on the LLM-driven Auto Quant Factory feature.
4. **Compute requirements**: qlib's RL training is not lightweight. Cemini's CPU-only Hetzner host (7 GB RAM ceiling) may not be the right home for qlib RL training. Consider laptop-side training + production-deployed inference-only.

### Citation

> Microsoft. (2020-2025). *Qlib: An AI-oriented Quantitative Investment Platform*. https://github.com/microsoft/qlib (MIT License; v0.9.7 latest release 2025-08-15)

## Snippets

> **qlib's mission framing (per repo description)**:
>
> "Qlib is an AI-oriented Quant investment platform that aims to use AI tech to empower Quant Research, from exploring ideas to implementing productions. Qlib supports diverse ML modeling paradigms, including supervised learning, market dynamics modeling, and RL, and is now equipped with https://github.com/microsoft/RD-Agent to automate R&D process." [Source: https://github.com/microsoft/qlib README, retrieved 2026-04-29 via Exa]

> **The platform's core paradigm framing**:
>
> "Qlib is an open-source, AI-oriented quantitative investment platform that aims to realize the potential, empower research, and create value using AI technologies in quantitative investment, from exploring ideas to implementing productions. Qlib supports diverse machine learning modeling paradigms, including supervised learning, market dynamics modeling, and reinforcement learning." [Source: https://github.com/microsoft/qlib README, retrieved 2026-04-29 via Exa]
