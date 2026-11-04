---
title: "P-ContextBench — from personal fact recall to personalised agent behaviour"
type: source
tags: [source, arxiv, benchmark, privacy, personalisation, agents]
related: []
maturity: draft
read_status: skimmed
created: 2026-11-03
updated: 2026-11-03
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | P-ContextBench: From Personal Fact Recall to Personalized Agent Behavior |
| Authors | Grant Nasir Brown, Abdul Basir Bari, Anmol Tadikonda, Isabel Song (San Francisco State University) |
| arXiv | 2610.40959 |
| Pages | 8 |
| Read status | skimmed (abstract) |

## Narrative

Evaluating whether a model can safely use **personal context** is hard because the context is private, fragmented, dynamic, and socially situated. Benchmarks usually sidestep this by handing the model a tidy profile.

P-ContextBench does not. It builds **population-structured, life-story-grounded digital humans** from demographic seeds reflecting the US population, and embeds traits and routines rather than presenting an explicit static profile.

### Why the construction matters

The gap between "recall a fact from a profile" and "behave correctly given a person's lived context" is the whole problem. A model that can recite a birthday has not shown it will avoid mentioning something painful, or that it understands a routine well enough not to interrupt it.

Building the context as a *life story* rather than a *record* is what makes the second thing measurable.

### Relevance here

This is the closest benchmark in the batch to the Atto problem, from the opposite side. Atto holds family history, and its hard bans exist because that context is exactly this kind of private, fragmented, socially situated material.

The transferable point is a design one: **a personal-context test set is not a list of fields.** It is a set of situations where the correct behaviour depends on understanding rather than lookup.

**Caveat.** Abstract only. No task count or score is reproduced here.

## Snippets

> "Rather than presenting personal context as explicit and static profiles, P-ContextBench embeds traits, routines, …" [Source: arxiv-2610.40959 p.1]

## Dead Ends

- **Citing a benchmark score.** Abstract only.
