#!/usr/bin/env bash
# Activate obsidian-second-brain for Cemini OSINT wiki (no bg agent, no stock init).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
VAULT="$ROOT/wiki"
SKILL="$HOME/.claude/skills/obsidian-second-brain"
SETTINGS="$HOME/.claude/settings.json"

echo "==> adopt_k92_phase0 (skills + setup.sh)"
bash "$ROOT/scripts/adopt_k92_phase0.sh"

echo "==> Cemini vault manual"
if [[ ! -f "$VAULT/_CLAUDE.md" ]]; then
  echo "ERROR: missing $VAULT/_CLAUDE.md — restore from git" >&2
  exit 1
fi

echo "==> Obsidian app vault chrome"
bash "$ROOT/scripts/setup_obsidian_vault.sh"

echo "==> SessionStart hook smoke test"
OUT=$(echo "{\"cwd\":\"$VAULT\"}" | OBSIDIAN_VAULT_PATH="$VAULT" python3 "$SKILL/hooks/load_vault_context.py")
echo "$OUT" | python3 -c "import sys,json; d=json.load(sys.stdin); print('OK inject', len(d['hookSpecificOutput']['additionalContext']), 'chars')"

echo "==> Background agent gate"
if jq -e '.env.OBSIDIAN_BG_AGENT_ENABLED == "1"' "$SETTINGS" 2>/dev/null; then
  echo "WARN: OBSIDIAN_BG_AGENT_ENABLED=1 — Cemini policy recommends OFF" >&2
else
  echo "OK bg agent inert (flag unset)"
fi

echo "==> Slash commands"
COUNT=$(ls "$HOME/.claude/commands"/obsidian-*.md 2>/dev/null | wc -l | tr -d ' ')
echo "OK $COUNT obsidian-* commands in ~/.claude/commands"

echo ""
echo "Active: SessionStart context + slash commands + wiki/_CLAUDE.md"
echo "Skipped: stock /obsidian-init, OBSIDIAN_BG_AGENT_ENABLED, cron"
echo "Optional: claude mcp add obsidian-vault (see setup.sh output)"
echo "Cursor: restart chat or open new agent session from OSINT WORKSPACE folder"
