#!/usr/bin/env bash
# OSINT K271 Phase-0 — two SPDX-confirmed REFERENCE clones only.
# Dual-ID: OSINT K271 = 24 Sep 2026 inbox. gh api 2026-09-24.
# 0 product Integrate GO. SPDX-null / size-skip / 404 / attack repo = no clone.
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

clone_ref "jev-curate" "https://github.com/AkashPriyadarshii/jev-curate.git" "MIT"
clone_ref "canny" "https://github.com/qkal/Canny.git" "MIT"

echo "=== SKIP (documented) — no product Integrate GO ==="
echo "hindsight MIT 758046 KB NO-CLONE"
echo "univer Apache 174006 KB NO-CLONE"
echo "Model-Optimizer Apache 149776 KB NO-CLONE"
echo "harness-sdk Apache 212322 KB NO-CLONE"
echo "jev-chat-jarvis MIT 20698 KB NO-CLONE"
echo "treg NOASSERTION 88763 KB NO-CLONE"
echo "google/ax Apache 44743 KB NO-CLONE"
echo "axe Apache 6086 KB NO-CLONE"
echo "learn-harness-engineering MIT 7254 KB skill text; no auto-evolve; NO-CLONE"
echo "ai-memory MIT 17776 KB NO-CLONE"
echo "apple-corelocation GPL-3.0 extract-only NO-CLONE"
echo "agent-desktop Apache 54976 KB NO-CLONE"
echo "typesafe-mario SPDX null NO-CLONE"
echo "jev-drone MIT 6842 KB NO-CLONE"
echo "OneVOneJev SPDX null NO-CLONE"
echo "neo4jev already prior FILE NO-CLONE"
echo "killmyidea SPDX null NO-CLONE"
echo "FluidUse Apache 48961 KB already SIZE-SKIP NO-CLONE"
echo "deleting-the-trace MIT 59 KB attack repo NO-CLONE"
echo "SkillGym MIT 221581 KB SIZE-SKIP NO-CLONE"
echo "InGuard Apache 804 KB image-gen NO-CLONE"
echo "Echo-Chamber 404 on 2026-09-24 NO-CLONE"
echo "=== DONE ==="
echo "0 product Integrate GO. FILE and HITL only. Do not swap /route."
echo "No product install. No weight download. Never auto-evolve skills."
echo "Keep the live jev path. Do not install Canny hooks."
echo "No xsp/pm scp. No LIVE Discord. Never npx github:. Never auto-arm."
