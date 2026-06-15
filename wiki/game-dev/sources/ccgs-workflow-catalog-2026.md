---
title: CCGS workflow-catalog.yaml — phase and artifact map
type: source
tags: [source, ccgs, workflow, claude-code, yaml]
keywords: [ccgs, workflow-catalog, phases, artifacts, gate-check]
related:
  - concepts/ccgs-workflow-extraction.md
  - entities/tools/claude-code-game-studios.md
  - sources/claude-code-game-studios-phase-0-audit-2026-06-13.md
read_status: read
source_type: upstream-config
source_url: https://github.com/Donchitos/Claude-Code-Game-Studios/blob/main/.claude/docs/workflow-catalog.yaml
maturity: validated
created: 2026-06-13
updated: 2026-06-15
---

## Raw Concept

Machine-readable **phase → steps → artifacts** catalog powering CCGS `/help` and progression hints.

## Narrative

### Seven phases [CONFIRMED — upstream YAML]

| Phase | next_phase | Purpose |
|-------|------------|---------|
| concept | systems-design | Idea → game-concept, art-bible, systems-index |
| systems-design | technical-setup | Per-system GDDs + cross review |
| technical-setup | pre-production | architecture.md, ADRs (min 3), control-manifest |
| pre-production | production | UX specs, prototype, epics/stories, vertical-slice |
| production | polish | sprint-plan, dev-story, QA loops |
| polish | release | balance, perf, soak |
| release | — | launch checklist, store |

### Artifact check types

- `glob` + optional `pattern`, `min_count`
- `required: true|false`, `repeatable: true`
- Phase gates **advisory** — user always decides proceed

### Sample required artifacts

| Step | Artifact path |
|------|---------------|
| engine-setup | `.claude/docs/technical-preferences.md` |
| game-concept | `design/gdd/game-concept.md` |
| map-systems | `design/gdd/systems-index.md` |
| architecture | `docs/architecture/architecture.md` |
| ADRs | `docs/architecture/adr-*.md` (≥3) |
| vertical-slice | `prototypes/*/REPORT.md` |

### 73 skills (directory names)

adopt, architecture-decision, architecture-review, art-bible, asset-audit, asset-spec, balance-check, brainstorm, bug-report, bug-triage, changelog, code-review, consistency-check, content-audit, create-architecture, create-control-manifest, create-epics, create-stories, day-one-patch, design-review, design-system, dev-story, estimate, gate-check, help, hotfix, launch-checklist, localize, map-systems, milestone-review, onboard, patch-notes, perf-profile, playtest-report, project-stage-detect, propagate-design-change, prototype, qa-plan, quick-design, regression-suite, release-checklist, retrospective, reverse-document, review-all-gdds, scope-check, security-audit, setup-engine, skill-improve, skill-test, smoke-check, soak-test, sprint-plan, sprint-status, start, story-done, story-readiness, team-audio, team-combat, team-level, team-live-ops, team-narrative, team-polish, team-qa, team-release, team-ui, tech-debt, test-evidence-review, test-flakiness, test-helpers, test-setup, ux-design, ux-review, vertical-slice

### 49 agents (names)

accessibility-specialist, ai-programmer, analytics-engineer, art-director, audio-director, community-manager, creative-director, devops-engineer, economy-designer, engine-programmer, game-designer, gameplay-programmer, godot-csharp-specialist, godot-gdextension-specialist, godot-gdscript-specialist, godot-shader-specialist, godot-specialist, lead-programmer, level-designer, live-ops-designer, localization-lead, narrative-director, network-programmer, performance-analyst, producer, prototyper, qa-lead, qa-tester, release-manager, security-engineer, sound-designer, systems-designer, technical-artist, technical-director, tools-programmer, ue-blueprint-specialist, ue-gas-specialist, ue-replication-specialist, ue-umg-specialist, ui-programmer, unity-addressables-specialist, unity-dots-specialist, unity-shader-specialist, unity-specialist, unity-ui-specialist, unreal-specialist, ux-designer, world-builder, writer

## Snippets

Extraction guide: @concepts/ccgs-workflow-extraction.md
