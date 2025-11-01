import requests
import sys
import os

def fetch_starred_repos(username, token, max_repos=10):
    repos = []
    page = 1
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github+json'
    }

    while len(repos) < max_repos:
        url = f'https://api.github.com/users/{username}/starred?page={page}&per_page=100'
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
        desc = repo['description'] or ''
        md += f"- [{repo['full_name']}]({repo['html_url']}): {desc}\n"
    return md

def main():
    import argparse

    parser = argparse.ArgumentParser(description="Append GitHub starred repos list to README.md")
    parser.add_argument('--token', required=True, help='GitHub Personal Access Token')
    parser.add_argument('--user', required=True, help='GitHub username')
    parser.add_argument('--output', default='README.md', help='Output Markdown file')
    parser.add_argument('--max', type=int, default=10, help='Max number of repos')
    args = parser.parse_args()

    repos = fetch_starred_repos(args.user, args.token, args.max)
    md = generate_markdown(repos, args.user)

    # Append to existing README.md
    with open(args.output, 'a', encoding='utf-8') as f:
        f.write(md)

if __name__ == '__main__':
    main()
