---
title: "Testimony of Chairman Michael S. Selig before the U.S. House Committee on Agriculture (April 16 2026)"
type: source
tags: [primary-doc, congressional-testimony, regulatory, cftc, prediction-markets, hyperliquid, cemini-internal]
clusters: [quant-finance]
related:
  - sources/3-19-compliance-research.md
  - sources/cftc-anprm-prediction-markets-2026-03-16.md
  - sources/cftc-v-arizona-tro-liburdi-2026-04-10.md
  - entities/platforms/kalshi.md
  - entities/platforms/polymarket.md
  - entities/platforms/hyperliquid.md
  - concepts/dcm-state-preemption.md
maturity: validated
read_status: skimmed
created: 2026-04-25
updated: 2026-04-25
---

## Relations

- @sources/3-19-compliance-research.md — Selig's prepared remarks reaffirm the DCM Core Principle enforcement posture this source documents
- @sources/cftc-anprm-prediction-markets-2026-03-16.md — Selig defended the ANPRM agenda and confirmed CFTC's view that the rulemaking is "grounded in a rational and coherent interpretation of the Commodity Exchange Act"
- @sources/cftc-v-arizona-tro-liburdi-2026-04-10.md — Selig confirmed on the public record that CFTC "filed complaints against Arizona, Connecticut, and Illinois seeking declaratory judgments affirming the CFTC's exclusive jurisdiction over event contracts"
- @entities/platforms/kalshi.md — primary DCM in subject of testimony; the trader-insider-trading line of questioning targeted Kalshi market access
- @entities/platforms/polymarket.md — adjacent platform; Trump Jr.'s advisory + investor relationships pressed by Rep. McGovern (D-MA)
- @entities/platforms/hyperliquid.md — Rep. Austin Scott (R-GA) pressed Selig on offshore perpetual-futures availability; Selig signaled plan to expand perp futures availability to retail
- @concepts/dcm-state-preemption.md — the AZ/CT/IL counter-suit confirmation moves preemption from "advocacy posture" to "documented federal litigation strategy"

## Raw Concept

- **Speaker**: Michael S. Selig, Chairman, U.S. Commodity Futures Trading Commission
- **Forum**: U.S. House of Representatives, Committee on Agriculture (full committee hearing)
- **Date**: April 16 2026
- **Type**: Prepared remarks + Q&A (multi-source coverage)
- **Location (primary, prepared remarks)**: https://www.cftc.gov/PressRoom/SpeechesTestimony/opaselig4
- **Location (Q&A coverage)**: PBS NewsHour / AP (https://www.pbs.org/newshour/politics/watch-live-cftc-chairman-testifies-before-house-panel-amid-scrutiny-of-prediction-markets); Yahoo Finance / Decrypt (https://finance.yahoo.com/markets/options/articles/cftc-chair-mike-selig-faces-165752773.html); Punchbowl Vault (https://punchbowl.news/article/vault/selig-house-hearing/); Prokopiev Law (https://www.prokopievlaw.com/post/cftc-chairman-selig-testifies-on-prediction-markets-crypto-and-enforcement-in-april-2026)
- **Retrieved**: 2026-04-25 via `mcp__exa__web_search_advanced_exa` (date-bounded April 2026)
- **Read status**: skimmed — prepared remarks corroborated; Q&A reconstructed from multi-source press coverage

## Narrative

Selig's first congressional testimony as CFTC Chairman following the March 2026 ANPRM and the federal preemption litigation. The hearing unfolded across two registers: the prepared remarks held the line on CFTC exclusive jurisdiction, while the Q&A absorbed bipartisan pressure on insider-trading proximity, sports-vs-event-contract conflation, war/death-related contracts, and offshore perpetual-futures availability.

### Prepared remarks — the official posture

Selig's opening framed enforcement, rulemaking, and federal preemption as a single coordinated agenda:

- **Enforcement absolutism**: *"to anyone who engages in fraud, manipulation, or insider trading in any of our markets: we will find you, and you will face the full force of the law."* Carries forward the framing of the Feb 25 2026 MNPI Enforcement Advisory ([CONFIRMED] in `@sources/3-19-compliance-research.md` S19).
- **Federal counter-suit confirmation**: Selig confirmed CFTC has *"filed complaints against Arizona, Connecticut, and Illinois seeking declaratory judgments affirming the CFTC's exclusive jurisdiction over event contracts."* This is the on-the-record confirmation that the federal government is actively suing states (as opposed to merely defending Kalshi suits) — the structural inversion `@concepts/dcm-state-preemption.md` documents.
- **Rulemaking defense**: defended the ANPRM (`@sources/cftc-anprm-prediction-markets-2026-03-16.md`) as proper process under the Commodity Exchange Act.

### Q&A — the credibility cost

Four lines of questioning under-cut the prepared frame; all bipartisan:

1. **Insider-trading proximity** (Rep. Jim McGovern, D-MA) — pressed Selig on a March 23 2026 oil-price wager (~$500M position) placed 15 minutes before President Trump's social-media post on Iran negotiations. Selig's response: *"I'm not going to play speculation games with you."* Background: President Trump's eldest son is an advisor to both Kalshi and Polymarket and an investor in the latter. The Trump family's Truth Social platform is launching a competing prediction market called *Truth Predict* — a political-economy fact that re-frames every CFTC enforcement decision.

2. **Sports-vs-event-contract conflation** (Rep. Gabe Vasquez, D-NM) — after Selig was unable to distinguish an unlabeled sports bet from an unlabeled event contract on the same baseball game, Vasquez: *"It's clear to me you can't tell [the difference], because the average consumer also can't tell."* This goes directly at the §5c(c)(5)(C) "gaming" definition the ANPRM's Question 19 invites public comment on (`@sources/cftc-anprm-prediction-markets-2026-03-16.md`).

3. **War/death-related contracts** (Rep. Jim Costa, D-CA) — *"I don't believe this is market innovation… that is profiting from tragedy."* Selig defended on statutory grounds — *"Our statute has a very broad definition of the term commodity and a very broad definition of the term swap"* — but did not commit to any prohibition under §5c(c)(5)(C)'s war/terrorism/assassination enumerated activities.

4. **Hyperliquid + offshore perpetual-futures spillover** (Rep. Austin Scott, R-GA) — pressed Selig on retail access to offshore perpetual futures. Selig signaled CFTC plans to expand perpetual-futures availability to retail (the path forward through CFTC-regulated venues). Adjacent to but outside the prediction-market frame; relevant for `@entities/platforms/hyperliquid.md` and the broader compliance posture for retail-derivatives venues.

### Architectural significance for Cemini

Selig's confirmation of the AZ/CT/IL counter-suits on the public record is the most architecturally relevant single fact — it demonstrates the CFTC will *sue states* to defend Kalshi's federal status, which is exactly what the compliance-leverage thesis at `@entities/platforms/kalshi.md` role 3 needs to credibly survive. The credibility cost of the Q&A (insider-trading proximity, sports-conflation, war-contracts) is real but does not unwind the prepared posture.

The Hyperliquid line of questioning is a parallel signal: the Commission's posture on retail perpetual-futures access is moving in a direction that *increases* the available venue surface, not decreases it. Note: Selig's "expand availability" signal is forward-looking commentary, not a regulatory action — it does not change the present-day non-US-retail status of the Hyperliquid platform.

## Snippets

*(populate from primary-source CFTC.gov transcript in subsequent deep-read pass; quotes used here are press-reconstructed from PBS / Yahoo-Decrypt / Punchbowl coverage and corroborated across two or more outlets)*
