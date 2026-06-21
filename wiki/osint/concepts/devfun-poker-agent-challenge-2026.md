---
title: dev.fun Poker Agent Challenge 2026 — researcher track
type: concept
tags: [concept, poker, devfun, heads-up, agent-eval, researcher-track, trueskill]
keywords: [poker agent challenge, researcher track, TrueSkill, heads-up, Tom Dwan, trajectory, Kaggle]
related:
  - concepts/devfun-researcher-pro-style-targets-2026-06.md
  - concepts/devfun-researcher-track-readiness-2026-06.md
  - concepts/devfun-researcher-pre-submit-recon.md
  - concepts/devfun-poker-competitor-github-recon-2026-06.md
  - concepts/generator-verifier-inference-time-steering.md
  - concepts/poker-arena-multi-axis-cognitive-profile.md
  - sources/arxiv-veritas-visual-verification-2606.18247-2026-06-18.md
  - sources/arxiv-probabilistic-agent-verification-2606.20510-2026-06-21.md
  - sources/arxiv-rng-bench-non-markov-mllm-2606.19338-2026-06-21.md
  - concepts/probabilistic-agent-policy-verification.md
  - concepts/non-markov-belief-state-benchmarks.md
  - sources/devfun-poker-agent-challenge-onepager-2026-06-18.md
  - sources/devfun-poker-researcher-track-email-2026-06-19.md
  - sources/devfun-researcher-track-discord-welcome-2026-06-18.md
  - sources/devfun-researcher-sandbox-bundle-discord-2026-06-20.md
  - entities/platforms/devfun-arena.md
  - sources/arxiv-poker-arena-multi-axis-2606-13815-2026-06-18.md
  - concepts/active-project-research-routing.md
  - sources/brief-k118-poker-agent-research-gaps-2026-06-17.md
maturity: validated
created: 2026-06-18
updated: 2026-06-21
---

## Relations

- @entities/platforms/devfun-arena.md
- @sources/devfun-poker-agent-challenge-onepager-2026-06-18.md
- @sources/devfun-researcher-track-discord-welcome-2026-06-18.md — official channel welcome (Researcher Round)
- @concepts/generator-verifier-inference-time-steering.md — VERITAS inference-time verifier steal (K123)
- @concepts/probabilistic-agent-policy-verification.md — trajectory risk bounds (K125)
- @concepts/non-markov-belief-state-benchmarks.md — Memory Gap ablation rubric (K125)
- @sources/arxiv-veritas-visual-verification-2606.18247-2026-06-18.md
- @sources/arxiv-poker-arena-multi-axis-2606-13815-2026-06-18.md — Raeth paper source
- @concepts/devfun-poker-competitor-github-recon-2026-06.md
- @gambling-wiki/concepts/poker-hl-analyst-loop.md — HL loop for live leak patches (shared methodology)

## Raw Concept

Cemini was accepted into the **dev.fun researcher track** (invite-only sandbox, BenchFlow eval). Operator goal: climb Researcher Round leaderboard, earn pool share + platform credits, and qualify for **Early July** finale vs **Tom Dwan / Jungleman** on stream. Top agents become **published challenge bots**.

## Narrative

### Challenge vs current prod

| Dimension | Playground S3 (background intel) | Researcher track (target) |
|-----------|----------------------------------|---------------------------|
| Format | 6-max NLHE PVP lobby | **Heads-up** sandbox [CONFIRMED email 2026-06-19] |
| Goal | Optional HUD intel | **TrueSkill** LB; top agent = **benchmark bot** |
| Eval | Slow lobby sample | **TrueSkill** + trajectory export; Kaggle + self-play SDK |
| Pro hook | — | Dwan + Jungleman pick **style-matched** bots |
| Timeline | Season-long | **Jun 21** beta · **Jun 25** public · **Early Jul** finale |
| Our rank | ~103 / 3450 chips (Jun 18) | Separate LB · invite cohort |

Do **not** assume the same `competition_id` as Playground — pin Researcher ID when API / Kaggle lists it (expected Jun 21).

### Format — HU [CONFIRMED]

- **devlord email (2026-06-19):** HU sandbox, TrueSkill ranking — `@sources/devfun-poker-researcher-track-email-2026-06-19.md`
- **Operator relay (2026-06-08):** `@sources/devfun-researcher-track-hu-format-2026-06-08.md`
- **Implication:** HU chart + 2-player gates; 6-max Playground logic is intel-only, not the submit target.

### Scoring — TrueSkill vs trajectory

| Source | Says |
|--------|------|
| Email (devlord) | Sandbox ranked by **TrueSkill**; champion = benchmark bot |
| Discord welcome | Trajectory export; how agents play (research contribution) |
| Raeth 2606.13815 | Nine-axis cognitive profile — discipline for exports, not necessarily dev.fun LB sort |

Optimize for **HU win rate / TrueSkill** in sandbox opponent mix; keep trajectory + M₁–M₉ gates as **submit hygiene** and style-rep insurance.

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
4. **Verifier steering (K123)** — gradient-free verifier stack + optional Best-of-N before submit (`CEMINI_VERIFIER_BON`).
5. **Trajectory discipline** — `export_researcher_trajectory.sh` after every benchmark run; post axis proxies in channel.
6. **Playground** — optional HUD/field intel; not the Researcher LB.
7. **Publish narrative** — structured policy + regression gates + trajectory contribution.

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
