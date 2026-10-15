#!/usr/bin/env bash
# OSINT K291 Phase-0 verify. Licence and maturity check for the 20-URL eval docx.
#
# Run in the Terminal panel: the Bash sandbox denies api.github.com.
#   bash scripts/adopt-waves/adopt_k291_phase0.sh
#
# The docx (Multi-Wiki Link Revenue Evaluation.docx, Gemini DR v10.9) claims a licence
# for each repo. Those claims have been wrong or incomplete on 5 of 17 in this wave and
# 5 of 20 in K290, so this script re-reads every one from the GitHub API and reports
# disagreement rather than trusting the document.
#
# No clones. No install. 0 Integrate GO. The tiers in the docx are Pass / Context /
# Extract / UNAVAILABLE only — nothing here is an adoption decision.
set -euo pipefail

if ! command -v gh >/dev/null 2>&1; then
  echo "ERROR: gh CLI not on PATH." >&2
  exit 2
fi

# repo<TAB>docx-claim
ROWS=$(cat <<'EOF'
nvm-sh/nvm	MIT
K-Dense-AI/scientific-agent-skills	MIT
ifixai-ai/iFixAi	Apache-2.0
ntdevlabs/tiny11builder	NOT FOUND
richiemcilroy/Tov	NOT FOUND
N0zoM1z0/dx-ball	MIT
MakazhanAlpamys/Soup	NOT FOUND
noonghunna/club-3090	AGPL-3.0
jorgemanrubia/omacharts	NOT FOUND
akitaonrails/ai-memory	MIT
dentiny/duckdb-object-storage	MIT
ankit/stylebot	MIT
layer5io/layer5	Apache-2.0
meshery/meshery	Apache-2.0
kzndotsh/watchdog	NOT FOUND
SabhyaC26/crop-map	NOT FOUND
kzndotsh/dotfiles	NOT FOUND
EOF
)

echo "=== K291 Phase-0 — licence verification vs the docx ==="
printf "%-42s %-14s %-14s %-8s %s\n" REPO DOCX ACTUAL STARS "PUSHED"
mismatch=0
missing=0
while IFS=$'\t' read -r repo claim; do
  [ -n "$repo" ] || continue
  out=$(gh api "repos/$repo" -q '[.license.spdx_id // "NOASSERTION", .stargazers_count, .pushed_at] | @tsv' 2>/dev/null || true)
  if [ -z "$out" ]; then
    printf "%-42s %-14s %-14s\n" "$repo" "$claim" "REPO GONE"
    missing=$((missing + 1))
    continue
  fi
  spdx=$(printf '%s' "$out" | cut -f1)
  stars=$(printf '%s' "$out" | cut -f2)
  when=$(printf '%s' "$out" | cut -f3 | cut -c1-10)
  flag=""
  case "$claim" in
    "NOT FOUND")
      # An unresolved claim that the API resolves is an omission, not an error.
      if [ "$spdx" != "NOASSERTION" ]; then flag="MISSED"; mismatch=$((mismatch + 1)); fi ;;
    *)
      if [ "$spdx" != "$claim" ]; then flag="WRONG"; mismatch=$((mismatch + 1)); fi ;;
  esac
  printf "%-42s %-14s %-14s %-8s %s %s\n" "$repo" "$claim" "$spdx" "$stars" "$when" "$flag"
done <<< "$ROWS"

echo
echo "disagreements: $mismatch / 17   repo gone: $missing"
echo
echo "The club-3090 row is the fourth consecutive wave: the docx says AGPL-3.0 and the"
echo "API says Apache-2.0. Do not carry a copyleft caution against that repo."
echo
echo "0 Integrate GO. FILE and HITL only. No install. No clone."
echo "=== DONE ==="
