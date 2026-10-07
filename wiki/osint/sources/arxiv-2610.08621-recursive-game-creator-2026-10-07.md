---
title: "Recursive Game Creator: an agentic product-level game harness (arXiv 2610.08621)"
type: source
tags: [source, k284, arxiv, game-dev, agents, harness, godot]
keywords: [recursive-game-creator, gamecraft-bench, godot, agent-harness, coding-native-player, reviewer]
related:
  - concepts/k284-arxiv-wave.md
  - concepts/agent-native-research-artifacts.md
maturity: draft
created: 2026-10-07
updated: 2026-10-07
read_status: read
---

## Relations

- @concepts/k284-arxiv-wave.md
- @concepts/agent-native-research-artifacts.md

## Raw Concept

| Title | Recursive Game Creator: An Agentic Product-Level Experience-Oriented Game Harness |
| Authors | Jiajun Chen, Haoyu Wu, Mingda Jia, Xihui Liu (HKU MMLab; Shenzhen Loop Area Institute) |
| Type | arXiv preprint (cs.AI) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2610.08621-recursive-game-creator-an-agentic-product-level.pdf` |
| Retrieved | 2026-10-07 |
| arXiv | 2610.08621v1 |
| read_status | read |

## Narrative

An **experience-oriented recursive harness** that refines a generated game from a runnable prototype into an *entertaining, product-level* game. Four LLM agent roles in a closed loop:

1. **Designer** — `Pt = Design(U, Gt, Ht−1) = (ht, Δt, At, Xt)`.
2. **Builder** — draft `Zt`, generate `X*t`, integrate `Ct`.
3. **Coding-Native Player** — writes **executable policies** `πt,k` and rolls out `τt,k = Rollout(Ct, πt,k)`. This is the key trick: the play-test runs **in code**, not through slow GUI/screenshot rollouts.
4. **Experience-Oriented Reviewer** — trajectory metrics + game-specific rubrics + visual evidence, with A/B version retention.

### Results

- **GameCraft-Bench: 72.70 → 77.89** over 3 rounds (+6.63 over a same-model baseline; Action category +9.66).
- **GameASG-Bench strict task success 25/47 (53.2%)**, +34.1% over baseline; mean runtime-check (L2) pass rate **93.4%**.
- User study: longer playtime, higher ratings.

### Why it matters here

The reusable idea is the **coding-native player** — replace expensive visual rollouts with an agent that writes a policy and executes it. That is a general harness pattern, not just for games. Relevant to the Game-dev wiki and to the CCC harness lane. **"Code is coming soon"; no repo URL.**

## Snippets

> "Coding-Native Player writes executable policies and rolls out ... avoids slow GUI/screenshot rollouts." [Source: arxiv-2610.08621-recursive-game-creator-an-agentic-product-level.pdf]

> "GameCraft-Bench overall 72.70→77.89 across 3 rounds; Action category +9.66." [Source: arxiv-2610.08621-recursive-game-creator-an-agentic-product-level.pdf]
