#!/usr/bin/env bash
# Federation wiki merge — cutover and decommission (migration plan 5.7).
#
#   local    turn ~/Projects/OSINT WORKSPACE into the merged repo, in place
#   archive  mark the 7 absorbed repos ARCHIVED with a pointer to the merged repo
#   verify   report the state
#
# The merged repo already exists at $MERGED and is pushed. `local` swaps the git
# directory and the wiki tree, and preserves every gitignored local path (.local/,
# the inbox, hot.md, .claude/ settings) because those are untracked.
#
# The old .git is kept as .git.premerge-local, and the pre-merge wiki tree as
# .wiki.premerge-local, until `verify` passes.
#
# Usage: bash scripts/merge_cutover.sh <local|archive|verify>

set -uo pipefail

PROJ="$HOME/Projects"
WORKSPACE="$PROJ/OSINT WORKSPACE"
MERGED="${MERGED:-$HOME/.cemini/wiki-merge-build/target}"
REMOTE="https://github.com/cemini23/llm-wiki-by-cemini.git"

SIBLINGS=("Cemini claude code CCC" "Cybersecurity wiki" "SEO:GEO B&M Business"
          "Image gen" "Gambling wiki" "Game Dev wiki" "3d printing")
DOMAINS="3d-printing ccc cybersec seo image-gen gambling game-dev osint"

die() { echo "ERROR: $*" >&2; exit 1; }

cmd_local() {
  [ -d "$MERGED/.git" ] || die "merged repo missing at $MERGED"
  [ -d "$WORKSPACE/.git" ] || die "workspace git missing at $WORKSPACE"
  [ -d "$WORKSPACE/wiki" ] || die "workspace wiki missing"

  echo "1. stash the pre-merge git and wiki aside"
  [ -e "$WORKSPACE/.git.premerge-local" ] && rm -rf "$WORKSPACE/.git.premerge-local"
  mv "$WORKSPACE/.git" "$WORKSPACE/.git.premerge-local"
  [ -e "$WORKSPACE/wiki.premerge-local" ] && rm -rf "$WORKSPACE/wiki.premerge-local"
  mv "$WORKSPACE/wiki" "$WORKSPACE/wiki.premerge-local"

  echo "2. install the merged git"
  cp -R "$MERGED/.git" "$WORKSPACE/.git"

  echo "3. restore the merged working tree (untracked local paths are untouched)"
  git -C "$WORKSPACE" checkout -f HEAD >/dev/null 2>&1 || die "checkout failed"

  echo "4. point origin at the merged remote"
  git -C "$WORKSPACE" remote set-url origin "$REMOTE" 2>/dev/null \
    || git -C "$WORKSPACE" remote add origin "$REMOTE"
  git -C "$WORKSPACE" fetch -q origin

  echo "5. remove the pre-merge wiki tree (kept at .git.premerge-local + the backup tar)"
  rm -rf "$WORKSPACE/wiki.premerge-local"

  echo "done"
}

cmd_archive() {
  for repo in "${SIBLINGS[@]}"; do
    d="$PROJ/$repo"
    [ -d "$d/.git" ] || { echo "skip $repo (no git)"; continue; }
    cat > "$d/ARCHIVED.md" <<'EOF'
# ARCHIVED — absorbed into the merged federation wiki

This repository's `wiki/` tree now lives in the merged repo at
**https://github.com/cemini23/llm-wiki-by-cemini** under `wiki/<domain>/`.

**Do not delete this repository.** It is the rollback: the merged repo's history was
rewritten (`git filter-repo`), so the pre-merge commit SHAs exist only here and in the
local backup tars.

Do not delete it either until its inbox in `research to be indexed/` is empty — that
inbox is gitignored and this repository is its only home.

See `briefs/2026-10-14_federation-wiki-merge-plan.md` §5.7 for the migration plan.
EOF
    git -C "$d" add ARCHIVED.md
    if git -C "$d" commit -q -m "ARCHIVED: absorbed into the merged federation wiki" \
        -m "The wiki/ tree now lives at wiki/<domain>/ in llm-wiki-by-cemini. Keep this repo: it is the rollback, and it still holds this domain's un-ingested inbox."; then
      echo "archived $repo"
    else
      echo "MARKED  $repo (commit blocked; ARCHIVED.md written)"
    fi
  done
}

cmd_verify() {
  echo "=== merged workspace ==="
  echo "  path:    $WORKSPACE"
  echo "  domains: $(ls -d "$WORKSPACE"/wiki/*/ 2>/dev/null | wc -l | tr -d ' ')"
  echo "  wiki md: $(find "$WORKSPACE/wiki" -name '*.md' 2>/dev/null | wc -l | tr -d ' ')"
  echo "  commit:  $(git -C "$WORKSPACE" log --oneline -1 2>/dev/null)"
  echo "  origin:  $(git -C "$WORKSPACE" remote get-url origin 2>/dev/null)"
  printf "  status:  "
  n=$(git -C "$WORKSPACE" status --porcelain 2>/dev/null | wc -l | tr -d ' ')
  [ "$n" -eq 0 ] && echo "clean" || echo "$n change(s)"
  echo
  echo "=== domain directories ==="
  for dom in $DOMAINS; do
    printf "  %-12s " "$dom"
    [ -d "$WORKSPACE/wiki/$dom" ] && echo "$(find "$WORKSPACE/wiki/$dom" -name '*.md' | wc -l | tr -d ' ') md" || echo "MISSING"
  done
  echo
  echo "=== local-only paths preserved ==="
  for p in ".local" "hot.md" "research to be indexed" ".claude"; do
    printf "  %-24s " "$p"
    [ -e "$WORKSPACE/$p" ] && echo present || echo "absent"
  done
  echo
  echo "=== rollback ==="
  echo "  old git:   $([ -d "$WORKSPACE/.git.premerge-local" ] && echo "$WORKSPACE/.git.premerge-local" || echo "(removed after a clean cutover)")"
  echo "  backup:    $(cat "$WORKSPACE/.local/.merge-backup-path" 2>/dev/null || echo '(see ~/.cemini/wiki-merge-backup-*)')"
}

case "${1:-verify}" in
  local)   cmd_local ;;
  archive) cmd_archive ;;
  verify)  cmd_verify ;;
  *) die "unknown command: $1" ;;
esac
