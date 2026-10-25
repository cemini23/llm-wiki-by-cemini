---
title: Firecrawl Government & Legal Index — zero-credit US law search
type: entity
tags: [tool, osint, firecrawl, legal, atto, pm-canary]
keywords: [firecrawl gov-index, firecrawl_gov_search, US statutes, vital records, apostille]
related:
  - tools/firecrawl.md
  - tools/firecrawl-mcp-server.md
  - sources/eval-multi-wiki-link-revenue-v10.9-2026-10-25.md
maturity: draft
created: 2026-10-25
updated: 2026-10-25
phase_0_verdict: GO — client verified
wire_status: integrate
wire_note: firecrawl_gov_search MCP tool for atto-mcp; five-field citation check before any statute is treated as fact.
---

## Raw Concept

Phase-0 on the Firecrawl Alexandria Government & Legal Index, 2026-10-25. Source: v10.9 multi-wiki link evaluation, URL 17, scored Extract (OSINT primary).

## Narrative

| Field | Value |
|-------|-------|
| **Product** | Firecrawl Alexandria — Government & Legal Index |
| **URL** | https://www.firecrawl.dev/gov-index |
| **Client repo** | https://github.com/firecrawl/cli (verified 2026-10-25) |
| **License** | Proprietary hosted service. Free, zero-credit tier for gov-index calls. CLI is open source. |
| **Coverage** | 30M+ US federal, state, county, municipal pages |
| **Verdict** | GO — client integration only |

### What it returns

Verbatim quote, document-type label (statute / regulation / agency guidance / court opinion / municipal code / fee schedule), canonical citation ID (e.g. `us:usc:42:1983`), and citation-graph links to controlling authority.

### Phase-0 verification

`firecrawl/cli` cloned 2026-10-25. Confirmed: `src/types/gov.ts`, `src/__tests__/alexandria-beta.test.ts`, and a `skills/firecrawl-alexandria` skill. The gov index is a real, shipped surface of the client.

Note: `firecrawl/firecrawl-js` does not exist — the CLI repo is `firecrawl/cli`.

### Where it lands

- **Atto** — US jure sanguinis concierge work needs state vital-record release statutes, county clerk fee schedules, apostille rules, and declaratory-judgment procedures. This covers the US half of those cases.
- **PM LP canary** — regulatory resolution verification for market settlement criteria.

### The guard that matters

The index mixes **binding** statutes with **non-binding** agency FAQs and press releases. An agent that reads a label without checking it will cite an FAQ as law.

Vaquill's five-field check must gate every result before it becomes a fact:

1. Official publisher domain
2. Capture date
3. Document-type binding label
4. Hierarchy and effective date
5. Verbatim quote plus canonical citation ID

Also: the index covers **US jurisdictions only**. It says nothing about Italian law. Atto's Italian side is unaffected.

## Snippets

> "gov-index covers only US federal, state, and local jurisdictions (not Italian law) and mixes binding statutes/regulations with non-binding agency FAQs and press releases" — source report, URL 17

## Dead Ends

- Assuming an agency FAQ is a statute. The label is present but an agent must read it.
