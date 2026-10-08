---
title: K285 Eval Wave — local inference, reverse engineering, agent orchestration (Oct 2026)
type: concept
tags: [k285, eval, local-inference, reverse-engineering, agent-orchestration, ccc, atto]
keywords: [k285, rapid-mlx, rea, artcraft, syntaqlite, validate-pyproject, background-agents, worldmonitor]
related:
  - concepts/k284-eval-wave.md
  - concepts/k285-arxiv-wave.md
  - concepts/k285-feeds-wave.md
  - concepts/active-project-research-routing.md
  - sources/eval-github-repository-revenue-2026-10-08.md
  - entities/tools/rapid-mlx.md
  - entities/tools/rea.md
  - entities/tools/syntaqlite.md
maturity: draft
created: 2026-10-08
updated: 2026-10-08
harness_verb: FILE
wire_status: policy_wired
---

## Relations

- @concepts/k284-eval-wave.md
- @concepts/k285-arxiv-wave.md
- @concepts/k285-feeds-wave.md
- @concepts/active-project-research-routing.md
- @sources/eval-github-repository-revenue-2026-10-08.md

## Raw Concept

K285 cluster hub. **One eval docx, 20 URLs.** Dual-ID **OSINT K285**. Theme: reverse engineering, local LLM inference, autonomous agent orchestration, graphics pipelines, developer toolchain validation.

## Narrative

### Tier spread

**1 Integrate · 5 Extract · 1 Watch · 10 Context · 3 Pass.**

### The Integrate row — local inference, again

**`raullenchai/Rapid-MLX`** — a drop-in **Apple Silicon LLM server** on MLX with an OpenAI/Anthropic-compatible endpoint, 3,941★. Same lane as K284's **`Strata`**: **offline, zero-token-cost inference** for Atto's Italian civil-record parsing and the local abliterated lab. ⚠ **Licence reads NOASSERTION** at the API level though the description claims Apache-2.0 — **confirm before wiring.**

**Two local-inference workers in two waves** (`Strata` K284, `Rapid-MLX` K285) is a clear signal: the local-inference lane is now the wiki's most consistently-recurring Integrate.

### The Extract rows

- **`morluto/rea`** (19,363★, **MIT**) — MCP-based **Hopper decompilation + execution tracing**. The standout: a Pass in K283, now an Extract. **Authorized-lab only.**
- **`storytold/artcraft`** (6,064★) — 3D staging / character-posing **before** generative video, for **Basgiath promo clips**. ⚠ NOASSERTION (the K284 `storytold` apps were Apache-2.0; the umbrella repo is not).
- **`LalitMaganti/syntaqlite`** (823★, Apache-2.0) — SQLite static linting + LSP. Atto vault tables; GuruWatcher ledgers.
- **`henryiii/validate-pyproject-schema-store`** (8★, Apache-2.0) — a **daily SchemaStore mirror**; low stars are expected.
- **`ColeMurray/background-agents`** (3,345★, MIT) — sandboxed `spawn-child` delegation. (Already an Extract in K283 for GuruWatcher; here for the local lab.)

### Watch

**`koala73/worldmonitor`** (88,036★, **AGPL-3.0**) — watch for a headless API/webhook path as a **geopolitical disruption circuit-breaker** for the Polymarket LP canary. Already an AGPL Watch from K261.

### Context / Pass

10 Context (egui, GDevelop, raddebugger, maki, pstack, convt, **openai/math**, AnyPS5, …). 3 Pass: **`fluffychat`** (AGPL), `pi-extensions`, `react-native-skia`.

### Phase-0 — all 20 real, zero 404 (second consecutive clean batch)

Unlike K281–K283 (6–7 dead links each), **K285 has zero dead links** and K284 had none either. Licence flags: **Rapid-MLX NOASSERTION**, **artcraft NOASSERTION**, **worldmonitor AGPL-3.0**, **AnyPS5 GPL-2.0**, `system-design-notes` none.

### Boundary

**Zero clones. Nothing vendored. No install.** REA = authorized scope. ArtCraft = fan-made, non-monetized. Atto PII stays local. **No xsp/pm scp.**

### Distribution

- `../atto/briefs/2026-10-08_k285-atto-local-inference-lint.md`
- `../Cybersecurity wiki/briefs/2026-10-08_k285-rea-background-agents.md`
- `Projects/dragon-rider-map/briefs/2026-10-08_k285-artcraft-clips.md`
- `../Gambling wiki/briefs/2026-10-08_k285-worldmonitor-canary.md`
