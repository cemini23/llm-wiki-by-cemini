---

title: different-ai/OpenWork — MCP desktop UI Extract for Atto
type: entity
tags: [entity, tool, mcp, atto, k204, extract, phase0]
keywords: [OpenWork, Claude Cowork, SKILL.md, local-first, FSL-1.1-MIT, atto-mcp, CONDITIONAL-GO]
related:
  - sources/eval-github-repo-revenue-evaluation-2026-07-29.md
  - concepts/gpuology-genealogy-agent-kit.md
  - concepts/wiki-tooling-evaluation.md
  - concepts/cemini-license-posture.md
maturity: validated
created: 2026-07-29
updated: 2026-07-31
wire_status: wont_wire
wire_note: desktop REFERENCE; Atto Extract brief only
---

## Relations

- @sources/eval-github-repo-revenue-evaluation-2026-07-29.md — K204 revenue eval (Extract)
- @concepts/gpuology-genealogy-agent-kit.md — Priority #1 kit / vault UI
- @concepts/wiki-tooling-evaluation.md — tier ritual
- @concepts/cemini-license-posture.md — MIT vs FSL boundary

## Raw Concept

Open-source desktop agent UI (Claude Cowork alternative) with MCP tooling + skill loading. ~17.4k★; default branch `dev`. Candidate **pattern source** for Atto’s local vault UX — not a drop-in product shell.

## Narrative

**Tier:** Extract (Atto)  
**Phase-0 verdict (2026-07-29):** **CONDITIONAL-GO Extract (patterns only).**

| Check | Result |
|-------|--------|
| Clone | `.local/adopts/openwork` shallow `dev` (~148M) |
| Root license | **MIT** except `/ee` |
| `ee/LICENSE` | **FSL-1.1-MIT** — Competing Use ban for commercial substitutes |
| `packages/openwork-ui-mcp` | Explicit **MIT**; `@modelcontextprotocol/sdk ^1.29.0`; `node --check` OK |
| Full product wire | **No** — Atto already has `apps/desktop` + Python `atto_mcp` |
| BR civic APIs (same eval) | Not adopted |

**Steal:** MIT UX / skill-router / tool-call rendering outside `ee/`.  
**Do not:** vendor Electron OpenWork as YourAtto; depend on `ee/`; treat `openwork-ui-mcp` as a client for `atto-mcp` (it controls OpenWork’s own UI bridge).

Script: `scripts/adopt_k204_phase0.sh` · Report: `.local/reports/k204-phase0-2026-07-29.md` · Atto visa: `Atto/docs/k204-openwork-visa.md`.

## Dead Ends

Shipping AGPL/GPL neighbors from the same eval batch into an OpenWork wrapper — license contagion. Using MediaCrawler patterns inside the same desktop binary — commercial disclaimer + ToS risk. Shipping `ee/` code in a commercial Atto kit — FSL Competing Use.
