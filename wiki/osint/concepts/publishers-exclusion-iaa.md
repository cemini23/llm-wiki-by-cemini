---
title: "Publisher's exclusion (IAA §202(a)(11) bona-fide-publication sense)"
type: concept
tags: [concept, legal, registration, investment-advisers-act, cftc-reg-4-14, cemini-internal]
keywords: [Investment Advisers Act, §202(a)(11), publisher's exclusion, bona fide financial publication, general circulation, regular circulation, individualized advice, CFTC Regulation 4.14, CTA exemption, 15-or-fewer, Lowe v. SEC, Internet Adviser Exemption, Rule 203A-2(e), de minimis]
related:
  - sources/3-19-compliance-research.md
  - sources/fintech-startup-legal-ip-roadmap.md
  - concepts/publishers-exclusion.md
  - concepts/publishers-exclusion-apa.md
  - concepts/ip-sale-readiness.md
  - concepts/ip-sale-corporate-structure.md
  - concepts/florida-fintech-sandbox.md
maturity: validated
created: 2026-04-25
updated: 2026-04-27
---

## Relations

- @sources/3-19-compliance-research.md — S4 is the canonical statutory framing for both the IAA exclusion and the parallel CFTC Reg 4.14 CTA exemption
- @sources/fintech-startup-legal-ip-roadmap.md — K7 deep-read 2026-04-27; paras 49–50 add the **Lowe v. SEC** SaaS framing + the **July 2024 amendment to Internet Adviser Exemption Rule 203A-2(e)** (eliminates 15-client de minimis exception)
- @concepts/publishers-exclusion.md — disambiguation stub at the original slug; landing page that distinguishes APA-sense vs. IAA-sense
- @concepts/publishers-exclusion-apa.md — the other concept sharing the phrase; APA exclusion-schedule mechanic for cherry-picking what gets transferred at acquisition (distinct legal context)
- @concepts/ip-sale-readiness.md — top-level acquisition-readiness synthesis where the IAA exemption matters as a registration-burden mitigation
- @concepts/ip-sale-corporate-structure.md — sibling regulatory-pathway page; the IAA exemption is one of three federal/state registration-avoidance options alongside CFTC Reg 4.14 and the Florida Fintech Sandbox
- @concepts/florida-fintech-sandbox.md — state-level alternative pathway for retail SaaS validation; sequences before federal exemption registration

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

### Lowe v. SEC applied to AI-driven SaaS (K7 framing)

K7 (@sources/fintech-startup-legal-ip-roadmap.md paras 49–50, deep-read 2026-04-27) is the corpus's most explicit framing of how the *Lowe* doctrine maps to AI-driven SaaS. The K7 analysis distinguishes two product configurations along the personalization axis:

- **Impersonal, non-tailored algorithmic SaaS** — the software produces general-purpose signals or trade ideas without reference to the user's individual financial situation, portfolio, or account context. K7 reads *Lowe* as **available** for this configuration: "the 'Publisher's Exemption' articulated in the Supreme Court case Lowe v. SEC allowed providers of impersonal, non-tailored financial software to avoid registration."
- **Personalized algorithmic SaaS** — the software analyzes the user's personal financial data or portfolio inputs to generate tailored trade execution. K7 reads *Lowe* as **not available**: "the SEC views highly sophisticated algorithms that analyze a user's personal financial data or portfolio inputs to generate tailored trade execution as crossing the line into actionable, regulated investment advice."

The personalization line is the operative distinction. A Cemini retail-SaaS pivot would need to make this design decision explicitly: ship general-purpose signal output (Lowe-eligible) or personalized portfolio-tailored execution (Lowe-ineligible, requires registration).

### Internet Adviser Exemption Rule 203A-2(e) — July 2024 amendment

K7 paras 49–50 also document a major regulatory update not addressed by the 3-19-compliance-research source: the **SEC's July 2024 amendment to the Internet Adviser Exemption (Rule 203A-2(e))**.

**Pre-amendment (legacy regime)**: Allowed automated investment advisers to register with the SEC (rather than navigating state-by-state) if they provided advice exclusively through an interactive website. The legacy rule contained a **15-client de minimis exception** permitting up to 15 non-internet clients (e.g., friends-and-family human-directed advisory) without breaking the federal-registration eligibility.

**Post-amendment (effective July 2024)**: To rely on the exemption, the software provider must:

1. Operate **exclusively** through an "operational interactive website" or digital platform.
2. **Eliminate all human-directed advisory services** — no carve-outs for in-person or phone-based advisory.
3. **Maintain zero non-internet clients** — the 15-client de minimis exception is **eliminated**.

The amendment is a **tightening of eligibility, not a loosening** — automated SaaS providers gain federal-registration access, but at the cost of any human-touch service line. For Cemini, the implication: a retail SaaS pivot that relied on the prior 15-client de minimis to also provide bespoke advisory to friends/family/early customers would no longer qualify under the post-July-2024 rule. The pivot must be **purely software** to use Rule 203A-2(e).

### Pathway comparison — which exemption to use

K7's framing positions §202(a)(11) bona-fide-publication, CFTC Reg 4.14, and the Internet Adviser Exemption Rule 203A-2(e) as three distinct registration-avoidance / registration-light pathways:

| Pathway | Authority | Use case | Constraint |
|---|---|---|---|
| **§202(a)(11) bona-fide-publication** *(this page)* | IAA 1940 + CFTC Reg 4.14 | Outright IP sale to single buyer; impersonal SaaS general-circulation publication | "No individualized advice" prong is the binding constraint |
| **CFTC Reg 4.14(a)(10) CTA exemption** | CFTC | Commodity/futures/swaps advisory with <15 clients + no public hold-out | Hard 15-client ceiling; no public marketing |
| **SEC Internet Adviser Exemption Rule 203A-2(e) (July 2024)** | SEC | Federally-registered automated SaaS advisory, no human services, zero non-internet clients | Post-July-2024 elimination of 15-client de minimis means **no human touch carve-outs** |
| **Florida Fintech Sandbox Ch. 559.952** *(see @concepts/florida-fintech-sandbox.md)* | Florida OFR | State-level supervised pilot pathway for novel products | Florida-only; consumer-count capped; supervised pilot only |

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

### S2 — Lowe v. SEC applied to AI SaaS (K7 paras 49–50)
> "If the firm intends to operate purely as a software-as-a-service (SaaS) provider—licensing the algorithmic trading bots to retail users without directly holding their funds—the regulatory classification becomes highly complex. Historically, the 'Publisher's Exemption' articulated in the Supreme Court case Lowe v. SEC allowed providers of impersonal, non-tailored financial software to avoid registration. However, the SEC views highly sophisticated algorithms that analyze a user's personal financial data or portfolio inputs to generate tailored trade execution as crossing the line into actionable, regulated investment advice. ... If the software directly interfaces with user brokerage accounts to execute trades autonomously, the SEC considers this discretionary portfolio management, unequivocally requiring registration."
>
> *— @sources/fintech-startup-legal-ip-roadmap.md K7 paras 49–50. The personalization-axis distinction (impersonal-non-tailored vs personal-portfolio-tailored) is the operative line that Lowe draws.*

### S3 — Internet Adviser Exemption Rule 203A-2(e) July 2024 amendment (K7 para 50)
> "In July 2024, the SEC amended the Internet Adviser Exemption (Rule 203A-2(e)), which allows automated providers to register directly with the SEC rather than navigating a complex patchwork of state-by-state regulators. To rely on this exemption, the software provider must operate exclusively through an 'operational interactive website' or digital platform, eliminate all human-directed advisory services, and maintain zero non-internet clients, officially eliminating the previous 15-client de minimis exception."
>
> *— @sources/fintech-startup-legal-ip-roadmap.md K7 para 50. The eliminated-15-client-de-minimis framing is the binding tightening — the rule grants federal-registration access at the cost of any human-touch service line.*
