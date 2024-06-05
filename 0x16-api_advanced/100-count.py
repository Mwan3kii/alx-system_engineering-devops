#!/usr/bin/python3
"""count words subredit"""
import requests


def count_words(subreddit, word_list, after=None, word_count={}):
    """
    Recursively queries the Reddit API, parses the titles of all hot articles,
    and prints a sorted count of given keywords.
    """
    if not word_list:
        return

    if after is None:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    else:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json?after={after}"

    headers = {'User-Agent': 'MyRedditScript/0.1'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']

        for post in posts:
            title = post['data']['title'].lower()
            words = title.split()
            for word in words:
                clean_word = ''.join(char for char in word if char.isalpha())
                if clean_word.lower() in word_list:
                    word_count[clean_word.lower()] = word_count.get(clean_word.lower(), 0) + 1

        new_after = data['data']['after']
        if new_after is not None:
            count_words(subreddit, word_list, new_after, word_count)
        else:
            sorted_word_count = sorted(word_count.items(), key=lambda item: (-item[1], item[0]))
            for word, count in sorted_word_count:
                print(f"{word}: {count}")
