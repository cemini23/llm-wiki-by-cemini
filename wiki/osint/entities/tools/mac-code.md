---
title: "mac-code — Apple Silicon MLX-Streaming Claude Code Variant (RED-FLAG: SSD wear)"
type: entity
tags: [tool, claude-code-alternative, apple-silicon, mlx, k39, adopt-tier-flagged, phase-0-pending, ssd-wear-risk]
keywords: [mac-code, walter-grace, apple silicon, mlx, ssd wear, f_nocache, quantized models, claude code alternative]
related:
  - sources/evaluating-project-links-stacks.md
  - concepts/tool-evaluation-framework.md
  - concepts/cemini-license-posture.md
maturity: draft
created: 2026-05-11
updated: 2026-05-11
phase_0_audit: PENDING — eval brief itself flags SSD wear from F_NOCACHE bypass; hardware-degradation risk
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

**PENDING — DEFER UNTIL HARDWARE-BUDGET QUESTION ANSWERED**. Lower priority than Meridian / DeepSeek-TUI / Obscura — those are workflow/security risks, this is hardware.

[Source: Evaluating Project Links for Stacks.docx URL 17; retrieved 2026-05-11]
