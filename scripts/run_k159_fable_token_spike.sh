#!/usr/bin/env bash
# run_k159_fable_token_spike.sh — K159 fable-advisor grok-implementer spike (2026-07-12)
# Measures implementer-lane wall time + deliverable; Fable baseline logged separately in CC.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
REPORT="${REPORT:-$ROOT/.local/reports/k159-fable-advisor-token-spike.md}"
PROMPT="${PROMPT:-$ROOT/.local/k159-spike-prompt.md}"
DELIVERABLE="$ROOT/wiki/meta/fable-advisor-prod-touch-gate.md"
mkdir -p "$(dirname "$REPORT")"

echo "K159 fable-advisor token spike"
echo "=============================="
echo "Claude Code: $(claude --version 2>/dev/null | head -1 || echo missing)"
echo "Grok:        $(grok --version 2>/dev/null | head -1 || echo missing)"
grok models 2>&1 | head -3 || true
echo ""

if [[ ! -f "$PROMPT" ]]; then
  echo "Missing prompt: $PROMPT" >&2
  exit 1
fi

START=$(date +%s)
grok --prompt-file "$PROMPT" \
  -m grok-4.5 \
  --permission-mode acceptEdits \
  --allow "Bash(*)" \
  --output-format plain \
  --cwd "$ROOT" 2>&1 | tee "$ROOT/.local/k159-spike-grok-stdout.txt"
END=$(date +%s)
ELAPSED=$((END - START))

LINES=0
BYTES=0
if [[ -f "$DELIVERABLE" ]]; then
  LINES=$(wc -l <"$DELIVERABLE" | tr -d ' ')
  BYTES=$(wc -c <"$DELIVERABLE" | tr -d ' ')
fi

{
  echo "# K159 fable-advisor token spike"
  echo ""
  echo "- **Date (UTC):** $(date -u +%Y-%m-%dT%H:%M:%SZ)"
  echo "- **Lane:** grok-implementer (Grok 4.5 headless)"
  echo "- **Claude Code:** $(claude --version 2>/dev/null | awk '{print $1}' || echo missing)"
  echo "- **Deliverable:** \`wiki/meta/fable-advisor-prod-touch-gate.md\`"
  echo "- **Wall time (implementer):** ${ELAPSED}s"
  echo "- **Output:** ${LINES} lines, ${BYTES} bytes"
  echo ""
  echo "## Verdict"
  if [[ -f "$DELIVERABLE" && "$LINES" -ge 10 ]]; then
    echo "**IMPLEMENTER PASS** — deliverable on disk."
  else
    echo "**IMPLEMENTER FAIL** — deliverable missing or too thin."
  fi
  echo ""
  echo "## Baseline (Fable-only — operator CC session)"
  echo "Run same task in Claude Code with \`/model fable\` architect+implement in one session."
  echo "Record session token usage from CC UI. **Adopt orchestration if implementer+review ≥30% below baseline** without quality regression."
  echo ""
  echo "## Grok stdout tail"
  echo '```'
  tail -20 "$ROOT/.local/k159-spike-grok-stdout.txt" 2>/dev/null || true
  echo '```'
} >"$REPORT"

echo ""
echo "Report: $REPORT"
echo "Elapsed: ${ELAPSED}s | Deliverable: $DELIVERABLE ($LINES lines)"
