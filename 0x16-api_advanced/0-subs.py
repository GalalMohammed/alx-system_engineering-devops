#!/usr/bin/python3
"""define number_of_subscribers function.

Example:
    number_of_subscribers = __import__('0-subs').number_of_subscribers

"""

import requests


def number_of_subscribers(subreddit: str) -> int:
    """Query the Reddit API and returns the number of subscribers.

    Args:
        subreddit (str): given subreddit.

    Returns:
        int.

    """
    # Send a GET request to the Reddit API
    response = requests.get(f"https://www.reddit.com/r/{subreddit}/about.json",
                            timeout=1, headers={"User-Agent": 'Galal'})
    return response.json().get("data").get("subscribers", 0)
