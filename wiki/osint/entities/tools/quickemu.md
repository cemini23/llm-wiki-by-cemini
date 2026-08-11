---
title: "quickemu — fast VM provisioning for macOS/Linux/Windows"
type: entity
tags: [tool, k231, cyber, vm, virtualization]
keywords: [quickemu, QEMU, virtual machines, local-abliterated-lab, whitehat]
related:
  - sources/eval-project-evaluation-revenue-2026-08-11.md
  - concepts/wiki-tooling-evaluation.md
maturity: draft
created: 2026-08-11
updated: 2026-08-11
phase_0_verdict: "GO Extract 2026-08-11 (MIT, ~1MB)"
---

## Relations

- @sources/eval-project-evaluation-revenue-2026-08-11.md — GO Extract (cyber lab)
- @concepts/wiki-tooling-evaluation.md

## Raw Concept

- **Repo**: `github.com/quickemu-project/quickemu`
- **License**: MIT [gh api override]
- **Tier**: Extract
- **Primary fit**: local-abliterated-lab — rapid, reproducible target VMs
- **Phase-0**: `.local/adopts/quickemu` ~1MB

## Narrative

Streamlines creating optimised Windows/macOS/Linux VMs — rapid, reproducible isolated targets for authorized whitehat exploit testing across OS architectures. Combo with vulnerable-kernel PoC references (e.g. Kernel-Exploit-Dojo — itself NO-GO) for immediate testing.

**Constraints:** strict network isolation for all vulnerable VMs; authorized targets only; never repurposed for crimeware; no prod trading hosts.
