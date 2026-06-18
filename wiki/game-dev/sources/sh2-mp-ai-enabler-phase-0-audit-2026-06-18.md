---
title: sh2_mp_ai_enabler Phase-0 audit — 2026-06-18
type: source
tags: [source, phase-0, stronghold-2, modding, audit]
keywords: [stronghold-2, multiplayer, ai, daerandin, gitlab]
related:
  - entities/tools/sh2-mp-ai-enabler.md
  - entities/tools/stronghold2-mp-ai-patch.md
  - concepts/stronghold-2-mod-ecosystem-shelf.md
  - sources/sh2-mod-ecosystem-scan-youtube-moddb-2026-06-18.md
read_status: read
source_type: operator-audit
source_url: https://gitlab.com/Daerandin/sh2_mp_ai_enabler
maturity: validated
created: 2026-06-18
updated: 2026-06-18
---

## Raw Concept

Phase-0 audit of **Daniel Jenssen / sh2_mp_ai_enabler** (v0.3.1) — primary maintained tool for **MP AI slot unlock** on Stronghold 2 Steam Edition.

## Narrative

### Method

Read GitLab README + release notes; compare to **Jpnock/Stronghold2-MP-AI** (MIT). Operator binary from [questforgaming.com/stronghold2](https://www.questforgaming.com/stronghold2/).

### Checks

| Gate | Result |
|------|--------|
| License | **None declared** on GitLab — reference/run only; prefer Jpnock for pattern-study if SPDX required |
| Maturity | v0.3.1 (Mar 2023); AUR package; Steam forum thread active |
| Mechanism | Launch before game; NOP 7 bytes on MP-AI UI guard + random-AI button guard; memory-only |
| Failure modes | Steam EXE update; host-only; forum reports AI may target host only in co-op |
| castle-sim fit | **NO-GO merge** — native Kingmaker+AI in greenfield |

### Steal value

| Extract | Skip |
|---------|------|
| Maintained operator path vs stale Jpnock signatures | Copying unlicensed binary into repo |
| Linux/Proton makefile build | Depending on patch for sim dev |
| Random-AI slot UX expectation | Expecting Firefly to add MP AI |

### Verdict

**CONDITIONAL-GO** — preferred retail research tool when bottle available. Install: gitignored `briefs/sh2-mp-ai-enabler-install.md`.

## Dead Ends

- Replacing Jpnock entity entirely — keep both; Jpnock remains MIT reference for signature methodology
