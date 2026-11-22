---
title: "GEO paid-placement networks — the supply side of generative-engine ranking"
type: concept
related:
  - sources/arxiv-geohunter-mapping-geo-network-wild-2611.26564.md
  - sources/arxiv-security-deep-research-agents-attack-surface-2611.20045.md
  - concepts/generative-engine-optimization.md
  - concepts/competitive-geo-citation-factors.md
  - concepts/ai-citation-sourcing-geo.md
  - concepts/evidence-ecosystem-geo.md
  - concepts/citation-building.md
updated: 2026-11-22
---

## Raw Concept

This page answers one question: who produces the content that generative engines cite, and how is that production organized? The source is @sources/arxiv-geohunter-mapping-geo-network-wild-2611.26564.md. The security survey @sources/arxiv-security-deep-research-agents-attack-surface-2611.20045.md supplies the threat framing.

## Narrative

GEO has two parts. First, a brand creates content that engines favor, such as ranked recommendation lists. Second, the brand places that content, in a coordinated way, on the platforms each engine reads. Many brands cannot do the second part alone, so agencies sell it as a service. This page describes the second part: the paid placement network.

A GEO paid-placement network is a set of accounts, often on user-generated-content (UGC) platforms, that a vendor controls. The vendor writes promotional articles for paying clients and publishes them through these accounts. Each article reads as an ordinary piece. The accounts do not signal that they work together.

**How a network is detected.** The GEOHunter study starts from articles that it ordered from a real vendor. It then follows client names across platforms. It accepts an account into the network when the account shows coordination: several clients, copied titles, or same-day bursts. In one measured network, coordination was the only visible signal. A content-level check on a single article is not enough.

**Why it works.** Generative engines retrieve pages and then synthesize an answer. The answer names some of the retrieved pages. A network that fills the retrieved set with its articles can therefore shape the answer. The GEOHunter study reports that 4.5% to 20% of retrievable cited pages came from one network, and that its clients were named in 52% of answers on eight of nine engines [TENTATIVE].

**Defense.** The evidence points to account-level and platform-level defenses. A provider can weight account diversity and posting history. A platform can detect coordinated accounts. A brand can audit who publishes the third-party pages that cite it. A content filter alone cannot separate a coordinated placement from a genuine article.

**Limits.** This model is measured on one network on three Chinese platforms. It does not show rates on Western engines, and the counts are lower bounds. The link between paid placement and answer share is correlational in the study, not a controlled experiment.

## Snippets

> "A single article reads as ordinary content, so detection must look at who publishes it and how they coordinate." — this wiki's summary of @sources/arxiv-geohunter-mapping-geo-network-wild-2611.26564.md. `[TENTATIVE]`
