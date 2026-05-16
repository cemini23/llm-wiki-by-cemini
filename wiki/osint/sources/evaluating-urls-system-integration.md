---
title: "K37 — Evaluating URLs for System Integration (21-URL Three-Surface Batch)"
type: source
tags: [source, evaluation-brief, tooling, three-surface-fit, ip-readiness, license-audit, k37]
keywords: [URL eval, weather APIs, agent frameworks, MCP servers, knowledge bases, three-surface evaluation, ip-sale-readiness]
related:
  - concepts/tool-evaluation-framework.md
  - concepts/cemini-license-posture.md
  - concepts/mcp-tool-marketplace.md
  - entities/tools/visualcrossing-weather.md
  - entities/tools/openweather-api.md
  - entities/tools/weatherapi-com.md
  - entities/tools/claude-bootstrap-maggy.md
  - entities/tools/paper2any.md
  - entities/tools/ui-tars-desktop.md
  - entities/tools/markdown-preview-pluk.md
  - entities/tools/asb-agent-security.md
  - entities/tools/beever-atlas.md
  - entities/tools/llms-from-scratch-rasbt.md
  - entities/tools/homelab-hub.md
  - entities/tools/ebay-mcp.md
  - entities/tools/contextlattice.md
maturity: validated
read_status: deep-read
created: 2026-05-11
updated: 2026-05-11
---

## Relations
- `@concepts/tool-evaluation-framework.md` — three-surface methodology applied here (Cemini prod / Wiki librarian server / Workflow laptop)
- `@concepts/cemini-license-posture.md` — license clean-list enforcement
- `@concepts/mcp-tool-marketplace.md` — multiple URLs evaluated as MCP-native or MCP-adjacent

## Raw Concept

- **Title**: Cemini and Wiki Stack: Technical Architecture and Integration Evaluation
- **Author**: User-prepared analyst memo (commissioned eval brief)
- **Type**: docx evaluation brief, 21 URLs scored on three-surface fit matrix
- **Location**: `cemini-librarian:/opt/cemini-bulk/research/Evaluating URLs for System Integration.docx`
- **Retrieved**: 2026-05-11
- **sha256**: `49480ac190ebb394…` (preingest verdict: NEW)
- **Pages**: 21 URLs scored — 8 UNAVAILABLE, 13 evaluated
- **Read-status**: deep-read

## Narrative

K37 batch — 21 URLs evaluated against the standard three-surface matrix (Cemini production stack / Wiki librarian server / Workflow laptop), each graded ✅/⚠️/❌ per surface with a recommendation tier: **Adopt** / **Steal-from** / **Reference-only** / **Defer** / **Reject**. 8 URLs were UNAVAILABLE at evaluation time and yielded no technical data.

### Tier rollup

| Tier | Count | URLs |
|------|------:|------|
| **Adopt** | 3 | Visual Crossing Weather (URL 3), UI-TARS-desktop (URL 9), markdown-preview-pluk (URL 13) |
| **Steal-from** | 6 | claude-bootstrap (URL 5), ASB (URL 14), Beever Atlas (URL 15), homelab-hub (URL 18), ebay-mcp (URL 20), contextlattice (URL 21) |
| **Reference-only** | 3 | WeatherAPI (URL 4), Paper2Any (URL 7), LLMs-from-scratch (URL 17) |
| **Defer** | 1 | OpenWeather (URL 2) |
| **UNAVAILABLE** | 8 | URLs 1, 6, 8, 10, 11, 12, 16, 19 |

### Domain clustering

- **Weather APIs** (URLs 1-4): three reachable, all scored against Cemini's prediction-market (Polymarket/Kalshi weather contracts) use case. Visual Crossing wins on 50-year historical depth + commercial-free-tier license.
- **Agent / coding frameworks** (URLs 5, 9, 11, 12): Maggy/claude-bootstrap is Steal-from for TDD-loop pattern. UI-TARS-desktop is Adopt for GUI automation of wiki curation. 11-12 unreachable.
- **Wiki / knowledge-base infrastructure** (URLs 15, 21): Beever Atlas exemplifies a 3-tier semantic store design that should inform Cemini's `llm-wiki-compiler` architectural roadmap. contextlattice is a reference impl for long-horizon agent memory split across hot/warm/cold storage.
- **Research workflow** (URLs 7, 13, 17): Paper2Any (reference-only, GPU-bound), markdown-preview (Adopt for macOS workflow + cross-wiki candidate), LLMs-from-scratch (educational reference).
- **Security / homelab** (URLs 14, 18): ASB (Agent Security Bench) → Steal-from for attack-model audit on Cemini's LangGraph. homelab-hub → Steal-from for Cytoscape.js graph viz pattern, transferable to wiki backlink visualization.
- **MCP server architectural blueprint** (URL 20): ebay-mcp explicitly Steal-from purely for the 300+ tool MCP-server scaling architecture, not eBay data per se.

### Cross-wiki routing

**URL 13 — markdown-preview** (pluk-inc/markdown-preview, macOS native, LaTeX+Mermaid support) is the only URL in this batch with strong cross-wiki utility. All 4 wikis (OSINT, image-gen, seo-geo, 3d-printing) are markdown-based, so this tool benefits every one. Routed via `cross_wiki_route.py` as a brief (not page — tangential to other wikis' core domains) to image-gen-wiki, seo-wiki, and 3d-printing-wiki.

### Reading method

- 13 reachable URLs read in full from the brief
- 8 UNAVAILABLE URLs flagged for re-resolution via Exa MCP (web_search_exa or crawling_exa) in a follow-up pass — Tier 1 gap detection will catch these as cited-unread stubs

### License posture warnings

- **claude-bootstrap (Maggy)**: license not surfaced in brief — Phase-0 audit needed before any code extraction
- **Beever Atlas**: license not stated — only architectural patterns to be lifted, no code, so license-clean per Cemini IP-sale-readiness policy
- **contextlattice**: license check pending — same constraint
- **ASB**: ICLR 2025 academic codebase — likely MIT/Apache but needs verification before any pattern lift
- **homelab-hub**: license check pending
- **ebay-mcp**: license check pending

All Phase-0 audits gated on user GO before any of these promote to a prod or workspace-laptop brief.

[Source: Evaluating URLs for System Integration.docx, retrieved 2026-05-11]
