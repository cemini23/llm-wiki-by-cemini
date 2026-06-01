---
title: Architecture — World Cup Bot key decisions
type: architecture-module
date: 2026-06-01
updated: 2026-06-02
tags: [architecture, adr, world-cup-bot]
ai-first: true
related:
  - projects/world-cup-bot/Architecture/Architecture - Overview.md
  - projects/world-cup-bot/World Cup Bot.md
  - projects/world-cup-bot/Architecture/Architecture - Pre-live POST checklist.md
  - projects/world-cup-bot/Architecture/OPEN-GAPS.md
  - entities/tools/world-cup-bot.md
maturity: validated
---

## Relations

- @projects/world-cup-bot/Architecture/Architecture - Overview.md
- @projects/world-cup-bot/Architecture/Architecture - Pre-live POST checklist.md
- @entities/tools/world-cup-bot.md

## For future Claude

ADRs and commit-mined decisions for **world-cup-bot**. Items marked (confidence: speculation) are inferred from commit subjects, not design docs.

<!-- @generated:start -->

## Commit-mined decisions

| Date | Commit | Decision | Confidence |
| --- | --- | --- | --- |
| 2026-05-29 | `7a78f20` | Replace operator-specific deploy paths with generic `deploy/systemd/` (portable OSS install) | stated (commit message) |
| 2026-05-29 | `6068f64` | Go-live safety: auto-cancel window, cancel-replace, kill-switch halt on cancel-window fills | stated |
| 2026-05-29 | `581411b` | Rewards sync CLI + cancel-replace ledger audit wiring | stated |
| 2026-05-30 | `6a2d51f` | Remove `github.com` URL from Pages sitemap (SEO hygiene) | stated |
| 2026-05-31 | `01af064` | CI: remove OSINT `@path` links from operator docs; ruff format | stated |
| 2026-05-31 | `37f866c` | Docs: UI dashboard URL uses `localhost` not `127.0.0.1` (operator clarity) | stated |
| 2026-06-01 | `806aa25` | `BuilderConfig(builder_code=...)` only — funder on client, not builder_address | stated |
| 2026-06-01 | `7054500` | Migrate live POST to `py-clob-client-v2` (Apr 2026 CLOB cutover) | stated |
| 2026-06-01 | `17a6647` | Scrub `exports/` PII; threshold guard skips `#` comments | stated |

## Architectural decisions (documented in repo)

| Decision | Rationale | Source |
| --- | --- | --- |
| **Shadow before live** | ≥3 days `plan --record --liquidity-gate` with `DRY_RUN=true` | `SHADOW.md` |
| **Config-owned thresholds** | Mids/bands in YAML; CI blocks hardcoded hot-path literals | `config/operating.yaml`, `scripts/check_hardcoded_thresholds.py` |
| **Phase router default OFF** | Module 1b shipped behind env flags until operator enables | `ROADMAP.md`, prod briefs |
| **Cross-venue alert-first** | Paper ledger + optional exec; not bundled LP auto-hedge | `README.md` Module 6 |
| **CLOB V2 before live POST** | Match CeminiSuite; monitor shadow ≠ POST proof | @projects/world-cup-bot/Architecture/Architecture - Pre-live POST checklist.md, `LESSONS.md` 2026-06-01 |
| **Public MIT boundary** | No prod keys, hostnames, or internal wiki paths in git | `CLAUDE.md`, entity page |

## Deferred (see OPEN-GAPS)

- Wiki enforcement at order time (`WC_WIKI_ENFORCEMENT=1`) — prod-only hook, OSS documented-only (confidence: high — K89 brief)
- LP promotion gates (DSR/MCPT) — shadow heuristic only for Issue 3 (confidence: high — ROADMAP)

<!-- @generated:end -->
