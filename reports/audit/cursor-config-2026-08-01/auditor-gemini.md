### Verdict
WARN — Core OSINT workflow is functional, but duplicate rules, duplicate MCPs, and a 28KB CLAUDE.md create severe token bloat, while a 4.3GB state DB wastes disk space.

### Day-to-day keep list
*   **`lazy-tool`**: Essential proxy for `prod-mcp` health and dynamic tool loading.
*   **`exa`**: Core for external research and gap-fills.
*   **`github` MCP**: Required for repo ops and PRs.
*   **Built-in browser**: Preferred over Playwright for visual verification.
*   **`route` / `claude-ds`**: Critical for outsourcing tasks and saving premium tokens.
*   **`cemini-goal-skill.mdc` & `phase1-wire`**: Core workflow skills.
*   **`discord-ops`**: Needed for dry-run alerts.

### Findings
| Severity | Finding | Evidence | Fix |
|----------|---------|----------|-----|
| Critical | Massive token bloat from duplicate rules | `tipdrop-route-outsource.mdc` and `cemini-route-outsource.mdc` are identical (2220 bytes) and both exist in global AND local `.cursor/rules/` (4x injection). | Delete `tipdrop-route-outsource.mdc` globally and locally; rely on the single `cemini-route-outsource.mdc`. |
| High | Disk space exhaustion from Cursor state | `state.vscdb` is 4.3GB and `anysphere.cursor-agent-worker` is 1.2GB. | Clear Cursor workspace state/chat history (`state.vscdb`) to reclaim ~5.5GB. |
| High | Context window sink from `CLAUDE.md` | `CLAUDE.md` is 27.8KB and is always injected into the agent context. | Move static reference material from `CLAUDE.md` to wiki pages; keep only core schema routing. |
| Warn | Duplicate MCP server registration | `codebase-memory-mcp` is defined in both `~/.cursor/mcp.json` and `OSINT WORKSPACE/.cursor/mcp.json`. | Remove `codebase-memory-mcp` from the local OSINT `mcp.json` to prevent duplicate tool schemas. |
| Warn | Dead MCP path in `lazy-tool.yaml` | `kb-server` points to `ssh cemini-librarian` which is decommissioned. | Remove `kb-server` from `.cursor/lazy-tool.yaml` to prevent timeout/hangs during reindex. |
| Info | Cold/unused MCPs polluting context | `cloudflare-*` suite, `stripe`, `mcp-legal-it`, and `playwright` are loaded but rarely used. | Set `"disabled": true` for these servers in `mcp.json` until explicitly needed. |

### Token waste map
1. **High**: 4x injection of the identical route rule (`tipdrop-route-outsource.mdc` + `cemini-route-outsource.mdc` in both global and local).
2. **High**: 28KB `CLAUDE.md` + 25KB OSINT rules injected into every single prompt.
3. **Medium**: Duplicate tool schemas from `codebase-memory-mcp` being registered in both global and local MCP configs.
4. **Medium**: Tool schema bloat from cold/reference MCPs (Cloudflare suite, Stripe, Playwright, mcp-legal-it).
5. **Low**: Session ritual checks running on every turn.

### DeepSeek / claude-ds automation candidates
| Task | Why DeepSeek | When keep Cursor premium |
|------|--------------|--------------------------|
| Multi-model config audits | Read-only analysis fits DeepSeek's context window perfectly; saves expensive premium tokens. | When the auditor needs to actually execute edits/fixes across multiple files. |
| Routine wiki ingest & linting | Batch text processing and formatting have a low reasoning ceiling. | Complex synthesis requiring cross-domain context or architectural decisions. |
| Tier-2 arXiv sweeps | High volume text extraction and summarization; easily parallelized. | Final operator GO/NO-GO synthesis and strategy formulation. |
| Codebase/script refactoring | Cheap and highly capable for standard Python/Bash scripts. | Novel architecture, complex debugging, or when LIVE Discord ops are required. |

### Confidence
high

### Unique angle
`codebase-memory-mcp` is registered in **both** the global `~/.cursor/mcp.json` and the local OSINT `.cursor/mcp.json`. This forces Cursor to load the same MCP server twice, polluting the LLM's context window with duplicate tool schemas on every turn. Additionally, `lazy-tool.yaml` hardcodes absolute paths to `Desktop/OSINT WORKSPACE` for `conductor` and `exa`, which is brittle compared to using `${workspaceFolder}`.

**Analyzing Audit Requirements**

I've reviewed the audit prompt and related configurations. My current focus is dissecting the findings and understanding the precise output format expected. I'm preparing to deliver a concise verdict with a brief justification, followed by a breakdown of daily metrics.

**Refining Metric Details**

I'm now categorizing findings and prioritizing token waste. My thoughts are on mapping automation candidates and assigning confidence levels. I'm also looking for a unique, easily overlooked angle for the report.

**Identifying Token Waste**

I'm currently focused on optimizing token usage by identifying and eliminating redundancies. Specifically, I've found duplicate rule injections and a decommissioned path in `lazy-tool.yaml`. My next step is to address the substantial token bloat caused by large context files like `CLAUDE.md`.

**Addressing Disk & Context**

I'm now tackling significant disk bloat from `state.vscdb` and identifying unused MCPs like `cloudflare` and `stripe`. My focus is on minimizing context injection, especially the large `CLAUDE.md` file and redundant rule injections, to reduce token waste.

**Refining Tool Configuration**

I'm now comparing DeepSeek and Cursor's strengths for specific tasks. My focus is on DeepSeek for multi-model config audits and routine wiki ingest due to its efficient context window. I'm also exploring a unique angle related to a potential path mismatch in `lazy-tool.yaml` and an enabled but possibly unused local MCP.

**Detecting Configuration Conflicts**

I've identified a critical duplication in `codebase-memory-mcp` registration across global and local Cursor configurations. Additionally, I've pinpointed a brittle hardcoded path in `lazy-tool.yaml` that bypasses `${workspaceFolder}`, presenting a robust, unique angle for the report.

**Confirming Duplicate Registrations**

I've confirmed the duplicate `codebase-memory-mcp` registration in both global and local configurations. This exact duplication means the same MCP server is loading twice, unnecessarily inflating the context window with redundant tool schemas. I'm now ready to draft the findings.

**Finalizing Report Details**

I've confirmed the core issues: massive token bloat from duplicated route outsourcing rules and significant disk space usage from Cursor's state files. My focus is now on finalizing the critical and high severity findings for the report, ensuring a clear fix is provided for each.

**Finalizing Core Findings**

I've confirmed the primary issues: significant token bloat due to duplicated outsourcing rules and excessive disk usage from state files. I am now focusing on detailing these high-severity findings and proposing clear, actionable solutions for the report.

**Finalizing Severity Assessments**

I'm now assigning severity levels to the identified issues. The duplicate MCP registration and token bloat from redundant rules are critical. Medium concerns include schema bloat and session ritual checks, while low severity applies to other minor optimizations. I'm preparing to document these clearly.

**Refining Unique Angle**

I'm now combining the duplicate `codebase-memory-mcp` registration with the brittle hardcoded paths in `lazy-tool.yaml` for a robust unique angle. I'm ensuring the report clearly articulates how these issues inflate the context window and present deployment fragility.

