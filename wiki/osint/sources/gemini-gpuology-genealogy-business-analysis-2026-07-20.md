---
title: GPUOLOGY Genealogy Business Analysis.docx (Gemini DR, 2026-07-20)
type: source
tags: [source, genealogy, product, gpuology, gemini-deep-research, k176, docx]
keywords: [jure sanguinis, Ancestry ToS, FamilySearch API, Cloudflare Access, Topola, Transkribus, Civile Sprints]
related:
  - concepts/gpuology-genealogy-agent-kit.md
  - concepts/computational-genealogy-archival-automation.md
  - concepts/italian-regional-genealogy-archive-playbook.md
  - entities/tools/familysearch-platform-api.md
  - entities/tools/gcerretani-antenati.md
  - entities/tools/topola-viewer.md
  - entities/tools/transkribus.md
  - entities/tools/autoresearch-genealogy.md
  - entities/tools/codice-fiscale-js.md
  - entities/tools/censusreporter.md
  - entities/tools/timemagazine-babynames.md
  - entities/tools/dhfbk-tint.md
  - concepts/active-project-research-routing.md
maturity: draft
read_status: read
created: 2026-07-20
updated: 2026-07-20
clusters: [genealogy, k176-ingest]
---

## Relations

- @concepts/gpuology-genealogy-agent-kit.md — product strategy synthesis (this ingest)
- @concepts/computational-genealogy-archival-automation.md — technical stack overlap
- @concepts/italian-regional-genealogy-archive-playbook.md — jure sanguinis / stato civile wedge
- @entities/tools/familysearch-platform-api.md — BYO-auth + compatibility review
- @entities/tools/gcerretani-antenati.md — IIIF / Antenati personal-use posture
- @entities/tools/topola-viewer.md — Cloudflare static viewer / .gdz
- @entities/tools/transkribus.md — HTR partner (Organisation API)
- @entities/tools/autoresearch-genealogy.md — prompt kit Extract for agent pack
- @entities/tools/codice-fiscale-js.md — K175 comune matrix (kit extract)
- @entities/tools/censusreporter.md — K175 US census staging extract
- @entities/tools/timemagazine-babynames.md — K175 SSA name priors
- @entities/tools/dhfbk-tint.md — K175 Italian NLP (private; ~1.2 GB RSS)
- @concepts/active-project-research-routing.md — family-tree co-primary

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | GPUOLOGY: Market Viability, Technical Feasibility, and Strategic Wedge Analysis |
| **Type** | Gemini Deep Research deliverable (operator prompt 2026-07-20) |
| **sha256** | `b2f2ab00d77cce141110b5d67c5f759b746fefb22032bcfb3b88cdf319342d0d` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/GPUOLOGY Genealogy Business Analysis.docx` |
| **Companion brief** | `briefs/2026-07-20_gpuology-product-brief.md` |
| **Companion prompt** | `briefs/2026-07-20_gpuology-gemini-deep-research-prompt.md` |

## Narrative

Gemini returns **CONDITIONAL-GO [HIGH]** for a hybrid **BYO-auth agent kit + private Cloudflare site + concierge upsell**, not a foundation model and not a silo scraper.

### Executive claims (tagged)

| Claim | Tag |
|-------|-----|
| Wedge = Italian *jure sanguinis* document staging (not Ancestry-index competition) | [HIGH] |
| Full-service citizenship firms ~$12k–$25k; kit/concierge can sit under that | [CONFIRMED] via BrightTax / Bersani Law cites in source |
| Ancestry May 2026 ToS bans AI training on their content + scraping | [CONFIRMED] per Genealogy Bargains cite — **re-verify live ToS before ship** [NEEDS VERIFICATION 2026-07-20] |
| FamilySearch API requires compatibility review; no “copy out without enrich” | [CONFIRMED] FS developer docs cites |
| Incumbent AI (Stories, Full-Text Search, Scribe, GAIA tease) does **not** own offline comune / apostille PM job | [HIGH] |
| Brand **GPUOLOGY** is a positioning risk (GPU ≠ genealogy demographic; AI fear) — alt names: Civile Sprints, ArchivalAgent, DiasporaDesk | [HIGH] |
| Hybrid model (kit + hosted private site + concierge) best moat vs one-shot kit or concierge-only | [HIGH] |

### First paid offer (source recommendation)

**“Stato Civile Baseline Protocol”** ~$499–$899: Mac setup + autoresearch prompts for Antenati + Transkribus credits (~50 acts) + private `.gdz` on Cloudflare Access. Upsell: concierge sprint ≥$2,500 for certified *copie* / translation / apostille.

### Kill criteria (6 months) — as written in DR

FS API rejection as extract tool · GAIA-class end-to-end foreign doc automation destroys concierge margin · CAC >$300 for kit · Antenati WAF permanently blocks IIIF agent pulls.

### Operator override (2026-07-20)

Operator **rejects** ToS / FS-compatibility / Antenati-WAF items as product kills. Doctrine: people’s own genealogical information should stay reachable; FS + Antenati + Ancestry-class research assist remain **in program**. See `@concepts/gpuology-genealogy-agent-kit.md` § Operator doctrine. Retain DR for pricing/wedge only.

### Operator caveats

- Bibliography includes a few off-topic URLs (e.g. GotSport “API” cite) — do not treat every cite as Ancestry-primary.
- Architecture “Cloudflare + Topola `.gdz`” is partly **inferred** as optimal (source self-check) though Topola `.gdz` support is repo-sourced.
- Personal pedigrees stay out of wiki; this page is methodology + market only.

## Snippets

> Verdict: CONDITIONAL-GO. Hybrid BYO-auth agent kit + private hosting; biggest opportunity Italian jure sanguinis; biggest risk hostile incumbent ToS. [Source: GPUOLOGY Genealogy Business Analysis.docx]

> Ancestry May 12, 2026 ToS: ban train/fine-tune AI on Ancestry content; ban robots/scraping. [Source: same → genealogybargains.com]

> FamilySearch: compatibility review; apps that “simply copy data out … without providing value back” denied. [Source: same → developers.familysearch.org]
