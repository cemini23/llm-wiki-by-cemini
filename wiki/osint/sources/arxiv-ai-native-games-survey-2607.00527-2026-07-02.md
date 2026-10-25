---
title: "AI Native Games — A Survey and Roadmap — arXiv 2607.00527"
type: source
tags: [arxiv, game-dev, llm, generative-ai, survey, k140, pdf]
keywords: [AI-native games, G/N taxonomy, core loop, mechanical invariants, runtime generative AI, PCG, interactive narrative]
related:
  - concepts/ai-native-games-taxonomy.md
  - concepts/castle-sim-rts-micromanagement-steals.md
  - concepts/devfun-researcher-track-readiness-2026-06.md
  - sources/arxiv-hrl-influence-map-starcraft-2606.30092-2026-06-30.md
  - sources/arxiv-2607.00190-latent-maps-performance-2026-07-03.md
maturity: draft
read_status: read
created: 2026-07-02
updated: 2026-10-25
clusters: [game-dev, agent-harness]
---

## Relations

- @concepts/ai-native-games-taxonomy.md — synthesized G/N framework
- @concepts/devfun-researcher-track-readiness-2026-06.md — poker Arena eval rubric parallels (mechanical invariants)

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | AI Native Games: A Survey and Roadmap |
| **Authors** | Xu, Meng, Xu, Verbrugge, Lucas, Zhao |
| **arXiv** | 2607.00527v1 |
| **Type** | PDF |
| **sha256** | `6c1086aff999b8d8d26045133b9a8a3e558b0d477fbb1a8d09cace246eb8c51b` |
| **Corpus** | 53 publicly available AI-native games/prototypes (curated list in paper) |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2607.00527-ai-native-games-a-survey-and-roadmap.pdf` |
| **Retrieved** | 2026-07-02 |
| **Read status** | read (abstract + intro + contributions) |

## Narrative

Defines **AI-native games** via counterfactual: if runtime generative AI were removed, **core loop collapses** — distinct from AI-assisted production, PCG-only, or optional chat NPCs.

### Contributions

1. **2×2 boundary matrix** — AI-native vs augmented vs boundary artifacts vs out-of-scope
2. **Corpus n=53** — screened public prototypes
3. **Dual-axis G/N taxonomy** — G = player-facing game type; N = dominant AI mechanic constitutive to play
4. **Roadmap** — controllable generation, inference economics, evaluation, safety, regulation

### Corpus concentration

Language-forward designs dominate (narrative adventure, epistemic interaction, generative narrative). **Underrepresented:** semantic adjudication, multi-agent simulation, generative construction, companion/relationship play.

**Design thesis:** organize **semantic openness** with **mechanical invariants** — goals, rules, state, feedback, pacing, agency.

**Cemini relevance:** game-dev + poker Arena harness — steal invariant-checklist for sandbox eval rubrics; not prod game adoption.

## Snippets

> "AI-native games are games in which generative AI functions as a constitutive core mechanism." [Source: arxiv-2607.00527 §1 (retrieved 2026-07-02)]

> "The central design problem is organizing semantic openness into stable gameplay." [Source: arxiv-2607.00527 abstract (retrieved 2026-07-02)]
