---
title: AI-native games — G/N taxonomy and mechanical invariants (K140)
type: concept
tags: [concept, game-dev, llm, generative-ai, taxonomy, k140, reference-only]
keywords: [AI-native, core loop, G-axis, N-axis, semantic adjudication, controllable generation, inference economics]
related:
  - sources/arxiv-ai-native-games-survey-2607.00527-2026-07-02.md
  - concepts/castle-sim-rts-micromanagement-steals.md
  - concepts/devfun-researcher-track-readiness-2026-06.md
  - concepts/poker-arena-multi-axis-cognitive-profile.md
  - sources/arxiv-2608.09574-hierarchical-game-llm-2026-08-11.md
maturity: draft
created: 2026-07-02
updated: 2026-08-11
---

## Relations

- @sources/arxiv-ai-native-games-survey-2607.00527-2026-07-02.md — Xu et al. survey (2607.00527)
- @concepts/poker-arena-multi-axis-cognitive-profile.md — nine-axis eval parallel (mechanical scoring of open-ended play)

## Raw Concept

What prompted this page: K140 survey defines when runtime LLM/generative AI is **constitutive** of play vs cosmetic — and argues successful designs enforce **mechanical invariants** on open-ended outputs.

## Narrative

### Counterfactual definition

Remove runtime generative AI → core loop **collapses or becomes fundamentally different** = AI-native. Excludes: dev-time AI, static AIGC assets, conventional game AI, optional chat NPCs, pure PCG without runtime interpretation.

### G/N dual axis

| Axis | Captures |
|------|----------|
| **G** | Player-facing game type (narrative adventure, simulation, …) |
| **N** | Dominant AI mechanic that makes generative AI indispensable (generative narrative, semantic adjudication, multi-agent sim, …) |

Corpus n=53 skews language-forward G-types; **semantic adjudication** and **multi-agent simulation** underrepresented — design gaps.

### Mechanical invariants (steal for harness)

Goals · rules · state · feedback · pacing · agency — make LLM outputs **interpretable and consequential**. Maps to:

- **castle-sim:** scripted win/lose + resource state despite procedural siege chatter
- **Poker Arena:** nine-axis rubric + verifier gates on `decide()` outputs

**Posture:** REFERENCE — game-dev taxonomy brief + optional poker rubric crosswalk.

Brief: `../projects/Game Dev wiki/briefs/2026-07-02_k140-ai-native-games-gn-taxonomy-steal.md`

## Snippets

> "Unbounded generation may increase variety while weakening the very structures that make play meaningful." [Source: arxiv-2607.00527 §1 (retrieved 2026-07-02)]
