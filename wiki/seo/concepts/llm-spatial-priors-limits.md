---
title: Where LLM spatial priors fail
type: concept
maturity: draft
related:
  - sources/arxiv-llm-spatial-priors-navigation-2611.18123.md
updated: 2026-11-16
---

## Raw Concept

Question this page answers: when is a language model a useful source of spatial layout information, and when is a measured layout better?

From arXiv 2611.18123.

## Narrative

Models capture categorical structure and miss metric structure.

What they get right: object frequencies by room type, room sizes, and object-to-object association (put the kettle near the fridge, move other things away).

What they get wrong: distance to walls does not follow real per-room-type differences, and movable furniture tends to pile at room centre rather than where real furniture sits. Constraints given in the prompt are followed partially — most objects go against a stated wall, but the room rectangle is not respected.

Contrast with the alternative. A prior estimated from real layouts reduced search cost in **every** room type tested, and by more than three times the reduction of the model-generated prior. Smoothing both shrank the gap but did not close it.

The usable pattern: let the model supply associations and draft coordinates, constrain them with an external component, then check geometrically. Do not substitute it for measured data when measured data exists.

[TENTATIVE] One preprint's abstract on two models and two layout datasets.

## Snippets

> "the models place most objects against that wall, but they do not keep all objects inside a given room rectangle."
