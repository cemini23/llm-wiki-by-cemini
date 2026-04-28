---
title: IRC §174 / §174A R&E expensing (TCJA 5-yr amortization → 2025 restoration)
type: concept
tags: [concept, tax, legal, cemini-internal, ip-sale]
keywords: [section 174, section 174a, tcja, r&e, research and experimentation, software development, amortization, sub-31m, small business, retroactive amendment, accelerate]
related:
  - sources/fintech-startup-legal-ip-roadmap.md
  - concepts/ip-sale-corporate-structure.md
  - concepts/ip-sale-readiness.md
  - concepts/irc-1235-capital-gains-safe-harbor.md
  - concepts/defend-trade-secrets-act.md
maturity: validated
created: 2026-04-27
updated: 2026-04-27
---

## Relations

- @sources/fintech-startup-legal-ip-roadmap.md — K7 deep-read 2026-04-27; paras 16–19 are the canonical statement of the §174 / §174A timeline + sub-$31M small-business carve-out + Florida 220.196 R&D credit interaction
- @concepts/ip-sale-corporate-structure.md — sibling tax-structure page; the §174A election is one of three load-bearing tax instruments alongside §475(f) MTM and §1235 capital-gains
- @concepts/ip-sale-readiness.md — parent thesis; component 6 (tax + legal structure) — §174A R&E expensing converts pre-sale dev costs into immediate ordinary deductions, increasing net cash retained for reinvestment / runway / IP-sale-prep work
- @concepts/irc-1235-capital-gains-safe-harbor.md — coordinated tax-treatment pair: §174A optimizes the **annual operating cost** side (R&E expense deduction); §1235 optimizes the **exit-event proceeds** side (capital-gains rate). Both apply simultaneously to the same Cemini-side activity (algorithm dev + future IP sale)
- @concepts/defend-trade-secrets-act.md — K7-tail concept-promotion 2026-04-27 — sibling regime; the same capitalized-R&E records that establish §174A small-business deduction also serve as the cost-of-development evidentiary substrate for the DTSA economic-value-from-secrecy burden under 18 U.S.C. § 1839 — dual-purpose accounting documentation

## Raw Concept

The question this page answers: **How does Cemini deduct R&E and software-development costs for federal tax purposes during the IP-sale-prep window, and how did the rules change between 2022 and 2025?**

Synthesized from @sources/fintech-startup-legal-ip-roadmap.md K7 deep-read 2026-04-27 (paras 16–19), which is the only source in the Cemini corpus to address §174 / §174A in any depth. K5 (3-9-pm-research) and K6 (3-10-ip-sale-audit) do not cover this regime, so K7 is the **single-source canonical reference** until/unless an additional source surfaces — see verification-needed flags `[NEEDS VERIFICATION 2026-04-27]` annotated below.

## Narrative

**[CONFIRMED — 2026-04-27 K7 deep-read] doc-only.** Tax-counsel deliverable; no engineering milestone tied to this page. The §174A election is exercised at year-end tax filing; the structural prerequisite is the entity classification (§1235-compatible disregarded-entity SMLLC, per @concepts/ip-sale-corporate-structure.md) which is already deployed.

### The TCJA 5-year amortization regime (2022–2024)

The Tax Cuts and Jobs Act of 2017 (TCJA) amended **IRC §174** to require that all domestic software-development costs (and other R&E expenditures) be **capitalized and amortized over 5 years**, effective for tax years beginning after December 31, 2021. Foreign-incurred R&E is amortized over 15 years.

Pre-TCJA, taxpayers had the option to deduct R&E costs **immediately as ordinary operating expenses** — the historical default since the 1950s. The TCJA change was particularly devastating for early-stage technology firms because it created a **cash-flow timing mismatch**: a startup spending $500K on software development in 2023 could only deduct $50K in 2023 (one-tenth of the annual cost under mid-quarter convention; ~$100K in subsequent full years), even though the full $500K was real cash going out the door. Effective marginal tax rates on profitable-but-cash-tight early-stage tech firms spiked materially.

K7 frames the impact as "drastically impacting the cash flow and operational runway of technology startups by preventing immediate expense deductions" (para 17).

### The 2025 §174A restoration

K7 para 18 documents the resolution: **2025 legislation restored full domestic expensing for R&E costs under a new §174A**, effective for the 2025 tax year. The substantive provisions:

1. **Full domestic R&E expensing restored** for tax years beginning January 1, 2025 — same as pre-TCJA default.
2. **Foreign R&E** remains subject to 15-year amortization (no change).
3. **Sub-$31M small-business carve-out**: taxpayers with **average annual gross receipts under $31 million** can elect either:
   - **Retroactive amendment** of prior returns (2022, 2023, 2024) to deduct R&E costs immediately in the year incurred, or
   - **Acceleration** of previously capitalized R&E costs into the current fiscal year as a single bulk deduction.
4. The sub-$31M threshold uses the standard small-business average-annual-gross-receipts measure (typically a 3-year trailing average per §448(c)).

### Cemini-side application

K7 para 18 lists the Cemini-relevant cost categories that qualify as deductible under §174A:

- Programming the trading bots (founder time, contractor fees)
- Compensating developers
- Acquiring historical tick data
- Building the server infrastructure (Hetzner deployment + Docker container topology)

