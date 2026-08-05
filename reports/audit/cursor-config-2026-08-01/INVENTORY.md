# Cursor config inventory — 2026-08-01

## Disk / state
6.3G	/Users/claudiobarone/Library/Application Support/Cursor
4.3G	/Users/claudiobarone/Library/Application Support/Cursor/User/globalStorage/state.vscdb
1.2G	/Users/claudiobarone/Library/Application Support/Cursor/User/globalStorage/anysphere.cursor-agent-worker
 75M	/Users/claudiobarone/Library/Application Support/Cursor/User/globalStorage/anysphere.cursor-retrieval
 14M	/Users/claudiobarone/Library/Application Support/Cursor/User/globalStorage/conversation-search.db
7.0M	/Users/claudiobarone/Library/Application Support/Cursor/User/globalStorage/state.vscdb-wal
6.0M	/Users/claudiobarone/Library/Application Support/Cursor/User/globalStorage/conversation-search.db-wal
496K	/Users/claudiobarone/Library/Application Support/Cursor/User/globalStorage/mcp-oauth-attempts
104K	/Users/claudiobarone/Library/Application Support/Cursor/User/globalStorage/anysphere.cursor-mcp
 32K	/Users/claudiobarone/Library/Application Support/Cursor/User/globalStorage/state.vscdb-shm
 32K	/Users/claudiobarone/Library/Application Support/Cursor/User/globalStorage/conversation-search.db-shm
491M	/Users/claudiobarone/.cursor

## Global MCP (~/.cursor/mcp.json)
servers: ['playwright', 'brave-search', 'github', 'codebase-memory-mcp', 'cloudflare', 'cloudflare-docs', 'cloudflare-bindings', 'cloudflare-builds', 'cloudflare-observability', 'stash', 'atto', 'stripe']

## OSINT project MCP
servers: ['lazy-tool', 'prod-mcp', 'exa', 'fetch', 'obsidian-vault', 'codebase-memory-mcp', 'discord-ops', 'chrome-devtools', 'mcp-legal-it']

## Global rules (~/.cursor/rules)
cemini-cursor-security-preflight.mdc
cemini-goal-skill.mdc
cemini-phase1-policy-wires.mdc
cemini-projects.mdc
cemini-route-outsource.mdc
tipdrop-route-outsource.mdc

## OSINT rules (alwaysApply + count)
      11
agent-setup-supply-chain.mdc
cemini-cursor-security-preflight.mdc
cemini-goal-skill.mdc
cemini-phase1-policy-wires.mdc
cemini-route-outsource.mdc
osint-ingest-gates.mdc
osint-mcp-defaults.mdc
osint-phase1-adopt-wires.mdc
osint-visual-deliverables.mdc
osint-workflow-operators.mdc
tipdrop-route-outsource.mdc

## OSINT skills
adopted-geo-tools
cemini-wiki-graph
cemini-wiki-ingest
cursor-audit
discord-ops
goal
grill-with-docs
i-have-adhd
notebooklm-osint-bridge
phase1-wire
route
searchos-progress
super-audit
to-issues
ui-skills

## User-global skills
adopted-geo-tools
agents-sdk
cloudflare
cloudflare-email-service
cloudflare-one
cloudflare-one-migrations
cursor-audit
durable-objects
goal
grill-with-docs
i-have-adhd
phase1-wire
route
sandbox-sdk
super-audit
to-issues
turnstile-spin
web-perf
workers-best-practices
wrangler

## Claude Code plugins (cache top)
fable-advisor
finance-skills
harness-marketplace
thedotmack
visual-explainer-marketplace

## Hooks
/Users/claudiobarone/.claude/settings.json
hooks keys ['PostCompact', 'SessionStart']

## CLAUDE.md / AGENTS sizes
   27809 /Users/claudiobarone/Projects/OSINT WORKSPACE/CLAUDE.md
   27809 total
     775 /Users/claudiobarone/Projects/OSINT WORKSPACE/.cursor/rules/agent-setup-supply-chain.mdc
     813 /Users/claudiobarone/Projects/OSINT WORKSPACE/.cursor/rules/cemini-goal-skill.mdc
    1106 /Users/claudiobarone/Projects/OSINT WORKSPACE/.cursor/rules/cemini-cursor-security-preflight.mdc
    2038 /Users/claudiobarone/Projects/OSINT WORKSPACE/.cursor/rules/cemini-phase1-policy-wires.mdc
    2048 /Users/claudiobarone/Projects/OSINT WORKSPACE/.cursor/rules/osint-visual-deliverables.mdc
    2146 /Users/claudiobarone/Projects/OSINT WORKSPACE/.cursor/rules/osint-workflow-operators.mdc
    2220 /Users/claudiobarone/Projects/OSINT WORKSPACE/.cursor/rules/cemini-route-outsource.mdc
    2220 /Users/claudiobarone/Projects/OSINT WORKSPACE/.cursor/rules/tipdrop-route-outsource.mdc
    2329 /Users/claudiobarone/Projects/OSINT WORKSPACE/.cursor/rules/osint-ingest-gates.mdc
    3814 /Users/claudiobarone/Projects/OSINT WORKSPACE/.cursor/rules/osint-mcp-defaults.mdc
    5019 /Users/claudiobarone/Projects/OSINT WORKSPACE/.cursor/rules/osint-phase1-adopt-wires.mdc
   24528 total

