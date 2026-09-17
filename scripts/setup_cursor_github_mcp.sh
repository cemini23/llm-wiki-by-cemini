#!/usr/bin/env bash
# Wire GitHub MCP into ~/.cursor/mcp.json without embedding a token.
# GUI Cursor does not inherit ~/.zshrc, so Bearer ${env:GITHUB_TOKEN} was empty
# ("Authorization header is badly formatted").
#
# Installs official github-mcp-server (stdio) + wrapper that reads:
#   GITHUB_PERSONAL_ACCESS_TOKEN / GITHUB_TOKEN → ~/.cemini/github-pat → gh auth token
#
# Usage:
#   bash scripts/setup_cursor_github_mcp.sh
#   bash scripts/setup_cursor_github_mcp.sh --write-pat-file   # snapshot gh token to ~/.cemini/github-pat
#   bash scripts/setup_cursor_github_mcp.sh --skip-download    # reuse existing binary
#
# Never prints the token. Never writes gho_/ghp_ literals into mcp.json.
set -euo pipefail

PAT_FILE="${HOME}/.cemini/github-pat"
MCP_FILE="${HOME}/.cursor/mcp.json"
WRAPPER_DST="${HOME}/.local/bin/mcp-github"
BIN_DST="${HOME}/.local/bin/github-mcp-server"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WRAPPER_SRC="${SCRIPT_DIR}/mcp_github.sh"
GH_MCP_VERSION="${GITHUB_MCP_VERSION:-1.9.0}"
WRITE_PAT_FILE=0
SKIP_DOWNLOAD=0

for arg in "$@"; do
  case "$arg" in
    --write-pat-file) WRITE_PAT_FILE=1 ;;
    --skip-download) SKIP_DOWNLOAD=1 ;;
    -h|--help)
      sed -n '2,16p' "$0"
      exit 0
      ;;
    *)
      echo "Unknown arg: $arg" >&2
      exit 1
      ;;
  esac
done

mkdir -p "${HOME}/.cemini" "${HOME}/.local/bin" "${HOME}/.cursor"
chmod 700 "${HOME}/.cemini"

if [[ "${WRITE_PAT_FILE}" -eq 1 ]] || [[ ! -r "${PAT_FILE}" ]]; then
  if ! command -v gh >/dev/null 2>&1; then
    echo "setup_cursor_github_mcp: gh CLI required to write ${PAT_FILE}" >&2
    exit 1
  fi
  gh auth token > "${PAT_FILE}"
  chmod 600 "${PAT_FILE}"
  echo "Wrote ${PAT_FILE} from gh keychain (chmod 600, not printed)"
fi

if [[ "${SKIP_DOWNLOAD}" -eq 0 ]] || [[ ! -x "${BIN_DST}" ]]; then
  if ! command -v gh >/dev/null 2>&1; then
    echo "setup_cursor_github_mcp: gh CLI required to download github-mcp-server" >&2
    exit 1
  fi
  arch="$(uname -m)"
  case "${arch}" in
    arm64|aarch64) asset="github-mcp-server_Darwin_arm64.tar.gz" ;;
    x86_64) asset="github-mcp-server_Darwin_x86_64.tar.gz" ;;
    *)
      echo "setup_cursor_github_mcp: unsupported arch ${arch}" >&2
      exit 1
      ;;
  esac
  sums="github-mcp-server_${GH_MCP_VERSION}_checksums.txt"
  tmp="$(mktemp -d)"
  trap 'rm -rf "${tmp}"' EXIT
  echo "Downloading github-mcp-server v${GH_MCP_VERSION} (${asset})"
  gh release download "v${GH_MCP_VERSION}" \
    -R github/github-mcp-server \
    -p "${asset}" \
    -p "${sums}" \
    -D "${tmp}"
  (
    cd "${tmp}"
    expected="$(awk -v f="${asset}" '$2==f {print $1}' "${sums}")"
    actual="$(shasum -a 256 "${asset}" | awk '{print $1}')"
    if [[ -z "${expected}" || "${expected}" != "${actual}" ]]; then
      echo "setup_cursor_github_mcp: checksum mismatch for ${asset}" >&2
      echo "  expected=${expected:-MISSING}" >&2
      echo "  actual=${actual}" >&2
      exit 1
    fi
    tar -xzf "${asset}"
    src="$(find . -type f -name github-mcp-server | head -1)"
    if [[ -z "${src}" ]]; then
      echo "setup_cursor_github_mcp: github-mcp-server binary not in tarball" >&2
      exit 1
    fi
    install -m 755 "${src}" "${BIN_DST}"
  )
  echo "Installed ${BIN_DST} (v${GH_MCP_VERSION}, checksum OK)"
fi

if [[ ! -f "${WRAPPER_SRC}" ]]; then
  echo "setup_cursor_github_mcp: missing ${WRAPPER_SRC}" >&2
  exit 1
fi
install -m 755 "${WRAPPER_SRC}" "${WRAPPER_DST}"
echo "Installed ${WRAPPER_DST}"

export MCP_FILE WRAPPER_DST
python3 << 'PY'
import json
import os
from pathlib import Path

mcp_path = Path(os.environ["MCP_FILE"])
wrapper = os.environ["WRAPPER_DST"]
data = {"mcpServers": {}}
if mcp_path.exists():
    data = json.loads(mcp_path.read_text())

servers = data.setdefault("mcpServers", {})
servers["github"] = {
    "type": "stdio",
    "command": wrapper,
    "args": [],
    "env": {},
    "disabled": False,
}
text = json.dumps(data, indent=2) + "\n"
for needle in ("gho_", "ghp_", "github_pat_"):
    if needle in text:
        raise SystemExit(f"refusing to write mcp.json: {needle} literal detected")
mcp_path.write_text(text)
print(f"Updated {mcp_path} — github uses wrapper (no embedded token)")
PY

cat <<EOF

GitHub MCP is wired for GUI Cursor (no shell env required).
  binary:  ${BIN_DST} (v${GH_MCP_VERSION})
  wrapper: ${WRAPPER_DST}
  token:   gh auth token → ${PAT_FILE} fallback

Reload: Settings → MCP → github → Retry
EOF
