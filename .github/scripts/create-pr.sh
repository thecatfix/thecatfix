#!/bin/bash
set -e

# Configure git for commits
git config --global user.name "github-actions[bot]"
git config --global user.email "github-actions[bot]@users.noreply.github.com"

# Check if there are changes
git add README.md
if git diff --staged --quiet; then
  echo "No changes to README.md, skipping PR creation"
  exit 0
fi

# Create a new branch for the PR
BRANCH_NAME="update-starred-repos-$(date +%Y%m%d-%H%M%S)"

# Commit changes to new branch
git checkout -b "$BRANCH_NAME"
git commit -m "🤖 Update README.md with latest starred repos"

# Push the branch
git push origin "$BRANCH_NAME"

# Create PR using GitHub CLI
gh pr create \
  --title "🤖 Update starred repositories list" \
  --body "## 🤖 Automated Update

This PR updates the README.md with the latest starred repositories from GitHub.

### Changes
- Updated starred repositories list
- Generated automatically every 6 hours

---
*This PR was automatically created by the [stars.yml](.github/workflows/stars.yml) workflow.*" \
  --base main \
  --head "$BRANCH_NAME"
