---
title: Trivy
type: entity
tags: [security, vulnerability-scan, containers]
keywords: []
related:
  - sources/3-19-compliance-research.md
  - sources/3-19-ip-sale-research.md
  - sources/github-action-and-workflow-research.md
  - entities/security/syft.md
  - entities/security/semgrep.md
maturity: validated
created: 2026-04-23
updated: 2026-04-24
---

## Relations

- @sources/3-19-compliance-research.md — CI/CD copyleft (GPL/AGPL) license-rejection mandate; primary OSS-contamination deal-killer mitigation
- @sources/3-19-ip-sale-research.md
- @sources/github-action-and-workflow-research.md
- @entities/security/syft.md
- @entities/security/semgrep.md

## Raw Concept

Synthesized from 2 source(s) referencing this entity across the Cemini research corpus. Category: security.

## Narrative

Trivy is Aqua Security's vulnerability scanner for container images,
IaC, and dependency manifests. Cemini's CI runs Trivy on every image
build + every Python requirements lock update; the CI gate fails on
HIGH or CRITICAL CVEs in Cemini's direct dependency graph (transitive
CVEs with no upstream fix are tracked but not blocked).

The IP-sale research frames Trivy output as a **continuous due-diligence
signal**: the acquirer inherits a living vulnerability posture rather
than a point-in-time snapshot, and the same tooling keeps running
post-transfer without rewiring.

## Snippets

*(populate as source stubs are deep-read.)*
