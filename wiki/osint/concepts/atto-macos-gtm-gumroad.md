---
title: Atto macOS GTM — Gumroad personas, pricing, listing
type: concept
tags: [concept, genealogy, atto, gtm, gumroad, macos, k185, draft]
keywords: [lifetime license, $49, $89, DIY jure sanguinis, notarization, Cloudflare Access, UPL]
related:
  - sources/gemini-atto-macos-gtm-2026-07-22.md
  - sources/gemini-atto-threat-model-2026-07-22.md
  - sources/gemini-italian-citizenship-software-map-2026-07-22.md
  - concepts/atto-local-first-threat-model.md
  - concepts/gpuology-genealogy-agent-kit.md
  - concepts/italian-citizenship-pathways-document-pipelines.md
  - sources/gemini-gpuology-genealogy-business-analysis-2026-07-20.md
maturity: draft
created: 2026-07-22
updated: 2026-07-22
---

## Relations

- @sources/gemini-atto-macos-gtm-2026-07-22.md — primary DR (K185)
- @sources/gemini-atto-threat-model-2026-07-22.md — privacy claims must survive SECURITY checklist
- @sources/gemini-italian-citizenship-software-map-2026-07-22.md — UPL / never-claim copy for listing
- @concepts/atto-local-first-threat-model.md — privacy claims in listing must match controls
- @concepts/gpuology-genealogy-agent-kit.md — product wedge this GTM sells
- @concepts/italian-citizenship-pathways-document-pipelines.md — DIY persona cost/risk driver
- @sources/gemini-gpuology-genealogy-business-analysis-2026-07-20.md — earlier market framing (K176)

## Raw Concept

How to position and sell Atto on Gumroad as a **pay-once macOS utility** — personas, tiers, listing outline, demo script, and claim boundaries — without practicing law or promising scrape/auto-merge magic.

## Narrative

### Personas

| Segment | JTBD | Price elasticity note |
|---------|------|------------------------|
| DIY jure sanguinis | Flawless document chain; avoid €600 + year loss | Tool ≪ single apostille/translation |
| Privacy genealogist | Evidence tree; no cloud auto-merge | Expects perpetual license (MacFamilyTree-class) |
| Independent consultant | Multi-client vaults; billable efficiency | Pro tier + commercial rights |

### Pricing (working thesis)

| Tier | Price | Includes |
|------|-------|----------|
| Standard (lifetime) | ~$49 | App + vault + checklists + local AI suggest |
| Pro / Consultant | ~$89 | + CLI wheel, multi-vault, commercial use |

Major-version lifetime; no monthly SaaS for core utility. Pack: notarized Universal `.dmg` · Setup PDF · Cloudflare family-share primer · Pro CLI wheel.

### Listing spine

1. **Headline:** local-first command center for Italian genealogy  
2. **Reality check:** non-refundable fees + discrepancy cost  
3. **Features:** vault sovereignty · Approve-only merge · citizenship checklists · optional Access share  
4. **This is / isn’t:** organizer ≠ attorney; sidecar ≠ scraper; suggest ≠ auto-merge  
5. **FAQ:** Ancestry contrast · no Terminal · no eligibility verdict · no cloud SSNs · migrate by copying `~/AttoVault` · 14-day refund  

### Ship gates

- Apple Developer ID + notarize + staple before Gumroad upload (`spctl -a -v` accepted)
- Marketing language passes UPL / AI-hallucination constraints (@concepts/italian-citizenship-pathways-document-pipelines.md status vocab)
- Privacy FAQ matches @concepts/atto-local-first-threat-model.md

Fee/law citations in the DR remain **[NEEDS VERIFICATION 2026-07-22]** before paid ads or hard fee claims on the listing.
