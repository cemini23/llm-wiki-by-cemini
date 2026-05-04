---
title: Autoresearch Loop Pattern — LLM Proposal × Objective Function × Automated Mutation/Rollback
type: concept
tags: [llm-agents, autoresearch, neuro-symbolic, multi-agent, conductor-evolution, prediction-markets, methodology-pattern]
keywords: [autoresearch-loop, sharpe-as-loss, neuro-symbolic-loop, gemini-sec-2-6, atlas-gic, conductor-priors, vibe-proving, darwinian-prompt-evolution]
related:
  - sources/gemini-sci-research-2602-03837.md
  - sources/links-2-5-4-tool-eval.md
  - entities/tools/atlas-gic-autoresearch.md
  - sources/agriciDaniel-claude-obsidian.md
  - concepts/llm-agent-systems.md
  - concepts/scatter-gather-topology.md
maturity: draft
created: 2026-05-04
updated: 2026-05-04
---

## Relations

- @sources/gemini-sci-research-2602-03837.md — §2.6 (Agentic Tool-Use & Automated Feedback) defines the canonical mathematical-research instance: LLM proposes math expression → autonomous code → numerical traceback → context injection
- @sources/links-2-5-4-tool-eval.md — origin discovery: the atlas-gic financial instantiation surfaces in the same week as the Gemini paper, allowing pattern-recognition across domains
- @entities/tools/atlas-gic-autoresearch.md — financial instantiation: Sharpe ratio replaces math hypothesis, git revert/commit replaces context injection
- @sources/agriciDaniel-claude-obsidian.md — claude-obsidian's `/autoresearch` multi-round loop (Wave 5B Adopt) is an independently-arrived-at version
- @concepts/llm-agent-systems.md — parent concept; autoresearch is a sub-pattern of the broader agentic systems family
- @concepts/scatter-gather-topology.md — LangGraph topology that hosts autoresearch nodes (proposal stage = scatter; objective evaluation = gather; mutation stage = state update before next scatter)

## Raw Concept

This page synthesizes a methodology pattern that emerged from three concurrent observations in the 2026-05-04 ingest batch:

1. **Gemini paper §2.6** documents the pattern in mathematical research with rigorous case studies (SNARGs flaw detection, spectral coefficients via Gegenbauer expansion)
2. **atlas-gic** instantiates the same pattern in algorithmic trading with rolling Sharpe as objective function
3. **claude-obsidian `/autoresearch`** (already in wiki via `@sources/agriciDaniel-claude-obsidian.md`) implements a generic multi-round version

Conductor v0.1.1 sits adjacent: its routing-decision loop has the proposal + objective structure but currently uses human-tuned `--build-priors` rather than autoresearch-driven mutation. This concept page is the architectural-evolution-target for Conductor.

## Narrative

### The pattern (load-bearing definition)

An **autoresearch loop** has three components:

```
┌──────────────┐    ┌────────────────────┐    ┌──────────────────┐
│  PROPOSAL    │ →  │  OBJECTIVE         │ →  │  MUTATION        │
│              │    │  EVALUATION        │    │  + ROLLBACK      │
│ LLM-generated│    │ Numerical /        │    │ State change OR  │
│ (text, code, │    │ behavioral check   │    │ revert; result   │
│ trade, etc.) │    │ against ground     │    │ feeds next loop  │
└──────────────┘    │ truth or KPI       │    │                  │
       ↑            └────────────────────┘    └────────┬─────────┘
       │                                                │
       └────────────────────────────────────────────────┘
                  Result becomes input to next iteration
```

The signature is: **proposal → ground-truth check → automated state mutation with reversibility**. Crucially, the loop runs without per-step human review — but the human sets the objective function and sets reversibility bounds.

### Three documented instantiations

| Domain | Proposal | Objective | Mutation | Reversibility |
|--------|----------|-----------|----------|---------------|
| **Math research** (Gemini §2.6) | Math expression / hypothesis | Python script numerical evaluation against known baseline | Context injection of traceback | Pure-functional; previous context preserved |
| **Algorithmic trading** (atlas-gic) | Agent system-prompt rewrite | Rolling Sharpe ratio over live performance | Git commit of new prompt | `git reset` if Sharpe degrades |
| **Multi-round research** (claude-obsidian `/autoresearch`) | Search query / synthesis | Quality / completeness heuristic | Iterative refinement | Branch-based; each round is standalone |

### Why this matters for Cemini

Conductor v0.1.1 has the **proposal + objective** structure (taxonomy classifier proposes routing → judge / cost-tracking objective) but lacks the **mutation/rollback** dimension as autoresearch:

