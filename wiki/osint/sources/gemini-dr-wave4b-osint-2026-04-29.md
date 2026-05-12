---
title: "Gemini Deep Research — Wave 4B: OSINT + Satellite + Wiki Tooling Link Evaluation (18 URLs, 2026-04-29)"
type: source
tags: [docx, librarian-tooling, link-evaluation, decision-record, gemini-dr-wave4, osint, satellite-imagery, cyber-threat-intel, cemini-internal]
keywords: [gemini-dr-wave4b, osint-link-evaluation, atomicmemory-llm-wiki-compiler-reaffirm, karpathy-microgpt-reference, ironsight, sightline, geointel, metabigor, cti-expert, onionscan-reject, telegramdigger, awesome-osint-arsenal, spaceshift-sateais-api, sunabaco-reject, slider-cira-colostate, geosentinel, satellites-pro, anti-hallucination-spot-check]
clusters: [librarian-tooling, link-evaluation, decision-record, osint]
related:
  - sources/gemini-dr-link-eval-2026-04-28.md
  - sources/gemini-dr-wave3-link-eval-2026-04-28.md
  - sources/gemini-dr-wave4a-cemini-stack-2026-04-29.md
  - sources/atomicmemory-llm-wiki-compiler.md
  - concepts/wiki-tooling-evaluation.md
  - concepts/ip-sale-readiness.md
  - concepts/high-signal-paper-patterns.md
  - sources/7onez-cti-expert.md
  - sources/spaceshift-sateais-api.md
  - sources/gemini-dr-wave5a-cemini-stack-2026-04-30.md
  - sources/gemini-dr-wave5b-osint-2026-04-30.md
maturity: validated
read_status: read
created: 2026-04-29
updated: 2026-04-29
---

## Relations

