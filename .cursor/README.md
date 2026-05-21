# Cursor MCP — OSINT workspace

## What loads here (project scope)

| Server | Role |
|--------|------|
| **lazy-tool** | Default tool surface — proxies conductor, kb-server, prod-mcp, fetch, exa |
| **prod-mcp** | CeminiSuite prod stack (requires tunnel on `:18002`) |
| **exa** | External research (`~/.cemini/exa-api-key` or `EXA_API_KEY`) |
| **fetch** | URL → markdown (`mcp-fetch-server`) |

## What loads globally (`~/.cursor/mcp.json`)

| Server | Role |
|--------|------|
| **stash** | Episodic memory at `localhost:8088` (librarian tunnel) |
| **brave-search** | Web search (`BRAVE_API_KEY` in that file — keep local, do not commit) |
| **playwright** | Browser automation |

**No duplicate stash:** this project does not define `librarian-stash`; use global **stash** only.

## After clone or tunnel reboot

```bash
# Tunnels (LaunchAgents should auto-start at login)
curl -s -o /dev/null -w 'stash:%{http_code}\n' http://127.0.0.1:8088/sse
curl -s -o /dev/null -w 'prod:%{http_code}\n' http://127.0.0.1:18002/mcp

# Rebuild lazy-tool catalog (from repo root)
lazy-tool reindex --config ".cursor/lazy-tool.yaml"
```

Then **Cursor Settings → MCP → Retry** on any red server, or **Developer: Reload Window**.

## Secrets

- **Exa:** `scripts/mcp_exa.sh` reads `~/.cemini/exa-api-key` (same as Claude Code / arXiv sweep).
- **Brave:** only in `~/.cursor/mcp.json` — never copy API keys into committed files.
- Copy `mcp.json.example` → `mcp.json` and fix absolute paths if you work on another machine.
