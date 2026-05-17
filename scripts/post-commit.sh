#!/usr/bin/env bash
# post-commit hook — sync the wiki to cemini-librarian whenever a commit
# touches wiki/.
#
# Why a commit hook instead of cron/launchd: the workspace lives under
# ~/Desktop, which macOS protects with TCC. cron- and launchd-scheduled
# background jobs cannot read ~/Desktop without Full Disk Access, so the
# old `0 * * * *` sync cron silently never ran (the librarian wiki went
# 5 days stale, 2026-05-12 → 2026-05-17). A git hook runs inside the
# interactive session, which already has the necessary file access — so
# the sync fires reliably, and it fires exactly when the wiki changes
# rather than on a fixed hour.
#
# The sync is launched detached (& + disown) so `git commit` returns
# immediately; progress lands in ~/Library/Logs/cemini-wiki-sync.log.

set -uo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null)" || exit 0
[[ -n "$REPO_ROOT" ]] || exit 0

# Only sync when the new commit actually touched the wiki.
if git diff-tree --no-commit-id --name-only -r HEAD 2>/dev/null | grep -q '^wiki/'; then
    bash "$REPO_ROOT/scripts/sync_wiki_to_librarian.sh" \
        >> "$HOME/Library/Logs/cemini-wiki-sync.log" 2>&1 &
    disown 2>/dev/null || true
fi

exit 0
