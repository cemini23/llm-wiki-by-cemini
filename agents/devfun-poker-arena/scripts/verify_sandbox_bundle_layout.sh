#!/usr/bin/env bash
# Verify sandbox PvP bundle matches docs.dev.fun researcher guide layout.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
AGENT_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
BUNDLE="${1:-${AGENT_DIR}/dist/sandbox-pvp-bundle.zip}"

cd "${AGENT_DIR}"
PY="${AGENT_DIR}/venv/bin/python"
if [[ ! -x "${PY}" ]]; then
  PY="python3"
fi

engine="${CEMINI_SANDBOX_ENGINE:-cemini}"
if [[ -z "${CEMINI_SANDBOX_ENGINE:-}" && -f config/researcher_sandbox_submit.pin.json ]]; then
  engine="$("${PY}" -c "import json; print(json.load(open('config/researcher_sandbox_submit.pin.json')).get('sandboxEngine', 'cemini'))")"
fi
export CEMINI_SANDBOX_ENGINE="${engine}"

if command -v uv >/dev/null 2>&1; then
  uv run python examples/submit_sandbox_pvp.py --build-only --bundle "${BUNDLE}"
else
  "${PY}" examples/submit_sandbox_pvp.py --build-only --bundle "${BUNDLE}"
fi

entries="$(unzip -Z1 "${BUNDLE}")"
if [[ "${engine}" == "gin_hu004" ]]; then
  required=(
    harness/strategy.py
    assets/gin_hu004_bridge.py
    assets/_vendor/gin_hu004/hu004.py
  )
else
  required=(
    harness/strategy.py
    assets/cemini_decide.py
  )
fi

missing=0
for path in "${required[@]}"; do
  if ! grep -Fxq "${path}" <<< "${entries}"; then
    echo "MISSING: ${path}" >&2
    missing=1
  fi
done

if [[ "${missing}" -ne 0 ]]; then
  echo "Bundle layout check FAILED: ${BUNDLE}" >&2
  exit 1
fi

echo "OK: ${BUNDLE} ($(unzip -l "${BUNDLE}" | tail -1 | awk '{print $NF}'))"
grep -E '^(harness/|assets/gin_hu004|assets/_vendor/gin_hu004|assets/cemini_decide|skills/)' <<< "${entries}" | head -20
