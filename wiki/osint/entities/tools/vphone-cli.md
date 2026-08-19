---
title: "vphone-cli — Apple Silicon iOS virt (MIT Extract REFERENCE)"
type: entity
tags: [tool, cyber, k242, mit, extract]
keywords: [vphone-cli, ios, virtualization, authorized-lab]
related:
  - sources/eval-local-agent-infra-2026-08-19.md
  - concepts/cemini-license-posture.md
  - concepts/local-abliterated-llm-pentest-stack.md
maturity: draft
created: 2026-08-19
updated: 2026-08-19
wire_status: policy_wired
wire_target: .cursor/rules/osint-phase1-adopt-wires.mdc
wire_note: Authorized lab REFERENCE; no AMFI/jailbreak writeup in wiki
---

## Relations

- @sources/eval-local-agent-infra-2026-08-19.md — K242 eval
- @concepts/cemini-license-posture.md
- @concepts/local-abliterated-llm-pentest-stack.md

## Raw Concept

K242 Phase-0 Extract REFERENCE. Clone `.local/adopts/vphone-cli` (~5.9MB). https://github.com/Lakr233/vphone-cli

## Narrative

| Field | Value |
|-------|--------|
| License | **MIT** [CONFIRMED gh 2026-08-19] |
| Local | `.local/adopts/vphone-cli` |
| Verdict | **Extract REFERENCE** |
| wire_status | `policy_wired` |

CLI around Apple Virtualization.Framework for virtual iOS guests on Apple Silicon. Useful as a **repeatable lab provisioning pattern** for authorized mobile assessment. Wiki does **not** document AMFI/SSV/Img4 bypasses or jailbreak recipes. Host SIP relaxation stays operator HITL.

## Snippets

> vphone-cli MIT Extract REFERENCE. No bypass writeup. [Source: `.local/reports/license-k242-2026-08-19.md`]
