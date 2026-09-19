#!/usr/bin/env bash
# OSINT K265 Phase-0 — SPDX-confirmed REFERENCE set only (shallow, --depth 1).
# Dual-ID: OSINT K265 = 19 Sep 2026 inbox (2 evals folded + LS + SecPro + WuBlock).
# 0 product Integrate GO. NOASSERTION / AGPL / SIZE-SKIP / SPDX-null / 404 = no clone.
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

clone_ref "jev-rules" "https://github.com/EliaAlberti/jev-rules.git" "MIT"
clone_ref "jev-codex-router" "https://github.com/0xNatoshi/jev-codex-router.git" "MIT"
clone_ref "SkillOpt" "https://github.com/microsoft/SkillOpt.git" "MIT"
clone_ref "tax-doc-classifier" "https://github.com/kyotofin/tax-doc-classifier.git" "Apache-2.0"
clone_ref "classifier-dev" "https://github.com/mrmps/classifier-dev.git" "MIT"
clone_ref "claude-reflect" "https://github.com/BayramAnnakov/claude-reflect.git" "MIT"

echo "=== SKIP (documented) — no product Integrate GO ==="
echo "jkudish/jev-mcp — already cloned; laptop MCP WIRE; never npx github"
echo "TheoLeeCJ/openjev — already cloned; FILE"
echo "fatwang2/awesome-jev — MIT list; skip clone"
echo "yibie/awesome-jev — SPDX null; NO-GO clone"
echo "convaiinnovations/laya — 404; NO-GO clone; LS FILE only"
echo "trycua/cua — SIZE-SKIP ~483MB; FILE mention HITL"
echo "Continuum-AI-Corp/OrcaPromptVault — AGPL skip"
echo "krillinai/OpenCreator — SPDX null; NO-GO clone"
echo "Sahil-SS9/hermes-project-stewardship — NOASSERTION; NO-GO clone"
echo "zhengkid/Dream-RSI — SPDX null; NO-GO clone"
echo "typesafe-ai/jev — proprietary; already using via jev-mcp"
echo "=== DONE ==="
