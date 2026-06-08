---
title: "Discord meta + tournament foundation (Jun 6)"
type: brief
tags: [brief, poker, devfun-arena, tournament, discord-intel, strategy]
created: 2026-06-06
status: ACTIVE — operator decisions; no official docs yet
source: Discord (dev.fun team) — [NEEDS VERIFICATION on docs.dev.fun when site stable]
---

## Target

Operator — dev.fun Playground / Tournament season strategy (`cemini_wiki_poker`).

## Summary

Arena site instability explains recent push/deploy friction — **rsync + manual restart** if SSH drops on deploy script; code still lands. **Nuts + R21–R22 live on prod.**

Strategic priority stack:

1. **Qualify** (top-20 **current** playground season) — chip survival, no rebuy mindset even in playground.
2. **Main KO tournament** (paired season) — Playground S*N* → free entry Tournament S*N*; **no rebuy**; early cold-start/HUD recon must not bust the run.
3. **Optimize** after qualification secured — field exploits, not playground vanity metrics.

**Season pairing (Discord 2026-06-08, clarified):** Multiple tournament seasons; **Playground S2 → Tournament S2** same logic as S1. S1 playground qual = **Tournament S1** only — does **not** auto-enter S2 tournament. Re-qualify on each new playground season.

Discord also flagged: uncertain multi-agent rules next season, X verification may apply to all entries, **more jackpot types** beyond S2 27o bluff.

---

## Discord intel (unofficial until docs update)

| Topic | Reported | Our posture |
|-------|----------|-------------|
| Site issues | Team working on fixes; explains API timeouts / deploy noise | Rsync-first deploy; `systemctl restart` if remote step 255 |
| Multi-agent | Unclear if multiple agents allowed next playground | **L5 probe pattern ready** — register unclaimed, claim winner only; don't depend on multi-submit |
| X verification | May be required for all agents (not just claim) | One **verified** handle (`cemini_wiki_poker`) stays primary; jackpot probe uses separate handle only if rules allow |
| Jackpots | S2 27o bluff + **additional jackpot types** coming | Keep `jackpot_27_decide.py` isolated; generic `jackpot_lane` config when rules drop |
| Documentation | Likely **not** updated yet | Treat Discord as `[TENTATIVE]`; verify via UI + hand export before rule-dependent code |

---

## Nuts flag — enable now?

**Yes**, with caveats already gated in code:

| Gate | Status |
|------|--------|
| `hand_nuts.py` + unit matrix | ✅ |
| Regression spots (4 nuts cases) | ✅ |
| Anti-profiling audit | ✅ 2026-06-06 |
| Preflight pytest | ✅ 147/147 (timeout fix 180→360s) |
| River-only, never-widen-preflop | ✅ by design |
| `CEMINI_NUTS_DETECT=0` code default | ✅ prod `.env` overrides to `1` |

**What it fixes:** catastrophic river folds (quads, nut straight) and enables value when enumeration proves unbeatable.

**What it does not fix:** early-phase busts, BTN limp-calls, cold-start spew — separate HL patches.

**Rollback:** set `CEMINI_NUTS_DETECT=0` in prod `.env` + `systemctl restart cemini-devfun-poker-lobby.service` — zero code deploy needed.

---

## Tournament foundation — design principles

### Problem we lived (S1a)

- Rank **#4 → ~#215 @ 540 chips** before HL patches — one bad streak from season over (rebuy API was disabled).
- **Cold-start HUD** + chart-first + multiway limp defense were under-tightened early.
- Volume/compounding saved us after fixes — but **main KO won't offer that reset**.

### Foundation layers (priority order)

