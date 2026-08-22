---
title: "TTWO / GTA 6 cashout thesis desk pull (2026-08-20)"
type: source
tags: [equity-research, options-flow, dark-pool, take-two, ttwo, gta6, leaks]
keywords: [TTWO, Take-Two, GTA 6, Unusual Whales, CyberLeek, Tom Henderson, DevEx, Shark Cards]
related:
  - entities/tickers/ttwo.md
  - concepts/gta6-convertible-currency-thesis.md
  - entities/companies/tiger-global-management.md
  - concepts/prediction-market-regulation-2026.md
  - sources/gemini-dr-ttwo-gta6-cashout-2026-08-20.md
  - concepts/grey-market-game-economies.md
maturity: draft
created: 2026-08-20
updated: 2026-08-20
read_status: deep-read
---

## Relations

- @entities/tickers/ttwo.md — ticker stub synthesized from this pull
- @concepts/gta6-convertible-currency-thesis.md — operator-positioned cashout thesis
- @entities/companies/tiger-global-management.md — Q1 2026 13F cut TTWO −65.75%
- @concepts/prediction-market-regulation-2026.md — CFTC event-contract bucket is the wrong rail for GTA$ FX
- @sources/gemini-dr-ttwo-gta6-cashout-2026-08-20.md — Gemini DR that answered this prompt; IR beats its FY26 table
- @concepts/grey-market-game-economies.md — unofficial CS2/Roblox analog Gemini omitted

## Raw Concept

- **Title**: Take-Two (NASDAQ:TTWO) — GTA 6 convertible-currency thesis; UW flow/darkpool weeks–months; FY26/FY27 financials; 2021–2026 leak archaeology
- **Author**: Cemini desk (operator-commissioned)
- **Type**: live market-data + IR + leak timeline + political-map pull
- **Location**: laptop brief `briefs/2026-08-20_ttwo-gemini-deep-research.md` (gitignored); UW JSON ephemeral `/tmp/ttwo_uw.json`; canvas `ttwo-gta6-cashout-thesis`
- **Retrieved**: 2026-08-20
- **Read-status**: deep-read

## Narrative

Desk session after operator GO to file a TTWO stub with **cashout as the thesis position** (not a hedged “unverified rumor only” page). Unusual Whales REST authenticated via tipdrop-scanner key on cemini-prod (`/opt/tipdrop-scanner/.env`). Darkpool path that works: `GET /darkpool/TTWO?date=YYYY-MM-DD` (default unfiltered call only returned the live session). Insider transaction route 404; `/insider/TTWO` is a person list, not Form 4s.

Tape 2026-08-20: TTWO **$237.55**, 52w **$187.63–$265.94**, mcap ~**$44.4B**, ~187.0M shares. UW next earnings **2026-11-05** (before GTA 6 **Nov 19**).

Synthesis on `@entities/tickers/ttwo.md` and `@concepts/gta6-convertible-currency-thesis.md`. Gemini Deep Research prompt (paste-ready) is in the laptop brief and in **Snippets** below.

## Snippets

### UW (2026-08-20, cemini-prod)

- info: `marketcap ≈ $44.32B`, `outstanding=186980443`, `avg30_volume≈2.13M`, `next_earnings_date=2026-11-05`, tag `gaming`, UW beta 0.67 (yfinance beta 0.98 — do not mix)
- IV rank 1y ~**48** (close $237.55, vol 0.409). Interpolated: 7d IV **49.6%** (81st pctile, ±4.8% implied); 30d **40.8%** (52nd); 90d **45.2%** (69th)
- Options volume 90d (2026-04-14 → 2026-08-20): call **803,986** vs put **427,297**, P/C **0.53**. Call premium field **$802.5M** vs put **$231.1M**. Monthly call vol: Apr 40k / May 197k / Jun 249k / Jul 138k / Aug MTD 180k
- Flow-alerts last ~10d (100 prints): 79 calls / 21 puts; call premium **$5.88M** vs put **$1.63M**. Largest: Sep 18 $210P **$778k** (5,538 contracts, 2026-08-12); Aug 28 $220C **$593k**; Nov 20 $260C **$367k** and $250C **$350k** (launch-week)
- Expiry OI (session): Sep 18 **83,485**; Aug 21 **52,957**; Jan 15 2027 **36,783**; Dec 18 **33,064**; Nov 20 **24,922**. Nov 20 max-pain **$210** vs spot ~$237 (call-lottery skew)
- Darkpool event days (`/darkpool/TTWO?date=` premium sum): May 21 (FY26 print) **$104.4M** / 344 prints; Jun 25 (GTA 6 preorder) **$83.4M** / 205; Aug 7 (Q1 FY27) **$66.2M** / 255; Aug 19 (CyberLeek day) **$55.9M** / 190; Jul 15 quiet **$43.0M** / 87. Leak day is **not** the largest print window
- Congress/PTR UW `ticker=TTWO`, 2024+: **16** trades, 10 sell / 6 buy. Names: Ro Khanna 5, Julia Letlow 3, Tony Wied 2. **Stephen I. Miran** (UW `member_type=executive`) **sold** $15k–$50k on **2025-06-09**. Lori Chavez-DeRemer also in the 2024+ list. This is personal-account flow, not a Take-Two appointment

