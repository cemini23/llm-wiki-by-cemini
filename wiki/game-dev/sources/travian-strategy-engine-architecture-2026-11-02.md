---
title: "Travian Strategy Engine architecture — T4 economy, siege maths, event-warp clock"
type: source
tags: [source, game-design, architecture, travian, simulation, typescript]
related:
  - sources/travian-civ-game-design-brief-2026-11-02.md
  - sources/travian-civ-deep-research-report-2026-11-02.md
  - concepts/travian-civ-browser-strategy-design.md
maturity: draft
read_status: skimmed
created: 2026-11-03
updated: 2026-11-03
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Technical Architecture and Mathematical Specification for a Single-Player Browser Strategy Engine (Travian T4 × Civilization Revolution) |
| Date | 2026-11-02 |
| Inbox | `Travian Strategy Engine Architecture.docx` |
| Words | 8,283 |
| Read status | skimmed — section headings and opening |

The specification the design brief critiques. It is the technical half of the game-time concept.

## Narrative

### The problem it states

Travian's depth comes from three coupled systems: interlocking exponential resource curves, asymmetric tribal logistics, and deterministic siege mathematics. Its commercial implementation couples those to a **250–300-day real-time server clock**, punitive offline vulnerability, and HTML tables that hide spatial warfare behind countdown timers.

Civilization Revolution showed the opposite is possible: a grand-strategy loop compressed into a **3–6 hour single-player session**, carried by AI personalities and visible territory.

The specification's job is to decouple Travian's mathematics from its wall clock.

### Structure

**Section 2 — the canonical model.**

| § | Content |
|---|---------|
| 2.1 | Resource production, oases, enhancers, storage curves |
| 2.2 | Building cost, construction time, queue mechanics |
| 2.3 | Asymmetric tribe matrices — Romans, Gauls, Teutons |
| 2.4 | Combat resolution, siege, and conquest mathematics |
| 2.5 | Culture points and imperial expansion |
| 2.6 | Core deterministic TypeScript simulation data structures |

**Section 3 — the invention.** Two pieces carry the design:

- **3.1 Analytical event-warp clock.** The mechanism that replaces real-time waiting. This is the single most load-bearing idea in the document and the one the design brief calls excellent.
- **3.2 AI warlord utility and state machine architecture.** How the Civilization-style opponents are modelled as utility maximisers over state.

**Section 4 — the client.**

- **4.1** 2D/2.5D web renderer comparison and semantic-zoom architecture, including Phaser 4 and a licence and policy gate.
- **4.2** Client-side persistence and Web Worker simulation architecture.

### Why the split matters

The document separates **deterministic simulation** from **presentation**. That is the right architecture for this game specifically, because the event-warp clock means the simulation must be able to advance by arbitrary amounts without a renderer running. If the economy lived in the render loop, warping would be impossible to implement correctly.

The same split makes headless testing possible, which is what the castle-sim precedent demonstrated — a working economy plus sixty automated tests.

### The caveat on this page

Only the shape was read, not the derivations. The siege formulas, the storage curves, and the event-warp mathematics are unverified here. Do not cite a formula from this page.

What the design brief says about the document as a whole is recorded at @sources/travian-civ-game-design-brief-2026-11-02.md, and it is not a compliment: the maths is sound and the build plan is two years long.

## Snippets

> "Merging these two paradigms into a standalone, offline-first browser strategy engine requires decoupling Travian's canonical mathematical engine from real-time wall-clock…" — §1

> "Classic real-time browser strategy games of the Travian (T3.6 and T4 Legends) lineage achieved enduring strategic depth by coupling interlocking exponential resource curves, asymmetric tribal logistics, and deterministic siege mathematics." — §1

## Dead Ends

- **Reading this as a build plan.** The companion brief's central argument is that it is a two-year scope dressed as four phases.
- **Citing formulas from this page.** Only headings were read.
