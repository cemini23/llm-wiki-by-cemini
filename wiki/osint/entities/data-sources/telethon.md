---
title: Telethon
type: entity
tags: [library, data-source, alt-data, messaging]
keywords: []
related:
  - sources/3-19-alternative-data-for-prediction-markets-research.md
  - sources/3-19-telegram-discord-research.md
  - entities/frameworks/finbert.md
  - concepts/publishers-exclusion-apa.md
maturity: validated
created: 2026-04-23
updated: 2026-04-23
---

## Relations

- @sources/3-19-alternative-data-for-prediction-markets-research.md
- @sources/3-19-telegram-discord-research.md
- @entities/frameworks/finbert.md
- @concepts/publishers-exclusion-apa.md

## Raw Concept

Synthesized from 2 source(s) referencing this entity across the Cemini research corpus. Category: data-sources.

## Narrative

Telethon is a Python MTProto library for reading Telegram channels and
groups as a user-agent (not a bot). Cemini uses Telethon to subscribe to
curated crypto-signal, macro-news, and sports/politics-commentary channels
whose message streams are tagged, de-duplicated, and scored by FinBERT
before being written to TimescaleDB as alt-data features.

Key architectural notes from the 3-19 Telegram/Discord research:
- User-agent MTProto (not Bot API) is required because many target
  channels don't publish a bot-accessible interface.
- Rate-limiting is aggressive on Telegram's side — Cemini stays well
  under limits via channel-rotation and cached join-state.
- The alt-data pipeline is explicitly flagged as a **publisher's-
  exclusion candidate**: institutional buyers may refuse to inherit
  Telegram-based alt-data feeds for reputational/compliance reasons,
  so this feature is gated behind a feature-flag that can be shipped-or-
  stripped for the IP-sale demo.

## Snippets

*(populate as source stubs are deep-read.)*
