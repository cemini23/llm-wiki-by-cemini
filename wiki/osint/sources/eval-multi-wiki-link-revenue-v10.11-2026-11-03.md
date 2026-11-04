---
title: Multi-Wiki Link Revenue Evaluation v10.11 — 20 URLs (2026-11-03)
type: source
tags: [source, eval, tool-evaluation, revenue-lens]
keywords: [multi-wiki link evaluation, runtime v10.11, phase-0, game-time, agent-desktop, theatre, desloppify]
related:
  - entities/tools/agent-desktop.md
  - entities/tools/theatre.md
  - entities/tools/svgjs.md
  - entities/tools/desloppify.md
  - entities/tools/scenario-labs-skills.md
  - entities/tools/webmcp.md
  - sources/eval-multi-wiki-link-revenue-v10.10-batch-c-2026-11-02.md
  - sources/arxiv-v10-11-skipped-no-lane-2026-11-03.md
  - "@game-dev-wiki/sources/travian-civ-game-design-brief-2026-11-02.md"
maturity: draft
created: 2026-11-03
updated: 2026-11-03
read_status: read
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Cemini Multi-Wiki Link Evaluation — Runtime v10.11 |
| Type | Generated evaluation report, agent-authored and cited |
| Received | 2026-11-03 |
| Inbox | `research to be indexed/Multi-Wiki Link Revenue Evaluation.docx` |
| Batch | 20 URLs, none deferred |
| Lens | revenue plus project fit |

**The version number advanced.** Three previous batches all carried "v10.10"; this one is v10.11. That is the first reliable batch marker since 2026-10-25.

**The priority stack changed.** It now reads: **#1 Atto + Collectibles + Game-Time (co-equal)**, #2 CeminiDFS + CeminiParlays, #3 GuruWatcher + Basgiath. Game-Time is new at the top, and GuruWatcher dropped from #2 to #3.

## Narrative

### Tier table

| # | Tool | Tier | Primary wiki | Project fit | License (verified) |
|---|------|------|--------------|-------------|--------------------|
| 1 | Humpalumps/Ultra-Water | Context | Game-dev | none | MIT |
| 2 | opentoonz/opentoonz | Context | Image-gen | none | BSD-3 |
| 3 | friction2d/friction | Context | Image-gen | none | GPL-3.0 |
| 4 | freemocap/freemocap | Context | Game-dev | none | AGPL-3.0 |
| 5 | NatronGitHub/Natron | Context | Image-gen | none | GPL-2.0+ |
| 6 | synfig/synfig | Context | Image-gen | none | GPL-3.0 |
| 7 | effekseer/Effekseer | **Extract** | Game-dev | game-time | MIT |
| 8 | theatre-js/theatre | **Extract** | Game-dev | game-time | Apache-2.0 core / AGPL-3.0 studio |
| 9 | pencil2d/pencil | Pass | Image-gen | none | GPL-2.0 |
| 10 | AcademySoftwareFoundation/openvdb | Context | Game-dev | none | Apache-2.0 |
| 11 | svgdotjs/svg.js | **Extract** | Game-dev | game-time, atto | MIT |
| 12 | webmcp.com | **Extract** | CCC | atto, local-abliterated-lab | n/a (W3C spec) |
| 13 | textjs.org | Context | CCC | none | not found |
| 14 | vercel-labs/agent-desktop | **Integrate** | CCC | collectibles, game-time, atto | Apache-2.0 |
| 15 | vercel-labs/wterm | Context | CCC | none | Apache-2.0 |
| 16 | scenario-labs/skills | **Extract** | Image-gen | game-time, basgiath, collectibles | MIT |
| 17 | peteromallet/desloppify | **Extract** | CCC | game-time, atto, collectibles | **custom, not OSI** |
| 18 | earendil-works/djs | Watch | CCC | game-time | not found |
| 19 | anthropics/FlashProve | Context | Cybersec | none | not found |
| 20 | recepkutuk/canon | Pass | CCC | none | not found |

Tally: 1 Integrate, 6 Extract, 1 Watch, 10 Context, 2 Pass, 0 unavailable.

### The batch is mostly about one project that does not exist yet

**Seven of the twenty URLs route to `/Users/claudiobarone/Projects/game-time`, and that directory does not exist.** Neither does any `game-time` working copy under `~/Projects`. The highest-count target in this batch is a project that has been named but not created.

That is not a defect in the report. It is the report doing its job early. But it reframes every game-time routing: these are **launch inventory for a project at day zero**, not improvements to a running system.

What game-time is comes from the three Travian documents that arrived in the same inbox — see @game-dev-wiki/sources/travian-civ-game-design-brief-2026-11-02.md. A single-player, offline-first browser strategy game that keeps Travian T4's economy and siege mathematics, replaces the 250–300-day server clock with a warp-to-next-event clock, and substitutes Civilization Revolution-style AI warlords for human rivals. Target session 3–6 hours, TypeScript, SQLite-WASM on OPFS.

