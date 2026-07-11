#!/usr/bin/env bash
# adopt_k159_local.sh — laptop install for K159 fable-advisor (2026-07-11)
set -euo pipefail

REPORT="${REPORT:-$(dirname "$0")/../.local/reports/k159-fable-advisor-local-adopt.md}"
mkdir -p "$(dirname "$REPORT")"

echo "K159 local adopt — fable-advisor"
echo "================================"

CC_VER="$(claude --version 2>/dev/null | awk '{print $1}' || echo missing)"
echo "Claude Code: $CC_VER (plugin wants ≥2.1.170)"

if ! claude plugin list 2>/dev/null | grep -q 'fable-advisor@fable-advisor'; then
  echo "Installing fable-advisor plugin..."
  claude plugin marketplace add DannyMac180/fable-advisor
  claude plugin install fable-advisor@fable-advisor
else
  echo "OK: fable-advisor plugin present"
  claude plugin marketplace update fable-advisor 2>/dev/null || true
  claude plugin update fable-advisor@fable-advisor 2>/dev/null || true
fi

GROK_STATUS="missing"
if command -v grok >/dev/null 2>&1; then
  GROK_STATUS="installed ($(
    grok --version 2>/dev/null | head -1 || echo version-unknown
  ))"
fi

CODEX_STATUS="missing"
if command -v codex >/dev/null 2>&1; then
  CODEX_STATUS="installed ($(
    codex --version 2>/dev/null | head -1 || echo version-unknown
  ))"
fi

{
  echo "# K159 fable-advisor local adopt"
  echo ""
  echo "- **Date:** $(date -u +%Y-%m-%d)"
  echo "- **Plugin:** fable-advisor@fable-advisor (user scope, enabled)"
  echo "- **Claude Code:** $CC_VER"
  echo "- **Grok lane:** $GROK_STATUS — install from https://x.ai/cli + \`grok login\` for default implementer"
  echo "- **Codex lane:** $CODEX_STATUS — GPT-5.6 Sol implementer when authenticated"
  echo "- **Session:** \`/model fable\` (or \`/model opus\` if no Fable on plan)"
  echo "- **Wiki:** @entities/tools/fable-advisor.md"
  echo "- **Prod brief:** briefs/xsp-2026-07-11_k159-fable-advisor-orchestration-steal.md (scp'd)"
  echo ""
  echo "## Smoke"
  echo ""
  echo "1. Open OSINT WORKSPACE in Claude Code; \`/model fable\`"
  echo "2. Delegate one wiki lint fix via orchestration skill; log token delta vs baseline"
  echo "3. Install Grok CLI before relying on grok-implementer lane"
} >"$REPORT"

echo ""
echo "Grok CLI:  $GROK_STATUS"
echo "Codex CLI: $CODEX_STATUS"
echo "Report:    $REPORT"
echo "Done."
