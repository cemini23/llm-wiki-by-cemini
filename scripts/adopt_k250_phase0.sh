#!/usr/bin/env bash
# OSINT K250 Phase-0 — budget <500MB new clones (shallow, --depth 1).
# Dual-ID: OSINT K250 = 29 Aug 2026 inbox (3 arXiv + 2 eval docx + 2 PDF notes).
# 0 new runtime Integrate GO. Never trust eval docx SPDX — verify via gh api.
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

# arXiv GO REFERENCE
clone google-research/reasoning-bank reasoning-bank
clone bingreeky/JIT JIT

echo "=== SKIP (documented) ==="
echo "abi/screenshot-to-code — K248 shelf"
echo "ComposioHQ/awesome-claude-skills — catalog only; no clone"
echo "addyosmani/agent-skills — federation skills; no duplicate clone"
echo "WikiSkill 2608.27454 — no public SPDX repo at Phase-0"
echo "grok_loop_engineering_note_HQ.pdf — operator PDF; no clone"
echo "harness_final.pdf — anonymous ReportLab note; no clone"
echo "eval links.docx — empty stub"
echo "=== DONE ==="

NEW=(reasoning-bank JIT)
for d in "${NEW[@]}"; do
  [ -d "$d" ] && du -sh "$d" 2>/dev/null || true
done
du -ch "${NEW[@]}" 2>/dev/null | tail -1 || true
