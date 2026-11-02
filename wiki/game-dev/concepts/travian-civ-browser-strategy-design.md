---
title: "Travian × Civilization browser strategy — design and feasibility"
type: concept
tags: [concept, design, browser, travian, strategy, feasibility]
keywords: [travian, civilization, single-player, browser game, utility ai, payback time]
related:
  - concepts/scope-tiers.md
  - concepts/vertical-slice-v0.md
  - concepts/indie-kingdom-builder-lessons.md
  - concepts/ai-assisted-game-dev-workflows.md
  - concepts/ai-game-dev-tool-stack-2026.md
  - concepts/agentic-npc-design-guardrails.md
  - concepts/stronghold-2-ai-lords.md
  - concepts/medieval-sim-fun-vs-accuracy.md
maturity: draft
created: 2026-11-02
updated: 2026-11-02
---

## Raw Concept

The question this page answers: **is a single-player, offline-first browser game that merges Travian T4's economy with Civilization Revolution's 3–6 hour pacing worth building, and what does our prior work say about how to build it?**

Inputs: a 90-page technical architecture specification for the game (local, 2026-11-02), three research passes (comparable games, 2026 tool stack, Travian/Civ strategy), the @entities/projects/castle-sim.md decision register and project log, the Basgiath design documents, and the pages in this wiki.

The long form is a local brief: `briefs/game-dev/2026-11-02_travian-civ-game-design-brief.docx` (gitignored). This page is the durable synthesis.

## Narrative

### Verdict

The market gap is real. The specified game is buildable. The specified **plan** is a two-year scope presented as four phases, and it would fail the same way our Stronghold clone failed — breadth before a recorded human "this is fun".

Three rules carry the decision:

1. Build one village, one tribe, one opponent first.
2. Make payback time the visible language of the economy.
3. Never punish absence; offline progress must be free, exact and previewable.

### 1. No commercial single-player Travian exists

Every commercial title in the lineage monetises time pressure: Travian Legends and Kingdoms score 1.6–1.8/5 on Trustpilot, Elvenar 1.6/5, and the genre's own comparison literature states that "every game in the genre is monetised on speed" [Source: https://nz.trustpilot.com/review/www.travian.com (retrieved 2026-11-02)].

