#!/usr/bin/python3
"""queries Reddit API and prints titles of first 10 hot posts"""
import requests


def top_ten(subreddit):
    """Prints titles of first 10 hot postsfor a given subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'MyRedditScript/0.2'}
    params = {'limit': 10}

    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            print(post['data']['title'])
    else:
        print(None)
