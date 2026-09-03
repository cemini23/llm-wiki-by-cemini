#!/usr/bin/env bash
# K177 Phase-0 — AGM Extract audit; OCR/AR/IE papers = Watch/Context (no clone).
# Clones → /tmp/k177-<slug>-audit ; report → .local/reports/k177-phase0-YYYY-MM-DD.md
# Cap: refuse clone dirs >500MB.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
REPORT_DIR="${ROOT}/.local/reports"
TODAY="$(date +%Y-%m-%d)"
REPORT="${REPORT_DIR}/k177-phase0-${TODAY}.md"
CAP_MB=500
mkdir -p "$REPORT_DIR"

{
  echo "# K177 Phase-0 report — ${TODAY}"
  echo
  echo "Script: \`scripts/adopt_k177_phase0.sh\`"
  echo "Policy: shallow clone to \`/tmp/k177-*-audit\` only; no Desktop install; no npm/pip/brew from README as trust root."
  echo
  echo "## Metadata (\`gh api\`)"
  echo
  echo "| Repo | SPDX | Stars | Size (KB) | Pushed | Archived |"
  echo "|------|------|-------|-----------|--------|----------|"
} >"$REPORT"

audit_meta() {
  local repo="$1"
  gh api "repos/${repo}" --jq '[.full_name, (.license.spdx_id // "null"), (.stargazers_count|tostring), (.size|tostring), .pushed_at, (.archived|tostring)] | @tsv' 2>/dev/null \
    | awk -F'\t' '{printf "| %s | %s | %s | %s | %s | %s |\n", $1, $2, $3, $4, $5, $6}'
}

audit_meta "agent-governance-manifest/agent-governance-manifest" >>"$REPORT" || echo "| agent-governance-manifest/agent-governance-manifest | ERROR | | | | |" >>"$REPORT"

{
  echo
  echo "## Shallow clones + failure-mode notes"
  echo
} >>"$REPORT"

dir="/tmp/k177-agm-audit"
echo "=== agent-governance-manifest (Extract) ==="
if [[ ! -d "${dir}/.git" ]]; then
  rm -rf "$dir"
  git clone --depth 1 --single-branch "https://github.com/agent-governance-manifest/agent-governance-manifest.git" "$dir"
fi
mb=$(du -sm "$dir" | awk '{print $1}')
echo "size_mb=${mb}"
if (( mb > CAP_MB )); then
  echo "FAIL ${dir} ${mb}MB > ${CAP_MB}MB cap — removing"
  rm -rf "$dir"
  echo "| \`agent-governance-manifest/agent-governance-manifest\` | Extract | **FAIL size** ${mb}MB | NO-GO |" >>"$REPORT"
  exit 1
fi

{
  echo "| \`agent-governance-manifest/agent-governance-manifest\` | Extract | ${mb}MB | MIT; \`.agm/\` + evidence validators; not AGENTS.md replacement; human maintainer authority |"
  echo
  echo "## Watch / Context (no clone)"
  echo
  echo "| Paper | Tier | Note |"
  echo "|-------|------|------|"
  echo "| 2607.15509 LLM-NAS HTR | Watch | Method only — genealogy contrast vs Transkribus; no GPT-5 NAS auto-loop |"
  echo "| 2607.15684 AR bugs | Context | Taxonomy for silent model-harness bugs |"
  echo "| 2607.15715 behavioral controllability | Context | Process-trace IE eval |"
  echo
  echo "## Verdict"
  echo
  echo "- **Extract:** AGM → CCC / federation agent-contribution gates (optional local adopt)."
  echo "- **No Integrate** this batch (do not force \`.agm/\` into CeminiSuite prod without operator GO)."
} >>"$REPORT"

echo "Wrote ${REPORT}"
