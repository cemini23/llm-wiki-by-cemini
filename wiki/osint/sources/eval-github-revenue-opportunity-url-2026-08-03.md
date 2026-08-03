---
title: "Eval — Revenue Opportunity URL Analysis 2026-08-03"
type: source
tags: [tool-eval, atto, guruwatcher, seo, k219]
keywords: [memvid, jobseek, whatsapp-mcp, future-agi, a11y, bettercap, uber-adr, agentic-soc]
related:
  - concepts/wiki-tooling-evaluation.md
  - concepts/cemini-license-posture.md
  - concepts/gpuology-genealogy-agent-kit.md
  - entities/tools/memvid.md
  - entities/tools/jobseek.md
maturity: draft
created: 2026-08-03
updated: 2026-08-03
read_status: deep-read
---

## Relations
- @seo-wiki/briefs/2026-08-03_k219-a11y-pass-legacy-tooling.md  (cross-wiki brief)

- @concepts/wiki-tooling-evaluation.md
- @concepts/cemini-license-posture.md
- @concepts/gpuology-genealogy-agent-kit.md
- @entities/tools/memvid.md
- @entities/tools/jobseek.md

## Raw Concept

| Field | Value |
|-------|--------|
| Title | Revenue Opportunity URL Analysis.docx |
| sha256 | `90e25c795a0ac6ab99ab2478b33975d4bcfff18a320221e197dff2b31659ba66` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/Revenue Opportunity URL Analysis.docx` |
| URLs | 20 (a11y / memory / MCP / SOC / networking) |
| read_status | deep-read |

## Narrative

Batch theme: AI memory, agentic security, MCP bridges, legacy a11y. Priority #1 Atto / #2 GuruWatcher.

| Repo | Eval tier | SPDX (`gh` 2026-08-03) | Cemini verdict |
|------|-----------|------------------------|----------------|
| a11y Pass×6 (tota11y, a11y, a11y.css, accessibility-fails, axe-cli, TheA11yMachine) | Pass | mixed / archived | **Pass → SEO wiki** — no active-stack extract |
| colophon-group/jobseek | Extract | **MIT** code + **CC BY-NC 4.0** data | **GO Extract** GuruWatcher poll→Discord alert patterns only — Phase-0 (~64MB); **no commercial use of job data** |
| memvid/memvid | Integrate | **Apache-2.0** | **GO Integrate REFERENCE** Atto single-file agent memory (Rust) — Phase-0 (~13MB) |
| lharries/whatsapp-mcp | Watch | **MIT** | **Watch** — PII / prompt-injection risk for Atto WhatsApp concierge |
| future-agi/future-agi | Watch | **Apache-2.0** | **Watch** — heavy infra vs local-first Atto |
| openhack / antivibe / FunnyWolf/agentic-soc-platform / bettercap / uber/ADR | Context | mixed (see spot-check) | Cybersec/CCC context only |
| motion.so, NeuroPurple, ghosttrace, gx10-token-tracker, loopx | UNAVAILABLE | — | No stub farm |

**License spot-check 2026-08-03** (do not trust docx SPDX alone): memvid **Apache-2.0**; jobseek **MIT** (+ CC BY-NC data); whatsapp-mcp **MIT**; future-agi **Apache-2.0**; bettercap **NOASSERTION**; agentic-soc **null SPDX → NO-GO adopt**; uber/ADR **Apache-2.0**.

## Snippets

> Integrating Memvid … collapsing complex vector databases and BM25 indices into a single, offline .mv2 file written in Rust … encrypt these single-file capsules with AES-256-GCM (.mv2e). [Source: Revenue Opportunity URL Analysis.docx]

> Jobseek … resilient, fault-tolerant extraction from complex DOM structures is directly applicable to GuruWatcher. [Source: Revenue Opportunity URL Analysis.docx]
