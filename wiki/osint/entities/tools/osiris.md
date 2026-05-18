---
title: "osiris (OSINT dashboard)"
type: entity
tags: [tool, osint, dashboard, gis, threat-intelligence, reject, no-license, k51]
keywords: [osiris, simplifaisoul, palantir-alternative, real-time-osint, gdelt, webgl-map, global-intelligence-platform]
related:
  - sources/multi-wiki-tool-eval-prompt-2026-05-18.md
  - concepts/cemini-license-posture.md
maturity: draft
created: 2026-05-18
updated: 2026-05-18
---

## Relations

- @sources/multi-wiki-tool-eval-prompt-2026-05-18.md — K51 multi-wiki tool-eval; Reject verdict, OSINT-primary fit
- @concepts/cemini-license-posture.md — no-license → reject; the IP-sale posture this verdict enforces

## Raw Concept

What prompted this page: K51 multi-wiki tool-eval (`@sources/multi-wiki-tool-eval-prompt-2026-05-18.md`) URL 30. Reject, OSINT-primary.

## Narrative

`simplifaisoul/osiris` — an open-source "Global Intelligence Platform", self-billed as a real-time OSINT dashboard and a direct **Palantir alternative**. Aggregates global intelligence feeds — aircraft, satellites, GDELT conflict events — onto a single 60fps WebGL map capable of rendering thousands of concurrent entities. 291★, active real-time commits. Stack: TypeScript, Next.js 16, MapLibre GL, Docker.

**Verdict: Reject** — `NO LICENSE FOUND`. This is the most genuinely OSINT-on-target item in the K51 batch: a real-time geospatial intelligence dashboard is exactly the kind of visualization layer the OSINT workspace could use. The reject is purely an IP-contamination guard — an unlicensed front-end cannot touch the proprietary OSINT architecture. **Re-evaluate if an explicit permissive license appears**; this is a Defer-grade tool wearing a Reject only because of the missing `LICENSE`.

`[NEEDS VERIFICATION 2026-05-18]` — check the repository root for a license declaration before any further consideration.
