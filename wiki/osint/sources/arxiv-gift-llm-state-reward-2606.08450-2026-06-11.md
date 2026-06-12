---
title: GIFT — LLM-guided state-reward interface for financial RL (arXiv 2606.08450)
type: source
tags: [source, arxiv, financial-rl, portfolio, llm, reward-shaping, ppo]
keywords: [2606.08450, GIFT, FSE, RRS, DGR, portfolio-management, state-reward-interface]
related:
  - concepts/llm-guided-financial-rl-interface.md
  - entities/tools/gift-finrl.md
  - concepts/llm-agent-systems.md
maturity: validated
read_status: skimmed
created: 2026-06-11
updated: 2026-06-11
---

## Relations

- @concepts/llm-guided-financial-rl-interface.md — synthesis hub
- @entities/tools/gift-finrl.md — Phase-0 NO-GO (no license on GitHub)
- @concepts/llm-agent-systems.md — constrained LLM use (design interface, not trade)

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | GIFT: LLM-Guided State-Reward Interface for Financial Reinforcement Learning |
| **arXiv** | 2606.08450 |
| **Repo** | https://github.com/KAG778/GIFT |
| **sha256** | `9a2b84ae74c705ea8dfc1d47259ca423e84ee79d9041ef125be3b79584d3ee22` |
| **Location** | `cemini-librarian:/opt/cemini-bulk/research/arxiv-2606.08450-gift-llm-guided-state-reward-interface-for-finan.pdf` |
| **Retrieved** | 2026-06-11 |
| **Read status** | skimmed — abstract, method overview, diagnostic motivation figure |

## Narrative

**GIFT** uses an LLM to design (not execute) the state–reward interface for PPO portfolio trading. Three guided components:

1. **FSE** — factor-guided state enhancement from momentum/vol/downside/liquidity/mean-reversion primitives
2. **RRS** — risk-rule-guided reward shaping (drawdown, turnover, diversification auxiliaries)
3. **DGR** — diagnostic-guided refinement via PPO rollouts feeding slope, autocorrelation, SNR back to the LLM

Guided LLM-PPO beats free-form LLM-PPO and vanilla PPO on training-signal diagnostics (Figure 1). Claim: raw OHLCV + short-horizon return is under-specified in non-stationary markets.

**Cemini mapping:** REFERENCE for **offline interface design** loops — analogous to conductor/kb context engineering (K110) but for FinRL env builders. Do **not** adopt repo (Phase-0 NO-GO). Steal pattern: constrain LLM to structured factor library + rollout diagnostics, never open-ended trade generation.

## Snippets

> "Rather than using the LLM to make trading decisions, GIFT uses Factor-guided State Enhancement … Risk-rule-guided Reward Shaping … and Diagnostic-guided Refinement."

> — [Source: arxiv-2606.08450-gift-llm-guided-state-reward-interface-for-finan.pdf Abstract, retrieved 2026-06-11]
