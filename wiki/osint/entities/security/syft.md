---
title: Syft
type: entity
tags: [security, sbom, supply-chain]
keywords: []
related:
  - sources/3-17-competition-research.md
  - sources/3-19-compliance-research.md
  - sources/3-19-ip-sale-research.md
  - sources/github-action-and-workflow-research.md
  - concepts/sbom.md
  - entities/security/cyclonedx.md
  - entities/security/trivy.md
maturity: validated
created: 2026-04-23
updated: 2026-04-24
---

## Relations

- @sources/3-17-competition-research.md
- @sources/3-19-compliance-research.md — automated SBOM generation cited as the cryptographic-proof artifact for the buyer's legal counsel; Track C audit found this is **not currently wired** (see @concepts/sbom.md retraction)
- @sources/3-19-ip-sale-research.md — auto-generated SBOMs cited as supply-chain-due-diligence accelerator (cuts buyer-side license-audit cycles)
- @sources/github-action-and-workflow-research.md
- @concepts/sbom.md
- @entities/security/cyclonedx.md
- @entities/security/trivy.md

## Raw Concept

Synthesized from 2 source(s) referencing this entity across the Cemini research corpus. Category: security.

## Narrative

Syft generates Software Bill of Materials (SBOM) artifacts from source
repos and container images. Cemini's CI pipeline produces CycloneDX-
format SBOMs with Syft on every build; the SBOM is attached as a
release artifact alongside the binary + signed attestation.

Documented motivation from the github-action-and-workflow research: an
institutional IP-sale buyer's supply-chain-security team will demand
SBOMs for every shipped artifact — having them auto-generated and
attested is a differentiator vs competing IP sellers who hand over
source tarballs without provenance.

## Snippets

*(populate as source stubs are deep-read.)*
