---
title: Inbox arXiv reject batch — 2026-07-17 (5 rejects; 2 re-drops + flow-matching / robot / evo-game)
type: source
tags: [source, triage, reject, arxiv]
keywords: [arxiv, triage, reject, digest, re-drop, flow-matching, robotics, evolutionary-games]
related:
  - sources/inbox-arxiv-reject-batch-2026-07-18.md
  - sources/inbox-arxiv-reject-batch-2026-07-16.md
  - sources/inbox-arxiv-reject-batch-2026-07-15.md
  - concepts/flow-field-pathfinding.md
  - concepts/game-ai-rl-augmentation-shelf.md
  - meta/cross-wiki-routing.md
  - concepts/game-dev-wiki-scope.md
read_status: read
source_type: operator-triage
maturity: validated
created: 2026-07-17
updated: 2026-07-18
---

## Raw Concept

Five PDFs from `2026-07-17-daily.md` (arxiv-only paper lane; news disabled). **All reject** — two sha re-drops from 07-16 plus three new false positives (ML flow-matching motion gen, robot causal testing, Hawk–Dove polymorphism math).

## Narrative

| arXiv ID | Title (short) | Verdict | Route |
|----------|---------------|---------|-------|
| 2607.06315 | Low-frequency recombination lines (galaxies/AGN) | **Reject (re-drop)** | Radio astronomy — @sources/inbox-arxiv-reject-batch-2026-07-16.md |
| 2607.11340 | CR-Solver continuum robot kinematics | **Reject (re-drop)** | Tendon-driven robot IK — @sources/inbox-arxiv-reject-batch-2026-07-16.md |
| 2607.14424 | ConFlow flow-matching motion generation | **Reject** | Generative **flow matching** for robot trajectories (VW / TUM) — not RTS flow fields |
| 2607.14826 | Interventional causal circuits (robot action testing) | **Reject** | Physical AI / motion-parameter testing (Bremen) — not Stagehand playtest |
| 2607.14950 | Polymorphism in stochastic evolutionary games | **Reject** | Hawk–Dove math (Bath) — not castle-sim / not poker-arena methodology |

**Phase-0:** none. **Local adopt:** none.

**Briefs:** none — no castle-sim research steal; no poker / David / prod mapping from this inbox.

**News:** lane disabled — no news rows.

**Action:** Archive 5 PDFs to egress; clear inbox.

## Snippets

```
python3 scripts/preingest_check.py → 5 NEW (2 sha match 07-16 reject batch)
ConFlow = flow matching (ODE neural sampler), not Emerson/Leif grid flow fields
```

## Dead Ends

- Treating ML “flow matching” papers as RTS flow-field research
- Routing evolutionary Hawk–Dove polymorphism into castle-sim lord AI or poker briefs from game-dev
