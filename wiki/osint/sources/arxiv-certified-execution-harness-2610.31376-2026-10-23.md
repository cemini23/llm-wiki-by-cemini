---
title: "Certified execution harness — a tool call fires only on present marks"
type: source
related:
  - concepts/k294-osint-wave.md
  - concepts/options-agent-order-boundary.md
maturity: draft
read_status: skimmed
updated: 2026-10-23
---

## Raw Concept

Title: A certified execution harness for agentic AI
Authors: Chao Gu, Quanyan Zhu
Type: arXiv preprint (2610.31376)
Inbox file: `research to be indexed/osint/arxiv-2610.31376-certified-execution-harness-for-agentic-ai-safe.pdf`
Location: `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2610.31376-certified-execution-harness-for-agentic-ai-safe.pdf`
Retrieved: 2026-10-23
Read status: skimmed (abstract)

## Narrative

A Petri net sits between the model and the tools. Marks are capabilities, approvals, and budgets.

A transition fires only when the marks it needs are present. A request with unmet or spent preconditions is refused regardless of the wording.

Tool outcomes are uncontrollable. In a replanning loop, each retry costs an inference call.

The conventional maximally permissive supervisor can be arbitrarily more intrusive than a stricter safe one. On the authors' autonomous release agent, safe deployment needs a step the supervisor can refuse after a rollout starts.

This is the same boundary rule as @concepts/options-agent-order-boundary.md. The mark is outside the model. **No install. No trade.**
