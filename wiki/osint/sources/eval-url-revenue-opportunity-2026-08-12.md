---
title: "Eval — Revenue Opportunity URL Evaluation 2026-08-12 (20-URL)"
type: source
tags: [eval, phase-0, k233, atto, guruwatcher, ccc, cyber]
keywords: [quotio, sentrux, watermarks-remover, reasoning-bank, crewlet, ai-reads-books, n8n-terry-guide, shieldbreak, agents-from-scratch, clapgrep, iron-proxy, spr-super, guppylm, anydoc, ext-anydoc, cariddi, opencodex, codex-self-improving-loop, courselit, tunnelto]
related:
  - entities/tools/anydoc.md
  - entities/tools/opencodex.md
  - entities/tools/iron-proxy.md
  - entities/tools/clapgrep.md
  - entities/tools/tunnelto.md
  - entities/tools/cariddi.md
  - entities/tools/quotio.md
  - entities/tools/sentrux.md
  - entities/tools/reasoning-bank.md
  - entities/tools/codex-self-improving-loop.md
  - concepts/cemini-license-posture.md
  - concepts/active-project-research-routing.md
  - sources/eval-url-revenue-opportunity-2026-08-11.md
  - sources/deep-research-url-evaluation-2026-08-13.md
  - sources/eval-url-revenue-opportunity-2026-08-14.md
maturity: draft
created: 2026-08-12
updated: 2026-08-14
read_status: read
---

## Relations

- @entities/tools/anydoc.md — GO Integrate (Atto doc parsing, MIT)
- @entities/tools/opencodex.md — GO Integrate (CCC multi-model proxy, MIT)
- @entities/tools/iron-proxy.md — GO Integrate (cyber lab egress, Apache-2.0)
- @entities/tools/clapgrep.md — GO Extract (Atto deep-PDF search, GPL-3.0 subprocess)
- @entities/tools/tunnelto.md — GO Extract (Atto vault sharing, MIT)
- @entities/tools/cariddi.md — Extract (cyber secret regex, GPL-3.0)
- @entities/tools/quotio.md — Extract (CCC API quota proxy, MIT)
- @entities/tools/sentrux.md — Extract (Atto/GW code quality gate, MIT)
- @entities/tools/reasoning-bank.md — WATCH (CCC, Apache-2.0)
- @entities/tools/codex-self-improving-loop.md — Extract (CCC memory schema, NOASSERTION)
- @concepts/cemini-license-posture.md
- @concepts/active-project-research-routing.md
- @sources/eval-url-revenue-opportunity-2026-08-11.md
- @sources/deep-research-url-evaluation-2026-08-13.md — K235 next 20-URL batch (different URL set)

## Raw Concept

