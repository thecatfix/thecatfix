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

# Use a consistent branch name instead of a timestamped one
BRANCH_NAME="automated-starred-repos-update"

# Create/Reset the branch and commit
git checkout -B "$BRANCH_NAME"
git commit -m "🤖 Update README.md with latest starred repos"

# Force push to the stable branch
git push origin "$BRANCH_NAME" --force

# Check if a PR already exists for this branch
PR_EXISTS=$(gh pr list --head "$BRANCH_NAME" --base main --json number --jq '.[0].number')

if [ -z "$PR_EXISTS" ]; then
  # Create PR using GitHub CLI if it doesn't exist
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
else
  echo "Pull request already exists (#$PR_EXISTS). Branch has been updated."
fi
