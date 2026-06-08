---
title: S2 heavy gap audit v2 — 3-model synthesis (138k rows, 101 rivals ≥200h)
type: brief
created: 2026-06-08
updated: 2026-06-08
pack: reports/gap-audit/pack-s2-heavy
models: [claude-opus-4-8-thinking-high, gpt-5.3-codex, kimi-k2.5]
export: reports/exports/playground-s2-live-archive
status: SHIPPED — S2 audit consensus patches (2026-06-08)
---

## Target

CeminiSuite / operator — **S2 playground qual** (`cmq57o53r0bhw18g23qkydb08`). Full-field export now mature: **138,256** submission rows, **101** agents with **≥200 hands**, **15** deep rival profiles.

## Summary

**Verdict: WARN (2/3) + FAIL (1/3) → treat as WARN.** All three models agree: **do not widen to field LAG (~36% VPIP)**; top-20 qual is won by **disciplined TAG + archetype exploits**, not volume. Consensus leaks: **blind/EP preflop junk (−100 cluster)**, **nemesis/HUD too name-narrow vs 101 mature rivals**, **pot-won proxy ≠ chip delta** (export rank-28 / 3-hand agents row is stale vs 181 submission rows).

**Unique Codex angle:** dual-mode **range-shape asymmetry** — deny premium-nits preflop, value-iso loose-passives, never bluff stations.

**Unique Opus angle:** separate Playground S2 qual trajectory from eval-panel self-play gate — two independent deploy gates (see Regime disclosure).

**Unique Kimi angle:** `BLIND_BLEED_GUARD` + `EP_RANGE_LOCK` as P0 (aggressive seat locks).

## Body

## Regime disclosure

Cross-regime comparisons in this brief are **scoped per competition** — never pooled:

| Regime | ID / surface | Hero metric cited | Comparable? |
|--------|--------------|-------------------|-------------|
| Playground S1a | `cmpy2qy65002ud9ej6b7jjq0l` | UI adj bb/100 rank #3 (2820) | S1 chip qual only |
| Playground S2 | `cmq57o53r0bhw18g23qkydb08` | 138k-row export; rank ~28 / 181 submission rows | S2 qual only — not vs S1 |
| Poker Eval panel | DeepCFR eval season | adj bb/100 −17.45 | Eval gate only — not Playground chip rank |

**Narrowing:** S1 EV rank does not imply S2 rank; S2 early sample is not EV-certified; eval-panel gate is a deploy widen blocker, not a qual prediction.

### Data pack (built 2026-06-08T22:25Z)

| Layer | v1 (Jun 8 AM) | v2 (this run) |
|-------|---------------|---------------|
| Submission rows | 287,857 (S1 pack) | **138,256** (S2 live) |
| Rivals profiled | 10 fixed handles | **15** top-rank agents with **≥200h** |
| Rivals in field ≥200h | n/a | **101** (see `rivals_200plus.md`) |
| Prompt size | ~69KB | **~44KB** |
| Build cmd | `build_heavy_audit_pack.py` | `--min-hands 200 --max-rivals 15` |

Rival sample set: `0xJeff_ai`, `long_ngu_poker`, `float_engine`, `claude-sonnet-46`, `fefou_v2`, `ebay`, `phoenix-rises-nrkdhd-v10`, `jeremy_tingleson`, `wemby_guy_v2`, `crypto-bro-agent`, `zephyr`, `long_tu`, `alnitak`, `einstein`, `phoenix-rises-nrkdhd-v108`.

### Three-model consensus

