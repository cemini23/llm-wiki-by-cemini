claude-ds - DeepSeek Claude Code (model=deepseek-v4-flash)
Install: /Users/claudiobarone/.deepseek-claude
PromptFile: /Users/claudiobarone/Projects/OSINT WORKSPACE/reports/audit/cursor-config-2026-08-01/claude-ds-prompt.txt
### Verdict
WARN — the core OSINT/route workflow is sound, but ~16K tokens of constant context per turn (including a byte-identical route rule loaded 2x per scope), 11 cold MCP servers, a stale Desktop-vs-Projects path drift, and **plaintext credentials in global mcp.json** must be fixed before scaling DeepSeek offload.

### Day-to-day keep list
- **lazy-tool MCP** — single proxy entry to prod-mcp/fetch/exa; the osint-mcp-defaults 3-step protocol is the correct research path
- **prod-mcp** (via lazy-tool) — read-only prod health, HOT daily
- **exa + fetch** (via lazy-tool) — research + URL verification; drop the direct-server duplicates
- **brave-search** — HOT web fallback (rotate/redact the key first, see Findings)
- **discord-ops** — DRY_RUN=true, safe and HOT for dry-run ops
- **chrome-devtools** — keep browser verify here; disable playwright (operator prefers built-in)
- **github MCP** — daily PR/issue work
- **route skill + one route-outsource rule** — the offload chain; keep exactly one copy (cemini), delete tipdrop
- **goal / phase1-wire / i-have-adhd / to-issues / super-audit / cursor-audit / searchos-progress / grill-with-docs** — active workflow skills
- **OSINT project rules**: osint-ingest-gates, osint-phase1-adopt-wires, osint-visual-deliverables, osint-workflow-operators, osint-mcp-defaults (trim stale librarian block)
- **cemini-cursor-security-preflight** — keep, but in exactly one scope

### Findings
| Severity | Finding | Evidence | Fix |
|----------|---------|----------|-----|
| critical | Plaintext credentials in global mcp.json: `BRAVE_API_KEY` and a GitHub Copilot Bearer `gho_…` token | `~/.cursor/mcp.json` lines 19 & 23–25 | Rotate both; move to env/keychain; never let any claude-ds/DeepSeek handoff read this file — free-OpenRouter models may log prompts, and the gho_ token is one grep away from a handoff |
| warn | Route rule loaded 2x per scope — `tipdrop-route-outsource.mdc` and `cemini-route-outsource.mdc` are byte-identical (both 2220B), both `alwaysApply`, in both global and OSINT scopes | `~/.cursor/rules/{cemini,tipdrop}-route-outsource.mdc`, `…/.cursor/rules/{cemini,tipdrop}-route-outsource.mdc`; alwaysApply lists show all 4 | Delete `tipdrop-route-outsource.mdc` in both scopes; keep cemini copy + canon `SKILL.md`. Saves ~1.1K tok/turn |
| warn | 5 rules duplicated across global and OSINT scopes (security-preflight 1106B, goal-skill 813B, phase1-policy-wires ~2038B, route-outsource 2220B, tipdrop 2220B) — likely injected twice when workspace open | Same filenames+bytes in both alwaysApply lists (lines 129–143) | De-scope: base-case rules (route, security-preflight) live global only; OSINT-specific stay project-only. Saves ~2.1K tok/turn |
| warn | `lazy-tool.yaml` sources point at `~/Desktop/OSINT WORKSPACE` while the active workspace is `~/Projects/OSINT WORKSPACE` | lazy-tool.yaml lines 15–19 (conductor) & 30–32 (exa) use Desktop; audit pack + project mcp.json use Projects | Reindex to the Projects path or delete the stale Desktop copy; verify no duplicate workspace is being indexed |
| warn | 11 COLD MCP servers enabled globally/project: cloudflare x5, stripe, obsidian-vault, mcp-legal-it, codebase-memory-mcp, stash (red) | `~/.cursor/mcp.json`, `…/.cursor/mcp.json`; operator "COLD/REFERENCE" | Disable in Cursor UI (toggle wins over `"disabled": false`); keep only the lazy-tool proxy paths |
| warn | `codebase-memory-mcp` registered in BOTH global and project mcp.json — double-spawn, and it's COLD | both mcp.json files list it | Remove one registration (keep project copy if used) |
| info | `fetch`/`exa` exposed both directly and proxied via lazy-tool → duplicate tool definitions / tool-list noise | `…/.cursor/mcp.json` + lazy-tool.yaml sources | Keep the lazy-tool proxy (per osint-mcp-defaults), disable direct fetch/exa, or vice versa — one path only |
| info | `kb-server` source still in lazy-tool.yaml though librarian is decommissioned (2026-06-14) — every lazy-tool start attempts an ssh to a dead host | lazy-tool.yaml lines 18–24; osint-mcp-defaults.mdc line 10 | Remove the kb-server source block; reindex |
| info | `state.vscdb` 4.3GB + `cursor-agent-worker` 1.2GB disk bloat | inventory lines 21–22 | Periodic cleanup/DB compaction; not a token issue |
| info | `osint-mcp-defaults.mdc` (3814B, alwaysApply) carries a stale dated librarian block + 3-step protocol; CLAUDE.md is 27.8KB flat with no hot/cold split | file content; audit note "always in agent context" | Trim stale block; split CLAUDE.md into slim always-include + on-demand reference files |

