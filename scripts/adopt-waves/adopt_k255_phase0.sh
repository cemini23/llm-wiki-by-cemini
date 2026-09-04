#!/usr/bin/env bash
# OSINT K255 Phase-0 — budget <500MB new clones (shallow, --depth 1).
# Dual-ID: OSINT K255 = 4 Sep 2026 inbox (16 arXiv + 1 eval docx + 13 newsletters).
set -euo pipefail
export GIT_TERMINAL_PROMPT=0
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
AD="$ROOT/.local/adopts"
mkdir -p "$AD"
cd "$AD"

clone_ref() {
  local name="$1" url="$2" lic="$3"
  if [[ -d "$name" ]]; then
    echo "SKIP exists: $name"
    return 0
  fi
  echo "=== REFERENCE clone: $name ($lic) ==="
  git clone --depth 1 "$url" "$name"
}

clone_ref "AREX-Skill" "https://github.com/VectorSpaceLab/AREX-Skill.git" "Apache-2.0"
clone_ref "Deep-CFR-2025" "https://github.com/milecdav/Deep-CFR-2025.git" "MIT"
clone_ref "FalconFlank" "https://github.com/MSNightmare/FalconFlank.git" "MIT"

echo "=== SKIP (documented) — no Integrate GO without operator review ==="
echo "2609.02786 SafeEvolve — paper only; no verified runtime repo"
echo "2609.03660 LUGL — PokerRL/luglrl cited; Deep-CFR REFERENCE only"
echo "2609.03884 hook-update attack — extract-only policy pattern"
echo "2609.02393 CAPTCHA solvers — no product wire"
echo "=== DONE ==="
