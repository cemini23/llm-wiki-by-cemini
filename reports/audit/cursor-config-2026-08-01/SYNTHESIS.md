# Cursor audit — configuration / token / MCP

**Date:** 2026-08-01  
**Mode:** `config-infra` (+ token economics + DeepSeek offload)  
**Roles → models:** config-semantics→`gemini-3.1-pro`, code-implementation→`gpt-5.6-sol-medium`, third-lens→`cursor-grok-4.5-high-fast`, DeepSeek→`claude-ds` (readonly)

**Overall:** SHIP-WITH-FIXES — day-to-day stack works; fix secrets + rule duplication + dead lazy-tool paths before scaling DeepSeek offload.

## Verdict rollup

| Auditor | Verdict |
|---------|---------|
| gemini-3.1-pro | WARN |
| gpt-5.6-sol-medium | FAIL (secrets + ~16k baseline tokens) |
| cursor-grok-4.5-high-fast | WARN |
| claude-ds (DeepSeek) | WARN |

## Consensus (≥2 auditors)

1. **CRITICAL — plaintext credentials in `~/.cursor/mcp.json`** (Brave API key literal + GitHub Bearer). Rotate; move to env/keychain; never hand this file to free/OpenRouter models.
2. **CRITICAL/HIGH — route rule 4× injection** — `tipdrop-route-outsource.mdc` ≡ `cemini-route-outsource.mdc` (2220B), both alwaysApply, both global + OSINT.
3. **HIGH — constant context floor ~16k tok/turn** — CLAUDE.md (~28KB) + OSINT AA rules (~25KB) + global AA (~13KB), with ~8KB pure cross-scope duplicates.
4. **HIGH — dead lazy-tool wiring** — `kb-server` → `ssh cemini-librarian`; conductor/exa still point at `~/Desktop/OSINT WORKSPACE` (Projects is live).
5. **WARN — cold MCP surface** — Cloudflare×5, stripe, stash (red), playwright, mcp-legal-it, obsidian-vault, duplicate codebase-memory.
6. **WARN — demote large alwaysApply negatives** — esp. `osint-phase1-adopt-wires` (~5KB); keep as globs or skill-gated.
7. **INFO/DISK — `state.vscdb` 4.3GB** — vacuum chats; not token but slows restore.
8. **DeepSeek ownership** — easy/mid mechanical via `/route` → claude-ds; hard/money/verdicts stay Cursor premium + Grok implement.

## Unique (single auditor — still investigate)

| Auditor | Unique angle |
|---------|----------------|
| gemini | `codebase-memory-mcp` double-registered → duplicate tool schemas every turn |
| gpt-sol | Global Claude SessionStart/PostCompact Obsidian hooks + 11 plugins inject into every CC session — demote to OSINT profile |
| grok | TipDrop twin **cognitively re-centers TipDrop** against WorkDir contract; replace 12-step ritual with one cadence script |
| claude-ds | Highest leverage = premium designs hot/cold split, **claude-ds mid-executes** the file moves; Desktop path drift makes lazy-tool look alive while divergent |

## Conflicts

| Topic | gemini | gpt-sol | grok | claude-ds | Resolution |
|-------|--------|---------|------|-----------|------------|
| Keep brave-search? | cold/disable | disable (prefer Exa+browser) | fallback only | HOT after key rotation | **Disable until key in env**; prefer Exa day-to-day |
| Keep direct exa vs lazy-tool only | keep exa | keep project exa; strip lazy fetch/exa | keep exa + lazy prod | prefer lazy-tool only | **Keep direct Exa HOT**; lazy-tool for prod-mcp; drop dead sources |
| Severity of secrets | (in Critical via bloat framing) | FAIL critical | critical | critical | Treat as **P0 rotate today** |

## Recommended fix order

1. **P0 — Rotate** Brave + GitHub tokens in `~/.cursor/mcp.json`; switch to env refs; do not paste file into DeepSeek/OpenRouter.
2. **P0 — Delete** `tipdrop-route-outsource.mdc` (global + OSINT); keep one `cemini-route-outsource.mdc` (prefer global only).
3. **P1 — Remove** `kb-server` + fix Desktop→Projects paths in `lazy-tool.yaml`; reindex.
4. **P1 — Disable cold MCP** (CF×5, stripe, stash, playwright, legal-it, obsidian, one of two codebase-memory).
5. **P1 — Demote AA** phase1-adopt-wires / visual / goal / security-preflight to requestable or globs; slim CLAUDE.md ritual → `check_all_cadences.sh`.
6. **P2 — Vacuum** Cursor `state.vscdb` / agent-worker after closing Cursor.
7. **P2 — Habit** — mid mechanical work always `/route` (claude-ds); premium for plan/verdict only.

## Day-to-day HOT keep (consensus)

| Layer | Keep |
|-------|------|
| MCP | `lazy-tool`→prod-mcp, `exa`, `github` (after rotate), built-in browser |
| Rules | one route trigger, supply-chain, shortened mcp-defaults, ingest-gates (already gated) |
| Skills | route, goal, wiki-ingest, phase1-wire, discord-ops (dry-run), audits on demand |
| Schema | CLAUDE.md core only (not full cadence checklist) |

## DeepSeek /route matrix (consensus)

| Lane | Own | Not |
|------|-----|-----|
| easy | wiki notes, lint drafts, triage, cadence summaries | money/security verdicts |
| mid | rule/MCP cleanup execute, mechanical refactors, audit inventories | final security sign-off |
| hard/money | — | architecture, trading reads, LIVE Discord, PII, secret migration design |

## Artifacts

- Pack: `reports/audit/cursor-config-2026-08-01/PROMPT.md`
- Inventory: `.../INVENTORY.md`
- Auditors: `auditor-{gemini,gpt-sol,grok,claude-ds}.md`
