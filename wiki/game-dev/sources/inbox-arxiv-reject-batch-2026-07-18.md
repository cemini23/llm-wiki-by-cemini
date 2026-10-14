---
title: Inbox arXiv reject batch — 2026-07-18 (5 re-drops; identical to 07-17)
type: source
tags: [source, triage, reject, arxiv]
keywords: [arxiv, triage, reject, digest, re-drop, flow-matching, robotics, evolutionary-games]
related:
  - sources/inbox-arxiv-reject-batch-2026-07-19.md
  - sources/inbox-arxiv-reject-batch-2026-07-17.md
  - sources/inbox-arxiv-reject-batch-2026-07-16.md
  - concepts/flow-field-pathfinding.md
  - concepts/game-ai-rl-augmentation-shelf.md
  - meta/cross-wiki-routing.md
  - concepts/game-dev-wiki-scope.md
read_status: read
source_type: operator-triage
maturity: validated
created: 2026-07-18
updated: 2026-07-19
---

## Raw Concept

Five PDFs from `2026-07-18-daily.md` (arxiv-only paper lane; news disabled). **All reject (re-drop)** — byte-identical sha256 set as @sources/inbox-arxiv-reject-batch-2026-07-17.md. Re-fetch loop closed 2026-07-18: digest indexer now catalogs arXiv IDs from reject-batch Narrative tables.

## Narrative

| arXiv ID | Title (short) | Verdict | Route |
|----------|---------------|---------|-------|
| 2607.06315 | Low-frequency recombination lines (galaxies/AGN) | **Reject (re-drop ×2+)** | @sources/inbox-arxiv-reject-batch-2026-07-17.md |
| 2607.11340 | CR-Solver continuum robot kinematics | **Reject (re-drop ×2+)** | @sources/inbox-arxiv-reject-batch-2026-07-17.md |
| 2607.14424 | ConFlow flow-matching motion generation | **Reject (re-drop)** | Flow matching ≠ RTS flow fields — @sources/inbox-arxiv-reject-batch-2026-07-17.md |
| 2607.14826 | Interventional causal circuits (robot action testing) | **Reject (re-drop)** | @sources/inbox-arxiv-reject-batch-2026-07-17.md |
| 2607.14950 | Polymorphism in stochastic evolutionary games | **Reject (re-drop)** | Hawk–Dove math — @sources/inbox-arxiv-reject-batch-2026-07-17.md |

**Phase-0:** none. **Local adopt:** none.

**Briefs:** none — no poker / David / prod mapping from this inbox.

**News:** lane disabled — no news rows.

**Action:** Archive 5 PDFs to egress; clear inbox.

## Snippets

```
python3 scripts/preingest_check.py → 5 NEW (sha256 identical to 07-17 reject batch)
sha: 25563ab9… / 43a48fb4… / 7996be2a… / c5583687… / 25f6496e…
```

## Dead Ends

- Re-ingesting the same arXiv-API false-positive set nightly without query tightening — mitigated by reject-batch Narrative ID indexing (2026-07-18)
- Treating ConFlow / Hawk–Dove re-drops as new research for castle-sim
