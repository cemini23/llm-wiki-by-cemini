---
title: "Multi-wiki revenue evaluation — 20 rows: Bedrock ecosystem, server tooling, agent runtimes (2026-10-06)"
type: source
tags: [source, k283, basgiath, minecraft, bedrock, eval, game-dev]
keywords: [k283, bedrock, mcpedl, curseforge, void-proxy, mc-mod-migrator, bedrock-ui-animations, simple-money, just-clock, books-bedrock, centralino]
related:
  - concepts/k283-eval-wave.md
  - concepts/k282-level-editors-wave.md
  - concepts/k281-basgiath-wave.md
  - concepts/active-project-research-routing.md
  - entities/tools/centralino-ai-studio-medico.md
  - entities/tools/mc-mod-migrator.md
  - entities/tools/void-minecraft-proxy.md
  - entities/tools/bedrock-ui-animations.md
  - entities/tools/simple-money-minecraft-bedrock-addon.md
maturity: draft
created: 2026-10-06
updated: 2026-10-06
read_status: read
---

## Relations

- @concepts/k283-eval-wave.md
- @concepts/k282-level-editors-wave.md
- @concepts/k281-basgiath-wave.md
- @concepts/active-project-research-routing.md

## Raw Concept

| File | `GitHub Revenue Opportunity Evaluation.docx` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/GitHub Revenue Opportunity Evaluation.docx` |
| Retrieved | 2026-10-06 |
| Dual-ID | **OSINT K283** |
| Batch theme | Minecraft Bedrock add-on architecture, dedicated server infrastructure, agent runtimes |
| Rows | 20 URLs |
| sha256 | `0c413e7b342e211c…` |

## Narrative

A 20-row eval batch. **13 of 20 rows route to Basgiath** — the Minecraft Bedrock fan project. This is the third Bedrock-facing wave in four days (K281, K282, K283). The eval ran the v10.7 prompt: every row scores `basgiath` overlap.

### Tier spread

| Tier | Count |
|------|-------|
| Integrate | 0 |
| Extract | 9 |
| Context | 7 |
| Pass | 4 |
| UNAVAILABLE | 0 |

### The Extract rows (9)

| URL | Technique | Basgiath overlap |
|-----|-----------|------------------|
| `Flower7C3/simple-money-minecraft-bedrock-addon` | Turnkey in-game currency: coin tiers, paper bills, crafting conversion, an ATM block. Packaged `.mcaddon` | 0.80 |
| `tfgh6/bedrock-ui-animations` | JSON UI easing curves, smooth progress-bar interpolation, transition keyframes | 0.85 |
| `Flower7C3/books-minecraft-bedrock-addon` | Readable custom books and lore-item schemas (no vanilla book-and-quill limit) | 0.75 |
| `kongbai9288/mc-mod-migrator` | Automated add-on schema migration across Bedrock engine updates | 0.70 |
| `void-community/Void` (see note) | Modern .NET 10 async packet-routing proxy with Docker/K8s; multi-world scaling | 0.75 |
| `Flower7C3/just-clock-minecraft-bedrock-addon` | On-screen HUD clock with mcfunction hooks, no experimental flags | 0.60 |
| `taixingbi/eval-bedrock-runtime-benchmark` | TTFT / cold-start latency benchmarking for model runtimes | (→ CCC) |
| `JeroenPieksma/claude-computer` | Vision-guided desktop automation via Claude Computer Use API | (→ CCC/cyber) |
| `albeSavvy/centralino-ai-studio-medico` | Italian telephony intent triage and dialogue routing | (→ **Atto**) |

### The Atto row (highest value)

`albeSavvy/centralino-ai-studio-medico` is a **medical-clinic phone switchboard**, but its core is an Italian-language voice/intent-routing pipeline. Scores `atto overlap 0.70`. The play: reuse Italian intent classification and appointment/inquiry patterns to triage *stato civile* / comune inquiries for Atto Concierge cases. The eval estimates 5-10 operator hours saved per case. **Privacy perimeter hits hard: client genealogical PII must never reach a third-party telephony model without a human gate.**

### The Context rows (7)

`LumaBerry13/behemoth` (boss entity mechanics), `Chlna6666/Better-Minecraft-Bedrock-Launcher` (multi-version test launcher), `Adarshstar/blaze-server-backup` (server backup automation), `leandrooryan/homed-wiki` (MkDocs gaming docs), `csgonovicecss/CS16MC` (competitive round-reset reference), `zhuzijiang/mc-server-deploy` (containerised server deploy), `JCzypie/JCtex` (texture pack structures).

### What was rejected (4 Pass)

`abdul200200-netizen/personal-ai-agent` (generic assistant, no fit), `roma234567/AUTOCLICKER` (**violates the manual-operator safety gate** — no unattended clickers), `PLANETA9091/privateB` (empty/unverifiable), `tfgh6/bedrock-ui-animations` (duplicate of URL 13).

### Implementation note — the Void URL is wrong

The docx names `github.com/void-community/Void`, but its own "works cited" resolves the real project to `github.com/caunt/Void` (MIT, ~26 stars, "Minecraft Proxy for Modded Servers"). Treat `void-community/Void` as a likely dead/incorrect URL; the technique (a modern proxy for modded servers) is real, and **the proxy is a Java-edition tool** — it does not proxy Bedrock Dedicated Server. Bedrock has no equivalent BungeeCord-style proxy in this batch. **This is a goal-match / stack-mismatch Pass-in-disguise** (same pattern as K282's `FabricModdingConventions`).

### License notes

- `void-community/Void` / `caunt/Void` → MIT (real repo).
- `Flower7C3/simple-money` → MIT (stated).
- All other 18 rows → `NOT FOUND`. Unverified.

### Eval-quality warning

**17 of 20 rows show `NOT FOUND` for stars / last-commit / issues.** Stack strings are mostly `CLAIMED (unverified)`. URL 20 is an exact duplicate of URL 13 — the batch list is partly generated, the same signal K281 (7/20 dead) and K282 (6/20 dead) showed. Score the *technique* the row names. Do not trust the row's metrics.

### Boundary

**Zero clones (bash has no network). Nothing vendored. 0 product Integrate GO.** Basgiath stays free and non-monetized: no Minecraft Marketplace, no official art or book text, "fan-made" labels. The virtual-currency row must stay **in-game roleplay tokens only** — no real-money, no paid perks.

### Distribution

- Bedrock HUD / currency / books / migration rows → `../Game Dev wiki/briefs/2026-10-06_k283-bedrock-addons-from-osint.md`
- Basgiath-facing extracts → `Projects/dragon-rider-map/briefs/2026-10-06_k283-basgiath-extracts.md`
- Atto telephony row → `../atto/briefs/2026-10-06_k283-italian-telephony-intake.md`
- CCC rows → `../Cemini claude code CCC/briefs/2026-10-06_k283-agent-harness.md`
- Texture row → `../Image gen/briefs/2026-10-06_k283-bedrock-textures.md`

## Snippets

> "The addon implements an end-to-end virtual economy system complete with custom blocks and balanced item conversion logic. Purely virtual in-game currencies satisfy all Basgiath non-monetization constraints." [Source: GitHub Revenue Opportunity Evaluation.docx]

> "Fluid UI animations distinguish standard fan creations from professional community maps." [Source: GitHub Revenue Opportunity Evaluation.docx]

> "Rapid version updates from Mojang frequently deprecate entity components and JSON UI tags, creating ongoing maintenance overhead for complex add-ons." [Source: GitHub Revenue Opportunity Evaluation.docx]

> "Although originally engineered for medical clinics, the core Italian voice and intent routing pipelines address a critical bottleneck in Atto's premium concierge operations." [Source: GitHub Revenue Opportunity Evaluation.docx]
