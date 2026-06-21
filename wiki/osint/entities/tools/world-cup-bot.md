---
title: World Cup Bot (public OSS)
type: entity
tags: [tool, polymarket, kalshi, world-cup-2026, lp-bot, open-source, cemini23, k82, k83, k84]
keywords: [world-cup-bot, advance-to-knockout, conviction-lp, github, mit, outlier-weekly, calendar-guard, cross-venue-scanner, rewards-sync, shadow-status, liquidity-scanner]
related:
  - projects/world-cup-bot/World Cup Bot.md
  - projects/world-cup-bot/CLOB-V2-live/Index.md
  - projects/world-cup-bot/CLOB-V2-live/World Cup Bot - CLOB V2 patch spec.md
  - projects/world-cup-bot/CLOB-V2-live/World Cup Bot - egress live layout.md
  - projects/world-cup-bot/Architecture/Architecture - Overview.md
  - projects/world-cup-bot/Architecture/Architecture - Pre-live POST checklist.md
  - projects/world-cup-bot/Architecture/OPEN-GAPS.md
  - projects/world-cup-bot/Architecture/Architecture - Key decisions.md
  - entities/tools/wc-ticket-monitor.md
  - concepts/world-cup-advance-market-bot-v1.md
  - sources/gemini-wc2026-group-b-lp-analysis-2026-05-29.md
  - sources/gemini-wc2026-third-place-advancement-2026-05-29.md
  - sources/gemini-wc2026-market-gap-live-verification-2026-05-29.md
  - sources/gemini-wc2026-cross-venue-scanner-research-2026-06-05.md
  - sources/gemini-wc2026-market-probability-gaps-2026-06-05.md
  - sources/gemini-wc2026-knockout-market-map-2026-06-05.md
  - sources/gemini-wc2026-prediction-markets-inventory-2026-06-09.md
  - sources/trading-posts-compilation-8-2026-06-09.md
  - concepts/pnl-attribution-versioning.md
  - concepts/trading-bot-logging-discipline.md
  - concepts/polymarket-sports-lp-operating-rules.md
  - concepts/world-cup-2026-group-conviction-matrix.md
  - "@seo-wiki/concepts/outlier-weekly-issue3-world-cup-bot-notes.md"
  - entities/tools/polymarket-gamma-api.md
  - entities/tools/polymarket-clob-api.md
  - entities/tools/openfootball-worldcup-json.md
  - entities/tools/mrfadi-polymarket-bot.md
  - sources/multi-wiki-tool-eval-50url-k102-2026-06-06.md
  - sources/world-cup-github-repo-eval-2026-05-29.md
  - sources/gemini-wc-lp-team-safety-assessments-2026-05-30.md
  - sources/gemini-wc-knockout-market-map-2026-05-30.md
  - sources/gemini-wc-inplay-pregame-lp-risks-2026-05-30.md
  - sources/gemini-wc-tournament-phase-router-2026-05-30.md
  - sources/gemini-wc-tournament-phase-router-architectural-spec-2026-05-31.md
  - sources/gemini-wc-conviction-config-audit-2026-05-31.md
  - sources/gemini-github-sports-betting-repos-landscape-2026-05-30.md
  - concepts/production-trading-blind-spots.md
  - concepts/shadow-to-live-transition-engineering.md
  - concepts/world-cup-tournament-phases-lp-strategy.md
  - concepts/cemini-workflow-tooling-audit-2026-05-30.md
  - meta/wc-lp-safety-cadence.md
  - concepts/cemini-knowledge-application-architecture.md
  - concepts/polymarket-negative-filter-trading.md
  - concepts/monokern-compounding-research-pipeline.md
  - concepts/harness-updating-vs-benefit-nonmonotonic.md
  - sources/monokern-research-pipeline-claude-notebooklm-obsidian-2026-06-01.md
  - sources/arxiv-harness-updating-not-benefit-2605.30621.md
  - concepts/system-scaling-harness-evaluation.md
  - sources/rohonchain-fifa-wc-shock-recovery-strategy-2026-06-02.md
  - sources/trading-posts-compilation-17-2026-06-03.md
  - concepts/polymarket-football-shock-recovery-trading.md
  - projects/world-cup-bot/Architecture/Architecture - match_shock_v1.md
  - projects/world-cup-bot/Architecture/Architecture - match_shock_pmxt_backtest.md
  - entities/people/rohonchain.md
