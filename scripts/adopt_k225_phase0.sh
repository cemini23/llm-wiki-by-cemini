#!/usr/bin/env bash
# K225 Phase-0 clones (SPDX-verified; target << 500MB new)
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
ADOPT="$ROOT/.local/adopts"
mkdir -p "$ADOPT"
clone() {
  local repo="$1" dest="$2"
  if [[ -d "$ADOPT/$dest/.git" ]]; then echo "exists $dest"; return; fi
  echo "cloning $repo -> $dest"
  git clone --depth 1 "https://github.com/${repo}.git" "$ADOPT/$dest"
}
# Atto Integrate / Extract
clone virgiliojr94/book-to-skill book-to-skill
clone superlinked/sie sie
clone zubair-trabzada/ai-sales-team-claude ai-sales-team-claude
clone zosmaai/pi-llm-wiki pi-llm-wiki
# Cyber / local-abliterated-lab Extract
clone shepherd-agents/shepherd shepherd
clone huangruiteng/loopx loopx
# GuruWatcher Watch
clone mubeng/mubeng mubeng
# CCC / xsp Extract
clone HKUDS/DeepCode DeepCode
# Tiny refresh
clone kepano/obsidian-skills obsidian-skills

echo "=== sizes ==="
du -sh \
  "$ADOPT/book-to-skill" \
  "$ADOPT/sie" \
  "$ADOPT/ai-sales-team-claude" \
  "$ADOPT/pi-llm-wiki" \
  "$ADOPT/shepherd" \
  "$ADOPT/loopx" \
  "$ADOPT/mubeng" \
  "$ADOPT/DeepCode" \
  "$ADOPT/obsidian-skills" 2>/dev/null
echo "K225 NO-GO: ScienceClaw NULL; bountyforge NULL; Argus NULL; Wan2GP NOASSERTION; L0p4Map GPL patterns-only; claude-red skip (skills present + size); bb Watch skip; KiroCrew size-skip (~395MB shallow)"
