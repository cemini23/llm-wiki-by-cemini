---
title: Skill vetting
type: concept
tags: [concept, llm-tooling, safety, methodology]
keywords: []
related:
  - sources/3-2-audit-dr.md
  - sources/3-6-git-1.md
  - sources/3-19-compliance-research.md
  - sources/3-19-ip-sale-research.md
  - concepts/cryptographic-audit-trail.md
  - entities/frameworks/fastmcp.md
  - concepts/ai-organisation-design.md
  - sources/omc-talent-container-paper.md
maturity: retracted
created: 2026-04-23
updated: 2026-04-24
---

## Relations

- @sources/3-2-audit-dr.md
- @sources/3-6-git-1.md
- @sources/3-19-compliance-research.md
- @sources/3-19-ip-sale-research.md — cited as part of LLM-architecture-defensibility deal signal (typed/gated/audited capability surface vs "agent runs SQL and prays")
- @concepts/cryptographic-audit-trail.md
- @entities/frameworks/fastmcp.md

## Raw Concept

Synthesized across 3 source(s) in the Cemini research corpus that reference this concept directly or by equivalent terminology.

## Narrative

**[RETRACTED — 2026-04-24 Track C audit]** The 5-point vetting checklist + vetting-ledger described below **does not exist in code**. Probes:
- `grep -rln --include="*.py" --exclude-dir=".worktrees" "skill_vetting\|vetting_ledger\|vetted_skills" .` → 0 hits.
- No vetting registry table in Postgres.
- `find . -name "*skill*" -o -name "*vetting*"` returns only `.claude/skills/{docker,new-contract,pitfalls,rl-retrain,step-recon}/SKILL.md` — **Claude-Code harness slash-commands for the dev loop**, not the MCP-tool vetting ledger the concept describes. Different concept.
- MCP tool safety is enforced lightly via `@mcp.tool(annotations={"destructive": False, "readOnly": True})` in `cemini_mcp/server.py` and the graceful-degradation pattern in `cemini_mcp/CLAUDE.md`, but there is **no central ledger of who vetted each tool or when**, no approval log, no 5-point checklist encoded anywhere.
- Adjacent evidence: Track B's `wiki_search` tool has one `audit_hash_chain` entry (`source_table=wiki_search_audit`) but its payload is an **error fallback** (`{"error":"invalid is not a valid git identifier...", "fallback":true}`), not a vetting-approval row.

Ticket (**P1**): *Ship skill-vetting ledger — table + per-tool vetting row + CI lint that every MCP tool has a ledger entry before merge*. Low-effort; catches regressions where a new MCP tool ships without explicit review. Gap memo: `briefs/track-c-walk-results.md`.

Original claimed narrative retained below as retracted-claim-of-record.

---

**Skill vetting** is the review process by which an MCP-exposed tool
(Anthropic Agent Skill, FastMCP server endpoint, LangGraph tool node)
is evaluated before it's made callable by the agent.

### Cemini's vetting checklist per the 3-2 audit + 3-19 compliance research
1. **Capability surface audit** — what irreversible state can the
   skill mutate? (Order submission, position close, credential
   rotation = highest tier.)
2. **Input validation** — every parameter typed by Pydantic v2;
   schemathesis-generated property tests run on the MCP schema.
3. **Authorization gate** — risk-engine state is checked before the
   skill executes; RED-regime + high-tier skills require an
   explicit human-in-the-loop confirmation.
4. **Audit anchoring** — every skill invocation + arguments +
   return value is pg_tamperlogged and Merkle-rooted.
5. **Rollback plan** — for any mutating skill, a compensating-action
   counterpart skill is registered alongside so the agent can
   undo a mistake within the same reasoning turn.

### Institutional-diligence signal
Skill vetting is how Cemini demonstrates to an IP-sale buyer that
its LLM layer is not a "let the agent run SQL and pray" architecture —
every capability is typed, gated, logged, and reversible.

## Snippets

*(populate as source stubs are deep-read.)*
