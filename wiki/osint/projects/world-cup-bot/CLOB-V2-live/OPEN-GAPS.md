---
title: World Cup Bot CLOB V2 — open gaps
type: concept
date: 2026-06-01
updated: 2026-06-02
tags: [world-cup-bot, clob-v2, gaps]
ai-first: true
related:
  - projects/world-cup-bot/CLOB-V2-live/Index.md
  - projects/world-cup-bot/CLOB-V2-live/World Cup Bot - CLOB V2 patch spec.md
  - projects/world-cup-bot/World Cup Bot.md
maturity: validated
---

# OPEN-GAPS — World Cup Bot CLOB V2 live

Updated: 2026-06-02

## Blocking live POST

| ID | Gap | Owner | Action |
|----|-----|-------|--------|
| G01 | **`py-clob-client` V1** in repo | world-cup-bot | **Closed** @ `7054500` — see [[World Cup Bot - CLOB V2 patch spec]] |
| G02 | **`order_version_mismatch`** on egress live plan | world-cup-bot | **Closed** 2026-06-01 — live plan cycle POST + cancel-replace OK on egress-fi |
| G03 | **`cemini-wc-live-plan.timer`** disabled on egress | operator | **Closed** 2026-06-01 — timer enabled + active |

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

- [x] Pull + pip install on egress (`py_clob_client_v2` 1.0.1)
- [x] Live plan smoke — quote_intent + order_cancel in ledger @ 2026-06-01T19:26Z
- [x] `cemini-wc-live-plan.timer` enabled
- [x] G01–G03 closed
- [x] Egress `git pull` to `d5a2f8e` (806aa25 builder fix in tree)
- [ ] Optional: export sanitized `shadow-status --json` to `exports/` for CI audit
