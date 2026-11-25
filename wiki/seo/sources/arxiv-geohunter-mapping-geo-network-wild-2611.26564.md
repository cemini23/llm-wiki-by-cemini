---
title: "GEOHunter: mapping a paid GEO placement network in the wild"
type: source
related:
  - concepts/generative-engine-optimization.md
  - concepts/geo-paid-placement-networks.md
  - concepts/competitive-geo-citation-factors.md
  - concepts/ai-citation-sourcing-geo.md
  - concepts/evidence-ecosystem-geo.md
  - concepts/geo-visibility-measurement.md
  - concepts/citation-building.md
updated: 2026-11-22
read_status: read
maturity: draft
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | GEOHunter: Mapping a Generative Engine Optimization Network in the Wild |
| Authors | Sean Tang, Peiran Wang, Ying Li, Esha Shivakumar, Tao Meng, Yuan Tian (UCLA; Georgia Tech) |
| arXiv | 2611.26564 |
| Pages | 21 |
| File | `arxiv-2611.26564-geohunter-mapping-a-generative-engine-optimizati.pdf` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/seo/arxiv-2611.26564-geohunter-mapping-a-generative-engine-optimizati.pdf` |
| Retrieved | 2026-11-22 |
| Read status | read |

## Narrative

This paper measures one paid GEO operation from the accounts that write its articles to the AI answers that cite them. The authors study three Chinese user-generated-content (UGC) platforms: Bilibili, Baijiahao, and 360kuai. A GEO vendor writes promotional articles, called placements, and publishes them through accounts it controls. Assistants then retrieve these articles and use them in answers.

The paper builds two tools. GEOHunter follows client names to find networks of accounts that post together. GEOPRobe asks nine assistants buyer questions and traces each cited page back to the network at three levels of strictness.

**Scale.** The network has 1,985 analyzed accounts and 466,357 inferred placements [TENTATIVE]. The crawl accepted 3,755 network accounts across the three platforms. On Bilibili alone, 2,397 of 8,525 found accounts were accepted. The authors say all counts are lower bounds, because the crawl only reaches accounts whose titles carry a searched client name.

**Exposure.** Across nine generative engines from the US and China, 4.5% to 20% of retrievable cited pages come from the network, depending on how strictly the authors attribute them [TENTATIVE]. On eight of the nine engines, the network's clients are named in 52% of answers, against 68% for category leaders used as controls [TENTATIVE].

**One worked case.** Asked to rank road-bike brands, Baidu's Wenxin assistant described a "one king and four queens" hierarchy in two of three runs. The "king" brand is a network client. Its accounts published 1,185 placements naming it since June 2024. Wenxin's answers carry the brand or the hierarchy in 51 of their 98 references.

**Defense.** The authors state that content-level defenses are not sufficient against coordinated UGC placements. Account-level and platform-level signals are needed. This finding is the main SEO lesson: a single article reads as ordinary content, so detection must look at who publishes it and how they coordinate.

The paper maps the supply side of GEO manipulation. It does not measure Western engines, and it studies one observed network. The numbers are single-source claims from this paper.

## Snippets

> "Across nine generative engines from both the US and China, we find that 4.5% to 20% of retrievable cited pages are attributable to the network... On eight of these engines, its clients are named in 52% of answers, against 68% for category leaders." [Source: `arxiv-2611.26564-geohunter-mapping-a-generative-engine-optimizati.pdf` p.1 (arXiv 2611.26564), retrieved 2026-11-22]

> "Our work reveals content-level defenses as insufficient against coordinated UGC placements, where account-level and platform-level signals are necessary for proper defense." [Source: same file, p.1]
