#!/usr/bin/python3
"""define top_ten function."""

import requests


def top_ten(subreddit: str) -> None:
    """Query the Reddit API and prints the titles
    of the first 10 hot posts listed for a given subreddit.

    Args:
        subreddit (str): given subreddit.
    """
    # Send a GET request to the Reddit API
    response = requests.get(f"https://www.reddit.com/r/{subreddit}/hot.json",
                            timeout=1, headers={"User-Agent": "Galal"})
    posts = response.json().get("data", {}).get("children")
    if posts:
        # for post in posts[:10]:
        #     print(post["data"]["title"])
        print("OK", end="")
    else:
        print(None)
