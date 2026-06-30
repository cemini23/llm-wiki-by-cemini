---
title: CoreCivic California City ICE turnkey research synthesis (June 2026)
type: concept
tags: [concept, osint, corecivic, ice, california, detention, event-study]
keywords: [CXW, California City, turnkey, Gomez Ruiz, Bonta, SB 29, federal purchase, DRI]
related:
  - entities/companies/corecivic.md
  - entities/tickers/cxw.md
  - entities/facilities/california-city-detention-facility.md
  - entities/companies/geo-group.md
  - concepts/geo-ice-turnkey-acquisition-thesis.md
maturity: draft
created: 2026-06-29
updated: 2026-06-30
---

## Relations

- @entities/companies/corecivic.md — operator / prospective seller
- @entities/tickers/cxw.md — listed equity
- @entities/facilities/california-city-detention-facility.md — 2,560-bed ICE site (Kern County)
- @entities/companies/geo-group.md — parallel turnkey peer (GEO)
- @concepts/geo-ice-turnkey-acquisition-thesis.md — shared ICE acquisition thesis (GEO-led April briefs)

## Raw Concept

Multi-track OSINT synthesis (local, state, federal, corporate, litigation) on whether **CoreCivic's California City Detention Facility** blocks, delays, or discounts ICE's hypothesized **turnkey federal purchase** of private detention assets. Session date 2026-06-29; complements @concepts/geo-ice-turnkey-acquisition-thesis.md with CXW-specific legal and operational friction.

## Narrative

### Facility snapshot

| Field | Value |
|-------|-------|
| **Operator / owner** | CoreCivic (CXW) |
| **Capacity** | 2,560 beds (operator); **1998 CUP authorizes 2,304**; city staff cited 2,816 — bed-count mismatch is live appeal issue `[CONFIRMED]` |
| **Address** | 22844 Virginia Blvd, California City, Kern County |
| **Opened** | Aug 27, 2025 (partial city entitlements) `[CONFIRMED]` |
| **ICE contract** | ~$130M through Aug 2027 (announced Sept 29, 2025) `[CONFIRMED]` |
| **Occupancy (Q1 2026)** | 1,817 detainees as of Mar 31, 2026 `[CONFIRMED]` |

### Federal turnkey frame (shared with GEO)

ICE's **Detention Reengineering Initiative (DRI)** targets ~92,600 beds / $38.3B by end FY2026 (Nov 30, 2026). Internal documents describe federal ownership to **circumvent state-level restrictions** `[CONFIRMED]`. **Ten turnkey slots** (existing CoreCivic/GEO-operated sites) are tier-1 design, not merely a warehouse fallback `[CONFIRMED]`.

WaPo draft reporting (Dec 2025) lists **two CoreCivic California facilities** plus six GEO sites; only **Tacoma** and **Aurora, CO** named publicly `[CONFIRMED]`. The two CXW CA targets are almost certainly **California City** and **Otay Mesa** — CoreCivic's only two CA ICE facilities `[INFERENCE]`.

**Funding:** OBBBA appropriated ~**$45B** for detention through **Sept 30, 2029** — no Q2–Q3 2026 use-it-or-lose-it cliff `[CONFIRMED]`. Cal City already under ICE contract through **Aug 2027** (~$130M/yr); ICE holds beds without owning `[CONFIRMED]`.

Zoley (GEO) and Swindle (CoreCivic) confirmed active sale discussions on Q1 2026 earnings calls; Zoley guessed **late Q2 / early Q3** for announcements `[CONFIRMED]`. Swindle prices off **depreciated replacement cost** (no public comps); expects to **retain management contract** post-sale `[CONFIRMED]`. As of 2026-06-29, **no CXW/GEO facility-sale 8-K** `[CONFIRMED]`. CXW Q1 guidance **excludes dispositions**; Apr 2026 **$100M term loan** framed alongside "potential asset sales" liquidity option `[CONFIRMED]`.

**Benchmark (Jun 26, 2026):** Bill Sutherland, PT **$36**, **80% probability × 2 facilities ≈ $680M after-tax** at 8.5× FY2027 EBITDA — **sites not named** in public coverage `[CONFIRMED note / TENTATIVE facilities]`.