The only direct competitor is **Pillage First! (Ask Questions Later)** — open source, browser, TypeScript/React, SQLite-WASM, AGPL-3.0, about 196 stars. It is in alpha, ships several releases a week, and has thin art and no campaign arc [Source: https://github.com/jurerotar/Pillage-First-Ask-Questions-Later (retrieved 2026-11-02)].

Its weakness is instructive: it simulates offline, but the FAQ admits that "we can't let the player know if they're under attack" [Source: https://pillagefirst.com/frequently-asked-questions (retrieved 2026-11-02)]. Catch-up simulation is fair for the player's own economy and hostile for incoming attacks. A complete campaign with no offline loss is the opening.

### 2. The endgame is the product

Travian's official design history shortens worlds to cut downtime; Tribal Wars players describe old worlds as "seas of grey & inactivity"; Grepolis endgames are "a cemetery of ghost cities". Against the Storm's designers give the cleanest rule: the best part of a city builder is the first two hours, so each run should **end as soon as victory is assured** [Source: https://www.polygon.com/videos/24058317/against-the-storm-city-builder-analysis/ (retrieved 2026-11-02)].

Implication: a 3–6 hour campaign with a real ending is not a compromise. It is the differentiator.

### 3. Expansion beats optimisation, and payback time proves it

Field production by level (x1): 3, 7, 13, 21, 31, 46, 70, 98, 140, 203, 280 per hour. Marginal payback rises from about 62 hours at level 0→1 to about 328 hours at 9→10. Bonus buildings add roughly +5% of base per level, so they pay only once fields are wide.

Official ROI guidance makes the same point at the top of the curve: Hero's Mansion 15→20 costs about 1.6 M for +2,625 crop/hr — a 607-hour payback — while a new village costs about 1.35 M for +16,800/hr — an 80-hour payback [Source: https://support.travian.com/en/articles/176-developpement-initial-retour-sur-investissement-roi (retrieved 2026-11-02)].

**Design use:** show "pays back in N hours" on every upgrade. It teaches the canonical build order without a tutorial, and it replaces the spreadsheet that Travian players keep on a second monitor.

### 4. The AI should be a greedy scheduler with a personality

Existing Travian bots are schedulers, not planners. Vangrd's farm optimiser ranks targets by YIELD = resources returned ÷ troops sent, tracks committed troops while waves are in flight, and adds jitter so intervals are not machine-perfect [Source: https://vangrd.bot/guides/farm-optimizer (retrieved 2026-11-02)].

Persona should be separate from competence:

| Axis | What it controls | Changes with difficulty? |
|---|---|---|
| Personality | Target priorities (economy, army, culture), risk tolerance, willingness to pact | No |
| Competence | Reaction delay, scouting thoroughness, queue idleness, candidates evaluated | Yes |

This is the same conclusion the Stronghold 2 material supports: readable AI with one signature and one exploitable weakness beats an AI that out-produces the player. Difficulty must not touch income.

### 5. Prior attempts: the toolchain works, breadth kills

Castle-sim reached a working economy, popularity, crime, ranks, markets and 60-plus automated tests in about a week. It was shelved. The useful half is the method:

- spike the largest unknown before features,
- one headless test scene per subsystem,
- decision register with revisit triggers,
- measure before optimising (flow fields were correctly deferred),
- an explicit cut list.

The harmful half is scope: "toy castle" became "personal Stronghold 2 clone" within a day, then 3D, popularity, honour, crime and feasts. Parity research against retail footage replaced a retail playtest. Automated tests proved correctness and never enjoyment.

Basgiath contributes the clearest rule: **one clip** that reads in two seconds on a phone, generated content rather than hand-built, stable APIs only, and a binary playtest checklist.

### 6. Tool stack: the specified renderer is a bet on one maintainer

The architecture spec recommends a 2D framework whose README labels itself "0.9, early development": seven GitHub stars, no stable release, effectively one maintainer, though genuinely active (commits on 2026-11-02, MCP package 0.28.0). Its headless-test and MCP ideas fit this game well [Source: https://github.com/debuffjp/debuff (retrieved 2026-11-02)].

| Layer | Verified choice |
|---|---|
| Renderer | Mature WebGL2 renderer (PixiJS 8.x); benchmark the young framework behind the same draw interface |
| Simulation | Renderer-free fixed-step integer loop at 20 Hz; plain typed-array structs, **no ECS** |
| RNG | pure-rand with per-system streams (`seedrandom` is dead since 2019) |
| Persistence | sqlite-wasm `opfs-sahpool` in one worker, Dexie fallback, `.sqlite` export; consider command-log saves |
| Tests | Vitest + fast-check + Playwright + pixelmatch; state-hash replay gate in CI |
| Agents | Playwright MCP and Chrome DevTools MCP |

The load-bearing rule is not the choice of renderer. It is that **the simulation owns no renderer types**, so every renderer stays replaceable.

### 7. Open questions before code

1. Session length: 3 hours or 6?
2. Villages per campaign: one, or three to five?
3. Battle agency: composition and timing only, or intervention during battle?
4. Map size: 900×900 is large for 6–8 opponents; 400×400 gives contact.
5. Art direction, before any asset is generated.
6. Target device: desktop only, or tablet?
7. Narration: story, or personalities only?
8. Distribution: itch.io, Steam wrapper, or self-hosted?

## Snippets

> "Whenever you open a game world, we simulate every event that would have taken place… we can't let the player know if they're under attack." [Source: https://pillagefirst.com/frequently-asked-questions (retrieved 2026-11-02)]

> "Every game in the genre is monetised on speed." [Source: https://riseofkingdomshandbook.com/guides/riseofkingdoms-games-like-rise-of-kingdoms (retrieved 2026-11-02)]

> "Same seed + commands = same match; saves are seed + command log." — Regnarium, a 30–45 minute browser 4X by a one-person studio [Source: https://muhammetsafak.com/labs/regnarium-lab/ (retrieved 2026-11-02)]

> "1) Pay for an advantage. 2) They nerf it. 3) Pay to regain the advantage. 4) Repeat." — Elvenar review, the clearest statement of why paid time is a trap [Source: https://ca.trustpilot.com/review/elvenar.com (retrieved 2026-11-02)]

## Dead Ends

- **ECS libraries for this game.** bitECS is near-dormant under one maintainer, miniplex is explicitly unmaintained, becsy is dormant, thyseus is pre-1.0. A 900×900 terrain is static data, and determinism is easier with ordered systems over plain structs.
- **`seedrandom`, `absurd-sql`, `localForage`.** Dead since 2019, 2023 and 2021.
- **Multi-tab SQLite over OPFS.** `opfs-sahpool` is single-tab by design; multi-tab needs COOP/COEP and a different VFS.
- **Building the specification's Phase 1–4 in order at full size.** Six warlords, three zoom tiers and a three-phase crisis before a human has finished Act I is the castle-sim failure repeated with better maths.
- **Retail footage as a substitute for play.** Comparing to YouTube is not a playtest; feel cannot be inferred from video.
