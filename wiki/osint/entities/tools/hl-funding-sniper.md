---
title: "hl-funding-sniper — Hyperliquid funding-rate capture bot (TheSmartApe)"
type: entity
tags: [entity, tool, hyperliquid, funding-rate, open-source, phase-0]
keywords: [hl-funding-sniper, thesmartape, hyperliquid-funding-bot, funding-rate-spike, telegram-alerts, mit, conditional-go]
related:
  - concepts/perps-dex-funding-carry-strategy.md
  - entities/platforms/hyperliquid.md
  - entities/people/the-smart-ape.md
  - sources/trading-posts-compilation-25-2026-05-27.md
  - entities/infrastructure/cemini-egress-fi.md
maturity: validated
created: 2026-05-27
updated: 2026-05-27
---

## Relations

- @concepts/perps-dex-funding-carry-strategy.md — strategy template
- @entities/platforms/hyperliquid.md
- @entities/people/the-smart-ape.md — author post
- @sources/trading-posts-compilation-25-2026-05-27.md — Post 16
- @entities/infrastructure/cemini-egress-fi.md — **no deploy** on egress; prod uses `HYPERLIQUID_PROXY` only

## Raw Concept

Open-source bot: `https://github.com/TheSmartApe/hl-funding-sniper`. K72 Phase-0 audit 2026-05-27.

## Narrative

### Phase-0 verdict: **CONDITIONAL-GO (steal-from)**

| Check | Result |
|-------|--------|
| License | **MIT** — `LICENSE` file in repo [CONFIRMED]. GitHub API returns `NOASSERTION` — **do not trust API** |
| Maturity | **0★**, single push 2026-05-26 — too immature to Adopt as runtime |
| Failure mode | Shipped `config.yaml` has `dry_run: false` + micro live-test sizing — **footgun** if run verbatim |
| Cemini overlap | `core/ems/adapters/hyperliquid.py` on prod already handles HL with Agent Wallet + `PAPER_MODE` + egress proxy |

### Architecture (upstream)

- Python 3, `hyperliquid-python-sdk`, YAML config, hourly funding tick
- Modules: `data_client`, `signal_engine`, `executor`, `risk_manager`, `backtest/`
- Optional Telegram alerts; `HL_PRIVATE_KEY` via env when live

### Cemini posture

- **Laptop:** reference clone `.local/tools/hl-funding-sniper-reference/` (venv; `dry_run` forced true) — backtest study only
- **Egress-fi:** **NO** install
- **Prod:** steal patterns into existing EMS adapter when funding-carry is scoped — brief `2026-05-27_k72-hl-funding-phase0-cemini.md` on `cemini-prod`

## Snippets

> "Opportunistic Hyperliquid funding-rate sniper bot — naked short on extreme funding APR with native HL SL/TP triggers" [Source: github.com/TheSmartApe/hl-funding-sniper README]
