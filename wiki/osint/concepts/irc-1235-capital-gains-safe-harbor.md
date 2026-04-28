---
title: IRC §1235 capital-gains safe harbor
type: concept
tags: [concept, tax, legal, m-and-a]
keywords: [1235, 1221, tcja, ltcg, holdco, opco, smllc, personal-efforts, 174a, r&e]
related:
  - sources/3-9-pm-research.md
  - sources/3-10-algorithmic-trading-ip-sale-audit.md
  - sources/3-19-compliance-research.md
  - sources/3-19-ip-sale-research.md
  - sources/fintech-startup-legal-ip-roadmap.md
  - concepts/ip-sale-readiness.md
  - concepts/ip-sale-corporate-structure.md
  - concepts/section-174-rd-expensing.md
  - concepts/milestone-ledger.md
maturity: validated
created: 2026-04-23
updated: 2026-04-27
---

## Relations

- @sources/3-9-pm-research.md — para 124 (HoldCo / OpCo dual-entity prescription that preserves §1235 flow-through)
- @sources/3-10-algorithmic-trading-ip-sale-audit.md — K6 deep-read 2026-04-27; full §2 audit of §1221(a)(3) post-TCJA exposure and §1235 carve-out path
- @sources/3-19-compliance-research.md
- @sources/3-19-ip-sale-research.md
- @sources/fintech-startup-legal-ip-roadmap.md — K7 deep-read 2026-04-27; paras 23–25 anchor the §1221(a)(3) trade-secret framing that §1235 is the carve-out from; paras 16–19 introduce the coordinated §174A R&E expense-deduction instrument
- @concepts/ip-sale-readiness.md
- @concepts/ip-sale-corporate-structure.md — dedicated dual-entity (HoldCo / OpCo) page; this §1235 page is the tax-treatment sub-thread of that umbrella structure
- @concepts/section-174-rd-expensing.md — K7 promotion 2026-04-27; coordinated tax-treatment pair — §174A optimizes the **annual operating cost** side (R&E expense deduction during pre-sale period); §1235 optimizes the **exit-event proceeds** side (capital-gains rate at sale). Both apply simultaneously
- @concepts/milestone-ledger.md — Git commit history is the load-bearing audit artifact for the §1235 personal-efforts test (proves individual-inventor authorship)

## Raw Concept

Synthesized across 4 source(s) in the Cemini research corpus that reference this concept directly or by equivalent terminology. K6 expansion 2026-04-27 added §1221(a)(3) post-TCJA framing, personal-efforts test specificity, and the Florida-vs-Wyoming SMLLC consistency note (both jurisdictions work for §1235 because both are disregarded entities for federal tax — what matters is the entity classification, not the state).

## Narrative

**[CONFIRMED — 2026-04-24 Track C audit] doc-only** — Legal/tax review deliverable (belongs at a CPA + transactional attorney), not software. No engineering milestone. Gap memo: `briefs/track-c-walk-results.md`.

**IRC §1235** provides a statutory safe harbor under the US Internal
Revenue Code for the **sale or exchange of a patent or rights therein
held by the inventor** — proceeds are taxed at long-term capital
gains rates regardless of holding period, and regardless of whether
installment payments make them look like royalty income.

### Why §1235 is structurally necessary post-TCJA

The Tax Cuts and Jobs Act of 2017 (TCJA) amended **IRC §1221(a)(3)** to
exclude self-created software, copyrights, literary, musical, or
artistic compositions, and similar property from the definition of a
**capital asset**. Default treatment of a sale of self-created software
is now **ordinary income** — taxed at the founder's marginal rate
(potentially 37% federal top bracket + NIIT 3.8% + state).

§1235 is the carve-out path back to long-term capital gains for
**inventor-held** IP. It is not automatic — it requires affirmative
qualification on each element of the test. The K6 audit
(@sources/3-10-algorithmic-trading-ip-sale-audit.md) treats §1235
qualification as the single most-load-bearing tax structural choice
in the IP-sale thesis: a failed §1235 qualification converts a
~20% LTCG outcome into a ~37%+ ordinary-income outcome on the entire
deal proceeds.

