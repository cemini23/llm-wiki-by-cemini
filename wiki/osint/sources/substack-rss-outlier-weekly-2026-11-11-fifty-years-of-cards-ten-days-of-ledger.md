---
title: "Outlier Weekly — fifty years of cards, ten days of ledger"
type: source
related:
  - concepts/card-comps-and-grading-option-value.md
  - concepts/osint-inbox-wave-2026-11-14.md
updated: 2026-11-14
---

## Raw Concept

| Field | Value |
|-------|--------|
| Title | Fifty Years of Cards. Ten Days of Ledger. |
| Author | Outlier Weekly |
| Type | newsletter, RSS; project log |
| URL | https://outlierweekly.substack.com/p/fifty-years-of-cards-ten-days-of |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/substack-rss-outlier-weekly-2026-11-11-fifty-years-of-cards-ten-days-of-ledger.md` |
| Retrieved | 2026-11-11 |
| Published | 2026-11-11 |
| Read status | read |

## Narrative

### The project

The author and his father catalogue a 50-year sports-card collection. The first ledger holds **1,068 rows**. The author builds the pricing pipeline; the father photographs cards daily.

### The coverage result

| Category | Rows |
|---|---|
| Rows with a numeric comp | 387 (36%) |
| Total comp value | $9,947.13 gross |
| Net after eBay fees (13.25% + $0.40) | $8,474.34 |
| Stamped NO_EVIDENCE | 614 |
| Waiting on a first price | 67 |
| Notes that yield a usable reference figure | 128, summing to $7,149.39 |

Fees take $1,472.79 before a single card ships.

The 614 NO_EVIDENCE rows are the point. The cell is not blank and not zero. It is a stated negative: a sale of that exact card was not found.

### The comp error that drove the design

Josh Caron, 2024 Bowman Draft Chrome Prospect Autograph, Blue Refractor, serial 071/150.

The first pass matched the base page and produced **$2.25**, the median of five real sales. The blue-refractor page shows **$19.99** for the most recent sale. Same card, same day, **8.9x** apart.

The base page was not lying. It answered a different question. A comp is a claim about a different card that shares a name.

Worst case in the collection: Reggie Crawford, 2024 Panini Impeccable, serial unreadable. Notes hold four candidate sales. The base page shows $17.99 on 25 September and $0.50 on 14 October; the Holo Silver page $3.80; the Holo Gold $9.75. That is **36x** across 19 days for a card that cannot be positively identified. The row stays NO_EVIDENCE.

### The rules the mistakes produced

- A serial Bowman, Topps, Chrome, Prizm, Select, Donruss or Gypsy Queen card does not match an unnumbered base page.
- When two sales of a supposed identical card differ by more than **3x**, the tool takes the median, not the latest. A 3x spread means two different cards sharing one name.
- When the tool cannot see the card, the comp cell stays empty. A bot that cannot verify a sale does not get to name a price.

### Grading as an option

The submission is an option: the fee is the premium and the grade spread is the payoff. The model returns the **breakeven PSA-10 probability**:

```
p* = (cost − lower_grade_gain) / (grade10_gain − lower_grade_gain)
```

Decision rule: 45% or below is a submission; above 70% is not; in between, a human decides.

Example: a raw 1955 Topps Jackie Robinson. Guide values: raw about $455, PSA 8 about $10,424, PSA 10 about $278,160. The PSA 8 is 23x raw; the PSA 10 is 611x. The author does not believe the $278,160 and labels it a guide, not a comp. Seven cards clear the bar, all vintage (Robinson, Berra, five Mantles); three are already in BVG slabs, so they are crossover decisions.

### Grade labels are not comparable

Sixteen graded cards show three tiers of "10":

| Label | Card | Comp |
|---|---|---|
| GMA Gem MT 10 | 2019 Zion Williamson | $1.25 |
| GMA 10 | 2015 Aaron Judge | $7.61 |
| BCCG 10 Mint or Better | 1992 Mariano Rivera | $52.25 |

The tool prices CSA and BCCG 9 slabs at PSA 8 / PSA 9, not PSA 9 / PSA 10. A slab with a comp under $15 sells as it sits.

### The spend gate

The gate answers one question: may this row go to a human? It never answers yes on its own. It holds no dollar threshold and no grade cutoff, so it cannot move either. It blocks **226 rows** today; the usual cause is a question mark in the year field or an unresolved photo citation.

### The cost basis

Of 1,068 cards, the cost basis is known for **zero**. There is a note on every card, many several hundred words, and nobody recorded what any card cost. The author therefore refuses to state whether the collection is up or down.

### Why it is filed here

The piece is a worked example of evidence discipline: a stated negative beats a plausible number, and a comp is a claim about a different asset. That is the same rule the wiki uses for citations and `[NEEDS VERIFICATION]` tags.

The forward call is logged: when real sale data replaces guide prices on the seven vintage candidates, at most three still clear the grading bar. Falsifier: five or more clear it. Resolve by 2027-05-11.

The piece is not investment advice and no card is a recommendation. See @concepts/card-comps-and-grading-option-value.md.

## Snippets

> "A comp is a claim about a different card that happens to share a name." [Source: substack-rss-outlier-weekly-2026-11-11-fifty-years-of-cards-ten-days-of-ledger.md]

> "Six hundred and fourteen cards now say NO_EVIDENCE in the price column. That is the literal text. Not blank, not zero, not a dash. A word that means: I looked, and I could not find a sale of this card." [Source: substack-rss-outlier-weekly-2026-11-11-fifty-years-of-cards-ten-days-of-ledger.md]

> "A grade you do not control. That is an option. The fee is the premium. The grade spread is the payoff." [Source: substack-rss-outlier-weekly-2026-11-11-fifty-years-of-cards-ten-days-of-ledger.md]