**Authority:** 8 U.S.C. § **1231(g)(1)** — acquire/build/operate detention facilities; **1231(g)(2)** — must consider purchase/lease of **existing** prisons/detention centers before new construction `[CONFIRMED]`.

### Legal layers — honest read

#### Federal purchase vs local appeal

| Question | Answer | Tag |
|----------|--------|-----|
| Can ICE buy while California City appeal is pending? | Yes legally; DHS may delay for diligence/optics | `[LIKELY]` |
| Does city approval block federal acquisition? | No — sale is CoreCivic → U.S.; municipal appeal is not a title encumbrance | `[CONFIRMED]` |
| After federal ownership, need city business license / site plan? | **Core federal detention mission:** no ordinary city permission required. **Expansion/alteration:** 40 U.S.C. § 3312 consult process; **CXW as operator:** neutral state laws (labor, workers' comp) may still bite | `[LIKELY]` |
| Does Gomez Ruiz PI block purchase? | No — binds **conditions**, not title transfer | `[LIKELY]` |

#### Regime switch — preemption vs concurrent jurisdiction (2026-06-30)

**Paradigm:** While **CoreCivic owns** → **State/local vs private operator** (CUP, business license, site plan, Bonta letters bite). After **U.S. acquires title** → **State vs federal sovereign** on detention mission; local zoning/CUP cannot permanently veto ICE-owned federal detention `[INFERENCE]`.

| Authority / doctrine | Application to Cal City | Tag |
|---------------------|-------------------------|-----|
| **Supremacy Clause** + **intergovernmental immunity** | Local CUP/zoning cannot lock doors of **federally owned** ICE detention executing federal mandate; DOJ injunction likely if city tries | `[INFERENCE]` |
| ***GEO Group, Inc. v. Newsom***, 50 F.4th 745 (9th Cir. 2022) (en banc) | California **cannot ban ICE** from using private contractors for immigration detention (AB 32); municipal ban weaker still | `[CONFIRMED]` |
| **40 U.S.C. § 3312** (Public Buildings Act) | Federal agency **must consult** local zoning on construction/alteration; **§3312(f)** — state/local lack jurisdiction to **veto** federal compliance with that section | `[CONFIRMED]` |
| **40 U.S.C. § 3112** | Federal acquisition does **not** automatically create **exclusive** federal jurisdiction; **concurrent** state jurisdiction unless formally accepted | `[CONFIRMED]` |
| **8 U.S.C. § 1231(g)** | Statutory authority to acquire/operate detention facilities | `[CONFIRMED]` |

**What survives post-purchase:** Gomez Ruiz PI + monitor; AB 103 (weakened); NEPA/APA (Gilroy template); **neutral, generally applicable** state laws — e.g. **workers' compensation** (Bonta hook), **Cal/OSHA**, health/building codes against **CoreCivic as employer/contractor** (not “release detainees” orders) `[TENTATIVE]`.

**What does not:** SB 29 local permit layer for **federal acquisition**; ordinary city **business license** for **federal operations on federal property** `[LIKELY]`.

#### Transaction / diligence layer (delay, not block)

11-model local-entitlement super-audit + external legal cross-ref (2026-06-30) — `.local/reports/audit/super-audit-cal-city-local-2026-06-30.md`:

| Issue | Pre-purchase impact | Post-purchase |
|-------|---------------------|---------------|
| **Dirty entitlement file** (appeals pending, Aug 2025 ops before Feb 2026 approvals) | **Closing conditions** — reps/warranties, **indemnity/escrow** (ICE OPLA / buyer counsel) | Mostly moot for title |
| **Bed-count mismatch** | **Underwrite at 2,304** (1998 CUP) until cured; 2,560 = operator claim; 2,816 = city staff cite — **256-bed / ~10% capacity haircut** on purchase math at risk `[INFERENCE]` | CUP cap limits **growth/pricing**, not current ops (1,817 < 2,304) |
| **Two appeal tracks** | Site plan → **PC (July 7)**; business license → **City Manager Grayson** (separate, sharper ops lever) | Moot for federal mission |
| **Purchase delay vs accelerate** | **Delay ~6–8/10** (diligence, price, optics); **accelerate ~2–4/10** (escape motive ≠ fast close) | Federal buy removes local license/zoning leverage |

**Operator thesis validated:** local friction **delays/reprices** federal purchase; **does not** permanently block federal detention or empty ~1,817 beds in 30–90 days `[TENTATIVE]`.

#### California state tools

| Tool | Pre-purchase (private CXW) | Post-federal ownership |
|------|---------------------------|-------------------------|
| **SB 29** local permit | Active — @entities/facilities/california-city-detention-facility.md DNDC suit | Bypassed for acquisition |
| **City license / site plan appeal** | July 7 PC site plan `[LIKELY]`; BL → City Manager Grayson | **Moot for core federal ops**; contractor/neutral-law friction may remain |
| **AB 32** private-detention ban | Unenforceable vs ICE contractors (GEO v. Newsom, 9th Cir. 2022) | Stronger federal shield |
| **AB 103** AG inspections | Bonta inspected Nov 2025; 5th report May 2026; Dec 19, 2025 DHS letter | **Weakened** — non-discriminatory inspection upheld (*U.S. v. California*, 921 F.3d 865) but access cooperation-dependent vs federally owned+operated site `[TENTATIVE]` |
| **AB 1801** (2025–26) | Assembly passed Apr 2026; Senate Judiciary + Local Gov — **not enacted** | **No effect** on direct federal purchase |
| **Gomez Ruiz PI + monitor** | Binds ICE/CoreCivic operations | **Still binds operations** (federal court) |
| **Federal procedural (NEPA/INA/APA)** | Gilroy model available | **Primary remaining CA lever** post-purchase — *Santa Clara v. ICE* (N.D. Cal. 5:26-cv-05604, filed Jun 10, 2026) `[CONFIRMED]` |

**Premise:** As of 2026-06-29 there is **no completed federal purchase** — Cal City is **CoreCivic-owned** under ICE contract; full state/local toolkit applies until a sale closes `[CONFIRMED]`.

#### Local proceedings (California City)

- **Feb 26, 2026:** City staff approved business license + site plan; administrative appeals filed late Feb 2026 `[CONFIRMED]`.
- **June 15, 2026:** AG Rob Bonta letter urges rejection of both appeals; cites SB 29, AB 103 conditions, federal litigation; asks ≥10-day public notice before hearings `[CONFIRMED]`.
- **June 16, 2026:** **Planning Commission meeting canceled — lack of quorum**; next regular PC meeting scheduled **July 7** `[CONFIRMED]` (city PDF).
- **July 7, 2026 — site plan appeal hearing:** **Multi-source scheduled** — city PC calendar (post–Jun 16 cancel), coalition notices (`bit.ly/iceout7726`), **Dolores Huerta Foundation flyer** (Jul 7, 5–6pm press / **6–8pm Site Plan Review Appeal**, 21000 Hacienda Blvd) `[LIKELY]`. Aligns with Bonta letter: **site plan appeal → Planning Commission**; **business license appeal → separate track** (City Manager Grayson per OAG letter, not necessarily same evening/Council vote). **Not a dispositive federal-purchase catalyst**; quorum-fail risk (Jun 16 precedent). Official city agenda PDF still ideal confirmation `[NEEDS VERIFICATION 2026-07-01]`.
- **Mayor Hawkins:** AG comments are recommendations; city **cannot halt federal detention**; lacks resources for litigation; will follow appeals process `[CONFIRMED]`. Council **quorum gaps** (2026) stalled formal action `[CONFIRMED]`.
- **Inadvertent.news (May 12, 2026):** CoreCivic Aug 2025 SB 29 **indemnification** letter; mayor says city paying defense on "city's dime" `[CONFIRMED]`.

**Appeal process:** Administrative appeal of Feb 26 entitlements lands at **City Council** (Municipal Code Title 1 Ch. 4 — Sec. 1-4.09; business license Sec. 3-2.3.204 appealable to Council; site plan Sec. 9-2.212). Bonta's substantive hooks: incomplete application materials; **detention use vs 1998 prison CUP**; bed-count mismatch `[CONFIRMED]`. **Appellant identity not named** in public sources `[NEEDS VERIFICATION 2026-06-29]`.

### Litigation (high-signal items often missed)

#### Gomez Ruiz v. ICE (N.D. Cal. 3:25-cv-09757) — conditions class action

Prison Law Office, ACLU, Keker — class of all detainees at California City.

| Date | Event |
|------|-------|
| Nov 12, 2025 | Class action filed |
| Dec 22, 2025 | TRO on urgent medical care |
| **Feb 10, 2026** | **PI granted in part** — medical staffing, attorney access, clothing, outdoor rec |
| **Feb 10, 2026** | Provisional class certified |
| **Mar 30, 2026** | Dr. Anandkumar appointed **external monitor** |
| Mar 2026 | CoreCivic intervenes; moves to **stay PI** pending appeal |
| **May 14, 2026** | Court **denies CoreCivic stay** — may not be fully reimbursed for compliance costs; Ninth Circuit appeal **26-1294** |

**Thesis impact:** Facility continues operating under **court-ordered compliance cost + monitor** — operational friction ICE/CoreCivic inherit on sale; not a municipal kill switch.

#### Dignity Not Detention v. California City / CoreCivic (E.D. Cal. 1:25-cv-01292)

SB 29 / permit challenge (Oct 2025). CoreCivic motion to dismiss (Jan 2026); city joined. **Mar 13, 2026:** Judge Thurston — decided on papers; **6+ month delay** (judicial resource emergency); no hearing scheduled `[CONFIRMED]`.

### ICE leadership / timing

| Date | Event |
|------|-------|
| Jun 1, 2026 | David Venturella (ex-GEO EVP) acting ICE director |
| Jun 27, 2026 | Trump nominates Lance Schroyer (Oklahoma field ops) as ICE director — third leadership change in ~8 weeks |
| DRI internal memo (Feb 5, 2026) | Venturella named debating detainee length-of-stay with USCIS Deputy Chief Tim Kaiser |

Venturella (ex-GEO EVP, ~$6M GEO compensation) acting since Jun 1; **Warren ethics letter (May 27, 2026)** demands recusal from GEO-benefiting matters `[CONFIRMED]`. Schroyer nominated **Jun 27, 2026**; Venturella stays until confirmation `[CONFIRMED]`. Mullin: DHS pivot to **"existing detention space with state/county partners"**; ~2/3 warehouse buys off-loaded; **DHS IG cost audit** (Salt Box: warehouses ~134% over market) chills large acquisitions `[CONFIRMED]`.

### Congressional / appropriations (Jun 2026) — post super-audit

| Date | Event | Tag |
|------|-------|-----|
| Jun 2, 2026 | Senate Approps HS — Mullin FY27 budget; **Delaney Hall (NJ)** (Britt/Murphy) | `[CONFIRMED]` |
| Jun 3, 2026 | House HS authorizing — FY27 DHS budget review | `[CONFIRMED]` |
| Jun 5, 2026 | House Approps HS **subcommittee markup** | `[CONFIRMED]` |
| Jun 10–12, 2026 | House Approps full committee → **H.R. 9310** reported; §223 **execution plan** for PL 119-21 funds | `[CONFIRMED]` |
| **Jun 25, 2026** | **House Approps HS oversight** — Mullin testimony (operator “last week” gap) | `[CONFIRMED]` |
| Jun 27, 2026 | Schroyer nominated ICE Director | `[CONFIRMED]` |

**Jun 25 hearing substance** `[CONFIRMED]` (AP, FNN, C-SPAN): HRW/PHR report (**52 deaths** cited); heated Underwood/DeLauro exchanges on custody deaths and reporting; Mullin ends **WEXMAC** DoD detention contract use; **reevaluating 11 warehouse purchases** (~$700M; due diligence failures); not a turnkey-8-K catalyst — **oversight friction** on expansion.

**Funding architecture (audit correction):** Turnkey **acquisition capital** primarily **OBBBA / PL 119-21 ~$45B detention line** (through ~FY2029) **plus** **Secure America Act (S. 2) ~$70B ICE/CBP** enacted **Jun 10, 2026** (second reconciliation tranche) `[CONFIRMED]`. FY27 bill (H.R. 9310, reported Jun 12) funds **base beds + O&S**; **§223** execution plan for PL 119-21 funds; **§218** bars ICE O&S funds for detention contracts where **two most recent OPR performance evals < “adequate”** — potential **Cal City contract risk** if Gomez Ruiz monitor findings flow into OPR scores `[CONFIRMED bill text; NOT enacted]`. Senate markup **not scheduled** as of 2026-06-29 `[NEEDS VERIFICATION]`. CR from Oct 1 historically likely — slows obligational rhythm, does not erase reconciliation authority.

**Purchase vs contract (Opus audit):** Mullin Jun 25 language favors **contracting existing operator beds** over **ownership transfer** — base case may be **revenue continuity without 8-K**, not failed program.

**Super-audit (11-model, 2026-06-30):** **REWORK** — all 11 auditors **WARN**; thematic framework OK; demote July 7 / jet / FY27-as-gate; Cal City first tranche **~10–20%**. Mega: `.local/reports/audit/super-audit-ice-turnkey-mega-2026-06-30.md`; **local entitlement:** `.local/reports/audit/super-audit-cal-city-local-2026-06-30.md`; full thesis: `.local/reports/audit/ice-turnkey-complete-thesis-2026-06-30.md`.

### Comparable — delay not death

**Leavenworth (CoreCivic):** KS Court of Appeals **upheld local SUP injunction Feb 27, 2026**; ~11 months delay; SUP approved early Mar 2026; intake resumed Mar 12 — contract stayed live `[CONFIRMED]`. **McFarland (GEO):** SB 29 PI template for CA expansion fights `[CONFIRMED]`.

### Capacity / demand (bear overlay)

ICE detained population **~58k daily avg** (Jun 2026) vs **~72k Jan peak**; officials cite **excess capacity** vs detainees `[CONFIRMED direction]`. CXW+GEO **>20,000 idle beds**. Cal City is **revenue continuity** (~1,817 occupied Mar 2026) more than **must-have critical-path capacity** `[INFERENCE]`.

### Open legislative watch — SB 1367 (Cervantes, 2026)

Would bar cities/counties from approving new land uses / change-of-use for detention (charter cities included). Senate Local Gov passed Apr 2026; re-referred Jun 2026 — **not law** as of 2026-06-29 `[CONFIRMED status]`. Would harden zoning overlay if enacted.

### Bull / bear scorecard

| Factor | Bull | Bear | Weight |
|--------|------|------|--------|
| ICE/DHS strategic intent | DRI mandates 10 turnkey; bypass CA explicit | Warehouse retreat; IG audit; Mullin stewardship | High |
| Earnings language | Active sale talks; Q2–Q3 window | CXW guidance excludes dispositions; Q2 elapsed | High |
| Leadership | Venturella ran negotiations | Schroyer confirmation pause | Medium |
| California City legal | Federal buy moots local appeal | Gomez Ruiz PI + monitor; Ninth Circuit appeal | High |
| California City local | Pre-close noise only | Bonta + organizers; indemnity dispute | Medium |
| Portfolio sequencing | 2 CXW CA sites on WaPo list; **buying escapes AB 103/SB 29** (Lever) | CA City legally encumbered; CXW wants replacement-cost pricing — stalemate risk | Medium |
| Demand | OBBBA funding; H2 pop recovery possible | Detained pop falling; ICE excess capacity | Medium |
| Analyst | Benchmark ~80% × 2 facilities, ~$680M (sites unnamed) | No 8-K; facilities not in CXW guidance | Medium |

#### Probability table (subagent merge, 2026-06-29)

| Scenario | P | Tag |
|----------|---|-----|
| ≥1 CXW or GEO facility sale to ICE within 12 mo | **~40–55%** (post-audit) | `[TENTATIVE]` |
| CXW sells ≥1 facility within 12 mo | **~45–55%** | `[TENTATIVE]` |
| Benchmark two-facility / ~$680M as modeled | **~35–45%** | `[TENTATIVE]` |
| **California City in first tranche** | **~10–20%** | `[TENTATIVE]` |
| **Closed federal purchase of Cal City in Q2–Q3 2026** | **Low** | `[INFERENCE]` |
| Sale 8-K before end Q3 2026 | ~30–40% | `[TENTATIVE]` |

#### Aggregate scores (1–10, session 2026-06-29)

| Lens | Score | Notes |
|------|-------|-------|
| Bull — turnkey thesis (GEO+CXW, 2026) | 6.5 | Real strategy; timing/price soft |
| Bull — California City in **first tranche** | 4 | PI + monitor + quorum-fragile July 7 |
| Bull — CXW paid for CA City specifically | 5 | Escape-state-oversight motive vs legal baggage |
| Bear — local appeal kills ops | 2 | Mayor + federal-buy workaround |
| Bear — Gomez Ruiz shuts intake | 3 | PI improves conditions; stay denied May 14 |
| Bear — no sales in 2026 | 3 | DRI Nov 30 + OBBBA; price stalemate possible |
| **Net Cal City near-term catalyst** | **~5** | Muddle-through / delay, not clean July 7 event |

### Base case (revised 2026-06-29, post subagent merge)

**Turnkey program is real (~6.5/10 bull-leaning)** but **closed Cal City purchase in Q2–Q3 2026 is unlikely**. Cal City reads as **delay-prone revenue continuity**, not critical-path capacity. **First tranche** likely cleaner GEO sites (Tacoma, Aurora) + stabilized non-CA CXW assets — unless ICE **prioritizes CA purchases to escape AB 103/SB 29** (Lever), in which case Cal City could be **discounted tranche 1**, not clean tranche 1. **Price stalemate** (Swindle replacement-cost vs ICE diligence) can slip any deal past Q3.

July 7 is **quorum-fragile** and **forum-contested** — not a reliable binary catalyst.

### Watchlist

| Priority | Catalyst | Trigger |
|----------|----------|---------|
| 1 | CXW/GEO **8-K** facility sale | Any day Q3 |
| 1b | **Senate Approps HS markup** + Schroyer confirmation | Congress.gov |
| 2 | **July 7 forum + agenda + quorum** (local noise) | City PDF / Granicus 72 hrs prior; PC vs Council |
| 2b | **N5000P / EJM55** DC weekend ADS-B export | Hex A63C56; ADS-B Exchange premium |
| 3 | **Gomez Ruiz** monitor / compliance escalation | E.D. Cal. docket |
| 4 | ICE **detained-population trend** | Vera / Deportation Data Project |
| 5 | **SB 1367** + **AB 1801** progression | CA Legislature |
| 6 | Schroyer confirmation | Senate |
| 7 | CXW **Q2 call** (~Aug 2026) | Buyback vs sale posture |

**Cemini posture:** wiki-only synthesis; no prod brief unless operator reopens CXW/GEO workstream.

## Snippets

> "Federal ownership model is designed to circumvent state-level restrictions."
> — [Source: Detention Pipeline / DRI research note (retrieved 2026-06-29)](https://detention-pipeline.transparencycascade.org/entry/national-detention-buildout-strategy-2026/)

> "Our guidance … does not include any additional acquisitions or dispositions, including the impact on earnings … that could result from any dispositions."
> — [Source: CoreCivic Q1 2026 earnings press release (retrieved 2026-06-29)](https://ir.corecivic.com/news-releases/news-release-details/corecivic-reports-first-quarter-2026-financial-results)

> "I look at it through the lens of what does it cost to build a facility today and what would that be on a **depreciated replacement cost** basis."
> — [Source: CXW Q1 2026 earnings call, Swindle (retrieved 2026-06-29)](https://www.insidermonkey.com/blog/corecivic-inc-nysecxw-q1-2026-earnings-call-transcript-1756881/)

> "DHS is moving swiftly to utilize **EXISTING** detention space with our state and county partners."
> — [Source: AP Mullin warehouse retreat coverage (retrieved 2026-06-29)](https://apnews.com/article/mullin-immigration-ice-warehouses-detention-c91e9a991664a7cdc18fe2e54138c9c4)

> Bonta urges California City to reject CoreCivic business license and site plan appeals; cites dangerous conditions under AB 103 and ongoing federal litigation.
> — [Source: OAG press release 2026-06-15](https://oag.ca.gov/news/press-releases/attorney-general-bonta-urges-city-leaders-reject-corecivic%E2%80%99s-applications)

## Dead Ends

- **July 7 as thesis kill switch** — forum contested (PC vs Council); June 16 quorum-fail precedent; not a confirmed dispositive ruling.
- **Bonta letter as legal veto** — recommendation to city only; no AG power to block federal acquisition.
- **Cal City automatically last in tranche** — buying may *prioritize* CA assets to escape state oversight; legal baggage still discounts price/timing.
