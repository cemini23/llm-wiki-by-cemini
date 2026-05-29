---
title: Bullpen CLI — Polymarket programmatic trading CLI
type: entity
tags: [entity, tool, polymarket, cli, claude-code, k80]
keywords: [bullpen, bullpen-cli, leaderboard, copy-trading, claude-code, sponsored]
related:
  - sources/youtube-polymarket-bots-batch-2026-05-29.md
  - concepts/polymarket-copy-trading-strategy.md
  - concepts/polymarket-api-reference.md
  - concepts/claude-code-trading-assistant-workflow-smb.md
maturity: draft
created: 2026-05-29
updated: 2026-05-29
---

## Relations

- @sources/youtube-polymarket-bots-batch-2026-05-29.md — Sharbel A. Claude Code build tutorial (2026-04-06)
- @concepts/polymarket-copy-trading-strategy.md — copy-bot stack reference
- @concepts/polymarket-api-reference.md — API surface overlap
- @concepts/claude-code-trading-assistant-workflow-smb.md — Claude Code build pattern (SMB parallel)

## Raw Concept

What prompted this page: YouTube *Full Polymarket Bot Build | Claude Code Tutorial* (Sharbel A., 2026-04-06) — sponsored walkthrough using **Bullpen CLI** for auth, leaderboard, and trade routing while Claude Code generates a copy-trading bot.

## Narrative

**Bullpen CLI** [TENTATIVE] — terminal tool from Bullpen (crypto trading app) exposing Polymarket programmatic access: device auth, leaderboard JSON export, profile/trade pulls, order execution, AI skills bundle.

### Sharbel build pattern (video)

- Claude Code + `dangerously skip permissions` + Bullpen install via Homebrew.
- Leaderboard: top **active** traders by weekly PnL (win rate often null in default feed).
- Copy bot spec: track top 10, **$5 fixed** per mirror, continuous polling/watch for new trades, TypeScript/Node, local dashboard with pause/resume, `trades.json` log.

### Cemini relevance

- **Steal-from CONDITIONAL-GO** — **`[TENTATIVE 2026-05-29]`** official docs at cli.bullpen.fi; binary/npm distribution (releases repo `BullpenFi/bullpen-cli-releases`, not open-source trading core). Alpha/beta — useful for Claude Code **prototypes** only; prod stack stays `py-clob-client-v2` + Gamma/Data API. TOS + custody model audit before any funded wallet link.
- Distinct from Pretracer/Kreo Telegram bots — developer CLI path.

## Snippets

> "Bullpen CLI handles all the authentication, the order routing, the wallet connection." [Source: https://www.youtube.com/watch?v=-F0dZ2GxSuA (retrieved 2026-05-29)]
