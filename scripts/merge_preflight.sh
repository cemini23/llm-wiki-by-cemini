#!/usr/bin/env bash
# Federation wiki merge — pre-flight (migration plan 5.1).
#
# Phase order matters. Each phase is idempotent and safe to re-run.
#
#   clean    commit in-progress work in all 8 repos (5.1.1)
#   backup   tar each repo's .git + working tree (5.1.2)  <- the only rollback
#   freeze   boot out the fetchers that write into wiki/ (5.1.3)
#   thaw     reverse of freeze
#
# Usage: bash scripts/merge_preflight.sh <clean|backup|freeze|thaw|status>

set -uo pipefail

PROJ="$HOME/Projects"
STAMP="$(date +%Y%m%d-%H%M%S)"
BACKUP="${CEMINI_MERGE_BACKUP:-$HOME/.cemini/wiki-merge-backup-$STAMP}"

# repo directory name -> federation domain id
WIKIS=(
  "OSINT WORKSPACE|osint"
  "Cemini claude code CCC|ccc"
  "Cybersecurity wiki|cybersec"
  "SEO:GEO B&M Business|seo"
  "Image gen|image-gen"
  "Gambling wiki|gambling"
  "Game Dev wiki|game-dev"
  "3d printing|3d-printing"
)

# LaunchAgents that fetch or generate content into a wiki tree (5.1.3).
FETCHERS=(
  com.cemini.daily-research-digest.plist
  com.cemini.daily-research-digest.3d-printing.plist
  com.cemini.daily-research-digest.ccc.plist
  com.cemini.daily-research-digest.cybersec.plist
  com.cemini.daily-research-digest.gambling.plist
  com.cemini.daily-research-digest.game-dev.plist
  com.cemini.daily-research-digest.image-gen.plist
  com.cemini.daily-research-digest.seo.plist
  com.cemini.wiki-gap-detect.plist
  com.cemini.federation-morning-summary.plist
  com.cemini.substack-rss-poller.plist
  com.cemini.inbox-notify.plist
)

die() { echo "ERROR: $*" >&2; exit 1; }

cmd_status() {
  echo "=== repo state ==="
  for entry in "${WIKIS[@]}"; do
    repo="${entry%%|*}"
    printf '%-28s ' "$repo"
    if [ -d "$PROJ/$repo/.git" ]; then
      n=$(git -C "$PROJ/$repo" status --porcelain | wc -l | tr -d ' ')
      ab=$(git -C "$PROJ/$repo" status -sb | head -1 | grep -o '\[.*\]' || true)
      echo "dirty=$n $ab"
    else
      echo "NO .git"
    fi
  done
  echo
  echo "=== fetchers loaded? ==="
  for f in "${FETCHERS[@]}"; do
    printf '%-52s ' "$f"
    if launchctl print "gui/$(id -u)/${f%.plist}" >/dev/null 2>&1; then echo "LOADED"; else echo "not loaded"; fi
  done
  echo
  echo "backup dir would be: $BACKUP"
}

cmd_clean() {
  local osint="$PROJ/OSINT WORKSPACE"

  # .wrangler/ is a Cloudflare tool cache, not content. Never commit it.
  if ! grep -qxF '.wrangler/' "$osint/.gitignore" 2>/dev/null; then
    printf '\n# Cloudflare wrangler local cache\n.wrangler/\n' >> "$osint/.gitignore"
    echo "osint: added .wrangler/ to .gitignore"
  fi

  for entry in "${WIKIS[@]}"; do
    repo="${entry%%|*}"; dom="${entry##*|}"
    [ -d "$PROJ/$repo/.git" ] || { echo "SKIP $repo (no .git)"; continue; }
    n=$(git -C "$PROJ/$repo" status --porcelain | wc -l | tr -d ' ')
    if [ "$n" -eq 0 ]; then echo "ok   $repo already clean"; continue; fi
    git -C "$PROJ/$repo" add -A
    if git -C "$PROJ/$repo" diff --cached --quiet; then
      echo "ok   $repo nothing staged after add"; continue
    fi
    git -C "$PROJ/$repo" commit -q -m "pre-merge: commit in-progress work before the federation merge

Records generated daily sweeps, local hook scripts and research artifacts so the
merge starts from a clean tree (migration plan 5.1.1)." \
      -m "Co-Authored-By: Claude Haiku 4.5 <noreply@anthropic.com>" \
      && echo "commit $repo ($n files)"
  done
}

cmd_backup() {
  mkdir -p "$BACKUP" || die "cannot create $BACKUP"
  for entry in "${WIKIS[@]}"; do
    repo="${entry%%|*}"; dom="${entry##*|}"
    [ -d "$PROJ/$repo/.git" ] || { echo "SKIP $repo"; continue; }
    out="$BACKUP/$dom.tar.gz"
    # .git first in the archive, then the working tree. This is the only rollback.
    tar -czf "$out" \
      --exclude='node_modules' --exclude='__pycache__' \
      -C "$PROJ/$repo" .git . 2>/dev/null \
      && printf '%-12s %s\n' "$dom" "$(du -h "$out" | cut -f1)"
  done
  echo
  echo "backup written to $BACKUP"
  echo "$BACKUP" > "$PROJ/OSINT WORKSPACE/.local/.merge-backup-path"
}

cmd_freeze() {
  for f in "${FETCHERS[@]}"; do
    label="${f%.plist}"
    if launchctl print "gui/$(id -u)/$label" >/dev/null 2>&1; then
      launchctl bootout "gui/$(id -u)/$label" 2>/dev/null && echo "froze  $label" || echo "FAIL   $label"
    else
      echo "skip   $label (not loaded)"
    fi
  done
}

cmd_thaw() {
  for f in "${FETCHERS[@]}"; do
    src="$HOME/Library/LaunchAgents/$f"
    label="${f%.plist}"
    [ -f "$src" ] || { echo "skip   $f (no plist)"; continue; }
    launchctl bootstrap "gui/$(id -u)" "$src" 2>/dev/null && echo "thawed $label" || echo "FAIL   $label"
  done
}

case "${1:-status}" in
  status) cmd_status ;;
  clean)  cmd_clean ;;
  backup) cmd_backup ;;
  freeze) cmd_freeze ;;
  thaw)   cmd_thaw ;;
  *) die "unknown phase: $1" ;;
esac
