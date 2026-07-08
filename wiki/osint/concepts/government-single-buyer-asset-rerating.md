---
title: Government single-buyer asset re-rating — cross-sector playbook
type: concept
tags: [concept, event-study, policy-trade, government-procurement, asset-rerate, sell-the-news, monitors]
keywords: [single buyer, turnkey purchase, offtake, price floor, DPA Title III, stigma discount, moncsolidated demand, sell the news]
related:
  - concepts/corrections-reit-asset-sale-event-study.md
  - entities/companies/corecivic.md
  - entities/companies/geo-group.md
  - entities/tickers/pltr.md
  - meta/ice-facility-jobs-cadence.md
  - meta/ice-detention-stats-cadence.md
maturity: draft
created: 2026-07-07
updated: 2026-07-07
---

## Relations

- @concepts/corrections-reit-asset-sale-event-study.md — the CXW/GEO template this generalizes
- @entities/companies/corecivic.md — first observed instance (Jul 2026 turnkey)
- @entities/companies/geo-group.md — pending second leg
- @entities/tickers/pltr.md — data/software analog (DHS/ICE spend)
- @meta/ice-facility-jobs-cadence.md — jobs-signal monitor lane
- @meta/ice-detention-stats-cadence.md — utilization monitor lane

## Raw Concept

Prompted 2026-07-07 by the question: *beyond CXW/GEO, what other industries/companies fit the same government-buyer asset-revaluation + sell-the-news logic, and what monitors apply?* Generalizes @concepts/corrections-reit-asset-sale-event-study.md from private detention into a reusable screen.

## Narrative

### The pattern (4 ingredients)

A tradeable **government single-buyer asset re-rating** needs all four:

1. **Dominant government counterparty** with a **policy mandate + budget surge** — one buyer whose demand can revalue an entire private asset base (ICE/DHS; DoD; DOE).
2. **Private operators owning hard, purpose-built, hard-to-replace assets** carried at a **stigma / policy discount** (ESG-excluded, permit-gated, or out-of-favor) — so the market embeds a low multiple vs replacement cost.
3. **A re-rating catalyst** that converts the government from *renter/regulator* to *buyer/backstop*: **turnkey asset purchase**, **long-term offtake**, **price floor**, **capacity contract**, **DPA Title III award**, or a **direct equity stake**.
4. **A crowded, front-run policy trade** → **sell-the-news** reaction risk; the **form of capital return** (buyback vs debt paydown vs M&A) determines whether the post-event drift is positive. See Campbell REIT event-study finding in @concepts/corrections-reit-asset-sale-event-study.md.

**Trade shape (learned from CXW Jul 6):** the event confirming (1)–(3) is usually **not** the entry; it is often the **exit** for front-runners. The repeatable edge is **pre-event detection** (ingredient timing) + **post-event convergence** only when a hard capital-return catalyst is dated.

### Sector / company candidates (tiered by fit)

| Tier | Sector | Names (tickers) | Government buyer | Re-rate mechanism | Notes |
|------|--------|-----------------|------------------|-------------------|-------|
| **A — direct analog** | Modular / gov housing | **Target Hospitality (TH)** | ICE / HHS / DHS | Family-residential + workforce housing contracts; land + modular assets | Closest operational cousin to CXW/GEO (Dilley/Pecos lineage) `[TENTATIVE]` |
| **A** | Private detention (2nd leg) | **GEO Group (GEO)** | ICE / USMS / BOP | Turnkey facility sale ~$300k/bed; electronic monitoring (BI Inc / ISAP) | Already the pending second leg — @entities/companies/geo-group.md |
| **B — strong cross-sector** | Rare earths / critical minerals | **MP Materials (MP)**, **USA Rare Earth (USAR)**, **Perpetua (PPTA)**, **Lithium Americas (LAC)** | DoD / DOE | Price floor + offtake + **equity stake**; DPA Title III; DOE loan | Govt-as-backstop revalues single-asset miners `[NEEDS VERIFICATION 2026-07-07]` |
| **B** | Nuclear fuel / uranium | **Centrus (LEU)**, **Cameco (CCJ)** | DOE | HALEU/LEU enrichment offtake; strategic reserve buys | Single-buyer enrichment contracts `[NEEDS VERIFICATION 2026-07-07]` |
| **B** | Defense / border-surveillance data | **Palantir (PLTR)**, **Leidos (LDOS)**, **V2X (VVX)** | DHS/CBP/DoD | ImmigrationOS / surveillance / logistics awards | Software multiple, not hard-asset — @entities/tickers/pltr.md |
| **C — watch / counter-case** | Government-tenant REITs | **Easterly Gov Properties (DEA)**, **Postal Realty (PSTL)** | GSA / USPS | Gov buys leased buildings → asset re-rate | **Counter-risk:** DOGE lease terminations cut the other way `[TENTATIVE]` |

### Monitor-lane mapping (which signal fires early)

The lesson from the CXW miss (below): **recorder deed monitors are confirmers, not alpha**. Rank lanes by lead time:

