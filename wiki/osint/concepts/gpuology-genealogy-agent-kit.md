---
title: GPUOLOGY / genealogy agent kit — product strategy
type: concept
tags: [concept, genealogy, product, gpuology, revenue, k176, draft]
keywords: [jure sanguinis, BYO-auth, Cloudflare Access, Topola, Transkribus, Civile Sprints, hybrid kit-concierge]
related:
  - sources/gemini-gpuology-genealogy-business-analysis-2026-07-20.md
  - concepts/computational-genealogy-archival-automation.md
  - concepts/italian-regional-genealogy-archive-playbook.md
  - concepts/active-project-research-routing.md
  - entities/tools/familysearch-platform-api.md
  - entities/tools/topola-viewer.md
  - entities/tools/transkribus.md
  - entities/tools/autoresearch-genealogy.md
  - entities/tools/gcerretani-antenati.md
  - entities/tools/codice-fiscale-js.md
  - entities/tools/censusreporter.md
  - entities/tools/timemagazine-babynames.md
  - entities/tools/dhfbk-tint.md
maturity: draft
created: 2026-07-20
updated: 2026-07-20
---

## Relations

- @sources/gemini-gpuology-genealogy-business-analysis-2026-07-20.md — primary market/ToS/DR source (K176)
- @concepts/computational-genealogy-archival-automation.md — shipped methodology stack
- @concepts/italian-regional-genealogy-archive-playbook.md — Italian wedge content
- @concepts/active-project-research-routing.md — family-tree co-primary
- @entities/tools/familysearch-platform-api.md — BYO-auth commercial path
- @entities/tools/topola-viewer.md — private static viewer
- @entities/tools/transkribus.md — HTR partner credits
- @entities/tools/autoresearch-genealogy.md — agent prompt pack
- @entities/tools/gcerretani-antenati.md — Antenati IIIF personal-use
- @entities/tools/codice-fiscale-js.md — K175 comune matrix extract
- @entities/tools/censusreporter.md — K175 US staging extract
- @entities/tools/timemagazine-babynames.md — K175 SSA name priors
- @entities/tools/dhfbk-tint.md — K175 Italian NLP (private; ~1.2 GB RSS)

## Raw Concept

Should Cemini productize the family-tree journey as a **vertical agent kit + private share site + optional concierge** (working title GPUOLOGY)? What wedge, ToS shape, pricing, and naming survive contact with RootsTech-era incumbents?

## Narrative

### Verdict

**CONDITIONAL-GO** on hybrid kit + Cloudflare private site + *jure sanguinis* concierge upsell. **NO-GO** on training a genealogy foundation model and **NO-GO** on Ancestry scrape / centralized FS harvest. [Source: @sources/gemini-gpuology-genealogy-business-analysis-2026-07-20.md]

### Wedge

| Own | Don’t fight |
|-----|-------------|
| Offline project management: *copia integrale*, PEC, apostille chain, evidence tags | Ancestry/FS/MH record indexes |
| Private invite-only family site (Access + Topola) | FamilySearch global collaborative tree |
| Human-gated merges (hallucination distrust is a feature) | “AI found your ancestor” marketing |

Primary segment: Italian-American (and parallel diaspora) researchers staging citizenship docs. Price anchors: consular fees, $499–$799/doc procurement cites, $12k–$25k full-service firms → kit $499–$899 and concierge ≥$2.5k sit as discounts-to-firms. [CONFIRMED] figures are third-party blog/law-firm cites in the DR — re-check before public pricing.

### Architecture (compliance-first)

```
Local (BYO keys / BYO FS OAuth)
  Gramps truth → GEDCOM/.gdz
  Claude Code + autoresearch prompts
  Optional Transkribus API (credits)
  Antenati IIIF → local disk only (personal/research use)
Cloud
  Cloudflare Pages + Access (invite email)
  Topola static viewer
```

Ancestry: operator-present assist only; May 2026 ToS AI-train + scrape bans → [NEEDS VERIFICATION 2026-07-20] before any marketing claim. FamilySearch: apply Read API as local lookup, not bulk extract.

### Naming

Working title **GPUOLOGY** is a **positioning risk** (GPU jargon + AI-fear conflict). DR alts: **Civile Sprints**, **ArchivalAgent**, **DiasporaDesk**. Trademark/domain still open. Prefer positioning lines that stress verification over AI:

- “Your private archival workspace, powered by automation, verified by you.”
- “We navigate the bureaucracy; you discover the history.”

### 90-day MVP (from DR)

1. Register brand (likely abandon GPUOLOGY moniker).
2. Topola → Cloudflare Pages + Access template + `.gdz` build CLI.
3. Fork/sanitize autoresearch-genealogy Italian stato civile prompts.
4. Transkribus Organisation plan + thin Python credit router.
5. Publish *jure sanguinis* verification playbook (human gates; 2024 ministry circular notes).
6. Landing page priced vs $12k+ firms; closed beta n=5 from citizenship forums.
7. FS Read API compatibility application (local lookup framing).
8. Legal review: Antenati IIIF agent on **user machine** vs commercial-kit clause (Decrees 161/2023, 108/2024).

### Kill criteria

FS rejects as extract tool · incumbent automates foreign-doc procurement end-to-end · kit CAC >$300 · Antenati WAF kills IIIF agent pulls.

### Cemini fit

Already have: Italian playbook, FS API entity, Topola Extract, autoresearch Integrate, Antenati tool, K175 CodiceFiscaleJS/Census Reporter extracts, private `Desktop/family/research/` lessons. Product work is packaging + ToS-safe distribution — not greenfield research.

## Snippets

> Hybrid (kit + hosted + concierge) = Very High revenue confidence; High moat vs incumbents. [Source: @sources/gemini-gpuology-genealogy-business-analysis-2026-07-20.md business-model table]
