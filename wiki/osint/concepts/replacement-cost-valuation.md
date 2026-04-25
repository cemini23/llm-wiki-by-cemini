---
title: Replacement-cost valuation
type: concept
tags: [concept, m-and-a, valuation]
keywords: []
related:
  - sources/3-10-cryptographic-research.md
  - sources/3-10-algorithmic-trading-ip-sale-audit.md
  - sources/3-19-ip-sale-research.md
  - concepts/ip-sale-readiness.md
  - entities/components/kelly-cvar-risk-engine.md
maturity: validated
created: 2026-04-23
updated: 2026-04-24
---

## Relations

- @sources/3-10-cryptographic-research.md
- @sources/3-10-algorithmic-trading-ip-sale-audit.md
- @sources/3-19-ip-sale-research.md — primary valuation methodology recommended for pre-revenue quant IP; sets the floor for the base+earnout deal structure
- @concepts/ip-sale-readiness.md
- @entities/components/kelly-cvar-risk-engine.md

## Raw Concept

Synthesized across 2 source(s) in the Cemini research corpus that reference this concept directly or by equivalent terminology.

## Narrative

**[CONFIRMED — 2026-04-24 Track C audit] doc-only** — Valuation methodology / APA deliverable, not software. No engineering milestone; no code walk required. Gap memo: `briefs/track-c-walk-results.md`.

**Replacement-cost valuation** is the framing the IP-sale research
recommends as the primary valuation anchor for the Cemini Financial
Suite — independent of P&L track record.

### The argument
An institutional buyer who decides to build an equivalent multi-asset
algorithmic-trading platform in-house would need, conservatively: 3–5
senior quants + 2 infra/devops engineers + 1 compliance lead + access
to TimescaleDB/Hyperliquid/Kalshi/OANDA integrations + a verified
Merkle-anchored audit trail + documented RL-research program + a
cryptographically-provable backtest record. `[RETRACTED 2026-04-24]`
Earlier phrasing included "a trained DeepSeek-R1 reasoning harness" in
the replacement-cost line-item; DeepSeek/Ollama are not deployed (see
@entities/infrastructure/deepseek-r1-14b.md), so the IP-sale
replacement-cost envelope should not bake in an LLM harness that
doesn't exist.

Replacement-cost estimate per the 3-10 cryptographic audit runs to
18–24 person-months of senior engineering effort + 6–9 months of
real-money paper-trading to generate a comparable track record. At
loaded senior-engineer costs + opportunity cost of delay, the
replacement envelope sits in the low-to-mid seven figures.

### Why this beats DCF or multiple-of-earnings
Cemini is pre-revenue for acquisition purposes. Multiples-of-earnings
on a prop book are distorted by leverage and regime. Replacement cost
gives both sides an auditable number that doesn't depend on projecting
out-of-sample returns — which an acquirer's risk-committee will
haircut aggressively anyway.

### Floor-price vs ceiling
Replacement cost is the floor. The ceiling is set by the acquirer's
own strategic value: the cost of NOT having the platform when a
competitor launches theirs. The IP-sale negotiation playbook structures
this as a base price (replacement-anchored) + earnout tiers tied to
strategy performance on the acquirer's capital.

## Snippets

*(populate as source stubs are deep-read.)*
