---
title: "Link evaluation gates v10.13 — how a graded URL becomes a queued item"
type: concept
related:
  - sources/2026-11-16-deep-research-link-eval-agentic-harnesses.md
  - sources/2026-11-16-deep-research-link-eval-game-media.md
  - entities/tools/chrome-devtools-mcp.md
  - entities/tools/neo4jev.md
  - @ccc-wiki/entities/tools/ag-ui.md
  - @ccc-wiki/entities/tools/jev-recipes.md
  - @ccc-wiki/entities/tools/plannotator.md
  - @ccc-wiki/entities/tools/product-engineering-skills.md
  - @ccc-wiki/entities/tools/univer.md
  - @game-dev-wiki/entities/tools/estella.md
  - @game-dev-wiki/entities/tools/ffmpeg-skill.md
  - @cybersecurity-wiki/entities/tools/claude-bughunter.md
  - @cybersecurity-wiki/entities/tools/wrapvm.md
  - @image-gen-wiki/entities/tools/claude-video.md
updated: 2026-11-16
---

## Raw Concept

The question this page answers: **when an evaluation report grades a URL Integrate or
Extract, what else must be true before the item enters a project upgrade queue?**

Raised by the two 2026-11-16 Deep Research batches, which together graded 16 winners
out of 40 URLs.

## Narrative

The evaluation report is evidence. It is not an approval. Four gates stand between a
tier and a queued item.

### Gate 1 — permissive licence

The repository must carry an SPDX-recognised permissive licence in its root, or the
page must be documentation rather than redistributable code.

Absence of a licence is not friction; it is a stop. Default copyright reserves all
rights, so no code may be copied or bundled. Check the repository root and the GitHub
licence API together — a tracker snapshot can disagree with both.

Split licences pass per item: `Claude-BugHunter` ships MIT code and CC-BY-4.0 prose,
which is fine as long as each extract respects its own terms. A commercial add-on tier
also passes, provided the extraction stays inside the open-source packages, as with
`univer`.

### Gate 2 — local-first execution

The item must work without a mandatory cloud call.

This gate fails items that look local and are not. `neo4jev` reads like an offline Jev
replica but calls a remote `system_one` service on every hop. `claude-video` runs
locally by default and silently uploads to the Gemini Files API when an API key is
present — the normal state on this machine.

The test is mechanical: run the feature with the network blocked and confirm it still
answers.

### Gate 3 — Workstation Harness Freeze

No new local Claude Code hooks, skills, plugins, or MCP routers may be staged during
the freeze. A grade of Integrate does not lift this gate.

Items that act only as reference architecture survive as wiki pages. Items that need
installation wait.

### Gate 4 — the gap must still be open

The claimed gap must not already be solved in the local project repository. Check the
repository, not the report.

Two checks from 2026-11-16 show why:

- game-time already ships Playwright under `packages/client/`, which narrows — but does
  not close — the `chrome-devtools-mcp` gap.
- collectibles holds `consignment_manifest.py`, `grade_calc.py`, and
  `grading_dry_run.py`, so the spreadsheet *math* exists and only the *review surface*
  is missing for `univer`.

A gap that cannot be checked is not a gap. When a project repository is absent from the
machine — as `local-abliterated-lab` is — the item cannot be queued, whatever its tier.

### What survives all four gates

A surviving item enters one living queue file per project,
`briefs/<project>-upgrade-queue.md`, ranked by return on effort. Never a per-URL brief.

| Outcome | Queue entry |
|---------|-------------|
| All four gates pass | Yes, ranked |
| Licence fails | No — wiki Context note only |
| Cloud dependency mandatory | No — wiki Context note only |
| Freeze blocks installation | No — wiki reference page only |
| Gap already solved | No — wiki note, or drop |
| Repository absent | No — blocked until the repository exists |

## Snippets

> Actionable budget: Max 2 URLs total across this batch may earn Integrate or Extract;
> all others default to Context / Watch / Pass.
> [Source: Cemini Multi-Wiki Link Evaluation.docx, research plan]

## Dead Ends

- **Treating the tier as the decision.** The report grades on merit against the stack,
  not on licence, locality, or freeze state. Two of sixteen winners failed a gate.
- **Reading "NOT FOUND" as a soft warning.** For a licence it is a hard stop.
