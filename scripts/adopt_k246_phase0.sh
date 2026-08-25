#!/usr/bin/env bash
# OSINT K246 Phase-0 — budget <500MB new clones (shallow, --depth 1).
# License: .local/reports/license-spot-check-2026-08-25-0914.txt
# Dual-ID: OSINT K246 = this inbox (25 Aug 2026).
# 0 new runtime Integrate GO. Never trust eval docx SPDX.
set -euo pipefail
export GIT_TERMINAL_PROMPT=0
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
AD="$ROOT/.local/adopts"
mkdir -p "$AD"
cd "$AD"

clone() {
  local slug="$1" dest="$2"
  if [ -d "$dest/.git" ]; then echo "HAVE $dest"; du -sh "$dest"; return; fi
  echo "CLONE $slug -> $dest"
  git clone --depth 1 "https://github.com/${slug}.git" "$dest"
  du -sh "$dest"
}

# Extract clones (license-corrected from license-spot-check-2026-08-25-0914.txt)
clone Leonxlnx/unlazy unlazy                              # MIT lazy-loading
clone MemMachine/MemMachine MemMachine                    # Apache-2.0 agent memory REFERENCE
clone NVIDIA/garak garak                                  # Apache-2.0 LLM vuln scanner REFERENCE
clone BagelHole/DevOps-Security-Agent-Skills devops-security-agent-skills  # MIT cyber skills REFERENCE
clone virgiliojr94/book-to-skill book-to-skill            # MIT skill-from-book pattern
clone rawfilejson/awesome-osint-arsenal awesome-osint-arsenal  # MIT OSINT catalog REFERENCE
clone sooryathejas/METATRON METATRON                      # MIT agent framework WATCH

echo "=== SKIP (documented, license-spot-check-2026-08-25-0914.txt) ==="
echo "dnsglobe / nullframe — HAVE from K243"
echo "prime-agent — HAVE entity; paper K309 policy_wired; clone optional size check"
echo "Pentest-Swarm-AI / VaultS3 / Clone-Wars / FluxER / OpenOutreach — AGPL/GPL Extract-only, no clone"
echo "oxalpha / LLM4Pentest / emailosint / Auto-Company — null SPDX, no clone"
echo "ui-ux-pro-max-skill / MengTo/Skills — do not copy into ~/.cursor/skills (misevolution HITL)"
echo "nuclei* — MIT known; no duplicate clone unless cyber brief requests"
echo "=== DONE ==="

NEW=(unlazy MemMachine garak devops-security-agent-skills book-to-skill awesome-osint-arsenal METATRON)
for d in "${NEW[@]}"; do
  [ -d "$d" ] && du -sh "$d" 2>/dev/null || true
done
du -ch "${NEW[@]}" 2>/dev/null | tail -1 || true
