---
title: "Publisher's exclusion (disambiguation)"
type: concept
tags: [concept, legal, disambiguation]
keywords: [publisher's exclusion]
related:
  - concepts/publishers-exclusion-apa.md
  - concepts/publishers-exclusion-iaa.md
maturity: validated
created: 2026-04-25
updated: 2026-04-25
---

## Relations

- @concepts/publishers-exclusion-apa.md — APA exclusion-schedule sense (M&A contract drafting)
- @concepts/publishers-exclusion-iaa.md — IAA §202(a)(11) bona-fide-publication sense (registration exemption)

## Raw Concept

Disambiguation landing page. The phrase "publisher's exclusion" appears in two distinct legal contexts in the Cemini research corpus, and prior to the 2026-04-25 split a single page was conflating both. This stub routes the reader to whichever sense their query is targeting.

## Narrative

Two distinct legal concepts share the surface phrase "publisher's exclusion":

| Sense | Page | Legal home | Mechanism | Cemini relevance |
|---|---|---|---|---|
| **APA exclusion schedule** | `@concepts/publishers-exclusion-apa.md` | M&A Asset Purchase Agreement contract drafting | Carve-out clause excluding specific components from the asset transfer | Protects deal value by pre-identifying problematic components for exclusion (Telegram alt-data, Finnhub commercial-license features, founder's personal Twitter scraping notes, Polymarket execution layer) |
| **IAA §202(a)(11)** | `@concepts/publishers-exclusion-iaa.md` | Investment Advisers Act 1940 + parallel CFTC Reg 4.14 | Registration exemption for non-personalized financial publications | Avoids RIA + CTA registration on outright IP sale (see `@sources/3-19-compliance-research.md` S4) |

Both senses share vocabulary ("exclusion" / "exclude") but operate at different layers of the IP-sale stack — the IAA exclusion is a *regulatory* posture (who needs to register), the APA exclusion is a *contractual* mechanic (what gets transferred). They co-exist in the deal architecture without conflict.

### Quick routing

- If your question is about **registration burden** (RIA, CTA, software-vendor exemption) → `@concepts/publishers-exclusion-iaa.md`
- If your question is about **what gets sold at acquisition** (asset transfer scope, deal-value protection) → `@concepts/publishers-exclusion-apa.md`

### History

The original `concepts/publishers-exclusion.md` page (created 2026-04-23, validated 2026-04-24) documented only the APA-schedule sense. A deep-read note in that page flagged the IAA-sense conflict against `@sources/3-19-compliance-research.md` S4. The 2026-04-25 split:
1. Renamed the original to `publishers-exclusion-apa.md` (preserves history via `git mv`)
2. Created the new IAA page at `publishers-exclusion-iaa.md`
3. Repurposed the original slug as this disambiguation stub

## Snippets

*(none — disambiguation stub; substantive snippets live on the two specific-sense pages)*
