---
title: atlas-gic — Autoresearch Loop with Sharpe-as-Loss-Function (NO LICENSE blocker)
type: entity
tags: [llm-agents, autoresearch, multi-agent, financial-research, reference-only, no-license, steal-from]
keywords: [atlas-gic, autoresearch, sharpe-ratio-loss, 25-agent-debate, darwinian-scoring, prompt-evolution, git-tracked-prompts, conductor-evolution-candidate]
related:
  - sources/links-2-5-4-tool-eval.md
  - sources/gemini-sci-research-2602-03837.md
  - concepts/autoresearch-loop-pattern.md
  - sources/agriciDaniel-claude-obsidian.md
maturity: draft
created: 2026-05-04
updated: 2026-05-04
---

## Relations

- @sources/links-2-5-4-tool-eval.md — origin source: 2026-05-04 Gemini DR eval, URL 9, **Steal-from** tier (license-blocked for code reuse)
- @sources/gemini-sci-research-2602-03837.md — atlas-gic is a financial-domain instantiation of the Gemini paper's Section 2.6 (Agentic Tool-Use & Automated Feedback / neuro-symbolic loop)
- @concepts/autoresearch-loop-pattern.md — concept page synthesizing this pattern; atlas-gic is the canonical financial example
- @sources/agriciDaniel-claude-obsidian.md — claude-obsidian's `/autoresearch` multi-round loop is an independently-arrived-at version of the same pattern

## Raw Concept

Multi-agent financial simulation framework implementing a continuous autoresearch loop: 25 LLM agents stratified across 4 hierarchical layers, each with distinct investment psychologies, debate live trades. The system identifies the worst-performing agent by rolling Sharpe ratio, prompts a meta-LLM to rewrite that agent's instructions, git-tracks the rewrite, and reverts via `git reset` if performance degrades.

Identified as **Steal-from-tier** in the 2026-05-04 Gemini DR eval — code cannot be deployed (NO LICENSE), but the architectural pattern can be re-implemented clean-room.

## Narrative

- **URL**: https://github.com/chrisworsey55/atlas-gic
- **License**: NO LICENSE [Source: links 2 5_4.docx URL 9 evaluator-confirmed unable to retrieve LICENSE file]
- **Stack**: Python 100%, Anthropic API (Claude Sonnet), Polygon + Finnhub + FRED data feeds, originally Azure VMs
- **Maturity**: 1.6k stars BUT only 4 total commits (sanitized static code-drop, not actively maintained)

### The pattern (load-bearing content)

1. **25 specialized agents** across 4 hierarchical layers, each representing a distinct investment psychology (macro-momentum, deep tech, etc.)
2. **Live market exposure**: agents propose trades against real Polygon/FRED feeds
3. **Objective scoring**: rolling Sharpe ratio applied per-agent
4. **Worst-performer identification**: lowest-Sharpe agent flagged each cycle
5. **Meta-LLM rewrite**: overarching LLM rewrites the flagged agent's system prompt
6. **Git-track**: rewrite committed as a discrete revision
7. **Revert-on-failure**: if subsequent live performance degrades, `git reset` rolls back
8. **Capital reallocation**: successful agents' votes weighted more heavily on subsequent decisions
9. **Layer escalation**: top-layer "Decision" synthesizers consume Layer 3 "Superinvestor" outputs; Layer 0 JANUS Meta-Layer detects market regime shifts

### Why this is the highest-leverage architectural pattern in the 5_4 batches

The pattern is the canonical instance of **agentic autoresearch** — an LLM proposes, an objective function judges, automated state mutation/rollback persists or discards changes. It directly parallels:

- **Gemini paper §2.6** (neuro-symbolic loop): LLM proposes math expression → code executes → traceback feedback. Mathematical correctness as objective function.
- **Conductor v0.1.1**: taxonomy-based routing decisions logged; `--build-priors` rebuilds routing distribution. Currently *human-tuned* (not autoresearch-driven), but the pattern is in scope for future evolution.
- **claude-obsidian `/autoresearch`** (`@sources/agriciDaniel-claude-obsidian.md`): multi-round research loop with iterative refinement. Same conceptual family.

### Why we cannot deploy atlas-gic code

- **NO LICENSE** → default copyright applies → cannot be modified, redistributed, or relied on commercially
- 4 total commits + Azure-specific deployment scripts → likely a static demo, not a maintained codebase
- Token-cost of 25-agent live debate matrix is "likely exorbitant and must be carefully benchmarked" per Gemini DR

### Adoption path: clean-room re-implementation

1. **Read the Gemini DR eval description** (this entity page is the canonical summary)
2. **Read the linked thoughtleader.school blog post** ("I Just One-Shotted A Blockbuster") for additional architectural detail [Source: links 2 5_4.docx works-cited list]
3. **Do NOT clone or read the atlas-gic repo source code** (NO LICENSE → derivative-work risk if implementation is informed by source reading)
4. **Re-implement the pattern from public description only**, in Python compatible with Cemini's existing LangGraph + FastMCP stack
5. **Stage as a brief**: `briefs/2026-05-04_autoresearch-loop-conductor-evolution.md` for the prod-server-side Claude session

### Token-cost concern

A 25-agent × 4-layer × N-decisions-per-day debate matrix consumes substantial Anthropic API budget. The shadow-mode-first principle from Conductor's deployment (`@hot.md` "30-day shadow mode for stash token-cost telemetry") applies here: any clean-room implementation should run in shadow mode against logged decisions before going live.

### Prediction-market relevance

The autoresearch pattern is venue-agnostic. Sharpe-as-loss works on any time series with profit/loss outcomes — equities, crypto, **and prediction-market binary contracts** (Kalshi/Polymarket). Per user note 2026-05-04: Cemini's prediction-market scope (sports, healthcare, politics, weather, economic indicators) means a clean-room atlas-gic-pattern implementation could optimize agent prompts against prediction-market outcomes the same way the original optimizes against equity Sharpe.

## Snippets

- **Autoresearch loop mechanics**: "iteratively refine live trading strategies. The system consumes massive streams of macroeconomic data and localized equity feeds to fuel a complex, four-layer hierarchical debate among 25 distinct LLM agents... isolating the worst-performing agent based strictly on real-world market outcomes—specifically measured by the rolling Sharpe ratio—and prompting the overarching LLM to fundamentally rewrite that agent's internal system instructions... git-tracked evolutionary history where successful prompt modifications are permanently committed, and failures are automatically reverted via git reset, leveraging Darwinian scoring methodologies." [Source: links 2 5_4.docx URL 9]

- **License blocker**: "License: NOT FOUND — flag for follow-up. A LICENSE file is indicated to exist in the repository structure, but the exact text and SPDX identifier cannot be successfully retrieved from the primary sources." [Source: links 2 5_4.docx URL 9]

- **Recommendation tier (clean-room only)**: "Steal-from. Due to the unverified license, the underlying code cannot be deployed, but the overarching architecture—specifically the brilliant Karpathy-style autoresearch loop utilizing the rolling Sharpe ratio as the primary loss function—must be rigorously studied and structurally translated into Cemini's LangGraph orchestrator." [Source: links 2 5_4.docx URL 9]

- **Maturity caveat**: "exhibits a total history of only 4 commits, strongly implying that the codebase represents a sanitized, static code-drop meant for demonstration rather than a mature, actively maintained software framework capable of surviving edge cases." [Source: links 2 5_4.docx URL 9]
