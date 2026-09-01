---
title: Grey-market game economies (CS2, Roblox, FIFA, GTAO)
type: concept
tags: [concept, virtual-currency, grey-market, cs2, roblox, gta-online]
keywords: [CSGO, CS2, skins, Steam Wallet, Skinport, CSFloat, BUFF163, DevEx, Robux, FIFA coins, PlayerAuctions, Shark Cards]
related:
  - concepts/gta6-convertible-currency-thesis.md
  - sources/gemini-dr-ttwo-gta6-cashout-2026-08-20.md
  - sources/ttwo-gta6-cashout-desk-2026-08-20.md
  - entities/tickers/ttwo.md
  - "@seo-wiki/concepts/ttwo-gta6-outlier-notes.md"
maturity: draft
created: 2026-08-20
updated: 2026-08-31
---

## Relations

- @gambling-wiki/briefs/2026-08-20_cs2-roblox-grey-cashout.md — CS2/Roblox grey cashout analog (OSINT keeps TTWO thesis)
- @concepts/gta6-convertible-currency-thesis.md — Model 4 (unofficial CS-style rail) on the GTA 6 thesis
- @seo-wiki/concepts/ttwo-gta6-outlier-notes.md — Outlier Weekly **LIVE** 2026-08-31: https://outlierweekly.substack.com/p/the-netflix-look-gave-gta-6-a-phone
- @sources/gemini-dr-ttwo-gta6-cashout-2026-08-20.md — Gemini omitted this analog
- @sources/ttwo-gta6-cashout-desk-2026-08-20.md — desk pull that named PlayerAuctions + Roblox DevEx
- @entities/tickers/ttwo.md — Take-Two sues the GTAO version of this rail

## Raw Concept

What this page answers: **people already turn in-game assets into real money** even when the publisher’s ToS says they cannot. Operator asked for Roblox, CS:GO/CS2, and peers as the analog if GTA 6 never ships an official PayPal button. Synthesized 2026-08-20 from SteamAnalyst/CSMarketCap/PriceEmpire recaps, Roblox Creator Hub DevEx docs, and Take-Two v. PlayerAuctions coverage.

## Narrative

There are **three different “I made money from a game” machines**. Mixing them is how the GTA 6 rumor stays confused.

| Machine | Who gets USD | Official? | Scarcity | Example |
| --- | --- | --- | --- | --- |
| **A. Creator DevEx** | KYC’d creators | Yes | N/A — take-rate on other players’ spend | Roblox DevEx; FiveM/Tebex |
| **B. Closed wallet + grey fiat rail** | Anyone who holds a **tradable item** | Publisher says no; market does it anyway | Item must be scarce + transferable | CS2 skins → Skinport/CSFloat/BUFF163 |
| **C. Infinite currency grey market** | Buyers of farmed/hacked balances | Publisher sues | Currency is not scarce | GTA$ / FIFA coins / Robux gift-code sellers |

Operator lived experience (A and B) is real. **GTA Online today is mostly C**, which is why Take-Two sues. A GTA 6 “CS:GO-style” outcome requires Rockstar to ship **tradable scarce objects** (unique cars, clothes, properties as inventory), not only GTA$. If they do, a Skinport analog appears whether Rockstar writes a cashout button or not.

### CS2 / CS:GO (Machine B)

Valve’s **Steam Community Market** lets you sell skins for Steam Wallet credit. Wallet funds **do not withdraw to a bank**. Third-party markets do: CSFloat (~2% seller fee), BUFF163 (~2.5%), Skinport (8% seller fee — 6% on high-value listings; 12% until ~Jul 2025; sellers cash out via **bank transfer through Adyen**, no PayPal payout), DMarket for faster fiat. SteamAnalyst: 22+ major third-party venues; Steam Market takes **15%**.

