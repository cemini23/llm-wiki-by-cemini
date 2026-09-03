#!/usr/bin/env bash
# K230 follow-up — Qwen-MM-Plugins Phase-0 (core Integrate → Atto)
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
AD="$ROOT/.local/adopts"
mkdir -p "$AD"
cd "$AD"
if [ -d Qwen-MM-Plugins/.git ]; then
  echo HAVE Qwen-MM-Plugins; du -sh Qwen-MM-Plugins; exit 0
fi
git clone --depth 1 https://github.com/QwenLM/Qwen-MM-Plugins.git Qwen-MM-Plugins
du -sh Qwen-MM-Plugins
head -3 Qwen-MM-Plugins/LICENSE
