---
title: "Markdown Preview — Native macOS .md Renderer (pluk-inc)"
type: entity
tags: [tool, markdown, macos, workflow, cross-wiki, k37]
keywords: [markdown, preview, pluk, adopt, three-surface-eval]
related:
  - sources/evaluating-urls-system-integration.md
  - concepts/tool-evaluation-framework.md
  - concepts/cemini-license-posture.md
maturity: draft
created: 2026-05-11
updated: 2026-05-11
---

## Relations
- `@sources/evaluating-urls-system-integration.md` — source evaluation brief (URL 13)
- `@concepts/tool-evaluation-framework.md` — three-surface methodology applied
- `@concepts/cemini-license-posture.md` — license posture context

**Cross-wiki briefs** (live in target wikis' `briefs/` folders, outside `wiki/`):
- image-gen-wiki: `briefs/2026-05-11_2026-05-11_markdown-preview-pluk-cross-wiki.md`
- seo-wiki: `briefs/2026-05-11_2026-05-11_markdown-preview-pluk-cross-wiki.md`
- 3d-printing-wiki: `briefs/2026-05-11_2026-05-11_markdown-preview-pluk-cross-wiki.md`

## Raw Concept

- **Repo / URL**: `github.com/pluk-inc/markdown-preview`
- **Tier (per source brief)**: **Adopt**
- **License**: [NEEDS VERIFICATION 2026-05-11] License unknown in brief — likely permissive given Homebrew tap distribution.

## Narrative

Native macOS .md previewer using swift-markdown (cmark-gfm wrapper) + WKWebView. Supports LaTeX + Mermaid + advanced markdown extensions. Bypasses Electron memory overhead. Install via `brew install --cask pluk-inc/tap/markdown-preview`.

### Integration vector

Adopt for workflow laptop. Set as default `.md` handler in macOS — accelerates manual review cycle for analytical briefs across all 4 wikis. **Cross-wiki candidate** — useful to image-gen-wiki, seo-wiki, 3d-printing-wiki since all are markdown-based.

### Risks

Strict OS lock-in: macOS 15 (Sequoia) or later required. Not deployable to Hetzner CPX21 (headless Linux).

[Source: Evaluating Urls System Integration.docx, URL 13]
