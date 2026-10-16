#!/usr/bin/env bash
# OSINT K292 Phase-0 — tool-eval wave (2026-10-16).
#
# The eval docx tiers two repos Integrate while recording their licence as NOT
# FOUND. This script reads every licence with `gh api` FIRST, so an Integrate
# decision cannot survive an unread licence, then clones the on-topic set.
#
# Requires network and `gh` auth. Run in the Terminal panel, not the agent sandbox.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
DEST="$ROOT/.local/adopts/k292"
BUDGET_KB=500000

echo "=== K292 Phase-0 — Multi-Wiki Repository Link Evaluation, 20 URLs ==="
echo "Priority: #1 Atto | #2 GuruWatcher + Basgiath | #3 CeminiDFS | #4 CeminiParlays"
echo "Docx tiers: Integrate 2 | Extract 6 | Watch 1 | Context 5 | Pass 6 | UNAVAILABLE 0"
mkdir -p "$DEST"

# repo<TAB>docx_tier<TAB>docx_licence_claim
ROWS=$(cat <<'EOF'
morluto/leantoken	integrate	NOT FOUND
morluto/flameox	integrate	NOT FOUND
xerj-org/xerj	extract	Apache-2.0
CapSoftware/Cap	extract	AGPL-3.0
frankbria/parallel-cc	extract	MIT
morluto/jacobian	extract	NOT FOUND
morluto/smokinggun	extract	MIT
lightseekorg/tokenspeed	watch	MIT
richiemcilroy/Tov	context	MIT
frankbria/auto-author	context	MIT
EOF
)

echo
echo "=== LICENCE VERIFICATION (gh api) — never trust the eval docx ==="
printf '%-28s %-10s %-14s %s\n' REPO TIER DOCX_CLAIM ACTUAL_SPDX
while IFS=$'\t' read -r repo tier claim; do
  [ -z "$repo" ] && continue
  actual=$(gh api "repos/$repo" --jq '.license.spdx_id // "NONE"' 2>/dev/null || echo "API-ERROR")
  printf '%-28s %-10s %-14s %s\n' "$repo" "$tier" "$claim" "$actual"
done <<< "$ROWS"

echo
echo "=== THE FINDING THIS RUN EXISTS TO CHECK ==="
echo "Both docx Integrate rows record licence NOT FOUND:"
echo "  morluto/leantoken   tier Integrate, revenue 'high, now', licence NOT FOUND"
echo "  morluto/flameox     tier Integrate, revenue 'high, now', licence NOT FOUND"
echo "The docx's own friction note says to verify the morluto SPDX strings before"
echo "redistribution. If either reads NONE / NOASSERTION above, DO NOT treat it as"
echo "Integrate. Record the reading and keep the tier at Extract."

echo
echo "=== CLONES (depth 1, budget ${BUDGET_KB}KB total) ==="
TOTAL=0
clone() {
  local repo="$1" name="${1##*/}"
  if [ -d "$DEST/$name" ]; then echo "  skip (exists) $name"; return 0; fi
  git clone --depth 1 --quiet "https://github.com/$repo.git" "$DEST/$name" 2>/dev/null || {
    echo "  FAILED $repo"; return 0; }
  local kb
  kb=$(du -sk "$DEST/$name" | cut -f1)
  TOTAL=$((TOTAL + kb))
  echo "  cloned $name (${kb}KB)"
}

# Integrate tier first, then the Extract tier that is on-topic. Each clone is a
# READ unless a product brief says otherwise.
for r in morluto/leantoken morluto/flameox; do clone "$r"; done
for r in xerj-org/xerj CapSoftware/Cap frankbria/parallel-cc morluto/jacobian morluto/smokinggun; do
  clone "$r"
done

echo
echo "=== TOTAL CLONE FOOTPRINT: ${TOTAL}KB (budget ${BUDGET_KB}KB) ==="
if [ "$TOTAL" -gt "$BUDGET_KB" ]; then
  echo "WARNING: over budget — prune before adopting."
  echo "  Measured 2026-10-16: 745404KB. xerj (275112KB) and Cap (324280KB) dominate."
  echo "  The 500000KB budget was set before those two were sized."
fi

echo
echo "=== NOT CLONED, and why ==="
echo "paperinstruments.com (Ultramarine) — a website, not a repo; API is proprietary"
echo "richiemcilroy/Tov, frankbria/auto-author, frankbria/codeframe      — Context tier"
echo "richiemcilroy/chippytea, frankbria/auto-modeler-evolve, sprintforge — Pass tier"
echo "N0zoM1z0/vocaloid-mcp, th08, th095  — off-topic (song synthesis, game reconstruction)"
echo "MakazhanAlpamys/Kaspi-Analytics-Platform, Permit-Forge             — off-topic"
echo "lightseekorg/tokenspeed             — Watch: MCP server dependency chain unresolved"

echo
echo "=== BOUNDARY ==="
echo "Cap is AGPL-3.0 on the main tree — isolate, never vendor into a product."
echo "Clones are REFERENCE data only. No install into prod. No scrape."
echo "Game-reconstruction repos (th08, th095): technique reference only, no assets."
echo "0 product Integrate GO this wave. FILE and HITL only."
echo "No xsp/pm scp. Never auto-arm. No watches.json write."
echo "=== DONE ==="