### Token waste map
1. **Constant context floor** — CLAUDE.md 27.8KB + OSINT rules 24.5KB + global rules 12.8KB ≈ 65KB ≈ **~16K tok/turn** — high (structural, biggest lever)
2. **Rule duplication** — route rule 2x/scope (4 loads) + 5 cross-scope rules ≈ **~3.2K tok/turn** pure waste — high, zero-value
3. **Multi-auditor premium runs** when `/route` would suffice (this audit = 4 auditors) — high $, variable token
4. **Cold MCP tool-list + process overhead** (cloudflare x5, stripe, obsidian, legal-it, stash) — med
5. **Session hooks ritual** (`SessionStart`/`PostCompact`) running every turn — med/low
6. **Duplicate tool definitions** (fetch/exa direct+proxy, codebase-memory 2x) — low
7. **state.vscdb 4.3GB / agent-worker 1.2GB / conversation-search.db** — high disk, not token

### DeepSeek / claude-ds automation candidates
| Task | Why DeepSeek | When keep Cursor premium |
|------|--------------|--------------------------|
| Easy text: wiki notes, briefs, report drafts, rewrite | easy lane → OpenRouter free → claude-ds, always-approve, near-zero cost | When content is money/security-sensitive or needs citation-level accuracy |
| to-issues / searchos-progress / task triage | mechanical, structured, cheap; perfect easy lane | When severity/label judgment actually matters |
| Rule dedup & MCP disable edits (mid) | claude-ds executes the Grok/premium-written plan with git protection; safe under always-approve | When the diff needs expert review before apply — keep final apply in premium |
| Recurring audits / postmortems (mid) | repetitive read+compare; DeepSeek scales cheaply | Final verdict + sign-off on premium (e.g. this audit's conclusion) |
| prod health checks via lazy-tool (easy) | read-only low-stakes queries | **Money reads** (conviction/regime/trading decisions) stay premium |
| Bulk mechanical refactors / workspace cleanup (mid) | mid-execute lane; mechanical, reversible | Hard multi-file changes with tests → premium plan + Grok implement |

**Route lanes, concretely:** easy → DeepSeek always; mid → Grok/premium plan + **claude-ds execute**; hard/money → premium plan + Grok implement — DeepSeek is *excluded* from hard by both the route contract (SKILL.md lines 84–87) and deepseek-v4-flash's ceiling. Keep the premium "understanding" boundary: never delegate verdicts, security decisions, or schema design to DeepSeek.

### Confidence
high — duplication, plaintext secrets, and path drift are directly verified from files; medium on exact token counts (byte→token estimates) and on Cursor's runtime behavior of loading both global+project alwaysApply scopes.

### Unique angle
The highest-leverage single move is **context-hygiene as a DeepSeek mid-execute task**: a premium model designs a hot/cold split (slim CLAUDE.md + one canonical route rule + single-scope base-case rules, ~65KB → ~25KB constant), then claude-ds mechanically executes the split under always-approve. And the thing every other auditor will miss: **lazy-tool is proxying to a stale `~/Desktop/OSINT WORKSPACE` copy** while the real workspace lives in `~/Projects` — so prod-mcp/exa/conductor look alive but may be hitting dead or divergent paths, and the fix is a reindex, not a code change.
