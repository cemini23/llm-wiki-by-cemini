---
title: GHunt — Google account enumeration framework
type: entity
tags: [entity, tool, osint, google, context, k235, cyber]
keywords: [GHunt, GAIA, Google-maps-reviews, OAuth-multilogin, Android-master-token]
related:
  - sources/deep-research-url-evaluation-2026-08-13.md
maturity: draft
created: 2026-08-13
updated: 2026-08-13
---

## Relations

- @sources/deep-research-url-evaluation-2026-08-13.md — K235 eval: Context (wiki/cyber methodology)

## Raw Concept

Repo `mxrch/GHunt` (19.3k★, last commit 2024-06-05). Maps target emails → Google footprint (Maps reviews, GAIA IDs, profile photos, connected services) via OAuth multilogin cookie generation from an Android master token; no Selenium. **License unverifiable**: docx claims AGPL-3.0, but repo has **no LICENSE file** (checked main + master); gh api NOASSERTION.

## Narrative

**Verdict: Context — wiki methodology only, no clone.** Value = state-of-the-art Google-accounts OSINT technique knowledge for the OSINT wiki + occasional authorized lab use; no revenue path (zero overlap with Atto's Italian civil-record focus). Constraints: aggressive use triggers account flagging/IP bans; Android-master-token auth stability post Google security changes unverified (docx NEEDS VERIFICATION carried forward). Authorized-scope testing only.

[Source: mxrch/GHunt (retrieved 2026-08-13)]
