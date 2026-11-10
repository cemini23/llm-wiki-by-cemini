---
title: "Verify foundational work, trust non-foundational work"
type: concept
related:
  - sources/newsletter-rss-pragmatic-engineer-2026-11-05-scaling-slack-and-github-with-maude-lemaire.md
  - sources/newsletter-rss-latent-space-2026-11-08-how-stanford-teaches-ai-native-engineering-mihai.md
  - concepts/ai-native-engineering-curriculum.md
  - concepts/agent-completion-verification-gates.md
updated: 2026-11-10
---

## Raw Concept

Question this page answers: which model output must a human check, and which may pass unread?

Synthesised from the Maude Lemaire interview and the Stanford CS146S interview.

## Narrative

Maude Lemaire, a principal engineer who worked on Slack, GitHub, and Cursor performance, states a simple rule. For platform work she personally verifies everything an LLM gives her, because ambitious structures can only be built on stable foundations.

The rule is a **partition**, not a blanket. Work splits into:

- **Foundational** — the data layer, the schema, the build, the measurement harness, the security boundary. A defect here propagates and is expensive to reverse. Verify by hand.
- **Non-foundational** — copy, scaffolding, throwaway analysis, a one-off script. A defect here is cheap. Accept and move on.

The Stanford CS146S material reaches the same place from a different direction. Last year's homework is now one prompt. What remains worth grading is whether the author understands the patch, especially what else it breaks.

### Why this matters for agent lanes

An agent harness cannot apply this rule by itself. A model does not know which of its outputs will become foundational. The partition is a human judgement made **before** the run, and it must be recorded in the task, not inferred later.

Practical form for Cemini:

1. Tag the task. Foundational work gets a verification step: a second model, a test, or a read-through.
2. Non-foundational work ships without the gate. Adding a gate to every task makes the gate meaningless.
3. Reclassify upward. When a throwaway script becomes a `scripts/` tool, it becomes foundational, and it needs the check it skipped.

The failure this prevents is the opposite of the usual complaint. The risk is not that the agent writes bad text; it is that a plausible-looking foundation is never checked because it looked routine.

## Snippets

> "When doing foundational work, Maude pays close attention to verifying the output of LLMs because she believes that ambitious structures can only be built on stable foundations." [Source: newsletter-rss-pragmatic-engineer-2026-11-05-scaling-slack-and-github-with-maude-lemaire.md]
