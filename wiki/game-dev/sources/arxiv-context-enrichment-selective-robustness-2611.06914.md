---
title: "A Framework for Context Enrichment and Selective Robustness in LLM Social Agents"
type: source
related:
  - concepts/npc-prompt-robustness.md
  - concepts/agentic-npc-design-guardrails.md
  - concepts/llm-npc-runtime-ai-shelf.md
updated: 2026-11-10
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | A Framework for Context Enrichment and Selective Robustness in LLM Social Agents |
| Author | Mattia Greiche, Reihaneh Rabbany, Maximilian Puelma Touzel (McGill University, Mila) |
| Type | arXiv preprint (cs.MA) — NeurIPS 2026 SocialAgent workshop |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/game-dev/arxiv-2611.06914-a-framework-for-context-enrichment-and-selective.pdf` |
| Retrieved | 2026-11-10 |
| File | `arxiv-2611.06914-a-framework-for-context-enrichment-and-selective.pdf` |
| Pages | 12 |
| arXiv | 2611.06914v1, 4 Nov 2026 |
| Read status | read |

## Narrative

This is a **validation-method** paper. The authors run LLM agents as social simulation participants. They report that small, meaning-preserving changes to prompt wording and format move agent behavior a lot. One cited study saw cooperation rates in a Prisoner's Dilemma shift by up to 76 percentage points [Source: arxiv-2611.06914-a-framework-for-context-enrichment-and-selective.pdf p.1]. Under that much variance, a simulation result is hard to defend.

**Two contributions.**

1. **Controlled context enrichment.** Five prompt conditions, using rule-based substitution at one fixed place in the prompt. The five are minimal, neutral padding, generic social background, descriptive decision grounding, and normative decision grounding. Only one additional block goes in at a time. The blocks do not accumulate. [Source: arxiv-2611.06914-a-framework-for-context-enrichment-and-selective.pdf pp.2-3]

2. **Selective robustness.** A single validation criterion with two halves. The agent must stay stable across surface forms that keep the same meaning. And the agent must move in the **prespecified** direction when something that matters changes in the world. Low surface sensitivity alone is not proof of quality; a model that ignores context and always picks the same action also scores well on it. [Source: arxiv-2611.06914-a-framework-for-context-enrichment-and-selective.pdf p.3]

**Pilot.** One focal agent acts as emergency-supply manager for Hospital A. It chooses TRANSFER or RETAIN against Hospital B. Two worlds: a shared regional supply arrangement and separate local ones. Four surface forms: canonical prose, bullets, key-value table, alternative prose. That gives 2 × 5 × 4 = 40 cells per model, with ten calls per cell — 800 calls total for two models. [Source: arxiv-2611.06914-a-framework-for-context-enrichment-and-selective.pdf pp.3-4, p.7]

**Result.** Grounded conditions raise world responsiveness for both models. Only one model also gains surface stability. The other model stays surface-sensitive. In its local normative condition, alternative prose produced 89.9% transfer, against at most 0.9% for the other three surfaces [Source: arxiv-2611.06914-a-framework-for-context-enrichment-and-selective.pdf p.4]. Same prompt meaning, a 89-point swing. [TENTATIVE — one model, one cell]

**Stated limits.** The pilot has one scenario and two models from one family. The authors do not claim a general effect. They also name a confound: grounded prompts repeat the world distinction more, so salience is not separated from grounding [Source: arxiv-2611.06914-a-framework-for-context-enrichment-and-selective.pdf p.5]. Code and data are public.

**Why this belongs in game-dev.** The paper is about social simulation, not games. But an agentic NPC is exactly an LLM agent that answers to a prompt and a world state. The selective-robustness test gives the NPC guardrail program a concrete acceptance test: vary the prompt format and the answer must not move much; change a real game fact and the answer must move. This is a method transfer to the Tier 3+ NPC shelf, not a shipped feature. Method page: @concepts/npc-prompt-robustness.md.

## Snippets

> "We call this joint requirement selective robustness: ideally, an agent should be insensitive to changes in representation that preserve the social meaning relevant to the decision, but sensitive to substantive changes in the social world that likely should affect the decision." [Source: arxiv-2611.06914-a-framework-for-context-enrichment-and-selective.pdf p.2]

> "Low surface sensitivity can be a sign of robustness, but it can also arise if the model simply ignores the social context or consistently chooses the same action." [Source: arxiv-2611.06914-a-framework-for-context-enrichment-and-selective.pdf p.3]

> "In Terra's local normative condition, alternative prose yields 89.9% transfer, compared with at most 0.9% for the other three surfaces." [Source: arxiv-2611.06914-a-framework-for-context-enrichment-and-selective.pdf p.4]

> "Selective robustness does not by itself establish fidelity to human behavior; it serves as an internal diagnostic." [Source: arxiv-2611.06914-a-framework-for-context-enrichment-and-selective.pdf p.5]
