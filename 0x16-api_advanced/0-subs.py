#!/usr/bin/python3
"""returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """
    Returns number of subscribers for a given subreddit.
    If the subreddit is invalid it returns 0.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'MyRedditScript/0.1'}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")
