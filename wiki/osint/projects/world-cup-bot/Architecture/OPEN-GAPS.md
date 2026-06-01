---
title: World Cup Bot architecture — open gaps
type: concept
date: 2026-06-01
updated: 2026-06-02
scanned-commit: d5a2f8e
ai-first: true
related:
  - projects/world-cup-bot/World Cup Bot.md
  - projects/world-cup-bot/Architecture/Architecture - Overview.md
  - projects/world-cup-bot/Architecture/Architecture - Key decisions.md
  - projects/world-cup-bot/Architecture/Architecture - Pre-live POST checklist.md
  - entities/tools/world-cup-bot.md
  - meta/wc-lp-safety-cadence.md
maturity: validated
---

## Relations

- @projects/world-cup-bot/World Cup Bot.md
- @entities/tools/world-cup-bot.md
- @meta/wc-lp-safety-cadence.md

## For future Claude

Gap list after `/obsidian-architect` @ `17a6647`. **Before live POST:** @projects/world-cup-bot/Architecture/Architecture - Pre-live POST checklist.md (mandatory). Re-run architect + pytest after each release.

## Closed in K93 adoption pass (2026-06-01)

| Gap | Fix |
| --- | --- |
| K91 fade_watch teams still on aggressive YAML lists | `conviction.yaml` v5 hygiene in world-cup-bot |
| No weekly external-research CLI mode | `weekly-osint-pipeline` research mode + Monokern OSINT concept |
| Advisor silent on injury-vs-YAML conflict | Restrictive-mode hint in `advisor.py` |

## Closed in architect pass (2026-06-01)

| Gap | Fix |
| --- | --- |
| No OSINT architecture hub | `wiki/projects/world-cup-bot/Architecture/*` + project note |
| Bugbot: exports leak paths/tracebacks | Scrubbed @ `17a6647`; CI `check_exports_sanitize.py` @ `36be032` |
| Bugbot: threshold guard false positives on `#` comments | `line_matches_threshold()` @ `17a6647` |
| ROADMAP test count drift (187 vs 189) | ROADMAP → 189 pytest |
| Entity page missing architecture links | Updated @entities/tools/world-cup-bot.md |
| No pre–live-POST stack parity gate | @projects/world-cup-bot/Architecture/Architecture - Pre-live POST checklist.md @ `d5a2f8e` |

## Still open (operator / product)

| Area | Why | Next step |
| --- | --- | --- |
| **SHADOW Phase 1 soak** | Pre–Issue 3 (2026-06-03) | ≥3 days `plan --record --liquidity-gate`; `shadow-status --min-phase 1` PASS |
| **LP safety DR** | Canada/Japan/Scotland/Brazil on `fade_watch` | Re-run DR **2026-06-06** per @meta/wc-lp-safety-cadence.md |
| **Phase router on prod** | Flags default OFF | Enable only via prod brief after operator sign-off |
| **Rewards timer** | Needs L2 on host | `world-cup-bot-rewards-sync.timer` after Phase 2 |
| **Wiki enforcement hook** | K89 documented-only | `WC_WIKI_ENFORCEMENT=1` on prod when brief ships |
| **CeminiSuite import** | Post shadow gate | OSINT `briefs/2026-05-29_world-cup-bot-cemini-import.md` |
| **Cross-venue pair refresh** | Slug drift | `discover` timer + manual `--discover-only` |
| **Trading VPS profile** | Non-US live LP | Phase 2–4 after SHADOW 3–4 |

## Still open (documentation / automation)

| Area | Why | Next step |
| --- | --- | --- |
| **`@generated` refresh script** | Manual architect re-run | Optional: wire `architect_scan.py` into OSINT cadence |
| **Scan manifest deps** | `architect_scan.py` lists only `pyyaml` | Document `[live]` extras in overview (done in module note) |
| **Daily note link** | No vault `daily/` folder in OSINT wiki | Log entry in `wiki/log.md` only |

## Out of scope (v1)

Hosted service, guaranteed edge, in-play quoting — see `ROADMAP.md` “Out of scope”.
