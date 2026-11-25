---
title: Media crisis framing — what counts as a crisis depends on the outlet
type: concept
maturity: draft
related:
  - sources/substack-rss-klement-2026-11-23-how-the-media-treats-climate-change-and-other-cr.md
updated: 2026-11-25
---

## Raw Concept

Question this page answers: do newspapers agree on what a crisis is, and what does that mean for keyword-based news signals?

From Klement on Investing, 2026-11-23, reporting a Lancaster University study of ten UK newspapers from 2015 to 2024.

## Narrative

**The study.** Ten UK newspapers, five left-leaning and five right-leaning, analysed by the language they use on specific topics over nine years.

**The finding.** The papers disagree on what counts as a crisis. Left-leaning papers frame climate change as a climate crisis. Right-leaning papers frame the energy crisis and the cost-of-living crisis after the 2022 invasion of Ukraine. They also disagree on which damage matters: environmental and lifestyle damage on the left, infrastructure and business damage on the right. [Source: substack-rss-klement-2026-11-23-how-the-media-treats-climate-change-and-other-cr.md]

**Why it matters for research.** A word like "crisis" or "damage" is a framing choice, not a neutral count. A keyword-based risk or sentiment score built over a mixed newspaper corpus will inherit each outlet's politics and will drift when the corpus mix changes.

**Practical rule.** When a news-sentiment feed uses keyword counting, split the corpus by outlet lean, or use outlet-relative z-scores, before aggregating. An absolute count of "crisis" mentions across papers measures editorial choice as much as world events.

**Limits.** One study, one country, one nine-year window. The mapping from framing to reader belief is asserted, not measured here.

[OPEN QUESTION 2026-11-25] Whether outlet-relative normalisation removes the bias, or only shifts it, is untested.
