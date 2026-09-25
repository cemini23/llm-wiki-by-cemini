#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
grep -q "1.64/35" wiki/concepts/k272-harness-evolution-wave.md
grep -q "deep-read" ROADMAP.md
grep -q "1.64/35" briefs/2026-09-25_k272-ccc-harness.md
grep -q "Further implementation: none" briefs/2026-09-25_k272-ccc-harness.md
lines=$(wc -l < wiki/log.md)
if [ "$lines" -lt 10000 ]; then
  echo "log truncated: $lines" >&2
  exit 1
fi
grep -q "Harness hub now records the grader MAE" wiki/log.md
echo "K272 follow gate OK"
