---
title: Undici (Node.js HTTP/1.1 client)
type: entity
tags: [tool, xsp, node, k168, extract]
keywords: [undici, Node fetch, HTTP client, MIT]
related:
  - sources/eval-github-repo-revenue-evaluation-2026-07-15.md
  - concepts/xsp-lane-trading-framework.md
  - concepts/wiki-tooling-evaluation.md
maturity: draft
created: 2026-07-15
updated: 2026-07-15
---

## Narrative

| Field | Value |
|-------|-------|
| **Repo** | [nodejs/undici](https://github.com/nodejs/undici) |
| **License** | MIT (~7.6k★) |
| **Verdict** | **Extract** — dispatcher / pooling patterns for XSP REST; respect Node≥20 / undici v8 |
| **Risk** | Recent SSRF/cache CVEs — pin patched releases only |

Prefer undici over Axios where Node already includes it; no blind global dispatcher swaps on Robinhood lanes without soak.
