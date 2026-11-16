---
title: Language models as closed-loop controllers
type: concept
maturity: draft
related:
  - sources/arxiv-llm-agent-battery-fast-charging-2611.18140.md
updated: 2026-11-16
---

## Raw Concept

Question this page answers: what changes when a language model is a controller rather than a predictor?

From arXiv 2611.18140 (battery fast-charging).

## Narrative

Three differences from the "LLM as predictor" pattern.

**Actions, not estimates.** The model emits an executable control action, so an error is an action taken, not a number on a page.

**Response in the loop.** It observes the resulting state and adjusts. The training corpus has to be state-action-response trajectories, not input-output pairs.

**Two-stage training.** Supervised fine-tuning first teaches the semantics of the domain and a feasible starting policy; policy optimisation then trades off competing objectives (throughput, degradation, constraints). SFT alone tends to produce plausible but objective-blind actions.

The reported result is longer cycle life than conventional and optimisation-based baselines at matched throughput, across five chemistries — in simulation only.

The transferable caution applies to any agentic control lane in this workspace: a simulation-grounded proof of concept is not a field result, and the gap between them is where most of the risk sits.

[OPEN QUESTION 2026-11-16] Whether the policy transfers to real cells with ageing, sensor noise and thermal variation is untested here.

## Snippets

> "a simulation-grounded proof of concept for using LLM agents as sequential decision makers."
