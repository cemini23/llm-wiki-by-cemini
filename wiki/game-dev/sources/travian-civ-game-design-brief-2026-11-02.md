---
title: "Travian × Civilization design brief — the critique of a two-year spec"
type: source
tags: [source, game-design, travian, civ, game-time, scope, risk]
related:
  - sources/travian-strategy-engine-architecture-2026-11-02.md
  - sources/travian-civ-deep-research-report-2026-11-02.md
  - concepts/travian-civ-browser-strategy-design.md
  - "@osint-wiki/sources/eval-multi-wiki-link-revenue-v10.11-2026-11-03.md"
maturity: draft
read_status: skimmed
created: 2026-11-03
updated: 2026-11-03
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Travian × Civilization — Design, research and risk context |
| Prepared for | Gemini, as design and risk context for the strategy engine architecture |
| Prepared by | Cemini research workspace |
| Date | 2026-11-02 |
| Companion | Travian Strategy Engine Architecture (technical specification) |
| Inbox | `2026-11-02_travian-civ-game-design-brief.docx` |
| Words | 7,344 |
| Read status | skimmed — executive summary and section headings |

**This is the document that names the project.** The v10.11 eval routes seven tools to `/Users/claudiobarone/Projects/game-time`, a directory that does not exist. This brief and its two companions are what game-time is meant to be.

## Narrative

### The thesis

A single-player Travian does not exist commercially. Every game in the lineage sells time pressure; a version that does not is a different product, not a clone. The brief treats that as the market gap and the whole reason to build.

### The critique — and this is the useful part

The brief is written *about* its own companion specification, and it does not flatter it.

| Finding | What it says |
|---------|--------------|
| **The spec is a finished game, not a first milestone** | Six warlords, three zoom tiers, artefacts, coalitions, a three-phase endgame crisis. "A two-year scope presented as four phases." |
| **The recommended renderer is pre-1.0** | An unproven dependency under a project that is already long. |
| **Clean-room parity is a trap when taken first** | Reproducing Travian's exact numbers before having a game is fidelity as procrastination. |
| **A mathematical specification is not a game** | Correct siege formulas do not produce a session a person wants to finish. |
| **The AI is the hardest part and is scheduled last** | The thing that makes the premise work is the thing deferred furthest. |

That last point is the sharpest. The entire pitch rests on AI warlords with faces, personalities, and diplomacy. Scheduling them last means the risk lands at the end, after everything else is built.

### What it draws on

Two prior Cemini projects are cited as evidence for both halves of the argument:

- **castle-sim** — a Godot Stronghold 2 clone, June–July 2026. Reached a working economy plus sixty automated tests in a short window. Scope stayed legible, with a decision register in `PROJECT_LOG.md`.
- **Basgiath** — a Minecraft Bedrock addon, 2026. Scope inflated through fidelity.

The brief extracts "rules that survived both projects" and states them as practice. The contrast is the point: one project held scope, the other did not, and the difference was fidelity pressure.

### Market sections

- **5.1 The Travian lineage: the defect is the product.** The waiting *is* the design in commercial Travian. Removing it changes the genre.
- **5.2 The direct competitor** — an unfinished open-source alpha, and the only direct one.
- **5.3 Short-session strategy games.** What makes compression work; cites 30-turn / 30–60-minute designs.
- **5.4 The closest technical twin.**
- **5.5 Player sentiment on offline progress.**
- **5.6 Eight lessons that transfer directly.**

### Technical sections

Renderer comparison (Phaser 4.2 among them, with a licence gate), simulation/state/AI, and persistence. The companion architecture document carries the detail.

### What this page is for

If game-time is started, this brief is the first thing to re-read, because it is the only document in the set arguing *against* the other two. The architecture document specifies the game; this one says the specification is too large to build as written.

## Snippets

> "The market gap is real. No commercial single-player Travian exists. The only direct competitor is an unfinished open-source alpha. Every commercial game in the lineage sells time pressure — which means a game that does not is a genuine product, not a clone." — executive summary

> "The attached specification is technically strong and strategically premature. Its maths, licence discipline and event-warp clock are excellent. Its build plan describes a finished game: six warlords, three zoom tiers, artefacts, coalitions, a three-phase endgame crisis. That is a two-year scope presented as four phases." — executive summary

## Dead Ends

- **Building the specification top to bottom.** The brief's own argument is that this is the failure mode, and that the AI — the reason the game exists — ends up last.
