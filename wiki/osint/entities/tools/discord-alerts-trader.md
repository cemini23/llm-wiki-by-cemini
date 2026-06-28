---
title: DiscordAlertsTrader — Discord alert parsing + broker adapters
type: entity
tags: [tool, discord, tipdrop, python, k133]
keywords: [DiscordAlertsTrader, AdoNunes, server_formatting, tipdrop, bto-stc]
related:
  - sources/eval-multi-wiki-discord-link-2026-06-28.md
  - concepts/wiki-tooling-evaluation.md
maturity: draft
created: 2026-06-28
updated: 2026-06-28
---

## Relations

- @sources/eval-multi-wiki-discord-link-2026-06-28.md — K133 Steal-from row

## Raw Concept

K133 eval of [AdoNunes/DiscordAlertsTrader](https://github.com/AdoNunes/DiscordAlertsTrader) — Python package parsing trading Discord alerts into broker actions.

## Narrative

| Field | Value |
|-------|-------|
| **Repo** | `AdoNunes/DiscordAlertsTrader` |
| **License** | **BSD-3-Clause** (`gh api` 2026-06-28) |
| **Stars / pushed** | 77★; pushed 2026-01-17 |
| **Stack** | Python 3.10; TDA, eTrade, Webull, IBKR, TradeStation adapters |
| **Verdict** | **Steal-from** — parse patterns only; **no** live auto-execution in TipDrop |
| **Steal** | `server_formatting.py` BTO/STC/SL/PT regex taxonomy; human-in-loop GUI pattern |

**Reject for TipDrop prod:** automated broker execution paths. Extract parsing logic into TipDrop signal normalizer only.

Brief: `../projects/tipdrop-workspace-kit/briefs/2026-06-28_k133-discord-alerts-trader-steal.md`

## Snippets

> Parses diverse analyst message formats; local polling when OCO unsupported. [Source: eval-multi-wiki-discord-link-2026-06-28.md URL 13]
