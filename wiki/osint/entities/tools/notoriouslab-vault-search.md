---
title: "vault-search — Obsidian + Ollama Semantic Search"
type: entity
tags: [tool, obsidian, semantic-search, ollama, reference-only, k38]
keywords: [notoriouslab, vault, search, reference-only, three-surface-eval]
related:
  - sources/link-evaluation-brief-trading-stack.md
  - concepts/tool-evaluation-framework.md
  - concepts/cemini-license-posture.md
maturity: draft
created: 2026-05-11
updated: 2026-05-11
---

## Relations
- `@sources/link-evaluation-brief-trading-stack.md` — source evaluation brief (URL 1)
- `@concepts/tool-evaluation-framework.md` — three-surface methodology applied
- `@concepts/cemini-license-posture.md` — license posture context

## Raw Concept

- **Repo / URL**: `github.com/notoriouslab/vault-search`
- **Tier (per source brief)**: **Reference-only**
- **License**: [NEEDS VERIFICATION 2026-05-11] License not located in source brief — severe IP-readiness blocker for any code lift.

## Narrative

Obsidian-tied semantic search plugin using local Ollama embeddings. Indexes personal markdown notes via high-dimensional vectors. Knowledge base contents never leave the local machine.

### Integration vector

Reference-only — Obsidian-specific architecture not deployable to headless Hetzner librarian. The pattern (Markdown → Ollama embedding → local vector search) is conceptual validation for the `llm-wiki-compiler` semantic-search design.

### Risks

License missing — hard blocker for code extraction into IP-sale-ready proprietary repo. Tight coupling to Obsidian frontend.

[Source: Link Evaluation Brief Trading Stack.docx, URL 1]