| Theme | Opus | Codex | Kimi | Decision |
|-------|------|-------|------|----------|
| Verdict | WARN | FAIL | WARN | **WARN** (early S2 sample + stale rank) |
| No LAG widen | ✓ | ✓ | ✓ | **LOCK** |
| Blind/EP −100 leak | ✓ P0 | ✓ P0/P7 | ✓ P0 | **Continue HL patches** (R5 shipped) |
| Archetype HUD/nemesis | phoenix cluster | premium_nit / wide_passive / linear_aggro | Jeff overlay + TM fold | **BACKLOG P1** |
| Tight-measured threats | fefou_v2 class | alnitak/einstein/long_tu | TM nemesis fold | **Steal blinds, fold to their raises** |
| Loose-passive exploit | value not bluff | iso + thin value | LP value bet +15% | **Experiment toggles only** |
| Export metric caution | reset/lag | structural −33 bb proxy | 89% zero payouts | **Use HL analyze + chipDelta timeseries** |

### Rejected (≥2 models)

- Global VPIP → 36% to chase leaderboard
- Disable `first_protect`
- Separate 27o probe agent
- Optimize on `payout_chips` as true bb/100
- Hero-call wide vs 0xJeff without linear 3b/trap structure

### Ranked patch backlog (merged)

| P | Patch | Models | Status |
|---|-------|--------|--------|
| P0 | Preflop blind/EP trash + stack-off guards | 3/3 | **SHIPPED** R1–R5 |
| P0 | Eval-panel self-play gate (−17.45) before widen | Opus | **SHIPPED** |
| P1 | Nemesis **archetypes** (`premium_nit`, `wide_passive`, `linear_aggro`) | Codex | **SHIPPED** |
| P1 | `premium_concentration_index` + `raise_gap` in HUD | Codex | **SHIPPED** |
| P1 | Phoenix-farm cluster rule | Opus | **SHIPPED** (`phoenix-` prefixes) |
| P1 | Add `jagoan_neon` to nemesis_seed | Opus | **SHIPPED** |
| P2 | LP iso vs loose-passive (`CEMINI_ISO_PASSIVE_LP`) | Codex/Kimi | **SHIPPED** |
| P2 | Seat matrix v2 (`CEMINI_SEAT_MATRIX_V2`) | Codex | **SHIPPED** |
| P0 | Eval-panel gate (`CEMINI_EVAL_PANEL_GATE`) | Opus | **SHIPPED** |
| P3 | Jeff-specific 4b/trap overlay | Kimi | **SHIPPED** |
| P3 | Split nemesis toggles per class | Codex | **SHIPPED** (per-class env) |

### S2 experiment plan (consensus)

| Hypothesis | Toggle | Metric | Stop |
|------------|--------|--------|------|
| Archetype nemesis over name-only | `CEMINI_NEMESIS_ARCHETYPE=1` | per-regime delta vs premium_nit / wide_passive buckets | Revert if any bucket − over 300 encounters |
| Premium-nit overfold | `CEMINI_HUD_PREMIUM_NIT=1` | stack-off loss vs low-PFR | Revert if pot-win −2pp |
| LP iso accumulates | `CEMINI_ISO_PASSIVE_LP=1` | uncontested pots / 400h rank | Revert if rank −8 |
| Panel gate before widen | self-play eval | per-regime floor −17.45 bb/100 | No widen until pass |

### Artifacts

```
reports/gap-audit/pack-s2-heavy/          # audit_prompt.md + rival_samples/
reports/gap-audit/premium-cursor/
  opus_20260608T2225Z.md
  codex_20260608T2225Z.md
  kimi_20260608T2225Z.md
prompts/s2_gap_retrospective_audit.md     # S2 template
scripts/build_heavy_audit_pack.py         # --min-hands 200
```

### Re-run

```bash
./scripts/sync_export_archive.sh playground-s2-live
uv run python scripts/build_heavy_audit_pack.py reports/exports/playground-s2-live-archive \
  --min-hands 200 --max-rivals 15
# cursor-audit 3× on pack-s2-heavy/audit_prompt.md + rival_samples/
```

## Sources

- Prod export rsync 2026-06-08T22:17Z
- Cursor audit subagents Opus / Codex / Kimi 2026-06-08T22:25Z
- Prior v1 synthesis brief `2026-06-08_s2-heavy-audit-synthesis.md` (S1-scale 287k pack, same repo)
