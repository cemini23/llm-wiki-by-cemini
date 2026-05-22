---
title: "osiris (OSINT dashboard)"
type: entity
tags: [tool, osint, dashboard, gis, threat-intelligence, reject, no-license, k51]
keywords: [osiris, simplifaisoul, palantir-alternative, real-time-osint, gdelt, webgl-map, global-intelligence-platform]
related:
  - sources/tool-eval-70urls-k57-2026-05-22.md
  - sources/multi-wiki-tool-eval-prompt-2026-05-18.md
  - concepts/cemini-license-posture.md
maturity: draft
created: 2026-05-18
updated: 2026-05-22
---

## Relations

- @sources/tool-eval-70urls-k57-2026-05-22.md — K57 eval incorrectly Adopt-tier; re-verification upholds Reject
- @sources/multi-wiki-tool-eval-prompt-2026-05-18.md — K51 multi-wiki tool-eval; Reject verdict, OSINT-primary fit
- @concepts/cemini-license-posture.md — no-license → reject; the IP-sale posture this verdict enforces

## Raw Concept

What prompted this page: K51 multi-wiki tool-eval (`@sources/multi-wiki-tool-eval-prompt-2026-05-18.md`) URL 30. Reject, OSINT-primary.

## Narrative

`simplifaisoul/osiris` — an open-source "Global Intelligence Platform", self-billed as a real-time OSINT dashboard and a direct **Palantir alternative**. Aggregates global intelligence feeds — aircraft, satellites, GDELT conflict events — onto a single 60fps WebGL map capable of rendering thousands of concurrent entities. 291★, active real-time commits. Stack: TypeScript, Next.js 16, MapLibre GL, Docker.

**Verdict: Reject — confirmed (again).** License checks 2026-05-18 and **2026-05-22**: GitHub API `license: null`, **no `LICENSE` / `COPYING` file**. K57 eval claimed **MIT** — **false positive** (same NO-LICENSE-FOUND retrieval gap as K53–K55). Stars ~1.8k (2026-05-22); still actively pushed.

Genuinely OSINT-on-target (Palantir-style dashboard: GDELT, aircraft, satellites, WebGL map) but unusable in IP-bearing surfaces until maintainer adds a permissive license. **Re-evaluate only on LICENSE file appearance.** `[CONFIRMED: unlicensed 2026-05-22]`
