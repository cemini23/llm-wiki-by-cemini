---
title: "Google Colab VS Code Extension"
type: entity
tags: [tool, vscode-extension, colab, gpu-remote, workflow, adopt, k38]
keywords: [google, colab, vscode, adopt, three-surface-eval]
related:
  - sources/link-evaluation-brief-trading-stack.md
  - concepts/tool-evaluation-framework.md
  - concepts/cemini-license-posture.md
maturity: draft
created: 2026-05-11
updated: 2026-05-11
---

## Relations
- `@sources/link-evaluation-brief-trading-stack.md` — source evaluation brief (URL 14)
- `@concepts/tool-evaluation-framework.md` — three-surface methodology applied
- `@concepts/cemini-license-posture.md` — license posture context

## Raw Concept

- **Repo / URL**: `developers.googleblog.com/google-colab-is-coming-to-vs-code`
- **Tier (per source brief)**: **Adopt**
- **License**: Free + paid tiers; Google ToS governs data usage

## Narrative

VS Code extension bridging local IDE to cloud-hosted Google Colab runtimes. Open .ipynb locally, execute on Google's remote GPUs/TPUs.

### Integration vector

Adopt — install locally for research phase. Enables rapid GPU-accelerated quant model iteration without local hardware upgrades.

### Risks

**Data egress vulnerability** — code on Colab transmits proprietary algorithmic logic + API keys to Google. Strict env-var discipline required. Never run prod-secrets through Colab.

[Source: Link Evaluation Brief Trading Stack.docx, URL 14]
