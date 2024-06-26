#!/usr/bin/python3
"""returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """
    Returns number of subscribers for a given subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'MyRedditBot/v1.0'}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")
