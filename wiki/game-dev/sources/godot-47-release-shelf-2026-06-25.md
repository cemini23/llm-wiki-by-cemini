---
title: Godot 4.7 release shelf — editor workflow + Asset Store — 2026-06-25
type: source
tags: [source, godot, release, digest, news]
keywords: [godot-4.7, asset-store, arealight3d, editor]
related:
  - entities/engines/godot-4.md
  - concepts/godot-castle-sim-tool-gap-shelf.md
  - sources/inbox-arxiv-reject-batch-2026-06-25.md
  - sources/inbox-arxiv-reject-batch-2026-07-10.md
  - sources/inbox-arxiv-reject-batch-2026-07-11.md
  - meta/cross-wiki-routing.md
read_status: read
source_type: news-digest
source_url: https://pantspantsrevolution.com/godot-4-7-release/
maturity: validated
created: 2026-06-25
updated: 2026-07-10
---

## Raw Concept

Digest picks for **Godot 4.7** (2026-06-21 news cluster): editor workflow improvements, 3D path tooling, AreaLight3D, new **Asset Store**. Watch item for castle-sim pin bump — not an adoption gate yet.

## Narrative

### Digest refs

| Ref | Headline | URL |
|-----|----------|-----|
| R15 | Knightli 4.7 feature roundup | https://knightli.com/en/2026/06/21/godot-4-7-new-features-editor-workflow-area-light-asset-store/ |
| R17 | Pants Pants Revolution release notes | https://pantspantsrevolution.com/godot-4-7-release/ |

### castle-sim relevance [TENTATIVE]

| Maybe useful (Fork B 3D) | Defer |
|--------------------------|-------|
| AreaLight3D for architect mood lighting | Pin bump before Phase-7 polish |
| Asset Store for placeholder props | Kenney/CC0 shelf already primary |
| Editor workflow QoL | Re-run Phase-0 only if 4.7 fixes NavigationAgent regressions |

**Verdict:** **WATCH** — note in @entities/engines/godot-4.md; no repo pin change until stable 4.7.x + castle-sim regression pass.

### Jul 2026 update [CONFIRMED — godotengine.org]

| Ref | Headline | URL |
|-----|----------|-----|
| R15 (2026-07-09 digest) | Godot **4.7.1 RC 2** | https://godotengine.org/article/release-candidate-godot-4-7-1-rc-2/ |

Patch RC — still **WATCH** for hera-agent-godot 4.7+ pin (@sources/hera-agent-godot-phase-0-audit-2026-06-26.md) and castle-sim regression before bump.

### Godot 4.8 dev snapshot [TENTATIVE — forum]

| Ref | Headline | URL |
|-----|----------|-----|
| R15 (2026-07-06 digest) | Godot **4.8 dev 1** | https://forum.godotengine.org/t/dev-snapshot-godot-4-8-dev-1/141298 |

Early dev track — **no pin change**; note only on @entities/engines/godot-4.md until 4.7.x stable ships.

## Dead Ends

- Adopting 4.7 mid-Tier-2 without `--path` regression — pin 4.5.2/4.6.x until story-029 perf gate re-run
