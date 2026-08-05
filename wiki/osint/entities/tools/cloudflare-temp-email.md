---
title: "cloudflare_temp_email"
type: entity
tags: [entity, tool, k182, k224, extract, guruwatcher]
keywords: [cloudflare-temp-email, mit, k182, k224, IMAP, D1]
related:
  - sources/eval-url-batch-agentic-edge-security-2026-08-05.md
  - entities/tools/cloudflare-os.md
  - concepts/gpuology-genealogy-agent-kit.md
  - concepts/wiki-tooling-evaluation.md
  - concepts/guruwatcher-newsletter-claim-ledger.md
  - sources/eval-url-revenue-opportunity-analysis-2026-07-22.md
maturity: draft
created: 2026-07-22
updated: 2026-08-05
wire_status: policy_wired
wire_target: .cursor/rules/osint-phase1-adopt-wires.mdc; ../GuruWatcher/.cursor/rules/guruwatcher-k224-phase1-wires.mdc
---

## Relations

- @sources/eval-url-batch-agentic-edge-security-2026-08-05.md — K224 Extract upgrade
- @entities/tools/cloudflare-os.md
- @concepts/gpuology-genealogy-agent-kit.md — Atto temp-email candidate
- @concepts/wiki-tooling-evaluation.md
- @concepts/guruwatcher-newsletter-claim-ledger.md
- @sources/eval-url-revenue-opportunity-analysis-2026-07-22.md — K182 eval

## Raw Concept

Phase-0 K182 Integrate; **K224 Extract** refresh for GuruWatcher / pm-canary testing. Repo: https://github.com/dreamhunter2333/cloudflare_temp_email

## Narrative

| Field | Value |
|-------|-------|
| **License** | **MIT** [CONFIRMED gh 2026-08-05] |
| **Tier** | Extract (was Integrate K182) |
| **Local** | `.local/adopts/cloudflare-temp-email` (~7.5MB) |
| **Route** | GuruWatcher newsletter signup tests + PM canary; Atto portal verify patterns |

D1 + WASM parse + Python SMTP/IMAP proxy. **Alert-test / canary only** — never orders; never auto-rewrite `watches.json`. Deliverability / CF shared-IP blacklist is the business risk.
