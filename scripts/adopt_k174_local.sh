#!/usr/bin/env bash
# Wire K174 Extract tools into Cursor skills across federation workspaces.
# Cap: <500MB new clones (code-review-graph + i-have-adhd already cloned by phase0).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
ADOPTS="${ROOT}/.local/adopts"
TIPDROP="${TIPDROP_ROOT:-/Users/claudiobarone/Desktop/projects/tipdrop-workspace-kit}"
CCC="${CCC_ROOT:-/Users/claudiobarone/Projects/Cemini claude code CCC}"
REPORT="${ROOT}/.local/reports/k174-local-adopt.md"
SKILL_SRC="${ROOT}/.cursor/skills/i-have-adhd/SKILL.md"
SYNC="${CCC}/scripts/sync_federation_cursor_skills.sh"

mkdir -p "$(dirname "$REPORT")" "${ROOT}/.cursor/skills/i-have-adhd"

if [[ ! -f "$SKILL_SRC" ]]; then
  echo "FAIL missing ${SKILL_SRC}" >&2
  exit 1
fi

# TipDrop direct refresh (also covered by federation sync)
if [[ -d "$TIPDROP" ]]; then
  mkdir -p "${TIPDROP}/.cursor/skills/i-have-adhd"
  cp "$SKILL_SRC" "${TIPDROP}/.cursor/skills/i-have-adhd/SKILL.md"
  echo "OK TipDrop i-have-adhd skill"
fi

# User-global + all federation workspaces via CCC sync (includes i-have-adhd domain skill)
if [[ -x "$SYNC" ]]; then
  bash "$SYNC"
else
  echo "WARN federation sync missing: $SYNC — falling back to user-global only" >&2
  mkdir -p "${HOME}/.cursor/skills/i-have-adhd"
  cp "$SKILL_SRC" "${HOME}/.cursor/skills/i-have-adhd/SKILL.md"
  echo "OK user-global ~/.cursor/skills/i-have-adhd/"
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

# Verify skill present in key workspaces + user-global
fail=0
for dest in \
  "${HOME}" \
  "${ROOT}" \
  "${CCC}" \
  "${TIPDROP}" \
  "/Users/claudiobarone/Projects/Gambling wiki" \
  "/Users/claudiobarone/Desktop/projects/CeminiSuite"
do
  [[ -d "$dest" ]] || continue
  if [[ -f "${dest}/.cursor/skills/i-have-adhd/SKILL.md" ]]; then
    echo "OK verify ${dest}/.cursor/skills/i-have-adhd/"
  else
    echo "FAIL verify ${dest}/.cursor/skills/i-have-adhd/" >&2
    fail=$((fail + 1))
  fi
done

{
  echo "# K174 local adopt"
  echo "- Date: $(date -u +%Y-%m-%dT%H:%MZ)"
  echo "- Cap: 500MB/clone (user gate)"
  echo "- code-review-graph: $(du -sh "$CRG" 2>/dev/null | awk '{print $1}') MIT Extract (MCP optional)"
  echo "- i-have-adhd: federation Cursor skill (user-global + all workspaces via sync_federation_cursor_skills.sh)"
  echo "- wigolo: Pass AGPL (no clone)"
  echo "- Weights: David PC only"
  echo ""
  echo "## Operator"
  echo "1. Cursor: skill \`i-have-adhd\` available in every Open Folder workspace + Home (\`~/.cursor/skills/\`)"
  echo "2. Claude Code: \`claude plugin marketplace add .local/adopts/i-have-adhd && claude plugin install i-have-adhd@i-have-adhd\` then \`/i-have-adhd\`"
  echo "3. Re-sync after skill edits: \`bash \\\"${CCC}/scripts/sync_federation_cursor_skills.sh\\\"\`"
  echo "4. Optional: pip install code-review-graph + MCP for large-repo TipDrop/xsp reviews"
} >"$REPORT"
echo "Report $REPORT"
exit "$fail"