Inventory × last-price “market cap” estimates wander: **~$3.5–4B** (LIS-SKINS 2025) to **~$6–7B** (PriceEmpire / CSMarketCap into Aug 2026). `[TENTATIVE]` — not a 10-K. The **Oct 22 2025** knife/glove trade-up patch (five Coverts → knife/gloves) is the cautionary: knives roughly halved; recaps cite **~$1.5–2.4B** marked down in ~24–48 hours. Valve can reset prices with a single patch. They generally **do not sue Skinport** the way Take-Two sues PlayerAuctions.

That is the analog: **official closed loop + unofficial fiat on-ramp/off-ramp that everyone uses.**

### Roblox (Machine A + some C)

Official: only **Earned Robux** cash out via DevEx. Purchased Robux do not. Standard rate **$0.0038** per Earned Robux after 5 Sep 2025 10:00 PT (old **$0.0035** until that balance is drained). The **$0.0054** rate from **8 Jun 2026** is a **conditional** rate on qualifying US 18+ spend (newsroom Apr 2026), not the universal rate. Minimum often cited **30,000** Earned Robux. Roblox Creator Hub is the locator. Secondary recaps: **>$1B** creator payouts Mar 2024–Mar 2025; **~$1.5B** in 2025 — `[TENTATIVE]` until Roblox 10-K.

Grey: Robux resellers / account markets exist and violate ToS (Roblox has also targeted PlayerAuctions-class sites). That is Machine C, not DevEx.

### FIFA / EA FC and Fortnite

**Ultimate Team coins:** tradable inside FUT; EA bans real-money coin sites; U7BUY-class shops still list “FC 26 coins.” Same shape as GTA$ — infinite-ish currency, publisher enforcement, grey buy-side.

**Fortnite V-Bucks:** mostly closed-loop cosmetics. Save the World daily V-Bucks are a founder leftover, not a cashout market. No CS-scale third-party skin FX.

### GTA Online (Machine C, sued)

Take-Two v. PlayerAuctions, C.D. Cal. **2:25-cv-01880**, filed **4 Mar 2025**: modded accounts, currency drops, boosting; Take-Two says Shark Cards are the legitimate rail and grey GTA$ is IP + ToS breach. Polygon: PlayerAuctions fee **≥12.99%**; complaint claims tens of millions in marketplace take. This is **already** “everyone still does it” on the **buy GTA$ with USD** side. The **sell grinded GTA$ for fiat** side is weaker than CS2 because GTA$ is not a scarce drop like a Karambit — bots print it, so the publisher treats it as an exploit, not a collector market.

### What this implies for GTA 6

- If VI Online is Shark Cards + no item trade: grey market stays Machine C (sued, hacky, not a CS analog).
- If VI ships **tradable unique items** (or official UGC objects with inventory): Machine B appears. Operator thesis survives **without** an official cashout UI.
- If VI ships **creator marketplace + Tebex/DevEx**: Machine A, Gemini’s Model 2. Also real money, also not player-wide P2E.

Gemini DR graded official Model 3 at <1% and never named Machine B. That omission is the ingest delta.

## Snippets

- Roblox Creator Hub: standard DevEx **0.0038** per Earned Robux after 5 Sep 2025; pre-cutoff balances at **0.0035**. [Source: https://create.roblox.com/docs/production/monetization/developer-exchange (retrieved 2026-08-20)]
- SteamAnalyst: third-party CS2 seller fees **2% (CSFloat) to 15% (SkinBaron)** vs Steam Market **15%**. [Source: https://www.steamanalyst.com/guides/marketplaces (retrieved 2026-08-20)]
- PriceEmpire recap: CS2 tradable-item value **>$6B** Oct 2025, ~**$7B** mid-Aug 2026 after the Oct 2025 crash recovered. [Source: vgtimes / PriceEmpire recap (retrieved 2026-08-20)] `[TENTATIVE]`

## Dead Ends

- No audited “CS2 market cap” in Valve SEC filings — third-party scrapes only
- FIFA coin-site GMV not in EA 10-K
- PlayerAuctions case status (judgment vs pending) not pulled from PACER this session
