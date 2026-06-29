#!/usr/bin/env bash
# Pin the next Researcher HU sandbox auto-submit target (git-tracked intent).
#
# Usage:
#   bash scripts/pin_researcher_sandbox_submit.sh
#   ARENA_RESEARCHER_COMP_ID=<id> AGENT_VERSION=<ver> bash scripts/pin_researcher_sandbox_submit.sh
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
AGENT_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
PIN="${AGENT_DIR}/config/researcher_sandbox_submit.pin.json"
COMP="${ARENA_RESEARCHER_COMP_ID:-cmqqqs05i1u7ppnu7stqbw7d8}"
AGENT_VERSION="${AGENT_VERSION:-}"
GIT_SHA="$(git -C "${AGENT_DIR}" rev-parse --short HEAD 2>/dev/null || echo unknown)"
if [[ "${GIT_SHA}" == "unknown" && -f "${PIN}" ]]; then
  GIT_SHA="$(python3 -c "import json; print(json.load(open('${PIN}')).get('gitCommit','unknown'))")"
fi
TS="$(date -u +%Y-%m-%dT%H:%M:%SZ)"

if [[ -z "${AGENT_VERSION}" && -f "${AGENT_DIR}/.env" ]]; then
  AGENT_VERSION="$(grep -E '^AGENT_VERSION=' "${AGENT_DIR}/.env" | head -1 | cut -d= -f2- || true)"
fi
if [[ -z "${AGENT_VERSION}" ]]; then
  AGENT_VERSION="researcher-jun21.${GIT_SHA}.${TS:0:10}"
fi

mkdir -p "${AGENT_DIR}/config"
cat > "${PIN}" <<EOF
{
  "competitionId": "${COMP}",
  "template": "static-agent",
  "replace": true,
  "build": true,
  "bundlePath": "dist/sandbox-pvp-bundle.zip",
  "agentVersion": "${AGENT_VERSION}",
  "gitCommit": "${GIT_SHA}",
  "pinnedAt": "${TS}",
  "notes": "Pinned by pin_researcher_sandbox_submit.sh — auto-submit timer consumes this file."
}
EOF

echo "Pinned ${PIN}"
echo "  competitionId=${COMP}"
echo "  agentVersion=${AGENT_VERSION}"
echo "  gitCommit=${GIT_SHA}"
