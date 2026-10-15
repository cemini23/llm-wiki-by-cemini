---
title: "K291 — game-dev wave (2026-10-14)"
type: concept
tags: [wave, k291, ingest, hub]
keywords: [K291, LLM game theory, agent negotiation, visual reasoning benchmark]
related:
  - sources/arxiv-choosing-llms-strategic-agent-interactions-2610.18354-2026-10-14.md
  - sources/arxiv-receiver-decides-agent-negotiations-2610.18424-2026-10-14.md
  - sources/arxiv-game2real-bench-toy-games-transfer-2610.18834-2026-10-14.md
maturity: draft
created: 2026-10-14
updated: 2026-10-14
---

## Relations

- @sources/arxiv-choosing-llms-strategic-agent-interactions-2610.18354-2026-10-14.md — model choice in strategic settings is game-specific
- @sources/arxiv-receiver-decides-agent-negotiations-2610.18424-2026-10-14.md — the holder decides, not the asker
- @sources/arxiv-game2real-bench-toy-games-transfer-2610.18834-2026-10-14.md — toy games correlate 0.935 with real-world visual reasoning

## Raw Concept

The question this page answers: **what did the K291 game-dev inbox contain, and does any of it bear on hobby game dev?**

**Honest answer: these are agent, game-theory, and benchmark papers. None is game-development research.** They were filed in this domain's inbox; they are recorded here for completeness and routed conceptually rather than as engine or tooling findings.

## Narrative

### Choosing LLMs for Strategic Agent Interactions

Extends game-theoretic LLM benchmarks by defining **strategic selection as a meta game layered on the base game**: each round a selector fields one model from a portfolio to play a payoff matrix that is **latent and learned online**.

Three findings worth keeping:
- **The evaluation signal is game-specific.** A model's strategic competence varies significantly with the game setup **and the opponent faced**.
- **Extracting a reliable signal needs far more seed runs** than conventional benchmarking uses.
- **Embedding-based and self-reflection selectors do not consistently capture the strategic signal.** A lightweight **multi-armed bandit** performs more reliably, though still below the best fixed model. Non-stationary and adversarial bandit variants **failed to beat a stationary bandit baseline**.

### Receiver Decides — Agent-to-Agent Negotiations

A round-robin tournament of **1,049 negotiations among fifteen agents**. In each, a REQUESTER raises money from a HOLDER holding a $100 endowment.

| Variance explained | Share |
|---|---|
| Which agent **holds** the money | **47%** |
| Which agent **asks** | **2%** |

Dropping the most extreme agents narrows it to 22% vs 4%. Holders that lose least **refuse the opening request**; turn-1 refusal rate ranks them by total losses (ρ = −0.73). Training moves this in both directions: fine-tuning Qwen3-8B on a persuasion corpus with almost no refusals raised its give-away as a holder from **12% to 84%**; distilling two never-losing holders into a 4B student cut losses from **95% to 1%**.

**The evaluation lesson:** test resource-holding agents **in the holder role**, including after persuasion fine-tuning.

### Game2Real-Bench

Does toy-game performance transfer to real-world visual reasoning? 1,000 independently generated game samples with programmatically verified answers, plus 400 real-world samples, connected by **shared reasoning requirements** rather than visual similarity. Across 25 VLMs, game and real-world performance correlate at **Pearson 0.935 / Spearman 0.935**. One-shot in-context transfer varies by capability: **constraint reasoning improves, fine-grained perception consistently declines**.

### Boundary

No install, no wire.

## Snippets

> "Knowing which agent holds the money explains 47% of the variance in the amount transferred; knowing which agent asks explains 2%." [Source: arxiv-2610.18424 p.1]

> "Evaluations of agents that hold resources should test them in the holder role, including after persuasion fine-tuning." [Source: arxiv-2610.18424 p.1]

> "Performance on game and real-world tasks shows consistent cross-setting trends, with a Pearson correlation of 0.935 and a Spearman correlation of 0.935." [Source: arxiv-2610.18834 p.1]

## Dead Ends

- Reading any of these as game-development guidance. They measure LLM agents in game-shaped settings; they say nothing about engines, assets, or slice workflow.
