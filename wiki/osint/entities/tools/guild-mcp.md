---
title: "guild — Agent-Coordination Substrate (eval-brief MISCHARACTERIZED as retrieval MCP)"
type: entity
tags: [tool, mcp-server, go-binary, agent-coordination, quest-lore-oath-brief, k38, phase-0-no-go-as-kb-replacement, eval-brief-mischaracterization]
keywords: [guild, mcp, defer, three-surface-eval, agent-substrate]
related:
  - sources/link-evaluation-brief-trading-stack.md
  - concepts/tool-evaluation-framework.md
  - concepts/cemini-license-posture.md
  - concepts/mcp-tool-marketplace.md
maturity: validated
created: 2026-05-11
updated: 2026-05-11
phase_0_audit: NO-GO as kb-server replacement 2026-05-11 — eval-brief framing mischaracterized the tool function; possible CONDITIONAL-GO for separate agent-coordination eval
adoption_status: DEFERRED 2026-05-11 (kb-server displacement framing rejected; separate agent-coordination eval not chartered)
---

## Relations
- `@sources/link-evaluation-brief-trading-stack.md` — source evaluation brief (URL 18)
- `@concepts/tool-evaluation-framework.md` — three-surface methodology applied
- `@concepts/cemini-license-posture.md` — license posture context
- `@concepts/mcp-tool-marketplace.md` — bus-factor + project-age rubric applied

## Raw Concept

- **Repo / URL** [VERIFIED 2026-05-11]: `github.com/mathomhaus/guild`
- **Tier (per source brief)**: Adopt → **DOWNGRADED 2026-05-11 to DEFERRED** on Phase-0 audit findings
- **License** [VERIFIED 2026-05-11]: **Apache-2.0**
- **Phase-0 audit** [VERIFIED 2026-05-11]: 156★ / 20 forks / 5 contributors / 28 open issues. Created 2026-04-20 (~3 weeks old at audit time). 4 releases. License is clean — adoption verdict is NOT a license issue. Uses `BAAI/bge-small-en-v1.5` int8 ONNX (~33 MB MANIFEST-pinned).

## Narrative — eval-brief mischaracterization

The K38 eval brief framed guild as a **"local-first search MCP server"** and a **"potential Ollama replacement on Hetzner CPX21"**. Phase-0 audit (read of `internal/lore/`, `AGENTS.md`, primary schema) reveals:

1. **guild is fundamentally an *agent-coordination substrate*** with `quest` / `lore` / `oath` / `brief` primitives (claim-and-clear task board with cascading dependency unblock). It is NOT a generic markdown-retrieval MCP.
2. **The BM25 + int8 ONNX + RRF retrieval stack is *internal to guild's lore archive*** — bound to its quest/lore/oath/brief schema — NOT a drop-in for kb-server's wiki-markdown serving.
3. **State lives in `~/.guild/` SQLite tied to guild's schema** (quests, lore, oath, brief tables) — does not ingest flat markdown directly.
4. **Cannot displace kb-server** for the Cemini wiki-serving use case.

### Integration vector

**NO-GO 2026-05-11 as kb-server replacement**. The eval brief's "Ollama replacement" framing was wrong; adopting under that framing leads to wasted integration work, then a Phase-1 rejection. kb-server stays as the wiki serving layer (decision finalized 2026-05-05 per ROADMAP).

**Possible CONDITIONAL-GO for a separate agent-coordination eval** — the quest/lore/oath/brief pattern may have value for the Cemini analyst-session-handoff problem. That eval is its own brief, not chartered here.

### Risks

1. **Mischaracterization-driven adoption** — adopting under "Ollama replacement" framing = wasted work + Phase-1 rejection.
2. **Project age + bus factor** — 3 weeks old at audit / 5 contributors / 156★ = single-day-dev/early-stage per `mcp-tool-marketplace.md` Pattern 2. Would require fork-and-pin if adopted now.

### Cost / footprint

| Item | Value |
|---|---|
| Subscription | $0 (pre-built binary) |
| RAM idle | ~40-60 MB |
| RAM loaded (int8 ONNX) | ~120-180 MB |
| CPX21 fit | OK — but does not address kb-server's job |

### Activation trigger

Charter a NEW eval brief focused on guild-as-analyst-session-handoff-substrate (separate workstream from K38's kb-server framing). Only then re-audit under the correct framing.

[Source: Link Evaluation Brief Trading Stack.docx, URL 18; Phase-0 audit 2026-05-11 reframing]
