### Verdict
**WARN** — day-to-day stack is usable, but Cemini systematically overpays Cursor tokens via alwaysApply duplication (~33KB when OSINT is open), a 28KB always-read `CLAUDE.md` (including a 4.5KB session ritual), and a cold global MCP surface that still exposes tool schemas.

### Day-to-day keep list
- **Rules (HOT):** one route contract (`cemini-route-outsource`), `osint-mcp-defaults`, `osint-ingest-gates` (already `alwaysApply: false` + globs — correct), `agent-setup-supply-chain`, `cemini-projects` (global map)
- **Skills (HOT):** `route`, `goal`, `cemini-wiki-ingest`, `phase1-wire`, `discord-ops` (dry-run)
- **MCP (HOT):** `lazy-tool` → `prod-mcp`, `exa`, `github`; built-in browser (not Playwright); `atto` only when Atto vault work
- **Schema:** keep `CLAUDE.md` as wiki canon — but **do not** keep the full session ritual + quarterly cadence checklist in the always-on path
- **Outsource path:** `/route` → OpenRouter free → Grok plan → **claude-ds** execute (mid); premium plan only for hard/money

### Findings
| Severity | Finding | Evidence | Fix |
|----------|---------|----------|-----|
| critical | Route contract injected **4×** every turn (tipdrop twin × project+global) | Identical `cemini-route-*` + `tipdrop-route-*` at project and `~/.cursor/rules`; ~8880 bytes of copies | Delete `tipdrop-route-outsource.mdc` (or make alias/stub `alwaysApply: false`); keep **one** alwaysApply route rule, preferably user-global only |
| critical | Plaintext secrets in global MCP config | `~/.cursor/mcp.json` holds Brave key + GitHub Bearer in JSON | Move to env / macOS keychain / Cursor secret refs; rotate exposed tokens |
| warn | alwaysApply double-layer: ~32.9KB when OSINT open | OSINT AA 20053 + global AA 12831; 5 overlapping filenames ≈8.2KB pure double-inject | Project keeps OSINT-only rules; federation skills (`goal`, `route`, `phase1`, `security-preflight`) live once under `~/.cursor/rules` |
| warn | `osint-phase1-adopt-wires` (5.0KB) is largest OSINT AA tax; mostly “don’t wire X” negatives | `.cursor/rules/osint-phase1-adopt-wires.mdc` 5019 bytes, `alwaysApply: true` | Demote to globs (`Atto/**`, `.local/adopts/**`, briefs) or `/phase1` skill-only |
| warn | Session-start ritual forces tool-call fanout for mostly-no-op checks | `CLAUDE.md` §Session-start ritual ~4584 bytes; steps 3–8 quarterly / one retired; federation morning summary already exists | Collapse to: `hot.md` + inbox + **one** `check_all_cadences.sh`; leave quarterly prompts to morning digest |
| warn | Cold MCP still registered globally (schema/attention tax) | Global: `cloudflare`×5, `stripe`, `stash`, `playwright`; OSINT: `obsidian-vault`, `mcp-legal-it`, `codebase-memory-mcp` (dup global), `chrome-devtools` | Disable or project-scope CF/Stripe; leave stash disabled; Playwright off (browser rule already prefers built-in); legal-it/obsidian on-demand |
| warn | lazy-tool catalog still indexes dead librarian paths | `.cursor/lazy-tool.yaml` sources `conductor` + `kb-server` → `ssh cemini-librarian`; catalog mtime Jun 18 | Drop dead sources; reindex; keep prod/exa/fetch only |
| warn | Premium multi-auditor / long parent sessions used where `/route` mid would pay | This pack itself; route skill says parent Cursor must not implement | Default: `/route` for impl+mechanical; Cursor premium for plan/architect + claim synthesis only |
| info | `state.vscdb` 4.3GB + agent-worker 1.2GB | Inventory disk lines; Cursor Support dir 6.3G | Disk/perf hygiene (vacuum/prune old chats); not per-turn tokens but slows restore and encourages huge transcript reattach |
| info | Search MCP overlap | Global `brave-search` + project `exa` (+ `fetch` direct and via lazy-tool) | Prefer Exa for research; Brave as fallback; one fetch path |

### Token waste map
1. **HIGH — alwaysApply stack (~33KB/turn when OSINT open)** — route×4 + federation rule dual-layer + 5KB adopt-wires negatives  
2. **HIGH — `CLAUDE.md` 28KB schema + ritual** — especially if agents re-read / obey 12 cadence checks every new chat  
3. **HIGH — cold MCP tool catalogs** — 5 Cloudflare servers + stripe + playwright + stash + legal/obsidian/chrome-devtools inflate discoverable tool surface  
4. **MED — skill inventory sprawl** — CF Workers skills, claude-red offensive packs, finance plugin skills discoverable far outside their domains  
5. **MED — staying in Cursor for mid work** — burns premium instead of claude-ds/`route-task`  
6. **MED — long agent transcripts / multi-auditor packs** — 18M transcripts folder; packed audits re-read inventory  
7. **LOW — `state.vscdb` 4.3GB** — disk/attention, not prompt tokens  
8. **LOW — duplicate `prod-mcp` direct + via lazy-tool** — small; keep one preferred path (lazy-tool)

### DeepSeek / claude-ds automation candidates
| Task | Why DeepSeek moves the needle | Keep Cursor premium |
|------|-------------------------------|---------------------|
| Mid-lane code/wiki mechanical edits via `/route` | Designed chain; always-approve; cheapest competent executor | Hard architecture, money, cross-wiki claim synthesis |
| `wiki_lint` / gap-detect fix drafts, `index.md` rows, `log.md` appends | Mechanical, local files, no secrets | Ingest takeaway discussion + human gates |
| Phase-0 clone audits (license/stars/layout) | Read-only explore scripts | GO/NO-GO judgment |
| Cadence runners + summarize due/not-due | Shell + short report; replaces ritual tool spam | Operator GO to actually run backtests |
| Skill/rule dedupe PRs (delete tipdrop twin, demote AA) | Boring file moves | Security review of MCP secret migration |
| Cloudflare Workers chores | Only when in CF project; use CF skills there | OSINT research sessions (disable CF MCP) |
| **Do not** offload | Secrets, LIVE Discord, Atto raw PII, Exa-paid deep research claims | Those stay gated / Cursor or human |

### Confidence
**high** on duplication math, cold MCP inventory, and ritual size; **medium** on exact per-turn tool-schema injection bytes (Cursor-internal); **high** that mid-lane `/route` + AA cleanup beats another premium auditor for spend.

### Unique angle
The tipdrop/cemini route twin is worse than “duplicate bytes”: it **cognitively re-centers TipDrop** on every turn while the skill text insists WorkDir must not default to TipDrop. You’re paying tokens to teach the model the wrong gravity well. Kill the twin, demote adopt-wires to globs, and replace the 12-step session ritual with one cadence script — that trio moves the needle more than pruning Cloudflare disk.