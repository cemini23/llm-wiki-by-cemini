---
title: "Software Licensing Architecture Research (Ed25519 / entitlements)"
type: source
tags: [source, atto, licensing, cryptography, k191]
keywords: [Ed25519, offline license, entitlements, Keygen, machine-file]
related:
  - sources/atto-commercial-migration-plan-2026-07-23.md
  - concepts/atto-macos-gtm-gumroad.md
  - concepts/atto-local-first-threat-model.md
  - entities/tools/license-guard-rs.md
  - entities/tools/licenseseat.md
maturity: draft
read_status: read
created: 2026-07-23
updated: 2026-07-23
clusters: [k191-ingest]
---

## Relations

- @sources/atto-commercial-migration-plan-2026-07-23.md
- @concepts/atto-macos-gtm-gumroad.md
- @concepts/atto-local-first-threat-model.md
- @entities/tools/license-guard-rs.md
- @entities/tools/licenseseat.md

## Raw Concept

| Field | Value |
|-------|-------|
| **Filename** | `Software Licensing Architecture Research.docx` |
| **sha256** | `a42bd75fa2fdddc7515ca717bb8c24b9b0fb48b8e0c0ed3f1e4491019119d725` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/Software Licensing Architecture Research.docx` |

## Narrative

Architectural guide for asymmetric offline licensing: **Ed25519** sign on server / verify with embedded public key (defeats classic keygens); entitlement schemas (PostgreSQL); node-lock / machine-file patterns; soft-gate vs hard DRM. Cites `sassman/license-guard-rs` and commercial Keygen/LicenseSeat-class systems. **Atto steal:** implement offline machine-file verify in Tauri; keep private key only on MoR webhook path — never in client. Pairs with K191 migration plan LicenseSeat recommendation.

## Snippets

Works-cited includes license-guard-rs (Ed25519 offline) and Keyforge offline JWT notes.
