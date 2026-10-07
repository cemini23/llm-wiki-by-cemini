---
title: Communication shapes collective inference in self-adapting LLM societies (2026-10-07)
type: source
tags: [source, arxiv, harness, agents, multi-agent, memory]
keywords: [mafia, broadcast-vs-turn-taking, inherited-notes, adaptation, collective-inference]
related:
  - concepts/agent-harness-castle-project.md
  - sources/arxiv-2610.04672-masbench-partial-observability-2026-10-07.md
  - sources/arxiv-2610.08215-learn2play-bench-experience-2026-10-07.md
  - sources/arxiv-2609.40324-cogentic-proof-harness-2026-10-03.md
  - sources/inbox-arxiv-reject-batch-2026-10-07.md
read_status: read
source_type: arxiv-paper
source_url: https://arxiv.org/abs/2610.05041
maturity: validated
created: 2026-10-07
updated: 2026-10-07
---

## Raw Concept

**arXiv:2610.05041** — a study of Mafia, a social-deduction game where an informed minority hides among an uninformed majority whose only evidence is open play. Authors: Haonan Huang (Princeton) and Joey Xiao (NYU). Method: the **zero-information game**, where each day's vote eliminates a random player, is exactly solved and used to score every society. Matched-casting comparisons between communication protocols isolate the effect of communication. Scale: societies of **8–100 claude-haiku-4-5 agents**, **7,416 analysed games**, **1.9M model calls**. Societies adapt by rewriting and inheriting **private strategy notes**. [CONFIRMED]

## Narrative

### Findings [CONFIRMED]

- Simultaneous **broadcast improves adversary identification over silence** in all nine compositions tested (8–46 players).
- **Turn-taking removes most of this advantage.** Its voting landslides are as frequent as broadcast's but land on mafia near chance (**1.08× versus 2.53×**).
- At **70 players**, agents reading eight statements per day identify adversaries **worse than silent** ones, and limited talk is worth less than at 46 players.
- **Adaptation is fast but need not help.** In first broadcast games, citizens announce their role far more often than mafia (**91% vs 30%**) and first-day votes find mafia at three times chance. **Within two generations citizens stop announcing and the cue fades**, a change the inherited notes carry.
- In controlled redeployments at 16 players, **societies carrying sixty generations of their own notes score below societies with none**.

### Why this matters for the agent harness [CONFIRMED]

This is the sharpest counterweight in the wiki to rule **H3** (promote only confirmed results into a durable ledger, from the Cogentic paper). H3 assumes an accumulating verified record helps. This study shows an **inherited notes corpus can actively harm** a society's collective inference: sixty generations of self-written notes scored below no notes at all. The adaptation can also destroy the very signal it relies on. The practical rule for castle-sim is to keep the durable ledger **verified and small**, re-validate inherited notes instead of trusting them, and treat "we have always done it this way" notes as a risk, not an asset. See @sources/arxiv-2609.40324-cogentic-proof-harness-2026-10-03.md and @sources/arxiv-2610.08215-learn2play-bench-experience-2026-10-07.md (which finds complete raw records beat summaries).

### Caveat [TENTATIVE]

The agents are one small model family in a social-deduction game. Society-level note inheritance is not the same as a coding-agent ledger. Treat the result as a caution to test, not as a proven effect on Godot swarms. [TENTATIVE]

## Dead Ends

- Trusting an inherited notes corpus without re-validation.
- Assuming more agent communication is always better.
- Copying a turn-taking discussion protocol for a castle-sim swarm without a matched-baseline test.
