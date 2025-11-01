import requests
import sys
import os


def fetch_starred_repos(username, token, max_repos=10):
    repos = []
    page = 1
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github+json",
    }

    while len(repos) < max_repos:
        url = (
            f"https://api.github.com/users/{username}/starred?page={page}&per_page=100"
        )
        resp = requests.get(url, headers=headers)
        if resp.status_code != 200:
            print(f"Failed to fetch starred repos: {resp.status_code} {resp.text}")
            sys.exit(1)
        page_repos = resp.json()
        if not page_repos:
            break
        repos.extend(page_repos)
        page += 1
    return repos[:max_repos]


def generate_markdown(repos, username):
    md = f"\n\n## ⭐ {username}'s Latest Starred Repositories\n\n"
    for repo in repos:
        desc = repo["description"] or ""
        md += f"- [{repo['full_name']}]({repo['html_url']}): {desc}\n"
    return md


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
    args = parser.parse_args()

    repos = fetch_starred_repos(args.user, args.token, args.max)
    md = generate_markdown(repos, args.user)

    # Update README.md by replacing existing starred repos section or appending if not found
    update_readme_with_starred_repos(args.output, md, args.user)


if __name__ == "__main__":
    main()
