import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import xml.etree.ElementTree as ET
import sys
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


def fetch_blog_posts(feed_url, max_posts=5):
    """Fetch blog posts from RSS feed with retries and custom headers."""
    session = requests.Session()
    retries = Retry(total=5, backoff_factor=1, status_forcelist=[502, 503, 504])
    session.mount("https://", HTTPAdapter(max_retries=retries))

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept": "application/rss+xml, application/xml;q=0.9, */*;q=0.8",
    }

    try:
        resp = session.get(feed_url, headers=headers, timeout=10)
        resp.raise_for_status()
        root = ET.fromstring(resp.content)

        posts = []
        items = root.findall("./channel/item")

        for i, item in enumerate(items):
            title_elem = item.find("title")
            link_elem = item.find("link")

            if (
                title_elem is not None
                and title_elem.text
                and link_elem is not None
                and link_elem.text
            ):
                title = title_elem.text.strip()
                link = link_elem.text.strip()

                # Highlight the latest post
                if i == 0:
                    posts.append(f"- **Latest: [{title}]({link})** 🚀")
                else:
                    posts.append(f"- [{title}]({link})")

            if len(posts) >= max_posts:
                break
        return posts
    except Exception as e:
        logging.error(f"Failed to fetch blog posts: {e}")
        return []


def update_readme(readme_path, posts):
    """Update README.md with blog posts between markers."""
    if not posts:
        logging.warning("No posts to update.")
        return

    try:
        with open(readme_path, "r", encoding="utf-8") as f:
            content = f.read()

        start_marker = "<!-- BLOG-POST-LIST:START -->"
        end_marker = "<!-- BLOG-POST-LIST:END -->"

        start_idx = content.find(start_marker)
        end_idx = content.find(end_marker)

        if start_idx == -1 or end_idx == -1:
            logging.error(
                f"Markers not found in {readme_path}. Ensure {start_marker} and {end_marker} exist."
            )
            return

        new_posts_content = "\n" + "\n".join(posts) + "\n"
        updated_content = (
            content[: start_idx + len(start_marker)]
            + new_posts_content
            + content[end_idx:]
        )

        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(updated_content)

        logging.info(f"Successfully updated {readme_path} with {len(posts)} posts.")
    except Exception as e:
        logging.error(f"Failed to update README: {e}")


if __name__ == "__main__":
    FEED_URL = "https://www.catfix.biz/blog-feed.xml"
    README_PATH = "README.md"

    blog_posts = fetch_blog_posts(FEED_URL)
    if blog_posts:
        update_readme(README_PATH, blog_posts)
    else:
        sys.exit(1)
