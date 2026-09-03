#!/usr/bin/env bash
# K222 Phase-0 — SpikeHTR only (Apache-2.0; <<500MB)
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
ADOPT="$ROOT/.local/adopts"
mkdir -p "$ADOPT"
if [[ -d "$ADOPT/SpikeHTR/.git" ]]; then
  echo "exists SpikeHTR ($(du -sh "$ADOPT/SpikeHTR" | awk '{print $1}'))"
else
  git clone --depth 1 https://github.com/QomolangmaH/SpikeHTR.git "$ADOPT/SpikeHTR"
fi
du -sh "$ADOPT/SpikeHTR"
echo "K222: no SkillEval HF download; no agent-failure code clone"