- Current: routing decisions logged → `--build-priors` rebuilds priors from full sample, manually triggered
- Autoresearch evolution: cost/judge metrics → automated taxonomy-or-pool mutation → automated revert if cost regresses

The atlas-gic pattern is the closest published template. The Gemini paper §2.6 is the theoretical justification. claude-obsidian's `/autoresearch` is the lighter-weight variant.

### Practical adoption path for Conductor

[NEEDS VERIFICATION 2026-05-04] — the path is conceptual until prototyped:

1. **Phase 0 — Define objective function rigorously**: Conductor's existing cost+judge metric is fine; codify it as a single scalar fitness function
2. **Phase 1 — Implement proposal generator**: LLM proposes new routing rule (e.g., "shift macro_analysis from reasoner-only to cascade") given recent decision logs
3. **Phase 2 — Apply proposal in shadow mode**: route N% of traffic via the proposed rule for K decisions
4. **Phase 3 — Compare objective**: shadow-mode fitness vs baseline fitness over the same window
5. **Phase 4 — Promote or revert**: if shadow fitness ≥ baseline + ε, promote (commit to config.yaml); else revert (no change)
6. **Phase 5 — Audit trail**: git-track every proposal-and-outcome to maintain rollback history

This is a **clean-room re-implementation of atlas-gic**'s pattern (per `@entities/tools/atlas-gic-autoresearch.md` license blocker), informed by the Gemini paper's theoretical frame.

### Prediction-market relevance

Per user note 2026-05-04: Cemini's prediction-market scope (Kalshi + Polymarket → sports, healthcare/biotech, politics, weather, economic indicators) is **objective-function-rich**. Each prediction-market vertical has a distinct ground-truth (event outcomes, FDA approvals, election results, weather observations, economic data releases) that serves as a clean objective function for autoresearch.

This is materially different from generic equity trading: prediction markets settle to known outcomes, so an autoresearch loop can use *post-resolution accuracy* as a more decisive objective than rolling Sharpe (which only gives signal over long windows). For a Cemini-on-prediction-markets autoresearch deployment, **Brier score + rolling profit** is the canonical fitness function — Brier score for calibration, rolling profit for execution quality.

### Risks of the pattern

1. **Reward hacking**: if the objective function is gameable, the LLM will game it. Cf. the Gemini paper's §2.4 ("Formalization & Rigor Checks") — the rigor checks exist precisely to prevent this.
2. **Token cost**: continuous proposal generation consumes API budget. atlas-gic's 25-agent debate matrix is "likely exorbitant" per Gemini DR. Conductor's autoresearch should be small-N (3-5 agents max) or shadow-mode-throttled.
3. **Local optima**: gradient-style mutation can get stuck. atlas-gic's Darwinian (worst-performer rewrite) approach mitigates this by being explicitly non-monotonic.
4. **Lack of explainability**: prompt mutations may yield improvements no human can explain. This is a feature in research contexts (the Gemini paper §2.2 cross-pollination cases) and a concern in production trading contexts (audit trail, regulatory exposure).

### What this is NOT

- Not RLHF — RLHF tunes model weights against human preferences; autoresearch tunes prompts/configs against numerical objectives
- Not agentic tool-use alone — that's just Sec 2.6's tool-call pattern; autoresearch adds the **automated state mutation** dimension
- Not "AutoML" — AutoML tunes hyperparameters within a fixed model architecture; autoresearch can tune the *architecture* (which agents, how routed, what prompts)

## Snippets

- **Gemini paper §2.6 (canonical neuro-symbolic loop)**: "The LLM generates a mathematical hypothesis or intermediate expression... autonomously writes an executable script (e.g., in Python) to evaluate its proposed math against a known numerical baseline... The system executes the code. If the code fails, hits a runtime error, or reveals numerical instability (such as catastrophic cancellation), the automated harness captures the exact execution traceback and injects it back into the LLM's context window. This programmatic loop allows the AI to systematically explore a tree of mathematical solutions, autonomously pruning dead-ends and self-correcting its algebra without requiring a human-in-the-loop for every intermediate step." [Source: arXiv:2602.03837v3 §2.6 p.10]

- **atlas-gic financial instantiation**: "isolating the worst-performing agent based strictly on real-world market outcomes—specifically measured by the rolling Sharpe ratio—and prompting the overarching LLM to fundamentally rewrite that agent's internal system instructions... a git-tracked evolutionary history where successful prompt modifications are permanently committed, and failures are automatically reverted via git reset, leveraging Darwinian scoring methodologies." [Source: links 2 5_4.docx URL 9]

## Dead Ends

*(none yet — concept just synthesized.)*
