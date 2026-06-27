#!/usr/bin/env bash
# Install OSINT leak-guard git hooks in federation repos that ship scripts/install-hooks.sh.
# Canon hook scripts live in OSINT WORKSPACE/scripts/{pre-commit,post-commit,install-hooks}.sh
set -euo pipefail

OSINT_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
CANON_PRE="${OSINT_ROOT}/scripts/pre-commit.sh"
CANON_POST="${OSINT_ROOT}/scripts/post-commit.sh"
CANON_INSTALL="${OSINT_ROOT}/scripts/install-hooks.sh"

WORKSPACES=(
  "${OSINT_ROOT}"
  "/Users/claudiobarone/Desktop/projects/CeminiSuite"
  "/Users/claudiobarone/Projects/CeminiSuite"
  "/Users/claudiobarone/Projects/Cemini claude code CCC"
  "/Users/claudiobarone/Projects/Gambling wiki"
  "/Users/claudiobarone/Projects/Game Dev wiki"
  "/Users/claudiobarone/Projects/Cybersecurity wiki"
  "/Users/claudiobarone/Projects/Image gen"
  "/Users/claudiobarone/Projects/SEO:GEO B&M Business"
  "/Users/claudiobarone/Projects/3D printing"
  "/Users/claudiobarone/Projects/cemini-federation-hub"
  "/Users/claudiobarone/Projects/castle-sim"
  "/Users/claudiobarone/Projects/CeminiDFS"
)

seed_hooks() {
  local dest="$1"
  local scripts_dir="${dest}/scripts"
  mkdir -p "${scripts_dir}"
  cp -f "${CANON_PRE}" "${scripts_dir}/pre-commit.sh"
  cp -f "${CANON_POST}" "${scripts_dir}/post-commit.sh"
  cp -f "${CANON_INSTALL}" "${scripts_dir}/install-hooks.sh"
}

echo "Federation git hooks sync (canon: ${OSINT_ROOT})"
count=0
for ws in "${WORKSPACES[@]}"; do
  if [[ ! -d "${ws}/.git" ]]; then
    echo "  SKIP no git ${ws}"
    continue
  fi
  if [[ ! -f "${ws}/scripts/install-hooks.sh" ]]; then
    seed_hooks "${ws}"
    echo "  SEED hooks scripts → ${ws}"
  fi
  (cd "${ws}" && bash scripts/install-hooks.sh)
  echo "  OK  ${ws}"
  count=$((count + 1))
done
echo "Installed hooks in ${count} repo(s)."
