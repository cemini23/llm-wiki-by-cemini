#!/usr/bin/env bash
# notebooklm_export_brief.sh — redacted brief → NotebookLM notebook (K84 workflow).
#
# Creates a sanitized copy under /tmp/ and prints next steps for notebooklm CLI.
# Does NOT upload automatically (operator confirms auth + topic).
#
# Usage:
#   bash scripts/notebooklm_export_brief.sh briefs/2026-05-30_k84-world-cup-conviction-v4-lp-safety-cemini.md

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
BRIEF="${1:-}"

if [[ -z "$BRIEF" || ! -f "$BRIEF" ]]; then
  echo "Usage: $0 briefs/<file>.md" >&2
  exit 1
fi

SLUG=$(basename "$BRIEF" .md)
SANITIZED="/tmp/cemini-nlm-export-${SLUG}.md"
TODAY=$(date +%Y-%m-%d)

# Strip lines that might carry secrets (conservative)
grep -Ev 'sk-[A-Za-z0-9_-]{20,}|5\.161\.|PRIVATE KEY|api[_-]?key|\.env' "$BRIEF" > "$SANITIZED" || cp "$BRIEF" "$SANITIZED"

echo "Sanitized export: $SANITIZED"
echo ""
echo "Next steps (see .cursor/skills/notebooklm-osint-bridge/SKILL.md):"
echo "  notebooklm auth check --test --json"
echo "  notebooklm create \"OSINT ${SLUG} ${TODAY}\""
echo "  notebooklm source add -n <NOTEBOOK_ID> --file \"${SANITIZED}\""
echo "  notebooklm audio create -n <NOTEBOOK_ID>   # optional podcast overview"

if command -v notebooklm >/dev/null 2>&1; then
  if notebooklm auth check --test --json 2>/dev/null | grep -q '"status": "ok"'; then
    echo ""
    echo "Auth OK — run create/add manually or pass --auto to future version"
  else
    echo ""
    echo "Run: notebooklm login"
  fi
fi
