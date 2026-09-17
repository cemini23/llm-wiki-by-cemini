# Cursor MCP — OSINT workspace

## Home vs this folder (why colors differ)

| Where you are | lazy-tool | stash | prod-mcp / exa / fetch |
|---------------|-----------|-------|-------------------------|
| **Cursor Home** (no folder) | Off / not listed | Global only — red if tunnel down | Not loaded |
| **OSINT WORKSPACE** open | Project — should be green | Global — green if tunnel up | Project servers |

**lazy-tool off at Home is correct.** Open **File → Open Folder → OSINT WORKSPACE** for wiki / conductor / kb / prod proxy tools.

**stash red at Home, green in OSINT:** usually the same global server — Home may have connected before the SSH tunnel finished. Fix:

```bash
curl -s -o /dev/null -w '%{http_code}\n' http://127.0.0.1:8088/sse   # expect 200
launchctl kickstart -k "gui/$(id -u)/com.cemini.stash-tunnel"
```

Then **Cursor Settings → MCP → stash → Retry** (or restart Cursor — see below).

---

## Reload Cursor after MCP changes

There is no separate “Developer: Reload” menu item in all builds. Use any of:

1. **Command Palette** (`Cmd+Shift+P`) → type **`Reload Window`** → run **Developer: Reload Window** (if shown) or **Reload Window**
2. **Cursor Settings → MCP** → **Retry** on each red server
3. **Quit Cursor completely** (`Cmd+Q`) and reopen — works every time; use this if MCP stays stale

---

## Project MCP (this folder)

**Turn lazy-tool ON:** `Cmd+Shift+J` → **Tools & MCP** → **lazy-tool** toggle → **On** (green).  
Cursor remembers this per machine. If it says **Off**, agents cannot reach kb-server / conductor — only prod/exa/fetch direct tools work.

| Server | Role |
|--------|------|
| **lazy-tool** | **Required — keep enabled** — conductor, kb-server, prod-mcp, fetch, exa (see `.cursor/rules/osint-mcp-defaults.mdc`) |
| **prod-mcp** | CeminiSuite prod (`:18002` tunnel) |
| **exa** | `scripts/mcp_exa.sh` → `~/.cemini/exa-api-key` |
| **fetch** | `mcp-fetch-server` |

## Global MCP (`~/.cursor/mcp.json`)

| Server | Role |
|--------|------|
| **stash** | Episodic memory `localhost:8088` |
| **brave-search** | Web search — `~/.local/bin/mcp-brave` + `~/.cemini/brave-api-key` |
| **playwright** | Browser automation (fallback; prefer built-in browser in chat) |
| **github** | PRs, issues, repos — `~/.local/bin/mcp-github` (official `github-mcp-server` stdio) |

Install / refresh **github**:

```bash
cd "/Users/claudiobarone/Projects/OSINT WORKSPACE"
./scripts/setup_cursor_github_mcp.sh
```

Token order: `GITHUB_PERSONAL_ACCESS_TOKEN` / `GITHUB_TOKEN` env → `~/.cemini/github-pat` → `gh auth token`. Never commit the PAT or put it in `mcp.json`. GUI Cursor does not inherit `~/.zshrc`.

No `librarian-stash` in this project (duplicate removed).

---

## Built-in browser + canvas (no extra MCP install)

| Capability | How |
|------------|-----|
| **Browser** | Cursor **built-in** `browser_*` tools in Agent chat (not Playwright by default). See `.cursor/rules/osint-visual-deliverables.mdc`. |
| **Canvas** | Agent writes `*.canvas.tsx` under the project canvases folder; open from chat sidebar. Skill: `~/.cursor/skills-cursor/canvas/SKILL.md`. Same rule file. |

Reload Cursor after first-time github MCP setup.

---

## Maintenance

```bash
curl -s -o /dev/null -w 'stash:%{http_code}\n' http://127.0.0.1:8088/sse   # often red after librarian decommission
curl -s -o /dev/null -w 'prod:%{http_code}\n' http://127.0.0.1:18002/mcp   # 406 = tunnel up

cd "/Users/claudiobarone/Projects/OSINT WORKSPACE"
lazy-tool reindex --config ".cursor/lazy-tool.yaml"
```

LaunchAgents: `com.cemini.prod-mcp-tunnel` (and optional `com.cemini.stash-tunnel` — stash may stay red; that is expected after librarian decommission 2026-06-14).

## Agent rules

- **OSINT folder:** `.cursor/rules/osint-mcp-defaults.mdc` (`alwaysApply: true`) — lazy-tool workflow
- **OSINT folder:** `.cursor/rules/osint-visual-deliverables.mdc` (`alwaysApply: true`) — built-in browser + canvas
- **All folders:** `~/.cursor/rules/cemini-projects.mdc` — which repo to open for which work

No extra rules in Cursor Settings UI are required if those `.mdc` files are present.

## Subagents

You do **not** need custom subagents per wiki. Use:

- **This agent** + lazy-tool + wiki for ingest/query/lint
- Cursor **Task** / explore subagent only for large codebase audits (optional)
- **Separate Open Folder** per repo (CeminiSuite vs OSINT vs sibling wikis) for the right `.cursor/mcp.json`

Sibling wikis (image-gen, seo, cybersec, ccc) live under `~/Projects/…` — open that wiki’s parent folder if you need project-specific MCP there.

## Secrets

- **Exa:** `~/.cemini/exa-api-key` or `EXA_API_KEY`
- **Brave:** `~/.cursor/mcp.json` only — never commit keys
