#!/usr/bin/env bash
# OSINT K262 Phase-0 — SPDX-confirmed REFERENCE set only (shallow, --depth 1).
# Dual-ID: OSINT K262 = 16 Sep 2026 inbox (1 eval + 10 arXiv/PDF + 12 newsletters).
# 0 Integrate GO. NOASSERTION / AGPL / SPDX-null / SIZE-SKIP = no clone.
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

clone_ref "security-audit-skill" "https://github.com/cloudflare/security-audit-skill.git" "MIT"
clone_ref "ScienceBuddy" "https://github.com/Gen-Verse/ScienceBuddy.git" "MIT"
clone_ref "open-code-review" "https://github.com/alibaba/open-code-review.git" "Apache-2.0"
clone_ref "oh-my-hermes" "https://github.com/rlaope/oh-my-hermes.git" "MIT"

echo "=== SKIP (documented) — no Integrate GO ==="
echo "LumosLab-Innovation/OpenHunterAI — NOASSERTION; NO-GO clone; FILE mention; no PoC"
echo "roboflow/supervision — MIT SIZE-SKIP ~4.3GB; FILE mention only; not product HTR"
echo "omkarcloud/google-maps-scraper — MIT; no clone (portal ToS / no mass unattended scrape)"
echo "fmzquant/strategies — SPDX null; NO-GO clone; FILE mention; no xsp scp"
echo "abue-ammar/tinycast — NOASSERTION; NO-GO clone"
echo "Tencent/WeKnora — NOASSERTION; NO-GO clone"
echo "multimodal-art-projection/YuE — Apache-2.0 OOD music; skip clone"
echo "debpalash/VoiceStudio — AGPL-3.0 skip; K261 reaffirm; no clone"
echo "ever-co/ever-gauzy — AGPL-3.0 skip; no clone"
echo "lnkiai/m3e-canvas — already K261 REFERENCE; no new clone"
echo "DefiLeoo/YOINK — FILE wiki-only; no pm scp; skip clone"
echo "=== DONE ==="
