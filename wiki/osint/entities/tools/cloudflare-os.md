---
title: "cloudflare/cloudflare-os"
type: entity
tags: [tool, phase-0, k224, guruwatcher, watch]
keywords: [cloudflare-os, Workers, KV, R2, Access, edge agents]
related:
  - sources/eval-url-batch-agentic-edge-security-2026-08-05.md
  - entities/tools/cloudflare-temp-email.md
  - concepts/wiki-tooling-evaluation.md
  - concepts/cemini-license-posture.md
  - concepts/guruwatcher-newsletter-claim-ledger.md
maturity: draft
created: 2026-08-05
updated: 2026-08-05
wire_status: policy_wired
wire_target: .cursor/rules/osint-phase1-adopt-wires.mdc; ../GuruWatcher/.cursor/rules/guruwatcher-k224-phase1-wires.mdc
---

## Relations

- @sources/eval-url-batch-agentic-edge-security-2026-08-05.md
- @entities/tools/cloudflare-temp-email.md
- @concepts/wiki-tooling-evaluation.md
- @concepts/cemini-license-posture.md
- @concepts/guruwatcher-newsletter-claim-ledger.md

## Raw Concept

K224 eval URL 17 Watch (+ blog URL 16 Context). Repo: https://github.com/cloudflare/cloudflare-os

## Narrative

| Field | Value |
|-------|--------|
| **Repo** | https://github.com/cloudflare/cloudflare-os |
| **License** | **Apache-2.0** [CONFIRMED gh 2026-08-05] |
| **Verdict** | **Watch REFERENCE** → GuruWatcher (no migrate-now) |
| **Local** | `.local/adopts/cloudflare-os` (~22MB) |

Serverless agent workspace on Workers + KV/R2 + Access. Eval ROI is negative vs mature Node/Python pollers. Keep as edge-OS pattern museum; **do not** rewrite prod `watches.json` pollers onto V8 isolates this batch. Vendor lock-in is the business risk.
