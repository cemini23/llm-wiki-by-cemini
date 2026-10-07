---
title: "URL revenue opportunity evaluation — 19 rows: agent tooling, local inference, clean-room creative suites, PS5 homebrew (2026-10-07)"
type: source
tags: [source, k284, eval, atto, local-inference, creative-suite, emulation]
keywords: [k284, photocraft, printcraft, designcraft, strata, monid, upleft, vectorcraft, lightcraft, treg, incredible, effectcraft, filmcraft, ps5]
related:
  - concepts/k284-eval-wave.md
  - concepts/active-project-research-routing.md
  - entities/tools/strata.md
  - entities/tools/artcraft-suite.md
  - entities/tools/treg.md
  - entities/tools/monid.md
maturity: draft
created: 2026-10-07
updated: 2026-10-07
read_status: read
---

## Relations

- @concepts/k284-eval-wave.md
- @concepts/active-project-research-routing.md
- @entities/tools/strata.md
- @entities/tools/artcraft-suite.md

## Raw Concept

| File | `URL Revenue Opportunity Evaluation.docx` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/URL Revenue Opportunity Evaluation.docx` |
| Retrieved | 2026-10-07 |
| Dual-ID | **OSINT K284** |
| Batch theme | Agent tooling, local model inference, clean-room creative suites, PS5 homebrew systems |
| Rows | 19 URLs |
| sha256 | `e75d66926870166a…` |

## Narrative

A 19-row eval batch with a **product/tooling theme**. Two clusters stand out: a **Rust clean-room creative suite** (the `storytold/*` "ArtCraft" apps → Atto document pipeline) and a **local 125B-MoE inference engine** (`Strata`). The tail is **PS5 homebrew emulation** — all Pass.

### Tier spread

| Tier | Count |
|------|-------|
| Integrate | 4 |
| Extract | 5 |
| Watch | 3 |
| Context | 2 |
| Pass | 5 |
| UNAVAILABLE | 0 |

### The Integrate rows (4)

| URL | What it is | Route |
|-----|-----------|-------|
| `storytold/photocraft` | Rust clean-room image editor — batch enhancement/cleanup of document scans | Atto — archive-scan cleanup |
| `storytold/printcraft` | Rust clean-room PDF workbench — compile/bind evidentiary PDF packets | Atto — dossier packet binding |
| `storytold/designcraft` | Rust clean-room page-layout / publishing (multi-page monograph) | Atto — family-history monograph layout |
| `Niko1221/Strata` | Local **125B MoE** inference on a gaming GPU + 64 GB RAM, exposed over a localhost OpenAI/Anthropic endpoint | Local abliterated lab; Atto air-gapped parsing |

The `storytold` trio is a **clean-room, pure-Rust reimplementation** of the Adobe creative apps (the "ArtCraft" project). The eval's play: an **offline client-dossier pipeline** — enhance scans (photocraft) → typeset the monograph (designcraft) → bind the PDF packet (printcraft) — removing Adobe licensing and keeping client PII local.

### The Extract rows (5)

`monid` ("OpenRouter for agent tools" — runtime API discovery/metering for GuruWatcher), `upleft` (native macOS markdown dossier inspector for Atto), `vectorcraft` (algorithmic pedigree/family-tree vector generation), `lightcraft` (RAW photo + colour calibration for Atto/family-tree), `treg` (Basgiath voiceover + TikTok clip skill — Fish Audio TTS + TikHub scraping).

### Watch rows (3)

`incredible.one` (desktop computer-use GUI automation — reliability/safety boundaries), `effectcraft` (headless motion-graphics for Basgiath trailers), `filmcraft` (headless NLE video pipeline for Basgiath clips).

### Pass rows (5) — emulation

`omarchy-apple-dev` (redundant non-Xcode iOS cross-compile) and the four **PS5 homebrew emulators** — `PS5_RetroArch`, `ProsperoEden` (Switch), `PS5X360` (Xbox 360), `PS5SX2` (PS2). The eval classes these Pass on **legal/scope grounds**; no code recorded.

### Implementation friction

- **photocraft** needs explicit `--automation-read-root` / `--automation-write-root` boundary flags. **Client PII stays in local storage (`~/AttoVault/`).**
- **Strata** locks **35–55 GB of system RAM** on first load and needs a fast NVMe SSD. Authorized-pentest scope applies.
- **treg / monid** — enforce spend ceilings on pay-per-call endpoints.
- **incredible** — desktop automation must never link to CeminiParlays slips or GuruWatcher trading channels.

### Boundary

**No clones (bash has no network). Nothing vendored. No install.** The Integrate rows are leads, human-gated. IP discipline holds: no official art or book text; the creative suite output stays fan-made and local.

### Phase-0 verification (2026-10-07) — every row is real

Verified via WebFetch (bash has no network). **All 19 GitHub repos exist and are active (pushed 2026-10-06/07).** Zero dead links — unlike K281–K283.

| Repo | Stars | License |
|------|-------|---------|
| `storytold/photocraft` (Photoshop) | 12,693 | Apache-2.0 |
| `storytold/filmcraft` (Premiere) | 2,443 | Apache-2.0 |
| `storytold/lightcraft` (Lightroom) | 2,006 | Apache-2.0 |
| `storytold/printcraft` (Acrobat) | 1,751 | Apache-2.0 |
| `storytold/vectorcraft` (Illustrator) | 1,610 | Apache-2.0 |
| `storytold/effectcraft` | 1,236 | Apache-2.0 |
| `storytold/designcraft` (InDesign) | 738 | Apache-2.0 |
| `Niko1221/Strata` | 16,491 | **MIT** |
| `superdesigndev/treg` | 4,651 | **NOASSERTION** (Apache-2.0 + additional terms) |
| `monid-ai/monid` | 2,462 | MIT |
| `shader-effects-inc/shaders` | 2,095 | MIT |
| `joshuaswarren/omarchy-apple-dev` | 827 | MIT |
| `blackbearreloaded/ProsperoEden` | 471 | GPL-3.0 |
| `Swordpdf/PS5SX2` | 371 | GPL-3.0 |
| `mihawk-99/PS5_RetroArch` | 219 | GPL-3.0 |
| `BrinooTk/PS5X360` | 161 | MIT |
| `joshuaswarren/omarchy-mlx` | 83 | MIT |
| `bitemyapp/upleft` | **6** | MIT |

Two corrections against the docx tier list:

- **`treg` is NOASSERTION**, not a clean open license — Apache-2.0 **plus additional terms**. Flag before any Basgiath wiring.
- **`upleft` has only 6 stars** — very early. The eval rated it Extract for Atto; treat it as a **read-the-idea** row, not a dependency.

**The `storytold` suite is the headline.** Seven active, Apache-2.0, pure-Rust clean-room reimplementations of the Adobe apps. That is an unusually clean licensing story for an Atto document pipeline.

### Distribution

- Atto document pipeline (photocraft/printcraft/designcraft/upleft/vectorcraft/lightcraft) → `../atto/briefs/2026-10-07_k284-atto-document-pipeline.md`
- Strata (local inference) → `../Cybersecurity wiki/briefs/2026-10-07_k284-strata-local-inference.md`
- GuruWatcher (monid) → `../GuruWatcher/briefs/2026-10-07_k284-monid-metering.md`
- Basgiath (treg/effectcraft/filmcraft) → `Projects/dragon-rider-map/briefs/2026-10-07_k284-basgiath-clips.md`
- PS5 emulation → Game-dev wiki (awareness only, Pass).

## Snippets

> "Integrating PhotoCraft, DesignCraft, and PrintCraft eliminates external Adobe licensing costs and automates dossier compilation." [Source: URL Revenue Opportunity Evaluation.docx]

> "Strata … Initial load locks 35 to 55 GB of system RAM and requires fast NVMe SSD storage for low-latency n-gram lookup table paging." [Source: URL Revenue Opportunity Evaluation.docx]

> "PhotoCraft requires explicit folder boundary flags (--automation-read-root / --automation-write-root) for agent execution; client PII must remain strictly confined to local storage." [Source: URL Revenue Opportunity Evaluation.docx]
