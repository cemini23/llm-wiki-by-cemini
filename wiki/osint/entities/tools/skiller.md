---
title: SKILLER — language-level RL skill extraction (paper + repo)
type: entity
tags: [entity, tool, agent-skills, rl, no-go, k233]
keywords: [skiller, skill-extraction, rl, small-lm, qwen, agent-skills]
related:
  - sources/arxiv-2608.10538-skiller-2026-08-12.md
  - concepts/agent-skill-rl-extraction.md
maturity: draft
created: 2026-08-12
updated: 2026-08-12
---

## Relations

- @sources/arxiv-2608.10538-skiller-2026-08-12.md
- @concepts/agent-skill-rl-extraction.md

## Raw Concept

`github.com/DANG-ai/SKILLER` — official implementation of arXiv 2608.10538. NOASSERTION SPDX (no LICENSE detectable via gh api), 1★, ~1.5MB, pushed 2026-08-12.

## Narrative

**Verdict: NO-GO clone** (no clean SPDX). Research-reference only: the RL-via-natural-language skill-authoring loop (strong model as actor/critic, small-model agent as environment) is a reusable pattern for generating `/route`-style skills for small local models in the CCC harness. See `@concepts/agent-skill-rl-extraction.md`.

[Source: arXiv:2608.10538]
