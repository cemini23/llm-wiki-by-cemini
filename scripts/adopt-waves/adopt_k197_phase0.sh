#!/usr/bin/env bash
# K197 Phase-0 — clone license-clean Integrate only (OpenCLI + t3code).
# GPL (netdata/amnezia) and Watch (redis/meili) are NOT cloned here.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
ADOPT="$ROOT/.local/adopts"
mkdir -p "$ADOPT"
cd "$ADOPT"

clone() {
  local url="$1" dir="$2"
  if [[ -d "$dir/.git" ]]; then
    echo "exists $dir"
    return 0
  fi
  git clone --depth 1 "$url" "$dir"
}

clone https://github.com/jackwener/OpenCLI.git opencli
clone https://github.com/pingdotgg/t3code.git t3code

du -sh opencli t3code 2>/dev/null || true
echo "K197 Phase-0 done under $ADOPT"
