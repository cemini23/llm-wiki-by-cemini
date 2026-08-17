---
title: "Agent skills as procedural anchors — not knowledge dumps"
type: concept
tags: [concept, skills, ccc, k240]
keywords: [procedural-anchoring, SKILL.md, retrieval-precision, library-cap, misevolution]
related:
  - sources/arxiv-2608.14036-demystifying-agent-skills-2026-08-17.md
  - concepts/skill-misevolution.md
  - sources/arxiv-2608.12851-skill-misevolution-2026-08-14.md
  - entities/tools/addyosmani-agent-skills.md
maturity: draft
created: 2026-08-17
updated: 2026-08-17
---

## Relations

- @sources/arxiv-2608.14036-demystifying-agent-skills-2026-08-17.md — primary source
- @concepts/skill-misevolution.md — three lifecycle gates (author/retrieve/execute)
- @sources/arxiv-2608.12851-skill-misevolution-2026-08-14.md — skills can get worse with practice
- @entities/tools/addyosmani-agent-skills.md — already K223; do not re-tier

## Raw Concept

What this page answers: why SKILL.md files help, why they stop helping as the library grows, and what Cemini must not automate. Synthesized from arXiv 2608.14036 (OSINT K240) + misevolution 2608.12851 (K237). Dual-ID: OSINT K240 ≠ CCC K240 robotics.

## Narrative

A skill is not a second memory of facts. Jiang et al. (2608.14036) isolate the mechanism: skills improve over raw workflow memory because they compress noisy trajectories into a short procedure — what to do, what to check, what to avoid. In their contrastive study, **procedural anchoring accounts for 65.7%** of skill-use cases versus **4.5%** for explicit knowledge injection `[TENTATIVE]`. Skills beat workflow memory by about 6 points in matched comparisons because they drop failed branches and verbose exploration, not because they inject missing world knowledge.

The second result is operational: **retrieval is the bottleneck**. As the candidate pool grows from 5 to 100, actual-use precision falls from 29.6% to 3.3%. Exact ground-truth invocation is neither sufficient nor necessary — a nearby skill can still help, and the "right" skill can still fail if the context is wrong. That is why a growing `.cursor/skills/` directory is not free: every added file taxes retrieval.

Misevolution (2608.12851) is the complementary failure: a "successful" trajectory that contains an unsafe shortcut becomes a reusable skill and later causes harm after the trigger is gone. The three gates — authoring, retrieval, execution — plus retirement on evidenced harm and a library cap — are the governance, not more SKILL.md files.

**Cemini steal:** write skills as procedural anchors. Keep a library cap and a retirement path. **No unattended auto-evolve** of `.cursor/skills/*`. Do not re-tier addyosmani/agent-skills (already K223 Integrate). CCC `/route` owns skill-library ops.

## Snippets

> "skills stabilize action rather than inject missing facts." [Source: arxiv-2608.14036 abstract]

> "as pools grow from 5 to 100, actual-use precision falls from 29.6% to 3.3%." [Source: arxiv-2608.14036 abstract]
