#!/usr/bin/env bash
# OSINT K267 Phase-0 — SPDX-confirmed REFERENCE set only (shallow, --depth 1).
# Dual-ID: OSINT K267 = 20 Sep 2026 inbox (2 evals + WuBlock Asia TOP10).
# 0 product Integrate GO. NOASSERTION / AGPL / GPL / SIZE-SKIP / SPDX-null = no clone.
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

clone_ref "openjev-razorback" "https://github.com/razorback16/openjev.git" "Apache-2.0"
clone_ref "winnow" "https://github.com/GhalebDweikat/winnow.git" "MIT"
clone_ref "foreman" "https://github.com/thruwire/foreman.git" "MIT"
clone_ref "typesafe-mcp" "https://github.com/itsmostafa/typesafe-mcp.git" "MIT"
clone_ref "pi-jev" "https://github.com/y0usaf/pi-jev.git" "MIT"
clone_ref "jev-desktop" "https://github.com/yikangy873-gif/jev-desktop.git" "MIT"

echo "=== SKIP (documented) — no product Integrate GO ==="
echo "TheoLeeCJ/openjev — already cloned as openjev; FILE canonical sibling"
echo "jkudish/jev-mcp — already cloned; laptop MCP WIRE; never npx github"
echo "jkudish/jev-browser — already cloned HITL cassette; skip Ying-Kai-Liao/jev-browser"
echo "bespokelabsai/nimble — SPDX null; NO-GO clone; FILE mention"
echo "Heman10x-NGU/openJev-verdict-2.0 — NOASSERTION; NO-GO clone; FILE mention"
echo "mizorewww/laya-mlx — Apache-2.0 FILE mention; eval Integrate OVERRIDE FILE; skip clone ~5.7MB"
echo "Sac-Y/Jev-cu — SPDX null; NO-GO clone; HITL cassette only"
echo "Anil-matcha/awesome-jev-by-typesafe — MIT list; skip clone"
echo "uehaj/jev-semgrep — NOASSERTION; NO-GO clone; cyber FILE; no PoC"
echo "burnigtm/jev-mcp — MIT fork FILE; never replace live mcp-jev; skip clone"
echo "TheoLeeCJ/SemIf — already FILE K265; skip clone"
echo "jixserver/free-for-dev — SPDX null; NO-GO clone"
echo "kerpopule/hermes-jev-skills — MIT FILE; no skill auto-evolve; skip clone"
echo "AbdelStark/awesome-typesafe — MIT list; skip clone"
echo "gakonst/evm-bend — SPDX null; NO-GO clone"
echo "BuilderIO/agent-native — SIZE-SKIP ~343MB + SPDX null; FILE mention HITL review UI"
echo "Open-Dev-Society/OpenStock — AGPL-3.0 extract-only; no clone"
echo "jexp/neo4jev — MIT FILE mention kinship; skip clone ~6.5MB; no auto-merge truth.ged"
echo "ellipsis-dev/blink — SPDX null; NO-GO clone"
echo "reticlehq/reticle — SIZE-SKIP + NOASSERTION; no clone"
echo "TianyuCodings/NanoJev — SIZE-SKIP ~62MB; FILE mention; no uncensored-weight pull"
echo "win4r/jev-skill-suggester — MIT FILE; no skill auto-evolve; skip clone"
echo "jarrodwatts/jev-trader — MIT FILE mention; skip clone; never orders; never auto-arm"
echo "typesafe-ai/skills — MIT FILE; no skill auto-evolve; skip clone"
echo "irfndi/prism-liquidity-agent — MIT FILE mention; skip clone; no pm scp"
echo "scadastrangelove/awesome-ai-security-tools — NOASSERTION; NO-GO clone; cyber FILE; no PoC"
echo "paperless-ngx/paperless-ngx — GPL-3.0 extract-only SIZE-SKIP; no clone"
echo "ikermoel/open-alternative-jev — Apache-2.0 FILE mention lab Watch; skip clone"
echo "=== DONE ==="
