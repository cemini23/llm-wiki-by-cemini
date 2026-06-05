---
title: "Gemini DR — WC tournament phase router architectural spec (v2)"
type: source
tags: [source, gemini-deep-research, world-cup-2026, phase-router, polymarket, k91]
keywords: [finite-state-machine, gamma-event-mix, phase-transitions, elimination-pruning, tournament-phases-yaml, ledger-attribution]
related:
  - sources/gemini-wc-tournament-phase-router-2026-05-30.md
  - concepts/world-cup-tournament-phases-lp-strategy.md
  - concepts/world-cup-advance-market-bot-v1.md
  - entities/tools/world-cup-bot.md
  - concepts/polymarket-sports-lp-operating-rules.md
  - sources/gemini-wc2026-knockout-market-map-2026-06-05.md
maturity: validated
read_status: deep-read
created: 2026-05-31
updated: 2026-05-31
---

## Relations

- @sources/gemini-wc-tournament-phase-router-2026-05-30.md — prior DR 10 baseline; this source adds implementation-level detail and test plan depth
- @concepts/world-cup-tournament-phases-lp-strategy.md — phase-by-phase synthesis target
- @concepts/world-cup-advance-market-bot-v1.md — v1 to v4 migration notes and module boundaries
- @entities/tools/world-cup-bot.md — implementation target for phase router hooks, CLI, and ledger fields

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Gemini DR — Tournament Phase Router Architectural Specification |
| Author | Gemini Deep Research |
| Type | docx synthesis report |
| Location | `cemini-librarian:/opt/cemini-bulk/research/Tournament Phase Router Design.docx` |
| Retrieved | 2026-05-31 |
| Read status | deep-read |

## Narrative

This report is a higher-granularity pass on the World Cup phase router design and confirms a deterministic **10-state FSM** as the safest control plane for the 48-team tournament expansion. It formalizes calendar + settlement-gated transitions ("Gamma event mix"), per-phase parameter overrides, elimination pruning, and replay/shadow testing requirements. It also reinforces separation between conviction data and phase mechanics to prevent strategy drift from hot-reload operations.

### Core architectural calls

| Area | Direction |
|------|-----------|
| State model | 10-state FSM (`pre_tournament` → `post_tournament`) with explicit enter/exit hooks |
| Transition guard | Require both chronological trigger and resolved market/oracle preconditions |
| Config separation | Keep phase mechanics in dedicated phase schema; keep team belief in `conviction.yaml` |
| Elimination risk | Trigger global team cancel across all derivative markets before oracle lag window |
| Ops control | Add CLI/state overrides and systemd env override for disaster recovery |
| Observability | Persist `tournament_phase` + `market_phase_id` on executions for phase-level PnL forensics |

### Notable implementation guidance

- Treat `group_to_knockout_transition` as a hard risk window: pause quoting and disable cross-venue routing.
- Increase cancel windows and tighten `min_mid`/risk caps as rounds compress and information asymmetry rises.
- Add durable transition loop that survives restarts and only advances when prerequisites are met.
- Use replay + shadow-mode validation before exposing capital to knockout phases.

### Quality note

The extracted appendix JSON block is partially malformed in the source export; prose and tabular sections remain coherent and were used as the canonical ingest reference.

## Snippets

> The transition model should not rely on wall-clock time alone; it must require both calendar and resolved-market conditions to avoid premature phase shifts. [Source: Tournament Phase Router Design.docx]

> Elimination events require immediate global pruning to prevent stale "zombie" exposure while oracle settlement lags. [Source: Tournament Phase Router Design.docx]
