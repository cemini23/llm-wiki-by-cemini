---
title: "K291 gambling feeds — regulatory and market batch, week of 2026-10-14"
type: source
tags: [feeds, regulation, sportsbook, prediction-markets, k291]
keywords: [Michigan cease-and-desist, offshore operators, Matchbook Betdaq, sweepstakes ban, Seminole DraftKings, BetMGM]
related:
  - concepts/k291-gambling-wave.md
maturity: draft
read_status: read
created: 2026-10-14
updated: 2026-10-14
---

## Relations

- @concepts/k291-gambling-wave.md — K291 gambling wave hub

## Raw Concept

Type: RSS batch, 21 items
Feeds: Legal Sports Report, Legal Sports Betting, SBC News, RotoBaller, Sharp Football Analysis
Location: `research to be indexed/gambling/` (21 `rss-*` files)
Retrieved: 2026-10-14
Read status: read (5 items fetched in full; 16 at title level)

**Fetch note:** Exa MCP is not exposed in this session, and both WebFetch and curl were refused — the publishers serve a Cloudflare challenge. Bodies were retrieved with a headless browser instead. Five substantive items were read in full; the remainder are recorded at headline level and are marked below.

## Narrative

### Michigan sends cease-and-desist letters to 33 offshore operators

The **Michigan Gaming Control Board** issued C&Ds to **33 offshore operators** for offering online casino, sweepstakes-style games, and sports betting to state residents. Named recipients include **Lucky Charm Sweep, Regal Casino and Sportsbook, Basepoker, Exclusive Casino, and Genie Jackpot**.

The MGCB's argument is consumer protection, not tax: illegal sites do not honour the state's **self-exclusion** register. Executive Director **Henry Williams**: "Offshore sites don't respect it. They will take a deposit from someone who has asked for help, and the MGCB has no way to help that person get it back."

| Statistic cited (AGA) | Value |
|---|---|
| US wagering, legal + illegal | **$673.6 bn/year** |
| Illegal market growth since 2022 | **+22%** |
| Online bettors unaware a site was illegal | **70%** |

**Note the scope:** Michigan has also targeted unlicensed operators **beyond offshore sites, including prediction markets**.

### Matchbook acquires Betdaq

**Matchbook** (founded 2004, Alderney) has taken over **Betdaq** (founded 2000 by Dermot Desmond, Dublin). The UK's major betting exchanges drop to **four**: Betfair Exchange, Spreadex, Smarkets, Matchbook.

Matchbook ties the deal to **prediction-market growth driving renewed demand for peer-to-peer pricing**. It became the **first UK firm to launch a prediction markets platform in December 2025**, and in 2026 has scaled both prediction-market and B2B activity. CEO Ronan McDonagh frames the thesis as "bettors get a better deal when prices are made by a market rather than a margin".

### Sweepstakes bans advance in Pennsylvania and Wyoming

| State | Instrument | Detail |
|---|---|---|
| **Wyoming** | Draft `27LSO-0098` | Sent to the Legislature's Management Council ahead of the 2027 session. Classifies online casino and sweepstakes as **professional gambling** — already a felony, up to **3 years**. |
| **Pennsylvania** | **HB 2801** | Fines sweepstakes operators up to **$500,000 per violation**. Session ends 30 Nov; bills do not carry over. |

The Wyoming draft is notable for reaching **service providers**, not just players — geolocation, payment processing, server hosting, platform services, gaming content, data services, and advertising are all named.

### Seminole Tribe sues DraftKings and its CEO

The **Seminole Tribe of Florida** sued **DraftKings**, CEO **Jason Robins**, and subsidiary **GUS III LLC** in Broward County's 17th Judicial Circuit — a **72-page complaint**. It targets **Pick6** (launched in Florida January 2026) and a sports tab added June 2026, alleging unlawful gambling against the Tribe's **2021 compact exclusivity**.

Five counts, including a **RICO claim against Robins**, deceptive trade practices, unfair competition, and declaratory judgment. Relief sought: injunction, restitution, disgorgement — **no dollar figure stated**. DraftKings maintains the products comply with the federal **Commodity Exchange Act** and calls Pick6 "a peer-to-peer fantasy sports variant".

### BetMGM Q3 — EBITDA up 112%, users down 3%

| Measure | Value | Change |
|---|---|---|
| Adjusted EBITDA | $41m → **$86m** | **+112%** |
| Monthly active users | **878,000** | **−3%** YoY |
| Net revenue | **$710m** | +7% YoY |
| Online sportsbook contribution | $202m → $216m | +7% |
| YTD net revenue | $2.01bn → **$2.11bn** | +5% |
| YTD iGaming | **$1.447bn** | +8% |

The MAU decline came **despite the 2026 World Cup knockout stages** falling in the period — the event most often cited as an acquisition tool. BetMGM calls the drop "as expected" and cites strong engagement. It expanded from Ontario into **Alberta**. [Source text states "Q3 2025"; filed verbatim. TENTATIVE.]

### Title-level items (not fetched)

| Item | Feed |
|---|---|
| Novibet "we are preparing something very big" sportsbook lead | SBC News |
| ANJ flags excessive risks of French sportsbooks as wagers hit record | SBC News |
| PointsBet expects H1 revenue drop with Alberta launch still pending | SBC News |
| First Bet debuts in the Sweden market | SBC News |
| Al Pennant odds +180 after sweep, Game 5 next | Legal Sports Betting |
| Fliff promo codes (×2) | Legal Sports Report |
| Fantasy football worksheets — Bills/Rams W5, NFL power rankings W6, Texans/Jaguars, Panthers/Eagles, Steelers/Buccaneers, Titans/Colts | Sharp Football |
| "Who should I start" W5 (×3) | RotoBaller |

**The nine fantasy worksheets and two promo-code pages are seasonal content with no durable finding.** They are archived but not written up.

## Snippets

> "The MGCB cited a study from the American Gaming Association that Americans wager $673.6 billion each year on both legal and illegal gambling platforms. The illegal market has grown 22% since 2022." [Source: legalsportsreport.com/281309 (retrieved 2026-10-14)]

> "Michigan has also targeted unlicensed operators beyond offshore sites, including prediction markets." [Source: legalsportsreport.com/281309 (retrieved 2026-10-14)]

> "exchanges and prediction markets are bringing peer-to-peer pricing to new audiences around the world, and this acquisition deepens the pool at the heart of everything we build." — Ronan McDonagh, Matchbook CEO [Source: sbcnews.co.uk (retrieved 2026-10-14)]

> "Operating an online casino or sweepstakes game for play by another person, or knowingly providing services for the purpose of operating, offering or promoting an online casino or sweepstakes game ... including geolocation services, payment processing, server hosting, platform services, gaming content, data services, promotion or advertising." [Source: legalsportsreport.com/281240, Wyoming draft 27LSO-0098 (retrieved 2026-10-14)]

> "The Tribe seeks an injunction, restitution, and disgorgement, with no dollar figure stated." [Source: legalsportsbetting.com (retrieved 2026-10-14)]

## Dead Ends

- **Fetching these feeds headlessly by default.** Cloudflare refused both WebFetch and curl; only a real browser session returned article bodies. Budget accordingly for gambling-domain feeds.
- **Reading the BetMGM user decline as a World Cup failure.** The article reports a 3% MAU fall *during* the World Cup knockout stages; the company calls it expected, and revenue rose 7%. Two metrics moved in opposite directions.
