---
title: sogen — userspace emulator (NO-GO)
type: entity
tags: [tool, emulator, gpl, k287, no-go]
keywords: [sogen, momo5502, userspace, emulator, gpl-2.0, k287]
related:
  - sources/eval-multi-repo-revenue-2026-10-09.md
maturity: draft
created: 2026-10-09
updated: 2026-10-09
phase_0_verdict: NO-GO
harness_verb: FILE
wire_status: wont_wire
wire_note: GPL-2.0 is not a permissive lab licence. No install. No lab brief.
---

## Relations

- @sources/eval-multi-repo-revenue-2026-10-09.md — K287 eval. Docx tier Extract. Phase-0 verdict NO-GO.

## Raw Concept

K287 Phase-0 on [momo5502/sogen](https://github.com/momo5502/sogen). Clone path `/tmp/k287-phase0/sogen`. No install.

## Narrative

sogen is a Windows and Linux userspace emulator. The docx scored it Extract for the authorized lab.

### Phase-0 (2026-10-09)

| Field | Value |
|-------|-------|
| Repo | `momo5502/sogen` |
| Stars | 3,659 |
| Last push | 2026-10-09 |
| gh api licence | **GPL-2.0** |
| File licence | GNU General Public License version 2 |
| Verdict | **NO-GO** |
| wire_status | `wont_wire` |

The docx left the licence blank. The API and the `LICENSE` file both say GPL-2.0. That licence is not permissive. A lab brief is allowed only when the licence is permissive. This row gets no lab brief.

### Failure mode

A GPL-2.0 emulator in the lab would put copyleft terms on lab code that links it. Do not clone it into the lab tree. The `/tmp` clone is the audit copy only.

## Snippets

> "GNU GENERAL PUBLIC LICENSE Version 2, June 1991" [Source: momo5502/sogen LICENSE, gh api 2026-10-09]
