#!/usr/bin/env bash
# K211 Phase-0 — MIT/Apache Extracts under 500MB
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DEST="$ROOT/.local/adopts"
mkdir -p "$DEST"
clone() {
  local repo="$1" name="$2"
  if [[ -d "$DEST/$name/.git" ]]; then echo "ok $name"; du -sh "$DEST/$name"; return; fi
  git clone --depth 1 "https://github.com/$repo.git" "$DEST/$name"
  du -sh "$DEST/$name"
}
clone matthieugraziani/genealogy_ai genealogy_ai
clone juntoku9/claude_immigration_attorney claude_immigration_attorney
clone openai/codex-security codex-security
clone kvcache-ai/AgentENV agentenv
echo "Total:"; du -sh "$DEST"/genealogy_ai "$DEST"/claude_immigration_attorney "$DEST"/codex-security "$DEST"/agentenv | awk '{s+=$1} END{print}'
echo "DONE — Extract only; no Atto product wire for AGPL/GPL deferred repos"