### Phase-0, 2026-11-03

GitHub egress is denied in the sandbox. Checks used package manifests and repository pages via web fetch.

| Tool | Report claim | Phase-0 finding | Effect |
|------|--------------|-----------------|--------|
| theatre-js/theatre | "Apache-2.0 for @theatre/core (shipped bundle); AGPL-3.0 for @theatre/studio (design/dev editor only)" | Confirmed exactly. `@theatre/core` `package.json` declares `"license": "Apache-2.0"`, version **0.7.0**. | **Clean, conditional on discipline.** Ship `@theatre/core` only. Any AGPL code reaching a shipped bundle is a problem. That separation must be enforced by the build, not by habit. |
| peteromallet/desloppify | "Custom license (free for any individual developer working independently or at a company for their own work, an…" | **Custom, not an OSI licence.** Free for individuals and for open-source companies, including commercial use. **For-profit closed-source companies that commercialise it are directed to the LICENSE file for pricing.** 4.0k stars, 919 commits, state in `.desloppify/`. | **The recommendation outruns the licence.** Extracting the scan → triage → queue *pattern* is fine. Running the tool inside a commercial Atto or Collectibles is a licensing question with a price attached. Do not treat it as free tooling. |
| scenario-labs/skills | "baseline-plus-delta prompt architecture + Grid Maker sprite sheets … automated Quality Gate grading … pre-spend cost-estimation" | **MIT confirmed.** But every generation skill requires **Scenario's MCP server** (`mcp.scenario.com`), an account or API key, and **"Creative Unit" credits**. The pre-spend cost estimation is cost estimation for *Scenario credits*. | **The cost gate is vendor-scoped.** Adopt the *pattern* — baseline+delta consistency, Grid Maker sheets, a pre-spend check — without adopting the dependency. For Collectibles, sending card images to a third-party generation cloud crosses the local-first boundary. |
| vercel-labs/agent-desktop | Integrate; "cuts GUI automation token spend by 78%–96%" | Apache-2.0. Already catalogued as Extract in v10.10 batch C. No new licence fact. The 78–96% figure is the report's own measurement, not a vendor benchmark. | Tier moved Extract → Integrate with **no independent evidence for the number**. See @entities/tools/agent-desktop.md. |
| earendil-works/djs | Watch — "18-hour prototype maturity, empty README, missing license file" | The report's own blockers are the correct ones. | Watch is right. Nothing to add. |

### What is actually worth doing

1. **agent-desktop** — the one Integrate, and the only item that changes how the operator works today rather than how a future project will be built.
2. **theatre core + svg.js** — two permissively-licensed runtime libraries for animation and SVG geometry. Small, clean, and both relevant to game-time's map and UI layer.
3. **The desloppify *pattern*** — scan, triage, and a persistent execution queue with blind scoring. Copy the loop shape. Pay for the tool only if a commercial use needs it.
4. **webmcp** — declaring read-only WebMCP tools on Atto's public portal. This is the same "agent discoverability" thread as @entities/tools/agentdiscoverability-track.md from v10.10 batch C, now with a concrete registration directory.

### What to leave alone

- **scenario-labs/skills** as a dependency. The pattern transfers; the vendor cloud does not fit the local-first boundary.
- **The nine image/video/animation Context entries** (Ultra-Water, opentoonz, friction, freemocap, Natron, synfig, openvdb, textjs, wterm). Catalogued so they are not re-evaluated; no action.
- **FlashProve** — Anthropic Frontier Red Team provable-inference prototype. Interesting, no route.

## Snippets

> "Primary lens: revenue + project fit; Priority #1 = Atto + Collectibles + Game-Time (co-equal); #2 = CeminiDFS + CeminiParlays; #3 = GuruWatcher + Basgiath (Minecraft); then wikis always; poker + TipDrop retired" — report header

> "scenario-labs/skills (/Users/claudiobarone/Projects/game-time baseline-plus-delta sprite consistency, Grid Maker sheets, pre-spend cost gate, and Quality Gate asset analysis)" — report, aggregate

> Desloppify is "free for any individual — whether working independently or at a company — to use for their own work", and "for open source companies to use in any capacity, including commercial". For-profit, closed-source companies are pointed to the LICENSE file for pricing. [repository page, fetched 2026-11-03]

> `@theatre/core` `package.json`: `"license": "Apache-2.0"`, version `0.7.0`. [fetched 2026-11-03]

## Dead Ends

- **Treating game-time as an existing project.** It has no directory. Every routing to it is launch inventory.
- **Reading desloppify as free tooling.** It is free for individuals; commercial closed-source use has a price.
- **Assuming the agent-desktop 78–96% figure is measured independently.** It is the report's own number.
