import requests
import sys
import os


def fetch_starred_repos(username, token, max_repos=10):
    """Fetch starred repos using REST API."""
    starred = []
    page = 1
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github+json",
    }

    while len(starred) < max_repos:
        url = (
            f"https://api.github.com/users/{username}/starred?page={page}&per_page=100"
        )
        resp = requests.get(url, headers=headers)
        if resp.status_code != 200:
            print(f"Failed to fetch starred repos: {resp.status_code} {resp.text}")
            sys.exit(1)
        page_starred = resp.json()
        if not page_starred:
            break
        starred.extend(page_starred)
        page += 1
    return starred[:max_repos]


def fetch_starred_repos_graphql(username, token, max_repos=10):
    """Fetch starred repos using GraphQL API."""
    url = "https://api.github.com/graphql"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }

    query = """
    query($login: String!, $first: Int!) {
      user(login: $login) {
        starredRepositories(first: $first, orderBy: {field: STARRED_AT, direction: DESC}) {
          edges {
            starredAt
            node {
              name
              owner {
                login
              }
              description
              url
              repositoryTopics(first: 5) {
                edges {
                  node {
                    topic {
                      name
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
    """

    variables = {"login": username, "first": max_repos}

    resp = requests.post(
        url, json={"query": query, "variables": variables}, headers=headers
    )

    if resp.status_code != 200:
        print(f"GraphQL query failed: {resp.status_code} {resp.text}")
        return []

    data = resp.json()

    starred = []
    if "data" in data and data["data"]["user"]["starredRepositories"]["edges"]:
        for edge in data["data"]["user"]["starredRepositories"]["edges"]:
            repo = edge["node"]
            starred.append(
                {
                    "name": repo["name"],
                    "full_name": f"{repo['owner']['login']}/{repo['name']}",
                    "description": repo["description"] or "",
                    "html_url": repo["url"],
                    "starred_at": edge["starredAt"],
                    "topics": [
                        topic_edge["node"]["topic"]["name"]
                        for topic_edge in repo["repositoryTopics"]["edges"]
                    ],
                }
            )

    return starred


def generate_markdown(starred, username):
    """Generate basic markdown from starred repos."""
    markdown = f"\n\n## ⭐ {username}'s Latest Starred Repositories\n\n"
    for repo in starred:
        desc = repo["description"] or ""
        markdown += f"- [{repo['full_name']}]({repo['html_url']}): {desc}\n"
    return markdown


def generate_enhanced_markdown(starred, username):
    """Generate enhanced markdown with topics and star dates."""
    markdown = f"\n\n## ⭐ {username}'s Latest Starred Repositories\n\n"
    markdown += "| Repository | Description | Topics | Starred |\n"
    markdown += "|------------|-------------|--------|---------|\n"

    for repo in starred:
        name = repo["full_name"]
        desc = (
            (repo["description"][:60] + "...")
            if len(repo["description"]) > 60
            else repo["description"]
        )
        topics = ", ".join(
            repo.get("topics", [])[:3]
        )  # Handle missing topics gracefully
        starred_date = repo.get("starred_at", "")[:10]  # Handle missing date

        markdown += (
            f"| [{name}]({repo['html_url']}) | {desc} | {topics} | {starred_date} |\n"
        )

    return markdown


def update_readme_with_starred_repos(output_file, new_md, username):
    """Update README.md by replacing existing starred repos section or appending if not found."""
    try:
        # Read existing README.md
        with open(output_file, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        # If file doesn't exist, just write the new content
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(new_md)
        return

    # Find the line with the starred repos header
    header_pattern = f"## ⭐ {username}'s Latest Starred Repositories"
    header_index = None

    for i, line in enumerate(lines):
        if header_pattern in line:
            header_index = i
            break

    if header_index is not None:
        # Remove from header line to end of file and append new content
        updated_lines = lines[:header_index]
        updated_lines.append(new_md.strip() + "\n")
    else:
        # No existing section found, append to end
        updated_lines = lines
        if updated_lines and not updated_lines[-1].endswith("\n"):
            updated_lines[-1] += "\n"
        updated_lines.append(new_md.strip() + "\n")

    # Write back to file
    with open(output_file, "w", encoding="utf-8") as f:
        f.writelines(updated_lines)


def main():
    import argparse

    parser = argparse.ArgumentParser(
        description="Append GitHub starred repos list to README.md"
    )
    parser.add_argument("--token", required=True, help="GitHub Personal Access Token")
    parser.add_argument("--user", required=True, help="GitHub username")
    parser.add_argument("--output", default="README.md", help="Output Markdown file")
    parser.add_argument("--max", type=int, default=10, help="Max number of repos")
    parser.add_argument(
        "--graphql", action="store_true", help="Use GraphQL API with enhanced features"
    )
    args = parser.parse_args()

    if args.graphql:
        starred = fetch_starred_repos_graphql(args.user, args.token, args.max)
        markdown = generate_enhanced_markdown(starred, args.user)
    else:
        starred = fetch_starred_repos(args.user, args.token, args.max)
        markdown = generate_markdown(starred, args.user)

    # Update README.md by replacing existing starred repos section or appending if not found
    update_readme_with_starred_repos(args.output, markdown, args.user)


if __name__ == "__main__":
    main()
