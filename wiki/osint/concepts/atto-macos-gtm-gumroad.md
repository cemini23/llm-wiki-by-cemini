---
title: Atto macOS GTM — Gumroad personas, pricing, listing
type: concept
tags: [concept, genealogy, atto, gtm, gumroad, macos, k185, draft]
keywords: [lifetime license, $49, $89, DIY jure sanguinis, notarization, Cloudflare Access, UPL]
related:
  - concepts/italian-citizenship-latam-audience-systems.md
  - entities/tools/instatic.md
  - sources/newsletter-rss-sparktoro-2026-07-24-brand-mentions.md
  - sources/gemini-atto-macos-gtm-2026-07-22.md
  - sources/gemini-atto-threat-model-2026-07-22.md
  - sources/gemini-italian-citizenship-software-map-2026-07-22.md
  - concepts/atto-local-first-threat-model.md
  - concepts/gpuology-genealogy-agent-kit.md
  - concepts/italian-citizenship-pathways-document-pipelines.md
  - concepts/italian-citizenship-youtube-soft-flags.md
  - concepts/italian-citizenship-primary-law-lock.md
  - sources/youtube-italian-citizenship-channels-2026-07-22.md
  - sources/gemini-gpuology-genealogy-business-analysis-2026-07-20.md
  - sources/atto-commercial-migration-plan-2026-07-23.md
  - sources/software-licensing-architecture-research-2026-07-23.md
  - sources/gemini-atto-landing-conversion-2026-07-23.md
  - sources/gemini-atto-acquisition-strategy-2026-07-23.md
  - sources/gemini-atto-marketing-compliance-2026-07-23.md
  - sources/gemini-atto-pricing-presentation-2026-07-23.md
  - concepts/youratto-lean-conversion-page.md
  - concepts/youratto-brand-identity.md
  - sources/gemini-atto-brand-identity-2026-07-24.md
  - entities/tools/licenseseat.md
  - entities/tools/license-guard-rs.md
  - sources/eval-url-revenue-cyber-agent-harness-2026-08-03.md
  - entities/tools/marketing-team-eve-template.md
maturity: draft
created: 2026-07-22
updated: 2026-08-03
---

## Relations

- @sources/eval-url-revenue-cyber-agent-harness-2026-08-03.md — K220 cyber/agent-harness revenue eval

- @concepts/italian-citizenship-latam-audience-systems.md — K203 LatAm GTM audiences

- @entities/tools/instatic.md — K195 Watch

- @sources/newsletter-rss-sparktoro-2026-07-24-brand-mentions.md — K193 brand-mention watch

- @concepts/youratto-brand-identity.md — K194 folio stack; Gumroad cover uses winning accent

- @sources/gemini-atto-brand-identity-2026-07-24.md — brand DR

- @concepts/youratto-lean-conversion-page.md — K192 lean youratto.com spine ($299 kit)

- @sources/gemini-atto-landing-conversion-2026-07-23.md — K192 CRO teardown

- @sources/gemini-atto-acquisition-strategy-2026-07-23.md — K192 organic GTM

- @sources/gemini-atto-marketing-compliance-2026-07-23.md — K192 claim fence

- @sources/gemini-atto-pricing-presentation-2026-07-23.md — K192 $299 kit framing

- @entities/tools/license-guard-rs.md — K191 Ed25519 Extract

- @entities/tools/licenseseat.md — K191 soft-gate candidate

- @sources/atto-commercial-migration-plan-2026-07-23.md — K191 MoR/LicenseSeat plan

- @sources/gemini-atto-macos-gtm-2026-07-22.md — primary DR (K185)
- @sources/gemini-atto-threat-model-2026-07-22.md — privacy claims must survive SECURITY checklist
- @sources/gemini-italian-citizenship-software-map-2026-07-22.md — UPL / never-claim copy for listing
- @concepts/atto-local-first-threat-model.md — privacy claims in listing must match controls
- @concepts/gpuology-genealogy-agent-kit.md — product wedge this GTM sells
- @concepts/italian-citizenship-pathways-document-pipelines.md — DIY persona cost/risk driver
- @concepts/italian-citizenship-youtube-soft-flags.md — anti-position vs YouTube eligibility CTAs
- @concepts/italian-citizenship-primary-law-lock.md — K187 court/statute copy boundaries
- @sources/youtube-italian-citizenship-channels-2026-07-22.md — ICA/IDCA competitor voice map
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

## K191 commercialization deltas (2026-07-23)

- Prefer **owned site + Stripe Checkout** over long-term Gumroad / MoR for day one (operator: US-heavy buyers, English-only app). Enable **Stripe Tax** when nexus/VAT registration is real. MoR (Lemon/Polar/Paddle) = later adjust if intl share or tax ops dominate.
- Soft-gate offline licensing via **LicenseSeat** (Ed25519 machine files, Stripe webhooks) — not hard DRM; pair with `license-guard-rs` reference.
- **macOS notarytool first**; defer Windows SmartScreen/Azure Trusted Signing to closed beta.
- Do not copy fund-industry dark-pattern personalization (Klement RSS contrast).

## K192 lean site deltas (2026-07-23)

- Live **youratto.com** sells **DIY kit — $299** (supersedes $49/$89 as primary public price for now).
- Full multi-page marketing site **deferred** — ship lean conversion spine only (@concepts/youratto-lean-conversion-page.md).
- Gemini DR pentad ingested: landing CRO · demo production · compliance · pricing · acquisition.
- Resolve before FAQ publish: ship **30-day** refund (Opus fact-check; match T&Cs); never claim Windows until shipped; avoid “automated lineage validation” / eligibility CTAs; drop Screen Studio OTP price anchor.
