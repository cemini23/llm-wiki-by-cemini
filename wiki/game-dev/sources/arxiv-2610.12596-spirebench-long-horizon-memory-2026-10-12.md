---
title: SpireBench — long-horizon strategic play, and why agent-written memory fails (2026-10-12)
type: source
tags: [source, arxiv, harness, benchmark, game-ai, memory]
keywords: [spirebench, slay-the-spire, long-horizon, cross-run-memory, risk-misjudgment, renaming-ablation]
related:
  - concepts/agent-harness-castle-project.md
  - concepts/game-ai-rl-augmentation-shelf.md
  - sources/arxiv-2610.05041-mafia-communication-collective-inference-2026-10-07.md
  - sources/arxiv-2610.11794-memento-3-reflective-rulebooks-2026-10-09.md
  - sources/inbox-arxiv-reject-batch-2026-10-12.md
read_status: read
source_type: arxiv-paper
source_url: https://arxiv.org/abs/2610.12596
maturity: validated
created: 2026-10-12
updated: 2026-10-12
---

## Raw Concept

**arXiv:2610.12596** — **SpireBench**. Authors: Scott C. Lowe (Vector Institute) and Sander W. Keemink (Radboud University). Agentic LLMs now tackle complex tasks, but **strategic reasoning over long horizons is under-studied** [CONFIRMED]. Most agentic benchmarks are **short and episodic**, and performance on long tasks is hard to dissect into stored knowledge, reasoning, and luck [CONFIRMED]. SpireBench has models play the **complete commercial deck-builder Slay the Spire**, where **early decisions decide long-term success** [CONFIRMED].

## Narrative

### Setup [CONFIRMED]

- 20 large language models play at the game's **highest difficulty** (Ascension 20, the Ironclad) [CONFIRMED].
- The authors state their harness is **the first to give a model the complete original game** [CONFIRMED]. They compare it with existing harnesses: MiniStS (one fight), Orak (combat and rewards only, rule bot plays the rest), and AgenticSTS (the sequel) [CONFIRMED].
- A run is scored by the **acts it clears**; **mean acts cleared (0–4) is the headline summary**. The final **floor reached** is also reported [CONFIRMED].
- Harness `CommunicationModPlus` keeps one conversation per floor. Models act only through tool calls and may return a whole turn's actions in one response [CONFIRMED].
- Every cohort plays the same **ten held-out seeds**. Human reference: Mega Crit telemetry (**206,082 A20 Ironclad runs**) and four expert streamers [CONFIRMED].

### Findings [CONFIRMED]

- Frontier models **beat heuristic baselines and match the average human player, but remain far behind experts** [CONFIRMED].
- The gap **widens as the run lengthens**: the strongest models win the first act as often as experts, then fall behind [CONFIRMED].
- What separates strong from weak models is **how well they play each fight**, not the route or the deck [CONFIRMED].
- **All of them misjudge risk over a run — preserving health rather than spending it to grow stronger** [CONFIRMED].
- A **comprehensive, self-consistent renaming of every game term** shows that **part of their performance rests on prior knowledge of the game** [CONFIRMED].
- Models **do not improve from the memories they write across runs**, which are **often wrong and overly cautious** [CONFIRMED].

### Why the memory finding matters most [CONFIRMED]

- This is the **third independent source** in this wiki showing that agent-written persistent notes fail to help and can actively mislead [CONFIRMED].
- The Mafia study (@sources/arxiv-2610.05041-mafia-communication-collective-inference-2026-10-07.md) found societies carrying **sixty generations of their own notes scored below societies with none**.
- Learn2Play found **complete raw records beat summaries** for learning.
- MEMENTO 3 (@sources/arxiv-2610.11794-memento-3-reflective-rulebooks-2026-10-09.md) responds with a **revisable rulebook accepted only on deterministic replay**.
- SpireBench adds the sharpest version: the written memories were **often wrong and overly cautious**, and models **did not improve from them at all** [CONFIRMED]. This directly strengthens rule **H8** in @concepts/agent-harness-castle-project.md.
- Second transfer: the **risk misjudgement** finding — agents preserve resources rather than invest them. This is a concrete failure mode to watch for in an AI lord that hoards instead of expanding.

### Caveat [TENTATIVE]

- Slay the Spire is a single-player, turn-based, perfect-information-ish deck-builder with a fixed card pool [TENTATIVE]. Long-horizon findings there may not transfer to a real-time RTS economy.
- The memory result is architectural rather than game-specific [TENTATIVE].

## Dead Ends

- Trusting an agent's cross-run notes without a replay or anchor check.
- Assuming a benchmark that is short and episodic can predict long-horizon play.
