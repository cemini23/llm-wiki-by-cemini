---
title: "Concordat: Typed Sessions for LLM Agents"
type: source
tags: [source, arxiv, llm-agents, typestate, session-types]
related: []
maturity: draft
read_status: skimmed
created: 2026-11-01
updated: 2026-11-01
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Concordat: Typed Sessions for LLM Agents |
| Authors | Milad Sikaroudi, Independent Researcher |
| arXiv | 2610.37461 |
| File | `arxiv-2610.37461-concordat-typed-sessions-for-llm-agents.pdf` |
| Retrieved | 2026-11-01 |
| URL | https://arxiv.org/abs/2610.37461 |
| Read status | skimmed (abstract + intro) |

## Narrative

LLM agents now take actions with real effects. Examples include cancelling bookings, issuing refunds, and changing accounts. A rule for those actions, such as an explicit customer confirmation before a change, usually sits in the prompt. The model follows that rule only as reliably as it chooses.

Concordat is a Python library. It treats an agent as an object. The object interface is a finite-state protocol, in the spirit of typestate and session types. The library enforces that protocol on the model at run time.

On every turn the model receives only the tools that are legal in the current protocol state. A call outside that set is rejected before it has a side effect. A decision reserved for a human can only be requested. Token budgets and tool-call budgets are charged and split linearly across handoffs. The library checks a protocol when the protocol is defined. It rejects a subclass that could bypass its parent protocol. The paper calls this check a behavioural form of Liskov substitution.

The authors compare a Concordat agent with the standard agent of τ-bench on its 50 airline tasks. They add simulated customers who pressure the agent to skip confirmation. The paper reports that the standard agent made changes without the required “yes” in 13 of 50 tasks with gpt-4.1, and in 29 of 128 task-runs with Claude Haiku 5.5. The Concordat agent made none. The paper reports no significant difference in task success. It reports that τ-bench’s own reward did not detect most of these violations. These counts are this paper’s own measurements. One source states them.

Concordat is open source. For an agent and coding-harness practitioner, the paper claims that a protocol can withhold illegal tools, reject a call before a side effect, and reject an unsafe subclass when the class is defined. The same evaluation claims that a task-success reward can miss a skipped confirmation.

## Snippets

> "We evaluate a Concordat agent against the standard agent of τ-bench on its 50 airline tasks, adding simulated customers who pressure the agent to skip confirmation. The standard agent made changes without the required “yes” in 13 of 50 tasks with gpt-4.1 and in 29 of 128 task-runs with Claude Haiku 5.5; the Concordat agent made none, with no significant difference in task success." [Source: `arxiv-2610.37461-concordat-typed-sessions-for-llm-agents.pdf` p.1 (arXiv 2610.37461), retrieved 2026-11-01]
