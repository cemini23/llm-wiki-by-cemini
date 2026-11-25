---
title: "Self-verification failure taxonomy — why agents pass their own tests and still fail"
type: concept
related:
  - sources/arxiv-scientific-coding-finite-element-analysis-2611.21176.md
  - concepts/agent-verification-patterns.md
  - concepts/generation-verification-gap-agent-artifacts.md
  - concepts/agent-completion-verification-gates.md
  - concepts/llm-verification-layer-accept-escalate-reject.md
  - concepts/execution-bound-evidence-certification.md
updated: 2026-11-25
maturity: draft
---

## Raw Concept

Question this page answers: an agent runs its tests, they pass, and the code is still wrong. What failed?

Synthesised from one source: `@sources/arxiv-scientific-coding-finite-element-analysis-2611.21176.md` (FEM-Bench extension, 2611.21176).

## Narrative

The authors ran 15 models on 17 finite element tasks, then six of them through two agentic harnesses with execution feedback. They analysed 249 failed agentic trajectories where the agent had passed its own checks.

Six failure categories appear. Two dominate:

- **Inadequate test coverage** — 73.1% of cases.
- **Reliance on generic consistency checks** — 70.3%.
- **Shared error** — 28.5% of cases, where the test repeats the implementation's mistake.

The consequence is visible in the Pass@3 versus Pass3 split. Claude Opus 5 with SimpleAgent reaches 96.5% Pass@3 (at least one of three succeeds) and 77.1% Pass3 (all three succeed). No pair exceeds 78.8% Pass3.

### The fix the paper tests

Separate the coder and the tester into different agents. That configuration reaches 97.6% Pass@3 and 88.8% Pass3, the best observed.

### Operating rules

1. **A test written by the same agent that wrote the code is weak evidence.** It can share the error.
2. **Coverage beats pass rate.** A passing narrow test says little.
3. **Report consistency, not only best-of-N.** Pass@3 flatters a model that sometimes fails; Pass3 shows the floor.

This is the same lesson as the "verify the artifact, not the claim" rule in `@concepts/agent-completion-verification-gates.md`. [TENTATIVE] single source.

## Snippets

> "The most common are inadequate test coverage (73.1%) and reliance on generic consistency checks (70.3%), and in 28.5% of cases the tests share an error with the implementation." [Source: arxiv-2611.21176-scientific-coding-with-large-language-models-evi.pdf p.1]

> "An exploratory configuration with separate coder and tester agents achieves the highest observed scores, with 97.6% Pass@3 and 88.8% Pass3." [Source: arxiv-2611.21176-scientific-coding-with-large-language-models-evi.pdf p.1]