### Why it matters to Cemini
The IP-sale thesis contemplates a large one-time proceeds event
(replacement-cost-anchored base + earnout tiers; see
@concepts/replacement-cost-valuation.md). Absent §1235, post-TCJA
default treatment recharacterizes the proceeds (including the earnout
portion) as **ordinary-income** — taxed at ~37% top marginal federal
rate plus NIIT plus state tax. Under §1235, the same proceeds are
taxed at 20% federal LTCG + NIIT + state, saving ~15–17% of the
proceeds in tax (delta depends on state and earnout cadence).

### Requirements
Cemini satisfies the core tests per the 3-19 compliance research and
the 3-10 audit:

1. **Individual "holder"** — the inventor must personally hold the
   IP at the time of transfer. A disregarded-entity SMLLC is
   pass-through for federal tax purposes, so IP held by a SMLLC is
   still treated as held by the individual member-inventor for
   §1235 purposes. **Florida and Wyoming SMLLCs both work** — the
   key is the disregarded-entity classification, not the
   state-of-formation. An S-corp or multi-member partnership
   wrapper would break the safe harbor because the entity itself
   becomes the holder.
2. **Personal-efforts / inventor test** — the founder must have
   personally created the IP (i.e., qualifies as the inventor under
   substantially-all-rights doctrine). The **Git commit history is
   the load-bearing audit artifact** for this test: an unbroken
   single-author commit chain from the initial commit through the
   transfer date is the cleanest possible proof. Mixed-author repos
   require either work-for-hire assignments from contributors or
   carve-out of contributor-authored modules from the §1235 transfer
   bundle. See @concepts/milestone-ledger.md — the milestone ledger
   in its prescribed cryptographically-anchored form would be a
   tamper-evident superset of this audit trail.
3. **Transfer of substantially all rights** — the APA must structure
   the deal as an **asset purchase**, not a license. A licensing
   structure (even with an exclusive worldwide field-of-use grant
   for a fixed term) does not satisfy §1235; the entire bundle of
   exclusive rights must transfer. See
   @concepts/publishers-exclusion-apa.md for the APA carve-out
   mechanics that interlock with this requirement.
4. **Not between related parties** — the buyer cannot be a
   controlled entity of the seller. An institutional acquirer
   (proprietary trading firm, fintech, systematic hedge fund) at
   arm's length satisfies this trivially.

### Structural interplay
The current Florida single-member LLC is a disregarded entity for
federal tax — proceeds flow to the individual inventor, preserving
§1235 eligibility. Upgrading to a **Wyoming HoldCo + Florida OpCo**
dual-entity (the prescribed structure per
@concepts/ip-sale-corporate-structure.md) does not break §1235
because both SMLLCs remain disregarded entities; the dual-entity
wrapper segregates **liability and asset-ownership topology**, not
income, and §1235 keys on the individual inventor not the state of
formation. An S-corp election on either entity would break §1235.

### Coordinated tax-treatment pair: §174A + §1235
K7 (@sources/fintech-startup-legal-ip-roadmap.md, deep-read
2026-04-27) is the corpus's most explicit framing of how §174A R&E
expensing pairs with §1235 capital-gains as **coordinated tax
instruments operating on distinct cost categories**:

- **§174A** (annual operating cost side) — deducts the cost of
  *building* the algorithm: programming time, contractor fees,
  developer compensation, historical tick data acquisition, server
  infrastructure. Restored 2025 for taxpayers with average annual
  gross receipts <$31M (Cemini sub-$1M sits comfortably under).
  Reduces the founder's annual federal taxable income during the
  IP-sale-prep window — converting capitalized R&E into immediate
  ordinary-expense deductions.
- **§1235** (exit-event proceeds side) — converts the IP-sale
  proceeds (base price + earnouts) from ordinary-income default
  (per §1221(a)(3) post-TCJA) to long-term capital-gains rate.
  Reduces the federal tax on the one-time exit event from ~37% top
  marginal + NIIT down to 20% LTCG + NIIT.

The two elections do not conflict — one operates on operating
expenses (deduction), the other on exit proceeds (recharacterization).
They apply simultaneously to the same Cemini-side activity (algorithm
dev → IP sale). See @concepts/section-174-rd-expensing.md for the
§174A details.

## Snippets

*(populate as source stubs are deep-read.)*
