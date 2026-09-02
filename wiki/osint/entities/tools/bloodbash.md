---
title: "BloodBash — offline AD graph (MIT Extract-only)"
type: entity
tags: [tool, cyber, k242, mit, extract-only]
keywords: [bloodbash, bloodhound, sharphound, authorized-lab]
related:
  - sources/eval-local-agent-infra-2026-08-19.md
  - concepts/cemini-license-posture.md
  - concepts/local-abliterated-llm-pentest-stack.md
maturity: draft
created: 2026-08-19
updated: 2026-08-19
harness_verb: FILE
wire_note: Authorized SharpHound JSON already collected; no PoC; not Integrate
---

## Relations

- @sources/eval-local-agent-infra-2026-08-19.md — K242 eval (docx Integrate **overridden**)
- @concepts/cemini-license-posture.md
- @concepts/local-abliterated-llm-pentest-stack.md — owned-lab only

## Raw Concept

K242 Phase-0 Extract-only. Clone `.local/adopts/BloodBash` (~104MB). https://github.com/SquidSec/BloodBash

## Narrative

| Field | Value |
|-------|--------|
| License | **MIT** [CONFIRMED gh 2026-08-19] |
| Local | `.local/adopts/BloodBash` |
| Verdict | **Extract-only** (docx Integrate wrong) |
| wire_status | `policy_wired` |

Offline NetworkX analysis of SharpHound / AzureHound JSON without Neo4j. **Authorized assessments only** on files the operator already collected from owned or contracted directories. No wiki PoC, no attack-path payloads, no third-party scopes. Not a prod or Atto runtime.

## Snippets

> BloodBash MIT Extract-only. No PoC. [Source: `.local/reports/license-k242-2026-08-19.md`]
