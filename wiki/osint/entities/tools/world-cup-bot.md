---
title: World Cup Bot (public OSS)
type: entity
tags: [tool, polymarket, kalshi, world-cup-2026, lp-bot, open-source, cemini23, k82, k83]
keywords: [world-cup-bot, advance-to-knockout, conviction-lp, github, mit, outlier-weekly, calendar-guard, cross-venue-scanner, rewards-sync, shadow-status]
related:
  - concepts/world-cup-advance-market-bot-v1.md
  - sources/gemini-wc2026-group-b-lp-analysis-2026-05-29.md
  - sources/gemini-wc2026-third-place-advancement-2026-05-29.md
  - sources/gemini-wc2026-market-gap-live-verification-2026-05-29.md
  - concepts/pnl-attribution-versioning.md
  - concepts/trading-bot-logging-discipline.md
  - concepts/polymarket-sports-lp-operating-rules.md
  - concepts/world-cup-2026-group-conviction-matrix.md
  - @seo-wiki/concepts/outlier-weekly-issue3-world-cup-bot-notes.md
  - entities/tools/polymarket-gamma-api.md
  - entities/tools/polymarket-clob-api.md
  - entities/tools/openfootball-worldcup-json.md
  - sources/world-cup-github-repo-eval-2026-05-29.md
  - sources/gemini-wc-lp-team-safety-assessments-2026-05-30.md
  - concepts/cemini-workflow-tooling-audit-2026-05-30.md
  - meta/wc-lp-safety-cadence.md
maturity: validated
created: 2026-05-29
updated: 2026-05-30
---

## Relations

- @concepts/world-cup-advance-market-bot-v1.md — full v1 architecture spec (private Cemini module shares this codebase)
- @concepts/pnl-attribution-versioning.md — `logic_version` + scope=current pattern mirrored in OSS ledger
- @concepts/trading-bot-logging-discipline.md — structured JSONL events with stable `event=` names
- @entities/tools/openfootball-worldcup-json.md — CC0 fixture data for calendar guard
- @entities/tools/polymarket-gamma-api.md — market discovery + reward params at runtime
- @entities/tools/polymarket-clob-api.md — quote POST, fill handler, rewards GET `/rewards/user`
- @seo-wiki/concepts/outlier-weekly-issue3-world-cup-bot-notes.md — Issue 3 marketing queue (2026-06-03)

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

Forks run on **bring-your-own-keys** via `.env`. Maintainer prod uses same code + private env on dedicated VPS (monitor + non-US trading split). Generic systemd install: `deploy/systemd/` — no operator hostnames in git.

### Status (2026-05-29)

| Module | State |
|--------|-------|
| Repo + docs | **Live** |
| **Scanner (1)** | **Live** — Gamma advance markets + reward params |
| **Conviction filter (2)** | **Live** — `config/conviction.yaml` **v4** (K84 LP safety gates) |
| **Quoter (3)** | **Live** dry-run + live POST (`clob_live.py`); cancel-replace + calendar auto-cancel |
| **Fill handler (4)** | **Live** — WS user channel + REST reconcile; kill-switch halt |
| **Calendar guard (5)** | **Live** — CC0 `data/worldcup2026-fixtures.json` |
| **Cross-venue scanner (6)** | **Live** — 15 cohort pairs in `config/cross_venue.yaml`; alert-only loop + webhook |
| **P&L ledger (7)** | **Live** — JSONL + `logic_version`; fills, cancels, **rewards sync** |
| **Go-live safety** | **Live** — auto-cancel window, cancel-replace, kill-switch pull, `cancel` CLI |
| **Operator alerts** | **Live** — optional `WC_ALERT_WEBHOOK_URL` (cancels + cross-venue ALERT) |
| **Shadow gate** | **Live** — `shadow-status` CLI (CI exit codes) |
| **Rewards ingestion** | **Live** — `rewards sync` → CLOB GET `/rewards/user` → `reward_accrual` rows |
| Gemini DR prompts | **Live** — `prompts/gemini-deep-research/` + `research gemini` CLI |
| Prod systemd (monitor) | **Brief staged** — `briefs/2026-05-29_wc-monitor-systemd-enable.md` |
| CeminiSuite import | **Pending** prod brief |

Logic version: **`wc_advance_lp_v4`** (cancel safety + ledger cancel audit).

### Deploy profiles (`deploy/systemd/`)

| Profile | Host | Units |
|---------|------|-------|
| **monitor** | US OK | cross-venue service, shadow-plan, scan, calendar-guard, discover, pnl-daily (rewards+pnl) |
| **trading** | Non-US only | preflight, watch, live-plan (Phase 4 manual enable) |

```bash
sudo bash deploy/systemd/install-systemd.sh --install-root /opt/world-cup-bot --profile monitor --enable
```

### CLI (operator)

```bash
world-cup-bot scan --conviction
world-cup-bot plan --record          # auto calendar-cancel + cancel-replace audit when --record
world-cup-bot watch --record         # fills + reconcile + kill-switch
world-cup-bot cancel --cancel-window
world-cup-bot rewards sync --record  # yesterday UTC default; dedup by reward_key
world-cup-bot shadow-status --min-phase 1
world-cup-bot cross-venue-scan --loop
world-cup-bot pnl --scope current
```

## Snippets

> "Your fork uses your `.env` and your keys only." — [SECURITY.md](https://github.com/cemini23/world-cup-bot/blob/main/SECURITY.md)

Ledger reward event (after `rewards sync --record`):

```json
{"event":"reward_accrual","logic_version":"wc_advance_lp_v4","team":"Turkey","rewards_usd":1.25,"reward_key":"2026-05-28:0x…","earn_date":"2026-05-28","source":"clob_rewards_user"}
```
