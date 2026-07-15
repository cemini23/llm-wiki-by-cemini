---
title: Stoplight Prism (OpenAPI mock + validate)
type: entity
tags: [tool, tipdrop, openapi, k168, extract]
keywords: [prism, OpenAPI, mock server, Apache-2.0]
related:
  - sources/eval-github-repo-revenue-evaluation-2026-07-15.md
  - entities/tools/fastify.md
  - concepts/wiki-tooling-evaluation.md
maturity: draft
created: 2026-07-15
updated: 2026-07-15
---

## Narrative

| Field | Value |
|-------|-------|
| **Repo** | [stoplightio/prism](https://github.com/stoplightio/prism) |
| **License** | Apache-2.0 (~5k★; ~14MB) |
| **Verdict** | **Extract** — TipDrop CI/local OpenAPI mock + request validation proxy |
| **Combo** | Pair with Fastify/OpenAPI specs (Watch) |

Decouple frontend/bot tests from live Discord/DB; catch contract breakages before MRR-facing deploys.