maturity: validated
created: 2026-05-29
updated: 2026-06-09
---

## Relations

- @projects/world-cup-bot/Architecture/Architecture - Overview.md — `/obsidian-architect` codebase map @ `17a6647`
- @projects/world-cup-bot/Architecture/Architecture - Pre-live POST checklist.md — mandatory before live POST (CLOB V2 + egress smoke)
- @projects/world-cup-bot/Architecture/OPEN-GAPS.md — architect gap tracker (shadow soak, router flags, DR cadence)
- @concepts/world-cup-advance-market-bot-v1.md — full v1 architecture spec (private Cemini module shares this codebase)
- @concepts/pnl-attribution-versioning.md — `logic_version` + scope=current pattern mirrored in OSS ledger
- @concepts/trading-bot-logging-discipline.md — structured JSONL events with stable `event=` names
- @entities/tools/openfootball-worldcup-json.md — CC0 fixture data for calendar guard
- @entities/tools/polymarket-gamma-api.md — market discovery + reward params at runtime
- @entities/tools/polymarket-clob-api.md — quote POST, fill handler, rewards GET `/rewards/user`, public `/book` depth
- @seo-wiki/concepts/outlier-weekly-issue3-world-cup-bot-notes.md — Issue 3 marketing queue (2026-06-03)
- @meta/wc-lp-safety-cadence.md — weekly DR re-run through tournament window (next **2026-06-06**)
- @concepts/polymarket-negative-filter-trading.md — K88 selection-before-speed; WCB `negative_filter_summary` + venue reconcile
- @concepts/cemini-knowledge-application-architecture.md — build loop exemplar of repeat-lesson failure (K89)
- @concepts/monokern-compounding-research-pipeline.md — K93 weekly `research run weekly-osint-pipeline`
- @concepts/harness-updating-vs-benefit-nonmonotonic.md — K93 advisor restrictive-mode discipline
- @sources/monokern-research-pipeline-claude-notebooklm-obsidian-2026-06-01.md
- @sources/arxiv-harness-updating-not-benefit-2605.30621.md
- @sources/rohonchain-fifa-wc-shock-recovery-strategy-2026-06-02.md — K94 @RohOnChain in-play shock-recovery; **orthogonal to v1** advance LP (see @concepts/polymarket-football-shock-recovery-trading.md)
- @concepts/polymarket-football-shock-recovery-trading.md — v2 module candidate; reinforces DR 09 `hard_halt` during live matches

### K93 adoptions (2026-06-01)

| Item | Repo | Status |
|------|------|--------|
| Conviction YAML v5 | `config/conviction.yaml` | **Shipped** — K91 teams removed from aggressive lists; `per_team` fade_watch unchanged |
| Weekly OSINT research mode | `prompts/deep-research-weekly-osint-pipeline.md` | **Shipped** |
| Advisor injury-delta hint | `world_cup_bot/advisor.py` | **Shipped** |
| Prod brief | `briefs/2026-06-01_k93-wc-bot-adoptions-cemini.md` | Staged → cemini-prod |

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

### Status (2026-06-03 — public launch)

