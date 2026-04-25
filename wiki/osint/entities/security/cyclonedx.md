---
title: CycloneDX
type: entity
tags: [security, sbom, standard]
keywords: []
related:
  - sources/3-17-competition-research.md
  - sources/3-19-compliance-research.md
  - sources/3-19-ip-sale-research.md
  - sources/github-action-and-workflow-research.md
  - concepts/sbom.md
  - entities/security/syft.md
maturity: validated
created: 2026-04-23
updated: 2026-04-24
---

## Relations

- @sources/3-17-competition-research.md
- @sources/3-19-compliance-research.md — clean dependency tree as cryptographic-proof artifact for buyer's legal counsel
- @sources/3-19-ip-sale-research.md — CycloneDX SBOMs cited as supply-chain-due-diligence accelerator; service + license-expression schema fields map cleanly to deal-killer ledger entries
- @sources/github-action-and-workflow-research.md
- @concepts/sbom.md
- @entities/security/syft.md

## Raw Concept

Synthesized from 2 source(s) referencing this entity across the Cemini research corpus. Category: security.

## Narrative

CycloneDX is the OWASP-maintained SBOM standard Cemini uses. Chosen
over SPDX for richer vulnerability- and service-descriptor schemas. The
Syft-produced SBOM is CycloneDX-formatted JSON, signed with cosign, and
published alongside every release.

The format choice is small but material in the IP-sale context: both
CycloneDX and SPDX are acceptable to most acquirers, but CycloneDX's
first-class service and license-expression fields map cleanly to the
deal-killer ledger (CCXT adapter licenses, Finnhub's commercial
license) without extra tooling.

## Snippets

*(populate as source stubs are deep-read.)*
