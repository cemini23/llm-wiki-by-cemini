#!/usr/bin/env bash
# K229 Phase-0 — GitHub Revenue Opportunity Evaluation.docx clones (<500MB).
# Never trust eval SPDX — gh api already verified MIT for these.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
ADOPTS="${ROOT}/.local/adopts"
mkdir -p "$ADOPTS"
cd "$ADOPTS"

clone_shallow() {
  local repo="$1" dir="$2"
  if [[ -d "$dir/.git" ]]; then
    echo "EXISTS $dir"
    return 0
  fi
  echo "CLONE $repo -> $dir"
  git clone --depth 1 "https://github.com/${repo}.git" "$dir"
  du -sh "$dir"
}

# Integrate / Extract / Watch (size-safe)
clone_shallow "shift-labs-ai/pi-rlm" "pi-rlm"
clone_shallow "HarrierOnChain/Prediction-Markets-Trading-Bot-Toolkits" "pm-trading-bot-toolkits"
clone_shallow "pikpikcu/airecon" "airecon"
clone_shallow "AWeirdDev/flights" "flights"
clone_shallow "serengil/deepface" "deepface"

# LifeOS ~456MB — under 500MB cap
clone_shallow "danielmiessler/LifeOS" "LifeOS"

echo "=== SKIP (documented, not cloned) ==="
echo "servo/servo ~1.9GB SIZE-SKIP"
echo "EpicStaff/EpicStaff NOASSERTION NO-GO"
echo "FUXA GPL+size (prior K228 skip)"
echo "cert-manager/layer5/Bannerlord/… Pass/Context wiki-only"

echo "=== DONE ==="
du -sh pi-rlm pm-trading-bot-toolkits airecon flights deepface LifeOS 2>/dev/null
