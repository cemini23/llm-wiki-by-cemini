---
title: "Intent contracts — separate the planner from the tool call, and measure what that buys"
type: concept
maturity: draft
related:
  - sources/arxiv-intent-contracts-tools-away-2611.24025.md
  - concepts/intent-governed-tool-authorization.md
  - concepts/agent-least-privilege-tool-selection.md
  - concepts/agent-runtime-guardrails.md
  - concepts/agent-execution-provenance.md
updated: 2026-11-22
---

## Raw Concept

What this page answers: if the planning model never holds a tool, does authorization get safer? From 2611.24025.

## Narrative

An intent contract is a logged record per step: a goal, a verbatim quotation of the user, and scope fields. Code validates it. A small trusted model checks it against the user's words and writes the actual tool call. The planner only sees tool output and chooses the next step.

**Three properties follow from the dispatch code**, if that code is correct:

- Every executed call is written by the trusted model.
- The planner's influence is confined to a contract logged before the call.
- The trusted side chooses how much of a request to execute.

These are code properties, not model properties. They hold only to the extent that the dispatch code is right.

**The measured result is a caution.** On three AmPermBench families, with gpt-6.1-terra as planner and GLM-5.3-Flash as trusted model:

- Under contracts, every changed object was named in the contract's goal.
- Under command review, the planner named objects in the command but rarely in the goal.
- When the planner added unrequested work, contracts completed the task in 27/30 runs; intent-visible review in 16/30, because a reviewer can only refuse a whole command.

But contracts did not reduce unauthorized actions. They were indistinguishable from blind review. Every state-changing condition hit a wrong target in 40 to 49% of runs. The cause is the planner's choice of object for an ambiguous reference. No trusted model in this setup sees the environment, so it cannot check that choice. Telling the executor to decline when unsure does not fix it.

**Scope and honest limits.** Benign over-reach, one model pair, cooperative models. No adversarial planner was tested.

**Lab use.** The separation is useful for evidence and audit trails, not as a proven security gain. Do not wire it as a control claim until an adversarial evaluation exists.

[Source: arxiv-2611.24025-intent-contracts-taking-tools-away-from-agents.pdf]

## Snippets

> "They are properties of that code and hold to the extent that it is correct."
[Source: arXiv:2611.24025v1 §1]
