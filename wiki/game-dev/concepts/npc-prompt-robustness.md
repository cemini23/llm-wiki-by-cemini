---
title: NPC prompt robustness — selective robustness as an acceptance test
type: concept
related:
  - concepts/agentic-npc-design-guardrails.md
  - concepts/llm-npc-runtime-ai-shelf.md
  - sources/arxiv-context-enrichment-selective-robustness-2611.06914.md
updated: 2026-11-10
---

## Raw Concept

An agentic NPC is an LLM that answers to a prompt and a game state. Its answer should not swing when the prompt is merely reworded, and it should change when a real game fact changes. This page records the test from arXiv 2611.06914 that puts both halves into one criterion. The question: how do we accept an NPC prompt as good, and not only fluent?

## Narrative

### The failure the test catches

The source paper reports that meaning-preserving prompt changes move LLM agent behavior a lot. One cited study saw a 76-point shift in cooperation rate from a format change alone. [Source: arxiv-context-enrichment-selective-robustness-2611.06914.md p.1] In a game, that is one NPC that behaves differently because a writer changed a list to bullet points.

### The criterion: selective robustness

Two halves. Both must hold.

| Half | Test | Fails when |
|------|------|-----------|
| **Surface invariance** | Same world, same context, different format: prose, bullets, key-value table, paraphrase. Behavior should stay close. | The model answers to the format, not to the world. |
| **World responsiveness** | Same format, one decision-relevant fact changed. Behavior should move in the direction set **before** the test. | The model ignores the game state. |

Neither half alone proves quality. A model that ignores context and always picks the same action is perfectly stable, and useless. A model that overreacts to phrasing looks responsive and is brittle. [Source: arxiv-context-enrichment-selective-robustness-2611.06914.md p.3]

### Same test, applied to context enrichment

The paper also separates four kinds of added context so their effects can be compared one at a time: neutral padding, generic social background, descriptive decision grounding, and normative decision grounding. Only grounded conditions gave both models a strong response to the world change. Only one of the two models also became more stable across formats. [Source: arxiv-context-enrichment-selective-robustness-2611.06914.md p.4] [TENTATIVE — pilot, one scenario, two models from one family]

### How this fits the NPC guardrail stack

@concepts/agentic-npc-design-guardrails.md section 6 already asks for tests with seeds, input logs, replay, and behavior snapshots with variance bounds. Selective robustness gives that section a concrete two-axis shape:

1. **Format sweep.** Hold the world fixed. Run the same NPC prompt as prose, bullets, key-value, and a paraphrase. Measure the spread in the chosen action or the action probability. A large spread is a failing prompt.
2. **World sweep.** Hold the format fixed. Change one fact that should matter — an ownership flag, a faction standing, a stockpile level. Check that the answer moves in the predicted direction. No movement is a failing prompt.
3. **Score on a plane, not a single number.** Plot mean surface sensitivity against world responsiveness. The target region is stable and responsive. Record both, as with the paper's two axes. [Source: arxiv-context-enrichment-selective-robustness-2611.06914.md p.4]

**Cheap version for a hobby project.** The full design is a factorial grid. A cut-down version still tests the idea: two formats, one world change, and a fixed set of canonical prompts. Even that catches a prompt that answers to formatting.

### Two cautions

**Grounding and salience are not separated.** The paper states a confound: a grounded prompt also repeats the world fact more, so a stronger world response may come from attention, not from grounding. A test that wants to separate these must equalize how often each condition states the fact. [Source: arxiv-context-enrichment-selective-robustness-2611.06914.md p.5]

**Do not pre-fill a recommended action.** This is rule **H5** in @concepts/agent-harness-castle-project.md, from a separate paper: a pre-filled default pulls an LLM's choice toward it. A default also contaminates the world-responsiveness test, because the answer tracks the default instead of the world. Keep the prompt neutral in both sweep axes.

### Status

This is a method page for the Tier 3+ NPC shelf. There is no NPC implementation and no measurement yet. The next step, when the shelf opens, is a small prompt set and a runner that applies the two sweeps.

## Snippets

> "Robustness should be selective: surface-level changes to a prompt should leave behavior stable, while substantively meaningful changes should alter behavior." [Source: arxiv-context-enrichment-selective-robustness-2611.06914.md p.3]

> "A larger difference in transfer probability between the regional and local worlds shows stronger responsiveness in the expected direction, but does not tell us whether the size of that response is appropriate." [Source: arxiv-context-enrichment-selective-robustness-2611.06914.md p.5]

## Dead Ends

- Using a single accuracy score for NPC prompt acceptance. It hides both failure axes: format sensitivity and world blindness.
