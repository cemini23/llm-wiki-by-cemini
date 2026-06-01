---
title: Architecture — Pre-live POST checklist
type: architecture-module
date: 2026-06-02
updated: 2026-06-02
tags: [architecture, world-cup-bot, clob-v2, launch-gate, checklist]
scanned-commit: d5a2f8e
ai-first: true
related:
  - projects/world-cup-bot/Architecture/Architecture - Overview.md
  - projects/world-cup-bot/Architecture/Architecture - deploy.md
  - projects/world-cup-bot/Architecture/OPEN-GAPS.md
  - projects/world-cup-bot/CLOB-V2-live/Index.md
  - projects/world-cup-bot/CLOB-V2-live/World Cup Bot - CLOB V2 patch spec.md
  - concepts/polymarket-retail-trading-discipline.md
  - concepts/shadow-to-live-transition-engineering.md
  - entities/tools/polymarket-clob-api.md
  - projects/world-cup-bot/Architecture/Architecture - Key decisions.md
  - projects/world-cup-bot/World Cup Bot.md
  - entities/tools/world-cup-bot.md
maturity: core
---

## Relations

- @projects/world-cup-bot/Architecture/Architecture - Overview.md — architect hub entry
- @projects/world-cup-bot/Architecture/Architecture - deploy.md — `live-plan` timer enable lives here
- @projects/world-cup-bot/CLOB-V2-live/Index.md — CLOB V2 prod handoff (2026-06-01)
- @concepts/polymarket-retail-trading-discipline.md — org-wide `py-clob-client-v2` pin
- @concepts/shadow-to-live-transition-engineering.md — shadow ≠ live POST proof
- @projects/world-cup-bot/Architecture/Architecture - Key decisions.md
- @projects/world-cup-bot/World Cup Bot.md

## For future Claude

**Mandatory gate before enabling live POST** (`DRY_RUN=false`, `cemini-wc-live-plan.timer`, or public “live LP ready”). Run on **every** release that touches order POST, `[live]` deps, or `clob_live.py`. **Monitor-only shadow (`DRY_RUN=true` on prod) does not satisfy this checklist.**

Origin: CLOB V1 shipped in OSS repo while CeminiSuite already used V2 — discovered on first egress live `plan` (`order_version_mismatch`). See `LESSONS.md` (2026-06-01).

---

## Repo / CI (must pass before merge)

| # | Gate | Verify |
|---|------|--------|
| R1 | `[live]` extra pins **`py-clob-client-v2`** (not archived `py-clob-client`) | `grep py-clob-client pyproject.toml` |
| R2 | **`clob_live.py` imports V2 only** | `python scripts/check_clob_v2_import.py` |
| R3 | Preflight requires **`py_clob_client_v2`** when `DRY_RUN=false` | `tests/test_preflight.py` + manual `preflight` |
| R4 | **`BuilderConfig(builder_code=...)` only** — funder on `ClobClient`, not `builder_address` | Match `@projects/cemini-financial-suite/.../polymarket_clob_v2_adapter.py` @ `806aa25` |
| R5 | CI installs `[live]` and runs R2 | `.github/workflows/ci.yml` |
| R6 | **pytest green** | `pytest` (196+ at `d5a2f8e`) |

## Stack parity (Cemini norm — not optional)

| # | Gate | Verify |
|---|------|--------|
| S1 | Cross-check **CeminiSuite** Polymarket order path | `CeminiSuite/services/llm_analyst/polymarket_clob_v2_adapter.py` + `polymarket_clob_writer.py` |
| S2 | Cross-check **wiki** pin | @concepts/polymarket-retail-trading-discipline.md — `[CONFIRMED]` V2 only since Apr 2026 cutover |
| S3 | **Bugbot / architect pass includes this page** | Do not sign “launch ready” from shadow-only + static review alone |

## Host / operator (before timer enable)

| # | Gate | Verify |
|---|------|--------|
| H1 | **Non-US egress** for live POST (geoblock) | `preflight` phase 3 / host not US/VA |
| H2 | `pip install -e ".[live]"` on trading host | `python -c "import py_clob_client_v2"` |
| H3 | L2 creds + `POLYMARKET_PRIVATE_KEY` + funder env | `preflight` → `clob_auth` PASS |
| H4 | **`POLYMARKET_BUILDER_CODE`** set if using builder attribution | Optional; if set, R4 shape applies |
| H5 | **Polymarket Exchange V2 wallet migration** (UI) | No `order_version_mismatch` on smoke |
| H6 | **One live smoke**: `DRY_RUN=false plan --record --liquidity-gate` | Ledger: `quote_intent` + `order_cancel`; **no** `order_version_mismatch` |
| H7 | Enable **`live-plan` timer** only after H6 | Operator GO; see @projects/world-cup-bot/Architecture/Architecture - deploy.md |

## Explicit non-gates (do not confuse with H6)

- Monitor **`shadow-status --min-phase 1`** with `DRY_RUN=true` — records intents only; **does not POST orders**
- **`preflight PASS`** on monitor while V1 was installed — was false green until R3 shipped
- **Bugbot clean** — does not check dependency parity with CeminiSuite

## Sign-off template

Copy into prod brief or `wiki/log.md` when closing a live-POST gate:

```
pre-live-POST | world-cup-bot @ <sha> | R1-R6 PASS | H6 smoke <UTC timestamp> | timer <enabled|held>
```

## References

- Patch spec: [[World Cup Bot - CLOB V2 patch spec]]
- Prod layout: [[World Cup Bot - egress live layout]]
- Closed instance: egress-fi 2026-06-01 @ `7054500` + `806aa25`, timer enabled after H6
