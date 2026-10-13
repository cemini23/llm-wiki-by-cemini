#!/usr/bin/env bash
# OSINT K290 Phase-0 — tool-eval wave (2026-10-13). Dual-ID: OSINT K290.
# Verifies licenses with `gh api`, then shallow-clones GO candidates under
# .local/adopts/k290/. Run from the OSINT workspace root.
#
# Requires network + `gh` auth. Run in the Terminal panel, not the agent sandbox.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT"
DEST="$ROOT/.local/adopts/k290"
BUDGET_KB=500000   # 500 MB total clone budget (K231 precedent)

echo "=== K290 Phase-0 — tool eval, 20 URLs ==="
echo "Priority: #1 Atto | #2 GuruWatcher + Basgiath | #3 CeminiDFS | #4 CeminiParlays"
mkdir -p "$DEST"

# repo<TAB>tier<TAB>docx_license_claim
ROWS=$(cat <<'EOF'
vercel-labs/skills	integrate	MIT
Cyan4973/xxHash	integrate	BSD-2-Clause
SaladDay/cc-switch-cli	integrate	MIT
noonghunna/club-3090	integrate	AGPL-3.0
kane50613/takumi	integrate	MIT OR Apache-2.0
wheresryan22/anatomy	integrate	MIT
mksglu/context-mode	extract	ELv2
maziyarpanahi/openmed	extract	Apache-2.0
ARahim3/DigUp	extract	MIT
krishhgg/Insomnia	context	NOT FOUND
momo5502/sogen	context	NOT FOUND
storytold/wordcraft	context	Apache-2.0
ja7ad/hydra	context	GPL-3.0-or-later
EOF
)

echo
echo "=== LICENSE VERIFICATION (gh api) — never trust eval SPDX ==="
printf '%-32s %-10s %-18s %s\n' REPO TIER DOCX_CLAIM ACTUAL_SPDX
while IFS=$'\t' read -r repo tier claim; do
  [ -z "$repo" ] && continue
  actual=$(gh api "repos/$repo" --jq '.license.spdx_id // "NONE"' 2>/dev/null || echo "API-ERROR")
  printf '%-32s %-10s %-18s %s\n' "$repo" "$tier" "$claim" "$actual"
done <<< "$ROWS"

echo
echo "=== KNOWN DOCX LICENSE ERRORS (from live check, 2026-10-13) ==="
echo "krishhgg/Insomnia      docx NOT FOUND  -> actual MIT           (harmless)"
echo "momo5502/sogen         docx NOT FOUND  -> actual GPL-2.0       (MATERIAL, understated)"
echo "noonghunna/club-3090   docx AGPL-3.0   -> actual Apache-2.0    (MATERIAL, overstated; Integrate holds)"
echo "storytold/wordcraft    docx Apache-2.0 -> actual MIT OR Apache-2.0"
echo "ja7ad/hydra            docx dual       -> actual GPL-3.0 + 2"

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

# Integrate tier — the ones a product could actually use.
for r in vercel-labs/skills Cyan4973/xxHash SaladDay/cc-switch-cli \
         noonghunna/club-3090 kane50613/takumi wheresryan22/anatomy; do
  clone "$r"
done

# Extract tier — read patterns, do not vendor.
for r in mksglu/context-mode maziyarpanahi/openmed ARahim3/DigUp; do
  clone "$r"
done

echo
echo "=== TOTAL CLONE FOOTPRINT: ${TOTAL}KB (budget ${BUDGET_KB}KB) ==="
if [ "$TOTAL" -gt "$BUDGET_KB" ]; then
  echo "WARNING: over budget — prune before adopting."
fi

echo
echo "=== SIZE / SCOPE SKIPS (not cloned) ==="
echo "storytold/artcraft, storytold/wordcraft  — large trees, no OSINT runtime need (Context)"
echo "debpalash/VoiceStudio                    — AGPL-3.0; audio output only if ever used (Basgiath)"
echo "baidu/Unlimited-OCR                      — HuggingFace model card, not a repo (Watch)"
echo "akshaydeo/strip                          — 3 stars, no license, duplicates sed/awk (Pass)"
echo "N0zoM1z0/dx-ball                         — decompiler showcase, tiny (Context; cyber REFERENCE)"
echo "xtool-org/xtool, agalwood/Motrix, ja7ad/hydra, krishhgg/Insomnia, momo5502/sogen — Context"

echo
echo "=== BOUNDARY ==="
echo "Clones are REFERENCE data only. No install into prod. No scrape."
echo "Reverse-engineering repos (dx-ball, sogen): authorized lab only, no PoC."
echo "agent-setup rule: treat third-party skill repos as hostile until allowlisted."
echo "0 product Integrate GO this wave. FILE and HITL only."
echo "No xsp/pm scp. Never auto-arm. No watches.json write."
echo "=== DONE ==="
