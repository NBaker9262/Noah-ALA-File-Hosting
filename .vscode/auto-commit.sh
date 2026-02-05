#!/usr/bin/env bash
# Auto-commit changes on save (called by Run On Save extension)
# Runs in workspace root. Be careful: this will commit and push changes.

set -euo pipefail
cd "${GITHUB_WORKSPACE:-$PWD}"

# If there are no changes, do nothing
if [ -z "$(git status --porcelain)" ]; then
  exit 0
fi

# Stage everything, commit and push
git add -A
MSG="Auto-save: $(date +'%Y-%m-%d %H:%M:%S')"
# Commit only if there are staged changes
if git diff --cached --quiet; then
  # nothing staged
  exit 0
fi

git commit -m "$MSG" || exit 0
# Push current branch
git push origin HEAD || true
