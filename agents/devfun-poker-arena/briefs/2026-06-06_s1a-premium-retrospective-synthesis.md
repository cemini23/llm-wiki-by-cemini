---
title: "Playground S1a — premium retrospective synthesis (4-model merge)"
type: brief
tags: [brief, poker, devfun-arena, retrospective, premium-llm, s1a, cursor-subagent]
created: 2026-06-06
updated: 2026-06-06
models:
  primary_cursor:
    - grok-4.3 (Cursor subagent)
    - gpt-5.3-codex (Cursor subagent)
  prior_api:
    - x-ai/grok-4.3 via OpenRouter
    - deepseek-reasoner via DeepSeek API
export: reports/exports/playground-s1-s1a-snapshot-2026-06-06/
raw_outputs: briefs/premium-pass-outputs/
status: P2 COMPLETE (v2) — 4-model merge; implement via HL rounds only
---

## Target

Unified retrospective for `cemini_decide.py` + KO foundation from **four premium passes**. Strategy-only — zero runtime LLM at decision time.

## Summary

**Unanimous across all 4 models:** early blind/EP trash + cold-start recon nearly busted S1a; **do not widen base VPIP** (#1 @ 12.3% / 9% WR); KO hour-one = survival lockdown; S1b exploits are **table-scoped toggles** only.

**Cursor Codex framing (new):** root failure mode is **phase confusion** — exploit logic firing before risk budget allows. Fix = explicit **two-lane architecture**: Survival Lane (S1a/KO hour-one) vs Conditional Exploit Lane (S1b, gated).

**Prior DeepSeek value kept:** S1b conditional 3-bet value, bounded BB defend vs proven maniacs, trap-call AA/KK — all **rejected as defaults**, **GO only** under strict gates (unchanged from v1 adjudication).

---

## Four-model consensus (implement)

| Theme | Grok×2 | DeepSeek | Codex | Decision |
|-------|--------|----------|-------|----------|
| Cold-start hands 1–50 | ≤8–10% VPIP, no steals/defends | Same | `COLD_START_NO_STEAL_UNTIL_DATA` | **ADOPT** — ≥10 hands/villain before any steal |
| EP/UTG/SB trash | #1 gap all passes | Same | SB complete block P0 | **ADOPT** — freeze + regression spots |
| Base VPIP/PFR | Lock | Lock | Lock | **LOCK** 12.3% / 4.3% |
| BTN limp-trash | Shipped R20 | BTN filter | Mirror to CO | **ADOPT** — `CO_LIMP_TRASH_MIRROR_R20` |
| KO no rebuy | Sit-out / join gates | 40bb sit-out | Hour-one = cold-start always | **ADOPT** — join gate <2× buy-in, 3600s retry |
| Nuts + stagger | Keep | Trap AA/KK S1b | Keep shipped | **KEEP** nuts; trap = S1b gated |
| Nemesis hunterguy102 | Rock mode | Tighter vs him | Tighten-first not counter-aggro | **ADOPT** — seed HUD at deploy from export |
| S1b LAG exploit | Conditional toggles | Wide defend/3-bet/float | Two-lane, toggles gated | **S1b only** — see toggle contract below |

---

## Two-lane architecture (Codex — adopt as mental model)

```
SURVIVAL LANE (default)
  S1a build, KO hour-one, cold-start, qualification_protect ON
  → chart-first, fold trash, no steals, stagger locks

CONDITIONAL EXPLOIT LANE (opt-in per table)
  ALL must be true:
    hands_observed ≥ 20 on ≥2 villains at table
    hero stack ≥ 60bb
    qualification_protect OFF
    HUD maniac confirmed (VPIP>45%, 3b%>30%)
    table ≤ 2 other LAGs
  → value 3-bet, bounded BB defend, trap AA/KK vs high-3b maniac only
```

**New from Cursor Grok:** gate **every** S1b toggle on `qualification_protect` explicitly — not just cold-start.

---

## S1b toggle contract (merged DeepSeek value + survival gates)

| Toggle | From | Active when | Rejected as default? |
|--------|------|-------------|----------------------|
| `THREE_BET_LAG_VALUE_ONLY` | DeepSeek + all | Exploit lane + JJ+/AQ+ vs CO/BTN LAG open | Yes — S1a/KO off |
| `DEFEND_BB_VS_STEAL_CONDITIONAL` | DeepSeek | Exploit lane + top 40% vs steal, max 30% stack | Yes — not K7o default |
| `TRAP_AA_KK_VS_HIGH_3B` | DeepSeek | Exploit lane + maniac 3b% > 30% + >80bb | Yes |
| `NEMESIS_EXTRA_TIGHT` | All | hunterguy102 / Thaddius — always on | No — tightening only |
| Postflop MDF / float / CR TPTK | DeepSeek | — | **DEFER** all passes |

---

## Ranked patch backlog (4-model merge)

| Pri | Guard | Sources | Status |
|-----|-------|---------|--------|
| P0 | `COLD_START_NO_STEAL_UNTIL_DATA` | Codex, Grok×2, DeepSeek | HL R21 |
| P0 | `CO_LIMP_TRASH_MIRROR_R20` | Codex, DeepSeek, synthesis | HL R21 |
| P0 | `SB_COMPLETE_TRASH_BLOCK` | Grok×2, Codex, analyze | Verify + spot |
| P0 | `EP_OPEN_BLOCK` | Grok×2 | Mostly shipped — audit |
| P1 | `JOIN_PACE_STACK_PROTECT` | Grok×2, Codex — stack <2000 → 3600s retry | lobby script |
| P1 | `NEMESIS_HUD_SEED` | Grok Cursor, DeepSeek — startup seed from export | S1b deploy |
| P1 | `qualification_protect` gates all S1b toggles | Grok Cursor **new** | env + decide |
| P2 | `THREE_BET_LAG_VALUE_ONLY` | DeepSeek (gated) | S1b flip Jun 7 |
| P2 | `TRAP_AA_KK_VS_HIGH_3B` | DeepSeek (gated) | S1b + regression |
| P3 | `STAGGER_LOCK_INTERACTION` audit | Grok Cursor **new** | preflight |
| P3 | `POSTFLOP_MDF_DRYBOARD` | DeepSeek | **Deferred** |

**Shipped:** BTN limp R20, `CEMINI_NUTS_DETECT=1`, stagger locks, HL R8–20.

---

## Cold-start policy (final — all models)

| Window | VPIP | Opens | Defends | Join |
|--------|------|-------|---------|------|
| 1–50 | ≤10% | 77+/ATs+/AQo+ CO/BTN only; tighter EP | **Fold all** vs raises | 1800s retry if ranked |
| 51–200 | ≤12% | Chart-only; no HUD steals | BB chart pairs + Axs vs LAG only if HUD partial | Normal unless <2000 chips |
| Exploit flip | 12–15% | Table toggles | Maniac margins | S1b compete env |

**Flip trigger:** 200+ hero hands AND 20+ hands on ≥2 villains AND stack ≥60bb AND rank ≤20 with buffer AND `qualification_protect` off.

**KO hour-one:** force Survival Lane regardless of chip lead (Codex + Grok Cursor).

---

## KO foundation (no rebuy)

1. Never treat playground rebuy history as safety net.
2. Join gate: stack < 1000 (buy-in) → extend retry 3600s; avoid 409 loops.
3. Max preflop commit: min(stagger lock, 12–15% stack) unless AA/KK/QQ or nuts flag.
4. All-in calls: AA/KK only when stack would stay ≥40bb (DeepSeek + Grok).
5. Table selection: avoid 3+ maniacs when stack <40bb (when API exposes roster).
6. Nemesis: hunterguy102 → tighten vs opens, never ego-defend (Codex: tightening-first).

---

## Regression spots (merged — next HL)

| ID | Spot | Forbidden |
|----|------|-----------|
| `prod_cold_start_btn_no_steal` | BTN 98s, first 10 hands unopened | bet/raise |
| `prod_q5o_co_vs_limp` | CO Q5o multiway limp | call/raise |
| `prod_72o_sb_complete` | SB 72o limped pot | complete |
| `prod_nemesis_tight_vs_hunter` | SB A5s vs hunterguy102 open | call |
| `prod_s1b_toggle_gate_low_stack` | Maniac table, hero <60bb | 3-bet lane |
| `prod_k7o_bb_no_exploit_cold` | BB K7o vs steal, HUD cold | call (DeepSeek defend rejected here) |

---

## What we kept from each pass

| Pass | Valuable lessons retained |
|------|---------------------------|
| **DeepSeek API** | Detailed S1b toggle specs; trap-call AA/KK; nemesis per-villain notes (Thaddius barrels, 0xJeff 3× sizing); regression spot granularity |
| **Grok OpenRouter API** | Compact survival lockdown; stack sit-out <18bb; grok_cluster_lock concept |
| **Grok Cursor subagent** | `qualification_protect` gates all toggles; nemesis seed at startup; stagger re-audit; 3600s join retry |
| **Codex Cursor subagent** | Two-lane architecture; phase confusion diagnosis; forbidden-action regression priority; explicit guard naming |

---

## Rejected (all passes agree)

- Base VPIP/PFR widening in S1a or KO hour-one
- Default BB defend K7o / float QT / MDF on dry boards
- Global 3-bet expansion without maniac HUD + stack gates
- Leaderboard vanity aggression while #1 with qualification buffer

---

## Raw outputs index

| Model | Path | Method |
|-------|------|--------|
| Grok 4.3 | `premium-pass-outputs/grok-4.3_cursor_subagent.md` | **Cursor subagent** |
| GPT-5.3 Codex | `premium-pass-outputs/gpt-5.3-codex_cursor_subagent.md` | **Cursor subagent** |
| Grok 4.3 | `premium-pass-outputs/grok-4.3_20260606T1556Z.md` | OpenRouter API |
| DeepSeek Reasoner | `premium-pass-outputs/deepseek-reasoner_20260606T1556Z.md` | DeepSeek API |
| Prompt | `reports/exports/.../premium_pass_prompt.txt` | shared input |
| Re-run script | `scripts/s1a_premium_retrospective_pass.py` | API fallback |

---

## Implementation status

| Field | Value |
|-------|-------|
| Status | **P2 COMPLETE v2** — Cursor subagent + prior API passes merged |
| Next | HL R21: cold-start + CO limp mirror; S1b append Jun 11 |
| Operator | Review two-lane architecture before S1b env flip |

## Sources

- @briefs/2026-06-06_s1a-retrospective-snapshot.md
- @briefs/2026-06-06_discord-meta-tournament-foundation.md
