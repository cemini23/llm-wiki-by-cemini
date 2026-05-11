---
title: "Google Colab VS Code Extension"
type: entity
tags: [tool, vscode-extension, colab, gpu-remote, workflow, k38, phase-0-conditional-go-deferred-on-spend]
keywords: [google, colab, vscode, defer, three-surface-eval, gpu-quota, gcp-egress]
related:
  - sources/link-evaluation-brief-trading-stack.md
  - concepts/tool-evaluation-framework.md
  - concepts/cemini-license-posture.md
maturity: validated
created: 2026-05-11
updated: 2026-05-11
phase_0_audit: CONDITIONAL-GO 2026-05-11 — official Google extension, Apache-2.0; defer on cost + scoped-use-case until both triggers fire
adoption_status: DEFERRED 2026-05-11 (no spend now; data-egress + feature-parity gaps; user "no spend" posture)
---

## Relations
- `@sources/link-evaluation-brief-trading-stack.md` — source evaluation brief (URL 14)
- `@concepts/tool-evaluation-framework.md` — three-surface methodology applied
- `@concepts/cemini-license-posture.md` — license posture context

## Raw Concept

- **Repo / URL** [VERIFIED 2026-05-11]: Google-published VSCode Marketplace extension (announced 2025-11-13, productionized 2026-02). Apache-2.0 extension code; Colab service governed by Google Colab ToS.
- **Tier (per source brief)**: Adopt → **CONDITIONAL-GO 2026-05-11 → DEFERRED 2026-05-11** on user no-spend posture + data-egress posture
- **License** [VERIFIED 2026-05-11]: **Apache-2.0** (extension code; clean on Cemini license posture). Service-side: Google Colab ToS applies to runtime usage.
- **Phase-0 audit** [VERIFIED 2026-05-11]: First-party Google extension (not third-party wrapper). v1.0 ~6mo old. Mac-compatible. Feature-parity gaps vs web Colab: `userdata.get()` Secrets API unavailable, `drive.mount()` unsupported, telemetry on by default.

## Narrative

Official Google-published VSCode extension bridging local `.ipynb` notebooks to GCP-hosted Colab Jupyter runtimes. Code in VSCode → executed on Google's remote GPUs/TPUs. Free tier (~30 GPU-hours/week, T4/TPU-v5e only, 12hr session cap, non-guaranteed availability) → Colab Pro $9.99/mo → Pro+ $49.99/mo (A100).

### Eval-brief assessment

The K38 eval brief framing ("local IDE + remote GPU = adopt now") is **overly optimistic** for the workspace's current "no spend" posture but not fundamentally mischaracterized — the product genuinely is what it claims to be. The gaps are not mischaracterization, they are posture-misalignment + omitted feature-parity caveats:

1. **Cost-model bleed under iteration**: free tier quota (30 GPU-hrs/wk) exhausts in 2-3 days of active quant backtesting / LLM fine-tuning, surfacing $9.99-$49.99/mo paid-tier decision under brief framing that suggested "free GPU = unlimited."
2. **Data egress to GCP is structural**: code/notebooks transmit to Google Colab runtime. Proprietary algo logic, API keys, model weights visible in cells are logged by Colab telemetry. Not opt-out-able for a workflow tool whose entire value prop is remote execution.
3. **Credential anti-pattern in VSCode**: Colab Secrets API (`userdata.get()`) available in web Colab is **NOT** available in the VSCode extension. Workarounds (env-var upload widgets, copy-paste into notebook cells) leak credentials to git history and Colab telemetry.
4. **Incomplete feature parity**: no `drive.mount()` blocks Drive-versioned dataset workflows; users revert to web Colab, negating the adoption.

### Integration vector

**DEFERRED 2026-05-11**. Apache-2.0 license is clean; product is legitimate; vendor is first-party Google. But user posture is "no spend now," and the workspace currently has no scoped non-sensitive GPU-bound workload that fits the free-tier quota envelope. Existing local stack (Jupyter via codeboarding, Cursor, claude-mem) handles current CPU-bound iteration; Cemini-prod backtesting runs on Hetzner CPX21 not on the laptop. No current Cemini Adopt path.

### Risks

1. **Cost-model entrapment** (MEDIUM-HIGH) — adopting under "free GPU" framing without an explicit paid-tier decision tree leads to surprise spend when quota exhausts mid-iteration.
2. **Data egress + credential leak** (MEDIUM-HIGH) — proprietary trading algo / model weights / API keys in notebook cells = visible to GCP. Direct conflict with IP-sale-readiness posture if any proprietary Cemini logic touches Colab.
3. **Feature-parity gap** (LOW-MEDIUM) — VSCode extension is a degraded surface vs web Colab; workflows designed for one don't transfer cleanly to the other.

### Activation trigger (DEFER → GO)

Adopt only when **both** fire:
1. **Spend budget cleared** — user explicitly clears $50-200/mo Colab Pro/Pro+ budget OR Cemini adopts a GCP credit allocation for backtesting compute, **AND**
2. **Use case strictly scoped** to non-sensitive experiments (e.g., publicly-available LLM fine-tuning on public datasets; weather-model backtesting against public NWS data — never proprietary trading algo iteration or trading-credential-handling notebooks).

Bonus pre-adoption check: GitHub-issue track on Colab Secrets API arriving in VSCode extension. Until then, env-var-only credential handling is the discipline floor.

[Source: Link Evaluation Brief Trading Stack.docx, URL 14; Phase-0 audit 2026-05-11]