## alwaysApply rules (frontmatter)
ALWAYS: /Users/claudiobarone/Projects/OSINT WORKSPACE/.cursor/rules/agent-setup-supply-chain.mdc (     775 bytes)
ALWAYS: /Users/claudiobarone/Projects/OSINT WORKSPACE/.cursor/rules/cemini-cursor-security-preflight.mdc (    1106 bytes)
ALWAYS: /Users/claudiobarone/Projects/OSINT WORKSPACE/.cursor/rules/cemini-goal-skill.mdc (     813 bytes)
ALWAYS: /Users/claudiobarone/Projects/OSINT WORKSPACE/.cursor/rules/cemini-phase1-policy-wires.mdc (    2038 bytes)
ALWAYS: /Users/claudiobarone/Projects/OSINT WORKSPACE/.cursor/rules/cemini-route-outsource.mdc (    2220 bytes)
ALWAYS: /Users/claudiobarone/Projects/OSINT WORKSPACE/.cursor/rules/osint-mcp-defaults.mdc (    3814 bytes)
ALWAYS: /Users/claudiobarone/Projects/OSINT WORKSPACE/.cursor/rules/osint-phase1-adopt-wires.mdc (    5019 bytes)
ALWAYS: /Users/claudiobarone/Projects/OSINT WORKSPACE/.cursor/rules/osint-visual-deliverables.mdc (    2048 bytes)
ALWAYS: /Users/claudiobarone/Projects/OSINT WORKSPACE/.cursor/rules/tipdrop-route-outsource.mdc (    2220 bytes)
ALWAYS: /Users/claudiobarone/.cursor/rules/cemini-cursor-security-preflight.mdc (    1106 bytes)
ALWAYS: /Users/claudiobarone/.cursor/rules/cemini-goal-skill.mdc (     813 bytes)
ALWAYS: /Users/claudiobarone/.cursor/rules/cemini-phase1-policy-wires.mdc (    1875 bytes)
ALWAYS: /Users/claudiobarone/.cursor/rules/cemini-projects.mdc (    4597 bytes)
ALWAYS: /Users/claudiobarone/.cursor/rules/cemini-route-outsource.mdc (    2220 bytes)
ALWAYS: /Users/claudiobarone/.cursor/rules/tipdrop-route-outsource.mdc (    2220 bytes)

## route / claude-ds
/Users/claudiobarone/.local/bin/claude-ds
claude-ds - DeepSeek Claude Code (model=deepseek-v4-flash)
Install: /Users/claudiobarone/.deepseek-claude
Permissions: --dangerously-skip-permissions (route always-approve default)
Usage: claude [options] [command] [prompt]

Claude Code - starts an interactive session by default, use -p/--print for
non-interactive output

Arguments:
  prompt                                            Your prompt

Options:
  --add-dir <directories...>                        Additional directories to allow tool access to
  --agent <agent>                                   Agent for the current session. Overrides the 'agent' setting.
  --agents <json>                                   JSON object defining custom agents (e.g. '{"reviewer": {"description": "Reviews code", "prompt": "You are a code reviewer"}}')
  --allow-dangerously-skip-permissions              Enable bypassing all permission checks as an option, without it being enabled by default. Recommended only for sandboxes with no internet access.
  --allowedTools, --allowed-tools <tools...>        Comma or space-separated list of tool names to allow (e.g. "Bash(git *) Edit")
  --append-system-prompt <prompt>                   Append a system prompt to the default system prompt
  --bare                                            Minimal mode: skip hooks, LSP, plugin sync, attribution, auto-memory, background prefetches, keychain reads, and CLAUDE.md auto-discovery. Sets CLAUDE_CODE_SIMPLE=1. Anthropic auth is strictly ANTHROPIC_API_KEY or apiKeyHelper via --settings (OAuth and keychain are never read). 3P providers (Bedrock/Vertex/Foundry) use their own credentials. Skills still resolve via /skill-name. Explicitly provide context via: --system-prompt[-file], --append-system-prompt[-file], --add-dir (CLAUDE.md dirs), --mcp-config, --settings, --agents, --plugin-dir.
  --betas <betas...>                                Beta headers to include in API requests (API key users only)

