---
title: "Pragmatic Engineer Pulse — Grok CLI repo upload incident"
type: source
tags: [source, rss, k172]
keywords: [k172]
related:
  - entities/tools/grok-build.md
  - entities/tools/grok-build-plugin-cc.md
  - concepts/coding-agent-substrate-steerability.md
  - concepts/wiki-tooling-evaluation.md
maturity: draft
read_status: read
created: 2026-07-17
updated: 2026-07-17
clusters: [k172-ingest]
---

## Raw Concept

| Field | Value |
|-------|-------|
| **sha256** | `08c20807ae7933ba8ebe47ea85db7078625b9791f0623864c96ddb203c4765d9` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/newsletter-rss-pragmatic-engineer-2026-07-16-the-pulse-groks-cli-caught-uploading-all-your-lo.md` |

## Narrative

Grok Build CLI (xAI) caught uploading entire local repos / home-dir content to cloud (GCS session traces), including .env/secrets risk. Contradicts local-first marketing. External coverage: wire analysis Jul 2026; server-side mitigation claimed ~Jul 13. **Hard pause** on secret-bearing trees until verified.
