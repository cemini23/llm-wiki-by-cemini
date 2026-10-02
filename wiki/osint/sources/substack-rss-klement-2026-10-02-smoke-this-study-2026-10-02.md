---
title: "Klement — You can smoke this study (2026-10-02)"
type: source
tags: [source, k278, macro, methodology]
keywords: [k278, ftse, p-hacking, methodology, no-level]
related:
  - concepts/k278-ood-stub-wave.md
maturity: draft
created: 2026-10-02
updated: 2026-10-02
read_status: skimmed
---

## Relations

- @concepts/k278-ood-stub-wave.md

## Raw Concept

| File | `substack-rss-klement-2026-10-02-you-can-smoke-this-study.md` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/substack-rss-klement-2026-10-02-you-can-smoke-this-study.md` |
| Archive | egress-fi 2026-10-02 |
| URL | https://klementoninvesting.substack.com/p/you-can-smoke-this-study |
| Retrieved | 2026-10-02 |
| sha256 | `76fcd23f58b2c9b5a7577054f64ce775b3174e729f05e0df0c055f8b1babaa41` |
| Dual-ID | **OSINT K278** |

## Narrative

A critique post about a weak study, and the clearest methodology lesson in the wave.

The study, by a researcher at a Greek university, looked for a stock-market anomaly around the UK's No Smoking Day. The method compared FTSE 100 returns on the designated Wednesday against other Wednesdays.

The reported findings, as summarised:

| Claim | Detail |
|-------|--------|
| Return difference | Lower returns on No Smoking Wednesdays |
| Significance | Only at the 10% level |
| Structural break | Identified at 1991 |
| Split | No difference 1984 to 1991; a difference after |
| After adding three controls | Significance rose to 5% |

The controls added were the share of UK smokers, the share who quit, and the share who own shares directly.

Klement's framing is the point. A result that is significant only at the 10% level, then becomes significant at 5% **after** controls are added, and sits on a structural break chosen from the same data, is a garden-variety multiple-comparisons problem. The title says the reader can smoke this study.

The transferable rule: **a significance level chosen after the fact is not evidence.** Three moves appear here that should each stop a claim — a 10% threshold, a break date fitted to the data, and controls added until the result clears 5%.

This matters for our own work because the wiki stores numeric claims. A claim that arrives with a p-value needs the threshold and the break date recorded beside it. No level to arm. FILE only.
