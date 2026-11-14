---
title: Card comps and grading option value — a worked evidence-discipline example
type: concept
related:
  - sources/substack-rss-outlier-weekly-2026-11-11-fifty-years-of-cards-ten-days-of-ledger.md
  - concepts/osint-inbox-wave-2026-11-14.md
updated: 2026-11-14
---

## Raw Concept

How do you price an asset with no liquid market? A 1,068-card collection is the test case. The answer is a stated negative, a same-name trap check, and an option model for grading.

Source: @sources/substack-rss-outlier-weekly-2026-11-11-fifty-years-of-cards-ten-days-of-ledger.md.

## Narrative

### Coverage is the first number

Of 1,068 rows:

| Status | Rows |
|---|---|
| Numeric comp | 387 (36%) |
| Stamped NO_EVIDENCE | 614 |
| Waiting on a first price | 67 |
| Notes with a usable reference figure | 128 |

Gross comp value is $9,947.13; net after eBay fees is $8,474.34. Fees take $1,472.79.

The lesson generalises past cards. On a thin market, the fraction of the universe with a price is the first statistic, and it is usually far smaller than an owner expects.

### The same-name trap

A comp is a claim about a different asset that shares a name. The worked example:

| Card | Page | Comp |
|---|---|---|
| Josh Caron, 2024 Bowman Draft Chrome Auto, Blue Refractor /150 | Base page | $2.25 |
| Same card | Blue Refractor page | $19.99 |

Same card, same day, **8.9x** apart. The base page was accurate; it answered a different question.

The worst case in the collection is 36x across 19 days for a card whose serial cannot be read. The row stays NO_EVIDENCE.

Three rules follow:

1. A serial or parallel card never matches an unnumbered base page.
2. When two sales of a supposed identical asset differ by more than 3x, take the median, not the latest.
3. When the tool cannot see the asset, the price cell stays empty.

### Grading as an option

The submission is an option position:

- premium = submission fee plus shipping
- payoff = the grade spread
- unknown = the grade

The model solves for the breakeven probability of the top grade:

```
p* = (cost − gain_lower) / (gain_top − gain_lower)
```

Decision rule: at or below 45% it is a submission; above 70% it is not; between, a human decides.

A raw 1955 Topps Jackie Robinson shows the shape. Guide values: raw about $455, PSA 8 about $10,424, PSA 10 about $278,160. The PSA 8 is 23x raw; the PSA 10 is 611x.

The author labels the PSA 10 figure a **guide, not a comp**, and says he does not believe it. That label is the method: the spread between the three figures is usable even when the top figure is not.

### Labels are not comparable

A "10" from a low-tier grader is not a PSA 10.

| Label | Card | Comp |
|---|---|---|
| GMA Gem MT 10 | 2019 Zion Williamson | $1.25 |
| GMA 10 | 2015 Aaron Judge | $7.61 |
| BCCG 10 Mint or Better | 1992 Mariano Rivera | $52.25 |

The tool therefore prices CSA and BCCG 9 slabs at PSA 8 and PSA 9 levels. A slab with a comp under $15 sells as it sits.

### The gate

The spend gate answers one question: may this row go to a human? It holds no dollar threshold and no grade cutoff, so it cannot approve on its own. It blocked 226 of 1,068 rows, mostly on a question mark in the year field or an unresolved photo citation.

### The cost-basis failure

Cost basis is known for **zero** cards. There is a note on every row and no purchase price on any of them. The author therefore refuses to say whether the collection is up or down.

That is the collector's reflex and also a research reflex: catalogue identity, ignore basis, then talk about returns.

### Why it belongs in this wiki

The method is the same one the wiki applies to claims:

| Card method | Wiki method |
|---|---|
| NO_EVIDENCE as a stated negative | `[NEEDS VERIFICATION]` with a date |
| A comp is a claim about a different card | A citation is a claim about a different context |
| Label a guide as a guide | Tag a single source `[TENTATIVE]` |
| A gate that never says yes | A lint that flags but does not decide |

The piece is not investment advice and names no recommendation.

## Snippets

> "The base page was not lying. It was answering a different question." [Source: substack-rss-outlier-weekly-2026-11-11-fifty-years-of-cards-ten-days-of-ledger.md]

> "The worst case is worse than 8.9." [Source: substack-rss-outlier-weekly-2026-11-11-fifty-years-of-cards-ten-days-of-ledger.md]
