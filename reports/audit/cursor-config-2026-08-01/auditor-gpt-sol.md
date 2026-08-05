### Verdict
FAIL — plaintext credentials, dead MCP paths, and roughly 16k tokens of overlapping baseline instructions need remediation.

### Day-to-day keep list
- Global `github` MCP, after credential rotation.
- Project `lazy-tool`, restricted to `prod-mcp`.
- Project `exa` for external research.
- Built-in browser/WebFetch instead of Playwright, Chrome DevTools, Brave, and fetch MCP.
- `route` skill; retain only one short global trigger rule.
- `agent-setup-supply-chain.mdc` as alwaysApply.
- A shortened `osint-mcp-defaults.mdc` covering wiki-first, prod routing, and safety boundaries.
- `fable-advisor`; optionally `i-have-adhd` if actively used.

### Findings
| Severity | Finding | Evidence | Fix |
|---|---|---|---|
| critical | Live credentials are stored in plaintext | `~/.cursor/mcp.json:18-25` contains Brave and GitHub credentials | Rotate both immediately. Replace literals with `${env:BRAVE_API_KEY}` and `${env:GITHUB_TOKEN}`, or a Keychain-backed wrapper. Never commit/copy this file. |
| warn | Route policy is injected four times | Global and project copies of both `cemini-route-outsource.mdc` and identical `tipdrop-route-outsource.mdc`; each ≈2.2KB | Delete both `tipdrop-*` files and both project route copies. Keep one global rule shortened to trigger, safety, and executor contract; leave details in `route/SKILL.md`. |
| warn | Other policies are duplicated globally and locally | Security, goal, and Phase-1 rules exist in both scopes | Keep one source only. Demote security, goal, and Phase-1 rules to `alwaysApply: false`; their descriptions/skills provide invocation. |
| warn | Dead services remain indexed | `.cursor/lazy-tool.yaml:12-24` references conductor and deleted `cemini-librarian` | Remove both source blocks. Reindex lazy-tool afterward. |
| warn | MCP surface is substantially over-enabled | Nine project and twelve global servers; most are documented COLD | Default-disable cold servers listed below and enable only for the relevant session. |
| warn | Global Claude hooks inject OSINT vault behavior into every session | `~/.claude/settings.json:6-30` runs Obsidian hooks on SessionStart/PostCompact | Remove global hooks or move them into an OSINT-specific launcher/settings profile. |
| warn | Eleven globally enabled plugins create irrelevant discovery/context | `~/.claude/settings.json:32-43` | Globally disable finance bundles, visual-explainer, harness, and claude-mem. Enable through task-specific profiles. |
| info | `CLAUDE.md` mixes schema with recurring runtime rituals | 27.8KB file; pack identifies session checks as a repeated sink | Preserve schema, but move cadence commands and historical architecture into referenced docs. Keep a 2–4KB operational entrypoint. |
| info | Cursor state storage is abnormally large | `state.vscdb` 4.3GB; agent worker 1.2GB | Close Cursor, back up state, use Cursor’s chat/history cleanup first. If unresolved, rename—not blindly delete—`state.vscdb` and allow recreation. Clear agent-worker cache only while Cursor is closed. |

Concrete MCP defaults:

- In project `.cursor/mcp.json`, keep enabled: `lazy-tool`, `exa`.
- Set `"disabled": true`: `prod-mcp` (reachable through lazy-tool), `fetch`, `obsidian-vault`, `codebase-memory-mcp`, `discord-ops`, `chrome-devtools`, `mcp-legal-it`.
- In global `~/.cursor/mcp.json`, keep enabled: `github`.
- Default-disable: `playwright`, `brave-search`, `codebase-memory-mcp`, all five Cloudflare servers, `stash`, `atto`, `stripe`.
- Enable `atto`, Stripe, Cloudflare, legal, or Discord only for explicitly relevant sessions. Discord remains dry-run unless LIVE OK.
- In `.cursor/lazy-tool.yaml`, retain only `prod-mcp`; remove conductor, kb-server, fetch, and exa. Direct Exa already exists.

Rules to demote to agent-requestable (`alwaysApply: false`):

- `cemini-cursor-security-preflight.mdc`
- `cemini-goal-skill.mdc`
- `cemini-phase1-policy-wires.mdc`
- `osint-phase1-adopt-wires.mdc`
- `osint-visual-deliverables.mdc`
- global `cemini-projects.mdc`

Keep alwaysApply:

- `agent-setup-supply-chain.mdc`
- shortened `osint-mcp-defaults.mdc`
- one concise global route trigger

### Token waste map
1. **High:** 27.8KB `CLAUDE.md` + 24.5KB project rules + 12.8KB global rules: approximately 16k tokens before task context.
2. **High:** Four route copies consume ≈8.9KB, roughly 2.2k tokens, while the full skill remains available separately.
3. **Medium-high:** MCP tool discovery across 21 configured entries, including five Cloudflare endpoints and duplicate codebase-memory.
4. **Medium:** SessionStart vault injection and PostCompact background processing on unrelated repositories.
5. **Medium:** Eleven globally enabled Claude plugins; finance/UI/harness skills are cold for ordinary wiki work.
6. **Low token / high disk:** 4.3GB Cursor state database and 1.2GB worker cache. Primarily storage/startup cost, not prompt tokens.

### DeepSeek / claude-ds automation candidates
| Task | Why DeepSeek | Keep Cursor premium when |
|---|---|---|
| Wiki lint, frontmatter repair, backlink symmetry | Mechanical and readily verified | Conflicts require semantic judgment |
| Daily cadence checks and report formatting | Deterministic shell/report workflow | A report changes trading posture |
| Digest extraction and source-page scaffolding | Repetitive Markdown generation | Sources contain PII or sensitive documents |
| Rule/MCP inventory and duplicate detection | Mostly parsing and comparison | Deciding security boundaries |
| Brief audits and stale-tag queues | Static checks with clear outputs | Evidence must be adjudicated |
| Test/lint execution and failure summaries | Cheap tool execution | Failures imply architecture changes |
| Routine git diff summaries and release notes | Low-risk summarization | Money, production, or legal changes |
| Lazy-tool reindex verification and health snapshots | Command-driven and reversible | Production remediation is requested |

Use `claude-ds --bare` for mechanical jobs where possible, passing only required files. Never send secrets, raw Atto PII, live Discord payloads, financial credentials, or unredacted MCP configuration.

### Confidence
High — based on the complete audit pack and direct inspection of both MCP configurations, lazy-tool catalog, route contract, Claude settings, plugin inventory, and rule frontmatter.

### Unique angle
The largest avoidable cost is not a single plugin: it is **policy multiplication**. Route behavior exists as a skill plus four alwaysApply copies. Converting policies into small trigger rules with detailed skill bodies preserves behavior while removing thousands of recurring tokens.