---
title: "dshackle — Ethereum/Bitcoin JSON-RPC proxy (Extract REFERENCE)"
type: entity
tags: [tool, phase-0, k240, rpc, extract]
keywords: [dshackle, emeraldpay, Apache-2.0, JSON-RPC]
related:
  - sources/eval-github-repository-stack-2026-08-16.md
  - entities/tools/dsh-vision-toolkit.md
  - concepts/cemini-license-posture.md
  - concepts/llm-routing-deepseek-openrouter-failover.md
maturity: draft
created: 2026-08-17
updated: 2026-08-17
harness_verb: FILE
---

## Relations

- @sources/eval-github-repository-stack-2026-08-16.md — K240 eval (docx Integrate overridden)
- @entities/tools/dsh-vision-toolkit.md — same-batch dsh Extract
- @concepts/cemini-license-posture.md
- @concepts/llm-routing-deepseek-openrouter-failover.md — name collision: this is RPC, not DeepSeek Harness

## Raw Concept

What prompted this page: K240 GitHub-stack eval. Docx Integrate + Apache-2.0 verified via `gh api`. **Not** a cemini-prod deploy.

## Narrative

| Field | Value |
|-------|--------|
| Repo | https://github.com/emeraldpay/dshackle |
| License | **Apache-2.0** [CONFIRMED gh 2026-08-17] |
| Local | `.local/adopts/dshackle` (5.6MB, depth-1) |
| Verdict | **GO Extract REFERENCE** — PM/RPC pattern only |
| wire_status | `policy_wired` |

Fault-tolerant JSON-RPC proxy / load balancer for Ethereum and Bitcoin node fleets (EmeraldPay). Useful as a **reference** for how a production PM/Kalshi/HL adapter might sit behind a retrying RPC facade. **HITL before any cemini-prod proxy.** Do not auto-deploy onto cemini-prod. Dual-ID: OSINT K240 ≠ CCC K240 robotics solver.

## Snippets

> Verdict: GO Extract REFERENCE (not prod auto-deploy). [Source: `.local/reports/license-k240-2026-08-17.md`]
