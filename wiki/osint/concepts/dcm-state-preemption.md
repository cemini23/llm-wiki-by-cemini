---
title: "DCM state-preemption (CFTC exclusive-jurisdiction vs. state authority over event contracts)"
type: concept
tags: [concept, legal, regulatory, preemption, prediction-markets, cftc, dcm, cemini-leverage]
keywords: [DCM, exclusive jurisdiction, swap, gaming, preemption, CEA Section 5c(c)(5)(C), Sixth Circuit split, Younger abstention]
related:
  - sources/substack-rss-event-horizon-2026-07-16-kalshi-teleprompter-insider.md
  - sources/substack-rss-event-horizon-2026-07-15-kalshi-flights-compute-cftc.md
  - sources/substack-rss-event-horizon-2026-07-14-kalshi-wc-volume-pro.md
  - sources/substack-rss-event-horizon-2026-07-13-kalshi-app-downloads.md
  - entities/tools/congress-legislators.md
  - sources/substack-rss-event-horizon-2026-07-08-kalshi-sdny-pi-denial.md
  - sources/substack-rss-event-horizon-2026-07-10-its-states-vs-prediction-markets-not-casinos-vs.md
  - sources/3-19-compliance-research.md
  - sources/cftc-anprm-prediction-markets-2026-03-16.md
  - sources/cftc-selig-house-ag-testimony-2026-04-16.md
  - sources/cftc-v-arizona-tro-liburdi-2026-04-10.md
  - entities/platforms/kalshi.md
  - entities/platforms/polymarket.md
  - concepts/ip-sale-readiness.md
maturity: validated
created: 2026-04-25
updated: 2026-07-17
---

## Relations

- @sources/3-19-compliance-research.md — establishes the DCM Core Principles 3 & 4 baseline this concept extends; S7 anchors the March 2026 ANPRM as the regulatory shift
- @sources/cftc-anprm-prediction-markets-2026-03-16.md — Question 19 (defining "gaming" under CEA §5c(c)(5)(C)) is the statutory hinge of the preemption fight
- @sources/cftc-selig-house-ag-testimony-2026-04-16.md — Chairman's on-the-record confirmation of the AZ/CT/IL federal counter-suits is the documented inversion (federal government suing states, not just defending Kalshi)
- @sources/cftc-v-arizona-tro-liburdi-2026-04-10.md — first federal-court ruling in this cycle finding CFTC "likely to ultimately win" on preemption; rejected *Younger* abstention because US is a party
- @entities/platforms/kalshi.md — primary DCM in scope; role 3 (compliance leverage point) thesis depends on preemption holding
- @entities/platforms/polymarket.md — on-chain platform also subject to the gaming-definition outcome
- @sources/substack-rss-wublock-2026-07-11-weekly-project-updates-bonkdao-suffers-governanc.md — K158 FCM margin application watch
- @sources/substack-rss-event-horizon-2026-07-10-its-states-vs-prediction-markets-not-casinos-vs.md — K158 NCLGS: states as primary opponent vs CFTC exclusive jurisdiction
- @concepts/ip-sale-readiness.md — the IP-sale defensibility story for any Kalshi-touching architecture is binary on the preemption outcome

## Raw Concept

The concept page that synthesizes the **swap-vs-wager structural dispute** that emerged across Feb 25 → Apr 25 2026: the question of whether prediction-market event contracts traded on a CFTC-Designated Contract Market (DCM) fall under federal CFTC exclusive jurisdiction (CEA §2(a)(1)(A) "swap" definition) or remain subject to state gambling licensing (where the contract depends on the outcome of a sporting event).

Synthesizes from: the CFTC ANPRM (`@sources/cftc-anprm-prediction-markets-2026-03-16.md`), Selig's House Ag testimony (`@sources/cftc-selig-house-ag-testimony-2026-04-16.md`), Liburdi's TRO (`@sources/cftc-v-arizona-tro-liburdi-2026-04-10.md`), and the broader compliance-research baseline at `@sources/3-19-compliance-research.md`. Brief-level synthesis at `briefs/2026-04-25_post-kalshi-advisory-regulatory-update.md`.

