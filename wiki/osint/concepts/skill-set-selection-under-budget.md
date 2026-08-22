---
title: Skill-set selection under budget — BPS, not top-k
type: concept
tags: [skills, routing, harness, submodular]
keywords: [BPS, monotone-submodular, token-penalty, bicriteria, skill-shadowing, EnvHarness, Task-CoEvolve]
related:
  - sources/arxiv-k244-harness-skill-selection-cluster.md
  - concepts/skill-misevolution.md
  - concepts/agent-toolkit-routing-research-backlog.md
maturity: draft
created: 2026-08-21
updated: 2026-08-21
---

## Relations
- @sources/arxiv-k244-harness-skill-selection-cluster.md
- @concepts/skill-misevolution.md
- @concepts/agent-toolkit-routing-research-backlog.md

## Raw Concept
Loading skills is a *set* decision under a token knapsack. Independent relevance scores + top-k / greedy packing ignore complementarity, redundancy, and the context penalty. Wrong skills can beat the no-skill baseline downward. BPS maximises monotone submodular benefit minus linear token penalty with a (1−1/e, 1) bicriteria guarantee.

## Narrative
This is the constructive answer to skill-misevolution: libraries grow, routers keep stuffing semantically similar docs, success falls.

Operating rules for CCC (propose-only):
1. **Select sets, not ranks.** Cover demanded capabilities; after coverage, extra tokens are mostly penalty. A look-alike distractor is worse than a redundant complement.
2. **Charge κ per token.** Compression of skill bodies is not optional polish.
3. **BPS-shaped search** over a shortlist (retrieve first, then set-select). Do not LLM-enumerate the whole registry in-context.
4. **Wrap envs (EnvHarness)** instead of generating new static worlds; keep the verifier.
5. **Co-evolve val tasks (Task-CoEvolve).** Variance-weight tasks near the frontier; estimate full-set scores; 20% evals can match or beat full-set search.

Against the routing backlog: replace “top-k skill router” tickets with a budgeted set selector. Neural capability encoders can stand in for lookup tables off-benchmark (BPS+encoder 0.68 vs lookup 0.73 in the paper).

Phase-0: none. Phase-1 leftover: none. Propose for `/phase1` in Cursor: BPS skill router, EnvHarness wrap.

## Snippets
See @sources/arxiv-k244-harness-skill-selection-cluster.md (0.73 vs 0.20–0.52; +9.0 EnvHarness; 80% fewer Task-CoEvolve evals).
