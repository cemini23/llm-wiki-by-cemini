---
title: IP-sale corporate structure (HoldCo / OpCo dual-entity)
type: concept
tags: [concept, legal, tax, m-and-a, cemini-internal, ip-sale]
keywords: [wyoming, florida, holdco, opco, smllc, charging-order, 475f, 3a5-4, lgpl, lei, gleif, 174a, 13h-1]
related:
  - sources/3-9-pm-research.md
  - sources/3-10-algorithmic-trading-ip-sale-audit.md
  - sources/3-19-compliance-research.md
  - sources/3-19-ip-sale-research.md
  - sources/fintech-startup-legal-ip-roadmap.md
  - concepts/ip-sale-readiness.md
  - concepts/irc-1235-capital-gains-safe-harbor.md
  - concepts/section-174-rd-expensing.md
  - concepts/florida-fintech-sandbox.md
  - concepts/replacement-cost-valuation.md
  - concepts/milestone-ledger.md
  - concepts/publishers-exclusion-apa.md
  - concepts/publishers-exclusion-iaa.md
  - entities/frameworks/nautilustrader.md
  - entities/platforms/interactive-brokers.md
  - entities/platforms/brex.md
  - entities/platforms/mercury.md
  - concepts/defend-trade-secrets-act.md
  - concepts/neural-magic-v-facebook.md
maturity: validated
created: 2026-04-27
updated: 2026-04-27
---

## Relations

