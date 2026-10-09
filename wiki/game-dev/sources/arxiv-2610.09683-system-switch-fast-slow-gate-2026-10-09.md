---
title: System Switch — when should a fast decision model stop and think? (2026-10-09)
type: source
tags: [source, arxiv, agents, harness, game-ai, architecture]
keywords: [dual-process, fast-slow-gate, auROC, calibration, deferral, doom]
related:
  - concepts/agent-harness-castle-project.md
  - concepts/game-ai-rl-augmentation-shelf.md
  - sources/arxiv-2610.03695-queen-chess-explains-moves-2026-10-05.md
  - sources/inbox-arxiv-reject-batch-2026-10-09.md
read_status: read
source_type: arxiv-paper
source_url: https://arxiv.org/abs/2610.09683
maturity: validated
created: 2026-10-09
updated: 2026-10-09
---

## Raw Concept

**arXiv:2610.09683** — **System Switch**, by Gianluca Bailo (independent researcher). [CONFIRMED]
The problem: **dual-process agents** pair a fast policy with a slow deliberative model. [CONFIRMED]
In real-time settings the slow model usually runs **continuously**. [CONFIRMED]
In turn-based agents and robot planners it is invoked **on events**, such as uncertainty or a detected failure. [CONFIRMED]
This study uses a **fast learned actor that takes every decision and hands control to a reasoning vision-language model only when a gate opens, while the game keeps running in real time**. [CONFIRMED]
Testbed: closed-loop **Doom**, using the open "System One" **typed-decision models** (0.15B to 9B parameters) served through a common **llama.cpp** interface. [CONFIRMED]

## Narrative

### Findings [CONFIRMED]

- (i) On 900 held-out questions, zero-shot decision models **over-choose collecting items**, 1.6–1.8 times more often than chance among their errors, whatever the option order — and option order does change some models' accuracy. [CONFIRMED]
- (ii) **Accuracy, calibration, and sensitivity are distinct**: models of similar accuracy differ widely in **AUROC**, and the most sensitive model's confidence tracks **which kinds of situation it fails**, not which of its answers are wrong. [CONFIRMED]
- (iii) Offline, **deferring the least-confident 30%** of decisions to a reasoning model gains over deferring at random **in proportion to the actor's AUROC** (rank correlation **0.87** over 18 actor/option-order pairs); with the actor and rate chosen on held-out games the gain is **+0.13 [0.08, 0.18]** with one option order and **+0.08 [0.02, 0.14]** with shuffled options, and reasoning carries about half of it. [CONFIRMED]
- (iv) In closed loop (33 games on three seeds), **no variant reaches the exit**. [CONFIRMED]
  Committing to plans, the reasoner's or a fixed explore rule's behind the same gate, covers more of the map, opens more doors and even makes an actor that stands still on its own play; with the rule, the agent dies more often. [CONFIRMED]
  The thoughts show where the chain breaks: told that some doors need keys, the reasoner takes ordinary doors for locked ones, which the state cannot tell apart, and without that knowledge it goes back to collecting. [CONFIRMED]

### Why this matters for the harness [CONFIRMED]

Two transfers. First, **the gate is the cost-control mechanism**. [CONFIRMED]
The castle-sim harness already splits a cheap executor swarm from an expensive planner/verifier. [CONFIRMED]
This paper gives the criterion for when to escalate — **defer on the least-confident fraction, and choose that fraction using AUROC (sensitivity), not accuracy**. [CONFIRMED]
Second, **accuracy is the wrong metric to select on**: two models can score alike and behave very differently when you need to know *when* they are wrong. [CONFIRMED]
Cross-link @concepts/game-ai-rl-augmentation-shelf.md and @sources/arxiv-2610.03695-queen-chess-explains-moves-2026-10-05.md (another fast-expert / slow-model split, there an expert encoder with a language-model explainer). [CONFIRMED]
Note contrast: H6 in @concepts/agent-harness-castle-project.md is expert-decides-and-LM-explains; here the fast actor decides and the slow model is *escalated to*. [CONFIRMED]

### Caveat [TENTATIVE]

The study is Doom, a single real-time game with a specific model family. [TENTATIVE]
The numbers are offline deferral gains plus one closed-loop setting. [TENTATIVE]
The gate criterion is the transferable part; the specific rates are not. [TENTATIVE]

## Dead Ends

- Running the slow deliberative model continuously in a real-time loop. [CONFIRMED]
- Picking a model by accuracy when the decision is whether to escalate. [CONFIRMED]
- Giving a reasoner game knowledge the state cannot contradict (the locked-door belief). [TENTATIVE]
