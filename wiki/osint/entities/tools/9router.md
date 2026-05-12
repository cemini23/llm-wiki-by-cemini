---
title: "9Router — Token-Compressing LLM Proxy (eval-brief MISCHARACTERIZED)"
type: entity
tags: [tool, llm-proxy, token-compression, k38, phase-0-no-go, eval-brief-mischaracterization, family-c-tos-risk]
keywords: [9router, defer, three-surface-eval, caveman-mode, oauth-grafting]
related:
  - sources/link-evaluation-brief-trading-stack.md
  - concepts/tool-evaluation-framework.md
  - concepts/cemini-license-posture.md
  - concepts/mcp-tool-marketplace.md
  - entities/tools/lazy-tool.md
  - entities/tools/claude-code-router.md
  - entities/tools/meridian.md
maturity: validated
created: 2026-05-11
updated: 2026-05-11
phase_0_audit: NO-GO (cemini-prod) 2026-05-11 — eval-brief framing mischaracterizes the tool; existing lazy-tool + claude-code-router cover the actual problem
adoption_status: DEFER-INDEFINITELY 2026-05-11
---

## Relations
- `@sources/link-evaluation-brief-trading-stack.md` — source evaluation brief (URL 15)
- `@concepts/tool-evaluation-framework.md` — three-surface methodology applied
- `@concepts/cemini-license-posture.md` — license posture context
- `@concepts/mcp-tool-marketplace.md` — Family-C TOS risk rubric applied
- `@entities/tools/lazy-tool.md` — already validated, 46% token reduction, single Go binary; covers 9router's compression role
- `@entities/tools/claude-code-router.md` — already validated, LLM routing layer; covers 9router's routing role
- `@entities/tools/meridian.md` — sibling Family-C TOS-risk candidate from K39 (OAuth-grafting pattern reference)

## Raw Concept

- **Repo / URL** [VERIFIED 2026-05-11]: `github.com/decolua/9router`
- **Tier (per source brief)**: Adopt → **DOWNGRADED 2026-05-11 to DEFER-INDEFINITELY** on Phase-0 audit findings
- **License** [VERIFIED 2026-05-11]: **MIT**
- **Phase-0 audit** [VERIFIED 2026-05-11]: 8,197★ / 1,316 forks / 79 contributors / 419 open issues. Created 2026-01-05; last push 2026-05-11. 46 releases. License is clean — adoption verdict is NOT a license issue.

## Narrative — eval-brief mischaracterization

The K38 eval brief framed 9router as a "lean OpenAI-compatible compress-then-forward proxy" claiming **~65% token reduction**. Phase-0 audit reveals:

1. **It is not a lean proxy**. It is a private-package Next.js 16 + React 19 dashboard (`9router-app`, `"private": true` in package.json) with bundled Cowork / MCP Marketplace / Tailscale / Cloudflare integrations. Footprint: monaco-editor + recharts + Material UI + sql.js.
2. **README's actual token-savings claim is 20-40%, not 65%**. The eval brief's 65% number cannot be reproduced from upstream documentation.
3. **Mechanism is `tool_result` content compression** ("Caveman Mode") — overlaps directly with Cemini's already-validated `lazy-tool` (46% reduction, MIT, single Go binary, 2026-05-09 brief).
4. **Family-C TOS risk** — the "free unlimited" providers (Kiro AI, OpenCode Free, Vertex credits) operate by OAuth-grafting onto third-party developer-tier auth. Direct conflict with Cemini's IP-sale-readiness license clean-list posture. Vendors will revoke at any moment.

### Integration vector

**NO-GO 2026-05-11**. Architectural fit + redundancy + TOS risk all reject. Cemini's existing stack (lazy-tool + claude-code-router) already covers the legitimate compression + routing functions at ~10× lower RAM footprint with no Family-C TOS exposure.

### Risks (if adopted anyway)

1. **Family-C TOS landmine** — free-tier providers via OAuth grafting violate Cemini's IP-sale-readiness license posture.
2. **Footprint mismatch** — full Next.js + monaco-editor + recharts + sql.js stack vs. lazy-tool's single Go binary on 2 vCPU / 4 GB CPX21.

### Activation trigger (if ever)

Revisit only if a specific 9router primitive (e.g., open-sse SSE-stall handling) emerges as un-replicable elsewhere AND the Family-C OAuth dependency can be cleanly removed.

[Source: Link Evaluation Brief Trading Stack.docx, URL 15; Phase-0 audit 2026-05-11 downgrade]
