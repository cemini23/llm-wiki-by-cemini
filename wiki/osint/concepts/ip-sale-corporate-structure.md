---
title: IP-sale corporate structure (HoldCo / OpCo dual-entity)
type: concept
tags: [concept, legal, tax, m-and-a, cemini-internal, ip-sale]
keywords: [wyoming, florida, holdco, opco, smllc, charging-order, 475f, 3a5-4, lgpl]
related:
  - sources/3-9-pm-research.md
  - sources/3-10-algorithmic-trading-ip-sale-audit.md
  - sources/3-19-compliance-research.md
  - sources/3-19-ip-sale-research.md
  - concepts/ip-sale-readiness.md
  - concepts/irc-1235-capital-gains-safe-harbor.md
  - concepts/replacement-cost-valuation.md
  - concepts/milestone-ledger.md
  - concepts/publishers-exclusion-apa.md
  - entities/frameworks/nautilustrader.md
maturity: validated
created: 2026-04-27
updated: 2026-04-27
---

## Relations

- @sources/3-9-pm-research.md — para 124 prescribes the dual-entity framework (IP HoldCo Wyoming-or-Delaware, OpCo Florida LLC) plus §475(f) MTM election; K5 deep-read 2026-04-26
- @sources/3-10-algorithmic-trading-ip-sale-audit.md — full §2(a) audit of dual-entity prescription (Wyoming chosen over Delaware on cost + charging-order + privacy grounds); §475(f) **rejected** for IP-sale-prep window (divergence with 3-9); K6 deep-read 2026-04-27
- @sources/3-19-compliance-research.md — concurrent regulatory framing (SEC dealer-rule 3a5-4 sub-$50M exclusion, Reg ATS, broker-dealer carve-outs)
- @sources/3-19-ip-sale-research.md — APA / earnout structuring (the deal layered on top of this corporate skeleton)
- @concepts/ip-sale-readiness.md — parent thesis; this page is the dedicated "component 6 (tax + legal structure)" expansion
- @concepts/irc-1235-capital-gains-safe-harbor.md — capital-gains regime that the disregarded-entity SMLLC choice preserves
- @concepts/replacement-cost-valuation.md — the valuation anchor that justifies the IP-segregation rationale (preserve the asset that's being valued)
- @concepts/milestone-ledger.md — the ledger that documents which IP shipped and when, which the HoldCo formally owns
- @concepts/publishers-exclusion-apa.md — APA carve-out mechanic that interlocks with the dual-entity structure
- @entities/frameworks/nautilustrader.md — the LGPL-3.0 dependency whose architectural-isolation requirement informs the OpCo-side container topology (separate-work doctrine)

## Raw Concept

The question this page answers: **What is the prescribed corporate-entity structure for a sub-$1M solo-operator AI trading platform being readied for an IP sale to an institutional acquirer?**

Synthesized from two corroborating Cemini-internal audits authored within ~2 days of each other (3-9-pm-research published 2026-03-08, 3-10-ip-sale-audit published 2026-03-10) and the broader 3-19 compliance + IP-sale research bundle. Both 3-9 and 3-10 converge on the dual-entity HoldCo / OpCo framework; they diverge on the §475(f) Mark-to-Market election (3-9 endorses, 3-10 rejects for IP-sale-prep purposes — see §475(f) discussion below).

## Narrative

**[CONFIRMED — 2026-04-27 K6 deep-read] doc-only.** Legal/tax review deliverable. No engineering milestone tied to this page; it captures the prescribed structure as a future reference. As of 2026-04-27, the deployed entity is a **Florida single-member LLC** only — the Wyoming HoldCo half of the prescription is unbuilt (see "Current state vs prescribed" below).

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

### §475(f) Mark-to-Market — the divergence

The two source audits **disagree** on whether the trading OpCo should make a §475(f) MTM election:

- **3-9-pm-research para 124** — recommends MTM. Rationale: Trader Tax Status removes capital-loss limitations and wash-sale accounting burdens during the high-frequency paper-trading validation phase, which is the operational regime for the OpCo.
- **3-10-ip-sale-audit §2** — rejects MTM. Rationale: The IP-sale-prep window is the wrong moment to flip an irrevocable election that converts trading gains/losses to ordinary income. The IP-sale event itself is the dominant tax outcome, and MTM ordinary-income treatment on the operational side does not interlock cleanly with §1235 capital-gains treatment on the IP side.

**Reconciliation**: the divergence is real but resolvable on object-of-the-tax. The two recommendations are addressing different things:
- 3-9 is optimizing the **OpCo's trading-book P&L** during paper-trading.
- 3-10 is optimizing the **HoldCo's IP-sale tax outcome** at exit.
Both can be true. The decision rule is timing: if the IP sale is imminent (≤24 months), defer MTM; if the operational regime will run multi-year, MTM may pencil. The §475(f) election is irrevocable absent IRS consent (Rev. Proc. 99-17) — file with eyes open.

### LGPL-3.0 architectural isolation as a corporate-structure adjacency

A side note that matters because it interlocks with the OpCo's Docker topology: NautilusTrader (see @entities/frameworks/nautilustrader.md) is licensed LGPL-3.0. LGPL-3.0's "separate work" doctrine permits proprietary code to use an LGPL library as long as the library is not statically linked into the proprietary work. **Architectural isolation pattern**: confine the LGPL library to its own Docker container; proprietary engines (the strategy and risk-engine containers) communicate with it over a network boundary — JSON `TradeSignal` payloads (Pydantic v2 schemas) over Redis pub/sub. This constitutes "separate work communicating at arm's length" and immunizes the proprietary engines from viral copyleft.

The corporate-structure relevance: the IP HoldCo owns the proprietary engines. The LGPL-isolated container is conceptually OpCo-side infrastructure. The architectural pattern is what makes the HoldCo's IP cleanly transferable in an APA without dragging LGPL-tainted artifacts into the deal.

### SEC Rule 3a5-4 dealer-registration carve-out

3-19-compliance-research and 3-10-ip-sale-audit both note that the new SEC dealer-registration rule (Rule 3a5-4, finalized 2024) attaches qualitative liquidity-provision tests at $50M+ AUM. A sub-$1M solo-operator OpCo sits comfortably under the threshold. The carve-out is structural — no special filing required to invoke it — but it informs the **scaling-tripwire**: if the OpCo grows past ~$25M AUM during the IP-sale-prep window, dealer-registration analysis becomes mandatory and the corporate structure may need to bifurcate further (separate dealer-registered execution sub-entity).

### Current state vs prescribed (server reality)

| Component | Prescribed (3-10 §2(a)) | Deployed (2026-04-27) | Gap |
|---|---|---|---|
| Wyoming IP HoldCo | Wyoming SMLLC, anonymous agent, ~$162/yr total | None | **Not formed** |
| Florida Trading OpCo | Florida SMLLC | Florida SMLLC ✓ | None |
| Operational license between them | License agreement HoldCo → OpCo | N/A (no HoldCo) | **Pending HoldCo formation** |
| §475(f) MTM election | Reject for IP-sale-prep window | Not elected ✓ (consistent with 3-10) | None |
| Architectural isolation (LGPL) | Container-isolated NautilusTrader | NautilusTrader in deps; container topology TBD per K5 | **Spot-check** |

The deployed Florida SMLLC alone is sufficient for §1235 capital-gains treatment if the founder is the sole member and the APA structures the deal as an asset purchase of substantially all rights. The Wyoming HoldCo upgrade is a **risk-reduction step** (insulation + charging-order + privacy), not a §1235 prerequisite.

### Decision rule for when to form the HoldCo

The prescribed sequencing per 3-10 is: form the Wyoming HoldCo **before** the first APA term sheet circulates. The reasoning is that an acquirer's deal counsel will scrutinize the IP chain-of-title — having the IP already vested in a clean HoldCo at term-sheet time avoids a mid-deal asset-restructuring sub-project that delays close. If the founder is not in active deal conversations, the HoldCo formation can wait; the cost of forming early is ~$162/year carrying cost plus paperwork.

## Snippets

> To fully insulate the intellectual property during the paper-trading validation phase, the overarching corporate entity should adopt a dual-structure framework: an IP HoldCo (registered in Wyoming or Delaware) that exclusively owns the source code and neural network weights, granting a limited operational license to a trading OpCo (e.g., a Florida LLC). The trading entity must execute a Section 475(f) Mark-to-Market election to achieve "Trader Tax Status," exempting the firm from capital loss limitations and wash sale accounting burdens during high-frequency validation.
>
> *— @sources/3-9-pm-research.md para 124. The 3-9 source's prescriptive paragraph; explicitly endorses §475(f) MTM. Note that 3-9 lists Wyoming **or** Delaware without choosing; 3-10 makes the Wyoming-specific case.*

> The recommended structure is a Wyoming-domiciled IP HoldCo (single-member LLC) with statutory charging-order protection per W.S. §17-29-503, paired with a Florida-domiciled trading OpCo (single-member LLC). Wyoming's formation and annual-maintenance costs (~$102 + ~$60) are materially below Delaware's, and Wyoming statute (unlike Delaware case law) explicitly extends charging-order-only remedy to single-member LLCs. Anonymous registered-agent formation is permitted in Wyoming.
>
> *— @sources/3-10-algorithmic-trading-ip-sale-audit.md §2(a). The 3-10 source's prescriptive paragraph; chooses Wyoming-over-Delaware on cost + statutory charging-order + privacy grounds. Diverges from 3-9 by **rejecting** the §475(f) MTM election in the IP-sale-prep window.*
