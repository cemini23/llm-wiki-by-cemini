---
title: "Intent Contracts — taking tools away from agents (2611.24025)"
type: source
maturity: draft
related:
  - concepts/intent-contract-planner-tool-separation.md
  - concepts/intent-governed-tool-authorization.md
  - concepts/agent-least-privilege-tool-selection.md
  - concepts/agent-runtime-guardrails.md
updated: 2026-11-22
---

## Raw Concept

- **Title:** Intent Contracts: Taking Tools Away from Agents
- **Authors:** Ziyuan Wang, Genliang Zhu, Xiaobo Chen, Chu Wang (independent; Georgia Tech; UMass Amherst; UIUC)
- **Type:** arXiv preprint (cs.CR)
- **Location:** `research to be indexed/cybersec/arxiv-2611.24025-intent-contracts-taking-tools-away-from-agents.pdf`
- **Retrieved:** 2026-11-19
- **arXiv:** 2611.24025v1, 18 November 2026
- **Read status:** read — 8 of 10 pages extracted 2026-11-22

## Narrative

An intent contract is an authorization interface. The planning model holds no tools. For each step it submits a short logged contract: a goal, a verbatim quotation of the user, and scope fields.

Code validates the contract. A small trusted model checks the contract against the user's words and writes the tool call itself. Three properties follow from the dispatch code, if that code is correct. Every executed call is written by the trusted model. The planner's influence on a call is confined to a contract logged before it. The trusted side decides how much of a request to carry out.

The comparison uses three conditions. Contract, blind review of a planner-written command, and intent-visible review that also sees the goal and a checked quotation. Models: gpt-6.1-terra as planner, GLM-5.3-Flash as trusted model. Benchmark: three AmPermBench task families.

The measurement is programmatic and time-aligned with the benchmark logs. Under contracts, every object changed was named in the goal of the contract that produced the change. Under review, the planner named objects in its commands but rarely in its goals.

The results are mixed, and the paper states them plainly. When the planner adds work the user never asked for, contracts complete the user's task in 27 of 30 runs. Intent-visible review completes 16 of 30, because a reviewer can only refuse a whole command.

The negative result is the important one for a lab. Contracts do not reduce unauthorized actions. They are indistinguishable from blind review. Once the benchmark's environment terms are clarified, every condition that changes state hits a wrong target in 40 to 49% of those runs. The error is the planner's choice of object for an ambiguous reference. No trusted model here can see the environment to check that choice. Telling the executor to decline when unsure does not change it.

Scope: benign over-reach with one pair of models. The paper does not evaluate an adversarial planner.

[Source: arxiv-2611.24025-intent-contracts-taking-tools-away-from-agents.pdf]

## Snippets

> "Contracts do not reduce unauthorized actions. They are indistinguishable from blind review."
[Source: arXiv:2611.24025v1 abstract]

> "That error is the planner's choice of objects for an ambiguous reference, which no trusted model here can see the environment to check."
[Source: arXiv:2611.24025v1 abstract]
