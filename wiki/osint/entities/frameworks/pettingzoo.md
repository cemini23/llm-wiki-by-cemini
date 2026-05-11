---
title: PettingZoo
type: entity
tags: [framework, reinforcement-learning, multi-agent, environments]
keywords: []
related:
  - sources/3-19-ip-sale-research.md
  - sources/3-19-telegram-discord-research.md
  - concepts/mappo.md
  - entities/frameworks/torchrl.md
  - sources/leworldmodel-2603.19312v2.md
maturity: validated
created: 2026-04-23
updated: 2026-05-11
---

## Relations

- @sources/3-19-ip-sale-research.md
- @sources/3-19-telegram-discord-research.md
- @concepts/mappo.md
- @entities/frameworks/torchrl.md

## Raw Concept

Synthesized from 2 source(s) referencing this entity across the Cemini research corpus. Category: frameworks.

## Narrative

PettingZoo is the multi-agent counterpart to Gymnasium — a library of
shared-environment interfaces for multi-agent RL. Cemini defines custom
PettingZoo environments modeling multi-venue execution problems:

- **MultiVenueExecEnv** — one agent per venue (Alpaca, OANDA,
  Hyperliquid, Kalshi), shared observation space over the market-wide
  state, reward shaped by portfolio-level Sharpe + slippage.
- **AlphaDecayEnv** — agents compete for finite alpha across
  correlated strategies; used to study strategy-portfolio capacity.

Trained via TorchRL + MAPPO on the Hetzner CPU host. The RL artifacts
are **research, not production policy** per the IP-sale compliance note
— the institutional buyer evaluates them as evidence of sophisticated
R&D, not as shipped trading logic.

## Snippets

*(populate as source stubs are deep-read.)*
