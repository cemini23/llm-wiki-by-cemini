---
title: "Institutional Intelligence Integration: Architecting Compliant Social Signal Extraction for Algorithmic Trading Systems"
type: source
tags: [docx, rl-marl, llm-agents, quant-finance, crypto, prediction-markets, cemini-internal]
clusters: [rl-marl, llm-agents, quant-finance, crypto, prediction-markets, cemini-internal]
related:
  - entities/data-sources/telethon.md
  - entities/infrastructure/deepseek-r1-14b.md
  - entities/infrastructure/timescaledb.md
  - entities/infrastructure/redis.md
  - entities/infrastructure/pgvector.md
  - entities/frameworks/langgraph.md
  - entities/frameworks/fastapi.md
  - entities/frameworks/torchrl.md
  - entities/frameworks/pettingzoo.md
  - concepts/ip-sale-readiness.md
  - concepts/mappo.md
maturity: validated
created: 2026-04-23
updated: 2026-04-23
---

## Relations

- @entities/data-sources/telethon.md
- @entities/infrastructure/deepseek-r1-14b.md
- @entities/infrastructure/timescaledb.md
- @entities/infrastructure/redis.md
- @entities/infrastructure/pgvector.md
- @entities/frameworks/langgraph.md
- @entities/frameworks/fastapi.md
- @entities/frameworks/torchrl.md
- @entities/frameworks/pettingzoo.md
- @concepts/ip-sale-readiness.md
- @concepts/mappo.md

## Raw Concept

- **Original title**: Institutional Intelligence Integration: Architecting Compliant Social Signal Extraction for Algorithmic Trading Systems
- **Author(s)**: _unknown (stub — not yet read)_
- **Type**: DOCX
- **Location**: research for cemini/3_19 telegram discord research.docx
- **Retrieved**: 2026-04-23 (filename date reflects download date, not publication)
- **Length**: —
- **Read status**: deep-read
- **Primary cluster**: rl-marl
- **All clusters**: rl-marl, llm-agents, quant-finance, crypto, prediction-markets, cemini-internal

## Narrative

### Abstract
Architecture for compliant social-signal extraction. Telegram via MTProto + Telethon is the only viable path; Discord is declared toxic (self-botting violates TOS, Privileged Intent approval blocks 100+ guilds, IP-ban risk = deal-killer). Key legal constraint: Telegram TOS §1.5 prohibits using platform data to train ML — architecture must strictly separate inference/feature-extraction from model training (use VADER lexicons + regex, discard raw text).

### Key findings
- Bot API inadequate — cannot gain admin in third-party crypto alpha channels; must use MTProto user account
- Telegram §1.5 blocks archiving for RL agent fine-tuning (would make IP toxic to buyers)
- Telethon has documented memory leak (Issue #3235) — must disable save_entities to stay under 150MB RAM per container
- 200-channel limit per user account — architecture must be selective, not broad
- Discord integration explicitly rejected: 4-6 weeks of anti-self-botting engineering, perpetual IP-ban risk, TOS violation = M&A deal-killer
- MkDocs compliance section must document the inference-not-training separation to reduce buyer due-diligence friction

### Entities referenced
Telegram, MTProto, Telethon, Pyrogram, python-telegram-bot, Discord, VADER, TorchRL, PettingZoo, DeepSeek-R1-14B, LangGraph, FastAPI, Redis, TimescaleDB, pgvector, X (Twitter)

### Concepts covered
passive channel monitoring, MTProto protocol, Telegram TOS §1.5 AI training prohibition, self-botting prohibition, Privileged Message Content Intent, ephemeral feature extraction, inference-training separation, compliance architecture documentation

## Snippets

*(None yet — populate on first deep read.)*
