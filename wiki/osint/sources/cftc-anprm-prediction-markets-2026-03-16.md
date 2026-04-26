---
title: "CFTC Advance Notice of Proposed Rulemaking — Prediction Markets (RIN 3038-AF65)"
type: source
tags: [primary-doc, federal-register, regulatory, cftc, prediction-markets, anprm, cemini-internal]
clusters: [quant-finance]
related:
  - sources/3-19-compliance-research.md
  - sources/cftc-selig-house-ag-testimony-2026-04-16.md
  - sources/cftc-v-arizona-tro-liburdi-2026-04-10.md
  - entities/platforms/kalshi.md
  - entities/platforms/polymarket.md
  - entities/data-sources/federal-register-api.md
  - concepts/dcm-state-preemption.md
maturity: validated
read_status: validated
created: 2026-04-25
updated: 2026-04-25
---

## Relations

- @sources/3-19-compliance-research.md — S7 references this same instrument as "March 2026 ANPRM"; this source page closes the matched-pair with full FR docket
- @sources/cftc-selig-house-ag-testimony-2026-04-16.md — Selig defended the ANPRM agenda before House Agriculture; companion advocacy artifact
- @sources/cftc-v-arizona-tro-liburdi-2026-04-10.md — TRO opinion cites the parallel ANPRM as evidence the regime is in active rulemaking
- @entities/platforms/kalshi.md — primary DCM in scope of the rulemaking
- @entities/platforms/polymarket.md — adjacent on-chain platform also subject to the rulemaking's "gaming" definition
- @entities/data-sources/federal-register-api.md — programmatic retrieval channel for this and adjacent FR docs; the wiki's standing path for any future RIN 3038-* lookup or comment-window monitoring
- @concepts/dcm-state-preemption.md — the ANPRM's Question 19 (CEA §5c(c)(5)(C) "gaming" scope) is the statutory hinge of the federal-vs-state preemption fight

## Raw Concept

- **Original title**: Prediction Markets — Advance Notice of Proposed Rulemaking
- **Issuing agency**: U.S. Commodity Futures Trading Commission (CFTC), under 17 CFR Chapter I
- **Identifiers**: RIN 3038-AF65; FR Doc 2026-05105; 91 FR 12516
- **Type**: Federal Register Advance Notice of Proposed Rulemaking (pre-rulemaking; no proposed rule text yet)
- **Issued**: March 12 2026 (CFTC Press Release 9194-26)
- **Federal-Register published**: March 16 2026
- **Comment deadline**: April 30 2026 (45-day window)
- **Companion instrument**: DMO Staff Letter 26-08 (Press Release 9193-26) issued same day
- **Location (primary)**: https://www.govinfo.gov/content/pkg/FR-2026-03-16/html/2026-05105.htm
- **Location (announcement)**: https://www.cftc.gov/PressRoom/PressReleases/9194-26
- **Retrieved**: 2026-04-25 via `mcp__exa__crawling_exa` (govinfo)
- **Read status**: validated — primary FR docket text crawled; ~30 numbered questions reviewed; statutory authority (CEA §5c(c)(5)(C)) verified against secondary coverage

## Narrative

The CFTC's first formal pre-rulemaking action on prediction markets in this regulatory cycle. The ANPRM operates as a structured public solicitation — ~30 numbered questions inviting comment on how the Commission should regulate event contracts going forward. No proposed rule text accompanies the ANPRM; that comes at the NPRM stage, conditional on the comment record.

**Statutory framework**: the document anchors regulatory authority in the Commodity Exchange Act, with particular weight on CEA Section 5c(c)(5)(C) — the public-interest review provision that lets the Commission prohibit an event contract if it falls into one of five enumerated categories: *gaming, terrorism, assassination, war, or activity unlawful under federal or state law*. Question 19 explicitly asks the public to define "gaming" under §5c(c)(5)(C). This is the statutory hinge: defining "gaming" tightly cedes sports-event contracts to Kalshi and similar DCMs; defining it broadly cedes them back to state gambling regulators. The state AGs litigating against Kalshi in NV/AZ/MI/MA all rely on the latter interpretation.

**Companion DMO Staff Letter 26-08**: issued the same day; near-term supervisory expectations for DCMs listing or overseeing event contracts. Carries operational weight independent of the ANPRM's eventual rule text — DCMs and their API participants are expected to comply with the Staff Letter's framing now, not after the comment window closes.

**Why this matters for the wiki**: `@sources/3-19-compliance-research.md` S7 already documents the existence of "the March 2026 ANPRM" as the regulatory shift triggering DCM Core Principles 3 & 4 enforcement. This page closes the matched-pair by anchoring the same instrument to its primary-source docket — moving the claim from [TENTATIVE] (deep-research source citing "March 2026 ANPRM") to [CONFIRMED] (FR Doc 2026-05105, 91 FR 12516, retrieved 2026-04-25 via Exa).

**Substantive comments filed during the window** (as of brief composition, 2026-04-25):
- **MindCast AI** (Apr 17 2026, https://www.mindcast-ai.com/p/cftc-rin-3038-af65) — Rule 40.11 amendment proposal targeting Question 19; argues for defining "gaming," restoring an economic-purpose screen, and requiring affirmative Commission approval for enumerated-activity contracts. Notes "deference vulnerabilities under *Loper Bright* that could undermine the Commission's preemption cases in the Ninth and Fourth Circuits" — a self-aware concession that even pro-CFTC commenters see exposure.

## Snippets

*(populate from crawled FR text in subsequent deep-read pass; primary-source corroboration already filed in the brief at `briefs/2026-04-25_post-kalshi-advisory-regulatory-update.md` §1)*
