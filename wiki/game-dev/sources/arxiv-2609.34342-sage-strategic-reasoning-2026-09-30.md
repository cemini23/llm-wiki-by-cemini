---
title: SAGE — structured strategic reasoning for LLM game agents (2026-09-30)
type: source
tags: [source, arxiv, game-ai, strategy, harness, llm]
keywords: [sage, anchor-adapt-recalibrate, imperfect-information, opponent-modelling, token-efficiency]
related:
  - concepts/game-ai-rl-augmentation-shelf.md
  - concepts/stronghold-2-ai-lords.md
  - concepts/rts-siege-ai-reference.md
  - sources/arxiv-2606.29932-saga-civrealm-strategy-agents-2026-07-05.md
  - sources/inbox-arxiv-reject-batch-2026-09-30.md
read_status: read
source_type: arxiv-paper
source_url: https://arxiv.org/abs/2609.34342
maturity: validated
created: 2026-09-30
updated: 2026-09-30
---

## Raw Concept

**arXiv:2609.34342** — **SAGE** is a training-free, inference-time framework that structures LLM strategic reasoning around three coordinated operations: **anchor**, **adapt**, and **recalibrate**. Anchor fixes reasoning to an equilibrium policy that supplies a strategically valid prior. Adapt conditions deviations from that anchor on a soft belief over opponent behavioural tendencies. This enables opponent-specific exploitation. Recalibrate distills strategically related interactions into counterfactual hypotheses about previously missing considerations, so past experience corrects the reasoning. [CONFIRMED]

The framework targets three failure modes of free-form reasoning: unsupported strategic assumptions, inconsistent opponent estimates, and interference from irrelevant past interactions. [CONFIRMED]

## Narrative

### evaluation [CONFIRMED]

- Tested on three repeated imperfect-information games: Leduc Hold'em, Liar's Dice, and Goofspiel, against varied opponent types.
- Against reasoning-intensive LLM agents (Suspicion-Agent, ReTA, Agent-Pro, EMO, Hypothetical Minds), SAGE reaches up to 127.6% payoff improvement in Liar's Dice.
- It cuts input and output token usage by up to 80% and 90%.
- In direct match-up play it attains non-negative mean payoff against 5/10 Leduc Hold'em, 8/10 Liar's Dice, and 8/10 Goofspiel opponents.
- Code is at https://github.com/chenzhwsysu57/SAGE. Authors: HKUST (Guangzhou), Johns Hopkins, Microsoft, Fudan, USTC.

### castle-sim / lord-AI relevance [CONFIRMED]

- Maps to the Stronghold 2 AI lord director in @concepts/stronghold-2-ai-lords.md and the siege AI shelf in @concepts/rts-siege-ai-reference.md.
- The useful ideas are opponent modelling from observed play, and explicit separation of a valid baseline policy from opponent-specific deviation.
- In a castle sim the analog is a lord director with a sane default build order plus bounded deviation when it reads the player's strategy.
- The token-efficiency result matters: structured reasoning beats verbose free-form reasoning, which helps any agent that must run inside a budget.

### Phase-0 / adoption [CONFIRMED]

- Phase-0 audit 2026-09-30: `github.com/chenzhwsysu57/SAGE` has **no LICENSE file** and no licence badge → **NO-GO clone**. Verdict: **STEAL-FROM** — reuse the anchor / adapt / recalibrate pattern only.
- SAGE is not RL, so it does not conflict with the deferred RL shelf in @concepts/game-ai-rl-augmentation-shelf.md.

## Dead Ends

- Free-form LLM reasoning over opponents without an anchor policy.
- Assuming card-game payoffs transfer to an RTS economy.
