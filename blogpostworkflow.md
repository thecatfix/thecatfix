# Jan 17 2025 Making the action inactive b/c of errors on runs

## This is the workflow for github action
name: Latest soggy blog post
on:
  schedule: # Run workflow automatically
    - cron: '0 * * * *' # Runs every hour, on the hour
  workflow_dispatch: # Run workflow manually (without waiting for the cron to be called), through the GitHub Actions Workflow page directly
permissions:
  contents: write # To write the generated contents to the readme

jobs:
  update-readme-with-blog:
    name: Update this repo's README with latest blog posts
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v3
      - name: Pull in posts from blog
        uses: gautamkrishnar/blog-post-workflow@v1
        with:

          feed_list: "https://www.catfix.biz/blog-feed.xml"
          template: $newline - [$title]($url)  


          
