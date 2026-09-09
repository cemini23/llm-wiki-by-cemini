#!/usr/bin/env bash
# OSINT K258 Phase-0 — budget <500MB new clones (shallow, --depth 1).
# Dual-ID: OSINT K258 = 9 Sep 2026 inbox (1 eval + 8 arXiv + 9 newsletters).
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

clone_ref "execcritic" "https://github.com/MSR-Orchard/execcritic.git" "Apache-2.0"
clone_ref "E2B" "https://github.com/e2b-dev/E2B.git" "Apache-2.0"

echo "=== SKIP (documented) — no Integrate GO ==="
echo "keploy/keploy — Apache-2.0 Extract SIZE-SKIP ~232MB"
echo "facebook/infer — MIT Context SIZE-SKIP ~244MB"
echo "SonarSource/sonarqube — LGPL-3.0 SIZE-SKIP ~946MB"
echo "federico-busato/Modern-CPP-Programming — CC-BY-SA-4.0 SIZE-SKIP ~684MB"
echo "Tencent/teamai-cli — SPDX NOASSERTION; no clone"
echo "scrapfly/Antibot-Detector — SPDX NOASSERTION; no clone"
echo "kaandemir993/DarkTortilla-... — no PoC; cyber awareness only"
echo "earthtojake/text-to-cad / pascalorg/editor — 3D-print skip local wire"
echo "=== DONE ==="