- @sources/3-9-pm-research.md — para 124 prescribes the dual-entity framework (IP HoldCo Wyoming-or-Delaware, OpCo Florida LLC) plus §475(f) MTM election; K5 deep-read 2026-04-26
- @sources/3-10-algorithmic-trading-ip-sale-audit.md — full §2(a) audit of dual-entity prescription (Wyoming chosen over Delaware on cost + charging-order + privacy grounds); §475(f) **rejected** for IP-sale-prep window (divergence with 3-9); K6 deep-read 2026-04-27
- @sources/3-19-compliance-research.md — concurrent regulatory framing (SEC dealer-rule 3a5-4 sub-$50M exclusion, Reg ATS, broker-dealer carve-outs)
- @sources/3-19-ip-sale-research.md — APA / earnout structuring (the deal layered on top of this corporate skeleton)
- @sources/fintech-startup-legal-ip-roadmap.md — K7 deep-read 2026-04-27; **earliest of three corroborating audits** (2026-02-25, predates 3-9 + 3-10 by ~2 weeks); most operationally granular treatment of the dual-entity prescription with full 11-step / 3-phase execution roadmap; endorses §475(f) MTM (joins K5; makes 3-source split 2-vs-1 in favor of endorsement)
- @concepts/ip-sale-readiness.md — parent thesis; this page is the dedicated "component 6 (tax + legal structure)" expansion
- @concepts/irc-1235-capital-gains-safe-harbor.md — capital-gains regime that the disregarded-entity SMLLC choice preserves
- @concepts/section-174-rd-expensing.md — K7 promotion 2026-04-27; coordinated tax-treatment instrument for R&E expense deduction (operating-cost side); pairs with §1235 (exit-event side) and §475(f) (trading-P&L side)
- @concepts/florida-fintech-sandbox.md — K7 promotion 2026-04-27; state-level innovation pathway (Ch. 559.952) available to the same Florida OpCo entity if Cemini pivots to retail SaaS
- @concepts/replacement-cost-valuation.md — the valuation anchor that justifies the IP-segregation rationale (preserve the asset that's being valued)
- @concepts/milestone-ledger.md — the ledger that documents which IP shipped and when, which the HoldCo formally owns
- @concepts/publishers-exclusion-apa.md — APA carve-out mechanic that interlocks with the dual-entity structure
- @concepts/publishers-exclusion-iaa.md — federal IAA / CFTC registration-exemption pair; relevant if the OpCo's product surface ever extends beyond proprietary trading
- @entities/frameworks/nautilustrader.md — the LGPL-3.0 dependency whose architectural-isolation requirement informs the OpCo-side container topology (separate-work doctrine)
- @entities/platforms/interactive-brokers.md — K7 promotion 2026-04-27; prescribed institutional brokerage for the Florida OpCo (Phase 3 step 9); LEI is the gating onboarding prerequisite
- @entities/platforms/brex.md — K7 promotion 2026-04-27; prescribed corporate banking primary for both HoldCo and OpCo (Phase 3 step 8); programmatic API access is what makes intercompany royalty automation tractable
- @entities/platforms/mercury.md — K7-tail concept-promotion 2026-04-27; **rejected alternative** to Brex for the corporate-banking layer (K7 paras 58–59); documented for completeness as a future-pivot fallback if the Brex pathway stalls
- @concepts/defend-trade-secrets-act.md — K7-tail concept-promotion 2026-04-27; federal civil cause of action (18 U.S.C. § 1836 / § 1839) for trade-secret misappropriation; the Wyoming HoldCo (this page's IP licensor) is the natural plaintiff in any future DTSA action; the dual-entity-segregation pattern is a DTSA-enforcement strategic decision as much as a tax/liability one
- @concepts/neural-magic-v-facebook.md — K7-tail concept-promotion 2026-04-27; D. Mass. case-precedent (settled 2023) where a former-employee trade-secret-leakage fact pattern played out in AI/ML context; the threat model that this page's dual-entity HoldCo / OpCo segregation + Intercompany IP License + Phase 2 step 7 trade-secret protocols address structurally

## Raw Concept

The question this page answers: **What is the prescribed corporate-entity structure for a sub-$1M solo-operator AI trading platform being readied for an IP sale to an institutional acquirer?**

Synthesized across **three corroborating Cemini-internal audits** authored over a ~3-week window:

1. @sources/fintech-startup-legal-ip-roadmap.md (K7, **2026-02-25** — earliest, most operationally granular)
2. @sources/3-9-pm-research.md (K5, 2026-03-08 — v11.0 project-state context)
3. @sources/3-10-algorithmic-trading-ip-sale-audit.md (K6, 2026-03-10 — Wyoming-specific refinement)

All three converge on the dual-entity HoldCo / OpCo framework. The lone substantive divergence is the §475(f) Mark-to-Market election: **K7 + K5 endorse**, **K6 rejects** for IP-sale-prep purposes — the split is now 2-vs-1 in favor of endorsement, though K6's object-of-the-tax reasoning remains a valid object-specific consideration (see §475(f) discussion below). The 3-document set reads as a **rolling refinement chain** rather than three independent recommendations: K7 establishes the legal/regulatory framework + sequenced execution roadmap; K5 re-anchors it in the v11.0 project-state context; K6 refines the HoldCo jurisdiction (Wyoming-specific) and re-evaluates §475(f) on object-of-the-tax grounds.

K7 also surfaces three new dimensions not covered by K5 / K6: **§174A R&E expensing** (the 2025 small-business R&E deduction restoration), **the Florida Fintech Sandbox Ch. 559.952** (state-level innovation pathway), and **operationally granular institutional infrastructure** (Brex banking, IBKR Pro brokerage, FIX CTCI, LEI registration). See dedicated pages for each.

## Narrative

**[CONFIRMED — 2026-04-27 K6 + K7 deep-read] doc-only.** Legal/tax review deliverable. No engineering milestone tied to this page; it captures the prescribed structure as a future reference. As of 2026-04-27, the deployed entity is a **Florida single-member LLC** only — the Wyoming HoldCo half of the prescription is unbuilt; the LEI and institutional banking/brokerage layer (K7-prescribed) are also unbuilt (see "Current state vs prescribed" below).

### Why a dual-entity structure at all
The IP-sale thesis (see @concepts/ip-sale-readiness.md) contemplates a one-time large proceeds event — base price anchored to replacement-cost valuation (see @concepts/replacement-cost-valuation.md) plus earnout tiers. The structural goals are four:

1. **Insulate the IP** from operational liability (broker disputes, wash-trading allegations, ordinary-course tort exposure on the OpCo side).
2. **Preserve §1235 capital-gains treatment** on the IP transfer at sale time (see @concepts/irc-1235-capital-gains-safe-harbor.md).
3. **Pre-empt §1221(a)(3) recharacterization** of self-created software as ordinary-income property post-TCJA — the §1235 carve-out is the only path back to LTCG, and §1235 keys on individual inventor + transfer of substantially all rights.
4. **Charging-order protection** on the IP-owning entity so a creditor of the founder (personal life events: divorce, judgment, accident) cannot reach the IP itself, only the distribution interest.

A single-entity structure satisfies (2) but fails (1), (3) is fragile, and (4) depends on state — Florida's SMLLC charging-order protection is statutorily weaker than Wyoming's.

### The prescribed structure

| Entity | Jurisdiction | Tax treatment | Role |
|---|---|---|---|
| **IP HoldCo** | Wyoming SMLLC (3-10 §2(a) preferred) or Delaware (3-9 alternative) | Disregarded entity for federal tax (so §1235 flow-through preserved) | Owns source code, model weights, training data rights, trademarks, SBOM lineage, milestone-ledger commits |
| **Trading OpCo** | Florida SMLLC | Disregarded entity (3-10) — or §475(f) MTM elective (3-9 divergence; see below) | Operates broker accounts, holds API keys, executes trades, books P&L. Pays HoldCo a limited operational license fee for IP use. |

Both entities are single-member LLCs with the same individual founder as sole member, so for federal tax both are pass-through to the founder's personal return. The dual-entity wrapper does not multiply tax events; it segregates **liability and asset-ownership topology**, not income.

### Wyoming over Delaware — the 3-10 reasoning

3-10-ip-sale-audit §2(a) prefers Wyoming over Delaware on three grounds:

- **Formation + maintenance cost**: Wyoming SMLLC formation ~$102; annual report fee ~$60 (2026). Delaware: ~$200 + $300 franchise tax annually. For a sub-$1M solo-operator pre-revenue posture, the Delaware brand premium is not worth ~$430/year.
- **Charging-order protection (single-member)**: Wyoming statute (W.S. §17-29-503) explicitly extends charging-order-only-remedy to single-member LLCs. Delaware applies the rule by case law not statute, and several jurisdictions have eroded SMLLC charging-order protection (cf. Olmstead v. FTC). Wyoming's statutory clarity matters when the threat model is "founder gets sued personally and the IP is the prize asset."
- **Privacy / anonymous registered-agent formation**: Wyoming permits anonymous registered-agent formation; the founder's name is not on the publicly searchable Secretary of State record. Delaware permits agents but member identity surfaces through standard due-diligence channels.

3-9-pm-research (para 124) lists Wyoming **or** Delaware as alternatives without choosing; 3-10 makes the Wyoming-specific case. Treat 3-10 as the operative prescription.

### §475(f) Mark-to-Market — the (resolved) divergence

The three source audits **split 2-vs-1** on whether the trading OpCo should make a §475(f) MTM election:

- **K7 / fintech-startup-legal-ip-roadmap paras 13–15** *(2026-02-25)* — **recommends MTM**. Rationale: §475(f) "completely exempts the trading activity from wash sale rules" + removes the $3,000 capital-loss limitation; converts gains/losses to ordinary business income. K7 frames it as a structural prerequisite for high-frequency algorithmic execution.
- **K5 / 3-9-pm-research para 124** *(2026-03-08)* — **recommends MTM**. Rationale: Trader Tax Status removes capital-loss limitations and wash-sale accounting burdens during the high-frequency paper-trading validation phase, which is the operational regime for the OpCo.
- **K6 / 3-10-ip-sale-audit §2** *(2026-03-10)* — **rejects MTM**. Rationale: The IP-sale-prep window is the wrong moment to flip an irrevocable election that converts trading gains/losses to ordinary income. The IP-sale event itself is the dominant tax outcome, and MTM ordinary-income treatment on the operational side does not interlock cleanly with §1235 capital-gains treatment on the IP side.

**Reconciliation**: the divergence is resolvable on object-of-the-tax. The three recommendations are addressing different things:
- K7 + K5 are optimizing the **OpCo's trading-book P&L** during paper-trading and operational running.
- K6 is optimizing the **HoldCo's IP-sale tax outcome** at exit.

All three can be true; the question is which object dominates the founder's actual tax exposure. The decision rule is timing: if the IP sale is imminent (≤24 months), defer MTM (K6 reasoning); if the operational regime will run multi-year before sale, MTM may pencil (K7 + K5 reasoning). The §475(f) election is irrevocable absent IRS consent (Rev. Proc. 99-17) — file with eyes open. **The 2-vs-1 split lands in K7 + K5's favor by source-count weight, but K6's object-specific reasoning remains valid for IP-sale-imminent scenarios** — engage tax counsel before filing.

### LGPL-3.0 architectural isolation as a corporate-structure adjacency

A side note that matters because it interlocks with the OpCo's Docker topology: NautilusTrader (see @entities/frameworks/nautilustrader.md) is licensed LGPL-3.0. LGPL-3.0's "separate work" doctrine permits proprietary code to use an LGPL library as long as the library is not statically linked into the proprietary work. **Architectural isolation pattern**: confine the LGPL library to its own Docker container; proprietary engines (the strategy and risk-engine containers) communicate with it over a network boundary — JSON `TradeSignal` payloads (Pydantic v2 schemas) over Redis pub/sub. This constitutes "separate work communicating at arm's length" and immunizes the proprietary engines from viral copyleft.

The corporate-structure relevance: the IP HoldCo owns the proprietary engines. The LGPL-isolated container is conceptually OpCo-side infrastructure. The architectural pattern is what makes the HoldCo's IP cleanly transferable in an APA without dragging LGPL-tainted artifacts into the deal.

### SEC Rule 3a5-4 dealer-registration carve-out

3-19-compliance-research and 3-10-ip-sale-audit both note that the new SEC dealer-registration rule (Rule 3a5-4, finalized 2024) attaches qualitative liquidity-provision tests at $50M+ AUM. K7 (fintech-startup-legal-ip-roadmap paras 36–40) is the **canonical statement** of the qualitative-test carve-out logic in the corpus: a firm triggers registration if it (a) regularly expresses two-sided trading interest at/near best available prices and (b) earns revenue primarily from bid-ask spread capture or maker-taker rebates. **Carve-out path**: directional / momentum / mean-reversion / statistical-arbitrage strategies that don't systematically capture the bid-ask spread on both sides avoid dealer classification. A sub-$1M solo-operator OpCo sits comfortably under the threshold. The carve-out is structural — no special filing required to invoke it — but it informs the **scaling-tripwire**: if the OpCo grows past ~$25M AUM during the IP-sale-prep window, dealer-registration analysis becomes mandatory and the corporate structure may need to bifurcate further (separate dealer-registered execution sub-entity).

### Large Trader Reporting Rule 13h-1 (K7 addition)

K7 paras 41–45 add a second SEC threshold not addressed by K5 / K6: **Rule 13h-1 Large Trader Reporting** — quantitative threshold of **2 million shares OR $20 million FMV per single calendar day**, OR **20 million shares OR $200 million FMV per calendar month**. Filing Form 13H assigns a **Large Trader Identification Number (LTID)** which the firm provides to all executing broker-dealers. K7 specifically warns that "active algorithmic startups can trigger these volume thresholds rapidly, even with modest capital, due to the high turnover velocity and continuous execution nature of automated strategies" (para 45) — making this a structural risk that surfaces faster than dealer-registration. K7 prescribes hardcoded volume monitoring (Phase 3 step 10): if the bot's turnover approaches the threshold, immediately pause operations to file Form 13H + obtain LTID.

### §174A R&E expensing (K7 addition)

K7 paras 16–19 add a coordinated tax-treatment dimension that K5 / K6 do not address: **IRC §174 / §174A**. The TCJA forced 5-year amortization of domestic R&E costs for tax years 2022–2024 (catastrophic cash-flow impact for early-stage tech). **2025 legislation restored full domestic expensing under §174A** for taxpayers with average annual gross receipts under **$31 million** — Cemini sits comfortably within this small-business carve-out. The §174A election is exercised at year-end tax filing on the federal return; retroactive amendment + acceleration provisions are available for 2022–2024 R&E spend. See dedicated @concepts/section-174-rd-expensing.md.

The §174A and §475(f) elections are coordinated tax instruments operating on **distinct cost categories** — §174A deducts the cost of *building* the algorithm (R&E expenses); §475(f) governs the tax treatment of the *trading P&L produced by running* the algorithm. They do not conflict.

### LEI / EIN sequencing (K7 addition)

K7 Phase 2 step 5 specifies the legal-identifier acquisition sequence: **separate EINs from the IRS for both HoldCo and OpCo** + **active Legal Entity Identifier (LEI) for the Florida OpCo via the Global LEI Foundation (GLEIF)**. The LEI is a 20-character alphanumeric global identifier mandated post-2008 for institutional brokerage onboarding. **No active LEI = no IBKR Pro corporate account** — the LEI is the gating onboarding prerequisite for Phase 3 step 9 (IBKR brokerage integration). LEI acquisition is fast (~24h) but must precede the brokerage application.

### Banking + brokerage infrastructure (K7 addition)

K7 paras 56–66 prescribe institutional-grade infrastructure that K5 / K6 don't address:

- **Banking**: Brex over Mercury for both HoldCo + OpCo (Phase 3 step 8). Brex's programmatic API access enables automated intercompany royalty transfers — operationally critical for the dual-entity structure to function as automated treasury operations rather than manual paper-and-wire transfers. See @entities/platforms/brex.md.
- **Brokerage**: Interactive Brokers (IBKR) Pro corporate account under the Florida OpCo (Phase 3 step 9), using the LEI + EIN. Three API tiers: Web REST API (account management), TWS API (algorithmic execution; Cemini's prescribed tier), FIX CTCI (lowest-latency, $1,500/month minimum — not currently relevant). **All corporate entities classified as "Professional Subscribers"** for market data — fixed cost dimension to factor into the operational cost model. See @entities/platforms/interactive-brokers.md.

### Current state vs prescribed (server reality)

| Component | Prescribed (consensus across K5+K6+K7) | Deployed (2026-04-27) | Gap |
|---|---|---|---|
| Wyoming IP HoldCo | Wyoming SMLLC, anonymous agent, ~$162/yr total (K6 specific; K5+K7 list WY-or-DE alternative) | None | **Not formed** |
| Florida Trading OpCo | Florida SMLLC (3-of-3 convergent) | Florida SMLLC ✓ | None |
| Operational license between them | Intercompany IP License Agreement HoldCo → OpCo (K7 Phase 1 step 4) | N/A (no HoldCo) | **Pending HoldCo formation** |
| §475(f) MTM election | **Endorse (K7 + K5; 2-vs-1 majority)** vs reject (K6 — IP-sale-imminent reasoning) | Not elected | **Decision pending — engage tax counsel** |
| §174A R&E expensing election (K7) | Sub-$31M small-business election for 2025 + retroactive 2022–2024 | Not yet exercised | **Awaiting tax-counsel engagement** |
| EIN — HoldCo (K7 Phase 2) | Acquire from IRS at HoldCo formation | N/A (no HoldCo) | **Pending HoldCo formation** |
| EIN — OpCo (K7 Phase 2) | Acquire from IRS at OpCo formation | OpCo EIN exists ✓ | None |
| LEI — OpCo (K7 Phase 2) | Acquire via GLEIF immediately post-formation | Not registered | **Required before institutional brokerage onboarding** |
| Local BTR — Broward + Davie (K7 Phase 1) | Broward County + Town of Davie BTR + Home Occupation BTR if home-office | Status unknown | **Spot-check** |
| Brex banking — HoldCo + OpCo (K7 Phase 3) | Brex over Mercury for programmatic intercompany automation | Banking unknown / informal | **Spot-check** |
| IBKR Pro corporate account (K7 Phase 3) | Apply under Florida OpCo using LEI + EIN | Cemini equities path = Alpaca; no IBKR | **Pending — depends on LEI** |
| Volume monitoring (Rule 13h-1, K7 Phase 3) | Hardcoded turnover-vs-threshold tracking | Not implemented | **Defer until trading volume nontrivial** |
| Architectural isolation (LGPL) | Container-isolated NautilusTrader | NautilusTrader in deps; container topology TBD per K5 | **Spot-check** |

The deployed Florida SMLLC alone is sufficient for §1235 capital-gains treatment if the founder is the sole member and the APA structures the deal as an asset purchase of substantially all rights. The Wyoming HoldCo upgrade is a **risk-reduction step** (insulation + charging-order + privacy), not a §1235 prerequisite.

### Decision rule for when to form the HoldCo

The prescribed sequencing per 3-10 is: form the Wyoming HoldCo **before** the first APA term sheet circulates. The reasoning is that an acquirer's deal counsel will scrutinize the IP chain-of-title — having the IP already vested in a clean HoldCo at term-sheet time avoids a mid-deal asset-restructuring sub-project that delays close. If the founder is not in active deal conversations, the HoldCo formation can wait; the cost of forming early is ~$162/year carrying cost plus paperwork.

## Snippets

### S1 — K7 / fintech-startup-legal-ip-roadmap paras 28–30 (earliest of trio, 2026-02-25)
> Under this architecture, the IP HoldCo is established as a separate legal entity, often in a jurisdiction with unparalleled privacy and asset protection standards, such as Wyoming or Delaware. The IP HoldCo holds the exclusive legal title to the source code, the trained AI models, the proprietary trading algorithms, and any associated trademarks or branding. The OpCo, registered as the Florida LLC to conduct the actual trading activity and interface directly with brokerages, holds no intellectual property assets of its own. ... This bifurcation provides profound risk mitigation. Proprietary algorithmic trading inherently involves catastrophic financial risks, including margin calls, flash crashes, or algorithmic malfunctions resulting in massive, rapid capital loss. If the OpCo faces insolvency or litigation from creditors or brokerages, the core intellectual property remains shielded within the entirely separate IP HoldCo.
>
> *— @sources/fintech-startup-legal-ip-roadmap.md K7 paras 28–30. Earliest of three corroborating audits (2026-02-25). Frames the dual-entity prescription with explicit liability-segregation reasoning; lists Wyoming or Delaware as alternatives without choosing (K6 makes the Wyoming-specific case).*

### S2 — K5 / 3-9-pm-research para 124 (2026-03-08)
> To fully insulate the intellectual property during the paper-trading validation phase, the overarching corporate entity should adopt a dual-structure framework: an IP HoldCo (registered in Wyoming or Delaware) that exclusively owns the source code and neural network weights, granting a limited operational license to a trading OpCo (e.g., a Florida LLC). The trading entity must execute a Section 475(f) Mark-to-Market election to achieve "Trader Tax Status," exempting the firm from capital loss limitations and wash sale accounting burdens during high-frequency validation.
>
> *— @sources/3-9-pm-research.md para 124. The 3-9 source's prescriptive paragraph; explicitly endorses §475(f) MTM. Note that 3-9 lists Wyoming **or** Delaware without choosing; 3-10 makes the Wyoming-specific case.*

### S3 — K6 / 3-10-algorithmic-trading-ip-sale-audit §2(a) (2026-03-10)
> The recommended structure is a Wyoming-domiciled IP HoldCo (single-member LLC) with statutory charging-order protection per W.S. §17-29-503, paired with a Florida-domiciled trading OpCo (single-member LLC). Wyoming's formation and annual-maintenance costs (~$102 + ~$60) are materially below Delaware's, and Wyoming statute (unlike Delaware case law) explicitly extends charging-order-only remedy to single-member LLCs. Anonymous registered-agent formation is permitted in Wyoming.
>
> *— @sources/3-10-algorithmic-trading-ip-sale-audit.md §2(a). The 3-10 source's prescriptive paragraph; chooses Wyoming-over-Delaware on cost + statutory charging-order + privacy grounds. Diverges from K5 + K7 by **rejecting** the §475(f) MTM election in the IP-sale-prep window — the lone substantive divergence in the 3-document corroboration set.*
