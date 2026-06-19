#!/usr/bin/env bash
# Pre-submit recon — read site/rules before first Researcher hand.
#
#   ./scripts/run_researcher_comp_recon.sh
#   ./scripts/run_researcher_comp_recon.sh --competition-id <id> --write-wiki-stub
set -euo pipefail
cd "$(dirname "$0")/.."

ARGS=()
while [[ $# -gt 0 ]]; do
  case "$1" in
    --competition-id) ARGS+=(--competition-id "$2"); shift 2 ;;
    --write-wiki-stub) ARGS+=(--write-wiki-stub); shift ;;
    *) echo "Unknown arg: $1" >&2; exit 2 ;;
  esac
done

if [[ ${#ARGS[@]} -gt 0 ]]; then
  uv run python examples/researcher_comp_recon.py "${ARGS[@]}"
else
  uv run python examples/researcher_comp_recon.py
fi