- @sources/gemini-dr-link-eval-2026-04-28.md — Wave 2 (24 URLs) of the Gemini DR link-evaluation lineage
- @sources/gemini-dr-wave3-link-eval-2026-04-28.md — Wave 3 (13 URLs) sibling
- @sources/gemini-dr-wave4a-cemini-stack-2026-04-29.md — Wave 4A sibling (30 URLs Cemini-stack focus)
- @sources/atomicmemory-llm-wiki-compiler.md — URL 2; Wave 4B reaffirms Adopt (already adopted as the librarian's serving layer per Wave 1+2 lineage)
- @concepts/wiki-tooling-evaluation.md — wave-evaluation parent
- @concepts/ip-sale-readiness.md — license analysis parent
- @concepts/high-signal-paper-patterns.md — rubric used to score the OSINT Adopts

## Raw Concept

- **Original title**: "Cemini Stack & Wiki Stack — Link Evaluation Brief" (same template title as Wave 4A; note user's OSINT focus implied by the file name "another Link Evaluation for Trading and Wiki Stacks 4_29.docx")
- **Source filename**: `another Link Evaluation for Trading and Wiki Stacks 4_29.docx`
- **Type**: User-authored Gemini Deep Research output (docx, 3.0 MB, 434 paragraphs, 70k characters)
- **Date**: Modified 2026-04-30 (UTC; author dropped 2026-04-29 EDT alongside Wave 4A)
- **URL count**: 18 evaluations
- **Evaluation framework**: same 8-section per-URL template as Wave 2/3/4A
- **Location after ingest**: cemini-librarian:/opt/cemini-bulk/research/another Link Evaluation for Trading and Wiki Stacks 4_29.docx
- **Read status**: read (full text extracted to /tmp; URL catalog + recommendation tier captured)
- **Discovered via**: User manual drop in inbox 2026-04-29
- **Primary clusters**: librarian-tooling, link-evaluation, decision-record, osint

### Why two Wave 4 docx?

Both docx files are dated 2026-04-29 and use the same template. **Brief A (this session's `wave4a` page)** focuses on Cemini-production-stack adoption candidates (MCP servers, trading tools, quant libs); **Brief B (this page)** focuses on **OSINT + satellite + wiki tooling** — a different domain. The user's workspace name ("OSINT WORKSPACE") signals the OSINT angle is part of the schema's broader purpose (per `@CLAUDE.md` "OSINT and financial research"), but Cemini's deployed stack is currently financial-only. **Brief B's adoption candidates are mostly research-only / future-OSINT-layer**, not immediate Cemini-stack integrations.

## Narrative

### Recommendation distribution (18 URLs)

| Tier | Count | URLs |
|---|---|---|
| **Adopt** | 3 | atomicmemory/llm-wiki-compiler (2) [reaffirm], 7onez/cti-expert (9), Spaceshift SateAIs API (14) |
| **Steal-from** | 3 | NoblerWorks-HQ/IRONSIGHT (5), ni5arga/sightline (6), h9zdev/GeoSentinel (17) |
| **Reference** | 5 | karpathy/microgpt.py (3), atiilla/GeoIntel (7), awesome-osint-arsenal (13), slider.cira.colostate.edu (16), satellites.pro (18) |
| **Defer** | 1 | j3ssie/metabigor (8) |
| **Reject** | 2 | s-rah/onionscan (11), sunabaco.com/event/05api (15) |
| **Unavailable** | 4 | alialsartawi7-sketch/ghosttrace (1), elementalsouls/Claude-OSINT (4), kawaiipantsu/telegramdigger (10), hackers-arise.com/open-source-intelligence-osint (12) |
| total | 18 | |

Adopt rate: 3/14 evaluable = **21%**. Lower than Wave 4A's 32%; consistent with the OSINT domain being less Cemini-stack-aligned.

### Pre-existing wiki integrations

**URL 2 — atomicmemory/llm-wiki-compiler**: already in wiki at `@sources/atomicmemory-llm-wiki-compiler.md`. Originally evaluated in Wave 1+2 as Adopt for the librarian server stack. Wave 4B reaffirms with detailed integration vector: "The llmwiki serve command must be configured as a persistent background process, exposing the official MCP server with a defined Tool Allowlist (e.g., kb_search_smart, kb_context, kb_read) on port 3838 over the Hetzner VPS Private Network." This matches the actual deployed pattern (Phase 3.5 — see `@concepts/librarian-server-architecture.md`) — confirming the Wave 4B evaluation is well-grounded.

**URL 3 — karpathy/microgpt.py**: this is the same gist the user asked about earlier in the 2026-04-29 session. Evaluated as Reference (not Adopt). Confirms the workspace's earlier decision to not ingest as a primary source. **External validation of the high-signal-paper-patterns rubric application**: Filter 3 (Cemini-domain mismatch) → Reference / Skip path.

### Per-URL summaries — Adopts

**URL 9: 7onez/cti-expert** — Cyber Threat Intelligence expert tooling
> Cyber-threat-intel pipeline, primarily for OSINT-event-driven analysis. **Cemini-relevance**: a future "OSINT-event ticker impact" analyst node could consume CTI data to flag ticker-relevant security events (e.g. exchange hack → SOL/COIN watchlist alert). Not immediately deployable; promotes the `wiki/concepts/osint-event-driven-analysis.md` concept (not yet created — would be the natural extension if Cemini takes on event-driven OSINT).

**URL 14: Spaceshift SateAIs API** (`sorae.info/biz/...` — Japanese space industry news) — closed/commercial API
> Japanese satellite imagery analytics API. **Cemini-relevance**: macro-event detection from satellite data (oil tanker tracking, port congestion, agricultural yields, etc.). Vendor closed-source API; integration cost depends on API pricing tier. **Defer-Cemini until macro-event-from-satellite analyst node is on the roadmap**. Adopt verdict here is more aspirational than immediate.

**URL 2: atomicmemory/llm-wiki-compiler** — already adopted (`@sources/atomicmemory-llm-wiki-compiler.md`). See cross-wave note above.

### Per-URL summaries — Steal-from

**URL 5: NoblerWorks-HQ/IRONSIGHT** — OSINT methodology / pattern source.

**URL 6: ni5arga/sightline** — OSINT visualization / data correlation tool. Steal-from the visualization patterns if Cemini ever surfaces an OSINT analyst dashboard.

**URL 17: h9zdev/GeoSentinel** — Geospatial intelligence pattern source.

### Per-URL summaries — Reference

- **URL 3: karpathy/microgpt.py** — see cross-wave note above; confirms the workspace's prior Skip decision.
- **URL 7: atiilla/GeoIntel** — Geospatial intelligence reference.
- **URL 13: rawfilejson/awesome-osint-arsenal** — Curated awesome-list for OSINT tools.
- **URL 16: slider.cira.colostate.edu** — Colorado State CIRA satellite imagery viewer (GOES-19). Reference; not deployable but useful for ad-hoc satellite checks (hurricane / storm impact on agricultural commodity tickers).
- **URL 18: satellites.pro** — Satellite tracking reference.

### Per-URL summaries — Defer

- **URL 8: j3ssie/metabigor** — OSINT scanner. Defer pending license + maintenance review.

### Per-URL summaries — Reject

- **URL 11: s-rah/onionscan** — Tor-network OSINT scanner. Reject for Cemini context (legal-risk + operational-distance from financial OSINT).
- **URL 15: sunabaco.com/event/05api** — Japanese event landing page (not a research/code asset). Reject.

### Cross-wave patterns

1. **Two-domain split**: Wave 4A (Cemini-stack) and Wave 4B (OSINT) covering the workspace's full scope ("OSINT + financial research" per CLAUDE.md). The 2-docx-same-day pattern matches Wave 1's similar split between `4-5-links.md` and `4-5-links-2.md`.

2. **OSINT layer is research-only currently**: 3 Adopts (cti-expert, atomicmemory-llm-wiki-compiler, Spaceshift) but only the wiki-compiler is deployed. The OSINT-data-layer extension is **roadmap candidate** — would require a new `concepts/osint-event-driven-analysis.md` page + dedicated analyst-node design.

3. **microgpt.py reference (URL 3)** echoes the user's earlier in-session question. The wiki's earlier decision (Skip / Reference-only) aligns with Gemini DR's independent assessment. Consistent rubric application.

### Open questions / NEEDS VERIFICATION

- **URL 5 IRONSIGHT license** [VERIFIED 2026-05-11: MIT] — `gh api repos/NoblerWorks-HQ/IRONSIGHT` → MIT, pushed 2026-04-26, 253 stars. Clean for steal-from.
- **URL 6 sightline license** [VERIFIED 2026-05-11: MIT] — `gh api repos/ni5arga/sightline` → MIT, pushed 2026-05-10, 355 stars. Clean.
- **URL 17 GeoSentinel license** [NEEDS MANUAL REVIEW 2026-05-11: NOASSERTION] — `gh api repos/h9zdev/GeoSentinel` → `NOASSERTION` (LICENSE file present but does not match a standard SPDX template). 908 stars, pushed 2026-04-25. Requires manual fetch + read of the LICENSE file before steal-from; not auto-resolvable.
- **URL 8 metabigor maintenance + license** [VERIFIED 2026-05-11: MIT, maintained] — `gh api repos/j3ssie/metabigor` → MIT, pushed 2026-02-15 (3 months stale but active OSINT project), 1.5k stars. License clean; maintenance acceptable for steal-from / reference.
- **URL 9 cti-expert license** [NEEDS MANUAL REVIEW 2026-05-11: NOASSERTION] — `gh api repos/7onez/cti-expert` → `NOASSERTION` (custom LICENSE file). 99 stars, pushed 2026-04-19. Requires manual fetch + read before adoption. Cemini-deployment-cost-estimate remains deferred until license clears.
- **URL 14 Spaceshift SateAIs API pricing tier + commercial-use-license** [NEEDS VERIFICATION 2026-04-29] — not a GitHub repo; vendor API pricing inquiry remains open. Defer until macro-event-from-satellite roadmap is active.

### Adoption summary (Cemini-pragmatic)

The 3 Adopts in Wave 4B fall into 3 maturity tiers:
1. **Already-deployed**: atomicmemory/llm-wiki-compiler (running on the librarian)
2. **Research-deferred**: 7onez/cti-expert (good fit if Cemini extends to event-driven OSINT; defer until that roadmap item is active)
3. **Aspirational**: Spaceshift SateAIs API (commercial API; integration cost analysis required first)

**Net Cemini-stack impact this session**: zero new immediate adoptions from Wave 4B. The wave functions more as **OSINT-roadmap-canvas** for future Cemini extensions than as immediate-deployment guidance.

## Snippets

> **The atomicmemory/llm-wiki-compiler reaffirmation (URL 2 evaluation excerpt)**:
>
> "The llm-wiki-compiler is an advanced command-line tool and Model Context Protocol (MCP) server engineered to automate the transformation of raw, unstructured data sources into a highly interlinked Markdown knowledge base… This compiler will operate as the primary daemon on the Hetzner CPX21 server. The llmwiki serve command must be configured as a persistent background process, exposing the official MCP server with a defined Tool Allowlist (e.g., kb_search_smart, kb_context, kb_read) on port 3838 over the Hetzner VPS Private Network." [Source: another Link Evaluation for Trading and Wiki Stacks 4_29.docx URL 2]

> **The microgpt.py Reference verdict (URL 3 evaluation excerpt — paraphrased per docx)**:
>
> Karpathy's microgpt.py gist (`8627fe009c40f57531cb18360106ce95`) is **Reference** — Karpathy is a high-trust source and the implementation is canonical-quality, but the gist is a pedagogical foundation for transformer training rather than an adoption candidate for Cemini's stack. The workspace already documents the Karpathy lineage via `@sources/llm-wiki.md` (the LLM-Wiki gist, different from this microgpt.py gist). Adding microgpt.py as a primary source would dilute the existing `karpathy` tag without adding deployment surface. [Source: another Link Evaluation for Trading and Wiki Stacks 4_29.docx URL 3 + workspace cross-reference]

> **OSINT-as-research-direction framing**:
>
> Wave 4B's effective output is mapping the OSINT extension space for Cemini, not adding immediate-deployment integrations. cti-expert, IRONSIGHT, sightline, GeoSentinel, GeoIntel collectively define a candidate `concepts/osint-event-driven-analysis.md` that would house Cemini's eventual macro-event-from-OSINT analyst node — but the corresponding Cemini-stack work is not yet on the roadmap.
