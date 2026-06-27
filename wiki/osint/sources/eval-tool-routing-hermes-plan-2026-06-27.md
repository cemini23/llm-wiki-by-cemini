---
title: "Tool Evaluation and Routing Plan.docx — Hermes-keyword eval (2026-06-27)"
type: source
tags: [tool-evaluation, hermes-collision, routing-plan, k132]
keywords: [hermes-agent, gbrain, codegraph, claude-mem, screenpipe, graphiti, no-mistakes, keyword-collision]
related:
  - concepts/wiki-tooling-evaluation.md
  - concepts/cemini-license-posture.md
  - entities/tools/hermes-agent.md
  - entities/tools/gbrain.md
  - entities/tools/codegraph.md
  - entities/tools/claude-mem.md
  - entities/tools/no-mistakes.md
  - entities/tools/graphiti.md
  - entities/tools/screenpipe.md
maturity: draft
read_status: read
created: 2026-06-27
updated: 2026-06-27
clusters: [agent-harness, wiki-tooling]
---

## Relations

- @concepts/wiki-tooling-evaluation.md — Phase-0 registry
- @entities/tools/hermes-agent.md — Steal-from (curator skill loop); not wholesale Adopt
- @entities/tools/gbrain.md — docx Adopt vs wiki **RETIRED 2026-05-18** — K132 re-eval

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Tool Evaluation and Routing Plan |
| **Type** | DOCX (`Tool Evaluation and Routing Plan.docx`) |
| **sha256** | `0f962de7de194d093fc5326bae2aab8b625c7ac0b71825e8d297d8db9732dbc6` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/Tool Evaluation and Routing Plan.docx` |
| **Retrieved** | 2026-06-27 (inbox) |
| **Read status** | read (tier aggregation + `gh api` spot-check) |

## Narrative

K132 **Hermes-keyword collision** batch — 71 URLs parsed from docx (NousResearch/hermes-agent ecosystem + unrelated `facebook/hermes`, Allegro, Hashicorp, HF model weights). Docx license claims overridden by **`gh api`** where noted.

### Tier distribution (docx → gh-verified)

| Tier | Count | K132 post-Phase-0 |
|------|-------|-------------------|
| **Adopt** | 6 | 4 confirmed MIT/Apache; **screenpipe NOASSERTION** → CONDITIONAL-GO; **gbrain** → re-eval spike only (entity RETIRED) |
| **Steal-from** | 7 | hermes-agent curator, NemoClaw, cc-switch, self-evolution, Hermes-Wiki (NO LICENSE), OmniAgent (NO LICENSE), OpenHuman (GPL) |
| **Reference-only** | 6 | orange-book, awesome lists, HF model cards |
| **Reject** | 25+ | Hermes Desktop/WebUI, `facebook/hermes`, Firecrawl **AGPL-3.0**, keyword noise |
| **UNAVAILABLE** | 25+ | HF GGUF weights, Mnemosyne 404 |

### Adopt — license spot-check (`gh api`, 2026-06-27)

| Repo | Docx | `gh api` | Posture |
|------|------|----------|---------|
| garrytan/gbrain | Adopt | **MIT**, 24.3k★ | **Re-eval spike** — was RETIRED; steal hybrid-search pattern only |
| colbymchenry/codegraph | Adopt | **MIT**, 55k★ | **CONFIRMED** — laptop Adopt (existing entity) |
| thedotmack/claude-mem | Adopt | **Apache-2.0**, 84k★ | **CONFIRMED** — installed laptop-side |
| screenpipe/screenpipe | Adopt | **NOASSERTION** | **CONDITIONAL-GO** — verify LICENSE before vendoring |
| getzep/graphiti | Adopt | **Apache-2.0**, 28k★ | **Adopt** — temporal KG entity stub |
| kunchenguid/no-mistakes | Adopt | **MIT**, 3.7k★ | **CONFIRMED** — K129 entity reaffirmed |

### Steal-from highlights

| Repo | License | Steal |
|------|---------|-------|
| NousResearch/hermes-agent | MIT | `agent/curator.py` 7-day skill consolidate/prune → `skill_audit.py` |
| NVIDIA/NemoClaw | Apache-2.0 | OS agent harness patterns → CCC |
| farion1231/cc-switch | MIT | Claude Code provider switching UX |

### Rejects aggregated (no per-URL stubs)

**Keyword collision:** `facebook/hermes`, `allegro/hermes`, `informalsystems/hermes`, `matcornic/hermes`, Hermes Desktop/WebUI/HUD variants.

**License poison:** `firecrawl/firecrawl` **AGPL-3.0** (docx incorrectly listed Adopt elsewhere in corpus — K74 REJECT stands).

**NO LICENSE / GPL:** Hermes-Wiki, autonovel, OpenHuman GPL-3.0.

## Snippets

> "Tier: Steal-from … Hermes Agent … curator.py module … 7-day cron cycle … grading, consolidating, and pruning the agent's markdown skill library" [Source: Tool Evaluation and Routing Plan.docx URL 1 (retrieved 2026-06-27)]
