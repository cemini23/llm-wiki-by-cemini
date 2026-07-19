#!/usr/bin/env bash
# Wire K174 Extract tools into Cursor/TipDrop; optional Claude plugin.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
ADOPTS="${ROOT}/.local/adopts"
TIPDROP="${TIPDROP_ROOT:-/Users/claudiobarone/Desktop/projects/tipdrop-workspace-kit}"
REPORT="${ROOT}/.local/reports/k174-local-adopt.md"
mkdir -p "$(dirname "$REPORT")" "${ROOT}/.cursor/skills/i-have-adhd"

# i-have-adhd Cursor skill (already written by ingest) — refresh TipDrop
if [[ -d "$TIPDROP" ]]; then
  mkdir -p "${TIPDROP}/.cursor/skills/i-have-adhd"
  cp "${ROOT}/.cursor/skills/i-have-adhd/SKILL.md" "${TIPDROP}/.cursor/skills/i-have-adhd/SKILL.md"
  echo "OK TipDrop i-have-adhd skill"
fi

# code-review-graph: document MCP install path (operator may pip install)
CRG="${ADOPTS}/code-review-graph"
cat >"${ROOT}/scripts/run_code_review_graph_help.sh" <<'E2'
#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "Clone: ${ROOT}/.local/adopts/code-review-graph"
echo "Docs:  ${ROOT}/.local/adopts/code-review-graph/docs/USAGE.md"
echo "Typical: cd repo && pip install code-review-graph && code-review-graph --help"
echo "MCP: see upstream README for Cursor/Claude MCP server config"
E2
chmod +x "${ROOT}/scripts/run_code_review_graph_help.sh"

{
  echo "# K174 local adopt"
  echo "- Date: $(date -u +%Y-%m-%d)"
  echo "- Cap: 500MB/clone (user gate)"
  echo "- code-review-graph: $(du -sh "$CRG" 2>/dev/null | awk '{print $1}') MIT Extract"
  echo "- i-have-adhd: Cursor+TipDrop skill wired; optional Claude plugin"
  echo "- wigolo: Pass AGPL (no clone)"
  echo "- Weights: David PC only"
  echo ""
  echo "## Operator"
  echo "1. Claude Code: \`claude plugin marketplace add .local/adopts/i-have-adhd && claude plugin install i-have-adhd@i-have-adhd\` then \`/i-have-adhd\`"
  echo "2. Optional: pip install code-review-graph + MCP config for large-repo TipDrop/xsp work"
} >"$REPORT"
echo "Report $REPORT"
