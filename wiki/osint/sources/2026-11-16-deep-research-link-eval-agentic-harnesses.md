---
title: "Deep Research link evaluation — agentic harnesses, MCP browser automation, Jev workflows (2026-11-16)"
type: source
related:
  - concepts/agent-link-evaluation-gates-v1013.md
  - entities/tools/chrome-devtools-mcp.md
  - entities/tools/neo4jev.md
  - "@ccc-wiki/entities/tools/plannotator.md"
  - "@ccc-wiki/entities/tools/ag-ui.md"
  - "@ccc-wiki/entities/tools/univer.md"
  - "@ccc-wiki/entities/tools/jev-recipes.md"
  - sources/2026-11-16-deep-research-link-eval-game-media.md
  - @ccc-wiki/entities/tools/product-engineering-skills.md
  - @cybersecurity-wiki/entities/tools/claude-bughunter.md
  - @cybersecurity-wiki/entities/tools/wrapvm.md
  - @image-gen-wiki/entities/tools/claude-video.md
  - sources/2026-11-17-deep-research-link-eval-design-motion-harness.md
  - "@ccc-wiki/entities/stitch-skills.md"
  - "@game-dev-wiki/entities/modern-web-guidance.md"
updated: 2026-11-24
---

## Raw Concept

- **Title:** Cemini Multi-Wiki Link Evaluation (batch A)
- **Author:** Deep Research evaluation run, operator-supplied rubric v10.13
- **Type:** vendor-link evaluation report (DOCX)
- **Location:** `cemini-egress-fi:/opt/cemini-bulk/research/osint/Cemini Multi-Wiki Link Evaluation.docx`
- **Retrieved:** 2026-11-16
- **Pages:** 20 URL records
- **Read status:** read

Batch theme: agentic harnesses, MCP browser and UI automation, Jev typed decision
workflows, and offensive/defensive security skills.

## Narrative

Twenty URLs were graded against the shipped stacks under rubric v10.13. The rubric
caps the batch at two winners. This run graded **14 winners** — 3 Integrate and 11
Extract — which breaks the stated budget. Treat the tiers as evidence, not as an
approved work order: the gates in
`@concepts/agent-link-evaluation-gates-v1013.md` decide what ships.

### Graded outcomes

| Tier | Count | Items |
|------|-------|-------|
| Integrate | 3 | `plannotator`, `modern-web-guidance-src`, `chrome-devtools-mcp` |
| Extract | 11 | `univer`, `ag-ui`, `stitch-skills`, `Claude-BugHunter`, `sub-agents` docs, `jev-recipes`, `aitmpl/senior-frontend`, `claude-video`, `product-engineering`, `wrapvm`, `neo4jev` |
| Context | 2 | `lazydsh`, `agent-hud-open` |
| Watch | 2 | `learn-agent`, `EquationGroup` |
| Pass | 2 | `phoneuse`, `copybook.page` |

### Findings that survived our own Phase-0

Three claims in the report did not survive a direct check:

- **`tobi/wrapvm` is graded Extract with a license gate of "NOT FOUND".** Direct
  check on 2026-11-16 confirms the repository root holds no `LICENSE`, `LICENSE.md`,
  `LICENSE.txt`, or `COPYING` file, and the GitHub API reports no SPDX id. All rights
  are reserved by default. The item fails the permissive-license gate.
  [CONFIRMED]
- **`neo4jev` needs a remote `system_one` call on every hop.** This was already
  recorded on @entities/tools/neo4jev.md from the 2026-11-11 batch. The report lists
  it as Extract without repeating the cloud dependency. It fails the local-first gate.
  [CONFIRMED]
- **`chrome-devtools-mcp` is graded Integrate for game-time, but game-time already
  ships Playwright** (`packages/client/playwright.config.ts`, `e2e/shell.spec.ts`).
  Playwright is a test runner; the MCP exposes CDP to an agent at run time. The two
  overlap less than the shared dependency suggests, but the gap is narrower than
  stated. [CONFIRMED — local repository check 2026-11-16]

### Where each winner routes

- **CCC wiki** — `univer`, `ag-ui`, `plannotator`, `stitch-skills`,
  `modern-web-guidance-src`, `chrome-devtools-mcp`, `jev-recipes`, `product-engineering`.
- **Cybersec wiki** — `Claude-BugHunter`, `wrapvm`.
- **Image-gen wiki** — `claude-video`, `stitch-skills`.
- **Game-dev wiki** — `stitch-skills`, `chrome-devtools-mcp`, `modern-web-guidance-src`.
- **OSINT wiki** — `neo4jev` (already held here).

### License position

Every surviving item is permissive: Apache-2.0 for `univer`, `plannotator`,
`stitch-skills`, `modern-web-guidance-src`, and `chrome-devtools-mcp`; MIT for
`ag-ui`, `jev-recipes`, `aitmpl/senior-frontend`, `claude-video`,
`product-engineering`, and `neo4jev`. `Claude-BugHunter` splits MIT code from
CC-BY-4.0 prose. `code.claude.com/docs/en/sub-agents` is product documentation, not
redistributable code.

`univer` carries a commercial boundary: the open-source `@univerjs/*`, `univer-cli`,
and `univer-sdk-skills` packages are Apache-2.0, but the Pro plugins, Server SDK, and
exchange servers need a separate commercial licence. Extraction must stay inside the
open-source packages.

## Snippets

> License: NOT FOUND (no LICENSE file detected in repository) — `tobi/wrapvm`
> [Source: Cemini Multi-Wiki Link Evaluation.docx, URL 19]

> Apache-2.0 for open-source `@univerjs/*`, `univer-cli`, and `univer-sdk-skills`;
> commercial Pro plugins (`@univerjs-pro/*`), Server SDK, and exchange servers require
> separate commercial licensing.
> [Source: Cemini Multi-Wiki Link Evaluation.docx, URL 1]

## Dead Ends

- **Trusting the report's license line for a repository that ships no licence.** The
  report marked `wrapvm` "friction only" while recording "NOT FOUND". Absence of a
  licence is a hard stop, not friction. Check the repository root.
- **Reading "Integrate" as approval to install.** The v10.13 Workstation Harness
  Freeze blocks new local hooks, skills, and MCP servers regardless of tier.
