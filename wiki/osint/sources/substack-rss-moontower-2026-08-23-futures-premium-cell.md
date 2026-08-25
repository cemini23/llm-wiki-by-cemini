---
title: Moontower Meta — futures premium cell
type: source
tags: [newsletter, k246, inbox-rss]
keywords: [substack, rss, k246]
related:
  - concepts/k246-newsletter-macro-wave.md
maturity: draft
created: 2026-08-25
updated: 2026-08-25
read_status: skimmed
---

## Relations
- @concepts/k246-newsletter-macro-wave.md
- _(none yet)_

## Raw Concept
- **title:** Moontower Meta — futures premium cell
- **type:** newsletter RSS ingest
- **location:** `cemini-egress-fi:/opt/cemini-bulk/research/osint/substack-rss-moontower-2026-08-23-futures-premium-cell.md`
- **retrieved:** 2026-08-25
- **URL:** https://moontowermeta.com/futures-premium-cell/
- **read-status:** skimmed

## Narrative
K246 newsletter ingest from inbox auto-fetch (2026-08-25).

## Snippets
Back in my SIG days, every trader had a cell on their spreadsheet showing the SPUs (the name for SPX futures back in the day; it’s derived from the September symbol) premium or discount to the “cash”.


  A little background


 The cash is the SPX index price based on its components’ spot prices. You can compute the index value from the stock bids, and that would be the “SPX cash bid”. You can do this for the offer as well. The average of the bid and offer is SPX mid-market.


 Futures contracts, based on no-arbitrage pricing, have a fair value based on what you gain or give up by owning the future instead of the cash basket. Since you save the interest on the cash it would cost to own the basket but forgo any dividends you would have received that offset the drop in the shares when they are paid the futures are valued as


 SPX + (interest – dividends)


 The interest and dividends are estimated from today until the futures’ expiry date.


 Assume:


 SPX cash mid market: 7,800


 RFR = 3.5%


 annual dividend yield =1.5%


 t = 1 year


 The 1-year future fair value is approximately 7800e (3.5% – 1.5%)*1  = 7957.57


 The basis between the future and the cash index was known as the EFP (“exchange for physical”). In our example, it equals 157.57


 If the future was trading 7977.57, we’d say “the futures are trading over”. In this case, it would be 20 points or about 25 bps rich as a percent of the cash index.


 This is an arbitrageable difference as a trading firm can sell
