---
title: "Markdown Preview — Native macOS .md Renderer (pluk-inc)"
type: entity
tags: [tool, markdown, macos, workflow, cross-wiki, k37]
keywords: [markdown, preview, pluk, adopt, three-surface-eval]
related:
  - sources/evaluating-urls-system-integration.md
  - concepts/tool-evaluation-framework.md
  - concepts/cemini-license-posture.md
maturity: validated
created: 2026-05-11
updated: 2026-05-11
adopted_as: /Applications/Markdown Preview.app (v0.0.21, 2026-05-11)
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
- **License**: **MIT** [VERIFIED 2026-05-11] — confirmed in `LICENSE` file at repo root.
- **Phase-0 maturity** [VERIFIED 2026-05-11]: 632★ / 31 forks / 7 open issues / 20 releases in ~13 days (created 2026-04-28, pre-1.0 at v0.0.21). High release cadence = active iteration with fast bug-fix turnaround. Apple Developer ID signed (`TeamIdentifier=5P3TSMNV42`), universal binary (x86_64 + arm64).
- **Laptop install** [VERIFIED 2026-05-11]: v0.0.21 via direct DMG download from GitHub release (Homebrew not present on this Mac). Installed at `/Applications/Markdown Preview.app`. No quarantine flag to clear. Phase 2 default-handler set deferred (requires `duti` install or one-time manual Finder action).

## Narrative

Native macOS .md previewer using swift-markdown (cmark-gfm wrapper) + WKWebView. Supports LaTeX + Mermaid + advanced markdown extensions. Bypasses Electron memory overhead.

Install path used here was direct DMG (Homebrew not on this laptop). Equivalent cask path remains `brew install --cask pluk-inc/tap/markdown-preview` for future systems.

### Integration vector

**Adopted 2026-05-11** for workflow laptop. Next step: set as default `.md` handler in macOS — accelerates manual review cycle for analytical briefs across all 4 wikis. **Cross-wiki candidate** — useful to image-gen-wiki, seo-wiki, 3d-printing-wiki since all are markdown-based.

### Risks

- Strict OS lock-in: macOS 15 (Sequoia) or later required. Not deployable to Hetzner CPX21 (headless Linux).
- Pre-1.0 version. Expect breaking changes. Pin v0.0.21 if a future release regresses.
- 13-day-old org — track upstream for sustained maintenance vs. abandonment.

[Source: Evaluating Urls System Integration.docx, URL 13]
