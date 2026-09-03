#!/usr/bin/env bash
# K175 Phase-0 — audit Integrate + Extract (no permanent install; no GPUOLOGY SaaS vendor).
# Clones → /tmp/k175-<slug>-audit ; report → .local/reports/k175-phase0-YYYY-MM-DD.md
# Cap: refuse clone dirs >500MB. CoreNLP model downloads are NEVER auto-fetched.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
REPORT_DIR="${ROOT}/.local/reports"
TODAY="$(date +%Y-%m-%d)"
REPORT="${REPORT_DIR}/k175-phase0-${TODAY}.md"
CAP_MB=500
mkdir -p "$REPORT_DIR"

repos=(
  "dhfbk/tint|Integrate|tint|GPL-3.0|Italian NLP / CoreNLP"
  "lucavandro/CodiceFiscaleJS|Extract|codice-fiscale-js|CC-BY-SA-4.0|comuni soppressi matrix"
  "censusreporter/censusreporter|Extract|censusreporter|MIT|US census staging schemas"
  "TimeMagazineLabs/babynames|Extract|babynames|MIT|SSA name frequency priors"
  "fivethirtyeight/data|Extract|fivethirtyeight-data|CC-BY-4.0|tidy sports/politics CSVs"
)

watch=(
  "newsapps/beeswithmachineguns|Watch|bees|MIT|AWS load swarm"
  "vbuterin/aztec_experiments|Watch|aztec|null|zk privacy experiments"
)

{
  echo "# K175 Phase-0 report — ${TODAY}"
  echo
  echo "Script: \`scripts/adopt_k175_phase0.sh\`"
  echo "Policy: shallow clone to \`/tmp/k175-*-audit\` only; no Desktop/family install; no npm/pip/brew from README; no CoreNLP model fetch."
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

for row in "${repos[@]}" "${watch[@]}"; do
  IFS='|' read -r repo _tier _slug _lic _note <<<"$row"
  audit_meta "$repo" >>"$REPORT" || echo "| ${repo} | ERROR | | | | |" >>"$REPORT"
done

{
  echo
  echo "## Shallow clones + failure-mode notes"
  echo
} >>"$REPORT"

clone_audit() {
  local repo="$1" slug="$2" tier="$3" note="$4"
  local dir="/tmp/k175-${slug}-audit"
  echo "=== ${repo} (${tier}) ==="
  if [[ -d "${dir}/.git" ]]; then
    echo "exists ${dir}"
  else
    rm -rf "$dir"
    git clone --depth 1 --single-branch "https://github.com/${repo}.git" "$dir"
  fi
  local mb
  mb=$(du -sm "$dir" | awk '{print $1}')
  echo "size_mb=${mb}"
  if (( mb > CAP_MB )); then
    echo "FAIL ${dir} ${mb}MB > ${CAP_MB}MB cap — removing"
    rm -rf "$dir"
    echo "| \`${repo}\` | ${tier} | **FAIL size** ${mb}MB | — | NO-GO clone |" >>"$REPORT"
    return 1
  fi

  # Failure-mode probes
  local notes=()
  if [[ "$slug" == "tint" ]]; then
    if rg -n -i "corenlp|stanford|download.*model|maven|gradle" "$dir" --glob '!*.jar' -g '!**/target/**' 2>/dev/null | head -20; then
      notes+=("CoreNLP/Maven deps present — models must NOT auto-download in Phase-0")
    fi
    notes+=("GPL-3.0 — private family OK; GPUOLOGY SaaS binary ship = NO-GO without compliance")
    notes+=("Java stack in Python-first family sprint — prefer JVM sidecar or skip")
  fi
  if [[ "$slug" == "codice-fiscale-js" ]]; then
    if rg -l -i "comuni|soppress|codiciCatastali|municipality" "$dir" 2>/dev/null | head -10; then
      notes+=("comune/soppressi data files present — Extract lookup tables")
    fi
    notes+=("CC-BY-SA-4.0 — sharealike if redistributing matrix in commercial kit")
  fi
  if [[ "$slug" == "censusreporter" ]]; then
    notes+=("Full web app — Extract schemas/API patterns only; do not run as genealogy SaaS")
  fi
  if [[ "$slug" == "babynames" ]]; then
    notes+=("US SSA bias — weak for Italian/Latin parish names; soft priors only")
  fi
  if [[ "$slug" == "fivethirtyeight-data" ]]; then
    notes+=("Static CSVs — structure > live feed; CC-BY attribution required")
  fi

  {
    echo "### \`${repo}\` — ${tier}"
    echo
    echo "- Clone: \`${dir}\` (${mb} MB)"
    echo "- Note: ${note}"
    for n in "${notes[@]:-}"; do echo "- ${n}"; done
    echo "- Top-level:"
    echo '```'
    ls -1 "$dir" | head -25
    echo '```'
    echo
  } >>"$REPORT"
}

# Watch: metadata only (no clone unless tiny)
{
  echo "## Watch (metadata only — no clone this run)"
  echo
  echo "- \`newsapps/beeswithmachineguns\` — aging AWS swarm; accidental self-DoS / bill risk → stay Watch"
  echo "- \`vbuterin/aztec_experiments\` — no SPDX; high regulatory friction → stay Watch"
  echo
  echo "## Clone audits (Integrate + Extract)"
  echo
} >>"$REPORT"

fail=0
for row in "${repos[@]}"; do
  IFS='|' read -r repo tier slug _lic note <<<"$row"
  if ! clone_audit "$repo" "$slug" "$tier" "$note"; then
    fail=1
  fi
done

{
  echo "## Verdicts (operator confirm)"
  echo
  echo "| Repo | Tier | Phase-0 verdict | Install path if GO |"
  echo "|------|------|-----------------|--------------------|"
  echo "| dhfbk/tint | Integrate | **CONDITIONAL-GO** — private family only; no CoreNLP model fetch until RAM measured; no SaaS vendor | \`~/Desktop/family/research/tools/tint\` after GO |"
  echo "| lucavandro/CodiceFiscaleJS | Extract | **GO (extract)** — copy comune tables / API patterns; do not npm-publish fork without SA review | private research / GPUOLOGY patterns |"
  echo "| censusreporter/censusreporter | Extract | **GO (extract)** — schema/API steal only | family US staging notes |"
  echo "| TimeMagazineLabs/babynames | Extract | **GO (extract)** — frequency tables as soft priors | entity-resolution pack |"
  echo "| fivethirtyeight/data | Extract | **GO (extract)** — tidy CSVs + attribution | CeminiDFS fixtures |"
  echo "| beeswithmachineguns | Watch | **NO-GO install** | — |"
  echo "| aztec_experiments | Watch | **NO-GO install** | — |"
  echo
  echo "## Supply chain"
  echo
  echo "- No \`npm i\` / \`pip install\` / \`brew\` from READMEs this run (K173)."
  echo "- Packages only if operator names them in a follow-up message."
  echo
} >>"$REPORT"

echo
echo "Report: ${REPORT}"
cat "$REPORT"
exit "$fail"
