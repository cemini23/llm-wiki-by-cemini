---
title: Italian citizenship YouTube soft-flags — evidence + court calendar for Atto
type: concept
tags: [concept, genealogy, citizenship, youtube, atto, k186, draft]
keywords: [Prenot@Mi evidence, GDPR Art 15, Cassazione 13818, Sezioni Unite, centralized Rome, soft-flag]
related:
  - sources/youtube-italian-citizenship-channels-2026-07-22.md
  - concepts/italian-citizenship-pathways-document-pipelines.md
  - concepts/atto-macos-gtm-gumroad.md
  - concepts/atto-local-first-threat-model.md
  - concepts/gpuology-genealogy-agent-kit.md
  - sources/gemini-italian-citizenship-software-map-2026-07-22.md
maturity: draft
created: 2026-07-22
updated: 2026-07-22
---

## Relations

- @sources/youtube-italian-citizenship-channels-2026-07-22.md — primary deep-watch source (K186)
- @concepts/italian-citizenship-pathways-document-pipelines.md — pathway IDs + status vocab; absorb evidence doc types
- @concepts/atto-macos-gtm-gumroad.md — “not a law firm / not YouTube eligibility oracle”
- @concepts/atto-local-first-threat-model.md — vault stores sensitive appointment proofs; strip before LLM
- @concepts/gpuology-genealogy-agent-kit.md — product hub
- @sources/gemini-italian-citizenship-software-map-2026-07-22.md — UPL never-claims

## Raw Concept

What Atto should **soft-flag and checklist** from high-signal Italian-citizenship YouTube (ICA / IDCA) without turning the app into a law firm or scraping Prenot@Mi.

## Narrative

### Soft-flag calendar (data-driven; no hard outcomes)

| Flag ID (proposed) | Trigger | UI posture |
|--------------------|---------|------------|
| `SF_TAJANI_COSTITUZIONALE` | Law 74 / Tajani under Constitutional review | “Court review pending — consult counsel; Atto does not predict rulings.” |
| `SF_MINOR_SEZIONI_UNITE` | Ancestor naturalized while next gen minor | Soft-flag judicial path; note pre-1975 minority age **21** as research hint only |
| `SF_APPT_IMPOSSIBLE` | User claims pre-27 Mar 2025 intent but no filing | Checklist for **evidence collection**; never “you are grandfathered” |
| `SF_VENUE_ROME_CENTRAL` | Abroad applicant long-horizon | Soft-flag future centralized mail office; current = consulate of residence |
| `SF_NAT_2YR_PARENT_GP` | Broken JS line but Italian parent/grandparent + Italy residency plan | Point to residency-naturalization *research* checklist — not auto-eligibility |

All flags: `legal_advice: false` · outcomes require human counsel.

### Appointment-failure evidence ontology (vault docs)

Proposed `DOC_*` additions (counsel-facing export, not auto-file):

| Doc ID | What to store | Notes |
|--------|---------------|-------|
| `DOC_PRENOTAMI_SCREENSHOT` | Dated calendar unavailability | Prefer **series** over weeks/months |
| `DOC_PRENOTAMI_ACCOUNT_EMAIL` | Account activation / registration email | Shows intent to book |
| `DOC_CONSULATE_CORRESPONDENCE` | Email / fax / formal notice | Incl. written “we will deny” |
| `DOC_CONSULATE_WAITLIST` | Wait-list confirmation | |
| `DOC_EMBASSY_SUSPENSION_NOTICE` | Official suspension of JS appointments | Used in Cassazione narrative |
| `DOC_GDPR_ART15_PACKET` | Optional Art.15 response from authorities | **Counsel-led**; Atto only stores files user imports |

IDCA angle: missing screenshots ≠ dead case — government-held Prenot@Mi-related data *may* exist; Atto must **not** auto-submit GDPR requests.

### Court glossary (help copy)

| Body | Role (operator-facing) |
|------|-------------------------|
| Corte Costituzionale | Whether a **law** complies with the Constitution |
| Corte di Cassazione | How lower courts should **interpret** the law; can unify conflicting lines (*Sezioni Unite*) |

### Steal from channels / drop

| Steal | Drop |
|-------|------|
| Evidence checklists; soft calendar language | “You still qualify” / “act as if Tajani doesn’t exist” CTAs |
| Birthright-recognition framing for *copy* caution | Guaranteed outcomes; Prenot@Mi bots |
| 2-year residency naturalization as **alternate path label** | Encoding firm fee quotes as product truth |
| Central Rome office as venue soft-flag | Scraping consulate calendars |

### Open verification

Lock against primary texts before UI ship: Cassazione **13818/2026**; Law 74/2025 / Circolari; any Constitutional Court judgment after Jun 9 2026 hearing; MAECI notices on centralized processing. [NEEDS VERIFICATION 2026-07-22]
