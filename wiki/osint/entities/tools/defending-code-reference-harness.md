---
title: anthropics/defending-code-reference-harness — sandboxed vuln-discovery pipeline
type: entity
tags: [entity, tool, cybersec, offensive-security, adopt, phase-0, k102]
keywords: [anthropic, asan, docker, sandbox, c-cpp, vulnerability-harness]
related:
  - sources/multi-wiki-tool-eval-50url-k102-2026-06-06.md
  - concepts/cemini-license-posture.md
maturity: validated
created: 2026-06-06
updated: 2026-06-06
phase_0_verdict: CONDITIONAL-GO
license_verified: Apache-2.0
repo: https://github.com/anthropics/defending-code-reference-harness
---

## Relations

- @concepts/cemini-license-posture.md — Apache-2.0 clean for steal/adopt

## Raw Concept

K102 Adopt (cybersec-primary); **Apache-2.0** in LICENSE file (~3.9k★). Eval tier correct; GitHub API returns `NOASSERTION` (metadata lag).

## Narrative

Anthropic reference pipeline: recon → vuln discovery → ASAN verification → report → patch for C/C++ targets. **vp-internal** Docker network + allowlist proxy — gold-standard pattern for running untrusted agent-generated exploit code off the laptop host.

**Phase-0 verdict: CONDITIONAL-GO** — laptop Docker only; steal `harness/prompts/` + network isolation pattern for cybersec wiki; **never** wire to `/opt/cemini` trading stack.

**Failure mode (agent harness class):** Docker-required; frontier-model cost in full pipeline; Mac/Linux via Docker Desktop.

## Snippets

> "Target image isolated on vp-internal network bound by strict allowlist proxy" [Source: defending-code README; K102 Phase-0 clone]
