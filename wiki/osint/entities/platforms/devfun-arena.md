---
title: dev.fun Arena (Poker Agent Challenge)
type: entity
tags: [entity, platform, poker, prediction-markets, devfun]
keywords: [dev.fun, arena.dev.fun, poker arena, six-max, researcher track, Monad]
related:
  - sources/devfun-poker-agent-challenge-onepager-2026-06-18.md
  - sources/devfun-researcher-track-discord-welcome-2026-06-18.md
  - concepts/devfun-poker-agent-challenge-2026.md
  - concepts/poker-arena-multi-axis-cognitive-profile.md
  - concepts/devfun-poker-competitor-github-recon-2026-06.md
  - sources/arxiv-poker-arena-multi-axis-2606-13815-2026-06-18.md
  - sources/brief-k118-poker-agent-research-gaps-2026-06-17.md
maturity: validated
created: 2026-06-18
updated: 2026-06-18
---

## Relations

- @sources/devfun-poker-agent-challenge-onepager-2026-06-18.md
- @concepts/devfun-poker-agent-challenge-2026.md
- @concepts/devfun-poker-competitor-github-recon-2026-06.md
- @concepts/poker-arena-multi-axis-cognitive-profile.md
- @sources/arxiv-poker-arena-multi-axis-2606-13815-2026-06-18.md

## Raw Concept

Operator platform for **AI agent poker benchmarks** on Monad — Playground qual seasons, Tournament KO brackets, and the **Researcher Round** sandbox (6-max benchmark, Jun 2026). Cemini agent: `cemini_wiki_poker` on `https://arena.dev.fun/api/arena`.

## Narrative

**Surfaces:**

| Surface | URL / entry |
|---------|-------------|
| Marketing | https://dev.fun/ |
| Docs | https://docs.dev.fun/ |
| Live arena | https://arena.dev.fun/ |
| API base (prod) | `https://arena.dev.fun/api/arena` |
| Onboarding skill | `https://arena.dev.fun/skills/arena.md` |
| Starter kit | `devfun-org/poker-arena-starter-kit` / `arena-pokerkit` |

**2026 prize narrative:** ~$50K total across playground, tournament, researcher track; one-pager cites **$30K** researcher pool component.

**Researcher Round [CONFIRMED Discord 2026-06-18]:** `#researcher-track` — $30K, 50 seats, Jun 21 beta; trajectory export; how-not-only-win eval.

**Format [TENTATIVE operator 2026-06-18]:** **6-max NLHE** sandbox (not HU-only). One-pager “heads-up” may describe finale/publish lane.

**Match defaults [TENTATIVE]:** **Multi-day** season grind (Playground style) — not Eval 500h; submit via `pokerkit run` lobby loop until skill file confirms length.

**Raeth benchmark (parallel):** https://poker.raeth.ai/ — academic nine-axis eval (2606.13815); separate LB from dev.fun Researcher Round.

**Fixed engine + LLM [CONFIRMED per PR 2026-06-18]:** researcher track fixes engine and base LLM — poker skill layer only (validate at beta against allowed `decide()` surface).

**Cemini posture:** optimize **6-max `cemini_decide.py`** + trajectory/axis exports for Researcher LB; Playground for optional HUD intel.

## Snippets

- PR (2026-06-18): "Researcher track that fixes the engine and underlying LLM, so builders compete on poker skill alone." [Source: https://www.prnewswire.com/news-releases/devfun-launches-poker-arena-the-first-public-benchmark-for-ai-agent-reasoning-302804245.html (retrieved 2026-06-18)]
