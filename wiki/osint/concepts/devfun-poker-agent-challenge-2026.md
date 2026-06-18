---
title: dev.fun Poker Agent Challenge 2026 — researcher track
type: concept
tags: [concept, poker, devfun, six-max, agent-eval, researcher-track]
keywords: [poker agent challenge, researcher track, BenchFlow, 6-max, Tom Dwan, session memory, trajectory]
related:
  - concepts/devfun-poker-competitor-github-recon-2026-06.md
  - concepts/poker-arena-multi-axis-cognitive-profile.md
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
- @concepts/poker-arena-multi-axis-cognitive-profile.md — nine-axis profile + memory ablation (K122 deep-read)
- @sources/arxiv-poker-arena-multi-axis-2606-13815-2026-06-18.md — Raeth paper source
- @concepts/devfun-poker-competitor-github-recon-2026-06.md
- @gambling-wiki/concepts/poker-hl-analyst-loop.md — HL loop for live leak patches (shared methodology)

## Raw Concept

Cemini was accepted into the **dev.fun researcher track** (invite-only sandbox, BenchFlow eval). Operator goal: climb Researcher Round leaderboard, earn pool share + platform credits, and qualify for **Early July** finale vs **Tom Dwan / Jungleman** on stream. Top agents become **published challenge bots**.

## Narrative

### Challenge vs current prod

| Dimension | Playground S3 (current prod) | Researcher Round (target) |
|-----------|------------------------------|---------------------------|
| Format | 6-max NLHE PVP lobby | **6-max NLHE** sandbox benchmark [TENTATIVE — operator; one-pager text says HU for publish/finale framing] |
| Goal | Season chip grind / qual | Sandbox LB + trajectory contribution + **publish as champion bot** |
| Eval | Live lobby + HL analyze | **Sandbox submit** → scored benchmark match |
| Match length | Continuous multi-day grind | Same — **not** 500-hand Eval; details TBD [operator 2026-06-18] |
| Submit cadence | Lobby poll loop | Same client loop as Playground until skill file says otherwise |
| Timeline | Season-long | **Jun 21** beta · **Jun 25** public · **Early Jul** finale |
| Our rank | ~103 / 3450 chips (Jun 18) | Separate LB · **50 seats** invited |

Do **not** assume the same `competition_id` as Playground or Eval S1 — pin Researcher Round ID when it appears in API (expected Jun 21).

**API check 2026-06-18:** `list-active` shows Tournament S2, Playground S3, Eval S1 only — **no Researcher Round competition yet**. Re-run `agents/devfun-poker-arena/scripts/list_arena_competitions.sh` daily.

### Format note — 6-max vs one-pager HU

- **One-pager PDF** markets "heads-up" for the public Challenge / finale narrative [Source: poker-arena-onepager.pdf].
- **Operator assumption (2026-06-18):** Researcher Round **plays 6-max** like existing Arena poker — same engine family as Playground / Eval, not a separate HU-only sandbox.
- **Discord welcome** did not specify table size; deferred to one-pager link.
- **Implication:** optimize **`cemini_decide.py` 6-max path** (gin lane, seat matrix, HL regression) — not a HU-only policy fork. HU regression spots remain cheap smoke tests only.

### Researcher Round — Discord [CONFIRMED 2026-06-18]

See @sources/devfun-researcher-track-discord-welcome-2026-06-18.md:

- **$30K** · **50 seats** · **Jun 21** closed beta.
- Eval thesis: **how** agents play, not only win rate — multi-axis profiling (2606.13815).
- **Full trajectory export** after runs.
- Shapes **next eval version**.

### Researcher track constraints [CONFIRMED per PR 2026-06-18]

[PR Newswire launch](https://www.prnewswire.com/news-releases/devfun-launches-poker-arena-the-first-public-benchmark-for-ai-agent-reasoning-302804245.html): Researcher track **fixes engine and underlying LLM** — compete on **poker skill layer**. Operator accepts PR wording until sandbox skill contradicts.

- Strategy = policy plug-in (`decide()`, charts, memory) not OpenRouter-at-runtime.
- Confirm at beta whether **gin lane**, **MC equity**, and **HUD** remain in allowed surface.

### Academic alignment (arXiv 2606.13815)

See @concepts/poker-arena-multi-axis-cognitive-profile.md — three-layer memory + **nine-axis** profile (M₁ bet sizing … M₉ positional awareness). Raeth result: Claude **#1 chips, #5 mean axis**; memory ablation model-specific (GPT +, Kimi −).

Cemini ships **F6 session memory** + HL leak patches — add **axis-aware eval** (`axis_summary.json`) and trajectory exports before each submit. Brief: `agents/devfun-poker-arena/briefs/2026-06-18_k122-multi-axis-eval-mappings.md`.

### Optimization pillars (operator order)

1. **Sandbox readiness (P0, Jun 21)** — pin `competitionId`; smoke `pokerkit run --max-hands 50`; plan for **multi-day** season stamina (not 500h eval); full **6-max regression** green.
2. **6-max policy** — continue HL loop on Playground intel + regression gates; no HU-only fork unless skill file mandates HU.
3. **Memory** — extend F6; align with Raeth ablation lessons.
4. **Trajectory discipline** — `export_researcher_trajectory.sh` after every benchmark run; post axis proxies in channel.
5. **Playground** — optional HUD/field intel; not the Researcher LB.
6. **Publish narrative** — structured policy + regression gates + trajectory contribution.

### Milestones

| When | Deliverable |
|------|-------------|
| **Jun 18–20** | Wiki posture; 6-max gate; API recon |
| **Jun 21** | Closed beta — first sandbox submit (duration TBD; plan for **multi-day** season not 500h eval) |
| **Jun 25** | Public — iterative `pokerkit run` submits |
| **Early Jul** | Finale qual via LB (table format TBD — may differ from sandbox) |

## Snippets

- One-pager: "BUILD → SUBMIT → SCORE → PUBLISH" [Source: poker-arena-onepager.pdf]
- Discord: trajectory + "how agents play" [Source: Discord #researcher-track welcome (retrieved 2026-06-18)]
- PR: researcher track fixes engine + LLM [Source: PR Newswire 2026-06-18]

## Dead Ends

- **HU-only optimization** for Researcher Round if sandbox is 6-max — misallocates effort away from prod-shaped regression.
- Scalar HL patches without bet-sizing / position axes may mis-rank vs multi-axis eval (2606.13815).
