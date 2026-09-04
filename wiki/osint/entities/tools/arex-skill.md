---
title: AREX-Skill — GitHub repos distilled into AutoML agent skills
type: entity
tags: [tool, k255, skills, automl, apache-2.0, harness]
keywords: [AREX-Skill, Repo-To-Skill, DisCo, VectorSpaceLab, 2609.02749]
related:
  - sources/arxiv-2609.02749-repo-to-skill-2026-09-04.md
  - concepts/k255-harness-evolution-wave.md
maturity: draft
created: 2026-09-04
updated: 2026-09-04
phase_0_verdict: GO REFERENCE
harness_verb: FILE
wire_note: Laptop REFERENCE clone only; never import into Claude, Codex, or federation skill directories
---

## Relations

- @sources/arxiv-2609.02749-repo-to-skill-2026-09-04.md — arXiv 2609.02749 Repo-To-Skill paper
- @concepts/k255-harness-evolution-wave.md — K255 harness cluster

## Raw Concept

| Field | Value |
|-------|-------|
| **Repo** | https://github.com/VectorSpaceLab/AREX-Skill |
| **License** | Apache-2.0 `[CONFIRMED]` gh api SPDX 2026-09-04 + `LICENSE` Apache-2.0 header |
| **Local** | `.local/adopts/AREX-Skill` (~442MB, shallow `--depth 1`) |
| **Stars** | 168 (2026-09-04) |
| **Last push** | 2026-09-03 (`ac3fe1af` add citation info) |

K255 Phase-0 prompted by Repo-To-Skill (arXiv:2609.02749). Official public runtime for the paper. Distills GitHub repositories into Agent Skills for autonomous ML research.

## Narrative

**Pattern.** DisCo (`@arex-skill/disco`) distills a repo or paper into an Agent Skills package: `SKILL.md` plus optional `references/` and `scripts/`. A router narrows a request area to family to repository skill root to sub-skill, then loads only that branch. Published library: 1,000 repository skill roots, 20 areas, 178 families, 5,000+ skills. Layout:

```text
skills/repositories/repo-skills/<skill-id>/SKILL.md
skills/repositories/repo-skills-router/
```

Managed install destination is the DisCo agent skills tree under the user home `.disco` directory. Export workflow `import-repo-skills-to-agent` copies selected graphs into Claude Code or Codex user-level skill directories.

**Domain fit vs Cemini.** AREX is an AutoML / paper-replication skill library (MLE-bench, PaperBench, FrontierCS, PassNet). Cemini already covers skill packaging via @entities/tools/book-to-skill.md (book corpus to Claude `SKILL.md`) and @entities/tools/skill-seekers.md (docs, repos, PDF to skills). Harness evolution is @entities/tools/starharness.md (stratified search, weights frozen, HITL). AREX does not replace those. It is a large third-party AutoML library, not a wiki-to-skill exporter and not a trading harness.

**Failure-mode audit (skill-library class).** Same class as SwarmVault / @entities/tools/agent-skill-manager.md: default skill destinations collide with mixed-repo federation sync.

| Check | Result |
|-------|--------|
| License | Apache-2.0 `[CONFIRMED]` — clears IP perimeter for REFERENCE |
| Skill layout | Nested `skills/repositories/repo-skills/<id>/` — not the Cursor per-skill `SKILL.md` layout |
| Default export | Claude Code and Codex user-level skill dirs — would pollute operator plus federation skill trees |
| Managed root | DisCo `.disco/agent/` tree — parallel skill root, not federation-compatible |
| Size | ~442MB — do not vendor |
| Installer | README documents a remote pipe installer — **never run**; no remote-pipe install, no prod copy |
| Unattended evolution | Creator can mint and refresh skills — HITL required; pairs SafeEvolve FILE on the hub |

**Verdict rationale.** **GO REFERENCE** (2026-09-04). License is clean. Repo is the paper companion and is active (push 2026-09-03). Pattern is useful as a citation for Repo-To-Skill. `harness_verb: FILE`. Do not Integrate. Do not run `disco repo-skills install`. Do not import into Claude, Cursor, or federation domain-sync skill directories. Laptop clone stays in `.local/adopts/`. Compare, do not copy, skill-router progressive-disclosure if CCC later designs a Cemini router.

## Snippets

> "An AREX Skill is a self-contained, agent-readable unit of operating knowledge. It uses the open Agent Skills format as its portable packaging convention, then adds the operating context an agent needs: when to use a capability, what to run, how to validate it, and how to recover when an experiment fails." [Source: VectorSpaceLab/AREX-Skill README.md (clone 2026-09-04)]

## Dead Ends

- Symlink AREX `repo-skills/` into federation skill sync — nested layout plus 1,000 roots would swamp Cursor and Claude skill discovery.
- Remote pipe installer for DisCo on the laptop or any Cemini host.
- Unattended DisCo Creator writes into Cursor skill dirs (StarHarness / SafeEvolve HITL gate).
