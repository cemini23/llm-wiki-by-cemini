---
title: "Gemini DR — WC 2026 tournament phase router (Module 1b)"
type: source
tags: [source, gemini-deep-research, world-cup-2026, phase-router, lp-bot, k85, k86]
keywords: [finite-state-machine, tournament-phases, cancel-team, scanner-phase-ids, dual-validation, ghost-quote]
related:
  - sources/gemini-wc-knockout-market-map-2026-05-30.md
  - sources/gemini-wc-inplay-pregame-lp-risks-2026-05-30.md
  - concepts/world-cup-tournament-phases-lp-strategy.md
  - concepts/world-cup-advance-market-bot-v1.md
  - concepts/polymarket-sports-lp-operating-rules.md
  - concepts/production-trading-blind-spots.md
  - entities/tools/world-cup-bot.md
  - entities/tools/openfootball-worldcup-json.md
maturity: validated
created: 2026-05-30
updated: 2026-05-30
---

## Relations

- @sources/gemini-wc-knockout-market-map-2026-05-30.md — DR 08 market inventory + `config/market_phases.yaml` seed
- @sources/gemini-wc-inplay-pregame-lp-risks-2026-05-30.md — cancel-window + ghost-quote context (DR 09)
- @concepts/world-cup-tournament-phases-lp-strategy.md — primary synthesis consumer
- @entities/tools/world-cup-bot.md — implementation target (`wc_advance_lp_v4` → v1b)

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Module 1b: Phase Router Architectural Design for World Cup 2026 Prediction Market Liquidity Provision |
| Author | Gemini Deep Research (prompt 10-tournament-phase-router) |
| Type | docx synthesis report |
| Location | `cemini-librarian:/opt/cemini-bulk/research/Tournament Phase Router Design.docx` |
| Retrieved | 2026-05-30 |
| Read status | deep-read |

## Narrative

Gemini DR **10** — architectural blueprint for **Module 1b / Phase Router**: a deterministic FSM overlaid on the trading daemon so one codebase switches strategy by tournament phase without manual rewrites or restarts. Prerequisite reports: DR 08 (market map) + DR 09 (in-play/pregame risks). **Appendix JSON partially corrupted** (`state_machine`, `migration_from_v1`, `open_questions` empty) — prose + tables are authoritative; YAML hand-merge into existing `config/market_phases.yaml` (repo name) rather than a separate `tournament_phases.yaml` file unless refactor is explicitly scoped.

### Ten-state FSM [TENTATIVE — single Gemini source]

| State | Window (2026) | Bot focus |
|-------|---------------|-----------|
| `pre_tournament` | Until 2026-06-11 | Outrights + long-duration advance only |
| `group_stage` | 2026-06-11 → 06-27 | Group advance + 90-min ML; max third-place contagion |
| `group_to_knockout_transition` | **Zero-day 2026-06-27** | Cascade advance resolutions; precompute R32 bracket; **disable cross-venue** |
| `round_of_32` | 2026-06-28 → 07-03 | Deprecate group regex; Reach-R16 / To Advance parity |
| `round_of_16` | 2026-07-04 → 07-07 | Roll capital to QF reach markets |
| `quarterfinal` | 2026-07-09 → 07-11 | **48h rest** — widest spreads, lowest KO adverse-selection epoch |
| `semifinal` | 2026-07-14 → 07-15 | Peak match liquidity; Reach-Final ≈ SF To Advance |
| `third_place` | 2026-07-18 (penultimate) | Lower volume; wider min spread |
| `final` | 2026-07-18 → 07-19 | Outright winner + single-match max deploy |
| `post_tournament` | After final whistle | Flatten books; archive ledger |

### Dual-validation transitions [TENTATIVE]

