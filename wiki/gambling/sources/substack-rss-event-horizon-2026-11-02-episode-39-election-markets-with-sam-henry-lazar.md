---
title: "Event Horizon #39 — election markets, Kalshi at $40bn, Polymarket's $3.9M refund"
type: source
tags: [source, newsletter, prediction-markets, kalshi, polymarket, regulation]
related:
  - "@osint-wiki/concepts/dcm-state-preemption.md"
  - sources/substack-rss-event-horizon-2026-11-03-five-thoughts-midterms-2026-11-03.md
maturity: draft
read_status: read
created: 2026-11-02
updated: 2026-11-02
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Episode 39: Election Markets With Sam Henry Lazarus Of The Council On Foreign Relations |
| Source | event-horizon (Next Event Horizon) |
| File | `substack-rss-event-horizon-2026-11-02-episode-39-election-markets-with-sam-henry-lazar.md` |
| Retrieved | 2026-11-02 |
| Published | 2026-11-02T12:03:41+00:00 |
| URL | https://nexteventhorizon.substack.com/p/episode-39-election-markets-with-cfr |
| Read status | read |

## Narrative

A weekly prediction-market briefing, published the day before the US midterms. The guest is Sam Henry Lazarus, a geoeconomics analyst at the Council on Foreign Relations, discussing his report on election betting. Daniel O'Boyle of InGame covers the news.

### The volume numbers

Saturday 31 October, Kalshi single-day volume was **$4.79 billion**. The mix:

| Segment | Share |
|---------|-------|
| Parlays | **73.9%** |
| Sports | 17.7% |
| Crypto | 7.6% |

Parlay volume rose week over week while single sports markets fell.

Seven-day trailing volume, designated contract markets only, ending 31 October:

| Venue | Volume |
|-------|--------|
| Kalshi | **$24.9bn** |
| DraftKings DKeX | $1.27bn |
| Novig | $826.6m |
| Underdog | $541m |
| Rothera | $344.1m |
| ProphetX | $64.9m |
| Polymarket US, Crypto.com/NADEX | not available |

Data is supplied by TickerTracker.

**The parlay share is the number to carry.** Three quarters of Kalshi's single-day volume on a Saturday is parlay product. That is the market CeminiParlays sits beside, and it frames any assumption that single-market sports is the main venue.

### Polymarket security incident

On 29 October, a **third-party vendor's performance-monitoring script** loaded on polymarket.com was compromised. The attacker replaced it with a script targeting users. For some users who had the site open during a short window that afternoon, it used the **active session** to sell positions and move funds out of the wallet. The vendor has confirmed the compromise publicly.

Polymarket returned **$3.9 million** to traders: $2.7 million plus $1.2 million to cover pause-related losses. Eligible wallets were identified from on-chain and trading data; no claims were required.

**Why this matters beyond the incident.** The attack path was a session-hijack through a trusted third-party script, not a contract or wallet-key compromise. Any venue that loads third-party JavaScript inherits that surface.

### Corporate and market structure

- **Kalshi is valued at $40 billion** per the show notes.
- The **Philadelphia 76ers** named Kalshi its Official Prediction Market Partner — the first NBA team to do such a deal, following the league-wide NBA partnership. The deal includes in-arena visibility, app and ticketing integrations, a fan platform with a $76,000 prize, and Kalshi funding a free-transit programme for one game.
- The brief notes the irony that LeBron James, a Polymarket partner, now plays for a Kalshi partner team.

### Utah — the live legal fight

Utah brought **criminal charges against Kalshi's co-founders**. The CFTC sought a preliminary injunction and temporary restraining order; a hearing was set for Friday.

Market response in Utah, per the brief: **Fanatics** will shut its "Markets" prediction product there. **DraftKings** removed all prediction-market contracts on sports, politics, and novelties. **FanDuel** ended those contracts.

**37 state attorneys general**, led in this filing by California's Rob Bonta, filed an amicus brief supporting Utah in *KalshiEX LLC v. Cox* at the Tenth Circuit. The argument is that federal preemption of state gambling law as applied to prediction markets is improper. It is the ninth time California has joined a multistate action against Kalshi and similar firms.

Kalshi's appeal asks the Tenth Circuit to find that the Commodity Exchange Act preempts Utah's constitutional prohibition on sports wagering as applied to its event contracts.

### The accuracy question

The brief assembles the pre-midterm scepticism:

- Several 2026 elections that polled as high as 90% for one candidate — Brazil, Serbia, Wisconsin — were upset by the underdog.
- On the next Israeli prime minister, Kalshi and Polymarket traders disagreed three days after polls closed.
- The author's framing: prediction markets call themselves "crystal balls" when right and "just probabilities" when wrong, and have moved toward the latter.
- Chuck Todd's analogy is quoted: "Would you get in an airplane that only had an 80% chance of landing?"
- Nate Silver is cited saying markets converge on the correct outcome faster than decision desks, and separately that markets create an incentive for fake pollsters to publish misleading data, move the market, and cash out.

### Regulation

Representatives Whitesides, Gallagher, Salinas, and Fong introduced the **No Bets on Wildfires Act**, banning wildfire-related contracts. Over $1 million had been wagered on Polymarket during the January 2025 Los Angeles fires.

The author's own view is that no one is offering wildfire markets now and the bill is a poor use of legislative time.

## Snippets

> "Kalshi volume: $4.79 billion · Parlays: 73.9% of volume · Sports: 17.7% of volume · Crypto: 7.6% of volume" [Source: https://nexteventhorizon.substack.com/p/episode-39-election-markets-with-cfr (retrieved 2026-11-02)]

> "A third-party vendor whose performance-monitoring script loaded on polymarket.com was compromised. The attacker replaced the script with one built to target Polymarket users… it used their active session to sell positions and move funds out of their wallet." — Polymarket statement, quoted in the brief [retrieved 2026-11-02]

> "In total, we're returning $3.9M to traders." — Polymarket statement [retrieved 2026-11-02]

> "Prediction markets have called themselves 'crystal balls' when they are right, and 'just probabilities' when they are wrong over the past two years." — the author [retrieved 2026-11-02]

## Dead Ends

- **Treating the $40bn Kalshi valuation as confirmed.** It is a show-note figure with no filing cited here.
- **Reading the 73.9% parlay share as a national figure.** It is one Saturday on one venue.
