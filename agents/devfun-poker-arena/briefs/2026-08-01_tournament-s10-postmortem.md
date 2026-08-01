---
title: Tournament S10 post-mortem — bust root cause + leader research
type: brief
tags: [brief, poker, tournament, s10, postmortem, research]
created: 2026-08-01
target: agents/devfun-poker-arena
---

## Target

Operator + next-season decide()/lobby posture. Evidence from prod journal + Arena leaderboards + public GitHub (2026-08-01).

## Summary

We did not lose once — we **busted four times**, paid **four rebuys**, peaked on **rebuy capital** (#9 @ 2433; API `bestRank=2`), then flipped gin ON while short and died permanently when the **5th rebuy jumped to 250 MON** with only ~1.54 MON left. Leaders are not mysterious CFRs in public repos; they are high-volume, positive chip/hand printers. Public stealables: **System 7** (SPR heuristics + versioned strategy + coach A/B) and **gin/poker-bot** (closed-loop strategy iteration + profiler).

## Regime disclosure

Comparisons in this brief are **single-regime** (HU Researcher sandbox and/or 6-max Playground chip-qual only). Not a multi-regime leaderboard claim; no free cross-regime superiority asserted. Tournament S10 bust timeline is ops evidence for that board only; Playground S9/S10/S11 leader rows are separate single-board snapshots.

## Exact failure timeline (journal CHASE + rebuy)

| When (UTC) | Event | Evidence |
|------------|-------|----------|
| Jul 30 13:08 | Enter T10, 1000 chips, rebuyCount=0 | join after pay |
| Jul 30 ~13–17 | Too tight (~76% fold) | phase action mix |
| Jul 30 17:40 | **Rebuy #1** → 1000 chips (hands 216) | rebuy after pay |
| Jul 30 20:38 | **Rebuy #2** → 1000 (hands 380) | bust from ~842 |
| Jul 31 00:18 | Peak **#9 @ 2433** | CHASE log max chips |
| Jul 31 01:08–01:28 | −833 chips in ~20m (#9→#20) | notable drop |
| Jul 31 09:09–09:19 | −899 chips (#26→#43) | notable drop |
| Jul 31 10:18 | **Rebuy #3** → 1000 (hands 1085) | bust from ~852 |
| Jul 31 12:58 | **Gin ON deploy** (operator panic widen) | restart + env |
| Jul 31 12:58–17:00 | Fold 38% / raise 18% (was ~79% / 7%) | post-gin mix |
| Jul 31 16:19 | Short stack **154 chips** still raising | journal actions |
| Jul 31 17:00 | **Rebuy #4** → 1000 (hands 1446) | last successful pay |
| Jul 31 17:10–17:20 | Spike to 1900 then wipe; **rebuy #5 fails** (needs 250 MON) | INSUFFICIENT_NATIVE |
| Aug 01 | Dead at 0, rank ~67, rebuy paused | wallet ~1.54 MON |

## Root causes (ranked)

1. **Wrong objective function mid-run.** Playground chip-qual TAG (we finished P10 #6 @ 18743 with **8.2%** “correct” rate) was kept into KO, then abruptly inverted to gin chase while short. Neither mode matches what T10 leaders do.
2. **Rebuy addiction masked insolvency.** Four paid resets created the illusion of a climb; peak stack was not organic from the opening 1000. Wallet drained; fee stepped to **250 MON**.
3. **No short-stack / ICM gate.** At 154–300 chips with chase+gin we kept raising. Leaders’ efficiency (~6–8 chips/submission) implies they avoid spew when short.
4. **Blind tax while nitty.** Pre-gin fold ~77–79% with raise ~5–8% cannot beat a field printing volume at VPIP~0.15–0.25 equivalent.
5. **Ops thrash.** Mid-tournament posture changes (prize cutoff, survival, gin, nemesis) without a frozen control arm or A/B. System 7’s whole point is *don’t* do this.
6. **Telemetry gap.** `s10-tournament-live` export crawl never ingested T10 `competition_id` hands (export is stuck on an old comp). Preflop jsonl only has 33 T10 rows. We cannot reconstruct hole-card-level bust spots from export — journal + leaderboard only.

## What leaders actually look like (live boards)

### Tournament S10 (now)

| Rank | Handle | Chips | Subs | Correct rate | Chips/sub |
|------|--------|------:|-----:|-------------:|----------:|
| 1 | whalealert | 18556 | 2513 | 15.2% | ~7.4 |
| 2 | page | 15968 | 2506 | 22.1% | ~6.4 |
| 3 | long_tu | 11024 | 2279 | 14.7% | ~4.8 |
| 4 | dre4mboat_ai | 10323 | 1305 | 13.4% | ~7.9 |
| 5 | thirteenshotv2 | 9661 | 1626 | 22.6% | ~5.9 |
| 14 | StartupBros | 3934 | 1959 | **30.5%** | ~2.0 |
| 17 | range_ledger | ~3541 | 1640 | **~49%** | ~2.2 |
| us | cemini_wiki_poker | 0 | 1461 | 11.9% | 0 |

Pattern: **volume + positive chip expectancy**, not ultra-high winrate. Selective high-WR bots (range_ledger) sit mid-pack on chips.

### Playground S10 (final board we were on)

lodestar, joseph, cosmometrics, batu_sabar, StartupBros, **us #6**, page, kav_grind, alex_nft, reichelligahh, flattened_v2*, xiishii_felt, si_nekat…

### Playground S11 (current)

flattened_v2_guard_04, lodestar, godam, pot_sheriff, lone_wolff, flattened_v2, flintlock, si_nekat, sam_whale, chad_bets…

### Playground S9 (past)

flattened_v2, highroller, si_nekat, neon_savage, pokerkit-starter-*, dre4mboat_ai, **solid_nash**, kav_grind…

### Past tournament intel (prior brief)

T9 #1 **halloran** — VPIP~0.26, PFR~0.11, AF~1.05, ~+16 chip/hand, huge volume. Not a nit; not a maniac.

## Public repo research (GitHub / HF)

**No public repos found** that clearly belong to whalealert, page, long_tu, halloran, lodestar, or flattened_v2 under those handles.

### Stealable Arena-adjacent repos

| Repo | Why it matters |
|------|----------------|
| [quantarmyz/system7-poker-arena](https://github.com/quantarmyz/system7-poker-arena) | **Best steal.** Deterministic heuristic + SPR/outs/texture, versioned `strategies/*.json`, hybrid LLM only on hard nodes, SQLite telemetry, coach A/B vs frozen control. Explicitly built for dev.fun Arena. |
| [gin/poker-bot](https://github.com/gin/poker-bot) | Self-improving strategy files; `anti_threshold` / `royal_adaptive` / `survival_balanced`; playstyle profiler (VPIP/PFR/AF); S1 tournament participant; adaptor for starter kit. |
| [devfun-org/poker-arena-starter-kit](https://github.com/devfun-org/poker-arena-starter-kit) | Official kit everyone forks. |
| [MaximKabaev/poker-arena](https://github.com/MaximKabaev/poker-arena) | Another Arena client stack (introspect schema). |
| HF papers (PokerGPT, Deep CFR, PokerKit lib) | Research refs — **not** drop-in Arena bots; multiway CFR still hard. |

## How to fix (do not ship mid-rebuy panic again)

### Non-negotiable process

1. **Frozen control arm.** One tagged decide+env. No gin flip while short.
2. **Rebuy budget cap.** Max N rebuys or max MON; auto pause (we finally did this after the damage).
3. **Hand telemetry that works.** Fix export crawl for live T10/S11 competition ids; record every decide with hole cards + stack + street + reason.
4. **A/B offline first.** Self-play / eval panel before lobby (System 7 + gin/poker-bot pattern).

### Strategy (next season / S11)

1. **Baseline = halloran-class TAG-plus**, not playground ultra-nit and not full gin: target ~20–26% VPIP, positive chips/hand, volume.
2. **Steal System 7 structure:** SPR commit gates, versioned ranges JSON, short-stack push/fold table when stack < ~15–20bb, HUD archetype adjusts — *not* global margin spam.
3. **Steal gin/poker-bot loop:** iterate named strategies with profiler gates; promote only if bb/100 beats frozen prior.
4. **Short-stack mode overrides chase.** When table stack < 20bb: disable gin widen and chase open equity; push/fold only.
5. **Do not rebuy T10** unless funding ≥250 MON *and* short-stack patch is live. Prefer **Playground S11** with control arm.

## Sources

- Prod journal `cemini-devfun-poker-lobby.service` 2026-07-30 → 2026-08-01
- Arena leaderboards: T10 `cms7hr1il20ya13wjj29s1o8h`, P10/P11/P9 comps in `.env`
- `briefs/2026-07-28_tournament-s10-go-live.md`, `briefs/2026-07-31_tournament-s10-climb-widen.md`
- GitHub: quantarmyz/system7-poker-arena, gin/poker-bot, devfun-org/poker-arena-starter-kit
- Brave search 2026-08-01 (dev.fun Arena + HF poker papers)
