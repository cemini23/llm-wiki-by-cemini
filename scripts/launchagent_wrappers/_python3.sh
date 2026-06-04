# shellcheck shell=bash
# Shared by LaunchAgent wrappers — resolve python3 without Desktop-only pyenv shims.
cemini_launchagent_python3() {
  local candidates=(
    "${HOME}/.pyenv/shims/python3"
    "/opt/homebrew/bin/python3"
    "/usr/local/bin/python3"
    "/Library/Developer/CommandLineTools/usr/bin/python3"
    "/usr/bin/python3"
  )
  local p
  for p in "${candidates[@]}"; do
    if [[ -x "$p" ]]; then
      echo "$p"
      return 0
    fi
  done
  command -v python3
}