Calendar timestamp alone is **insufficient**. Transition executes only when **100% of relevant market resolutions** for the exiting phase have settled on-chain. Example: do not load `round_of_32` until all group advance contracts settled. Match-integer gates bind progression to FIFA fixture IDs: R32 exit after matches **73–84**; R16 **85–92**; QF **93–96**; SF **97–98**; final resolution on match **100**. Weather/postponement delays pause FSM without premature phase load.

### Config decoupling

- **`conviction.yaml`** — team probabilities + sizing only; hot-reload without FSM pollution
- **`market_phases.yaml`** (report says `tournament_phases.yaml`) — FSM calendar bounds, `scanner_phase_ids[]`, `operating_overrides`, `cross_venue_enabled`, `require_full_settlement_to_exit`

### Per-phase operating overrides (dynamic injection)

| Parameter | Group stage | Knockout phases |
|-----------|-------------|-----------------|
| `cancel_hours` | 10 | **24** (recovery / card suspension volatility) |
| `min_mid` | ~0.05 OK for outliers | Tighten (e.g. halt below **0.15** in SF) |
| `bilateral_threshold` | Tighter (capture rewards) | Wider (preserve capital on elimination risk) |
| `daily_adverse_cap` | Spread across many markets | Concentrated on fewer fixtures |
| `cross_venue_enabled` | true (alert-only v1) | **false** during zero-day transition |

### Scanner regex injection

Phase router injects `scanner_phase_ids[]` — deprecate prior round patterns on transition. Separate **90-min regulation** (`^(.+)-vs-(.+)-winner$`) from **To Advance** (`^will-(.+)-advance-past-(.+)$`) and **Reach milestone** patterns. Group pattern example from report: `^world-cup-(.+)-to-advance-to-knockout-stages$`; R16 era: `^world-cup-(.+)-to-reach-quarterfinals$` [TENTATIVE regex — validate against live Gamma slugs].

### Conviction carry-forward / ghost quote

On elimination: broadcast **`--cancel-team`** (CLI: `phase purge --team <slug>`) to purge **all open orders across all phases** for that team before the ghost-quote window (stadium API ~3s vs consumer stream 40–60s). At **85′ tied** in KO: halt 90-min market quoting immediately (draw → 1.0 in regulation book while advance still ~0.5).

### CLI + systemd

| Command | Purpose |
|---------|---------|
| `world-cup-bot phase status` | JSON: active state, time-in-state, settlement threshold to next transition |
| `world-cup-bot phase set <phase_id>` | Force transition (qualitative deep-liquidity pre-list) |
| `world-cup-bot phase purge --team <slug>` | Emergency carry-forward cancel |

- **Auto-detect default:** UTC vs `calendar_start`/`calendar_end` in YAML + Gamma event mix regex confirmation
- **Override:** `WC_TOURNAMENT_PHASE=<state>` bypasses calendar + settlement checks
- **systemd:** `SIGUSR1` reload re-parses phase YAML without dropping websockets

### Ledger extensions

Append on every trade/cancel/poll: `tournament_phase`, `market_phase_id` (regex category hash).

### Testing + migration

1. **Replay logs** — 2022/2023 WC JSONL accelerated; validate T-10h halt + dual-validation
2. **Shadow May 2026** — dry-run with manual `phase set` to reject premature R16 quotes
3. **Migration checklist:** extend scanner regex array; isolate resolution typologies; FSM daemon; `--cancel-team` routing; JSONL schema expansion

**Estimated effort:** **12 engineer-days** [TENTATIVE — appendix]; DR 08 prose had ~4d for scanner-only — router + FSM + ledger is larger scope.

## Snippets

> Mixing phase transition logic into conviction.yaml creates an anti-pattern — probability hot-reloads must not re-evaluate the chronological FSM. [Source: Tournament Phase Router Design.docx]

> During group_to_knockout_transition, cross_venue_enabled: false — dedicate API budget to latency-sensitive book-pulling on primary venue. [Source: Tournament Phase Router Design.docx]

> Appendix JSON state_machine array empty in Gemini export — build FSM table from prose above. [Ingest note 2026-05-30]