```
┌─────────────────────────────────────────────────────────────┐
│ L0  SURVIVAL — never bust below buy-in / table min           │
│     chart-only EP/MP, SB complete fold, BTN trash no limp    │
│     stagger locks when ranked, qualification_guard tiers     │
├─────────────────────────────────────────────────────────────┤
│ L1  RECON — HUD cold-start: chart-first until N hands/villain│
│     export top-20 VPIP seed on deploy (S1b optional)         │
│     slow join retry when #1 / top-5 (FIRST/LEAD protect)   │
├─────────────────────────────────────────────────────────────┤
│ L2  QUALIFY — chips/hand > win rate; volume without spew     │
│     playground top-20 buffer; don't chase #1 width in build  │
├─────────────────────────────────────────────────────────────┤
│ L3  EXPLOIT — rock steal / maniac call margins (S1b/KO)    │
│     field intel briefs → targeted HL rounds only             │
├─────────────────────────────────────────────────────────────┤
│ L4  JACKPOT LANES — isolated agents, session caps (lottery) │
│     never merge into prod qualification decide()             │
└─────────────────────────────────────────────────────────────┘
```

### Cold-start / early session checklist (KO-critical)

Before any "optimize for EV" widening:

1. **Hands 1–50:** EP VPIP ≤ 18%, zero trash opens, zero BTN limp-calls (`_is_sb_complete_trash`).
2. **HUD:** `cold_start=True` until ≥10 observed actions per villain ID — no steal widening.
3. **Join pace:** `CEMINI_FIRST_JOIN_RETRY_S=1800` when rank ≤1 with buffer; don't flood tables during recon.
4. **Monitor:** `./scripts/cemini_playground_status.sh` — if chips < 2× buy-in, flip to **survival-only** profile (disable steals, lead_blind_steal only with chart raise).
5. **Regression library:** every analyze `-100` row → frozen spot before next deploy.

---

## Planned: full-season retrospective (premium models)

**When:** after S1b closes (Jun 11+) or before KO if site exports stable.

**Deliverable:** one brief + patch backlog ranked by chip delta × frequency.

| Phase | Action | Tooling |
|-------|--------|---------|
| P0 | Export full competition hands + field report | `export_competition_hands.py`, `competition_field_report.py` |
| P1 | Aggregate: position leaks, villain archetypes, time-of-day variance | local scripts |
| P2 | **1–2 premium model passes** on anonymized analyze + worst-50 hands | DeepSeek R1 / Claude via OSINT routing — **strategy only, no runtime LLM** |
| P3 | Output: ranked patch list, cold-start policy tweaks, KO env table | `briefs/2026-06-XX_s1-retrospective.md` |
| P4 | Implement top 3 patches + regression spots; preflight; deploy when site stable |

**Prompt shape:** "Given these 50 worst hands and field VPIP distribution, what *structural* guards are missing — not hand-specific hero calls?"

---

## Next playground / KO — decision tree

```
Site stable?
  no  → hold deploys; keep lobby running; log only
  yes → deploy queued HL patches; enable nuts if not already

Multi-agent allowed?
  yes → L5: 3–5 unclaimed probes S1b; claim best by rank+chips
  no  → single verified agent; A/B via local self-play + eval only

X required for all entries?
  yes → register/verify before window; one public brand handle
  no  → probes stay unclaimed until claim gate

Jackpot rules published?
  yes → P3 jackpot register per `agents/devfun-poker-arena/briefs/2026-06-04_s2-jackpot-27-bluff-scope.md`
  no  → feature-flag hands list; no prod bleed
```

---

## Immediate actions

| # | Action | Owner | Status |
|---|--------|-------|--------|
| 1 | Enable `CEMINI_NUTS_DETECT=1` prod | agent | **done** 2026-06-06 |
| 2 | Pause deploy until Discord/site stable | operator | recommended |
| 3 | HL R20 BTN limp patch | agent | **on prod** |
| 4 | Schedule S1 retrospective brief | operator | after Jun 11 |
| 5 | S1b env flip Jun 7 | operator | ROADMAP table |
| 6 | Jackpot probe creds isolated | operator | P3 when S2 live |

---

## Edge boundary

- No Discord quotes as public X content without scrubbing.
- No prod credential rotation during site outage.
- Jackpot hunt on main bot is gated (`maybe_hunt_action`); no parallel probe service.

## Sources

- Discord dev.fun team (2026-06-06, 2026-06-08 season pairing)
- `agents/devfun-poker-arena/briefs/2026-06-03_playground-top20-qualification.md`
