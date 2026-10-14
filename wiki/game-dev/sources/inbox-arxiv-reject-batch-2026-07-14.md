---
title: Inbox arXiv reject batch — 2026-07-14 (1 ingest + 4 rejects)
type: source
tags: [source, triage, reject, arxiv]
keywords: [arxiv, triage, reject, digest, world-model, type-theory, music, robotics]
related:
  - sources/inbox-arxiv-reject-batch-2026-07-13.md
  - sources/inbox-arxiv-reject-batch-2026-07-12.md
  - sources/arxiv-2607.10174-vrexplorer-vr-testing-2026-07-14.md
  - sources/vrexplorer-phase-0-audit-2026-07-14.md
  - meta/cross-wiki-routing.md
  - concepts/game-dev-wiki-scope.md
read_status: read
source_type: operator-triage
maturity: validated
created: 2026-07-14
updated: 2026-07-14
---

## Raw Concept

Five PDFs from `2026-07-14-daily.md`. **One ingest** (VRExplorer), **four reject**. Influence-map / lockstep / navmesh digest clusters again mixed game-adjacent hits with PL theory, AV robotics, social robotics, and music harness false positives.

## Narrative

| arXiv ID | Title (short) | Verdict | Route |
|----------|---------------|---------|-------|
| 2607.10174 | VRExplorer Unity VR testing | **Ingest + Phase-0** | @sources/arxiv-2607.10174-vrexplorer-vr-testing-2026-07-14.md → **NO-GO adopt** |
| 2607.05966 | Imagined rollouts kinematic (DreamerV3 / DMC) | **Reject** | AV Systems Lab world-model diagnostic — not game AI |
| 2607.07475 | Agent-exploitation affordances | **Reject** | Social-robotics ontology (LAAS-CNRS); not NPC/RTS |
| 2607.08547 | Potential Functions as Types (Calf/Giralf) | **Reject (re-drop)** | PL amortized-cost type theory; influence-map false positive (@sources/inbox-arxiv-reject-batch-2026-07-12.md) |
| 2607.11334 | Generate–verify–repair twelve-tone music | **Reject** | Music composition harness; lockstep false positive → harness pattern note @ccc-wiki only |

**Phase-0:** VRExplorer → **NO-GO adopt** / STEAL-FROM patterns (@sources/vrexplorer-phase-0-audit-2026-07-14.md). No local adopt (undeclared license + Unity VR).

**Briefs:** castle-sim legacy — research shelf only (`briefs/research/vrexplorer-model-based-playtest-shelf.md`). No poker / xsp / pm / David / prod scp from this inbox.

**Parallel ingest (news):** SH4 Gameindustry review already on @sources/stronghold-4-public-demo-2026-06-24.md (R3 07-08); grid placement + Phaser MCP already shelved prior days. No new news pages.

**Action:** Archive 5 PDFs to egress; clear inbox.

## Snippets

```
python3 scripts/preingest_check.py → 5 NEW
Phase-0: TsingPig/VRExplorer shallow clone ~272MB; license null; NO-GO adopt
```

## Dead Ends

- Treating CMU "potential functions" cost types as RTS influence maps
- Treating DreamerV3 walker iKCE as castle-sim world-model shelf (wrong domain vs MIRA)
- Adopting Unity VRExplorer under the <500 MB local-adopt rule without license