## Narrative

### The structural dispute

The federal-vs-state regulatory tension over prediction-market event contracts reduces to one statutory question: do contracts where the payoff depends on the outcome of a real-world event (sporting result, election outcome, weather print, macroeconomic release) fit the CEA's definition of *swap* — placing them under the CFTC's exclusive jurisdiction over Designated Contract Markets — or are they wagers subject to state gambling licensing?

**CFTC position** (per Liburdi's April 10 TRO order):
> "The Act grants the CFTC 'exclusive jurisdiction' over the regulation of 'swaps,' traded or executed on a Designated Contract Markets."

**Kalshi's framing** (per PBS / AP coverage 2026-04-14):
> "Kalshi's customers engage in 'swaps' between one another instead of betting against the 'house.'"

**State position** (NV, MA, MI, AZ AGs): when users wager on outcomes — particularly sporting outcomes — the contracts depend on the *outcome of sporting events*, not on the *type of "occurrence"-based event* contemplated under the CEA. State gambling licensing then applies regardless of the federal label.

### The statutory hinge — CEA §5c(c)(5)(C)

The CFTC's own ANPRM (`@sources/cftc-anprm-prediction-markets-2026-03-16.md`) concedes the open question via Question 19, which asks the public to define "gaming" under CEA §5c(c)(5)(C). That section is the public-interest review provision that lets the Commission prohibit an event contract if it falls into one of five enumerated categories: *gaming, terrorism, assassination, war, or activity unlawful under federal or state law*.

The structural tension this concedes:
- Defining "gaming" tightly → sports-event contracts survive on Kalshi (favorable to CFTC's exclusive-jurisdiction theory)
- Defining "gaming" broadly → sports-event contracts revert to state licensing (favorable to state AGs)

The MindCast AI public comment (2026-04-17) captures the strategic exposure even pro-CFTC commenters acknowledge:
> "deference vulnerabilities under *Loper Bright* that could undermine the Commission's preemption cases in the Ninth and Fourth Circuits"

### K158 — States as primary opponent (Event Horizon, NCLGS Jul 2026)

Industry coalition frames fight as **casinos vs prediction markets**; Event Horizon argues the durable conflict is **state police power vs CFTC exclusive jurisdiction** — bipartisan AG alignment, state C&D letters, Kalshi suing states, aligned state tax/licensing incentives with casinos without requiring conspiracy. Chairman Selig (Jul 10): CFTC will defend exclusive jurisdiction over commodity derivatives including PMs; challenges preempting states in court. Complements SDNY PI denial (K149): federal preemption is **contested on multiple fronts** simultaneously. Source: `@sources/substack-rss-event-horizon-2026-07-10-its-states-vs-prediction-markets-not-casinos-vs.md`.

### SDNY Kalshi PI denial (2026-07-08 — K149)

SDNY denied Kalshi's TRO/PI against **New York** gaming enforcement on sports event contracts — finding CEA does **not** preempt NY gambling laws as applied; presumption against preemption in traditional police-power field. Kalshi → **Second Circuit** appeal. Elevates **home-state enforcement risk** even where other circuits/TROs favored DCM jurisdiction. Source: `@sources/substack-rss-event-horizon-2026-07-08-kalshi-sdny-pi-denial.md`.

### Current circuit alignment (as of 2026-04-25)

**For CFTC / federal preemption:**
- **Third Circuit** (NJ): upheld Kalshi preliminary injunction 2-1 ~Apr 6-9 2026
- **D. Ariz.** (Liburdi TRO Apr 10, expired Apr 24): "CFTC likely to ultimately win"
- **Tennessee federal court** (per gamblinginsider 2026-04-03 split coverage): ruled for Kalshi

**For states / state regulation:**
- **NV state court** (Judge Jason Woodbury Mar 21 2026): TRO blocking Kalshi sports/election/entertainment event contracts; Nevada Gaming Control Board "reasonably likely to prevail"
- **MA state court** (earlier): ruled for state

**Sixth Circuit split** (per gamblinginsider 2026-04-03): "There is a split among federal courts, including a split in the Sixth Circuit." The intra-circuit split is the standard SCOTUS-cert trigger.

### Forward path

The state-action pattern clusters on **sports + election** event contracts. Pure economic-print contracts (CPI, Fed Funds rate, weather) have not drawn equivalent state attention. The CFTC's preemption theory is **strongest for the latter** and **weakest for sports** — which is precisely where the litigation pressure concentrates. The §5c(c)(5)(C) "gaming" definition that the ANPRM's Question 19 invites comment on will functionally decide which side of the split the contested product line lands on.

Likely resolution path:
1. **April 30 2026** — ANPRM comment deadline closes; comment record fixes public positions
2. **Q2-Q3 2026** — NV TRO → preliminary-injunction → trial; outcome here is leading indicator on whether sports-contract litigation can survive preemption
3. **Q3-Q4 2026** — Sixth Circuit en banc consideration or cert petitions; Supreme Court is the only forum that resolves federal-vs-state cleanly
4. **Open** — CFTC NPRM draft; whether the proposed rule narrows or broadens "gaming" under §5c(c)(5)(C) determines whether sports contracts survive in the rulemaking pipeline alongside the litigation pipeline

### Architectural significance for Cemini

The compliance-leverage thesis at `@entities/platforms/kalshi.md` role 3 — that Kalshi DCM-status is *"structurally cleaner for an IP-sale-to-institutional-buyer story than operating on an unregistered offshore exchange"* — depends on preemption holding. The thesis **strengthens** if SCOTUS sides with CFTC: the federal government has now demonstrated it will sue states to defend Kalshi's exclusive-jurisdiction status, which is the strongest possible compliance-leverage signal. The thesis **weakens** to a state-by-state cascade if SCOTUS sides with states: every state-residence-aware position-routing layer becomes a hard requirement on the API participant, not the DCM.

The structural risk is **binary, not gradient**. A pre-acquisition due-diligence process today should treat "preemption holds" vs "states win" as two materially different architectures. See `briefs/2026-04-25_post-kalshi-advisory-regulatory-update.md` §4 for the implications walk-through.

## Snippets

### S1 — Liburdi's preemption finding (paraphrased from secondary)
> "The Act grants the CFTC 'exclusive jurisdiction' over the regulation of 'swaps,' traded or executed on a Designated Contract Markets."
[Source: Liburdi TRO Apr 10 2026, as quoted in Gambling Insider, "CFTC Granted TRO To Halt Arizona's Criminal Prosecution of Kalshi" (2026-04-13), retrieved 2026-04-25; see `@sources/cftc-v-arizona-tro-liburdi-2026-04-10.md`]

### S2 — Selig's federal counter-suit confirmation (verbatim, prepared remarks)
> "filed complaints against Arizona, Connecticut, and Illinois seeking declaratory judgments affirming the CFTC's exclusive jurisdiction over event contracts"
[Source: Chairman Selig prepared remarks before House Committee on Agriculture, April 16 2026; see `@sources/cftc-selig-house-ag-testimony-2026-04-16.md`]

### S3 — MindCast AI deference-vulnerability concession (public comment)
> "deference vulnerabilities under *Loper Bright* that could undermine the Commission's preemption cases in the Ninth and Fourth Circuits"
[Source: MindCast AI, "CFTC RIN 3038-AF65" public comment to ANPRM (2026-04-17), retrieved 2026-04-25; cited in `@sources/cftc-anprm-prediction-markets-2026-03-16.md`]
