---
title: "World Spirits Atlas — growth, technical SEO and monetization playbook"
type: source
related:
  - concepts/atlas-engine.md
  - sources/world-spirits-atlas-architecture-2026-11-25.md
  - sources/world-spirits-atlas-specification-2026-11-25.md
updated: 2026-11-25
---

## Raw Concept

| Field | Value |
|-------|--------|
| Title | Open-Source Growth, Technical SEO, and Monetization Playbook for the World Spirits Atlas and Shared Atlas Engine |
| Author | Operator document, no named author |
| Type | Operator document, .docx, growth and business plan |
| Location | `research to be indexed/osint/World Spirits Atlas Growth Strategy.docx` |
| Retrieved | 2026-11-25 |
| Pages | 273 paragraphs, 6 tables |
| Read status | skimmed (naming, SEO architecture, monetization pillars) |

## Narrative

### What it is

The go-to-market layer for the same product. It covers brand architecture, programmatic SEO, a launch sequence, and four monetization pillars. [Source: World Spirits Atlas Growth Strategy.docx]

### The asymmetric two-brand split

The recommendation is to separate the consumer product from the engine:

- **Consumer atlases** sit as subdirectories under one umbrella domain: `/spirits`, `/spices`, `/coffee`, `/wine`. A single domain compounds link equity and lets each new atlas inherit crawl depth on day one.
- **The open-source engine** sits on its own developer domain and GitHub organization. That isolates alcohol-compliance requirements from software adopters and preserves clean merger or spin-out optionality.

The reason for the split is a policy risk, not aesthetics. Google's link-spam policy names site-wide footer badges as an example of link spam. A followed "Built with" badge across four domains risks algorithmic neutralisation. The playbook's fix is a `nofollow` plus `data-nosnippet` footer badge, with at most one followed branded link on an about page.

### SEO architecture

The engine is static-site generated, with MapLibre vector hydration. Indexation gates run at build time, using practitioner heuristics: at least three structured-data dimensions and about 60 percent unique page-specific content per page. The context claim is that Google's March 2026 core update cut thin programmatic sites by 50 to 80 percent. That number is a third-party estimate, not a primary source. [TENTATIVE]

The rollout is a 90-day staged indexation plan and 50 target search clusters.

### Launch sequence

A 48-hour developer velocity blitz on days 1 and 2, then a 12-day staggered rollout across nine Reddit communities, each with a bespoke artefact rather than a promotional link. The reason given for the blitz is that GitHub Trending is a velocity measure, so a heavy first two days matters more than an even drip.

### The four monetization pillars

1. **Archival giclée prints** through an API-first fulfilment partner, triggered from the map export drawer. Worked unit economics: a 24 by 36 inch unframed print at $60 retail leaves about $31 gross profit after shipping and card fees.
2. **Spaced-repetition study packs** built on Anki's FSRS scheduler, aimed at WSET Level 2 and Level 3 candidates and bar teams. Free browser quiz and open JSON; paid individual pack and venue licence.
3. **Curated affiliates**, kept out of map chrome and body copy, inside disclosed drawers on style and region pages. Bookshop.org for books, glassware programmes, bottle finders.
4. **Privacy-first sponsorship**, no programmatic display ads. GitHub Sponsors and Open Collective at the engine layer; a quiet "Atlas Patron" card on the consumer site.

### Honest limits

The document is a plan. All revenue figures are modelled. Several claims are third-party estimates. One internal inconsistency: the free map download is labelled CC BY-SA in the growth document, while the architecture document specifies CC BY 4.0 for curated data. Resolve before shipping. [NEEDS VERIFICATION 2026-11-25]

### Reuse value

High for any programmatic atlas or open-data product in the workspace. The two-brand split and the build-time indexation gates are the transferable parts, not the spirits-specific content.
