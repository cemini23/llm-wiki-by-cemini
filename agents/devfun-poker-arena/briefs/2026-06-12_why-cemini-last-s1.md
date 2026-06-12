---
title: Why Cemini is last — Tournament S1 post-mortem
type: brief
tags: [brief, poker, devfun-arena, tournament, placement, gin-style, rebuy]
created: 2026-06-12
updated: 2026-06-12
competition: cmq6l1gnq0lkz60y9i9d9eca1
agent_version: s1t.2785b1d.tournament-s1
---

## Target

Operator (claude.ai + prod handoff)

## Summary

**Rank 132 / 132+, 0 chips, busted.** Not mainly “bad poker math on one hand” — **years of stack came from ultra-tight-passive play (9.4% VPIP / 1.4% PFR) in a LAG field**, plus **showdown blowups** when we finally contest. **Gin-style aggression shipped but never got Arena sample** because **rebuy failed**: wallet holds ~0.1 MON, rebuy fee is **250 MON**.

## Body

### 1. Field mismatch (primary)

Leaders play **2–5× our VPIP** and **10–20× our PFR**. We fold ~95% of hands to zero delta. Tournament chips require **contesting pots**; passive survival bleeds via occasional big losses and no compounding wins.

**vs gin/poker-bot v1:** Their bot is simpler (score-based preflop + HU aggression) but **plays more hands**. Our stack layers (cold-start, lane_tight, KO survival, HL fold patches) **stacked on a nit base** and suppressed opens.

### 2. Where chips went (loss attribution)

From 1556 submission rows (−6930 chips total):

- **1473 pushes** (no chip delta) — fold/check out
- **−6867** in **≤5 mega-loss showdowns** (TT, 99, QQ, AK-type lines)
- **−320** preflop fold tax; **−7052** postflop

**Final bust:** `Ac Kc` −330 vs two pair on `8s Tc Qs 2c 8h` at ~330 stack.

Full tables: `reports/hl-loop/loss_attribution_s1_2026-06-12.md`

### 3. HL loop misfit

HL optimized **fold frequency** on a bot already folding **>90%**. Each R-round added river/fold guards; **PFR stayed ~1%**. Correct pivot (shipped `2785b1d`): gin `anti_threshold` preflop + HU c-bet, cold-start steal off, placement_chase bypass — but **unvalidated live**.

### 4. Rebuy / wallet (current blocker)

| Item | Value |
|------|--------|
| Agent | `cemini_wiki_poker` (`cmpy4lcyi001y11vnekn1zlo3`) |
| Wallet | `0x7d2a755dfa58e70eFde21d5e88b23632AfeF0bEF` |
| Balance | **~0.099 MON** |
| Rebuy fee | **250 MON** (402 `paymentRequirements`) |
| Error | `503 NATIVE_TRANSFER_PREFLIGHT_FAILED` |

**Operator actions:**

1. Send **≥250 MON** to agent wallet on Monad (or use Arena UI manual rebuy if available).
2. Restart lobby or wait for next rebuy attempt after fund block clears.
3. Confirm `hands` increment in export; re-check VPIP/PFR after **≥50 hands**.

**Code fix (local, deploy when ready):** wallet precheck + 6h rebuy backoff on fund failure (`run_cemini_lobby.py`) — stops log spam and surfaces balance vs fee.

### 5. Success criteria after rebuy

| Metric | Current | Target (4–7 days live) |
|--------|---------|----------------------|
| Arena VPIP | 9.4% | **18–25%** |
| Arena PFR | 1.4% | **8–15%** |
| Placement | 132 | Top 50% field |
| HL R23 | blocked at 1556h | Run at **≥1606h** — **aggression patches only** |

### 6. Do not do next

- Another HL round of **more folds** on EP/river without PFR recovery.
- Deploy-only strategy changes with **0 chips** and no export movement.
- Assume self-play gin gate (54% VPIP) transfers to Arena without measurement.

## Sources

- Arena export `agents.jsonl` / `submissions.jsonl` on `cemini-prod`
- `reports/hl-loop/latest_analyze.txt` (last 50 seated hands)
- `reports/hl-loop/loss_attribution_s1_2026-06-12.md`
- gin/poker-bot v1 audit (session 2026-06-11)
- Prod wallet/rebuy probe 2026-06-12
