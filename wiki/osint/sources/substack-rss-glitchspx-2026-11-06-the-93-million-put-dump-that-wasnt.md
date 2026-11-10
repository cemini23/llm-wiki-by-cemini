---
title: "GlitchSPX — the $93 million put dump that was not a dump"
type: source
related:
  - concepts/k296-feeds-wave.md
  - concepts/options-flow-package-reading.md
  - concepts/tape-reading-order-flow-day-trading.md
  - concepts/xsp-vol-regime-gates.md
updated: 2026-11-10
---

## Raw Concept

| Field | Value |
|-------|--------|
| Title | The $93 Million Put "Dump" That Wasn't |
| Author | Glitch (Glitch SPX, Talon Weekly) |
| Type | newsletter, RSS |
| Location | `research to be indexed/substack-rss-glitchspx-2026-11-06-the-93-million-put-dump-that-wasnt.md` |
| Retrieved | 2026-11-06 |
| File | substack-rss-glitchspx-2026-11-06-the-93-million-put-dump-that-wasnt.md |
| Read status | read |

## Narrative

### The print

On Friday November 6 at **3:25:48 PM ET**, 77,555 SPY 740 puts traded, about **$93.2m**, 100% at the bid. Flow feeds reported a large bearish position being dumped. The reading was that someone gave up on downside protection, or turned bullish.

The tape shows three legs in the same exchange within five microseconds:

| Leg | Side | Contracts |
|---|---|---|
| SPY 740 put | sold | 77,555 |
| SPY 725 put | bought | 188,808 |
| SPY 710 put | sold | 111,253 |

**77,555 + 111,253 = 188,808.** The sizes add up, so the three prints are one negotiated package. The trader collected about **$5.5m** on the package. [Source: substack-rss-glitchspx-2026-11-06-the-93-million-put-dump-that-wasnt.md]

### Why the labels failed

A floor package sets **one price for the whole package**, then splits that price across the parts in any way that sums correctly. Each part can print at the bid, at the ask, in the middle, or outside the quotes.

Friday's split:

- 740 put at $12.00, **below** its $12.14 bid
- 710 put at $4.58, **above** its $4.57 ask
- 725 put at $7.34, mid

So most feeds reported three separate stories, and all three were wrong. The largest leg — the 725 purchase at $138.6m — was ignored because a mid-price print scores zero on "who was aggressive" screens. [Source: substack-rss-glitchspx-2026-11-06-the-93-million-put-dump-that-wasnt.md]

### The four trade types

Every option trade is a buy or a sell, and an open or a close. The bid/ask label answers only the first question. A real buy at the ask can be a buy-to-close.

The same desk did all four in the week:

- **Bought to open** the 740 puts on Monday at the ask. Open interest rose about 72,000 the next morning, which is the confirmation.
- **Sold to close** the 740 puts on Friday at the bid. Every feed called it a dump.
- **Most likely sold to open** the 710 puts on Friday. It printed above the ask, so every feed called it a buy.
- **Likely bought to close** about 22,250 of the 725 puts at the mid. Most feeds ignored it.

### The history

On Monday November 2 at 3:02:27 PM ET, the same 77,555 contracts of the SPY November 20 740 put traded in a floor package, swapped for 750 puts. Open interest confirmed the roll:

- 750 put open interest: **137,633** on Nov 2 → **88,721** on Nov 3
- 740 put open interest: **57,611** on Nov 2 → **129,312** on Nov 3

SPY was about $754.92. The 740 put cost about $6.76, so it was cheap insurance about 2% below spot.

The week then did the work. SPY rallied to about $769 on Wednesday, then fell from about $766 to about $733 on Thursday, a 4% day. On Friday, with SPY near $737.8, the desk sold the same puts at about $12.01. The put went from $6.76 to $12.01, **up 78%**. [Source: substack-rss-glitchspx-2026-11-06-the-93-million-put-dump-that-wasnt.md]

The pattern: the new insurance always sits about $13–15 below spot. That is a standing, scheduled hedge programme, not a directional bet.

### The desk's signature

The desk sizes trades as fixed slices of a base quantity of about **55,600 contracts**: 0.2x, 0.4x, 0.6x, 0.8x, 1x, 2x. The programme is visible across days, exchanges, and expiries, and runs at least from October 21.

### The four checks before calling a print "bought to open"

1. **Is it alone?** Look for other trades in the same second, same exchange, with sizes that add up, and check for a multi-leg tag.
2. **Was it urgent?** A sweep of several exchanges at the ask is different from a quiet mid print.
3. **Is it bigger than open interest?** More contracts traded than existed means at least part is new.
4. **Did next-morning open interest rise by about that size?** That is the only real confirmation that a position opened.

### The honest caveat

The author states the confidence split plainly. The package reading is high confidence. The side the desk is on is lower confidence. The test is Monday's open interest. If the 740 puts fall by about 77,000 and the 725 puts rise, the reading holds. If the opposite happens, the read was wrong. [Source: substack-rss-glitchspx-2026-11-06-the-93-million-put-dump-that-wasnt.md]

## Snippets

> "Most feeds showed only the first line, the '$93M put sale'. That line on its own looks dramatic. All three together tell a calm, ordinary story." [Source: substack-rss-glitchspx-2026-11-06-the-93-million-put-dump-that-wasnt.md]

> "On a package, the bid/ask label is just how the price was split, so it may not even be a buy." [Source: substack-rss-glitchspx-2026-11-06-the-93-million-put-dump-that-wasnt.md]

> "The flow that looks the scariest is often the most boring underneath: a professional moving their insurance." [Source: substack-rss-glitchspx-2026-11-06-the-93-million-put-dump-that-wasnt.md]

## Dead Ends

- **Reading a single large print as a signal.** The loudest leg is often one part of a package.
- **Using "at the ask" as a proxy for "bought to open".** It fails on packages, on price-improvement auctions, on stale quotes, and on trades done with stock.
- **Trusting a print with a missing multi-leg tag.** On Monday the tag arrived late and was dropped, so the feed showed a false $52m bearish purchase.
