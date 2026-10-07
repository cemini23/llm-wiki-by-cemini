---
title: "Developer resource revenue evaluation — 20 rows: frontend architecture, agent UI design registries, compute kernels (2026-10-07)"
type: source
tags: [source, k284, eval, design, frontend, ccc, seo, agent-ui]
keywords: [k284, refero-styles, 21st-dev, uiverse, scrolltide, kage-design, motion-primitives, pricing-pages, cta-gallery, shaders, nextjs-16]
related:
  - concepts/k284-eval-wave.md
  - concepts/active-project-research-routing.md
  - entities/tools/refero-styles.md
  - entities/tools/21st-dev.md
maturity: draft
created: 2026-10-07
updated: 2026-10-07
read_status: read
---

## Relations

- @concepts/k284-eval-wave.md
- @concepts/active-project-research-routing.md

## Raw Concept

| File | `Developer Resource Revenue Evaluation.docx` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/Developer Resource Revenue Evaluation.docx` |
| Retrieved | 2026-10-07 |
| Dual-ID | **OSINT K284** |
| Batch theme | Frontend architecture, AI agent UI design registries, component primitives, high-performance compute kernels |
| Rows | 20 URLs |
| sha256 | `0192b608d376a754…` |

## Narrative

A 20-row eval batch with a **design/web-frontend theme** — a departure from the K281–K283 infra/agent batches. Most rows are **UI galleries and component registries**. The eval ran the v10.7 prompt, so `atto` overlap is scored.

### Tier spread

| Tier | Count |
|------|-------|
| Integrate | 3 |
| Extract | 8 |
| Context | 8 |
| Pass | 0 |
| UNAVAILABLE | 1 |

### The Integrate rows (3) — all design tooling, all MCP

| URL | What it is | Route |
|-----|-----------|-------|
| `styles.refero.design` (Refero Styles) | Design-style library with an **MCP server** that streams `DESIGN.md` tokens into Cursor/Claude | CCC — feeds coding agents a design contract |
| `21st.dev` | shadcn component registry with an **MCP connector** | CCC — streams components into active frontends |
| `uiverse.io` | Open **CSS/Tailwind** component library (toggles, controls) | CeminiDFS / CeminiParlays UI |

The eval's headline claim: agent-written frontends drift because the agent has **no design contract**. Both Refero and 21st.dev close that gap by handing the agent explicit tokens and a verified component registry.

### The Extract rows (8)

`Next.js 16.4` (`ensureStatic` static-export guarantee), `shader-effects-inc/shaders` (WebGPU background shaders + MCP), `scrolltide.co` (scroll-driven landing prompts), `kage.design` (Claude/Cursor component prompt templates), `kinetics.colorion.co` (micro-interaction CSS/React), `motion-primitives.com` (morphing dialogs, tab expanders), `pricingpages.design` (tier-comparison matrix), `cta.gallery` (CTA card layouts).

### Context rows (8) and the Pass/UNAVAILABLE

Eight galleries are reference-only (minimal.gallery, awwwards, land-book, footer.design, navbar.gallery, 404s.design, kitbitz.art, DeepGEMM). **`pingdotgg/ts-rust` is UNAVAILABLE — 404.**

### License notes

- `shader-effects-inc/shaders` core is **MIT**; the platform presets at shaders.com are **proprietary**.
- `scrolltide.co` is a **$299 proprietary** prompt library — extract the prompt *grammar*, do not copy code.
- `DeepGEMM` MIT. `uiverse.io` and `motion-primitives.com` MIT/open.

### Cross-note — `shaders` appears twice

`shader-effects-inc/shaders` is **Extract in this docx (A)** and **Context in the sibling docx (B)**. Both routes agree it is a **WebGPU visual reference**; the Extract rating here is for Atto landing-page conversion. See @sources/eval-url-revenue-opportunity-2026-10-07.md.

### Phase-0 verification (2026-10-07) — the docx was wrong on the one "UNAVAILABLE" row

Verified via WebFetch (bash has no network). **Every row resolved.**

- **`pingdotgg/ts-rust` EXISTS** — 159★, MIT, pushed 2026-10-07, "An experimental Rust port of the TypeScript 7 compiler (tsc)". **The docx rated it UNAVAILABLE / 404 — that is a false negative.** It is a real, active project; re-score it on its merits.
- `shader-effects-inc/shaders` — 2,095★, **MIT** (confirms the docx). Active, pushed 2026-10-07.
- `styles.refero.design` — confirms "DESIGN.md for Cursor/Claude Code/Codex". `21st.dev` — React + Tailwind/shadcn registry. `motion-primitives.com`, `kage.design`, `scrolltide.co`, `404s.design`, `pricingpages.design`, `cta.gallery`, and the Next.js 16.4 post all resolve.
- **`uiverse.io` — HTTP 403 to automated fetch.** May exist but blocks bots; treat as unverified-by-fetch.

**Eval-quality note, inverted:** unlike K281–K283 (6–7 of 20 dead per batch), this batch has **zero dead links**. The one error is a false *negative*.

### Boundary

**No clones (bash has no network). Nothing vendored.** The Integrate rows are **MCP connectors** — wiring them means an install into Cursor/Claude config, which is **human-gated**. The shaders row needs WebGPU canvas fallbacks for older browsers. Atto share routes never expose unredacted genealogical records.

### Distribution

- Design-registry + prompt rows → `../Cemini claude code CCC/briefs/2026-10-07_k284-design-registries.md`
- Landing/CTA/pricing rows → `../SEO:GEO B&M Business/briefs/2026-10-07_k284-landing-conversion.md`
- Shaders / awwwards / kitbitz → Image-gen + Game-dev awareness.
- UIverse → `../Gambling wiki/briefs/2026-10-07_k284-uiverse-ui.md`

## Snippets

> "Integrating Refero Styles MCP (URL 7) and 21st.dev MCP (URL 16) supplies explicit DESIGN.md tokens and verified component registries directly to coding agents, cutting frontend development overhead by over 50 hours." [Source: Developer Resource Revenue Evaluation.docx]

> "Scrolltide is a $299 proprietary prompt library (extract prompt grammar without copying code)." [Source: Developer Resource Revenue Evaluation.docx]

> "`pingdotgg/ts-rust` … repository unreachable / 404." [Source: Developer Resource Revenue Evaluation.docx]
