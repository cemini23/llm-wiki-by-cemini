---
title: World Cup Bot CLOB V2 — open gaps
type: concept
date: 2026-06-01
updated: 2026-06-01
tags: [world-cup-bot, clob-v2, gaps]
ai-first: true
related:
  - projects/world-cup-bot/CLOB-V2-live/Index.md
  - projects/world-cup-bot/CLOB-V2-live/World Cup Bot - CLOB V2 patch spec.md
  - projects/world-cup-bot/World Cup Bot.md
maturity: validated
---

# OPEN-GAPS — World Cup Bot CLOB V2 live

Updated: 2026-06-01

## Blocking live POST

| ID | Gap | Owner | Action |
|----|-----|-------|--------|
| G01 | **`py-clob-client` V1** in repo | world-cup-bot | **Shipped** @ `7054500` — see [[World Cup Bot - CLOB V2 patch spec]] |
| G02 | **`order_version_mismatch`** on egress live plan | world-cup-bot | Verify on egress after pull + wallet V2 migration |
| G03 | **`cemini-wc-live-plan.timer`** disabled on egress | operator | Enable after G01 + preflight PASS |

## Egress / ops

| ID | Gap | Notes |
|----|-----|-------|
| G04 | Geoblock API labels FI IP as `DE/blocked` | POST reaches CLOB (400 not 403); P2 probe improvement in patch spec |
| G05 | `install-wc-egress.sh` on Cemini `main` | **Shipped** — CeminiSuite @ commit after `4348d467` |
| G06 | Wallet V2 / pUSD migration | Operator UI step before sizing live pilot |

## Shadow / PnL

| ID | Gap | Notes |
|----|-----|-------|
| G07 | **0 fills** on shadow ledger | Expected until live quotes or external resting orders; watch on egress fills live ledger |
| G08 | Shadow PnL floor N/A | Gate applies after Phase 2 fills exist |

## Policy flags (unchanged)

| ID | Gap | Value |
|----|-----|-------|
| G09 | Phase router | OFF |
| G10 | FIFA match gate | OFF |
| G11 | Cross-venue auto-exec | OFF |

## After V2 merge

- [ ] Pull + pip install on egress
- [ ] One manual live plan smoke
- [ ] Enable `cemini-wc-live-plan.timer`
- [ ] Update this file — close G01–G03
- [ ] Optional: export sanitized `shadow-status --json` to `exports/` for CI audit
