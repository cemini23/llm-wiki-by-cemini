#!/usr/bin/env bash
# K224 Phase-0 clones (SPDX-verified; total << 500MB)
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
ADOPT="$ROOT/.local/adopts"
mkdir -p "$ADOPT"
clone() {
  local repo="$1" dest="$2"
  if [[ -d "$ADOPT/$dest/.git" ]]; then echo "exists $dest"; return; fi
  git clone --depth 1 "https://github.com/${repo}.git" "$ADOPT/$dest"
}
clone langchain-ai/deepagents deepagents
clone apisec-inc/AI-Surface AI-Surface
clone criptogus/HermesOffice HermesOffice
clone zhaoxuya520/reverse-skill reverse-skill
clone dreamhunter2333/cloudflare_temp_email cloudflare-temp-email
clone cloudflare/cloudflare-os cloudflare-os
du -sh \
  "$ADOPT/deepagents" \
  "$ADOPT/AI-Surface" \
  "$ADOPT/HermesOffice" \
  "$ADOPT/reverse-skill" \
  "$ADOPT/cloudflare-temp-email" \
  "$ADOPT/cloudflare-os"
echo "K224: khoj AGPL Watch no-clone; onyx NOASSERTION no-clone; autonomous-computer Context skip (~344MB)"
