#!/usr/bin/env bash
# sync_federation_digest_bundle.sh — push canonical digest + Agent Reach bundle to federation wikis.
#
# Updates:
#   - Each wiki's scripts/ (reference copy; LaunchAgents use ~/.cemini/launchagent/osint/)
#   - ~/.cemini/launchagent/osint/ payload (what federated morning jobs actually run)
#   - config/agent_reach_daily_sources.example.json per wiki (if missing or --force-config)
#   - arxiv_fallback block in daily_research_config.yaml (if missing)
#
# Usage:
#   bash scripts/federation/daily_digest/sync_federation_digest_bundle.sh
#   bash scripts/federation/daily_digest/sync_federation_digest_bundle.sh --force-config

set -euo pipefail

OSINT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"
FORCE_CONFIG=0
[[ "${1:-}" == "--force-config" ]] && FORCE_CONFIG=1

PROJECTS="${CEMINI_PROJECTS_ROOT:-$HOME/Projects}"
PATHS_DIR="$HOME/.cemini/wiki-paths"
PAYLOAD_DIR="$HOME/.cemini/launchagent/osint"

resolve_3d_printing_repo() {
  local candidate
  for candidate in "${PROJECTS}/3D printing" "${PROJECTS}/3d printing"; do
    if [[ -d "$candidate" ]]; then
      printf '%s\n' "$candidate"
      return 0
    fi
  done
  printf '%s\n' "${PROJECTS}/3D printing"
}

WIKI_REPOS=(
  "$OSINT_ROOT"
  "${PROJECTS}/SEO:GEO B&M Business"
  "${PROJECTS}/Cemini claude code CCC"
  "${PROJECTS}/Cybersecurity wiki"
  "${PROJECTS}/Gambling wiki"
  "${PROJECTS}/Game Dev wiki"
  "${PROJECTS}/Image gen"
  "$(resolve_3d_printing_repo)"
)

PY_BUNDLE=(
  daily_research_digest_run.py
  daily_research_fetch.py
  arxiv_api_search.py
  wiki_source_index.py
  agent_reach_daily_social.py
)

sync_scripts_to_repo() {
  local dest_root="$1"
  local scripts_dir="${dest_root}/scripts"
  mkdir -p "$scripts_dir"
  for f in "${PY_BUNDLE[@]}"; do
    local src="${OSINT_ROOT}/scripts/${f}"
    local dst="${scripts_dir}/${f}"
    [[ "$src" -ef "$dst" ]] && continue
    cp -f "$src" "$dst"
  done
  rm -rf "${scripts_dir}/agent_reach_wrapper"
  cp -R "${OSINT_ROOT}/scripts/agent_reach_wrapper" "${scripts_dir}/agent_reach_wrapper"
  find "${scripts_dir}/agent_reach_wrapper" -name '__pycache__' -type d -prune -exec rm -rf {} + 2>/dev/null || true
  chmod 644 "${scripts_dir}"/*.py
  chmod 644 "${scripts_dir}/agent_reach_wrapper"/*.py 2>/dev/null || true
}

sync_scripts_to_payload() {
  mkdir -p "$PAYLOAD_DIR"
  for f in "${PY_BUNDLE[@]}"; do
    cp -f "${OSINT_ROOT}/scripts/${f}" "${PAYLOAD_DIR}/${f}"
  done
  rm -rf "${PAYLOAD_DIR}/agent_reach_wrapper"
  cp -R "${OSINT_ROOT}/scripts/agent_reach_wrapper" "${PAYLOAD_DIR}/agent_reach_wrapper"
  find "${PAYLOAD_DIR}/agent_reach_wrapper" -name '__pycache__' -type d -prune -exec rm -rf {} + 2>/dev/null || true
  chmod 644 "${PAYLOAD_DIR}"/*.py "${PAYLOAD_DIR}/agent_reach_wrapper"/*.py 2>/dev/null || true
}

sync_allowlist_config() {
  local dest_root="$1"
  local cfg_dir="${dest_root}/config"
  local dest="${cfg_dir}/agent_reach_daily_sources.example.json"
  mkdir -p "$cfg_dir"
  if [[ "$FORCE_CONFIG" -eq 1 || ! -f "$dest" ]]; then
    local src="${OSINT_ROOT}/config/agent_reach_daily_sources.example.json"
    [[ "$src" -ef "$dest" ]] || cp -f "$src" "$dest"
  fi
}

patch_arxiv_fallback() {
  local cfg="${1}/scripts/daily_research_config.yaml"
  [[ -f "$cfg" ]] || return 0
  python3 - "$cfg" <<'PY'
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    raise SystemExit("PyYAML required")

path = Path(sys.argv[1])
data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
if data.get("arxiv_fallback"):
    print(f"  arxiv_fallback present — skip {path}")
    raise SystemExit(0)

fallback = {
    "enabled": True,
    "request_interval_seconds": 3,
    "max_terms_per_query": 6,
}
# Insert after fetch block for readability
ordered: dict = {}
for key, value in data.items():
    ordered[key] = value
    if key == "fetch":
        ordered["arxiv_fallback"] = fallback
if "arxiv_fallback" not in ordered:
    ordered["arxiv_fallback"] = fallback

path.write_text(
    yaml.safe_dump(ordered, sort_keys=False, allow_unicode=True),
    encoding="utf-8",
)
print(f"  patched arxiv_fallback → {path}")
PY
}

echo "=== Sync federation digest bundle (canonical: $OSINT_ROOT) ==="

sync_scripts_to_payload
echo "  payload → $PAYLOAD_DIR"

for repo in "${WIKI_REPOS[@]}"; do
  if [[ ! -d "$repo" ]]; then
    echo "WARN: skip missing repo $repo" >&2
    continue
  fi
  echo "--- $(basename "$repo") ($repo)"
  if [[ "$(cd "$repo" && pwd -P)" != "$(cd "$OSINT_ROOT" && pwd -P)" ]]; then
    sync_scripts_to_repo "$repo"
  else
    echo "  canonical OSINT — skip self script copy"
  fi
  sync_allowlist_config "$repo"
  patch_arxiv_fallback "$repo"
done

echo "Done. Reload LaunchAgents if wrappers changed:"
echo "  bash \"$OSINT_ROOT/scripts/reinstall_morning_launchagents.sh\""
