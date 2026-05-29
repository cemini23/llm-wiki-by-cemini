---
title: World Cup Bot (public OSS)
type: entity
tags: [tool, polymarket, kalshi, world-cup-2026, lp-bot, open-source, cemini23, k82]
keywords: [world-cup-bot, advance-to-knockout, conviction-lp, github, mit, outlier-weekly, calendar-guard]
related:
  - concepts/world-cup-advance-market-bot-v1.md
  - concepts/pnl-attribution-versioning.md
  - concepts/trading-bot-logging-discipline.md
  - concepts/polymarket-sports-lp-operating-rules.md
  - concepts/world-cup-2026-group-conviction-matrix.md
  - entities/tools/polymarket-gamma-api.md
  - entities/tools/polymarket-clob-api.md
  - entities/tools/openfootball-worldcup-json.md
  - sources/world-cup-github-repo-eval-2026-05-29.md
maturity: draft
created: 2026-05-29
updated: 2026-05-30
---

## Relations

- @concepts/world-cup-advance-market-bot-v1.md — full v1 architecture spec (private Cemini module shares this codebase)
- @concepts/pnl-attribution-versioning.md — `logic_version` + scope=current pattern mirrored in OSS ledger
- @concepts/trading-bot-logging-discipline.md — structured JSONL events with stable `event=` names
- @entities/tools/openfootball-worldcup-json.md — CC0 fixture data for calendar guard
- @entities/tools/polymarket-gamma-api.md — market discovery + reward params at runtime
- @entities/tools/polymarket-clob-api.md — quote POST + fill handler

## Raw Concept

Public MIT implementation of the K82 World Cup advance-market bot.

| Field | Value |
|-------|-------|
| Product name | **World Cup Bot** |
| GitHub | [cemini23/world-cup-bot](https://github.com/cemini23/world-cup-bot) |
| License | MIT |
| Local clone | `~/Desktop/projects/world-cup-bot` |
| Marketing | [Outlier Weekly](https://outlierweekly.substack.com) Issue 3 — **2026-06-03** |

## Narrative

### Public boundary

The repo is **fully public**. It ships MIT code, docs, and `.env.example` placeholders only — never prod keys, wallet addresses, or internal server paths.

Forks run on **bring-your-own-keys** via `.env`. Maintainer prod uses same code + private env on `cemini-prod` / `@entities/infrastructure/cemini-egress-fi.md`.

### Status (2026-05-30)

| Module | State |
|--------|-------|
| Repo + docs | **Live** |
| **Scanner (1)** | **Live** — `world_cup_bot/scanner.py` + `scan` CLI |
| **Conviction filter (2)** | **Live** — `config/conviction.yaml` + `conviction.py` |
| **Quoter (3)** | **Dry-run** — `quoter.py`; live CLOB on Cemini prod only |
| **Calendar guard (5)** | **Live** — CC0 `data/worldcup2026-fixtures.json` |
| **P&L ledger (7)** | **Live** — JSONL + `logic_version` registry (`config/strategy_logic_versions.yaml`); `pnl --scope current` default per @concepts/pnl-attribution-versioning.md |
| Fill handler (4) / cross-venue (6) | **Pending** |
| CeminiSuite import | **Pending** prod brief |

CLI:

```bash
pip install -e ".[dev]"
world-cup-bot calendar --team Mexico
world-cup-bot scan --conviction
world-cup-bot plan --record
world-cup-bot pnl
```

## Snippets

> "Your fork uses your `.env` and your keys only." — [SECURITY.md](https://github.com/cemini23/world-cup-bot/blob/main/SECURITY.md)