## security preflight latest
lrwxr-xr-x@ 1 claudiobarone  staff  64 Jul 31 09:16 /Users/claudiobarone/.cursor/security-preflight/latest -> /Users/claudiobarone/.cursor/security-preflight/20260731T131604Z
## Rule byte totals
OSINT alwaysApply rules:    24528
User-global alwaysApply:    12831
OSINT CLAUDE.md:    27809

## Duplicate route rules

## MCP json sizes
    1754 /Users/claudiobarone/.cursor/mcp.json
    2089 /Users/claudiobarone/Projects/OSINT WORKSPACE/.cursor/mcp.json
    3843 total

## Global MCP server details

## settings.json keys
['cursor.agent.autoRun', 'cursor.agent.autoRunAllowlist', 'remote.SSH.remotePlatform', 'update.releaseTrack', 'window.autoDetectColorScheme']
...
len 5

## AGENTS.md / .cursorrules
none

## Claude plugins enabled
/Users/claudiobarone/.claude/plugins/installed_plugins.json
{
  "version": 2,
  "plugins": {
    "claude-mem@thedotmack": [
      {
        "scope": "user",
        "installPath": "/Users/claudiobarone/.claude/plugins/cache/thedotmack/claude-mem/13.12.4",
        "version": "13.12.4",
        "installedAt": "2026-05-11T02:23:56.569Z",
        "lastUpdated": "2026-07-25T23:04:58.168Z",
        "gitCommitSha": "68b077f7f79fdbcc98fb0445a9b9ceebf0070d22"
      }
    ],
    "finance-market-analysis@finance-skills": [
      {
        "scope": "user",
        "installPath": "/Users/claudiobarone/.claude/plugins/cache/finance-skills/finance-market-analysis/9.1.0",
        "version": "9.1.0",
        "installedAt": "2026-05-11T02:46:36.559Z",
        "lastUpdated": "2026-07-21T21:40:34.895Z",
        "gitCommitSha": "fa526ce0011800896e78037ffa0302ed54a3d94f"
      }
    ],
    "finance-social-readers@finance-skills": [
      {
        "scope": "user",
        "installPath": "/Users/claudiobarone/.claude/plugins/cache/finance-skills/finance-social-readers/9.1.0",
        "version": "9.1.0",
        "installedAt": "2026-05-11T02:46:36.565Z",
        "lastUpdated": "2026-07-21T21:40:34.891Z",
        "gitCommitSha": "fa526ce0011800896e78037ffa0302ed54a3d94f"
      }
    ],
    "finance-data-providers@finance-skills": [
      {
        "scope": "user",
        "installPath": "/Users/claudiobarone/.claude/plugins/cache/finance-skills/finance-data-providers/9.1.0",
        "version": "9.1.0",
        "installedAt": "2026-05-11T02:46:36.570Z",
        "lastUpdated": "2026-07-21T21:40:34.892Z",
        "gitCommitSha": "fa526ce0011800896e78037ffa0302ed54a3d94f"
      }
    ],
    "finance-startup-tools@finance-skills": [
      {
        "scope": "user",
        "installPath": "/Users/claudiobarone/.claude/plugins/cache/finance-skills/finance-startup-tools/9.1.0",
        "version": "9.1.0",
        "installedAt": "2026-05-11T02:46:36.572Z",
        "lastUpdated": "2026-07-21T21:40:34.887Z",
        "gitCommitSha": "fa526ce0011800896e78037ffa0
## lazy-tool.yaml head
# Workspace lazy-tool catalog — used by Cursor MCP (see .cursor/mcp.json).
# Rebuild after tunnel changes:
#   lazy-tool reindex --config .cursor/lazy-tool.yaml
#   bash scripts/lazy_tool_enrich_prod_health.sh   # polymarket/stream health FTS aliases
app:
  name: lazy-tool-osint

storage:
  sqlite_path: ".cursor/lazy-tool-catalog.db"

sources:
  - id: "conductor"
    type: server
    transport: stdio
    command: "python3"
    args:
      - "/Users/claudiobarone/Desktop/OSINT WORKSPACE/conductor/mcp_server.py"
  - id: "kb-server"
    type: server
    transport: stdio
    command: "ssh"
    args:
      - "cemini-librarian"
      - "cd /opt/cemini-wiki && KB_TOOL_ALLOWLIST=kb_search,kb_search_smart,kb_context,kb_read,kb_list,kb_vault_status,kb_safety_check node /opt/kb-server/src/mcp.js"
  - id: "prod-mcp"
    type: server
    transport: http
    url: "http://localhost:18002/mcp"
  # stash: SSE-only — use global ~/.cursor/mcp.json "stash" (not lazy-tool-indexable)
  - id: "fetch"
    type: server
    transport: stdio
    command: "npx"
    args:
      - "-y"
      - "mcp-fetch-server"
  - id: "exa"
    type: server
    transport: stdio
    command: "/Users/claudiobarone/Desktop/OSINT WORKSPACE/scripts/mcp_exa.sh"
