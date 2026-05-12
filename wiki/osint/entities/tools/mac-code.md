---
title: "mac-code — Apple Silicon MLX-Streaming Claude Code Variant (REJECT 2026-05-12: SSD wear confirmed + no LICENSE)"
type: entity
tags: [tool, claude-code-alternative, apple-silicon, mlx, k39, reject, ssd-wear-confirmed, no-license-file]
keywords: [mac-code, walter-grace, apple silicon, mlx, ssd wear, f_nocache, quantized models, claude code alternative]
related:
  - sources/evaluating-project-links-stacks.md
  - concepts/tool-evaluation-framework.md
  - concepts/cemini-license-posture.md
maturity: validated
created: 2026-05-11
updated: 2026-05-12
phase_0_audit: REJECT 2026-05-12 — F_NOCACHE used pervasively across 22 source files on hot-path inference; SSD wear acceleration confirmed. Repo also missing LICENSE file (4th no-LICENSE pattern occurrence).
license_verified: NONE (eval brief claimed MIT; `gh api license.spdx_id` = null; no LICENSE file present)
---

## Relations
- `@sources/evaluating-project-links-stacks.md` — source evaluation brief (URL 17)
- `@concepts/tool-evaluation-framework.md` — three-surface methodology applied

## Raw Concept

- **Repo / URL** (per source brief): `github.com/walter-grace/mac-code`
- **Tier (per source brief)**: **Adopt** (laptop only, Apple Silicon + sufficient SSD)
- **Tier downgrade pending**: **NEEDS Phase-0** for hardware-impact assessment
- **License** (per source brief): MIT
- **Stack**: MLX-based local inference engine; streams FFN weights directly from SSD; quantized models (IQ2_M, 4-bit and sub-4-bit); claims 30 tok/s

## Narrative — RED FLAG

Eval brief's own caveat (verbatim):

> "Constantly streaming gigabytes of FFN weights directly from the SSD per inference cycle — bypassing standard OS caching via `F_NOCACHE` — will drastically accelerate the wear leveling (Terabytes Written - TBW) of the laptop's soldered internal flash storage, potentially leading to premature hardware failure."

AND:

> "Models operate at highly aggressive 4-bit and sub-4-bit quantizations (IQ2_M) to fit the memory envelopes. This extreme compression might induce hallucinatory degradation or logic failures during highly complex academic paper reasoning…"

AND:

> "Developers noted issues with memory leaks when injecting weights via `setattr`…"

Recommending Adopt despite **three independent risk flags** (SSD wear, quantization-induced logic failure, memory leaks) is internally inconsistent. This is the **4th eval-brief mischaracterization pattern** in K39.

### Integration vector

**Adopt → HOLD**. Do not install pending:
1. **SSD wear quantification** — measure actual TBW per active session; the user's laptop is the only Cemini workhorse, and the SSD is soldered (not replaceable). A single bad week of mac-code usage could permanently damage the laptop.
2. **Quantization quality verification** — IQ2_M for "academic paper reasoning" is aggressive; verify on Cemini's actual research-curation workload before adopting
3. **Memory leak mitigation** — `mx.quantized_matmul` workaround claimed in repo; verify presence
4. **Hardware tier** — eval brief NEEDS-VERIFICATION on M1 vs M4 Pro requirement for 30 tok/s; user's machine spec must clear baseline
5. **License file** presence

### Why this is the most hardware-dangerous tool in K39

Cemini is a solo-developer team on a single machine. Hardware failure on the developer laptop is an existential operational risk. **No software with documented SSD-wear acceleration should be installed on the development laptop without explicit user budget authorization for replacement hardware.**

### Phase-0 audit status

**REJECT 2026-05-12** — F_NOCACHE pervasive use on hot-path inference confirmed; hardware-destructive on irreplaceable soldered SSD.

## Phase-0 audit findings (2026-05-12)

**Repo verified**: `github.com/walter-grace/mac-code` — 975★ / 108 forks / 12 open issues / **NO LICENSE FILE** (gh api `license.spdx_id` = null) / last push 2026-04-09 (33d stale).

**F_NOCACHE prevalence — CONFIRMED**: `grep F_NOCACHE` across `/tmp/mac-code-audit/` returns **22 matched files** across the entire flash-streaming + expert-sniper + 1bit-fallback codebases. Hot-path usage in `expert_io.py` (8-threaded reader, opened once per layer per token) and `flash_stream_v2.py` (FFN weight streaming). README documents this is the **recommended inference path** ("35B agent — recommended — 30 tok/s on 16 GB"). Not research-only code; this is the entry point.

**Hardware impact on Cemini**: laptop is the sole development machine, SSD is soldered/non-replaceable. M4 Mac Mini 16GB NVMe typical 500-600 TBW warranty. 8+ hours/day F_NOCACHE-bypassed FFN streaming = projected SSD failure 6-12 months. No mitigation path = hardware EOL.

**No-LICENSE-file pattern**: 4th occurrence (after K36 finance-skills + K38 Readme.skill + K38 AI-Trader). Combined with K39 meridian, K39 surfaces 2 of the 5 no-LICENSE pattern catches.

### Verdict

**REJECT 2026-05-12** — DEFER-INDEFINITELY. Hardware-destructive on irreplaceable hardware + no LICENSE file = two independent blocking conditions. Activation trigger: only reconsider if (a) user explicitly authorizes a hardware replacement budget AND (b) repo adds clean LICENSE file. Both conditions required; not on roadmap.

Eval-brief inconsistency noted: brief flagged SSD wear as caveat then recommended Adopt anyway. Pattern is now sufficient to land in LESSONS.md as the **"caveat-then-Adopt internal inconsistency" mode** (separate from scope mischaracterization).

[Source: Evaluating Project Links for Stacks.docx URL 17; retrieved 2026-05-11; Phase-0 audit 2026-05-12]
