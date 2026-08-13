---
title: apkleaks — APK endpoint/secret scanner (JADX + regex JSON)
type: entity
tags: [entity, tool, mobile-security, apk, cyber, k235, extract]
keywords: [apkleaks, JADX, secret-scan, endpoints, regex-patterns, CVE-2021-21386]
related:
  - sources/deep-research-url-evaluation-2026-08-13.md
maturity: draft
created: 2026-08-13
updated: 2026-08-13
---

## Relations

- @sources/deep-research-url-evaluation-2026-08-13.md — K235 eval: Extract (local-abliterated-lab)

## Raw Concept

Repo `dwisiswant0/apkleaks` (6.1k★, last commit 2025-08-20). Decompiles APKs via JADX and applies customizable JSON regex patterns to detect hardcoded API keys, URIs, PII. Docx license claim: Apache-2.0 (**unverified this session** — no clone; Extract tier). History: CVE-2021-21386 OS command injection in package parsing (fixed).

## Narrative

**Verdict: Extract (local-abliterated-lab) — isolate APK decompilation.** Valid whitehat surface (authorized mobile assessments); the automated JADX + regex-JSON workflow replaces manual static-analysis sweeps. Constraints: decompile **untrusted APKs only inside the lab's isolation boundary** (malicious APK parsing history — CVE-2021-21386); verify JADX binary pathing handles obfuscated dex without crashing the wrapper (docx NEEDS VERIFICATION carried forward). Verify Apache-2.0 before code-level reuse.

[Source: dwisiswant0/apkleaks (retrieved 2026-08-13)]
