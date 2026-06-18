---
title: dev.fun Poker Agent Challenge 2026 — researcher track
type: concept
tags: [concept, poker, devfun, heads-up, agent-eval, researcher-track]
keywords: [poker agent challenge, researcher track, BenchFlow, heads-up, Tom Dwan, session memory]
related:
  - sources/devfun-poker-agent-challenge-onepager-2026-06-18.md
  - sources/devfun-researcher-track-discord-welcome-2026-06-18.md
  - entities/platforms/devfun-arena.md
  - sources/arxiv-poker-arena-multi-axis-2606-13815-2026-06-18.md
  - concepts/active-project-research-routing.md
maturity: validated
created: 2026-06-18
updated: 2026-06-18
---

## Relations

- @entities/platforms/devfun-arena.md
- @sources/devfun-poker-agent-challenge-onepager-2026-06-18.md
- @sources/devfun-researcher-track-discord-welcome-2026-06-18.md — official channel welcome (Researcher Round)
- @sources/arxiv-poker-arena-multi-axis-2606-13815-2026-06-18.md — multi-axis eval + memory ablation (Raeth)
- @gambling-wiki/concepts/poker-hl-analyst-loop.md — HL loop for live leak patches (shared methodology)

## Raw Concept

Cemini was accepted into the **dev.fun researcher track** (invite-only sandbox, BenchFlow eval). Operator goal: climb Challenge leaderboard, earn researcher pool share + platform credits, and qualify for **Early July** finale seat vs **Tom Dwan / Jungleman** on stream. Top agents become **published challenge bots**.

## Narrative

### Challenge vs current prod

| Dimension | Playground S3 (current prod) | Poker Agent Challenge (target) |
|-----------|------------------------------|--------------------------------|
| Format | 6-max NLHE seasons | **Heads-up** (one-pager) |
| Goal | Top-20 qual → tournament entry | Sandbox LB + **publish as champion bot** |
| Eval | Live lobby + HL analyze | **Sandbox submit** → scored match |
| Timeline | Season-long grind | **Jun 21** beta · **Jun 25** public · **Early Jul** finale |
| Our rank | ~103 / 3450 chips (Jun 18) | Researcher sandbox (separate LB) · **50 seats** invited |

Do **not** assume the same `competition_id` or API surface — confirm sandbox IDs when Researcher Round comp appears in API (expected Jun 21).

**API check 2026-06-18:** `list-active` shows Tournament S2, Playground S3, Eval S1 only — **no Researcher Round competition yet**. Re-run `agents/devfun-poker-arena/scripts/list_arena_competitions.sh` daily until Jun 21.

### Researcher Round — Discord confirmation [CONFIRMED 2026-06-18]

Operator welcome in `#researcher-track` (@sources/devfun-researcher-track-discord-welcome-2026-06-18.md):

- **$30K** pool · **50 seats** (invited only) · **Jun 21** closed beta.
- Explicit eval framing: study **how** agents play, not only win rate — aligns with multi-axis profiling (2606.13815).
- **Full trajectory export** after arena runs — log structured `reasoning` + action sequences for submission/analysis.
- Community input shapes **next eval version** — opportunity to contribute axis metrics / memory ablation narrative.

### Researcher track constraints [NEEDS VERIFICATION 2026-06-18]

Press release states researcher track may **fix engine and underlying LLM** so entrants compete on **poker skill alone**. Implications:

- Strategy may be a **policy plug-in** (chart / rules / small `decide()`) not full stack with OpenRouter routing.
- Our **session memory (K118 F6)** and **multi-axis** tuning still matter if the sandbox exposes opponent history and repeated sessions.
- Validate whether **gin lane**, **MC equity**, and **HUD export** are allowed in sandbox or stripped to fixed inference.

### Academic alignment (arXiv 2606.13815)

Raeth / IIT Roorkee **Poker Arena** paper (same name, workshop) stresses:

- **Three-layer memory:** within-hand, session, cross-session.
- **Nine-axis cognitive profile** beats scalar chip leaderboard for ranking models (Claude Opus won chips but mid-pack on axis score).

Cemini already ships **session showdown memory (F6)** and **HL scalar leak patches** — researcher optimization should add **axis-aware eval** (bet sizing, positional awareness) not only bb/100.

### Optimization pillars (operator order)

1. **Sandbox readiness (P0, by Jun 21)** — register researcher sandbox; document submit command, match length, allowed dependencies; HU regression suite green.
2. **HU policy** — dedicated `decide()` path or table-size branch: gin `try_preflop` / `try_postflop_free` already HU-oriented; extend selfplay gate to **HU 500-hand** BenchFlow mirror.
3. **Memory** — extend F6 to within-hand action sequence + cross-session villain file; align with Raeth ablation lessons.
4. **Eval discipline** — multi-axis proxy metrics in selfplay (open sizing buckets, positional fold rates) before each sandbox submit; **export trajectory JSON** after each run for researcher contribution narrative.
5. **6-max deprioritize** — keep playground lobby for data/HUD only; stop chasing top-20 qual.
6. **Publish narrative** — scan scores (personality/memory) + stable agent handle for "bot to beat" branding.

### Milestones

| When | Deliverable |
|------|-------------|
| **Jun 18–20** | Wiki + brief; HU test matrix; sandbox API recon |
| **Jun 21** | Closed beta — first sandbox submission |
| **Jun 25** | Public launch — iterative submits |
| **Early Jul** | Finale qualification via LB rank |

## Snippets

- One-pager: "BUILD → SUBMIT → SCORE → PUBLISH" [Source: poker-arena-onepager.pdf]
- Discord: "sandbox benchmark for studying how poker agents actually play, not just whether they win" [Source: Discord #researcher-track welcome (retrieved 2026-06-18)]
- "Top agents go live on as champion agents that everyone else can come and challenge."

## Dead Ends

- Optimizing **only** 6-max Playground rank without HU sandbox path does not advance Challenge LB.
- Single scalar HL patches without bet-sizing / position axes may mis-rank vs multi-axis eval (2606.13815).
