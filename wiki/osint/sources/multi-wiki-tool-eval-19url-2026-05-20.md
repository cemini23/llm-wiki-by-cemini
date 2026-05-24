---
title: "Multi-Wiki Tool Evaluation (K55, 19-URL batch, May 2026)"
type: source
tags: [source, tool-evaluation, multi-wiki, cross-wiki-routing, license-evaluation, k55]
keywords: [k55-tool-eval, 19-url-batch, ai-polymarket-agent, delive, src-hunter-skill, nexttrade-revisited, centpro, scalar-field, tugarecon, h4x-tools, bluehood, cf-hero, openhuman-eval, hackingtool-plugin, jarvis, super-spr, awesome-claude, the-book-of-secret-knowledge, edgesecurityaccess, ip-sale-readiness, license-spot-check]
related:
  - concepts/cemini-license-posture.md
  - concepts/tool-evaluation-framework.md
  - entities/tools/ai-polymarket-agent.md
  - entities/tools/centpro.md
  - entities/tools/scalar-field.md
  - entities/tools/nexttrade.md
  - sources/multi-wiki-tool-eval-36url-wiki-ingestion-2026-05-24.md
maturity: validated
read_status: deep-read
created: 2026-05-20
updated: 2026-05-20
clusters: [tool-evaluation]
---

## Relations
- @image-gen-wiki/briefs/2026-05-20_2026-05-20_k55-delive-asr-persona-ops.md  (cross-wiki brief)
- @cybersecurity-wiki/briefs/2026-05-20_2026-05-20_k55-tool-eval-cybersec-items.md  (cross-wiki brief)
- @ccc-wiki/briefs/2026-05-20_2026-05-20_k55-tool-eval-and-openhuman-ccc-items.md  (cross-wiki brief)

- @concepts/cemini-license-posture.md — license-hygiene policy referenced throughout the eval
- @concepts/tool-evaluation-framework.md — multi-wiki tier framework used here
- @entities/tools/ai-polymarket-agent.md — primary Cemini-financial adoption candidate from this batch
- @entities/tools/centpro.md — commercial closed-source Reject (the bot @stacyonchain promoted in Posts.docx K55)
- @entities/tools/scalar-field.md — YC commercial closed-source Reject
- @entities/tools/nexttrade.md — already in wiki from K54; eval URL 15 here re-evaluates it (Steal-from same verdict, but K54 already corrected the stack misidentification)

## Raw Concept

- **Title**: "Strategic Asset Evaluation for the Cemini Multi-Wiki Ecosystem"
- **Type**: LLM-generated tool evaluation report ("v4, May 2026", same template family as K51 / K53 / K54)
- **URLs**: 19
- **Length**: 583 lines (~3.0 MB docx, includes embedded figures)
- **Location**: `cemini-librarian:/opt/cemini-bulk/research/multi-wiki-tool-eval-prompt-19url-2026-05-20.docx`
- **Retrieved**: 2026-05-20 (dropped into `research to be indexed/`)

## Narrative

Fifth tool-evaluation batch in roughly a month (K49 / K50 / K51 / K53 / K54 → K55). Same scoring framework: Adopt / Steal-from / Defer / Reference-only / Reject / UNAVAILABLE, with a per-URL fit matrix across 7 surfaces (Cemini financial / OSINT wiki / Cybersec wiki / Image-gen wiki / SEO wiki / 3D-printing wiki / CCC wiki).

### Verdict rollup

**3 Adopt** / **4 Steal-from** / **2 Defer** / **4 Reference-only** / **3 Reject** / **1 UNAVAILABLE** across 19 URLs.

| Tier | Count | URLs |
|---|---|---|
| **Adopt** | 3 | ai-polymarket-agent (Cemini-fin + CCC), DeLive (CCC + image-gen + OSINT secondary), src-hunter-skill (Cybersec + CCC) |
| **Steal-from** | 4 | tugarecon (Cybersec), bluehood (Cybersec), H4X-Tools (OSINT + Cybersec), NextTrade (Cemini-fin) |
| **Defer** | 2 | hackingtool-plugin (CCC + Cybersec), J.A.R.V.I.S (CCC) |
| **Reference-only** | 4 | osint_stuff_tool_collection (OSINT), awesome-claude (CCC), Windows-Terminal-Guide (CCC + Cybersec), the-book-of-secret-knowledge (CCC + Cybersec) |
| **Reject** | 3 | Scalar Field (none — YC closed-source SaaS), CentPRO (none — Windows binary subscription), CF-Hero (none — Apache-2.0 noted but Cloudflare-origin-disclosure ToS risk) |
| **UNAVAILABLE** | 1 | EdgeSecurityAccess (404, repo deleted/private) |

### License pattern

