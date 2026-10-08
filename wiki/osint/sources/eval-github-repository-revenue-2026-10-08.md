---
title: "GitHub repository revenue evaluation — 20 rows: reverse engineering, local inference, agent orchestration (2026-10-08)"
type: source
tags: [source, k285, eval, local-inference, reverse-engineering, agent-orchestration, ccc, atto]
keywords: [k285, rapid-mlx, rea, artcraft, syntaqlite, validate-pyproject, background-agents, worldmonitor, raddebugger, anyps5]
related:
  - concepts/k285-eval-wave.md
  - concepts/active-project-research-routing.md
  - entities/tools/rapid-mlx.md
  - entities/tools/rea.md
  - entities/tools/syntaqlite.md
maturity: draft
created: 2026-10-08
updated: 2026-10-08
read_status: read
---

## Relations

- @concepts/k285-eval-wave.md
- @concepts/active-project-research-routing.md

## Raw Concept

| File | `GitHub Repository Revenue Evaluation.docx` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/GitHub Repository Revenue Evaluation.docx` |
| Retrieved | 2026-10-08 |
| Dual-ID | **OSINT K285** |
| Batch theme | Reverse engineering, local LLM inference, autonomous agent orchestration, graphics pipelines, developer toolchain validation |
| Rows | 20 URLs |
| sha256 | `0192b608…`-class docx (re-run of the same 20-URL tooling hunt) |

## Narrative

A 20-row eval batch weighted toward **local inference, reverse-engineering tooling, and agent orchestration**. Several rows are **re-evaluations** of repos named in earlier batches (AnyPS5, rea, background-agents, fluffychat).

### Tier spread

| Tier | Count |
|------|-------|
| Integrate | 1 |
| Extract | 5 |
| Watch | 1 |
| Context | 10 |
| Pass | 3 |
| UNAVAILABLE | 0 |

### The Integrate row (1)

**`raullenchai/Rapid-MLX`** — a drop-in **local Apple Silicon LLM inference server** on MLX, exposing an OpenAI/Anthropic-compatible endpoint. The eval's play: **zero-PII local parsing** for Atto's Italian civil-record work, with no cloud API cost. Fits the same lane as K284's `Strata`.

### The Extract rows (5)

| URL | Technique | Route |
|-----|-----------|-------|
| `morluto/rea` | **MCP-based Hopper decompilation + execution tracing** for agents | Local abliterated lab (authorized scope) |
| `storytold/artcraft` | 3D spatial staging / character-posing pipeline before generative video | Basgiath promo clips |
| `LalitMaganti/syntaqlite` | SQLite static linting + LSP validation | Atto vault tables; GuruWatcher ledgers |
| `henryiii/validate-pyproject-schema-store` | Offline-pinned `pyproject.toml` schema validation | Python toolchain hardening |
| `ColeMurray/background-agents` | Sandboxed `spawn-child` delegation + managed skills | Local abliterated lab |

### The Watch row (1)

**`koala73/worldmonitor`** — Watch for a headless API/webhook path that could serve as a **geopolitical disruption circuit-breaker** for the Polymarket LP canary. (The wiki already tracks `worldmonitor` as an AGPL Watch from K261.)

### Context and Pass

Ten Context rows: AnyPS5 (12.8k★, PS5 executable tooling), RAD Debugger, system-design-notes, maki, egui, GDevelop, pstack, convt, **`openai/math`** (the 722-papers repo), awesome-opus5-5-videos. Three **Pass**: `fluffychat` (AGPL), `narumiruna/pi-extensions`, `wcandillon/react-native-skia`.

### Re-evaluations vs earlier waves

- **`boykopovar/AnyPS5`** — **Pass in K283** (unverified binary translation, legal risk) → **Context** here (12.8k★). The technique is still not adopted; only the reference value changed.
- **`morluto/rea`** — **Pass in K283** → **Extract** here. Worth noting the flip.
- **`ColeMurray/background-agents`** — Extract in K283 (GuruWatcher) → Extract here (local lab). Consistent.

### Implementation friction

- **Rapid-MLX** needs **Apple Silicon + MLX-quantized weights**.
- **REA** needs a local **Hopper Disassembler** and a **whitehat authorized scope**.
- **background-agents** needs a container runtime (Modal/Daytona/Docker) and is **single-tenant**.

### Boundary

**No clones (bash has no network). Nothing vendored. No install.** REA is authorized-lab only. ArtCraft output stays fan-made and non-monetized. Atto work keeps client PII local.

### Phase-0 verification (2026-10-08) — every row is real, again

Verified via WebFetch (bash has no network). **All 20 repos exist; zero 404.** This is the **second consecutive all-real batch** (K284 was the first), inverting the K281–K283 pattern.

| Repo | Stars | License |
|------|-------|---------|
| `koala73/worldmonitor` | **88,036** | **AGPL-3.0** |
| `emilk/egui` | 31,013 | Apache-2.0 |
| `4ian/GDevelop` | 27,254 | **NOASSERTION** |
| `liquidslr/system-design-notes` | 24,200 | **none** |
| `morluto/rea` | 19,363 | MIT |
| `boykopovar/AnyPS5` | 12,923 | **GPL-2.0** |
| `openai/math` | 11,291 | Apache-2.0 |
| `wcandillon/react-native-skia` | 8,698 | MIT |
| `EpicGames/raddebugger` | 7,983 | MIT |
| `storytold/artcraft` | 6,064 | **NOASSERTION** |
| `raullenchai/Rapid-MLX` | 3,941 | **NOASSERTION** (claims Apache-2.0) |
| `ColeMurray/background-agents` | 3,345 | MIT |
| `krille-chan/fluffychat` | 3,199 | **AGPL-3.0** |
| `yihui-dev/awesome-opus5-5-videos` | 2,979 | MIT |
| `backnotprop/pstack` | 1,266 | MIT |
| `tontinton/maki` | 1,205 | MIT |
| `LalitMaganti/syntaqlite` | 823 | Apache-2.0 |
| `narumiruna/pi-extensions` | 667 | MIT |
| `opencoredev/convt` | 224 | **AGPL-3.0** |
| `henryiii/validate-pyproject-schema-store` | **8** | Apache-2.0 |

**Licence flags for the Integrate/Extract rows:**

- **`Rapid-MLX` licence RESOLVED 2026-10-08: Apache-2.0.** The API reports NOASSERTION only because GitHub's detector could not match the file; the `LICENSE` file itself reads "Licensed under the Apache License, Version 2.0". **Clean to wire.**
- **`storytold/artcraft` is NOASSERTION** (the K284 `storytold` apps were cleanly Apache-2.0 — the umbrella repo differs).
- **`worldmonitor` is AGPL-3.0** — copyleft; reference only, never vendor.
- **`validate-pyproject-schema-store` has only 8 stars** — tiny, but it is a **daily mirror** of SchemaStore, so low stars are expected.

Note: **`AnyPS5` is GPL-2.0** — K283 rated it Pass on legal grounds; the GPL and the console-binary scope both argue against adoption.

### Distribution

- Rapid-MLX + syntaqlite → `../atto/briefs/2026-10-08_k285-atto-local-inference-lint.md`
- REA + background-agents → `../Cybersecurity wiki/briefs/2026-10-08_k285-rea-background-agents.md`
- ArtCraft → `Projects/dragon-rider-map/briefs/2026-10-08_k285-artcraft-clips.md`
- validate-pyproject → CCC / CeminiDFS toolchain.
- worldmonitor → Gambling wiki (LP canary awareness).

## Snippets

> "Rapid-MLX … delivers drop-in local Apple Silicon LLM inference server, cutting $50–$150/mo in API costs and guaranteeing 100% offline PII isolation for Atto MCP workflows." [Source: GitHub Repository Revenue Evaluation.docx]

> "ArtCraft requires GPU-backed inference pipelines and adherence to Basgiath's non-monetized fan policies." [Source: GitHub Repository Revenue Evaluation.docx]
