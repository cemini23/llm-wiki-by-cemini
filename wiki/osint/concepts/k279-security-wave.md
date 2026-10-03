---
title: K279 Security Wave (Oct 2026)
type: concept
tags: [security, k279, infra, agents]
keywords: [k279, pace, teamcity, capability, no-poc]
related:
  - concepts/k278-security-wave.md
  - sources/arxiv-2610.01349-pace-2026-10-03.md
  - sources/substack-rss-secpro-2026-10-02-teamcity-2026-10-03.md
maturity: draft
created: 2026-10-03
updated: 2026-10-03
harness_verb: FILE
wire_status: policy_wired
---

## Relations

- @concepts/k278-security-wave.md
- @sources/arxiv-2610.01349-pace-2026-10-03.md
- @sources/substack-rss-secpro-2026-10-02-teamcity-2026-10-03.md

## Raw Concept

K279 cluster hub. Dual-ID **OSINT K279**. Prior @concepts/k278-security-wave.md.

## Narrative

Two items. One is a design result for our own gates; the other is an infrastructure lesson. **No PoC.**

### Admission review is not enforcement

PACE opens with a result that should change how we think about allowlists:

**A safe tool variant and a leaking variant can produce identical admission evidence.** If you only vet a tool before it runs, you cannot distinguish them. So a sound gate cannot relax call-time mediation just because the schema passed review.

Their answer is to mediate every call at the last enforceable boundary — confine paths, verify the effect of each call against the capabilities compiled from the request, and block before dispatch. Numbers: 0 of 30 adaptive-search attacks succeeded against it, versus 21 of 30 undefended, and all 157 boundary calls were blocked before dispatch. Utility cost at most 2.92 points.

The ablation names what does the work: **effect verification**, not ambient monitoring. And boundary adaptation is what keeps refusal from becoming indiscriminate.

The authors bound their own claim carefully — guarantees cover only the flows the schema exposes, and paraphrase, translation, and fragmentation sit outside it. Read that as the honest limit of any such gate.

### The infrastructure lesson

A CI/CD server flaw, fixed in two versions, exploited by ransomware groups. The reason it is ransomware-relevant: a build server holds trusted access to repositories, agents, credentials, artefacts, and deploy targets, so it is a path to everything downstream.

The step teams skip is **credential rotation**. Patching without rotating leaves the attacker's access intact, because the credentials are the actual prize.

That applies here. Our own runners are trusted automation hosts in the same class.

### Boundary

**No PoC. No exploit steps. No payloads. No procedure.** Defensive framing only. FILE.

**Cemini posture:** FILE. **0 product Integrate GO.**
