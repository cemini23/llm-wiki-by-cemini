---
title: "Repository Revenue Evaluation — 20 rows (2026-10-02)"
type: source
tags: [source, k278, eval, tooling, license]
keywords: [k278, eval-docx, gh-api, spdx-mismatch, no-clone]
related:
  - concepts/k278-ood-stub-wave.md
maturity: draft
created: 2026-10-02
updated: 2026-10-02
read_status: skimmed
---

## Relations

- @concepts/k278-ood-stub-wave.md

## Raw Concept

| File | `Repository Revenue Evaluation Plan.docx` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/Repository Revenue Evaluation Plan.docx` |
| Archive | egress-fi 2026-10-02 |
| Retrieved | 2026-10-02 |
| Dual-ID | **OSINT K278** |
| sha256 | `103acbc5b856ec369601155387628b4a2bb00e1c7cff3fadc7501f629303c996` |
| Batch theme | Agent execution harnesses, marketing conversion, code knowledge graphs, sandbox runtimes, local dev tooling |

## Narrative

Twenty rows. Zero clones. **0 product Integrate GO.**

Every license below was checked with `gh api` on 2026-10-02. The docx claims are recorded beside them, because the eval makes four claims that do not survive a check.

### The docx claims that failed verification

| Repo | Docx claim | `gh api` 2026-10-02 |
|------|-----------|---------------------|
| sdcb/SimdPaddleOCR | "MIT (CLAIMED via dependency chain)" | **Apache-2.0** |
| mksglu/context-mode | "Elastic License 2.0 (ELv2)" | **NOASSERTION** |
| getsentry/sentry | "FSL-1.1-Apache-2.0" | **NOASSERTION** |
| cursor/plugins | "MIT / Apache-2.0 (CLAIMED)" | **null** |

Two more rows carry a null or NOASSERTION SPDX with no docx claim at all. **A null SPDX records the pattern only. No clone.**

### The twenty rows

| # | Repo | Tier | Docx license | `gh api` SPDX | Size KB | Stars |
|---|------|------|--------------|---------------|---------|-------|
| 1 | sdcb/SimdPaddleOCR | Context | MIT (claimed) | **Apache-2.0** | 131687 | 385 |
| 2 | JuliusBrussee/caveman | Extract | not found | Apache-2.0 | 14966 | 108854 |
| 3 | DietrichGebert/ponytail | Integrate | MIT | MIT | 2666 | 151160 |
| 4 | pbakaus/impeccable | Integrate | not found | Apache-2.0 | 379873 | 73974 |
| 5 | NVIDIA/OpenShell | Extract | Apache-2.0 | Apache-2.0 | 77669 | 14237 |
| 6 | heygen-com/hyperframes | Extract | not found | Apache-2.0 | 488380 | 55597 |
| 7 | coreyhaines31/marketingskills | Integrate | not found | MIT | 3417 | 52232 |
| 8 | mksglu/context-mode | Integrate | ELv2 | **NOASSERTION** | 31909 | 24915 |
| 9 | google/skills | Context | Apache-2.0 | Apache-2.0 | 4303 | 20604 |
| 10 | getsentry/sentry | Extract | FSL-1.1 | **NOASSERTION** | 952938 | 44921 |
| 11 | colbymchenry/codegraph | Integrate | not found | MIT | 35096 | 72825 |
| 12 | cursor/plugins | Extract | MIT/Apache | **null** | 10006 | 9399 |
| 13 | mvschwarz/openrig | Watch | not found | Apache-2.0 | 31654 | 4018 |
| 14 | Effect-TS/effect | Context | MIT | MIT | 136214 | 16395 |
| 15 | pablostanley/yoinks | Extract | MIT | MIT | 342 | 3219 |
| 16 | kentcdodds/kody | Watch | not found | NOASSERTION | 69638 | 718 |
| 17 | unxed/f4 | Context | BSD-3-Clause | BSD-3-Clause | 34752 | 235 |
| 18 | yetone/magpie | Integrate | MIT | MIT | 41259 | 4190 |
| 19 | mpfaffenberger/code_puppy | Extract | MIT | MIT | 16116 | 840 |
| 20 | gkjohnson/three-gpu-pathtracer | Context | MIT | MIT | 954910 | 1887 |

### Why no row is adopted

**SimdPaddleOCR** was the only row with an Atto angle. Its docx license claim is wrong, and the model is a Chinese PP-OCRv6 stack. Atto works on Italian civil records, and the project bans unverified cloud HTR. It is a name.

**Four size skips apply.** impeccable is 379 MB; hyperframes is 488 MB; sentry is 952 MB; three-gpu-pathtracer is 954 MB. Even a permissive license does not justify that footprint for a wiki tool.

**Two rows sit behind a copyleft-or-restricted class.** mksglu/context-mode is claimed as Elastic License 2.0, and getsentry/sentry is claimed as FSL. Neither SPDX resolves on `gh api`. Treat both as restricted until a human reads the actual license file.

**Everything else is a name or a pattern.** ponytail and impeccable and codegraph are CCC-harness names. marketingskills and hyperframes route to SEO and image-gen. openrig and kody are Watch. None is a product install.

### The durable lesson

This is the fourth wave where the eval docx overstated a license. The invariant stands: **never trust eval SPDX — `gh api` every adopt.** Four of twenty claims failed a one-command check.

**Cemini posture:** FILE. Zero clones. **0 product Integrate GO.** No install. No skill auto-evolve.
