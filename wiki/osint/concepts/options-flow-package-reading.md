---
title: Options flow package reading — why the bid/ask label lies
type: concept
related:
  - concepts/k296-feeds-wave.md
  - sources/substack-rss-glitchspx-2026-11-06-the-93-million-put-dump-that-wasnt.md
  - concepts/tape-reading-order-flow-day-trading.md
  - concepts/xsp-vol-regime-gates.md
updated: 2026-11-10
---

## Raw Concept

How to read a large multi-leg options print without being fooled by the trade-side label. Prompted by the SPY November 6, 2026 package.

## Narrative

Most flow screens answer one question: **was the print at the bid or at the ask.** That answers buy or sell. It does not answer open or close, and it does not identify the initiator of a package.

### The four trade types

| | Opens | Closes |
|---|---|---|
| **Buy** | buy to open | buy to close |
| **Sell** | sell to open | sell to close |

A print at the ask can be a buy to close. A print at the bid can be a sell to close. Neither tells you about a new position.

### Why packages break the label

A floor package is agreed as **one price for the whole structure**. The floor then allocates that price across the legs in any way that sums correctly. Each leg can print at the bid, at the ask, in the middle, or outside the quotes.

The result is a false decomposition. In the November 6 SPY case, one three-leg package printed as three unrelated stories:

- the 740 put "sold at the bid" for $93m — read as protection being dumped;
- the 710 put "bought at the ask" for $51m — read as a crash bet;
- the 725 put "at the mid" for $139m — read as noise and skipped by most feeds.

The true structure was the opposite. The 725 put was the **purchase**, and it was more than twice the size of the loud leg. [Source: substack-rss-glitchspx-2026-11-06-the-93-million-put-dump-that-wasnt.md]

Four other cases break the label in the same way:

1. **Price-improvement auction.** The fill prints between the bid and the ask, so there is no side to read.
2. **Quote moved in the milliseconds before the print.** A trade "above the ask" may be above an ask that no longer exists.
3. **Traded with stock.** The option price is set with the equity leg, not on the screen.
4. **Missing or late multi-leg tag.** The feed may show one leg as a standalone print.

### The four checks

Before treating a large print as a new directional position:

1. **Is it alone?** Look for other trades in the same second, on the same exchange, with sizes that reconcile.
2. **Was it urgent?** A multi-exchange sweep at the ask differs from a quiet mid print.
3. **Is it larger than open interest?** More contracts than existed means at least part is new.
4. **Did next-morning open interest move by about that size?** This is the only confirmation that a position opened. It still does not say which side the initiator holds.

### Package arithmetic

Reconcile the sizes. In the November 6 case, 77,555 sold plus 111,253 sold equalled 188,808 bought. That identity, plus the five-microsecond timing and the same exchange, is what proves one package.

### The hedge-versus-bet test

A large put trade is either insurance or a directional bet. They look identical on a flow feed. The distinguishing signals:

- built from spreads and packages, not a single contract;
- the new strike sits a fixed distance below spot every time;
- the position is **re-hedged** after a move instead of closed;
- the programme pays through losing weeks without stopping;
- trades are floor-negotiated at a scheduled time in fixed sizes.

In the November 6 case, the desk rolled insurance from 750 to 740 on November 2 and from 740 to 725 on November 6, always about $13–15 below spot. That is risk management, not a view. [Source: substack-rss-glitchspx-2026-11-06-the-93-million-put-dump-that-wasnt.md]

### What it means for a retail flow bot

- Do not score a print by aggressor side alone. A mid-price print can be the largest and most informative leg.
- Require the next-morning open-interest change before emitting a signal.
- Separate **hedging flow** from **directional flow** in the output. A hedge tells you about someone's book, not about the next move.

## Snippets

> "On a package, the bid/ask label is just how the price was split, so it may not even be a buy." [Source: substack-rss-glitchspx-2026-11-06-the-93-million-put-dump-that-wasnt.md]

> "Only the next morning's open interest tells you whether anything opened." [Source: substack-rss-glitchspx-2026-11-06-the-93-million-put-dump-that-wasnt.md]

> "77,555 + 111,253 = 188,808. That's not a coincidence. It's one trade with three parts." [Source: substack-rss-glitchspx-2026-11-06-the-93-million-put-dump-that-wasnt.md]

## Dead Ends

- **Scoring trades by "aggressor side" only.** The largest leg of the November 6 package scored zero on that metric.
- **Using a single print as a signal.** It is often one leg of a package.