| Module / feature | State |
|------------------|-------|
| Repo + docs | **Public v1** — Outlier Weekly Issue 3; README launch section; SHADOW split-ledger trap @ `97e7745` |
| **Scanner (1)** | **Live** — Gamma advance markets + reward params |
| **Conviction filter (2)** | **Live** — `config/conviction.yaml` **v5** (K91 fade_watch + K93 list hygiene) |
| **Quoter (3)** | **Live** dry-run + live POST; cancel-replace + calendar auto-cancel |
| **Fill handler (4)** | **Live** — WS + REST reconcile; kill-switch; queue depletion + vol cooldown |
| **Calendar guard (5)** | **Live** — CC0 fixtures; `fixture-check` upstream diff |
| **Cross-venue scanner (6)** | **Live** — 15 cohort pairs; alert loop; paper `--record`; Phase B manual fills + reconcile; **Phase C auto exec** (gated OFF, `WC_CROSS_VENUE_AUTO_EXEC`) |
| **P&L ledger (7)** | **Live** — JSONL + `logic_version`; fills, cancels, rewards sync; **K102 open:** streak-based quote-size scaling + multi-layer PnL gates (steal from @entities/tools/mrfadi-polymarket-bot.md) |
| **Liquidity gate** | **Live** — CLOB `/book`; bid $50 / ask $15 band floors (WC tune); auto-clear `human_review` |
| **Go-live safety** | **Live** — auto-cancel, cancel-replace, kill-switch, `cancel` CLI |
| **Operator automation** | **Live** — `conviction-staleness`, `conviction-patch`, fixture-check |
| **Operator alerts** | **Live** — optional `WC_ALERT_WEBHOOK_URL` |
| **Shadow gate** | **Live** — `shadow-status` prints ledger path + CI exit codes |
| **Rewards ingestion** | **Live** — `rewards sync`; **separate** systemd timer (opt-in Phase 2+) |
| Gemini DR prompts | **Live** — `prompts/gemini-deep-research/` + `research gemini` CLI; **DR 08–10 ingested 2026-05-30** → `config/market_phases.yaml` + router spec |
| Prod systemd (monitor) | **Deployed** on `cemini-prod` — refresh units after `17708e1` pull |
| **Steal-from audit (K85)** | **Live** — daily adverse cap, 429 preflight, event log, CI TruffleHog/vet, shadow fixture gate |
| **Knowledge audit (K88/K89)** | **2026-05-31** — `negative_filter_summary` on plan; `venue-reconcile compare`; Wave 3b wiki enforcement **prod-only** |
| CeminiSuite import | **Brief staged** — `briefs/2026-05-29_world-cup-bot-cemini-import.md` (OSINT) |

Logic version: **`wc_advance_lp_v4`** · paper arb: **`wc_cross_venue_paper_v1`** · exec: **`wc_cross_venue_exec_v1`**. **167 pytest**.

### K94 research note — in-play shock recovery (2026-06-02)

@RohOnChain published a **match-market shock-recovery** framework (detect → 5D bucket → percentile ladder → 4¢ exit). **Not v1 scope** — WC Bot explicitly excludes in-play quoting. Indirect value: validates why advance LP must cancel before kickoff.

**Scaffold shipped:** `match_shock.py`, `config/shock_match.yaml`, `scripts/shock_backtest/` (10 pytest). Spec: @projects/world-cup-bot/Architecture/Architecture - match_shock_v1.md · backtest: @projects/world-cup-bot/Architecture/Architecture - match_shock_pmxt_backtest.md

### Deploy profiles (`deploy/systemd/`)

| Profile | Host | Units |
|---------|------|-------|
| **monitor** | US OK | cross-venue, shadow-plan (`--liquidity-gate`), scan, calendar, discover, **pnl-daily** (PnL only), conviction-staleness, fixture-check; rewards-sync installed but timer off by default |
| **trading** | Non-US only | preflight, watch, live-plan (Phase 4 manual enable) |

Shadow ledger default on VPS: `data/local/shadow_ledger.jsonl` via `WC_LEDGER_PATH`.

```bash
sudo bash deploy/systemd/install-systemd.sh --install-root /opt/world-cup-bot --profile monitor --enable
```

### CLI (operator)

```bash
world-cup-bot scan --conviction --liquidity
world-cup-bot liquidity-scan
world-cup-bot plan --record --liquidity-gate
world-cup-bot watch --record
world-cup-bot cancel --cancel-window
world-cup-bot rewards sync --record   # L2 required; separate cron unit
world-cup-bot shadow-status --min-phase 1
world-cup-bot conviction-staleness --notify
world-cup-bot fixture-check --notify
world-cup-bot cross-venue-scan --loop
world-cup-bot pnl --scope current
world-cup-bot venue-reconcile compare polymarket-export.csv
```

## Snippets

> "Your fork uses your `.env` and your keys only." — [SECURITY.md](https://github.com/cemini23/world-cup-bot/blob/main/SECURITY.md)

Liquidity operating thresholds (WC advance — not live prices):

```yaml
liquidity:
  min_depth_within_reward_spread_usd: 50   # bid band
  min_ask_depth_within_reward_spread_usd: 15
  auto_clear_human_review: true
```

Ledger reward event (after `rewards sync --record`):

```json
{"event":"reward_accrual","logic_version":"wc_advance_lp_v4","team":"Turkey","rewards_usd":1.25,"reward_key":"2026-05-28:0x…","earn_date":"2026-05-28","source":"clob_rewards_user"}
```
