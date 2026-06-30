---
title: OpenIM Server — instant messaging backend (Go)
type: entity
tags: [entity, tool, messaging, infrastructure, k137]
keywords: [open-im-server, openimsdk, IM, webhooks, REST, Apache-2.0]
related:
  - sources/eval-multi-wiki-openclaw-ecosystem-2026-06-30.md
  - concepts/polymarket-bot-architecture.md
  - concepts/scatter-gather-topology.md
maturity: draft
created: 2026-06-30
updated: 2026-06-30
---

## Relations

- @sources/eval-multi-wiki-openclaw-ecosystem-2026-06-30.md — K137 Steal-from row

## Raw Concept

K137 eval surfaces [openimsdk/open-im-server](https://github.com/openimsdk/open-im-server) — mature Go IM stack with REST/webhooks (not OpenClaw-native; batched in ecosystem docx).

## Narrative

| Field | Value |
|-------|-------|
| **Repo** | `openimsdk/open-im-server` |
| **License** | **Apache-2.0** (`gh api` 2026-06-30) |
| **Stars / pushed** | ~16.5k★; pushed 2026-06-26 |
| **Verdict** | **Steal-from** — event-push + connection management patterns for bot transport layers |
| **Steal** | Webhook callback design, scalable connection mgmt — reference for PM/Kalshi alert fan-out (not Adopt wholesale) |

**Posture:** wiki-only steal; cluster RPC mapping to cemini containers `[NEEDS VERIFICATION 2026-06-30]`.

## Snippets

> Apache-2.0 Go IM server — REST API + webhooks for high-throughput business systems. [Source: eval docx URL 11; gh 2026-06-30]
