import requests
import xml.etree.ElementTree as ET
import sys


def fetch_blog_posts(feed_url, max_posts=5):
    """Fetch blog posts from RSS feed."""
    try:
        resp = requests.get(feed_url)
        resp.raise_for_status()
        root = ET.fromstring(resp.content)

        posts = []
        for item in root.findall("./channel/item"):
            title_elem = item.find("title")
            link_elem = item.find("link")

            if title_elem is not None and link_elem is not None:
                title = title_elem.text
                link = link_elem.text
                posts.append(f"- [{title}]({link})")

            if len(posts) >= max_posts:
                break
        return posts
    except Exception as e:
        print(f"Failed to fetch blog posts: {e}")
        return []


def update_readme(readme_path, posts):
    """Update README.md with blog posts between markers."""
    if not posts:
        return

    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()

    start_marker = "<!-- BLOG-POST-LIST:START -->"
    end_marker = "<!-- BLOG-POST-LIST:END -->"

    start_idx = content.find(start_marker)
    end_idx = content.find(end_marker)

    if start_idx == -1 or end_idx == -1:
        print("Markers not found in README.md")
        return

    new_posts_content = "\n" + "\n".join(posts) + "\n"
    updated_content = (
        content[: start_idx + len(start_marker)] + new_posts_content + content[end_idx:]
    )

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(updated_content)


if __name__ == "__main__":
    feed_url = "https://www.catfix.biz/blog-feed.xml"
    readme_path = "README.md"
    posts = fetch_blog_posts(feed_url)
    if posts:
        update_readme(readme_path, posts)
        print(f"Successfully updated README.md with {len(posts)} posts.")
    else:
        print("No posts found or failed to fetch.")
