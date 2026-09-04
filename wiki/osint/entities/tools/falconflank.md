---
title: FalconFlank — CrowdStrike Falcon privilege-escalation research (Extract-only)
type: entity
tags: [tool, k255, cyber, extract-only, mit]
keywords: [FalconFlank, CrowdStrike, Falcon, privilege-escalation, MSNightmare]
related:
  - concepts/k255-eval-github-wave.md
  - concepts/k255-cybersec-wave.md
maturity: draft
created: 2026-09-04
updated: 2026-09-04
phase_0_verdict: EXTRACT-ONLY
harness_verb: FILE
wire_note: NO-GO Integrate; cybersec-wiki awareness only; no PoC; do not execute clone binaries
---

## Relations

- @concepts/k255-eval-github-wave.md — K255 eval GitHub wave (Phase-0 spot-check)
- @concepts/k255-cybersec-wave.md — K255 cybersec EXTRACT-ONLY posture

## Raw Concept

| Field | Value |
|-------|-------|
| **Repo** | https://github.com/MSNightmare/FalconFlank |
| **License** | MIT `[CONFIRMED]` gh api SPDX 2026-09-04 + `LICENSE` MIT (copyright 2026 INFINITE NIGHTMARE) |
| **Local** | `.local/adopts/FalconFlank` (~7.3MB, shallow `--depth 1`) |
| **Stars** | 488 (2026-09-04) |
| **Last push** | 2026-09-03 (`702b574` Update README.md) |

K255 Phase-0 eval-docx / GitHub-wave spot-check. Offensive privilege-escalation research against CrowdStrike Falcon Sensor. Clone is REFERENCE for license and posture only.

## Narrative

**Pattern.** Visual Studio C++ research project. README claims a privilege-escalation against CrowdStrike Falcon Sensor on current Windows 11 / Windows Server 2025 builds. Tree includes source, a Visual Studio solution, and a prebuilt `x64/Release/` binary. **This page does not describe the technique, payloads, or reproduction steps.**

**Domain fit vs Cemini.** Cybersec-wiki awareness only. Not CeminiSuite, not trading, not Atto, not OSINT collection. Sibling EXTRACT-ONLY posture to @entities/tools/bloodbash.md (authorized-lab AD graphs; no PoC). Hook-update attack paper (arXiv:2609.03884) on the same K255 cyber/harness wave is also extract-only policy — no attack templates in the wiki (`cemini-invariants`).

**Failure-mode audit (offensive-exploit class).** Default EXTRACT-ONLY / NO-GO Integrate for this tool class, even when SPDX is MIT and stars are high.

| Check | Result |
|-------|--------|
| License | MIT `[CONFIRMED]` — does **not** clear Integrate for exploit research |
| Content | Offensive privilege-escalation research + prebuilt binary |
| Wiki policy | No PoC snippets, no reproduction, no DLL/macro/load-path detail |
| Binary | `x64/Release/FalconFlank.exe` + `.pdb` in the clone — **do not execute** |
| Eval override | Eval wave may list GitHub URLs as revenue/spot-check; **docx Integrate is wrong** |
| Routing | cybersec-wiki awareness brief only; no OSINT product wire |

**Verdict rationale.** **EXTRACT-ONLY** (2026-09-04). Equivalent to **NO-GO Integrate**. `harness_verb: FILE`. Keep the clone for license proof and a one-line awareness note. Do not copy source into the wiki. Do not scp to prod. Do not run the binary. Operator HITL if cybersec-wiki wants a stub that points here without technique text.

## Snippets

No exploit quotes. Clone README is offensive research; keep it off this page.

## Dead Ends

- Integrate, vendor, or compile the clone on any Cemini host.
- Paste reproduction steps, exclusion advice, or payload variants into wiki, briefs, or Discord.
- Treat star count (488) or MIT SPDX as a GO signal for exploit code.
