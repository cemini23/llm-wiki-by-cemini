---
title: ReqClarifyBench — interactive requirement clarification before coding (2026-10-12)
type: source
tags: [source, arxiv, harness, agents, benchmark, requirements]
keywords: [reqclarifybench, clarification, vague-intent, repository-level, rework, specification]
related:
  - concepts/agent-harness-castle-project.md
  - concepts/ai-assisted-game-dev-workflows.md
  - concepts/vertical-slice-v0.md
  - sources/arxiv-2610.08215-learn2play-bench-experience-2026-10-07.md
  - sources/inbox-arxiv-reject-batch-2026-10-12.md
read_status: read
source_type: arxiv-paper
source_url: https://arxiv.org/abs/2610.13022
maturity: validated
created: 2026-10-12
updated: 2026-10-12
---

## Raw Concept

**arXiv:2610.13022** — **ReqClarifyBench**. Authors: Mingyu Chen, Zhiqing Zhong, Manyi Wang, Linxi Liang, Rouyu Chen, Pinjia He (The Chinese University of Hong Kong, Shenzhen) [CONFIRMED]. Software development moves toward users describing what they want and LLMs implementing it [CONFIRMED]. The bottleneck becomes **whether the LLM truly understands what the user wants** [CONFIRMED]. Users begin with **vague intent**; requirements are **progressively clarified through interaction** [CONFIRMED]. In **repository-level** development, an incorrect guess about intent **propagates through later phases and causes costly rework** in long-horizon tasks [CONFIRMED].

## Narrative

### The gap they target [CONFIRMED]

Existing repository-level code-generation benchmarks evaluate generation directly from **either complete specifications or underspecified requests** [CONFIRMED]. They skip the **pre-coding requirement clarification** step [CONFIRMED]. Prior clarification studies mainly target **function-level** tasks and missed real-world complexity [CONFIRMED]. So it was unclear how well LLMs turn vague intent into clear requirements through interaction, and how that capability affects downstream code generation [CONFIRMED].

### ReqClarifyBench [CONFIRMED]

An interactive requirement clarification benchmark for repository-level development, with **341 tasks** across **game, miniapp, and web** (140 from GameCraft-Bench, 100 from MiniAppBench, 101 from WebGen-Bench) [CONFIRMED]. Each task has a **high-level vague user intent** and a **detailed requirement document** (avg 193 atomic requirements, 2,380 tokens) [CONFIRMED]; intents average only 13 tokens [CONFIRMED]. Six LLMs ran against three personas: Expert Nitpicker, Vague Requester, Mind Changer [CONFIRMED]. Key results: clarification effectiveness does not translate into document quality — GPT-5.6-Sol had the best documents (BERTScore F1 0.774, ReqAlign 0.727) but the weakest clarification (EQR 0.196), while Gemini-3.1-Pro clarified best (EQR 0.334) but scored ReqAlign only 0.357 [CONFIRMED]. Interactive clarification improved documents: average ReqAlign rose from 0.212 to 0.494 (+133.1%) [CONFIRMED]. Coding-agent harnesses (Claude Code, Codex) raised clarification effectiveness but did **not** raise document quality — ReqAlign fell 15.2% (Claude) and 24.0% (GPT) under Expert Nitpicker [CONFIRMED]. Clarification also helped downstream code: game scores rose 0.012 → 0.273 → 0.418 (intent → direct doc → clarified doc) [CONFIRMED].

### Why this matters for the castle-sim harness [CONFIRMED]

This is the strongest direct match in the wiki to the **planner → executor handoff** [TENTATIVE]. The operator is a solo hobbyist who starts each milestone with a vague intent ("the castle should feel more like Stronghold's economy") [TENTATIVE]. The planner turns that into a slice spec, and everything downstream inherits the planner's reading [TENTATIVE]. The paper says an **incorrect guess about intent propagates and the rework is costly in long-horizon work** — exactly this project's shape [CONFIRMED]. This supports a new harness rule: **the planner should surface ambiguity and ask before writing the spec, rather than resolving it silently** [TENTATIVE]. Cross-links @concepts/ai-assisted-game-dev-workflows.md, @concepts/vertical-slice-v0.md (the slice spec is the artifact at risk), and @sources/arxiv-2610.08215-learn2play-bench-experience-2026-10-07.md (a related finding that the harness, not just the model, drives outcomes).

### Caveat [TENTATIVE]

The benchmark's tasks are repository-level software projects, and clarification quality is judged in that context. A solo hobby project has one known user (the operator), so clarification is cheap. The transfer is easier here than in a multi-client agency setting.

## Dead Ends

- Letting the planner silently resolve a vague operator intent.
- Treating a passing build as evidence the requirement was understood.
- Assuming a coding-agent harness fixes clarification: it raised question quality but lowered document quality in this study.
