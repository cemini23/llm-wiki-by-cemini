---
title: dev.fun Arena (Poker Agent Challenge)
type: entity
tags: [entity, platform, poker, prediction-markets, devfun]
keywords: [dev.fun, arena.dev.fun, poker arena, six-max, researcher track, Monad]
related:
  - sources/devfun-poker-agent-challenge-onepager-2026-06-18.md
  - sources/devfun-poker-researcher-track-email-2026-06-19.md
  - sources/devfun-researcher-track-discord-welcome-2026-06-18.md
  - sources/devfun-researcher-sandbox-bundle-discord-2026-06-20.md
  - sources/devfun-researcher-track-hu-format-2026-06-08.md
  - concepts/devfun-poker-agent-challenge-2026.md
  - concepts/devfun-researcher-track-readiness-2026-06.md
  - concepts/devfun-researcher-pre-submit-recon.md
  - concepts/poker-arena-multi-axis-cognitive-profile.md
  - concepts/devfun-poker-competitor-github-recon-2026-06.md
  - sources/arxiv-poker-arena-multi-axis-2606-13815-2026-06-18.md
  - sources/brief-k118-poker-agent-research-gaps-2026-06-17.md
  - entities/platforms/devfun-heads-up-pvp-s3.md
  - entities/tools/pokerkit.md
  - sources/eval-poker-github-repos-2026-06-26.md
maturity: validated
created: 2026-06-18
updated: 2026-06-26
---

## Relations

- @sources/devfun-poker-agent-challenge-onepager-2026-06-18.md
- @concepts/devfun-poker-agent-challenge-2026.md
- @concepts/devfun-poker-competitor-github-recon-2026-06.md
- @concepts/poker-arena-multi-axis-cognitive-profile.md
- @sources/arxiv-poker-arena-multi-axis-2606-13815-2026-06-18.md

## Raw Concept

Operator platform for **AI agent poker benchmarks** on Monad — Playground qual seasons, Tournament KO brackets, and the **Researcher track** (**HU** sandbox, Jun 2026). Cemini agent: `cemini_wiki_poker` on `https://arena.dev.fun/api/arena`.

## Narrative

**Surfaces:**

| Surface | URL / entry |
|---------|-------------|
| Marketing | https://dev.fun/ |
| Docs | https://docs.dev.fun/ |
| Live arena | https://arena.dev.fun/ |
| API base (prod) | `https://arena.dev.fun/api/arena` |
| Onboarding skill | `https://arena.dev.fun/skills/arena.md` |
| Heads-up ladder skill | `https://arena.dev.fun/skills/headsup-ladder.md` — static-agent submit + poll (no live `/texas/*`) |
| Starter kit | `devfun-org/poker-arena-starter-kit` / `arena-pokerkit` |
| Researcher (email) | Self-play SDK + **Kaggle** competition page [URL in operator email — pin at signup] |

**2026 prize narrative:** ~$50K total across playground, tournament, researcher track; one-pager cites **$30K** researcher pool component.

**Researcher track [CONFIRMED email 2026-06-19]:** **Heads-up** sandbox ranked by **TrueSkill**; top agent becomes **field benchmark**; Dwan + Jungleman select **style-matched** bots for representation. Tooling: self-play SDK, Kaggle, sponsored sandbox credits. Timeline: **Jun 21** beta · **Jun 25** public.

**Researcher Round Discord [CONFIRMED 2026-06-18]:** trajectory export; how-not-only-win eval — complements TrueSkill LB with research/axis narrative.

**Match defaults [TENTATIVE]:** multi-day or SDK-driven sandbox length — confirm Kaggle rules + `skillFile` at beta.

**Raeth benchmark (parallel):** https://poker.raeth.ai/ — academic nine-axis eval (2606.13815); useful for axis discipline; **LB sort may be TrueSkill on dev.fun sandbox**.

**Fixed engine + LLM [CONFIRMED PR; email broadens submit types]:** PR says fixed engine for strategy layer; email allows weights / LLM+w/key — **verify Kaggle interface** vs our pure `decide()` agent.

**Cemini posture:** **Researcher PRIMARY** — HU `cemini_decide.py`, TrueSkill-oriented HU selfplay, trajectory/axis gates before submit; Playground = background intel only.

## Snippets

- PR (2026-06-18): "Researcher track that fixes the engine and underlying LLM, so builders compete on poker skill alone." [Source: https://www.prnewswire.com/news-releases/devfun-launches-poker-arena-the-first-public-benchmark-for-ai-agent-reasoning-302804245.html (retrieved 2026-06-18)]
