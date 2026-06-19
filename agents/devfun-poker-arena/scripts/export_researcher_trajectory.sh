#!/usr/bin/env bash
# Post-run trajectory bundle for dev.fun Researcher Round.
#
#   ./scripts/export_researcher_trajectory.sh --selfplay path/to/trajectory.jsonl
#   ./scripts/export_researcher_trajectory.sh --competition-id <compId>
#   ./scripts/export_researcher_trajectory.sh --export-dir reports/exports/...
set -euo pipefail
cd "$(dirname "$0")/.."

SELFPLAY=""
EXPORT_DIR=""
COMP=""
OUT_DIR=""
HERO="${ARENA_HERO_HANDLE:-cemini_wiki_poker}"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --selfplay) SELFPLAY="$2"; shift 2 ;;
    --export-dir) EXPORT_DIR="$2"; shift 2 ;;
    --competition-id) COMP="$2"; shift 2 ;;
    --out-dir) OUT_DIR="$2"; shift 2 ;;
    --hero) HERO="$2"; shift 2 ;;
    *) echo "Unknown arg: $1" >&2; exit 1 ;;
  esac
done

if [[ -z "$OUT_DIR" ]]; then
  TS=$(date -u +%Y%m%dT%H%M%SZ)
  OUT_DIR="reports/researcher-round/${TS}"
fi
mkdir -p "$OUT_DIR"

if [[ -n "$COMP" ]]; then
  ARENA_EXPORT="${OUT_DIR}/arena-export"
  TOP_AGENTS="${CEMINI_EXPORT_TOP_AGENTS:-50}"
  echo "==> Arena export competitionId=${COMP} top-agents=${TOP_AGENTS} (+hero always)"
  uv run python examples/export_competition_hands.py \
    --match "$COMP" \
    --top-agents "$TOP_AGENTS" \
    --replays-top-agents 1 \
    --out-dir "$ARENA_EXPORT"
  EXPORT_DIR="$ARENA_EXPORT"
fi

SUMMARY_ARGS=(--out-dir "$OUT_DIR" --hero "$HERO")
if [[ -n "$SELFPLAY" ]]; then
  dest="${OUT_DIR}/selfplay_trajectory.jsonl"
  if [[ "$SELFPLAY" != "$dest" ]]; then
    cp "$SELFPLAY" "$dest"
    SUMMARY_ARGS+=(--selfplay "$dest")
  else
    SUMMARY_ARGS+=(--selfplay "$SELFPLAY")
  fi
fi
if [[ -n "$EXPORT_DIR" ]]; then
  SUMMARY_ARGS+=(--export-dir "$EXPORT_DIR")
fi

if [[ -z "$SELFPLAY" && -z "$EXPORT_DIR" ]]; then
  echo "ERROR: pass --selfplay, --export-dir, or --competition-id" >&2
  exit 2
fi

echo "==> Axis proxy summary"
uv run python examples/researcher_trajectory_summary.py "${SUMMARY_ARGS[@]}"

echo "Trajectory bundle → ${OUT_DIR}"
