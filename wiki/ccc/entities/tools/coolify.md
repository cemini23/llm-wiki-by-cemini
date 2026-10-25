---
title: Coolify — self-hosted PaaS (Context)
type: entity
tags: [tool, ccc]
keywords: [coolify, self-hosted paas, laravel, docker]
related:
  - @osint-wiki/sources/eval-multi-wiki-link-revenue-v10.9-2026-10-25.md
maturity: draft
created: 2026-10-25
updated: 2026-10-25
phase_0_verdict: CONTEXT
wire_status: none
wire_note: Wiki reference only. No install.
---

## Raw Concept

URL row of @osint-wiki/sources/eval-multi-wiki-link-revenue-v10.9-2026-10-25.md. Tier **Context** — reference only, no revenue path.

## Narrative

| Field | Value |
|-------|-------|
| **Repo** | https://github.com/coollabsio/coolify |
| **License** | Apache-2.0 |
| **Maturity** | 63.9k stars. PHP Laravel and Svelte, 363 service templates, built-in MCP server, Cloudflare Tunnel provisioning. |
| **Verdict** | CONTEXT |

Coolify is a mature self-hosted deployment dashboard. It duplicates what already runs: GuruWatcher on a 15-minute systemd timer on cemini-egress-fi, PM LP canary on `compose.polymarket.canary.yml`, and Atto on Stripe plus LicenseSeat.

The control plane needs 2 cores and 2 GB RAM before any workload runs. v4.4.7 and v4.5.0 recently patched several critical dependency CVEs (PHP2Shell, Sentinel, cloudflared certificate). Putting a web-facing PaaS dashboard beside `/opt/guru-watcher/` widens the attack perimeter for no revenue.

## Dead Ends

- Placing a PaaS control plane on cemini-egress-fi. Wider CVE surface, no revenue path.
