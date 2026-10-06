---
title: K283 Eval Wave — GitHub repos + Bedrock ecosystem (Oct 2026)
type: concept
tags: [k283, eval, agent-harness, local-rag, bedrock, basgiath, minecraft, ccc]
keywords: [k283, open-notebook, tester-army-e2e, agency-agents, ralph-claude-code, background-agents, hotpath-rs, keyed-lock, simple-money, bedrock-ui-animations, mc-mod-migrator, centralino]
related:
  - concepts/k282-level-editors-wave.md
  - concepts/k281-basgiath-wave.md
  - concepts/k283-arxiv-wave.md
  - concepts/k283-feeds-wave.md
  - concepts/active-project-research-routing.md
  - sources/eval-github-repos-dev-tools-2026-10-06.md
  - sources/eval-bedrock-ecosystem-2026-10-06.md
  - entities/tools/open-notebook.md
  - entities/tools/tester-army-e2e.md
  - entities/tools/agency-agents.md
  - entities/tools/ralph-claude-code.md
  - entities/tools/background-agents.md
  - entities/tools/keyed-lock.md
  - entities/tools/hotpath-rs.md
  - entities/tools/deepgemm.md
  - entities/tools/outreachr.md
  - entities/tools/centralino-ai-studio-medico.md
  - entities/tools/mc-mod-migrator.md
  - entities/tools/void-minecraft-proxy.md
  - entities/tools/bedrock-ui-animations.md
  - entities/tools/simple-money-minecraft-bedrock-addon.md
maturity: draft
created: 2026-10-06
updated: 2026-10-06
harness_verb: FILE
wire_status: policy_wired
---

## Relations

- @concepts/k282-level-editors-wave.md
- @concepts/k281-basgiath-wave.md
- @concepts/k283-arxiv-wave.md
- @concepts/k283-feeds-wave.md
- @concepts/active-project-research-routing.md
- @sources/eval-github-repos-dev-tools-2026-10-06.md
- @sources/eval-bedrock-ecosystem-2026-10-06.md

## Raw Concept

K283 cluster hub. **Two eval docx, 40 URLs.** Dual-ID **OSINT K283**. Batch split: developer tools / agent harnesses / local RAG (docx A) and Bedrock ecosystem / server tooling (docx B).

## Narrative

Two eval batches landed together. Docx A (dev tools, agent harnesses, local RAG, CAD, concurrency) and docx B (Bedrock ecosystem, server tooling, agent runtimes). Both ran the v10.7 prompt, so `atto`, `guruwatcher` and `basgiath` overlap are scored on every row.

### Tier spread

| Batch | Integrate | Extract | Watch | Context | Pass | UNAVAILABLE |
|-------|-----------|---------|-------|---------|------|-------------|
| A — dev tools | 1 | 6 | 2 | 6 | 5 | 0 |
| B — Bedrock | 0 | 9 | 0 | 7 | 4 | 0 |

**One product Integrate GO: `lfnovo/open-notebook`.** First in four waves.

### The headline — open-notebook (Integrate)

`lfnovo/open-notebook` is a self-hosted, MIT-licensed multi-modal RAG stack — a private NotebookLM. It ingests PDFs, audio and images, exposes REST APIs, and runs vector search over local Ollama models. Scores `atto high`, `genealogy high`, `local-abliterated-lab high`. The play: let Atto Concierge operators query thousands of pages of municipal registry PDFs with page-level citations, **without** sending client PII to a cloud model. **Verified 2026-10-06** (WebFetch): the repo exists, is MIT, ~39.9k stars — the eval's claim holds. Human-gated; local-only inference; no automated write to `truth.ged`.

### Agent-harness extracts (CCC)

- **`tester-army/e2e`** — run the agentic UI test once, then **replay the cached action trace** in CI. Kills per-run LLM token cost. Atto share-portal CI.
- **`msitarzewski/agency-agents`** — 140+ persona definitions with explicit boundaries. CCC / Atto engineering briefs.
- **`frankbria/ralph-claude-code`** — the **Ralph loop**: feed test failures and linter output back to Claude Code until validation passes. Atto parser fixes.
- **`kim-em/hex-dev`** — ports-and-adapters scaffolding (Context).

### GuruWatcher extracts (the useful pairing)

- **`ColeMurray/background-agents`** — async workers for detached long-running jobs.
- **`ldm0/keyed-lock`** — per-key mutex, so parallel newsletter ingests touch distinct tickers without a global lock.

Together they close the race-condition gap when concurrent ingests update the same watch ledger. **Alert-only invariant unchanged: never place orders, never clobber `watches.json`.**

### CeminiParlays extract

`pawurb/hotpath-rs` — Rust hot-path profiler. Profile the copula correlation engine so ranked-EV recomputes stay instant when lines move. **Manual slip entry unchanged; never auto-submit.**

### Basgiath extracts (docx B)

The Bedrock batch is **13-of-20 Basgiath-facing**. The five clear Extract techniques: **`simple-money`** (in-game roleplay currency: coins, bills, ATM block), **`bedrock-ui-animations`** (JSON UI easing — flight speedometer, stamina bars), **`books-minecraft-bedrock-addon`** (readable lore items), **`mc-mod-migrator`** (automated schema migration across Mojang updates), and **`just-clock`** (HUD timer). All stay **free and non-monetized** — in-game tokens only, no Marketplace, no official novel text.

### The Atto telephony row

`albeSavvy/centralino-ai-studio-medico` is a medical-clinic switchboard, but its core is an **Italian voice / intent-routing pipeline**. `atto overlap 0.70`. Reuse the Italian intent classification for *stato civile* / comune inquiry triage. **Hard gate: client genealogical PII must never reach a third-party telephony model without a human gate.**

### Goal-match / stack-mismatch (a recurring Pass)

The docx names `void-community/Void` for a modern .NET-10 modded-server proxy. Its own works-cited resolves the real project to **`caunt/Void`** — a **Java-edition** proxy. Bedrock Dedicated Server has no equivalent BungeeCord-style proxy in this batch. **Goal match, stack mismatch** — same lesson as K282's `FabricModdingConventions`.

### Eval-quality warning

**`NOT FOUND` on 34 of 40 rows** across both docx (metadata: stars / last-commit / issues). Stack strings are mostly `CLAIMED (unverified)`. Docx B lists a duplicate URL (20 = 13). That is the third batch in four days with generated-looking URL lists (K281: 7/20 dead, K282: 6/20 dead). **Score the technique the row names; do not trust the row's metrics.** Only `open-notebook` was independently verified.

### Boundary

**Zero clones (bash has no network). Nothing vendored. One product Integrate GO (`open-notebook`), human-gated.** Basgiath non-monetized. Atto PII perimeter intact.

### Distribution

- `../atto/briefs/2026-10-06_k283-open-notebook-local-rag.md`
- `../atto/briefs/2026-10-06_k283-italian-telephony-intake.md`
- `../GuruWatcher/briefs/2026-10-06_k283-guruwatcher-concurrency.md`
- `../Cemini claude code CCC/briefs/2026-10-06_k283-agent-harness.md`
- `../Gambling wiki/briefs/2026-10-06_k283-hotpath-rs.md`
- `../Game Dev wiki/briefs/2026-10-06_k283-bedrock-addons-from-osint.md`
- `Projects/dragon-rider-map/briefs/2026-10-06_k283-basgiath-extracts.md`
- `../3d printing/briefs/2026-10-06_k283-cad-emulation.md`
- `../Image gen/briefs/2026-10-06_k283-bedrock-textures.md`
