---
title: SpeedrunBench — LLM agents must beat their own best strategy (2026-10-07)
type: source
tags: [source, arxiv, harness, agents, benchmark, game-ai]
keywords: [speedrunbench, speedrunning, strategy-formation, self-improvement, long-horizon]
related:
  - concepts/agent-harness-castle-project.md
  - sources/arxiv-2610.08215-learn2play-bench-experience-2026-10-07.md
  - concepts/game-ai-rl-augmentation-shelf.md
  - sources/arxiv-2609.40324-cogentic-proof-harness-2026-10-03.md
  - sources/inbox-arxiv-reject-batch-2026-10-07.md
read_status: read
source_type: arxiv-paper
source_url: https://arxiv.org/abs/2610.08076
maturity: validated
created: 2026-10-07
updated: 2026-10-07
---

## Raw Concept

**arXiv:2610.08076** — **SpeedrunBench**, from Patronus AI, University of Washington, and Institute of Science Tokyo. It evaluates frontier LLM agents across **9 games** on video-game **speedrunning** — finding the fastest way to complete a game under set conditions. Speedrunning surfaces unorthodox play that needs deep mastery of game mechanics. The framing question: can LLM agents go **beyond what humans have already solved**, instead of reproducing known solutions? To do well, an agent must repeatedly improve its strategy, reflect on performance, exploit gained knowledge, and reason over a long horizon to beat **itself and everyone else**.

## Narrative

### What it measures [CONFIRMED]

- 9 games across 6 genres: Super Mario Bros (NES), Super Mario Land (Game Boy), SuperTux (browser) — platformers; Pokémon Blue/Red (Game Boy), Tuxemon (browser) — RPGs; Mario Kart 64 (N64), SuperTuxKart (browser) — racing; Civilization I (strategy); Astray (browser puzzle).
- Three settings: ONLINE (agent picks the next action from frames), OFFLINE-SCRATCH (build a valid frame-indexed trace with no seed), OFFLINE-SEED (improve a seeded trace). Offline runs give 200 turns by default.
- Scoring: frames to reach the goal, compared with human world records (real-time attack).
- No agent reaches a world record under a practical budget; the best mean is more than 2× slower. Models span 316%–432% of the record. Only three vision models reach Pokémon's first badge ONLINE: Opus 5 is about 4× slower than the record, Grok 4.6 nearly 12×.
- OFFLINE-SCRATCH separates route-builders from refiners: 5 of 6 models clear SuperTux 3.8–4.9× faster from scratch than from the seed. With an in-turn scorer (up to 200 evaluations), DeepSeek-V4-Pro hits 1,847 frames on SuperTux, within 7% of the record.
- The paper claims strategy formation — not task completion — is the interesting capability. Completion metrics score many of these runs identically; speed still separates them.

### castle-sim / agent-harness relevance [CONFIRMED]

- SpeedrunBench scores **self-improvement over repeated attempts**, not one-shot success. That matches the castle-sim W2 harness milestone loop (rule **H3** in @concepts/agent-harness-castle-project.md, the verified ledger later rounds build on). "Beat your own record" is the cleanest form of that loop.
- The games are a game-AI reference in the same family as @concepts/game-ai-rl-augmentation-shelf.md. But speedrunning rewards exploit-finding, not believable opponent behaviour. The wiki's lord-AI target is authenticity, not optimality — the objective differs on purpose.

### Caveat [TENTATIVE]

- Speedrunning rewards degenerate exploits and frame-perfect execution. That is close to the opposite of the Stronghold-style readable AI this project wants. The transferable part is the *measurement shape*, not the objective.

## Dead Ends

- Optimizing a castle-sim AI for speed instead of believability.
- Treating a speedrun exploit as a design insight.
