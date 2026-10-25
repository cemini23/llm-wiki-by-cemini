---
title: "Poker GitHub Repository Evaluation.docx — 30-repo eval (2026-06-26)"
type: source
tags: [tool-evaluation, poker, github-audit, license-compliance, k130]
keywords: [poker-eval, rlcard, pokerkit, PokerHandEvaluator, PokerRL, GPL-poison, devfun-arena]
related:
  - concepts/wiki-tooling-evaluation.md
  - concepts/cemini-license-posture.md
  - concepts/devfun-poker-agent-challenge-2026.md
  - concepts/poker-arena-multi-axis-cognitive-profile.md
  - entities/tools/rlcard.md
  - entities/tools/pokerkit.md
  - entities/platforms/devfun-arena.md
  - sources/eval-url-cemini-research-2026-06-25.md
  - entities/tools/ai-pokergame.md
  - sources/eval-github-repo-plan-dfs-marl-poker-osint-2026-07-01.md
maturity: draft
read_status: read
created: 2026-06-26
updated: 2026-10-25
clusters: [poker, eval, agent-harness]
---

## Relations

- @concepts/wiki-tooling-evaluation.md — Phase-0 registry
- @concepts/cemini-license-posture.md — docx license claims overridden by `gh api`
- @entities/tools/pokerkit.md — Adopt (already deployed in Arena starter kit)
- @entities/tools/rlcard.md — Adopt (MIT; gambling-wiki primary)
- @entities/platforms/devfun-arena.md — production dependency on PokerKit

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Poker GitHub Repository Evaluation |
| **Author** | Gemini Deep Research (30 GitHub URLs) |
| **Type** | DOCX (`Poker GitHub Repository Evaluation.docx`) |
| **sha256** | `fec5f94c4629de1995c156b2bb0bccde1d925f790b95a39f31a70173a0e574ba` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/Poker GitHub Repository Evaluation.docx` |
| **Retrieved** | 2026-06-26 (inbox) |
| **Read status** | read (tier aggregation + Adopt license spot-check) |

## Narrative

K130 poker-repo eval batch for **dev.fun Researcher Round** tooling stack. Maps RL environments, hand evaluators, and legacy GPL bots against co-primary **poker-arena** + **gambling-wiki** surfaces.

### Recommendation distribution

| Tier | Count | Notes |
|------|-------|-------|
| **Adopt** | 2 | **pokerkit** (MIT, already in Arena); **rlcard** (MIT, offline baseline env) |
| **Steal-from** | 4 | PokerHandEvaluator, pokersolver, PokerGPT, DouZero |
| **Reference-only** | 8 | PyPokerEngine, pokerregion/poker, PokerRL, scrumonline, slack-poker-bot, Hatjitsu, poinz, planning-poker |
| **Reject** | 15 | GPL/AGPL poison (dickreuter/*, pokerth), NO LICENSE (fedden/poker_ai, deuces, chenosaurus/poker-evaluator, …) |
| **UNAVAILABLE** | 1 | gin/poker-bot/tree/v2 |

### Adopt — license spot-check (`gh api`, 2026-06-26)

| Repo | Docx tier | License | Posture |
|------|-----------|---------|---------|
| uoftcprg/pokerkit | Adopt | **MIT** | **CONFIRMED** — canonical Arena engine (`agents/devfun-poker-arena` pyproject) |
| datamllab/rlcard | Adopt | **MIT** | Offline HU baseline / chart ablation env (gambling-wiki primary) |

### Steal-from (no entity stubs)

| Repo | License | Steal |
|------|---------|-------|
| HenryRLee/PokerHandEvaluator | Apache-2.0 | Fast C++/Python hand ranking vs treys hot path |
| goldfire/pokersolver | MIT | JS hand solver patterns (Arena uses treys — reference only) |
| HarperJonesGPT/PokerGPT | MIT | LLM decision scaffolding reference |
| kwai/DouZero | Apache-2.0 | Imperfect-info self-play patterns (Dou Dizhu — not NLHE) |

### Rejects aggregated (no per-URL stubs)

**GPL/AGPL:** dickreuter/Poker, dickreuter/neuron_poker (GPL-3.0), pokerth/pokerth (AGPL-3.0).

**NO LICENSE:** fedden/poker_ai, worldveil/deuces, chenosaurus/poker-evaluator, jacobhyphenated/PokerServer, geobalas/Poker (eval Reject — stale/abandoned), WangAnXin/poker, Jeremiah9000/Poker-with-Python, Tairraos/Poker.JS, zifeiy/poker-game-demo, christophschmalhofer/poker, tianlanlandelan/poker, alexyz/poker.

## Snippets

> "This repository is undeniably the most robust, fully featured analytical poker framework in the set." [Source: Poker GitHub Repository Evaluation.docx URL 24 uoftcprg/pokerkit (retrieved 2026-06-26)]

> "RLCard represents the premier Python toolkit for wrapping discrete card games into modular RL paradigms." [Source: Poker GitHub Repository Evaluation.docx URL 20 datamllab/rlcard (retrieved 2026-06-26)]

## Dead Ends

- Docx over-routes scrumonline/planning-poker as poker repos — **false positive**; Reference-only at best, not Arena stack.
- gin/poker-bot v2 tree URL **UNAVAILABLE** — do not Adopt from cached eval text.
