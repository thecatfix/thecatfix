#!/bin/bash
set -e

# Configure git for commits
git config --global user.name "github-actions[bot]"
git config --global user.email "41898282+github-actions[bot]@users.noreply.github.com"

# Setup GitHub CLI for authenticated commits
gh auth setup-git

# Import GPG key for commit signing
echo "$GPG_PRIVATE_KEY" | gpg --import --batch

# Configure GPG signing
git config --global commit.gpgsign true
git config --global user.signingkey E8BF5233471A35B6

# Create a new branch for the PR
BRANCH_NAME="update-starred-repos-$(date +%Y%m%d-%H%M%S)"

# Commit changes to new branch
git checkout -b "$BRANCH_NAME"
git add README.md
git commit --signoff -m "🤖 Update README.md with latest starred repos"

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
