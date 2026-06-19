---
title: UnofficialCrusaderPatch2 — Stronghold Crusader mod (steal-from)
type: entity
tags: [entity, tool, stronghold, modding, steal-from]
keywords: [ucp, stronghold, crusader, aiv, patch, mit]
related:
  - entities/games/stronghold-series.md
  - concepts/stronghold-modding-ecosystem-shelf.md
  - concepts/stronghold-systems-inventory.md
  - concepts/rts-siege-ai-reference.md
  - sources/tool-evaluation-cross-wiki-routing-2026-06-13.md
  - sources/unofficial-crusader-patch2-phase-0-audit-2026-06-13.md
  - concepts/tool-evaluation-cross-wiki-batch-2026-06-13.md
  - concepts/stronghold-crusader-ai-modding-shelf.md
maturity: validated
created: 2026-06-13
updated: 2026-06-15
---

## Relations

- @concepts/stronghold-modding-ecosystem-shelf.md — sibling mod repos (mostly unlicensed)

## Raw Concept

[`UnofficialCrusaderPatch/UnofficialCrusaderPatch2`](https://github.com/UnofficialCrusaderPatch/UnofficialCrusaderPatch2) — community **balancing and bugfix patch installer** for Stronghold Crusader 1 (~435★, MIT).

## Narrative

### What it exposes [CONFIRMED — eval + repo]

- Binary patching for legacy Crusader executable
- **AIV** (AI village) injection and custom lord behaviors
- Community-driven pathfinding and economy balance fixes
- Active issue queue (500+ open) — living design discussion (e.g. Nomad AI)

### Value for castle-sim [TENTATIVE]

| Study | Apply in Godot |
|-------|----------------|
| AIV layout parameters | Data-driven castle templates + defense priorities |
| Balance patch rationale | Economy tuning notes in wiki, not binary patches |
| Path bug postmortems | Navigation regression tests |

**Do not** ship Firefly assets or patch binaries — design archaeology only.

### Security cross-link

Memory hooking techniques → @cybersecurity-wiki stub (offensive case study). Not used in castle-sim runtime.

Design notes brief: `briefs/systems/aiv-design-notes.md` (local, gitignored).

### Phase-0 audit (2026-06-13)

| Check | Result |
|-------|--------|
| License | MIT [CONFIRMED] |
| Runtime | Patch retail Crusader exe — **NO-GO** for castle-sim |
| Study | AIV categories, balance changelogs, issue threads |
| Audit | @sources/unofficial-crusader-patch2-phase-0-audit-2026-06-13.md |

### Verdict

**STEAL-FROM** — patterns and balance *intent*; MIT allows reading source for reimplementation ideas.

## Snippets

Research entry points:

```
issues/301 — Nomad AI discussion
docs/ — patch changelogs (pathfinding, unit caps)
AIV examples bundled with patch releases (verify license on bundled files separately)
```

## Dead Ends

- Running UCP2 as dependency of castle-sim — different engine, different binary
- Importing community AIV binaries from unlicensed sibling repos — see modding shelf reject list