The Cemini deployed posture (single-member Florida SMLLC, sub-$1M scale, founder-only) sits comfortably **under the $31M threshold**. The full-restoration-for-2025 path applies straightforwardly. The retroactive-amendment / acceleration provisions for 2022–2024 are available if cumulative R&E spend during those years was material enough to warrant the amended-return work. **[NEEDS VERIFICATION 2026-04-27]** the exact 2022–2024 R&E spend total against the founder's tax records — the K7 source frames this as a tax-counsel-engagement workstream, not a self-serve calculation.

### Florida R&D Tax Credit (Statute 220.196) — incompatible with LLC structure

K7 para 19 surfaces a state-level wrinkle: **Florida Statute 220.196** provides a **10% R&D Tax Credit on qualified research expenses exceeding a calculated base amount** for "targeted industries" including Information Technology. However, the credit is **statutorily restricted exclusively to C-Corporations**.

A single-member Florida LLC cannot claim the credit without electing C-Corp tax status via IRS Form 8832, which would re-introduce the double-taxation problem documented in @concepts/ip-sale-corporate-structure.md and break the §1235 disregarded-entity safe harbor in @concepts/irc-1235-capital-gains-safe-harbor.md.

K7's verdict (para 19): "the federal pass-through benefits and MTM trading efficiencies of an LLC vastly outweigh the restrictive state-level R&D credits afforded to C-Corporations." **The Florida 220.196 credit is therefore not available to Cemini under the prescribed corporate structure.** Documented here for completeness; not actionable.

### Interaction with §475(f) MTM election

The §174A election (R&E expense deduction) and the §475(f) MTM election (Trader Tax Status, ordinary-income trading P&L) operate on **distinct cost categories** and do not conflict:

- **§174A** deducts the cost of *building the algorithm* (R&D expenses).
- **§475(f) MTM** governs the tax treatment of the *trading P&L produced by running the algorithm* (gain/loss recognition).

The two elections are coordinated tax instruments that together optimize the OpCo's federal tax liability during the IP-sale-prep window. K7 prescribes both (Phase 2 step 6 for §475(f); §174A is implicit in the discussion but doesn't get a discrete execution-roadmap step).

### Decision rule: when to file

The §174A election is exercised on the federal tax return for the year the deduction is claimed. The retroactive-amendment / acceleration path requires Form 1040X (or entity equivalent) for the prior years.

K7 doesn't prescribe the filing sequence explicitly, but the natural order is:

1. **2025 return**: file with full domestic R&E expensing deducted under §174A as the default — immediate runway benefit.
2. **2022–2024 amended returns** (if material R&E spend in those years): retroactive amendment to recover the deferred deductions. This is a tax-counsel workstream — the founder should not self-amend.
3. **Coordinate with §475(f) MTM filing** if both elections are being exercised in the same year — the §475(f) deadline is the unextended due date of the **prior year's** return, so timing-coordinate the two.

## Snippets

### S1 — TCJA 5-year amortization regime (K7 para 17)
> "An AI-driven trading firm incurs substantial capital expenditures in algorithmic development, raw data acquisition, and reinforcement learning model training. The tax treatment of these expenses is rigidly governed by Internal Revenue Code Section 174. Between 2022 and 2024, amendments introduced by the Tax Cuts and Jobs Act (TCJA) required all domestic software development costs to be capitalized and amortized over a restrictive five-year period, drastically impacting the cash flow and operational runway of technology startups by preventing immediate expense deductions."
>
> *— @sources/fintech-startup-legal-ip-roadmap.md K7 para 17. Statement of the 2022–2024 problem.*

### S2 — §174A 2025 restoration + sub-$31M carve-out (K7 para 18)
> "Recent legislative updates, effective for the 2025 tax year, have restored full domestic expensing for research and experimentation (R&E) costs under Section 174A. Small business taxpayers with average annual gross receipts under $31 million can elect to retroactively amend prior returns or accelerate previously capitalized costs into the current fiscal year. Consequently, the costs associated with programming the trading bots, compensating developers, acquiring historical tick data, and building the server infrastructure can now be fully deducted as ordinary operating expenses in the year they are incurred."
>
> *— @sources/fintech-startup-legal-ip-roadmap.md K7 para 18. Canonical statement of the §174A restoration.*

### S3 — Florida 220.196 R&D Credit C-Corp-only restriction (K7 para 19)
> "Florida offers a state-level Research and Development Tax Credit, authorized under Florida Statute 220.196, which allows a 10% credit on qualified research expenses exceeding a calculated base amount. However, participation in this specific program is statutorily restricted exclusively to C-Corporations operating within targeted industries, such as Information Technology. An LLC seeking this specific state-level credit would be required to elect C-Corporation tax status via IRS Form 8832, thereby triggering the double taxation issues previously outlined. Therefore, for a proprietary trading firm, the federal pass-through benefits and MTM trading efficiencies of an LLC vastly outweigh the restrictive state-level R&D credits afforded to C-Corporations."
>
> *— @sources/fintech-startup-legal-ip-roadmap.md K7 para 19. The "Florida 220.196 R&D credit is not available to Cemini" finding.*
