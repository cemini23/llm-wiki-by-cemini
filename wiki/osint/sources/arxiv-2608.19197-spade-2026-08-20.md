---
title: "SPADE — self-play in adaptive synthetic executable environments (arXiv 2608.19197)"
type: source
tags: [arxiv, rl, poker, k243]
keywords: [SPADE, self-play, Gym, hint-based-regret, environment-designer]
related:
  - entities/tools/spade.md
  - concepts/llm-environment-engineer-rl-curriculum.md
  - concepts/poker-arena-multi-axis-cognitive-profile.md
  - concepts/cemini-license-posture.md
  - sources/eval-multi-repo-revenue-2026-08-20.md
maturity: draft
created: 2026-08-20
updated: 2026-08-20
read_status: read
---

## Relations

- @entities/tools/spade.md — MIT Extract clone; poker Arena REFERENCE
- @concepts/llm-environment-engineer-rl-curriculum.md — environment design as a learnable component
- @concepts/poker-arena-multi-axis-cognitive-profile.md — Arena REFERENCE; no decide() retune
- @concepts/cemini-license-posture.md — MIT confirmed; clone allowed
- @sources/eval-multi-repo-revenue-2026-08-20.md — same-day OSINT K243 evals (no poker Integrate)

## Raw Concept

| Field | Value |
|-------|--------|
| Paper | arXiv:2608.19197, "SPADE: Self-Play in Adaptive Synthetic Executable Environments" |
| Authors | Bo Liu, Simon Yu et al. (UW / Stanford / Northeastern / CMU / MIT / NUS / SNU / Stevens / Chicago) |
| Retrieved | 2026-08-20 |
| File | `arxiv-2608.19197-spade-self-play-in-adaptive-synthetic-executable.pdf` |
| sha256 | `2459c2b53e79ebf0ceec4879b4163d0f992c7f1073e7503408b2399e1911fe6e` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2608.19197-spade-self-play-in-adaptive-synthetic-executable.pdf` |
| Repo | https://github.com/spade-rl/spade — **MIT, Extract clone** |
| Dual-ID | **OSINT K243**. Poker Arena REFERENCE. Do not retune `decide()` unless a one-line steal already exists in Arena briefs. |

## Narrative

SPADE trains a single LLM in two roles: an Environment Designer that writes complete long-horizon Gym-style environments (`reset()`/`step()` with state, reward, and verification code) and a Reasoning Agent that acts in them. The Designer's reward is **hint-based regret** — the gap between agent return with and without a privileged hint — so environments sit at the edge of capability while remaining feasible. Grounding the Designer on pretraining-corpus documents plus an accumulated environment memory is reported as critical.

**Concrete claim `[TENTATIVE]`:** at 30B, SPADE beats the strongest fixed-environment baseline by +5.3 average across eight held-out math/science/code/reasoning benches, +5.7 on BFCL v4 multi-turn, and +13.9 on ACEBench-Agent. Poker Arena steal: synthetic executable environments as a REFERENCE curriculum generator — not a live-betting loop. Clone MIT `.local/adopts/spade`. No jailbreak / exploit env generation.

## Snippets

> "By making environment design itself a learnable component, SPADE takes a concrete step toward open-ended self-improvement." [Source: arxiv-2608.19197 abstract]
