#!/usr/bin/python3
"""Defines recursively subredit"""
import requests


def recurse(subreddit, hot_list=None, after=None):
    """returns list containing titles of articles for subreddit"""
    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'MyRedditScript/0.1'}
    params = {'limit': 100, 'after': after}

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        hot_list.extend(post['data']['title'] for post in posts)
        new_after = data['data']['after']
        if new_after is not None:
            return recurse(subreddit, hot_list, new_after)
        else:
            return hot_list
    else:
        return None

