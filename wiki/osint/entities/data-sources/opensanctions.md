---
title: OpenSanctions
type: entity
tags: [data-source, osint, compliance, sanctions, peps, due-diligence]
keywords: [opensanctions, ofac, sdn, eu-consolidated, hmt, un, peps, sanctions-screening]
related:
  - concepts/ip-sale-readiness.md
maturity: draft
created: 2026-04-25
updated: 2026-04-25
---

## Relations

- @concepts/ip-sale-readiness.md — primary use case: any acquirer due-diligence pass will run Cemini's commercial counterparties (data vendors, exchange relationships, customer LP-style relationships if any) through sanctions screening. Pre-running OpenSanctions on the same set surfaces issues before diligence does.

## Raw Concept

Added 2026-04-25 from the [public-apis](https://github.com/public-apis/public-apis) curated list. Compliance/sanctions data has been silent in the wiki to date; adding this gives an OSINT-quality source for both M&A due-diligence and any future entity-research thread that touches geopolitically exposed counterparties.

## Narrative

OpenSanctions aggregates international sanctions lists and politically
exposed persons (PEPs) data into a unified, queryable, openly
licensed dataset. Sources include:

- **OFAC SDN** (US Treasury Specially Designated Nationals)
- **EU Consolidated List** of financial sanctions
- **UK HMT Consolidated Sanctions List**
- **UN Security Council Consolidated List**
- **OFSI** (UK Office of Financial Sanctions Implementation)
- **National PEP datasets** from 50+ countries
- **Crime / interpol** wanted lists (where openly published)

**Cemini relevance** (two distinct angles):

1. **IP-sale-readiness compliance posture** — when the wiki's
   `@concepts/publishers-exclusion-apa.md` flags counterparty risk
   (Telethon channels, Polymarket exposure, etc.), an OpenSanctions
   screening pass is the systematic version of that intuition.
   Acquirer due-diligence will run this; pre-running it removes
   surprise.
2. **OSINT entity research** — for any future ticker / company
   research thread that touches geopolitically exposed names
   (defense, materials, payment rails into restricted jurisdictions),
   OpenSanctions gives the structural baseline rather than relying
   on news-search heuristics.

**Authentication**: none for the public API; commercial use of bulk
data requires a license agreement. The hosted API is free for
reasonable-volume queries.

**License**: data licensing varies by source — most underlying
sanctions lists are government works (public domain or CC0); the
aggregated dataset is published under [CC-BY 4.0 + Public Sector
Information licensing](https://www.opensanctions.org/licensing/).
Commercial-use clean if attribution is preserved.

**Integration angle (not yet wired)**: a one-shot screen against
Cemini's vendor list (Polygon, Finnhub, Hetzner, DeepSeek, etc.) plus
any counterparty in the IP-sale-readiness diligence package. Result
either surfaces nothing (clean baseline) or flags a hit that needs
mitigation before deal-room.

## Snippets

- API root: https://www.opensanctions.org/docs/api/
- Search: `GET https://api.opensanctions.org/search/default?q=ACME+Corp`
- Match (entity resolution): `POST https://api.opensanctions.org/match/default`
- Licensing: https://www.opensanctions.org/licensing/
