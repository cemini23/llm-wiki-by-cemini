---
title: "haloy — zero-downtime Docker deploys on unmanaged VPS"
type: entity
tags: [tool, k231, devops, guruwatcher, pm, xsp]
keywords: [haloy, zero-downtime, Docker, reverse proxy, YAML, deploys]
related:
  - sources/eval-url-revenue-opportunity-2026-08-11.md
  - concepts/wiki-tooling-evaluation.md
  - sources/eval-project-evaluation-revenue-2026-08-11.md
maturity: draft
created: 2026-08-11
updated: 2026-08-11
phase_0_verdict: "GO Extract 2026-08-11 (MIT, ~8.6MB)"
---

## Relations

- @sources/eval-project-evaluation-revenue-2026-08-11.md

- @sources/eval-url-revenue-opportunity-2026-08-11.md — GO Extract (GW/xsp/pm)
- @concepts/wiki-tooling-evaluation.md

## Raw Concept

- **Repo**: `github.com/haloydev/haloy`
- **License**: MIT [gh api override]
- **Tier**: Extract
- **Primary fit**: Cemini prod bots — zero-downtime deployments (GuruWatcher timer, xsp modules, pm-canary)
- **Phase-0**: `.local/adopts/haloy` ~2.2MB

## Narrative

Go utility + custom reverse proxy for zero-downtime Docker deployments on unmanaged VPS (simple YAML config; handles image uploads and layer pushes over flaky connections; pre-deployment health checks; failed container log surfacing). Standardizes rollout of the 4 xsp-killer modules and GuruWatcher production timer without dropping webhooks during transition.

**Constraints:** **do not replace prod nginx without human GO**; latency overhead verification under GuruWatcher webhook payloads before production deploy; alert/execution separation unchanged.