- **NO LICENSE FOUND**: 6 (Scalar Field, hackingtool-plugin, CentPRO, osint_stuff_tool_collection, J.A.R.V.I.S, H4X-Tools — though some of these are markdown-document repos where "no license" is materially different from "no license on executable code")
- **UNVERIFIED**: 1 (awesome-claude — eval flagged a LICENSE reference in its schema but couldn't confirm SPDX)
- **GNU GPLv3 (poison-pill for IP-sale)**: 2 (tugarecon, the-book-of-secret-knowledge — confirmed by eval; the latter's license-status was contested in K42, see Dead Ends below)
- **MIT**: 5 (ai-polymarket-agent, bluehood, NextTrade, src-hunter-skill, +1 other)
- **Apache-2.0**: 2 (DeLive, CF-Hero)
- **BSD-3-Clause**: 1 (super/SPR)
- **UNAVAILABLE**: 1 (EdgeSecurityAccess)
- **UNVERIFIED+unknown**: 1 (Bytez docs — eval claimed serverless model-inference API surface, license status unclear)

**Per K53/K54 verified failure mode**: the "NO LICENSE FOUND" label is a retrieval artifact a non-trivial fraction of the time. Spot-check via GitHub API (`/repos/{owner}/{repo}/license`) is mandatory before final Reject. See `Dead Ends` below and the K53 license-check follow-up pattern in `@concepts/cemini-license-posture.md`.

### Critical findings for the Cemini/OSINT side

#### 1. `kaktusesquire6rmu/ai-polymarket-agent` — Adopt, Cemini-fin primary (eval URL 5)

**The most important Cemini-relevant finding in this batch.** Comprehensive production-grade MCP server connecting AI agents directly to Polymarket: standard stdio transport; AI-utility functions including `search_markets`, `get_market_odds` (using Polymarket-specific `conditionId` parameters); FastAPI + Web3.py event-driven structure; MIT-licensed. 671 stars. The eval's verdict matches Cemini's existing Polymarket-MCP-server line (already includes `caiovicentino-polymarket-mcp-server` from K30 Wave 5).

**Note**: the eval flags this as "Adopt" but the wiki already has equivalent or overlapping coverage:
- `@entities/tools/polymarket-agents.md` — Polymarket's *own* official MIT-licensed framework (eval URL 5's `Polymarket/agents` references this in its "Works cited" #11)
- `@entities/tools/caiovicentino-polymarket-mcp-server.md` — K30 Adopt MCP-server bridge

The `kaktusesquire6rmu/ai-polymarket-agent` repo (NOT the same as `Polymarket/agents`) is a third party building on top of the official framework. Need to check if it offers anything the existing wiki entries don't — particularly `search_markets` / `get_market_odds` ergonomics. → new entity page created (`@entities/tools/ai-polymarket-agent.md`); spot-check needed before Phase-0 audit.

#### 2. `XimilalaXiang/DeLive` — Adopt, CCC + image-gen + OSINT secondary (eval URL 16)

Apache-2.0 Electron + React + TS desktop app. Captures local system audio, translates to real-time subtitles using 12 ASR backends / 60+ languages. Exposes MCP server + configurable Agent Skill (disabled by default, Bearer auth) for Claude Code access to system transcription contexts. Adoptable. Routed to CCC wiki brief (primary fit); also useful for OSINT (audio→text → wiki ingestion of meeting/interview material) and image-gen wiki (persona-ops voice/TTS synchronization).

#### 3. `MyuriKanao/src-hunter-skill` — Adopt, Cybersec + CCC (eval URL 18)

MIT Claude Code skill for bug-bounty / SRC / penetration testing. 305 structured payloads, 19 attack playbooks, 263 WAF bypass variants, integrates `jshookmcp` MCP server for browser manipulation + Frida memory validation + WASM RE. Off-topic for OSINT financial research → routed to **both** ccc-wiki (as a SKILL.md design exemplar) and cybersecurity-wiki (as an offensive-security tooling adoption) briefs.

#### 4. `austin-starks/NextTrade` — Steal-from, Cemini-fin (eval URL 15)

Re-evaluation of a tool already in the wiki since K54 (`@entities/tools/nexttrade.md`). The K55 eval **repeats** the K54 stack-misidentification (claims Python; the repo is TypeScript) — see existing K54 page for verified facts. K55 verdict (Steal-from for genetic-algorithm hyperparameter-optimization math) matches K54's downgraded verdict. **No change** to the existing entity page; logged here as a verification datapoint that the K55 eval is making the same retrieval errors as prior batches.

#### 5. `centpro.bot` — Reject, **explicitly the bot promoted in Posts.docx K55 Post 4** (eval URL 4)

CentPRO is the `centpro.bot` Windows application promoted by @stacyonchain in the Posts.docx K55 batch. The eval correctly identifies it as: closed-source, $49/month or $120 lifetime, delivered as compressed archive via Telegram, Windows binary, no Linux/Python integration path, vendor-lock-in supply-chain risk. Hard Reject. → new entity page `@entities/tools/centpro.md` records the Phase-0 NO-GO with the cross-link to the @stacyonchain promotion.

#### 6. `scalarfield.io` — Reject, YC closed-source SaaS (eval URL 1)

Y-Combinator Spring 2025 company building an "agentic trading desk" — a closed-source competitor to what Cemini is itself building. Reject for both architectural (vendor lock-in) and IP-sale-readiness reasons. Worth a stub entity page as a competitive-intelligence marker.

#### 7. `KochiyaSanaeNya/EdgeSecurityAccess` — UNAVAILABLE (eval URL 19)

GitHub 404 — repo deleted or set to private. No further action. Eval correctly refused to synthesize from cached data (anti-hallucination discipline).

### Cross-wiki routing (4 destination briefs needed)

Most of this batch is **cybersec-primary** (6/19) or **CCC-primary** (7/19), not OSINT. Briefs created via `cross_wiki_route.py`:

| Target wiki | URLs (Adopt/Steal-from/Defer/Ref) |
|---|---|
| cybersecurity-wiki | tugarecon (Steal), bluehood (Steal), H4X-Tools (Steal), src-hunter-skill (Adopt), hackingtool-plugin (Defer), super-SPR (Steal), Windows-Terminal-Guide (Ref), the-book-of-secret-knowledge (Ref), CF-Hero (Reject — but reverse-proxy origin discovery is cybersec-relevant) |
| ccc-wiki | ai-polymarket-agent (Adopt, secondary fit), DeLive (Adopt), src-hunter-skill (Adopt), awesome-claude (Ref), hackingtool-plugin (Defer), J.A.R.V.I.S (Defer), the-book-of-secret-knowledge (Ref), Windows-Terminal-Guide (Ref) |
| image-gen-wiki | DeLive (Adopt, ASR for persona-ops) |
| seo-wiki | (none — no SEO-primary items in this batch) |

OSINT-side entity pages created in this wiki: ai-polymarket-agent (primary Adopt), CentPRO (Reject; cross-references the @stacyonchain Posts.docx promotion), Scalar Field (Reject stub for competitive-intel tracking).

### Dead Ends

**The eval re-makes the K53/K54 NO-LICENSE-FOUND false-negative pattern**. From K53 follow-up: 5 of the eval's NO-LICENSE-FOUND items turned out to have clean licenses on GitHub API spot-check. K55 has 6 items in this state — they need GitHub-API verification before being treated as licensing rejects. Specifically:
- `cipher387/osint_stuff_tool_collection` (eval URL 6) — 7,875★ markdown-document repo; the "NO LICENSE" matters less because the artifact is a list of external URLs, but verify before fork.
- `vil/H4X-Tools` (eval URL 14) — Python OSINT toolkit, eval says NO LICENSE but classed as Steal-from anyway; verify SPDX.
- `AKCodez/hackingtool-plugin` (eval URL 3) — 1★, low-traction; license verification less urgent given the Defer tier.
- `GauravSingh9356/J.A.R.V.I.S` (eval URL 13) — verify before any code lift.
- `JSONbored/awesome-claude` (eval URL 7) — eval flagged UNVERIFIED; GitHub API will return SPDX if present.
- `scalarfield.io` + `centpro.bot` — Reject regardless, no license check needed (commercial closed products).

**This is logged as a recurring Dead End in `@concepts/cemini-license-posture.md`** — the no-license-default of the LLM-eval template is unreliable enough that license-check should be a mandatory post-ingest pass.

## Snippets

> "Adopt: 3 (ai-polymarket-agent, DeLive, src-hunter-skill); Steal-from: 4 (tugarecon, bluehood, H4X-Tools, NextTrade); Defer: 2 (hackingtool-plugin, J.A.R.V.I.S); Reference-only: 4 (osint_stuff_tool_collection, awesome-claude, Windows-Terminal-Guide, the-book-of-secret-knowledge); Reject: 3 (Scalar Field, CentPRO, CF-Hero); UNAVAILABLE: 1 (EdgeSecurityAccess)" [Source: Multi-Wiki Tool Evaluation Prompt.docx — Aggregate summary]

> "License pattern summary: NO LICENSE FOUND: 6; Poison-pill licenses caught: 2 (GNU GPLv3, GPL-3.0 License); Clean MIT / Apache / BSD: 10" [Source: Multi-Wiki Tool Evaluation Prompt.docx — License pattern summary]

> "CentPRO operates as a fully automated, local Windows application that executes pre-built trading logic on short-term prediction markets ... a compressed archive via an automated Telegram system. ... Relying on an opaque Windows binary completely circumvents internal security audits and violates the IP-sale readiness protocols." [Source: Multi-Wiki Tool Evaluation Prompt.docx — URL 4 reasoning]

> "The ai-polymarket-agent provides a comprehensive, production-grade developer framework engineered to interface AI agents directly with Polymarket via the Model Context Protocol (MCP). ... Protected by a highly permissive MIT License, the framework can be adopted immediately, heavily customized, and fully integrated into the proprietary intellectual property portfolio without legal friction." [Source: Multi-Wiki Tool Evaluation Prompt.docx — URL 5 reasoning]
