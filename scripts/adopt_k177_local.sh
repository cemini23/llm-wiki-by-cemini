#!/usr/bin/env bash
# Wire K177 AGM Extract into .local/adopts (<<500MB). No pip install of AGM as default.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
ADOPTS="${ROOT}/.local/adopts"
REPORT="${ROOT}/.local/reports/k177-local-adopt.md"
REPO_URL="https://github.com/agent-governance-manifest/agent-governance-manifest.git"
DEST="${ADOPTS}/agent-governance-manifest"
CAP_MB=500

mkdir -p "$ADOPTS" "$(dirname "$REPORT")"
if [[ ! -d "${DEST}/.git" ]]; then
  git clone --depth 1 --single-branch "$REPO_URL" "$DEST"
fi
mb=$(du -sm "$DEST" | awk '{print $1}')
if (( mb > CAP_MB )); then
  echo "FAIL ${DEST} ${mb}MB > ${CAP_MB}MB" >&2
  rm -rf "$DEST"
  exit 1
fi
{
  echo "# K177 local adopt — $(date +%Y-%m-%d)"
  echo
  echo "- AGM: \`${DEST}\` (${mb}MB) — Extract schemas / \`.agm/\` patterns for CCC"
  echo "- No pip install by default; operator: \`pip install -r requirements.txt && pytest -q\` in adopt dir if dogfooding"
  echo "- OCR NAS / AR bugs / IE controllability: wiki concepts only — no clones"
} >"$REPORT"
echo "OK ${DEST} ${mb}MB"
cat "$REPORT"
