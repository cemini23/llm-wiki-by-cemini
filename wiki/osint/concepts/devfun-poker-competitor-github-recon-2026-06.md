---
title: dev.fun Poker Arena — public competitor GitHub recon (2026-06)
type: concept
tags: [concept, poker, devfun, osint, competitor-recon]
keywords: [github, poker-agent, gin poker-bot, system7, kecodot, arena-pokerkit]
related:
  - concepts/devfun-poker-agent-challenge-2026.md
  - concepts/devfun-researcher-track-readiness-2026-06.md
  - entities/platforms/devfun-arena.md
maturity: draft
created: 2026-06-18
updated: 2026-06-18
---

## Relations

- @concepts/devfun-poker-agent-challenge-2026.md
- @entities/platforms/devfun-arena.md
- @sources/devfun-researcher-track-discord-welcome-2026-06-18.md

## Raw Concept

GitHub + Hugging Face sweep for **accidentally public** dev.fun Poker Arena competitor bots (Jun 2026). Goal: steal implementation patterns before Researcher Round (Jun 21).

## Narrative

### Match length correction [operator 2026-06-18]

Researcher Round / tournament seasons run **multi-day** continuous arena grinds (Playground S1–S3, Tournament S1–S2), **not** the 500-hand Poker Eval PVE benchmark. Official Researcher match parameters **not posted yet** — do not plan around Eval S5 500h defaults.

### Tier A — full public bots (high signal)

| Repo | URL | What it is | Steal priority |
|------|-----|------------|----------------|
| **gin/poker-bot** | https://github.com/gin/poker-bot | Full 6-max stack: `survival_sixmax`, `auto_research_v001`–`v008`, CFR Kuhn, population selfplay, promotion gates, arena adaptor | **P0** — closest to our problem shape |
| **kecodot/poker-agent** | https://github.com/kecodot/poker-agent | Data-driven engine: strategy mixer (limp_value / raise_exploit / hybrid), pool classifier, position preflop sizing, leak detector, MC equity | **P1** — mixer + pool dynamics |
| **quantarmyz/system7-poker-arena** | https://github.com/quantarmyz/system7-poker-arena | `decide_system7.py` — exploit HUD node-locking, SPR, 4-grade board texture, treys eval, no LLM at runtime | **P1** — postflop taxonomy + HUD exploit |

### Tier B — partial / scaffold

| Repo | Notes |
|------|--------|
| **MaximKabaev/poker-arena** | L1/L2 router + safe-default; not a finished exploitative bot |
| **devfun-org/poker-arena-starter-kit** | Canonical kit only |
| **zgl95116-sys/HoldemAgentBench** | Agent harness benchmark, not dev.fun prod bot |

### Tier C — official public data (legal, high value)

| Asset | URL | Use |
|-------|-----|-----|
| Reasoned decisions v0 | https://huggingface.co/datasets/dannyobito/arena-poker-reasoned-decisions-v0 | 1000 MS3 reasoning traces; rubric fields `vr,ke,bf,pp,sr` |
| Arena pokerkit hands | https://huggingface.co/datasets/dannyobito/arena-pokerkit-hands | Offline `decide()` replay adapter |
| PR sample packet | PR cites ~41k decisions / ~2.6k hands Hugging Face |

### Named leaderboard rivals — no public code found

Handles from our field exports (`hunterguy102`, `thaddius`, `range_ledger`, `arjun_c`, etc.) — **no matching public `decide()` repos** on GitHub search. Nemesis HUD tuning remains export-driven, not repo theft.

### API key leaks

GitHub code search for live `arena_sk_*` keys: **examples and test placeholders only** — no competitor production keys found in public repos.

### Recommended steals for `cemini_decide.py`

1. **gin `auto_research_v008`** — preflop loose-call layer: position-aware max pot-odds (IP 28%, BB 25%, OOP 20%) for marginal hands (score 38–50); multiway guard ≤3 opponents; stack-commit cap 15%. Addresses over-folding playable defends.
2. **gin `profiled_counter_adaptive`** — per-villain counter lines when HUD N sufficient (parallel to our nemesis + field export HUD).
3. **kecodot `StrategyMixer`** — smooth weight blend across strategies vs hard routing; pool classifier passive/aggressive/mixed.
4. **system7** — board texture grades + SPR commit rules + archetype exploit deviations gated on HUD sample size (N<100 = baseline).
5. **HF reasoned-decisions** — calibrate public `reasoning` YAML quality for Researcher trajectory contribution.

### Phase-0 next steps

- ~~Clone `gin/poker-bot` → diff `survival_sixmax` open ranges vs our seat matrix / gin lane.~~
- ~~Run `auto_research_v008` selfplay vs our gate; port proven patches as regression spots.~~ **Done 2026-06-18** — `gin_style.py` `try_preflop_v008_rescue` (loose-call 38–50 + BB/SB blind defense); `tests/test_gin_v008_preflop.py`; gate PASS with `CEMINI_GIN_V008=1`.
- Do **not** copy repo wholesale — gin repo has **no LICENSE file** [TENTATIVE]; ported algorithm only with source comment in `gin_style.py`.
- Deferred: kecodot `StrategyMixer`, system7 postflop taxonomy, v007 river bluff-catch (action_mix may cover).

## Snippets

- gin v008: "marginal holdings (score 38–50) at pot odds … +EV to call in six-max" [Source: https://github.com/gin/poker-bot (retrieved 2026-06-18)]

## Dead Ends

- No public repos for top Playground chip leaders by handle search.
- `kecodot/poker-agent` last push 2026-05-30 — may be pre-Researcher iteration; still useful architecture reference.
