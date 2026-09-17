#!/usr/bin/env bash
# OSINT K263 Phase-0 — SPDX-confirmed REFERENCE set only (shallow, --depth 1).
# Dual-ID: OSINT K263 = 17 Sep 2026 inbox (1 eval + 9 arXiv/PDF + Donny + 5 newsletters).
# 0 Integrate GO. NOASSERTION / AGPL / SIZE-SKIP / proprietary = no clone.
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

clone_ref "openjev" "https://github.com/TheoLeeCJ/openjev.git" "MIT"
clone_ref "jev-ultrafast" "https://github.com/browser-use/jev-ultrafast.git" "MIT"
clone_ref "BrowserSkill" "https://github.com/Tencent/BrowserSkill.git" "MIT"
clone_ref "data-formulator" "https://github.com/microsoft/data-formulator.git" "MIT"
clone_ref "jev-mcp" "https://github.com/jkudish/jev-mcp.git" "MIT"
clone_ref "knowledge-work-plugins" "https://github.com/anthropics/knowledge-work-plugins.git" "Apache-2.0"
clone_ref "ECC" "https://github.com/affaan-m/ECC.git" "MIT"
clone_ref "agent-lsd" "https://github.com/Golim/agent-lsd.git" "MIT"

echo "=== SKIP (documented) — no Integrate GO ==="
echo "nvidia/skillspector — already entity; no new clone; FILE bump; no skill auto-evolve"
echo "JustVugg/colibri — already Watch; no new clone"
echo "Tencent/WeKnora — NOASSERTION; NO-GO clone (K262 reaffirm)"
echo "TencentCloud/Octop — Pass; skip clone"
echo "cilium/cilium — Apache-2.0 SIZE-SKIP ~545MB; Pass"
echo "roboflow/supervision — MIT SIZE-SKIP ~4.3GB; reaffirm"
echo "coder/coder — AGPL-3.0 skip"
echo "n8n-io/n8n — NOASSERTION; NO-GO clone"
echo "anthropics/claude-code — proprietary Pass; already in use; do not vendor"
echo "theoephraim/awesome-cloudflare-selfhosted — FILE list; skip clone"
echo "ScienceIDE — no SPDX URL in PDF; no clone"
echo "=== DONE ==="
