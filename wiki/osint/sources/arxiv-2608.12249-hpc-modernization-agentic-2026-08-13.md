---
title: "Agentic Workflow for Legacy HPC Modernization (GAMESS F77→F2008)"
type: source
tags: [arxiv, k235, hpc, agentic-workflow, legacy-code, verification-oracle, ccc]
keywords: [2608.12249, GAMESS, Fortran, modernization, agentic, verification-oracle, human-gates]
related:
  - concepts/agentic-legacy-code-modernization.md
  - concepts/agent-harness-verification-bottleneck.md
maturity: draft
created: 2026-08-13
updated: 2026-08-13
read_status: skimmed
---

## Relations

- @concepts/agentic-legacy-code-modernization.md — synthesized pattern page
- @concepts/agent-harness-verification-bottleneck.md — same thesis as K234 Charity Majors lane

## Raw Concept

| Field | Value |
|-------|--------|
| arXiv | 2608.12249 (2026-08-12) |
| Authors | Shen, Sosonkina (Old Dominion); Xu, Gordon (Iowa State / Ames Lab) |
| sha256 | `3f7144bbad58ae8f3a721340d88e8dcfc06c2152f9a0dec0fc91c801550ff034` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2608.12249-an-agentic-workflow-for-legacy-hpc-modernization.pdf` |
| retrieved | 2026-08-13 |

## Narrative

Production-scale agentic conversion of the GAMESS two-electron-integral core (48-year-old codebase): 12 source files, **56,448 lines F77 → F2008**, fixed-form to free-form. Three prompt-specialized agent roles work under a **version-controlled specification the agents themselves authored and revised**, humans hold a small number of gates, and safety comes from an **exact verification oracle inherited from the domain** — chemistry output compared **bit-for-bit** against golden references (a difference in the 12th decimal counts as failure) plus GAMESS's own 51 standard + 49 Jenkins tests per file.

Results: all 12 files pass both check suites; aggregate line count -0.94% (agents neither padded nor over-compressed); subroutine count preserved exactly (mechanically checkable spec requirement); 11/12 arithmetically correct and 11/12 compiling clean on first attempt. Validation sweep: 7h29m total (~37 min/file), time scales with file count, not size.

**The escaped defect** (the lesson): GAMESS packs shell indices into a 64-bit word and writes it through a `DOUBLE PRECISION IX(*)` real-typed alias; the agent faithfully translated the declaration as `REAL(real64) :: IX(*)` — compiles clean, satisfies the style guide, locally accurate rendering, and wrong (high-order shifts no longer land). Survived agents + compiler; caught only by the bit-for-bit oracle. **Boundary of safe delegation = exactly where the domain oracle stops seeing.** Repos: `gms-bbg/test-validation`, `shenyuzhong/gamess-modernization-paper`.

Routing: CCC/wiki (agentic workflow pattern; human-gate + oracle structure maps to /route SIP Verify gate).

[Source: arXiv:2608.12249]

## Snippets

> "The boundary of safe delegation lies exactly where that oracle stops seeing." [Source: arXiv:2608.12249 p.1]

> "The original declaration had always contradicted the code semantics, so reproducing it faithfully is precisely [the failure]" [Source: arXiv:2608.12249 p.7-8]
