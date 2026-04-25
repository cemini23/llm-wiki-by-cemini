---
title: "Publisher's exclusion (IAA §202(a)(11) bona-fide-publication sense)"
type: concept
tags: [concept, legal, registration, investment-advisers-act, cftc-reg-4-14, cemini-internal]
keywords: [Investment Advisers Act, §202(a)(11), publisher's exclusion, bona fide financial publication, general circulation, regular circulation, individualized advice, CFTC Regulation 4.14, CTA exemption, 15-or-fewer]
related:
  - sources/3-19-compliance-research.md
  - concepts/publishers-exclusion.md
  - concepts/publishers-exclusion-apa.md
  - concepts/ip-sale-readiness.md
maturity: draft
created: 2026-04-25
updated: 2026-04-25
---

## Relations

- @sources/3-19-compliance-research.md — S4 is the canonical statutory framing for both the IAA exclusion and the parallel CFTC Reg 4.14 CTA exemption
- @concepts/publishers-exclusion.md — disambiguation stub at the original slug; landing page that distinguishes APA-sense vs. IAA-sense
- @concepts/publishers-exclusion-apa.md — the other concept sharing the phrase; APA exclusion-schedule mechanic for cherry-picking what gets transferred at acquisition (distinct legal context)
- @concepts/ip-sale-readiness.md — top-level acquisition-readiness synthesis where the IAA exemption matters as a registration-burden mitigation

## Raw Concept

This page documents the **Investment Advisers Act §202(a)(11) "publisher's exclusion"** in its bona-fide-publication sense: the registration exemption that lets publishers of general-circulation, regular-circulation financial publications avoid RIA registration when they don't offer individualized advice. The parallel CFTC Regulation 4.14 provides equivalent relief from CTA registration on closely-aligned conditions.

Created 2026-04-25 as part of the disambiguation split — the wiki's original `publishers-exclusion.md` page documented only the APA exclusion-schedule mechanic, while `@sources/3-19-compliance-research.md` § Investment Advisers Act and the Publisher's Exclusion uses the same phrase in this distinct IAA-statutory sense.

## Narrative

### Statutory framework

The Investment Advisers Act of 1940 §202(a)(11) defines "investment adviser" with several enumerated exclusions. The "publisher's exclusion" is the carve-out for publishers of bona fide financial publications that meet three conditions:

1. **Bona fide** — the publication is a genuine business of providing financial commentary, not a vehicle for evading registration
2. **General and regular circulation** — distributed broadly and on a recurring schedule, not bespoke to individual subscribers
3. **No individualized advice** — content is not tailored to specific subscriber circumstances or trading accounts

The Supreme Court's *Lowe v. SEC*, 472 U.S. 181 (1985) is the foundational precedent — held that a financial newsletter publisher fell within the §202(a)(11) exclusion despite providing market commentary, because the publication was non-personalized and offered to the general public rather than tailored to individual recipients.

### Parallel CFTC Regulation 4.14 CTA exemption

The Commodity Exchange Act analog: under CEA §1a(12) and CFTC Regulation 4.14, a developer is exempt from Commodity Trading Advisor (CTA) registration when:

- Advice is **not based upon knowledge of or tailored to a customer's particular trading account**, OR
- They provide advice to **15 or fewer persons** in a 12-month period AND **do not hold themselves out to the public** as a CTA

The two exemptions operate as a coordinated regulatory pair: §202(a)(11) handles RIA registration (securities side), CFTC Reg 4.14 handles CTA registration (futures/swaps side). For a software vendor selling source code as a one-time outright sale to a single institutional buyer, both exemptions are typically available simultaneously.

### Cemini relevance — IP-sale-readiness application

The compliance-research source's framing (`@sources/3-19-compliance-research.md` S4) anchors this exemption pair in the specific Cemini IP-sale fact pattern:

- **Outright source-code sale, not ongoing advisory** — selling the algorithmic engine as a software-vendor agreement is structurally different from operating it as an investment adviser. No discretionary management of buyer assets; no individualized recommendations to multiple parties.
- **≤15 advisees over 12 months** — a single institutional buyer comfortably falls within the 15-or-fewer threshold for CFTC Reg 4.14
- **Documentation does double duty** — the MkDocs-Material + SBOM + audit-log artifacts that satisfy FINRA NASD 1032(f) supervisory-readability also support the "no individualized advice" prong by demonstrating the system's general-purpose architectural framing rather than buyer-specific tailoring

### Distinction from the APA-schedule sense

The phrase "publisher's exclusion" appears in two distinct legal contexts in the Cemini research corpus:

| Sense | Legal home | Mechanism | Cemini relevance |
|---|---|---|---|
| **IAA §202(a)(11)** *(this page)* | Investment Advisers Act 1940 + parallel CFTC Reg 4.14 | Registration exemption for non-personalized financial publications | Avoids RIA + CTA registration on outright IP sale |
| **APA exclusion schedule** *(`@concepts/publishers-exclusion-apa.md`)* | M&A Asset Purchase Agreement contract drafting | Carve-out clause excluding specific components from the asset transfer | Protects deal value by pre-identifying problematic components for exclusion |

Both senses share the surface vocabulary "exclusion" / "exclude" but operate at different layers of the IP-sale stack: the IAA exclusion is a *regulatory* posture (who needs to register), the APA exclusion is a *contractual* mechanic (what gets transferred). They co-exist in the deal architecture without conflict.

The disambiguation landing page at `@concepts/publishers-exclusion.md` routes readers to whichever sense their query is targeting.

## Snippets

### S1 — IAA §202(a)(11) publisher's exclusion + CFTC Reg 4.14 CTA exemption (verbatim from compliance-research source)
> "Furthermore, the system may fall under the 'publisher's exclusion,' which exempts publishers of bona fide financial publications of general and regular circulation that do not offer individualized advice. Similarly, under the CEA and CFTC Regulation 4.14, a developer is exempt from CTA registration if their advice is not based upon knowledge of or tailored to a customer's particular trading account, or if they provide advice to 15 or fewer persons in a 12-month period and do not hold themselves out to the public as a CTA."
[Source: 3_19 Compliance Research.docx, § The Investment Advisers Act and the Publisher's Exclusion, ¶26 — see `@sources/3-19-compliance-research.md` S4]
