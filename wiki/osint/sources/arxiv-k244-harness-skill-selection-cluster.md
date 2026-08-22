---
title: K244 cluster — EnvHarness wrap, BPS skill-set selection, Task-CoEvolve val tasks
type: source
tags: [agents, harness, skills, routing, evaluation]
keywords: [EnvHarness, EnvRigger, BPS, submodular, bicriteria, Task-CoEvolve, Meta-Harness, skill-router]
related:
  - concepts/skill-set-selection-under-budget.md
  - concepts/skill-misevolution.md
  - concepts/agent-toolkit-routing-research-backlog.md
  - concepts/wayfinder-fog-of-war-planning.md
  - sources/arxiv-2608.20317-browsecomp-plus-climbmix.md
maturity: draft
created: 2026-08-21
updated: 2026-08-21
read_status: skimmed
---

## Relations
- @concepts/skill-set-selection-under-budget.md
- @concepts/skill-misevolution.md
- @concepts/agent-toolkit-routing-research-backlog.md
- @concepts/wayfinder-fog-of-war-planning.md
- @sources/arxiv-2608.20317-browsecomp-plus-climbmix.md

## Raw Concept
- **title:** Harness / skill-selection cluster (three papers, one ingest)
- **author:** (1) Chengsong Huang et al. — EnvHarness; (2) Yu Chen, Ruishuo Chen, Xun Wang, Zhuoran Li, Longbo Huang (IIIS, Tsinghua) — BPS; (3) Atsuyuki Miyai, Kiyoharu Aizawa, Toshihiko Yamasaki (UTokyo) — Task-CoEvolve
- **type:** arXiv cluster (3 papers)
- **location:** `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2608.19880-envharness-awakening-static-worlds-for-agent-lea.pdf`; `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2608.19993-optimal-skill-selection-for-llm-agents-with-prov.pdf`; `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2608.20169-task-coevolve-efficient-harness-optimization-via.pdf`
- **retrieved:** 2026-08-21
- **pages:** three arXiv HTML abstracts + method/result sections
- **read-status:** skimmed

## Narrative
Three independent 2026-08 papers that should be read as one CCC routing decision: *do not rebuild the env; do not top-k skills; do not eval the whole val set every iteration.*

**EnvHarness / EnvRigger (2608.19880).** Static envs are blind to an agent’s weaknesses. EnvHarness is a programmable plug-in layer that wraps a static environment through standard interfaces and **keeps the original verifier**. EnvRigger treats the policy as a black box, diagnoses flaws from trajectories, synthesizes harness components, and validates on fresh rollouts. Up to +9.0 held-out, 9.8% fewer execution steps, across five benchmarks / four domains. GitHub not confirmed at ingest (author Chengsong-Huang; paper implies code). Steal: wrap, don’t rebuild.

**Optimal Skill Selection / BPS (2608.19993).** https://arxiv.org/abs/2608.19993. Skill selection is set-level, not per-skill ranking. Objective: monotone submodular capability benefit G(S) minus linear token penalty κ·ℓ(S), under hard token budget B. BPS (Best Prefix Selection): density-greedy chains from size-≤2 seeds, record every prefix, pick best F. Bicriteria (1−1/e, 1) — tight on the benefit coefficient. Contamination-controlled BigCodeBench fork: BPS 0.73 task success vs 0.20–0.52 for released routers / retrievers / executor self-select; 28% fewer tokens than the strongest released router. Complementary skills 93% vs one-capability 0%; a look-alike distractor −23 pp. Top-k is the misevolution path.

**Task-CoEvolve (2608.20169).** https://github.com/Agent4Science-UTokyo/Task-CoEvolve. Harness opt usually evals the full val set every iteration. Task-CoEvolve co-evolves val tasks: variance-weighted sampling (Bernoulli variance of historical success, floor for never-solved, uncertainty bonus) plus sampling-aware full-set score (Hájek or anchored difference). Matches full-set search at ~20% evals (80% fewer); on Terminal-Bench 2.1, 67–80% search-cost cut, ~1 pt gap vs full search. At 20% it can *beat* full-set (less val overfitting).

Cluster steal for CCC: BPS set-level skill select, EnvHarness wrap, Task-CoEvolve variance-weighted val tasks. Propose-only — not Adopt this wave.

## Snippets
> EnvHarness … wraps a static environment to reshape its behavior without modifying the underlying logic … ensuring every reshaped environment retains its original verifier … up to a 9.0-point improvement on held-out instances with 9.8% fewer execution steps. [Source: https://arxiv.org/abs/2608.19880 (retrieved 2026-08-21)]

> We give the first model of how the selected skill set shapes execution outcomes and cast skill selection as … monotone submodular benefit minus context penalty. … BPS … bicriteria (1−1/e, 1) … 0.73 measured task success versus 0.20–0.52 for released skill routers … on 28% fewer tokens. [Source: https://arxiv.org/abs/2608.19993 (retrieved 2026-08-21)]

> Task-CoEvolve … uses variance-weighted sampling based on past outcomes to focus evaluation on tasks near the agent’s capability frontier … matches the final performance of full-set search while reducing the number of evaluations during optimization by 80%. [Source: https://arxiv.org/abs/2608.20169 (retrieved 2026-08-21)]