| Field | Value |
|-------|--------|
| File | `Revenue Opportunity URL Evaluation.docx` |
| sha256 | `bd016f28999d82b80350779f67d3649494d309ab5063c0d1a40c3b4fd5bd33bb` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/Revenue Opportunity URL Evaluation.docx` |
| retrieved | 2026-08-12 |
| URLs evaluated | 20 |
| Theme | Agentic workflow optimization, document parsing for archives, local AI security isolation |

## Narrative

20-URL revenue-opportunity evaluation, batch-theme "agentic workflow optimization, document parsing for archives, and local AI security isolation." Docx license claims were **never trusted** — re-verified via `gh api repos/<owner>/<repo>` (full table in `[Source: .local/reports/license-spot-check-2026-08-12-0825.txt]`).

### Verdict aggregate (with license re-verification)

| Tier | Count | URLs |
|------|-------|------|
| Integrate | 3 | **anydoc** (MIT ✓), **iron-proxy** (Apache-2.0 ✓), **opencodex** (MIT ✓) |
| Extract | 8 | Quotio (MIT), Sentrux (MIT), AI-reads-books (MIT), ShieldBreak (MIT), clapgrep (GPL-3.0), cariddi (GPL-3.0), codex-self-improving-loop (NOASSERTION), tunnelto (MIT) |
| Watch | 4 | reasoning-bank (Apache-2.0), spr-networks/super (BSD-3-Clause), courselit (AGPL-3.0), (+ n8n-terry-guide) |
| Context | 4 | watermarks-remover (MIT), n8n-terry-guide (NOASSERTION), agents-from-scratch (MIT), ShieldBreak (MIT, also Context) |
| Pass | 3 | Crewlet (SaaS), guppylm (NOASSERTION), ext-anydoc (PHP bindings, MIT) |

Docx claimed `NOT FOUND` for several licenses that gh api actually resolves (e.g. quotio → MIT, ShieldBreak → MIT, agents-from-scratch → MIT) — reproducing the systematic "NO LICENSE FOUND false-negative" pattern already documented in K53/K54. Trust gh api, not docx.

### Integrate-tier Phase-0 verdicts

- **anydoc** (`firecrawl/anydoc`, MIT, 14,856★, 0.7MB, pushed 2026-08-10) — **GO Integrate (Atto)**. Rust lib + CLI + Node/Py bindings + Agent Skill converting PDF/DOCX/PPTX/XLSX/ODT/RTF/EPUB/CSV → GFM Markdown in single-digit ms, fully local. Caveat: text-layer-only — rasterized scans (Italian civil records are scanned) still need the HTR/OCR path (Transkribus per Atto constraints). Do not use anydoc as OCR replacement.
- **iron-proxy** (`paradigmxyz/iron-proxy`, Apache-2.0, 596★, 3.3MB, active) — **GO Integrate (cyber lab)**. Go single-binary MITM egress proxy + DNS server, default-deny, boundary secret injection (proxy tokens swapped at egress), upstream IP deny list (SSRF/IMDS protection), streaming-aware, PostgreSQL MITM w/ RLS. Directly hardens agent-sandbox egress in the local-abliterated-lab.
- **opencodex** (`lidge-jun/opencodex`, MIT, 9,505★, 93MB, pushed today) — **GO Integrate (CCC)**. Local provider proxy translating OpenAI Codex Responses API ↔ Anthropic/Gemini/Grok/GLM/DeepSeek/Kimi/Qwen/Ollama; works with Codex CLI/App/SDK, Claude Code, Claude Desktop, Grok Build; account-pooling + dashboard on :10100. 175MB depth-1 clone (asset-heavy); watch upstream API-schema breakage.

### Extract-tier pattern notes

Rejects/pass aggregate here (no reject-stub farm). Extract = steal-from pattern, no binary adoption:
- **clapgrep** (GPL-3.0) — run as isolated CLI subprocess only (GPL static-link friction); deep search inside text-layer PDFs for Atto surname/geo lookups.
- **tunnelto** (MIT) — ephemeral public URLs for client vault previews; enforce automated teardown (PII exposure risk).
- **cariddi** (GPL-3.0) — reuse the 500+ secret-detection regex signatures internally, do not deploy crawler against external targets.
- **quotio** (MIT) — native macOS multi-provider quota/auto-failover proxy; pattern relevance for the llm-routing failover lane; do not route Atto PII through unverified endpoints.
- **sentrux** (MIT) — pure-Rust real-time architectural sensor / code-quality gate; useful as a pre-commit quality gate for AI-generated code in Atto/GW.
- **codex-self-improving-loop** (NOASSERTION — no clean SPDX) — durable markdown memory schema (PROFILE.md/ACTIVE.md) as a pattern for agent-session state; no code adoption.
- **AI-reads-books-page-by-page** (MIT) — sliding-window chunking + progressive summarization for long PDF archives; LLM hallucination risk requires human-gate.
- **ShieldBreak** (MIT) — Windows Defender evasion POC; cybersec-lab context only, network-isolated.

### Watch notes

- **reasoning-bank** (Apache-2.0) — MaTTS memory-aware test-time scaling; compute-heavy, watch for lighter adoption.
- **spr-networks/super** (BSD-3-Clause) — per-device WiFi VLAN isolation; blocked by hardware transition friction; extract nftables patterns.
- **courselit** (AGPL-3.0) — self-hosted LMS for Atto playbook; AGPL backend open-sourcing friction; activate only if SaaS fees become prohibitive.
- **n8n-terry-guide** (NOASSERTION) — self-healing homelab workflows w/ Telegram HITL gate; context only (blast radius too high for integration).

[Source: Revenue Opportunity URL Evaluation.docx] · [Source: .local/reports/license-spot-check-2026-08-12-0825.txt]
