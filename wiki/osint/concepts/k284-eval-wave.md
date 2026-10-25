---
title: K284 Eval Wave — design registries + clean-room creative suite (Oct 2026)
type: concept
tags: [k284, eval, design, frontend, creative-suite, local-inference, ccc, seo, atto]
keywords: [k284, refero-styles, 21st-dev, uiverse, storytold, photocraft, printcraft, designcraft, strata, treg, monid, ps5]
related:
  - concepts/k283-eval-wave.md
  - concepts/k284-arxiv-wave.md
  - concepts/k284-feeds-wave.md
  - concepts/active-project-research-routing.md
  - sources/eval-developer-resource-2026-10-07.md
  - sources/eval-url-revenue-opportunity-2026-10-07.md
  - entities/tools/strata.md
  - entities/tools/artcraft-suite.md
  - entities/tools/treg.md
  - entities/tools/monid.md
  - entities/tools/refero-styles.md
  - entities/tools/21st-dev.md
  - concepts/k285-eval-wave.md
maturity: draft
created: 2026-10-07
updated: 2026-10-25
harness_verb: FILE
wire_status: policy_wired
---

## Relations

- @concepts/k283-eval-wave.md
- @concepts/k284-arxiv-wave.md
- @concepts/k284-feeds-wave.md
- @concepts/active-project-research-routing.md
- @sources/eval-developer-resource-2026-10-07.md
- @sources/eval-url-revenue-opportunity-2026-10-07.md

## Raw Concept

K284 cluster hub. **Two eval docx, 39 URLs.** Dual-ID **OSINT K284**. Theme split: **design/UI registries** (docx A) and **agent tooling / local inference / creative suites** (docx B).

## Narrative

Two eval batches landed together, both **product/creative** rather than infrastructure.

### Tier spread

| Batch | Integrate | Extract | Watch | Context | Pass | UNAVAILABLE |
|-------|-----------|---------|-------|---------|------|-------------|
| A — developer resources | 3 | 8 | 0 | 8 | 0 | 1 |
| B — URL revenue | 4 | 5 | 3 | 2 | 5 | 0 |

### Docx A — the design-registry batch

Three **Integrate** rows, all design tooling with **MCP connectors**: **Refero Styles** (streams `DESIGN.md` tokens into Cursor/Claude), **21st.dev** (shadcn component registry), **UIverse** (CSS/Tailwind controls). The eval's thesis: **agent-written frontends drift because the agent has no design contract** — these hand it one. Extraction rows are landing/CTA/pricing patterns (→ SEO wiki) plus WebGPU shaders. **`pingdotgg/ts-rust` was rated UNAVAILABLE — but Phase-0 found it alive (159★, MIT).**

### Docx B — the creative-suite and inference batch

The headline is the **`storytold` "ArtCraft" suite** — seven **active, Apache-2.0, pure-Rust clean-room reimplementations** of the Adobe apps (photocraft/Photoshop 12.7k★, filmcraft/Premiere, lightcraft/Lightroom, printcraft/Acrobat, vectorcraft/Illustrator, effectcraft, designcraft/InDesign). The play: an **offline Atto document pipeline** — enhance scans → typeset the monograph → bind the PDF packet — no Adobe licence, no client PII leaving the laptop.

The second headline is **`Niko1221/Strata`** (16.5k★, MIT) — a local **125B-MoE** inference engine on a gaming GPU + 64 GB RAM, exposed over a localhost OpenAI/Anthropic endpoint. For the local abliterated lab and air-gapped Atto parsing.

Also Extract: `monid` (agent-tool metering → GuruWatcher), `upleft` (**only 6★** — read the idea, not a dependency), `vectorcraft`, `lightcraft`, `treg` (Basgiath voiceover/TikTok).

### The Pass tail — PS5 emulation

Five Pass rows: `omarchy-apple-dev` and four **PS5 homebrew emulators** (`PS5_RetroArch`, `ProsperoEden`, `PS5X360`, `PS5SX2`). Classed Pass on legal/scope grounds. **No code recorded.**

### Eval-quality — inverted this time

Unlike K281–K283 (6–7 dead URLs each), **this batch has zero dead links.** All 19 GitHub repos verified alive. The one error is a **false negative** (`ts-rust`). Two license corrections against the docx: **`treg` is NOASSERTION** (Apache-2.0 + additional terms), and the **`storytold` suite is Apache-2.0** (clean).

### Boundary

**Zero clones (bash has no network). Nothing vendored. No install.** Design-registry Integrate rows are **MCP installs — human-gated**. Atto work keeps client PII local; the creative-suite rows need `--automation-read-root` / `--automation-write-root` boundaries. **No xsp/pm scp.**

### Distribution

- `../Cemini claude code CCC/briefs/2026-10-07_k284-design-registries.md`
- `../atto/briefs/2026-10-07_k284-atto-document-pipeline.md`
- `../Cybersecurity wiki/briefs/2026-10-07_k284-strata-local-inference.md`
- `../GuruWatcher/briefs/2026-10-07_k284-monid-metering.md`
- `../Gambling wiki/briefs/2026-10-07_k284-uiverse-ui.md`
- `../SEO:GEO B&M Business/briefs/2026-10-07_k284-landing-conversion.md`
- `Projects/dragon-rider-map/briefs/2026-10-07_k284-basgiath-clips.md`