### IR (Take-Two FY26 release, ended Mar 31 2026)

- Net Bookings **$6.72B** (+19%); GAAP revenue **$6.66B**; RCS **78%** of bookings; GAAP EBITDA **$760.6M**; GAAP net loss **$298.2M**. Share count ~185.6–186.5M
- FY27 outlook: Net Bookings **$8.0–$8.2B**; GAAP revenue **$7.9–$8.1B**; Non-GAAP EBITDA **$1,013–$1,070M**; OCF **>$1B**; capex ~$200M
- GTA 6 dated **November 19, 2026** (PS5 / Xbox Series). Zelnick: FY27 “new record levels… driven by” GTA VI

### Henderson 2021 (still live)

- [https://x.com/_tom_henderson_/status/1400498601353220097](https://x.com/_tom_henderson_/status/1400498601353220097) — Jun 3 2021: missions pay “bitcoin instead of cash”; stock market + crypto broker. Later walkback: fictional in-game crypto, later said **scrapped**, never a real-money rail. Wayback fetch of that URL 404/timeout this session — Dexerto/Coinspeaker still quote the original text

### Gemini Deep Research prompt (paste into Gemini)

```
You are doing Deep Research for a public-equity / OSINT desk. Date context: 20 Aug 2026. Ticker NASDAQ:TTWO (Take-Two Interactive). Rockstar Games is a wholly owned label. Grand Theft Auto VI is dated 19 Nov 2026 (PS5 / Xbox Series).

OPERATOR THESIS (treat as the hypothesis to stress-test, not as a fact): GTA 6 will ship an in-game currency that can be cashed out for real money — Roblox-like. The rumor is old (2021–2026), not a one-week Discord spike. Prefer creator-gated cashout (DevEx / UGC marketplace) as the legally shippable form, but also hunt player-wide convertibility. Do not flatten leaks into confirmed product. Cite primary URLs, archive.org / archive.ph snapshots, 8-K/10-K locators, and tweet IDs.

Run TWO workstreams. Return one report with Part A then Part B. Lead each claim with CONFIRMED / TENTATIVE / NO_EVIDENCE. If a page is 404, search Wayback CDX + archive.ph + Nitter / bibliogram mirrors before declaring it gone.

PART A — Leak archaeology (Rockstar scrubs; use Wayback)
1. Tom Henderson / Insider Gaming, 3 Jun 2021: tweet https://x.com/_tom_henderson_/status/1400498601353220097 and any follow-ups / grain-of-salt / later “scrapped” walkbacks (Notebookcheck, Insider Gaming). Capture original wording vs later wording.
2. Inverse Jul 2022 cycle; Rockstar Nov 2022 crypto/NFT ban on GTA V RP servers. What exactly was banned?
3. 2022 90-video GTA 6 leak (September): any currency / stock-market / crypto UI in the dumped footage? Primary: GTAForums, contemporaneous Polygon/Kotaku. Do not rely on 2026 recaps.
4. 2023–2025 P2E / $RSTAR / “GTA coin” social posts — grade source quality. Discard Watcher.Guru-class unless a primary exists.
5. FiveM / Cfx.re: Rockstar acquisition terms, creator marketplace payouts, current legal analog for official UGC cashout.
6. CyberLeek Discord 19 Aug 2026: “currency … traded to real life money (like Robux).” Same actor: Solana memecoin, paid poll. GamingCulture variant: cashout for creators on in-game social. Vice Cash / $VICE stills. HUD dual-money (wallet vs house) — Polygon said cash vs property, not cashout UI.
7. Take-Two litigation vs PlayerAuctions / grey-market GTA$ sellers. What does the complaint say the company is protecting?
8. GTA Online Shark Cards + current ToS: “no cash value” language. Search FY26 10-K accession 0001628280-26-037434 and latest GTA Online terms for virtual currency / redemption.
9. Roblox DevEx vs player Robux (players cannot cash purchased Robux). Diablo III RMAH postmortem as the open-loop caution.
10. Aug 27 2026 Netflix “Extended Look”: any official language on UGC, social, marketplace, currency. If not yet aired, list what would confirm vs kill the thesis.

PART B — TTWO financials, flow, political map
1. FY26 (ended 31 Mar 2026) and Q1 FY27 (ended 30 Jun 2026) from IR + 10-K/10-Q: Net Bookings, GAAP revenue, RCS %, GAAP vs Adj. EBITDA, GAAP NI, OCF, cash, short-term investments, long-term debt, revolving credit, Zynga notes 2026/2028, digital mix, GTA V units. Reconcile street vs company. Do not mix GAAP EBITDA with Adj.
2. FY27 guide $8.0–$8.2B bookings / EBITDA $1,013–$1,070M. How much is implied GTA 6 vs GTA Online vs 2K/Zynga? Zelnick “haven’t sold one unit yet” on not raising guide.
3. Options: Nov 20 2026 (day after launch) $290C / $300C volume and OI. 90-day call vs put volume. IV rank vs 7d event IV. Is flow launch-lottery or a cashout-specific strip?
4. Dark pool / block prints May–Aug 2026 around 21 May earnings, 25 Jun preorder, 7 Aug Q1, 19 Aug leak. Is leak-day unique?
5. 13F: Tiger Global Q1 2026 cut TTWO −65.75% (1.73% of book). Other large holders add/cut Q1–Q2 2026.
6. OpenSecrets org D000079035: 2024 cycle contributions, party split, lobbying $. ESA (Entertainment Software Association) lobbying + PAC C00439216. LDA filings. FEC.
7. Leadership: Strauss Zelnick (CBS chair history, ZMC, donation history), Karl Slatoff, Lainie Goldstein, Daniel Emerson, Rockstar principals (Houser status). Board bios vs Trump 2025–26 administration (family, donors, CFTC/Treasury/Commerce appointments). Rotating-door into ESA or Take-Two from CFTC/FinCEN/OCC. If none, say NO_EVIDENCE — do not invent nepotism.
8. Congressional / executive PTR in TTWO 2024–2026 (House, Senate, CEA, cabinet). Buys vs sells. Stephen Miran, Lori Chavez-DeRemer if present.
9. Regulatory: FinCEN FIN-2013-G001 CVC/MSB if GTA$ substitutes for money; state MTL; IRS virtual currency. Contrast with Kalshi/Polymarket CFTC DCMs and Hyperliquid US geo-block — those do NOT repeal money-transmitter rules.
10. Product incentive test: why Shark Cards die if players can farm and sell GTA$; why DevEx-style creator payouts (player spend → Rockstar → KYC creator) preserve RCS.

Deliverable:
- 1-page verdict: what form of cashout is most likely to ship, with probability language tied to evidence (not vibes)
- Timeline table 2021→2026 with source URLs + archive snapshots
- Financial snapshot table with 10-K/8-K locators
- Political-map table: each name, role, donation/lobby/PTR, verdict (capture / noise / NO_EVIDENCE)
- Falsifiers: what Aug 27 look, launch ToS, and FY27 10-K would have to say to kill the thesis
- Open questions only Gemini could not close
```

## Dead Ends

- Laptop had **no** `UNUSUAL_WHALES_API_KEY`; pull required `ssh cemini-prod`
- `GET /stock/TTWO/darkpool` 404; working path is `/darkpool/TTWO?date=`
- `/stock/TTWO/insider` and `/insider/TTWO/transactions` 404; `/insider/TTWO` is names only
- Wayback `web.archive.org/web/202106/https://twitter.com/_Tom_Henderson/status/1400441082090840067` 404 (wrong ID). Correct ID **1400498601353220097**. CDX fetch timed out
- OpenSecrets HTML blocked by Cloudflare bot-check this session; 2024 cycle **$912,663** contributions / **$0** lobbying from a prior Brave snippet — re-verify in Gemini DR
- yfinance “today” volume was a partial print (55k) during RTH; use median 90d **~1.95M** and UW avg30 **~2.13M**