| Lane | Lead time | Applies to | Wired today? |
|------|-----------|------------|--------------|
| **Federal procurement** — USASpending (keyless) / SAM.gov: appraisal, escrow, survey, environmental, title-services awards tied to named assets; J&A notices | **Earliest** (pre-deal diligence) | All tiers | **Yes (2026-07-07)** — `scripts/intel/monitors/procurement.py`. J&A precedent: @sources/ice-ja-26-0143-first-american-escrow-2026.md |
| **Jobs / hiring anomaly** — operator careers feeds, vendor backfill | Weeks | detention, modular housing | **Yes** (ICE) — `scripts/intel/monitors/jobs.py` |
| **Utilization stats** — ICE ADP / capacity; DOE reserve draws | Weeks–months | detention, uranium | **Yes** (ICE) — `scripts/intel/monitors/detention_stats.py` |
| **DoD/DOE announcements** — defense.gov contracts, Federal Register, DPA Title III | Days–weeks | minerals, uranium, defense | **No** |
| **SEC EDGAR full-text** — "turnkey", "definitive agreement", "sale of facility" 8-K/8-K Item 1.01/2.01 | **Coincident** (day-of) | all public tickers | **Yes (2026-07-07)** — `scripts/intel/monitors/edgar_fulltext.py` |
| **County recorder deed index** — grantee = United States | **Lagging** (post-close) | real-asset owners | Partial (ICE) — `scripts/intel/monitors/recorder.py` |

**Priority build order:** (1) ~~SEC EDGAR full-text coincident catch~~ **BUILT 2026-07-07** (`edgar_fulltext.py`; validated live against efts.sec.gov — 22 "turnkey" 8-Ks in a June–July window) → (2) ~~SAM.gov/USASpending early diligence lane~~ **BUILT 2026-07-07** (`procurement.py`; validated live — surfaced **First American Title → U.S. ICE** awards $60k 2026-06-02 + $25k 2025-10-16, the exact pre-diligence signal the recorder missed) → (3) extend jobs/utilization to Tier-A names. Recorder stays as falsifier only.

**Multi-thesis plumbing (2026-07-07):** `scripts/intel/paths.py` now resolves the active thesis from `CEMINI_THESIS_ID` (default `ice-turnkey`) or a per-call `thesis_id=`, so one monitor codebase serves `gov-asset-rerate` without forking paths. Run the lanes:
- EDGAR: `python3 scripts/gov_asset_edgar_monitor.py --thesis gov-asset-rerate --notify` (config `edgar-fulltext.yaml`)
- Procurement: `python3 scripts/gov_asset_procurement_monitor.py --thesis gov-asset-rerate --notify` (config `usaspending.yaml`)

**Live procurement finding (2026-07-07):** the first sweep already returned **First American Title Insurance Company** contracts awarded by **U.S. Immigration and Customs Enforcement** — a title/escrow vendor + ICE combination that is a leading (weeks–months) indicator of facility-acquisition diligence, consistent with the J&A precedent. Worth a standing watch; escalate on **new** ICE-side title/escrow/appraisal awards tied to named GEO/CXW/TH sites. `[NEEDS VERIFICATION 2026-07-07]` tie specific awards to specific facilities.

### Why the CXW recorder monitor didn't fire `[CONFIRMED 2026-07-07]`

Three independent failure modes — a case study in why deed monitors are weak alpha:

1. **Not scheduled** — no `com.cemini.recorder` LaunchAgent installed; last report is `2026-07-02` (close date), **nothing ran on Jul 6** (8-K day). Install: `bash scripts/install_recorder_discord_launchagent.sh`.
2. **Blind spots on the exact sold sites** — Kern (Cal City) is manual index-only (no headless search); San Diego (Otay) is **Akamai-WAF blocked** in headless → needs Owner Alert subscription. Both sold sites were un-queryable by automation.
3. **Structural lag** — a grant deed to the United States records **after** the 8-K/PR (and after any leak). The recorder can only *confirm*, never *front-run*, a same-day-filed federal purchase.

**Takeaway:** re-weight the thesis monitors toward **procurement (SAM.gov)** and **EDGAR full-text** lanes; treat recorder as a falsifier. The jobs.yaml `event_watch` already flags this ("8-K … confirmation/falsifier, not alpha source").

### Open questions to resolve via Exa

- Does **Target Hospitality** own (vs lease) the land under its ICE/HHS sites? (determines whether a turnkey-sale re-rate is even possible) `[NEEDS VERIFICATION 2026-07-07]`
- Real, dated instances of **DoD/DOE equity stakes or price floors** revaluing MP/USAR/PPTA/LEU in 2025–2026, and the announcement-day reaction (sell-the-news or sustained?) `[NEEDS VERIFICATION 2026-07-07]`
- Whether **DEA/PSTL** gov-tenant REITs have any precedent of the government *buying* leased buildings (vs terminating leases). `[NEEDS VERIFICATION 2026-07-07]`

## Dead Ends

- **County-recorder-as-alpha** — three failure modes above. Kept as a falsifier lane only; do not size a trade on recorder silence or a recorder hit.

## Snippets

> 8-K Item 1.01 / 2.01 facility-sale disclosure (confirmation/falsifier, not alpha source)
> — [Source: config/theses/ice-turnkey/jobs.yaml event_watch (retrieved 2026-07-07)]
